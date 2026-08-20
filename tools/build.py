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

ASSET_CSS = """
@page{ size:8.5in 11in; margin:0.85in;
  @bottom-center{ content:counter(page); font-family:"OV Sans"; font-size:8pt; color:#4A5058; } }
html{ font-family:"OV Serif",Georgia,serif; font-size:10.5pt; line-height:15pt; color:#16191E; }
h1{ font-family:"OV Sans"; font-size:22pt; font-weight:700; letter-spacing:-.025em; color:#1F3F68; margin:0 0 4pt; }
h2{ font-family:"OV Sans"; font-size:13pt; font-weight:700; color:#1F3F68; margin:18pt 0 6pt; break-after:avoid; }
h3{ font-family:"OV Sans"; font-size:10.5pt; font-weight:700; text-transform:uppercase; letter-spacing:.05em;
    color:#16304F; margin:14pt 0 4pt; break-after:avoid; }
blockquote{ border-left:3px solid #C0722C; background:#F6EADC; margin:10pt 0; padding:9pt 12pt;
  font-size:9pt; line-height:13pt; color:#8A4E17; }
blockquote p{ margin:0 0 4pt; } blockquote > :last-child{ margin-bottom:0; }
pre{ font-family:"OV Mono"; font-size:8.4pt; line-height:12.6pt; background:#F4F0E8;
  border-left:3px solid #1F3F68; padding:10pt 12pt; white-space:pre-wrap; break-inside:avoid; }
code{ font-family:"OV Mono"; font-size:9pt; }
pre code{ font-size:8.4pt; background:none; }
table{ border-collapse:collapse; width:100%; margin:10pt 0; font-size:8.8pt; line-height:12.5pt; break-inside:avoid; }
thead th{ font-family:"OV Sans"; font-size:7.5pt; font-weight:700; letter-spacing:.08em; text-transform:uppercase;
  color:#fff; background:#1F3F68; text-align:left; padding:5pt 7pt; }
tbody td{ padding:5pt 7pt; border-bottom:.5pt solid #D8D3C9; vertical-align:top; }
tbody tr:nth-child(even){ background:#F4F0E8; }
ul,ol{ padding-left:15pt; } li{ margin-bottom:3pt; }
hr{ border:none; border-top:1px solid #D8D3C9; margin:14pt 0; }
"""

FONT_FACES = """
@font-face { font-family:"OV Serif"; src:url("fonts/SourceSerif4-Regular.ttf") format("truetype"); font-weight:400; }
@font-face { font-family:"OV Serif"; src:url("fonts/SourceSerif4-SemiBold.ttf") format("truetype"); font-weight:600; }
@font-face { font-family:"OV Serif"; src:url("fonts/SourceSerif4-Italic.ttf") format("truetype"); font-weight:400; font-style:italic; }
@font-face { font-family:"OV Sans"; src:url("fonts/Archivo-Regular.ttf") format("truetype"); font-weight:400; }
@font-face { font-family:"OV Sans"; src:url("fonts/Archivo-Bold.ttf") format("truetype"); font-weight:700; }
@font-face { font-family:"OV Mono"; src:url("fonts/JetBrainsMono-Regular.ttf") format("truetype"); font-weight:400; }
"""

def build_assets():
    """Export every asset-vault file as a standalone PDF, and copy the editable originals."""
    import shutil
    src = BUILD/"assets"
    dst = OUT/"assets"
    dst.mkdir(parents=True, exist_ok=True)
    css = CSS(string=FONT_FACES + ASSET_CSS, base_url=str(STYLE))
    n = 0
    for f in sorted(src.glob("*.md")):
        if f.name == "BRAND-ASSETS-NEEDED.md":
            continue
        shutil.copy(f, dst/f.name)                      # editable original
        body = render(f)
        html = SKEL.format(body=body)
        HTML(string=html, base_url=str(STYLE)).write_pdf(dst/(f.stem + ".pdf"), stylesheets=[css])
        n += 1
    for f in sorted(src.glob("*.csv")):
        shutil.copy(f, dst/f.name)                      # spreadsheet-ready
    print(f"   asset vault: {n} PDFs + editable .md/.csv -> output/assets/")

if __name__ == "__main__":
    args = sys.argv[1:]
    retail = "--retail" in args
    if "--preview" in args:
        build(preview=True, retail=retail)
    else:
        build(preview=False, retail=retail)
        build(preview=True, retail=retail)
        build_assets()
