# Build Notes

How to rebuild *The OneVision Playbook*, what to edit, and where everything lives.

## Rebuild

```bash
./build.sh                 # full book + preview + asset vault
./build.sh --preview       # preview only (front matter + Chapter 1)
./build.sh --retail        # strips [STORY NEEDED] slots — the sellable build
```

First run on a clean machine:

```bash
pip install weasyprint markdown
```

Fonts are committed under `build/style/fonts/` and embedded at build time. No network needed.

## Outputs

| File | What it is |
|---|---|
| `output/OneVision-Playbook.pdf` | The full designed book, 147 pages |
| `output/OneVision-Playbook-Preview.pdf` | Front matter + Chapter 1, for free lead-gen |
| `output/assets/*.pdf` | Every asset-vault file as a standalone PDF |
| `output/assets/*.md` | The same files, editable |
| `output/assets/*.csv` | Trackers and calculators, spreadsheet-ready with formulas |
| `output/debug-full.html` | The assembled HTML, for diagnosing layout |

## Where to edit

| To change | Edit |
|---|---|
| A chapter | `build/chapters/NNN-slug.md` |
| Cover, copyright, how-to-use, system map | `build/front/` |
| Asset index, 30/60/90, glossary, sources, clearance | `build/back/` |
| An asset-vault file | `build/assets/` |
| Any design — type, colour, page furniture, components | `build/style/book.css` |
| Asset-vault design | `ASSET_CSS` inside `tools/build.py` |

Files are assembled in filename order. Chapters use hundreds (`010`, `020`) with part dividers on the round hundreds (`000`, `100`), so there's room to insert without renumbering.

## How a chapter file works

Markdown for prose, raw HTML for the styled components. The wrapper carries `markdown="1"` so both work together.

```html
<section class="chapter" id="chNN" data-part="Part One — The Setup" markdown="1">
<div class="chap-head">
<span class="chap-num">1</span>
<span class="chap-stage">The Domino System · Stage 3 — Volume</span>
<h1>Chapter Title</h1>
<p class="chap-promise">By the end of this chapter you'll…</p>
</div>
... markdown prose ...
</section>
```

The table of contents is generated from `id="chNN"`, the `<h1>`, and `data-part`. Page numbers resolve automatically through CSS `target-counter`.

**One gotcha:** inside a `markdown="1"` block, indented raw HTML gets parsed as a code block. Keep nested HTML unindented. The system-map page avoids this by being pure HTML with no `markdown="1"`.

### Components available

`.principle` · `.pull` · `.donow` · `.script` + `.script-label` · `.warn` · `.failure` (a `<dl>`) · `.metric` · `.checklist` · `.storyslot` · `.attrib`

Tables get zebra rows automatically.

## Design spec as built

- Trim 8.5 × 11 in. Margins 0.95 in top/bottom, 0.9 in outer, 1.1 in inner, mirrored
- Body: Source Serif 4, 11/16 pt
- Headings: Archivo, tight tracking
- Script boxes: JetBrains Mono
- Palette — navy `#1F3F68` (from the mark), amber `#C0722C`, paper `#F4F0E8`, ink `#16191E`
- Running heads: chapter title verso, book title recto. Folios bottom outer
- Chapters open recto; part dividers open recto
- All fonts embedded. Full book well under the 25 MB ceiling

## Before this goes on sale

1. **Fill the story slots.** `grep -rin "story needed" build/chapters/` — 24 markers across 17 chapters. Chapters 1, 8, 10, 16 and 18 cannot ship without them.
2. **Clear client names.** See `build/back/50-clearance.md`, then delete that file from the retail build.
3. **Attorney review** of assets 05, 06, 07 (MSA, SOW, Proposal).
4. **Re-check Chapter 11** fees and timelines against current carrier requirements.
5. **Re-check Chapter 17** against current law and update the date line. The TCPA revocation-all rule lands 31 Jan 2027.
6. **Swap the logo.** `assets/onevision-mark.svg` is a reconstruction — the real file never reached the build session. Replace it and set the wordmark in the real typeface, outlined.
7. **Run `./build.sh --retail`** and confirm no story slots survive.

## Source material

`source/` holds four third-party copyrighted books, gitignored and never committed. They are a curriculum reference, not a proof layer. Frameworks drawn from them are attributed by name in body text and in `build/back/40-sources.md`. No third-party prose, table, script, or number is reproduced. See `CLAUDE.md`.
