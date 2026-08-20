# CLAUDE.md — The OneVision Playbook

Project rules for every session. Read before writing anything.

## What this is

A commercial digital product: a sellable PDF book teaching the marketing and agency-building
system behind OneVision Marketing (now Aventis Marketing). Priced $47–$197. Buyer is 18–28,
wants to start or grow a local marketing/lead-gen agency, and has already been burned by at
least one guru course.

Author: Isaiah Wright. Written in first person as Isaiah.

Master spec: `PROMPT.md`. Phase outputs: `build/01-extraction.md`, `build/02-method.md`,
`build/03-outline.md`, `build/chapters/`, `build/assets/`.

## ⚠️ Source material is third-party copyrighted work

`./source/` holds four Alex Hormozi `$100M Playbook` PDFs (Branding, Pricing, Lead Nurture,
Retention), © 2025 Acquisition.com LLC / Bumble IP LLC. Every page is stamped
**"NOT FOR DISTRIBUTION."** They are **not** Isaiah's documents.

Rules, no exceptions:

- **Never** reproduce their prose, tables, scripts, or numbers in the book or its assets.
- Attribute frameworks to their originator by name ("Hormozi's four pillars of lead nurture")
  and teach **Isaiah's application** in **Isaiah's own words**.
- **Never** use `$100M`, `Acquisition.com`, or Hormozi's name in a title, subtitle, chapter
  name, or asset filename. Body-text attribution only.
- Third-party statistics quoted in those books (Profitwell, HBR, Velocify, InsideSales,
  Hubspot, Lead Connect) must be verified at the **original** source and cited to the
  original — never to the playbook that quoted it.
- The PDFs are gitignored. Never commit them. Never paste extended passages into any file.
- They are a **curriculum reference**, not a proof layer. The proof layer is Isaiah's own
  numbers, stories, and builds.

## Zero-fabrication rule

Never invent a client name, revenue figure, case study, testimonial, screenshot, or result.
If a story slot needs filling and Isaiah hasn't supplied material, insert
`[STORY NEEDED: describe the moment you first ___]` and keep moving.

Real client names get `[CLIENT NAME — CONFIRM PERMISSION]` and go on a clearance list at the
end for Isaiah to approve. Fabricated proof is the one failure mode that can get him sued.

Anything not sourced from the PDFs or Isaiah's answers gets marked `[GAP]`.

## Voice

- **First person as Isaiah.** "I charged," "I lost that client," "I built this automation."
- **Second person for instruction.** "You're going to open GoHighLevel and…"
- Short paragraphs, 1–4 sentences. Read on a phone as often as a laptop.
- Concrete over abstract, always. Not "prospect consistently" — "40 outreach touches before
  noon, tracked in a pipeline stage called Cold."
- Contractions fine. Slang fine when it's how Isaiah actually talks. **No profanity.**
- **No emoji in the book body.**
- Direct, young, competitive, no corporate fluff. Athlete framing is authentic — use it where
  it earns its place, don't force it into every chapter.
- If a section starts sounding like a LinkedIn post, delete it and write the version he'd say
  out loud to a friend at a bar.

### Banned phrases

`in today's digital landscape` · `leverage` (as a verb) · `game-changer` · `unlock` ·
`supercharge` · `it's important to note` · `in conclusion` · `the truth is` ·
any sentence beginning with `Imagine`

### Banned structure

The three-item list where every item is the same length and starts with a gerund. Vary rhythm.

## Chapter template

Every chapter, in this order:

1. **Cold open** (150–300 words) — a specific real scene. Names, places, dollar amounts, dates.
2. **The principle** — one bolded sentence.
3. **Why most people get this wrong** — name the common approach, dismantle it.
4. **The system** — numbered steps, with tool, setting, and click path where relevant.
5. **The asset** — script/template/table/checklist, in-line and saved to `build/assets/`.
6. **Failure modes** — 3–5 specific breakages and the fix for each.
7. **The metric** — the number that proves it's working, and what "good" looks like.
8. **Do this now** (15–45 minutes) — one executable action, finishable today.

Length 1,500–3,000 words. If a chapter can't fill that with substance, merge it. Never pad.

## Quality bar — self-audit before showing any chapter

- [ ] Could a reader execute this without buying anything else or asking a follow-up?
- [ ] Does it contain something specific to Isaiah's experience, impossible to find in a
      generic article?
- [ ] Are all numbers either verified from sources/Isaiah's answers, or clearly labeled as an
      example?
- [ ] Zero banned phrases?
- [ ] A real story, not a hypothetical one?
- [ ] Does "Do this now" actually take under 45 minutes?
- [ ] Would a skeptical 22-year-old who paid $97 feel this chapter alone was worth $20?

## Compliance — bake in, don't bolt on

- **No income claims or guarantees.** Never "you'll make $10k/month." Results language
  describes Isaiah's experience; it never predicts the reader's.
- Watch for imported lift ranges ("20–40%, sometimes 200%+"). Any lift figure must be labeled
  an illustrative model or Isaiah's own measured result — never a promise.
- **Earnings disclaimer** on the copyright page, referenced in the intro.
- **Not legal advice** wherever contracts, TCPA, consent, or c. 93A come up. Tell readers to
  have a licensed attorney in their state review anything they use.
- Every contract template carries the header: *template only, review with counsel before use.*

## Build

```bash
./build.sh                      # regenerate both PDFs into output/
pip install weasyprint           # primary pipeline: MD → HTML + CSS Paged Media → PDF
python3 -c "..."                 # see build.sh for the exact invocation
```

Pipeline preference: WeasyPrint first; Pandoc → Typst or Pandoc → XeLaTeX as fallback.
Trim 8.5×11". Margins 0.9" outer, 1.1" inner. Body: humanist serif 11/16pt. Headings:
geometric or grotesque sans, tight tracking. Embed all fonts. Final file under 25MB.

Outputs: `output/OneVision-Playbook.pdf`, `output/OneVision-Playbook-Preview.pdf`,
`output/assets/`, `output/build-notes.md`.

## Working agreement

Work in phases. **Stop at every CHECKPOINT and wait for Isaiah's input.** Do not batch-draft
the book. One chapter, show it, then continue.
