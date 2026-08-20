#!/usr/bin/env python3
"""
The OneVision Playbook — build pipeline.
Markdown (+ inline HTML components) -> single HTML -> PDF via WeasyPrint.

    python3 tools/build.py            # full book + preview
    python3 tools/build.py --preview  # preview only
    python3 tools/build.py --retail   # hide [STORY NEEDED] slots (retail build)
"""
import sys, re, pathlib, datetime
import markdown
from weasyprint import HTML, CSS

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILD, OUT, STYLE = ROOT/"build", ROOT/"output", ROOT/"build"/"style"
OUT.mkdir(exist_ok=True)

MD = markdown.Markdown(extensions=["tables", "attr_list", "md_in_html", "sane_lists", "footnotes"])

def render(path):
    MD.reset()
    return MD.convert(path.read_text(encoding="utf-8"))

def ordered(d):
    return sorted(d.glob("*.md")) if d.exists() else []

def collect(preview=False):
    parts = []
    for f in ordered(BUILD/"front"):
        parts.append(render(f))
    chapters = ordered(BUILD/"chapters")
    if preview:
        # front matter through the end of the first real chapter
        keep = []
        for f in chapters:
            keep.append(f)
            if 'class="chapter"' in f.read_text(encoding="utf-8"):
                break
        chapters = keep
    for f in chapters:
        parts.append(render(f))
    if not preview:
        for f in ordered(BUILD/"back"):
            parts.append(render(f))
    return "\n".join(parts)

def toc_html():
    """Build the TOC from chapter files: reads the h1 and the data-part marker."""
    rows, current = [], None
    for f in ordered(BUILD/"chapters"):
        txt = f.read_text(encoding="utf-8")
        m_id = re.search(r'id="(ch\d+)"', txt)
        m_t  = re.search(r'<h1[^>]*>(.*?)</h1>', txt, re.S)
        m_p  = re.search(r'data-part="([^"]+)"', txt)
        m_n  = re.search(r'class="chap-num">(\d+)<', txt)
        if not (m_id and m_t):
            continue
        if m_p and m_p.group(1) != current:
            current = m_p.group(1)
            rows.append(f'<li class="part-label">{current}</li>')
        title = re.sub(r"<[^>]+>", "", m_t.group(1)).strip()
        num = m_n.group(1) if m_n else ""
        rows.append(f'<li><a href="#{m_id.group(1)}"><span class="num">{num}</span>{title}</a></li>')
    return ('<section class="toc"><h2>Contents</h2><ol>' + "".join(rows) + "</ol></section>")

SKEL = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>The OneVision Playbook</title></head><body>{body}</body></html>"""

def build(preview=False, retail=False):
    front = collect(preview)
    # TOC is injected after the cover + copyright, before the system map
    body = front.replace("<!--TOC-->", toc_html())
    if retail:
        body = re.sub(r'<div class="storyslot">.*?</div>', "", body, flags=re.S)
    html = SKEL.format(body=body)
    dbg = OUT/("debug-preview.html" if preview else "debug-full.html")
    dbg.write_text(html, encoding="utf-8")
    name = "OneVision-Playbook-Preview.pdf" if preview else "OneVision-Playbook.pdf"
    doc = HTML(string=html, base_url=str(STYLE)).render(
        stylesheets=[CSS(filename=str(STYLE/"book.css"))])
    doc.write_pdf(OUT/name)
    size = (OUT/name).stat().st_size/1024/1024
    print(f"   {name}: {len(doc.pages)} pages, {size:.2f} MB")
    return len(doc.pages)

if __name__ == "__main__":
    args = sys.argv[1:]
    retail = "--retail" in args
    if "--preview" in args:
        build(preview=True, retail=retail)
    else:
        build(preview=False, retail=retail)
        build(preview=True, retail=retail)
