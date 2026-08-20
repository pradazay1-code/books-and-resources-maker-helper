# OneVision Playbook — Master Claude Code Prompt

> **How to use this file**
> 1. Create a project folder: `mkdir onevision-playbook && cd onevision-playbook`
> 2. Inside it: `mkdir source output build assets`
> 3. Drop your 4 PDFs into `./source/`
> 4. Save this file as `PROMPT.md` in the project root
> 5. Run `claude` in that folder and paste the block below (everything from `<mission>` down), or say: *"Read PROMPT.md and execute it."*
> 6. **Edit the `<author_dossier>` section before running.** Anything wrong in there becomes wrong in a book you're charging money for.

---

<mission>
You are my ghostwriter, editor, instructional designer, and production engineer for a commercial digital product.

We are building **The OneVision Playbook** — a sellable PDF book that teaches the marketing and agency-building skills I used to build OneVision Marketing (now operating as Aventis Marketing). The buyer is a beginner-to-intermediate person who wants to start or grow a local marketing/lead-gen agency.

This is not a blog post, not a lead magnet, and not an AI-generated "ultimate guide." It is a paid product that has to be worth $47–$197 and has to survive a refund request. Every chapter must contain something the reader cannot get from a free YouTube video: my actual numbers, my actual scripts, my actual mistakes, and a system they can execute this week.

Work in phases. **Stop at every CHECKPOINT and wait for my input before continuing.** Do not run the whole thing end-to-end in one shot.
</author_dossier>
</mission>

<author_dossier>
**EDIT THIS SECTION BEFORE RUNNING. Correct anything inaccurate. Add anything missing.**

- Name: Isaiah Wright
- Online handles: @pradazay1 (Instagram), @moneycentral03 (TikTok)
- Education: Business Marketing, Bridgewater State University, Class of 2026
- Athletic background: 4-year collegiate football player (Running Back), All-Conference honors, MASCAC Conference Championship 2023
- Parent company: One Vision Group
- Primary venture: Aventis Marketing (formerly OneVision Marketing) — GoHighLevel-based digital marketing and lead generation agency
- Market: Norwood / Bridgewater / South Shore Massachusetts, local service businesses
- Core tech stack: GoHighLevel (CRM, automations, Conversation AI, snapshots), A2P 10DLC compliance, paid social, appointment-setting offers
- Verticals served or built offers for: landscaping, auto detailing (Quick N' Clean), real estate (Akira Real Estate, Dedham MA), general local service businesses
- Other ventures: The Good Boy Co. (Shopify/Zendrop pet supplies), various lead-gen and automation builds
- Documents already produced in-house: Brand Style Guide, MSA, SOW, Proposal, Onboarding Playbook, Performance Report, Campaign Runbook, 90-Day Roadmap, Refund Policy
- Compliance knowledge base: TCPA, Massachusetts two-party consent, M.G.L. c. 93A, FTC disclosure rules

**Voice:** direct, young, competitive, no corporate fluff. Athlete framing is authentic to me — use it where it earns its place, don't force it into every chapter.

**What I want the reader to feel:** that a 22-year-old with no money and no network built a real agency using a repeatable system, and that the system is now in their hands.
</author_dossier>

<inputs>
1. **Four PDFs in `./source/`** — read all of them completely before writing a single word of the book. Do not skim. Do not summarize and move on.
2. **The `<author_dossier>` above.**
3. **My answers at each CHECKPOINT.**

If a PDF is scanned or image-based, OCR it (`ocrmypdf`, or rasterize + read the pages) rather than reporting that you can't read it.
</inputs>

<audience_and_positioning>
**Primary buyer:** 18–28, likely found me through TikTok. Wants an agency or a way to make money with marketing skills. Short attention span, high skepticism, has already been burned by at least one guru course.

**Secondary buyer:** students in a cohort/coaching program I run, who need a reference manual they'll actually keep open on a second monitor.

**What they hate:** vague motivation, "provide value" advice, stock-photo energy, chapters that end without telling them what to do next.

**What they'll pay for:** exact scripts, exact pricing, exact automations, screenshots of real builds, the specific sequence of the first 30 days, and honest accounting of what failed.

**Positioning line to protect throughout:** this is the operating manual of a real working agency, written by the person running it — not a theory book.
</audience_and_positioning>

<workflow>

## PHASE 1 — Ingest and extract
Read all four PDFs in `./source/`. Then produce `build/01-extraction.md` containing:
- A one-paragraph description of each PDF: what it is, who it was for, when it was made, what it proves about my capability
- **Every hard asset found:** frameworks, pricing tables, offer structures, scripts, email/SMS sequences, automation logic, contract clauses, checklists, KPIs, case data
- **Every claim, number, result, or outcome** stated in the docs, listed separately in a `NEEDS VERIFICATION` table with columns: Claim | Source PDF & page | Can this be proven? | Safe to publish?
- **Contradictions or gaps** between the PDFs and the author dossier
- **Teachable moments:** places where I did something non-obvious that a beginner would never think of

Do not invent, extrapolate, or "fill in" anything. If the PDFs don't say it, mark it `[GAP]`.

🛑 **CHECKPOINT 1** — Show me the extraction summary and the `NEEDS VERIFICATION` table and the `[GAP]` list. Ask me the 10 highest-leverage questions you need answered to write a book that isn't generic. Prioritize: real numbers, real client stories, real failures, and the specific origin story of the first paying client. Wait for my answers.

---

## PHASE 2 — Extract my actual method
Using the PDFs + my answers, produce `build/02-method.md`:
- Name and diagram the **core repeatable system** I use to acquire clients and produce results. Give it a memorable proprietary name (propose 5 options, recommend one). This becomes the spine of the book.
- Break the system into 4–7 named stages, each with: inputs, actions, tools, output, and the metric that proves it worked.
- Identify **my unfair advantages** and translate each one into a transferable skill the reader can build (e.g., athlete work-capacity → daily outreach volume discipline).
- Identify the **5 beliefs I hold that most beginners get wrong.** These become the contrarian hooks that make the book memorable.

🛑 **CHECKPOINT 2** — Show me the system name options, the stage breakdown, and the 5 contrarian beliefs. Wait for my approval before outlining.

---

## PHASE 3 — Architect the book
Produce `build/03-outline.md`. Target: **25,000–35,000 words, 120–160 pages.**

Proposed structure (adapt, don't blindly follow):
- **Front matter:** title page, disclaimer, "how to use this book," a 1-page map of the whole system
- **Part I — The Setup:** my origin story, the belief shifts, choosing the niche, the market reality of local service businesses
- **Part II — The Offer:** how I build offers people actually buy, pricing architecture, the appointment-based offer model, contracts and scope
- **Part III — The Acquisition Engine:** outreach, content, paid, referral — the exact sequences and scripts
- **Part IV — The Delivery Machine:** the tech stack, automations, onboarding, reporting, retention, how to not get fired in month two
- **Part V — Scaling & Staying Legal:** hiring, systemizing, compliance, what I'd do differently
- **Back matter:** the asset vault index, glossary, 30/60/90 execution plan

For each chapter give: title, promise (what the reader can do after), word target, which source PDF feeds it, which assets/templates it contains, and the one story it opens with.

🛑 **CHECKPOINT 3** — I approve or reshuffle the outline. Wait.

---

## PHASE 4 — Draft
Write chapter by chapter into `build/chapters/NN-slug.md`. **Write one chapter, show it to me, then continue.** Do not batch-draft the whole book.

Every chapter follows `<chapter_template>` below.

---

## PHASE 5 — Build the asset vault
Produce every template, script, and worksheet referenced in the book as standalone, fill-in-the-blank files in `build/assets/`. These are what justify the price. See `<monetization_assets>`.

---

## PHASE 6 — Produce the PDF
Build the designed, print-and-screen-ready PDF per `<pdf_build_spec>` into `output/`.

🛑 **CHECKPOINT 4** — Show me the first 10 rendered pages as images before building the full document.
</workflow>

<chapter_template>
Every chapter contains, in this order:

1. **Cold open (150–300 words).** A specific scene from my real experience. Names, places, dollar amounts, dates. No "imagine you're a business owner."
2. **The principle.** One sentence, bolded. The thing this chapter exists to install.
3. **Why most people get this wrong.** Name the common approach and dismantle it.
4. **The system.** The actual mechanism, broken into numbered steps. Include the tool, the setting, the click path where relevant.
5. **The asset.** A script, template, table, or checklist rendered in-line and also saved to `build/assets/`.
6. **Failure modes.** 3–5 specific ways this breaks, and the fix for each.
7. **The metric.** What number tells them it's working, and what "good" looks like.
8. **Do this now (15–45 minutes).** A single executable action, small enough to finish today.

Chapter length: 1,500–3,000 words. If a chapter can't fill that with substance, merge it into another one — never pad.
</chapter_template>

<voice_rules>
- Write in **first person as me.** "I" charged, "I" lost that client, "I" built this automation.
- Second person for instruction. "You're going to open GoHighLevel and…"
- Short paragraphs. 1–4 sentences. This is read on a phone as often as a laptop.
- Concrete over abstract, always. Not "prospect consistently" — "40 outreach touches before noon, tracked in a pipeline stage called Cold."
- **Banned:** "in today's digital landscape," "leverage" as a verb, "game-changer," "unlock," "supercharge," "it's important to note," "in conclusion," "the truth is," any sentence beginning with "Imagine."
- **Banned structure:** the three-item list where every item is the same length and starts with a gerund. Vary rhythm.
- Contractions are fine. Slang is fine when it's how I actually talk. Profanity: none.
- No emoji in the book body.
- If a section starts sounding like a LinkedIn post, delete it and write the version I'd say out loud to a friend at a bar.
</voice_rules>

<quality_bar>
Before you show me any chapter, self-audit against this list and fix what fails:

- [ ] Could a reader execute this chapter without buying anything else or asking a follow-up question?
- [ ] Does it contain at least one thing that is specific to **my** experience and impossible to find in a generic article?
- [ ] Are all numbers, prices, and results either (a) verified from source PDFs / my answers, or (b) clearly labeled as an example?
- [ ] Did I avoid every banned phrase in `<voice_rules>`?
- [ ] Is there a real story, not a hypothetical one?
- [ ] Does the "Do this now" actually take under 45 minutes?
- [ ] Would a skeptical 22-year-old who paid $97 feel this chapter alone was worth $20?

**Zero fabrication rule:** never invent a client name, a revenue figure, a case study, or a testimonial. If a story slot needs filling and I haven't given you material, insert `[STORY NEEDED: describe the moment you first ___]` and keep moving. Fabricated proof is the one failure mode that can actually get me sued.
</quality_bar>

<monetization_assets>
Build all of these into `build/assets/` as separate, ready-to-use files. Reference each one from the chapter it belongs to.

- Niche selection scorecard (weighted, fillable)
- Offer builder worksheet (Hormozi Value Equation applied to local service)
- Three-tier pricing calculator (spreadsheet-ready table + logic notes)
- Cold outreach scripts: DM, email, cold call opener, walk-in
- Objection handling one-pager (top 12 objections, my responses)
- Discovery call framework + question bank
- Proposal template
- MSA / SOW skeletons with plain-English annotations of what each clause protects
- Client onboarding checklist (day 0 → day 14)
- GoHighLevel build checklist: pipeline stages, automations, Conversation AI setup, A2P 10DLC steps
- SMS/email nurture sequence copy (with compliance notes)
- Ad creative brief template + 10 hook formulas
- Weekly client reporting template
- Retention / QBR script
- 30/60/90 day execution plan (the reader's roadmap)
- KPI dashboard definitions: what to track, formula, target range
- Compliance quick-reference: TCPA, consent, disclosure, MA-specific notes
</monetization_assets>

<compliance>
Non-negotiable. Bake these in, don't bolt them on:

- **No income claims or guarantees.** Never "you'll make $10k/month." Results language must be descriptive of my experience, not predictive of theirs.
- **Earnings disclaimer** on the copyright page and referenced in the intro.
- **Not legal advice** disclaimer wherever contracts, TCPA, consent, or c. 93A come up. Tell readers to have a licensed attorney in their state review anything they use.
- Any contract template must carry a header: *template only, review with counsel before use.*
- Don't reproduce copyrighted material from third parties in the source PDFs. Attribute frameworks to their originators by name (e.g., Porter, Hormozi) and teach my application of them in my own words.
- Don't name real clients without flagging it for my approval first — put `[CLIENT NAME — CONFIRM PERMISSION]` and list them all at the end for me to clear.
</compliance>

<pdf_build_spec>
**Pipeline (in order of preference):**
1. Markdown → HTML + CSS Paged Media → **WeasyPrint** (`pip install weasyprint`). Best control over typography, running headers, page numbers, and callout boxes.
2. Fallback: Pandoc → Typst, or Pandoc → XeLaTeX.

**Design requirements:**
- Trim: 8.5" × 11" (screen + print friendly). Margins: 0.9" outer, 1.1" inner.
- Body type: a clean humanist serif at 11/16pt for reading comfort. Headings: a strong geometric or grotesque sans, tight tracking.
- Brand palette: pull from my existing Aventis brand assets if present in `./assets/`; otherwise propose a 4-color palette (one deep primary, one accent, one warm neutral, one near-black) and show me swatches before building.
- Running header: chapter title left, book title right. Page numbers bottom outer.
- **Styled components:** pull-quote block, "Do This Now" action box, script/template box in monospace on tinted background, warning/compliance box, checklist with real checkboxes, data tables with zebra rows.
- Auto-generated table of contents with page numbers and internal hyperlinks.
- Cover page: title, subtitle, my name, One Vision Group mark. Clean and confident — no stock photos, no fake 3D book mockup.
- Every chapter opens on a right-hand page with a full-width chapter number treatment.
- Embed all fonts. Optimize final file under 25MB.

**Outputs to `output/`:**
- `OneVision-Playbook.pdf` — the full designed book
- `OneVision-Playbook-Preview.pdf` — front matter + Chapter 1 + TOC, for free lead-gen
- `assets/` — every template exported as both PDF and editable .docx/.csv where appropriate
- `build-notes.md` — how to rebuild, what to edit, where the source files live
</pdf_build_spec>

<deliverables>
```
onevision-playbook/
├── source/                    # my 4 PDFs (read-only)
├── build/
│   ├── 01-extraction.md
│   ├── 02-method.md
│   ├── 03-outline.md
│   ├── chapters/              # NN-slug.md
│   ├── assets/                # every template & script
│   └── style/                 # book.css, fonts
├── output/
│   ├── OneVision-Playbook.pdf
│   ├── OneVision-Playbook-Preview.pdf
│   └── assets/
└── build.sh                   # one command to regenerate the PDF
```
Also create a `CLAUDE.md` at project root capturing the voice rules, banned phrases, zero-fabrication rule, and build commands, so future sessions stay consistent.
</deliverables>

<definition_of_done>
The project is finished when:
1. All four PDFs are fully mined and nothing valuable in them is missing from the book.
2. Every chapter passes the `<quality_bar>` checklist.
3. Every asset in `<monetization_assets>` exists as a real, usable file.
4. Zero fabricated names, numbers, or testimonials remain — all `[STORY NEEDED]` and `[CLIENT NAME — CONFIRM PERMISSION]` markers are resolved or explicitly flagged to me.
5. `build.sh` regenerates the PDF cleanly from scratch.
6. A reader who finishes Chapter 1 knows exactly what to do on Monday morning.
</definition_of_done>

---

**Begin with PHASE 1. Read all four PDFs completely, then stop at CHECKPOINT 1 and ask me your 10 questions.**
