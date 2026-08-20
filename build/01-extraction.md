# 01 — Extraction

**Phase 1 output. Read before answering CHECKPOINT 1.**
Source files: `./source/` (4 PDFs). Page numbers below are **PDF page indexes** (what you get if you jump to that page in a reader), not the printed folio numbers, which run 2–4 pages behind.

---

## ⚠️ FINDING THAT CHANGES THE PROJECT — read this first

The four PDFs in `./source/` are **not your documents.** They are Alex Hormozi's commercial `$100M Playbook` series, published by Acquisition.com / Bumble IP, LLC.

| File | Actual title | Author | Copyright |
|---|---|---|---|
| `100M_Playbook__Branding.pdf` | *$100M Playbook: Branding — How to Make Anyone or Anything Famous on Purpose* | Alex Hormozi | © 2025 Acquisition.com LLC |
| `100M_Playbook__Pricing.pdf` | *$100M Playbook: Pricing — Instant Ways to Make More Profit in Any Business* | Alex Hormozi | © 2025 Acquisition.com LLC |
| `100M_Playbook__Lead_Nurture.pdf` | *$100M Playbook: Lead Nurture — How to get more leads to respond, schedule, and show* | Alex Hormozi | © 2025 Bumble IP, LLC, licensed to Acquisition.com |
| `100M_Playbook__Retention.pdf` | *$100M Playbook: Retention — How to Get Customers to Keep Buying* | Alex Hormozi | © 2025 Acquisition.com LLC |

Every page of all four carries a running footer: **"NOT FOR DISTRIBUTION."** The Lead Nurture copyright page (PDF p.3) additionally reserves *"rights for text and data mining and training of artificial technologies or similar technologies."*

**What this means for the book:**

1. **`PROMPT.md` assumed the wrong inputs.** The `<author_dossier>` lists your in-house documents — Brand Style Guide, MSA, SOW, Proposal, Onboarding Playbook, Performance Report, Campaign Runbook, 90-Day Roadmap, Refund Policy. **None of them are in `./source/`.** Not one.
2. **There is zero Isaiah Wright material in these files.** No OneVision/Aventis story, no GoHighLevel build, no Norwood/Bridgewater client, no pricing you charged, no number you produced. The PDFs prove what you *studied*, not what you *built*.
3. **The `<workflow>` Phase 1 instruction "what it proves about my capability" cannot be answered from these files.** What they prove is that you read the right operators.
4. **The `<compliance>` block already anticipated this case** and it governs: *"Don't reproduce copyrighted material from third parties in the source PDFs. Attribute frameworks to their originators by name (e.g., Porter, Hormozi) and teach my application of them in my own words."* That rule is now the spine of the whole build, not a footnote.

**So the project is still fully buildable — but the sources have swapped roles.** They are not the proof layer. They are the *curriculum reference* layer. The proof layer has to come from you, at CHECKPOINT 1. Concretely:

- These PDFs can tell us **what mechanisms to teach** (activation points, speed-to-lead, availability, value-based pricing).
- They cannot supply **a single sentence of publishable prose, a single number, or a single story.**
- The `$100M`, `Acquisition.com`, and Hormozi marks are registered trademarks. The book can say *"Hormozi's four pillars of lead nurture"* as attribution. It cannot use `$100M` in a title, subtitle, chapter name, or asset name.

**Repo hygiene:** I have added `source/*.pdf` to `.gitignore`. Committing "NOT FOR DISTRIBUTION" books to a GitHub repo is redistribution. The PDFs stay local; the extraction below stays in git.

---

## Per-PDF description

### 1. Branding (36 PDF pages)

A short trade booklet arguing that branding is a *measurable, mechanical* discipline rather than an aesthetic one. Written for the operator who already sells something and suspects logo/color talk is a waste of time — Hormozi opens by explicitly rejecting "Marketing 101 class on branding, presentation, colors, and logos" (p.7). Published 2025 as a lead-in to Acquisition.com's `/scale` consulting call (the back-page CTA, p.35). Its core move is redefining "brand" as **pairing** — a definition chosen because it yields actions, where the nine popular definitions he quotes (p.8) do not. **What it proves about your capability:** nothing about you; it does tell us which model of brand you're likely operating from, and it is the one worth teaching a local-service audience because it's testable.

### 2. Pricing (61 PDF pages)

The longest and densest of the four, and the one with the most directly transferable hard assets. Two halves: a conceptual first third (the "business genie" thought experiment proving price beats acquisition and retention for profit leverage, pp.7–17; the three pricing models, pp.18–21; ~15 stated rules of pricing, pp.22–24), then ten discrete "pricing plays" (pp.28–59), each formatted identically — *How I learned this / How it works / Examples / Steps to implement / My advice*. Written for a small-business owner who will not rebuild their offer but will change a billing cycle. **What it proves about your capability:** nothing about you; it is the strongest structural template in the set — that repeating four-part play format is a book architecture worth borrowing (the format, not the content).

### 3. Lead Nurture (44 PDF pages)

The most operationally specific of the four, and the closest to what Aventis actually sells. Frames itself narrowly: *"This playbook solves one problem: maximizing 30-day show rates"* (p.8). Origin story is June 2020 COVID, a piece of software called ALAN (Artificial Lead Automation & Nurture), and a data hire who found four variables correlated with show rate — which become the **Four Pillars: Availability, Speed, Personalization, Volume** (p.9), plus Execution as a fifth chapter. Contains the only verbatim **sales scripts** in the entire source set (pp.19–20). Sold to a competitor in 2021. **What it proves about your capability:** nothing about you — but this is the document whose subject matter overlaps your GoHighLevel appointment-setting offer almost exactly, which makes it the highest-risk file for accidental paraphrase and the highest-value file for contrast (your book can show the *GHL build* that implements this; the PDF only describes the behavior).

### 4. Retention (35 PDF pages)

A checklist book on churn, built from a stated research method (interview the outliers, do a "common factors analysis" — pp.5–6, borrowed from Hormozi's Department of Defense consulting days). Two generations of content: the older **5 Horsemen of Retention** derived from gym owners under 3% monthly churn (p.7), and a newer **9-step Churn Checklist** derived from Skool platform data (p.16). Repeatedly honest that the mechanism is unknown: *"I don't know why these things work... I just know that they work"* (p.8). **What it proves about your capability:** nothing about you; it is the direct answer to your outline's Part IV promise, "how to not get fired in month two," and the activation-point concept is the single most transferable idea in the entire source set for an agency.

---

## Hard asset inventory

Everything below is **Hormozi's IP**. This is a map of *what mechanisms exist*, for deciding what your book teaches in your own words with your own numbers. Nothing here is drop-in copy.

### Frameworks

| Framework | Source | What it does |
|---|---|---|
| Brand = deliberate **pairing** of your thing with things your audience likes | Branding p.9 | Converts "brand" from aesthetic to action |
| **Reach / Influence / Direction** — 3 measures, 8 brand positions | Branding pp.11–13 | Reach = advertising output; influence = chance behavior changes; direction = toward/away |
| **4-step brand build**: who → what they like → associate → optimize | Branding p.22 | Spine of the booklet |
| **Ideal-customer 4 criteria**: growing, has money, easy to target, in pain | Branding p.23 | Niche screen — directly relevant to your niche scorecard asset |
| **Levels of Authority**: what we say → what others say → what they experience | Branding p.26 | Ranked by influence, ascending |
| **5 market directions**: up / down / adjacent / broader / narrower | Branding p.28 | Repositioning options |
| **Bouquet metaphor** for brand composition | Branding pp.28–29 | One rotten flower spoils the arrangement |
| **The business genie**: 2x customers vs. 2x purchases vs. 2x price | Pricing pp.7–15 | Proves price is the highest-leverage variable |
| **3 pricing models**: cost-plus / competitor / value-based | Pricing pp.18–20 | With pros and cons for each |
| **10 pricing plays** (see table below) | Pricing pp.28–59 | Each with a fixed 4-part structure |
| **Four Pillars of Lead Nurture**: Availability, Speed, Personalization, Volume | Lead Nurture p.9 | Derived from ALAN appointment data |
| **3 speed types**: to first contact / to first appointment / of response | Lead Nurture p.17 | |
| **6 personalization tactics** | Lead Nurture pp.24–30 | Channel, qualify, route, segment, incentivize, prove |
| **5 call outcomes** when scheduling | Lead Nurture p.19 | No-response / unqualified / free-now / pulled-forward / confirmed |
| **BAMFAM** — Book A Meeting From A Meeting (credited to Sharran Srivatsaa) | Lead Nurture p.35 | Never end a call without the next one booked |
| **Common factors analysis** — interview outliers, overlap their answers | Retention pp.5–6 | The research method behind the book |
| **5 Horsemen of Retention** | Retention p.7 | Attendance tracking, 2x/wk outreach, handwritten cards, events, exit interviews |
| **9-step Churn Checklist** | Retention p.16 | Activation → onboard → incentivize → community → fire bad → annual → cancel call → survey → journey |
| **Activation point**: *"Every customer that does X or gets Y stays longer than customers who don't"* | Retention p.17 | The highest-transfer idea in the set |
| **4-step customer journey**: activate → testimonial → refer → ascend | Retention p.30 | |
| **A-C-A**: Acknowledge, Compliment, Ask | Retention p.29 | Check-in message structure |
| **Push vs. pull incentives** | Lead Nurture p.28 | Gift before (reciprocity) vs. A/B choice assuming attendance |

### Pricing tables and structures

The ten plays and their stated lift (Pricing p.27):

| # | Play | Stated increase | Pages |
|---|---|---|---|
| 1 | Monthly → 28-day billing cycles | 8.3% | 28–29 |
| 2 | Processing fee + second form of payment | 3–4% | 30–32 |
| 3 | Sales tax passed through | 0–10% | 33–35 |
| 4 | Annual CPI price increases written into contract | 3–10% | 36–38 |
| 5 | Longer-duration billing options | 10–15% | 39–41 |
| 6 | Round up (7s→9s, add .99) | 1–3% | 42–44 |
| 7 | Annual renewal fee on top of monthly | 10% | 45–48 |
| 8 | Automatic continuity / continued access | 10% | 49–53 |
| 9 | Ultra-high-ticket anchor | 10–15% | 54–55 |
| 10 | Priced guarantee / warranty upsell | 5–20% | 56–59 |
| | **Stated total** | **26.8%–63.8%** | |

Other pricing structures: value-based price test table (price × clicks × conv × churn × LTV × total return, p.20, repeated Retention p.11); billing-cycle churn table (annual 2% / quarterly 5% / monthly 10.7%, p.39); renewal-fee sizing (0.5x monthly = +4.15%, 1x = +8.3%, 2x = +16.6%, 3x = +24.9%, p.47); continuity priced at 5–20% of core offer (p.50); anchor economics ($440 → $890 LTV, p.55); "big head, long tail" $6,800 one-time + $199/mo (Retention p.26).

### Scripts (all verbatim Hormozi — structure is usable, wording is not)

| Script | Source | Purpose |
|---|---|---|
| Appointment pull-forward call | Lead Nurture pp.19–20 | Confirm → qualify (who / what they want / what they've tried) → offer earlier slot |
| Re-confirmation | Lead Nurture p.20 | When the time can't move |
| Hot handoff / closer edification | Lead Nurture p.20 | Three-way intro to the closer |
| Second-form-of-payment ask | Pricing p.30 | "You can save the 3.99% by providing a second form of payment…" |
| Sales tax on invoice | Pricing p.34 | Dry, matter-of-fact, cite the code, separate line item |
| CPI increase disclosure | Pricing p.38 | Delivered at paperwork, not during the sale |
| Renewal fee "reason why" | Pricing p.47 | Rate protection / cancellation-fee prepayment |
| Warranty upsell | Pricing p.58 | "You just want the standard warranty on that?" |
| Annual billing downsell ladder | Pricing p.41 | Full price first → annual discount → quarterly → monthly |
| Gift card push incentive | Lead Nurture p.28 | Sent whether they show or not |
| A/B pull incentive | Lead Nurture pp.28–29 | Choice assumes attendance |
| Cancellation save | Retention p.28 | Redo or upsell; "get in the angry boat with them" |
| Retention survey pair | Retention p.29 | Keep-one / remove-one questions |

### Sequences and cadences

- **Outreach cadence, 8 steps** (Lead Nurture pp.31–32): call within 5 min → double-dial → voicemail → text → repeat double-dial+text 2 more times day 1 → 2 calls/day for days 2–3 → 1 call+text/day for 4 more days → long-term nurture.
- **Automated reminders** (p.33): immediate confirmation, 24h, 12h, 3h. Include name, date, time, and the area code you'll call from.
- **Manual reminders from a real phone** (p.34): night before ~6pm, morning of ~8am, 60 min prior. Multiple short messages, not one block.
- **Availability targets** (p.43): 7 days/week; 9am–9pm EST; 4 slots/hour; self-scheduling with steps removed.
- **Speed targets** (p.43): contact under 5 min (stretch: 60 sec); book same-day / next-day / day-after; 72-hour max scheduling window.
- **Retention cadences**: outreach 2x/week (Retention p.7); member events every 21/42/63 days (p.7); 1-on-1 check-in every 2–3 weeks (p.29); survey 2x/year (p.29); re-test activation points every 6–12 months (p.19).

### Checklists

One-page tear-off checklists at the back of three books: Branding (p.36), Lead Nurture (pp.43–44), Retention (pp.34–35). These are the format model for your asset vault — each is a single page, all checkboxes, no prose.

### KPIs and definitions

- **Schedule rate** = % of engaged leads who schedule. **Show rate** = % of scheduled who show. **Throughput** = % of engaged leads who show. Worked example: 100 leads → 50% schedule → 50% show → 25% throughput (Lead Nurture p.7).
- **Churn** = customers lost ÷ original pool, counted only against the opening cohort; new signups in-period don't affect it (Retention p.9).
- **Usage churn** = still subscribed, stopped using — leading indicator (Retention p.23).
- **Structural churn** = VSMB customers going out of business (Retention p.15).
- **Activation point** = leading indicator of retention (Retention p.17).
- Track and rank reps by **show rate, close rate, and lead-to-close** — not close rate alone (Lead Nurture p.40).
- Rep commission bump for show rate: **5–30% of what they make on a sale** (Lead Nurture p.40).

### Contract clauses referenced

Only three, all in Pricing, all as concepts rather than drafted language: right to annual CPI increase (p.38), annual renewal fee with initials next to both rate and fee (p.47), automatic continuity with explicit up-front agreement and a "don't be a sneak" warning against undisclosed continuity (p.52). **There is no MSA, SOW, proposal, or any drafted contract language anywhere in the source set.**

---

## NEEDS VERIFICATION

Every claim, number, and outcome stated across the four PDFs. Two categories matter and they behave very differently:

**Category A — Hormozi's proprietary claims about his own businesses.** Unverifiable by us, and not ours to make. Safe to publish: **No**, in every case. Not because they're false, but because repeating them makes your book a summary of his. A handful can appear as *attributed* one-liners; the table flags those.

**Category B — third-party research he cites.** Potentially usable, but only if you verify at the original source and cite the original, not the playbook.

### Category A — Hormozi proprietary claims

| Claim | Source & page | Can this be proven? | Safe to publish? |
|---|---|---|---|
| 10.1M person audience across platforms in ~4 years | Branding p.7 | Not by us | No |
| Sold 1M+ copies of last two books | Branding p.7 | Not by us | No |
| Acquisition.com deals worth hundreds of millions | Branding p.7 | Not by us | No |
| Friend earning ~$40k/mo affiliate commissions at 10–20%, would make $500k+/yr switching | Branding pp.4–5 | No | No |
| Manufacturer: "most expensive line I've ever made" | Branding p.4 | No | No |
| Unbranded vs. branded ad table: $2,500 vs $5,500 price, 1% vs 3% CTR, 4% vs 6% conv, 4:1 vs 45:1 ROAS | Branding p.20 | No — illustrative model, not disclosed as measured | No |
| "4.5x the sales and 11x the returns" from that table | Branding p.21 | No | No |
| Pepsi/Kendall Jenner ad pulled within six days, sales suffered | Branding pp.14–15 | Partially — widely reported news event | Only as a cited news event with a source; the sales claim needs a source |
| Gym price $99 → $299, lost 30% of members, 200 → 140 | Pricing p.22 | Not by us | No — but this is the single clearest teaching example of price/volume tradeoff; **build the equivalent from your own numbers** |
| Restaurant 4% processing fee: $1M rev, 9% margin, profit $90k → $130k (+44%) | Pricing p.25 | Arithmetic checks; the restaurant is anecdotal | Math is generic and re-derivable; **rebuild with your own worked example** |
| 28-day billing = 8.3% permanent revenue increase | Pricing p.28 | Arithmetic checks (13 cycles vs 12) | The arithmetic is a fact, not IP — usable if you derive it yourself |
| Automatic continuity produced $150k/month pure profit | Pricing p.49 | Not by us | No |
| Workshop speaker made $750k/yr from one contract line | Pricing p.49 | No | No |
| Round-up added ~$50,000/yr | Pricing p.44 | Not by us | No |
| Round-up: $104/yr and $155.48/yr per client, +4.25% to +11.1% | Pricing pp.42–43 | Arithmetic checks against stated prices | Method usable; **numbers must be yours** |
| "No change in conversion" from round-up | Pricing p.43 | No — no test data shown | No |
| Mentor John's 22-location tanning chain sold to LA Fitness; $39×12 + $99 = $567 = $47/mo effective (+20%) | Pricing pp.45–46 | Arithmetic checks; the story is anecdotal | Arithmetic yes, story no |
| Tailor's $16,000 suit anchor | Pricing p.54 | No | No |
| Ultra-high anchor: LTV $440 → $890 | Pricing p.55 | Illustrative model | Model usable, numbers must be yours |
| Friend implemented anchor, now sells only that, "millions per year" | Pricing p.55 | No | No |
| Warranty upsell covered ~half of sales-team commissions | Pricing p.57 | Not by us | No |
| Buffett raised See's Candies prices 50+ times in 51 years, some years 17%, $1B+ profit impact | Pricing p.38 | Partially — Buffett has discussed See's pricing publicly; the specifics need sourcing | Only with an independent citation |
| Warren Buffett quotes (pricing power; 20 years to build a reputation; price vs. value; premium brand) | Branding pp.20, 22, 27; Retention p.10 | Yes — widely published | Yes, attributed to Buffett directly, not via the playbook |
| Naval quote on sales/marketing/product | Retention p.4 | Yes — widely circulated | Yes, attributed |
| ALAN managed 4,000+ appointments/day | Lead Nurture p.6 | Not by us | No |
| ALAN sold to a larger competitor in 2021 | Lead Nurture p.7 | Partially — public record | Only as attributed background |
| Portfolio companies generate 20,000+ leads/day | Lead Nurture p.9 | Not by us | No |
| The four ALAN show-rate correlations (slots, days-out, follow-ups, responses) | Lead Nurture pp.6–7 | Not by us | Findings can be attributed as Hormozi's; the *underlying behaviors* are yours to teach and measure |
| "20–40%, sometimes 200%+ increases in appointments" | Lead Nurture p.13 | Not by us | **No — this is exactly the kind of range that reads as an income claim** |
| Nail salon story (Leila, June 2021, four salons) | Lead Nurture pp.11–12 | No | No |
| ALAN beta tester's shirt-color text trick | Lead Nurture p.23 | No | No |
| Timeshare rep: #1 of ~3,000 reps, 5 of 6 years, 5x'd office, company $200M → $1B over 5 years | Lead Nurture pp.25–26 | Not by us | No |
| Jacob: 150-call quota, 400 calls/day, top salesman of 26, "yellows are the new gold" | Lead Nurture pp.37–39 | Not by us | No — but the *principle* (volume, no lead-cherry-picking) is teachable in your own words |
| 1,000 gym owners in the program; avg microgym owner earns $30,000/yr; 12.5% margins | Retention p.4 | Not by us | No |
| 15% monthly churn = 83% annual member loss; 250 members needs 208 replacements | Retention p.4 | Arithmetic checks | Math is re-derivable and worth teaching with your own churn numbers |
| 5 Horsemen results: churn +50% M1, −50% M2, −50% M3; 10%→15%→7%→3% | Retention p.8 | Not by us | No |
| "Shaking the tree" — churn rises before it falls | Retention p.8 | Not by us | Concept can be taught attributed; the numbers can't |
| 9%→3% churn = 3.3x LTV; 10%→3% = 3.3x LTV | Retention pp.8, 13 | Arithmetic checks (1/0.09 vs 1/0.03) | Formula is standard — teach the formula, derive it yourself |
| Gym Launch competitor comparison: 70x more profit, customers worth $5,000 vs $42,000 first-year | Retention p.18 | Not by us | No |
| Fast Cash Play: churn 8% → 3% within 6 months | Retention p.18 | Not by us | No |
| 1-on-1 onboarding gave 25% boost in ascensions; company went $2M/month → $2M/week | Retention p.21 | Not by us | No |
| Skool: hosts with 3+ group members stay much longer; engagement level 3 = longest retention | Retention pp.17, 22 | Not by us | No — but activation-point *method* is the most valuable transferable idea in the set |
| Newsletter friend at $500k/month; churn rose every time he added deliverables | Retention p.12 | No | No |
| "Overwhelm is the #1 reason for churn" | Retention p.12 | Asserted, not evidenced | Only as attributed opinion |
| Gym Launch on its 10th version, each shorter | Retention p.12 | Not by us | No |
| Exit interviews save ~half of cancellations; ~25% churn cut assuming half show; 33% LTV increase | Retention pp.7, 28 | Not by us | No |
| PR agency advised 10x'd over 24 months | Retention p.18 | No | No |
| 10–20% take annual at "buy 10 get 2 free"; 30% if default; 35–40% by phone | Retention p.26; Pricing p.40 | Not by us | No |
| Involuntary churn from card changes = 1.2–1.7%/month, 24–34% of total churn at 5% churn | Pricing pp.30–31 | Industry-adjacent; no source given in text | Only with an independent, citable source |
| Second-card LTV gains: +31% to +51% at 5% churn | Pricing p.31 | Modeled from the above | Model only, with your own inputs |
| Automatic continuity math: LTV $5,600 → $7,400 (+32%), 50% take rate | Pricing p.51 | Illustrative model | Model usable, numbers must be yours |
| Grand Slam offer table: $5,000 vs $112,000 collected, 0.5:1 vs 11.2:1 ROAS | Retention p.27 (reproduced from *$100M Offers*) | No | **No — this is lifted from another Hormozi book, double-flagged** |
| "Average small business runs 7–10% net margins (Investopedia)" | Pricing p.26 | Verifiable at source | Yes, if verified and cited to Investopedia |
| "Average gym runs 12.5% net margins" | Pricing p.43 | No source given | No |
| "78% of businesses are in the service industry" | Pricing p.33 | No source given | No |
| Average US rent increase 3.18% annually | Pricing p.36 | Verifiable | Only with an independent citation |
| $100 in 2024 = $79 in 2017 (21% purchasing power loss) | Pricing p.37 | Verifiable via BLS CPI | Yes, if recalculated from BLS with current dates |

### Category B — third-party research cited in the PDFs

Usable **only** after you or I verify at the original source and cite the original. Several are years old and some are marketing-vendor studies rather than peer-reviewed work — treat accordingly.

| Statistic | Attributed to | Source & page | Notes |
|---|---|---|---|
| 1% pricing improvement ≈ 2x as efficient as retention, ~4x acquisition, across 512 companies | Profitwell | Pricing pp.15–16 | Also the basis for the whole genie framing. Verify; Profitwell is now Paddle |
| Companies that test pricing more often make more profit and grow faster | Profitwell | Pricing p.16 | Same source |
| Billing-cycle churn: annual 2%, quarterly 5%, monthly 10.7% | Profitwell | Pricing p.39 | Patrick Campbell, sold Profitwell $250M in 2022, 14,000 memberships |
| 391% increase in conversions when contacted within 60 seconds | Velocify | Lead Nurture p.17 | Verify; vendor study |
| Contact within 1 hour = 7x more likely to qualify; 60x vs 24 hours | Harvard Business Review | Lead Nurture p.17 | HBR "Short Life of Online Sales Leads," 2011 — old, verify currency |
| 78% of customers buy from whoever responds first | Lead Connect | Lead Nurture p.17 | Verify; vendor study |
| Average first response takes 42 hours | InsideSales.com | Lead Nurture p.9 | Verify |
| Salespeople average 1.3 attempts; 44% stop after the first | InsideSales.com / RAIN Group | Lead Nurture p.9 | Verify |
| Hubspot improved email ROI 7x after segmenting | Hubspot | Lead Nurture p.26 | Verify |
| 5% retention increase → 25–95% profit increase | Harvard Business Review | Retention p.14 | Reichheld/Sasser 1990 — very old, still widely cited, verify |
| Costs 5x–25x more to acquire than retain | HBR (implied) | Retention p.14 | Attribution vague in source; verify independently |

---

## Contradictions and gaps vs. the author dossier

| # | Dossier says | Sources say | Impact |
|---|---|---|---|
| 1 | Four PDFs are my material, proving my capability | Four PDFs are Hormozi's copyrighted commercial books | **Total.** The entire evidentiary basis of the book is missing |
| 2 | In-house docs exist: Brand Style Guide, MSA, SOW, Proposal, Onboarding Playbook, Performance Report, Campaign Runbook, 90-Day Roadmap, Refund Policy | None present in `./source/` | The `<monetization_assets>` list assumed these could be adapted. They must be supplied or built from scratch |
| 3 | Core stack: GoHighLevel, A2P 10DLC, Conversation AI, snapshots | Zero mentions of GoHighLevel, A2P, 10DLC, or any named CRM anywhere in 176 pages | Every click-path, every automation, every build screenshot is a `[GAP]` |
| 4 | Compliance knowledge: TCPA, MA two-party consent, M.G.L. c. 93A, FTC disclosure | Zero mentions. Sources say only "follow the laws in your area" and "be compliant, which varies by state" | The compliance chapter and quick-reference asset have **no source support** and must come from you plus counsel |
| 5 | Market: Norwood / Bridgewater / South Shore MA, local service businesses | Sources use gyms, supplements, assisted living, timeshare, insurance, Skool, software | No local-service-MA specificity exists to draw on |
| 6 | Verticals: landscaping, auto detailing (Quick N' Clean), real estate (Akira Real Estate, Dedham MA) | Not mentioned | All client stories are `[GAP]` |
| 7 | Positioning: "operating manual of a real working agency, written by the person running it" | Sources supply no operating detail from your agency | **This positioning is currently unsupported and is the thing a refund request would attack** |
| 8 | Athlete framing is authentic and should earn its place | No athletic content in sources | Fine — this is yours, sources were never going to supply it |
| 9 | `<pdf_build_spec>` says pull brand palette from Aventis assets in `./assets/` | `./assets/` is empty | Palette must be proposed for your approval (Phase 6, CHECKPOINT 4) |
| 10 | Book targets local agency owners | Pricing plays assume subscription/retail/gym/physical-product contexts; several (sales tax, warranty upsells, round-up on weekly billing) map poorly onto a monthly retainer agency | Translation work required; can't lift the play list wholesale |

---

## Teachable moments

The `<workflow>` asked for "places where **I** did something non-obvious that a beginner would never think of." **The sources contain none of these about you** — they are all `[GAP]` pending CHECKPOINT 1.

What the sources *do* contain is non-obvious mechanisms worth teaching *in your own application*. Listing them because they're the raw material for your Part II–IV chapters and for the contrarian beliefs in Phase 2:

1. **Availability beat speed as the top show-rate driver** (Lead Nurture pp.11–12). Genuinely counterintuitive — everyone optimizes response time; the data said number of bookable slots mattered more. For an agency this reframes the whole client-calendar conversation.
2. **Adding friction on purpose when appointment quality drops** (Lead Nurture p.16). Video, sales letter, or price above the scheduler. Beginners only ever remove friction.
3. **Actively canceling sales appointments** with unqualified leads to free capacity (Lead Nurture p.24).
4. **Routing the best leads to the best closers** rather than distributing evenly (Lead Nurture pp.25–26). Most agencies round-robin.
5. **Churn rises before it falls** when you start retention work — "shaking the tree" (Retention p.8). Without this warning, an operator quits the intervention in week 3. This is exactly the "don't get fired in month two" material.
6. **The activation point method** — find the top 20% of long-staying customers, find the common thing they did, then engineer everyone toward it (Retention pp.17–19). Transfers directly to agency client retention.
7. **Adding deliverables can increase churn** (Retention p.12). Overwhelm, not underdelivery, kills accounts. Contradicts the beginner instinct to pile on value when a client goes quiet.
8. **Usage churn as leading indicator** (Retention p.23) — the client who stopped logging in is already gone, just still paying. Directly buildable as a GHL alert.
9. **Match billing cadence to value cadence** — one-time value billed one-time, ongoing value billed ongoing (Pricing p.24). The "lookback window" idea: clients judge you on the last billing cycle, not the relationship. This is the single most useful pricing idea for an agency retainer.
10. **Longer billing cycles reduce churn** (Pricing pp.23, 39) — bill as far out as you can.
11. **High close rate means prices are too low** (Pricing p.22). Over 50% consistently = raise.
12. **Display price in the smallest increment, bill on the longest** (Pricing p.24).
13. **BAMFAM** (Lead Nurture p.35) — treat "I'll follow up" as an objection to be handled.
14. **Rank reps by lead-to-close, not close rate** (Lead Nurture p.40) — close rate rewards cherry-picking.
15. **Brand pivots are net-change bets** (Branding pp.29–30) — you will lose audience; the only question is the ratio.
16. **Recover from a brand mistake by burying it, not deleting it** (Branding pp.31–32).
17. **The "how would I churn 100% of customers?" inversion** (Retention p.10) — a fast diagnostic that produces a to-do list.
18. **Common factors analysis as a research method** (Retention pp.5–6) — interview the outliers, overlap the answers. This is how *you* could produce original data for the book from your own client base.

---

## `[GAP]` list

Everything the book needs that **no source file supplies.** Grouped by how it gets filled.

### Fillable only by you (CHECKPOINT 1 and beyond)

- `[GAP]` Origin story — how OneVision Marketing started, when, why, from what
- `[GAP]` **The first paying client** — who, what vertical, how they were found, what you charged, what happened
- `[GAP]` The rename to Aventis Marketing — when and why
- `[GAP]` One Vision Group's relationship to Aventis
- `[GAP]` Every price you have ever charged: setup fees, retainers, per-appointment, per-lead, rev-share
- `[GAP]` Your actual offer structure and what's in each tier
- `[GAP]` Client count, current and peak
- `[GAP]` Longest-retained client and how long
- `[GAP]` Every client outcome — appointments booked, leads generated, close rates, cost per lead
- `[GAP]` **Your failures** — clients lost, refunds issued, campaigns that produced nothing, and why
- `[GAP]` Every GoHighLevel build detail: pipeline stage names, automation triggers, workflow logic, Conversation AI prompts, snapshot contents
- `[GAP]` Your A2P 10DLC registration experience — timeline, rejections, what the brand/campaign registration actually required
- `[GAP]` Your outreach method and its real numbers: channel, volume/day, response rate, booking rate
- `[GAP]` Your discovery call structure and the objections you actually hear
- `[GAP]` Contents of your existing in-house documents (MSA, SOW, Proposal, Onboarding Playbook, Performance Report, Campaign Runbook, 90-Day Roadmap, Refund Policy, Brand Style Guide)
- `[GAP]` The Good Boy Co. outcome — worth telling only if it failed instructively
- `[GAP]` Which client names you can use, and whether written permission exists
- `[GAP]` Your ad spend and results, if you've run paid
- `[GAP]` Your own churn rate and what caused each loss
- `[GAP]` Athletic-background moments specific enough to carry a cold open (a practice, a game, a coach, a number)
- `[GAP]` The cohort/coaching program referenced as secondary buyer — does it exist yet, what's in it

### Fillable by research (I can do this)

- `[GAP]` TCPA current requirements and 2024–2026 rule changes
- `[GAP]` A2P 10DLC registration process, current carrier requirements, current fees
- `[GAP]` Massachusetts two-party consent law (M.G.L. c. 272 § 99) as it applies to recorded sales calls
- `[GAP]` M.G.L. c. 93A as it applies to service agreements and advertising
- `[GAP]` FTC endorsement/testimonial disclosure rules, 2023 revision
- `[GAP]` Current GoHighLevel UI click paths (must be dated in the book — this UI changes)
- `[GAP]` Verification of every Category B statistic above at original source
- `[GAP]` Local-service-business market data for Massachusetts

### Structural gaps

- `[GAP]` No drafted contract language exists anywhere in sources — MSA/SOW skeletons must be written from scratch and carry the counsel-review header
- `[GAP]` No niche-selection scorecard exists — Hormozi's 4 criteria are a starting point, weighting is yours
- `[GAP]` No objection-handling material of any kind in any source — all 12 objections must come from your calls
- `[GAP]` No reporting template or QBR structure in any source
- `[GAP]` No ad creative briefs or hook formulas in any source
- `[GAP]` The Hormozi Value Equation, referenced in `<monetization_assets>`, is from *$100M Offers* — **not in this source set.** Attribute by name and teach your application; do not reproduce it
- `[GAP]` `./assets/` is empty — no Aventis brand files, so no palette, logo, or type to build from

---

## Compliance flags carried forward

1. **Copyright is the live risk on this project.** Four "NOT FOR DISTRIBUTION" books cannot supply prose, tables, scripts, or numbers to a product you sell. Attribution by name + your own application in your own words is the only safe path, and `<compliance>` already requires it.
2. **Trademarks.** `$100M`, `Acquisition.com`, and the Hormozi name are protected. Attribution in body text is fine; titles, subtitles, chapter names, and asset filenames are not.
3. **The "20–40%, sometimes 200%+" style range is the highest-risk pattern to import.** `<compliance>` bans income claims. Any lift figure in your book must be labeled as an illustrative model or as your own measured result, never a promise.
4. **Every third-party statistic must be cited to its originator**, not to the playbook that quoted it.
5. **No client name appears in the book without a `[CLIENT NAME — CONFIRM PERMISSION]` marker** cleared by you. The dossier already names Quick N' Clean and Akira Real Estate — both are flagged pending your written permission.
6. **The compliance chapter has no source support.** It rests entirely on your knowledge plus my research, and must carry the not-legal-advice disclaimer prominently.
