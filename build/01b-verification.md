# 01b — Source Verification & Compliance Research

Closes the research `[GAP]`s from `01-extraction.md`. Two jobs: verify every third-party
statistic at its **original** source, and pin down the compliance facts the book has to get
right. Done independently of Isaiah's answers.

Researched 2026-08-20. **Anything with a date on it needs a re-check before publication.**

---

## Part 1 — Statistic verification

### ⚠️ CORRECTION: the retention statistic is misquoted

This one matters. It's the most-cited number in the retention world and the playbook repeats
the wrong version.

| | |
|---|---|
| **As printed in the source PDF** | "increasing retention by five percent increased profits by twenty-five to **ninety-five** percent" (Retention p.14) |
| **What the original actually says** | Reducing customer defections by 5% boosts profits by **25% to 85%** |
| **Original source** | Frederick F. Reichheld & W. Earl Sasser Jr., *"Zero Defections: Quality Comes to Services,"* **Harvard Business Review, September–October 1990** |
| **Underlying data** | 85% in one bank branch system, 50% in an insurance brokerage, 30% in an auto-service chain |

The "95%" figure is a decades-old misquote that propagated across marketing blogs until it
became the version everyone repeats. **Isaiah's book should use 25–85% and cite Reichheld &
Sasser 1990 directly** — or better, skip it. It is **36 years old**, drawn from bank branches
and auto shops in the late 1980s, and it says nothing about a 2026 local-service agency.

There's an opportunity here. Getting this right is cheap credibility: a reader who has seen
"25–95%" in ten guru courses and sees the correctly sourced number in Isaiah's book learns
something about how carefully the rest of it was written.

### ✅ VERIFIED — safe to cite

**Lead response time — the strongest statistic in the entire source set**

- **Claim:** contact within an hour → ~7x more likely to qualify the lead than an hour later;
  **60x** more likely than waiting 24+ hours.
- **Original:** James B. Oldroyd, Kristina McElheran & David Elkington, *"The Short Life of
  Online Sales Leads,"* **Harvard Business Review 89, no. 3 (March 2011).**
- **Sample:** audited **2,241 US companies.** Real peer-reviewed-adjacent research with a
  named methodology, not a vendor blog post.
- **Verdict:** cite it, name the authors and the year. **Flag the age** — 2011 predates
  widespread SMS-first lead handling. Isaiah's own speed-to-lead numbers would be a stronger
  proof point if he has them.

### ⚠️ USE WITH CAUTION — vendor research, and the framing is loose

**Velocify 391%**

- **As printed:** "A 391% increase in sales conversions occurs when leads are contacted within
  the first 60 seconds." (Lead Nurture p.17)
- **What the study found:** calling within **1 minute** vs. **at 2 minutes** → 391% higher
  conversion. At 2 minutes it's 160%, at 3 minutes 120%. The comparison is minute-one against
  minute-two, *not* against "later" in general.
- **Source:** Velocify, "Insurance Industry Online Buyer Experiences," ~May 2014, analyzing
  3.5M+ leads. Vendor-published; Velocify sold lead-response software.
- **Verdict:** if used, state the actual comparison and name Velocify and the year. Do not
  round it into "391% more conversions if you call fast."

**Profitwell / 512 companies**

- **Claim:** a 1% improvement in pricing beats a 1% improvement in retention or acquisition;
  pricing is the #1 growth lever.
- **Status:** the study is real — Profitwell compared acquisition, retention, and monetization
  across **512 companies** and found monetization (pricing) the highest-impact lever at equal
  relative improvement. The **specific "2x retention / 4x acquisition" ratios need the original
  chart** before being printed as fact.
- **Note:** Profitwell was acquired by **Paddle** in 2022. Cite as "Profitwell (now Paddle)."
- **Bigger caveat:** the dataset is **SaaS subscription companies.** Isaiah's readers run local
  service agencies. The directional lesson survives; the ratios shouldn't be presented as
  applying to a landscaping retainer.

### ❌ NOT VERIFIED — do not print

| Statistic | Attributed to | Problem |
|---|---|---|
| 78% buy from whoever responds first | Lead Connect | Vendor claim, no locatable primary study |
| Average first response = 42 hours | InsideSales.com | Company rebranded to XANT then dissolved; original study not locatable |
| 1.3 average attempts; 44% quit after one | InsideSales / RAIN Group | Two different sources merged into one claim |
| Hubspot 7x email ROI after segmenting | Hubspot | No locatable primary source |
| Costs 5x–25x more to acquire than retain | "HBR" | Attribution is vague in the source; this is folk wisdom with no single citable study |
| Average gym runs 12.5% net margins | none given | No source in the PDF |
| 78% of businesses are service businesses | none given | No source in the PDF |

**Recommendation: cut all seven.** None are load-bearing. A book that cites two rock-solid
studies reads as more credible than one that sprays nine shaky ones. And every one of these
is the kind of stat a skeptical reader can fail to find in thirty seconds of searching.

---

## Part 2 — Compliance research

> **Not legal advice.** This is research to make the book accurate. Isaiah must have a licensed
> Massachusetts attorney review every contract template, consent flow, and compliance claim
> before the book ships.

### TCPA — the ground moved, and the playbooks predate it

The source PDFs say only "follow the laws in your area." That's useless to a reader about to
send 4,000 texts. Here's the actual current state, and it changed **twice** since those books
were written:

| Date | What happened |
|---|---|
| **Jan 24, 2025** | The Eleventh Circuit **vacated the FCC's "one-to-one consent" rule** in *Insurance Marketing Coalition v. FCC* — holding the FCC exceeded its authority by redefining prior express written consent. The rule had been due to take effect days earlier |
| **Apr 11, 2025** | Text-message **opt-out / revocation rule took effect** — revocation must be honored, and honored promptly |
| **Aug 29, 2025** | FCC **reinstated the prior "prior express written consent" standard** following the vacatur |
| **Jan 2026** | FCC **delayed the broader "revocation-all" requirement** — which would treat one opt-out as revoking consent across all of a sender's messaging purposes and channels — **until January 31, 2027** |

**Why this matters to the book:** that January 2027 date lands during the book's shelf life.
Any chapter covering SMS consent needs to be written with that change coming, and dated
explicitly so a reader in 2028 knows to re-check. The lead-gen offer Isaiah sells lives or
dies on this.

### A2P 10DLC — the operational detail no free video covers well

Mandatory. **Since February 2025 all major carriers block unregistered A2P traffic outright.**
Not throttled — blocked.

| Item | Current |
|---|---|
| Brand registration | ~$4 sole proprietor; **$48+ standard brand** (includes secondary vetting) |
| Campaign registration | ~**$15–17 per campaign** vetting fee; $15 per additional campaign under the same brand |
| Monthly campaign fee | **$1.50–$10 per campaign per month**, varies by use case |
| Carrier surcharges | **$0.003–$0.005 per SMS** (AT&T, T-Mobile, Verizon) |
| Brand approval time | **1–3 business days** |
| Campaign approval time | **3–7 business days**; **10–15 during high-volume periods** |

Registration requires EIN, use case, **sample messages, and proof of opt-in.**

**This is a chapter on its own.** It's unglamorous, it's where beginners get blocked for weeks,
and it's exactly the "cannot get this from a free YouTube video" material the mission calls
for. **`[GAP]` — Isaiah's own registration story (what got rejected, how long, what he'd
change) would make this the best chapter in the book.**

### Massachusetts recording law — the dossier's framing needs a small correction

The dossier calls this "Massachusetts two-party consent." That's the common shorthand, but
**M.G.L. c. 272 § 99 is technically an anti-*secret*-recording statute**, and the distinction
changes what a reader has to do.

- § 99(B)(4) defines "interception" as to **secretly** hear or record a wire or oral
  communication. **"Secretly" is the operative element of every offense under the statute.**
- Practical effect: if every party **knows** the recording is happening, there's no violation.
  An announcement at the top of the call — including an automated "this call may be recorded"
  — puts parties on notice and satisfies it.
- **Penalties are severe: a felony, up to 5 years in state prison and a $10,000 fine**, plus
  civil damages.
- **Interstate:** Massachusetts law governs recordings made in-state regardless of where the
  other party sits. The federal one-party-consent baseline does not save you.

**Why it matters here:** Isaiah's own field — recorded sales calls, GoHighLevel call tracking,
AI call handling — sits directly on this statute. And the Hormozi scripts include the line
"calling from XYZ on a recorded line," which is the right instinct. Worth teaching *why* that
line exists, not just to copy it.

### M.G.L. c. 93A — the one that bites agencies

- Prohibits **unfair or deceptive acts or practices** in trade or commerce. Covers services.
- **§ 9** = consumer claims. **§ 11** = **business-to-business** claims. An agency's client is
  a business, so **§ 11 is the live exposure.**
- **A written demand letter is a prerequisite** for consumer claims, with a **30-day** window
  to make a reasonable settlement offer.
- **Up to treble damages plus attorney's fees** where the violation was willful or knowing, or
  where relief was refused in bad faith.

**Direct implication for the book:** overpromising results in a proposal isn't just bad
practice in Massachusetts, it's a statute with a damages multiplier attached. This is the
strongest possible argument for the book's own no-income-claims rule — and it's an argument
Isaiah can make to his *readers* about their own client proposals. That's a chapter hook.

### FTC Endorsement Guides — revised, effective July 26, 2023 (16 CFR Part 255)

- **Material connections** between endorser and advertiser must be disclosed.
- Testimonial claims **must be truthful and represent typical results.**
- **"Clear and conspicuous"** means *difficult to miss and easily understandable by ordinary
  consumers* — unavoidable, standing out by color, font, size, location, duration, speed.
- The definition of "endorsement" was **broadened** to cover tags, reviews, social media
  mentions, virtual influencers, fake reviews, and organizational seals.

**Two implications.** First, for Isaiah's own book: any testimonial he prints, and any results
he describes, falls under this. Second, and more useful, it's teachable material — his readers
will be running ads and collecting testimonials for clients, and "represent typical results"
is precisely the rule agencies break by accident.

---

## What this changes in the build

1. **Cut seven unverifiable statistics.** Keep two well-sourced ones. Fewer, stronger.
2. **Fix the retention number to 25–85%** and cite Reichheld & Sasser 1990 — or drop it for
   Isaiah's own churn data.
3. **A2P 10DLC earns a full chapter**, not a bullet in a compliance appendix.
4. **Compliance chapter must be dated in-text** ("as of [month/year]") because TCPA is actively
   moving and the revocation-all rule lands January 31, 2027.
5. **Correct the "two-party consent" shorthand** to the secrecy standard — it's more accurate
   and easier for a reader to actually comply with.
6. **93A § 11 becomes the spine of the contracts chapter.** Treble damages is the reason the
   templates matter, and it's a better motivator than "be professional."

## Sources

- [HBR, "The Short Life of Online Sales Leads" (Oldroyd, McElheran, Elkington, March 2011)](https://hbr.org/2011/03/the-short-life-of-online-sales-leads)
- [HBR, "Zero Defections: Quality Comes to Services" (Reichheld & Sasser, Sept–Oct 1990)](https://hbr.org/1990/09/zero-defections-quality-comes-to-services)
- [Velocify insurance lead-response study (PR Newswire, May 2014)](https://www.prnewswire.com/news-releases/biggest-insurance-companies-keep-their-customers-waiting-velocify-study-finds-258281391.html)
- [Eleventh Circuit vacates FCC one-to-one consent rule (Venable)](https://www.venable.com/insights/publications/2025/01/eleventh-circuit-overrules-fccs-one-to-one)
- [FCC repeals one-to-one consent rule following Eleventh Circuit (Womble Bond Dickinson)](https://www.womblebonddickinson.com/us/insights/blogs/fcc-repeals-one-one-consent-rule-following-eleventh-circuit-decision)
- [TCPA in 2026: consent, revocation, litigation status](https://compliancehub.wiki/tcpa-2026-consent-revocation-one-to-one-rule-vacated-compliance/)
- [A2P 10DLC fees — GoHighLevel support](https://help.gohighlevel.com/support/solutions/articles/155000005200-a2p-10dlc-messaging-fees-registration-monthly-and-carrier-costs)
- [A2P 10DLC registration guide 2026](https://hexalevel.com/a2p-10dlc-registration-guide-2026/)
- [Massachusetts recording law — Digital Media Law Project](http://www.dmlp.org/legal-guide/massachusetts-recording-law)
- [Massachusetts recording laws 2026](https://www.recordinglaw.com/party-two-party-consent-states/massachusetts-recording-laws/)
- [The Massachusetts Consumer Protection Law — Mass.gov](https://www.mass.gov/info-details/the-massachusetts-consumer-protection-law)
- [Chapter 93A § 11 in business litigation — Nelson Mullins](https://www.nelsonmullins.com/insights/insights/the-double-edged-sword-of-chapter-93a-section-11-in-massachusetts-business-litigation)
- [FTC Endorsement Guides, Federal Register, July 26 2023](https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising)
- [FTC's Endorsement Guides: What People Are Asking](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking)
