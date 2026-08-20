<section class="chapter" id="ch12" data-part="Part Four — The Delivery Machine" markdown="1">
<div class="chap-head">
<span class="chap-num">12</span>
<span class="chap-stage">The Domino System · Stage 5 — Build</span>
<h1>The Build</h1>
<p class="chap-promise">By the end of this chapter you'll stand up a working client account in a defined order, and know which pieces must exist before you turn anything on.</p>
</div>

<div class="storyslot"><b>Story needed — cold open, 150–300 words</b>
The first build you did for a paying client. What broke. What you didn't know you needed until it was missing. How long it actually took versus what you told them.</div>

<div class="storyslot"><b>Author note — needs Isaiah's actual build</b>
This chapter gives the build order and the architecture, which transfer across any CRM. What it cannot supply is Isaiah's specific implementation: his real pipeline stage names, which automations fire on which triggers, how his Conversation AI is prompted and where it hands off to a human, and what's inside his snapshot. Those details are what make this chapter un-copyable. Replace the bracketed sections before publication.</div>

<div class="warn" markdown="1">
### On software interfaces
This book describes GoHighLevel because that's the platform this agency runs on, and the architecture below applies to any CRM with pipelines, automations, and a calendar. **Interfaces change constantly.** Menu names and click paths in any book about software are wrong within a year. What doesn't change is the order you build in and the reason for each piece — that's what this chapter is really about. Screenshots and exact paths, where included, are accurate as of the date noted.
</div>

## The principle

<div class="principle"><span class="label">The principle</span><p>Build in the order of dependency, not the order of visibility. The pieces that block other pieces go first, even when they show the client nothing.</p></div>

## Why most people get this wrong

They build the fun parts first.

Automations are satisfying. Dragging a workflow together and watching it fire feels like real progress. So that's where the first day goes — and then the whole thing sits idle for a week because messaging isn't registered, or because nobody defined what happens when a lead comes in at 8pm on a Saturday.

The other mistake is building something too complicated to hand over. If your client can't understand where a lead is in the process by glancing at one screen, you've built a system that requires you to interpret it — which means every question becomes a phone call, and your margin quietly disappears into support.

<p class="pull">A build the client can read is worth more than a build that's clever. You're not being paid for complexity. You're being paid for a full calendar.</p>

## The system

### Build order

<table>
<thead><tr><th>#</th><th>Step</th><th>Why here</th></tr></thead>
<tbody>
<tr><td><strong>1</strong></td><td>A2P 10DLC brand + campaign submitted</td><td>Runs on carrier time. Blocks all SMS. Day one, no exceptions</td></tr>
<tr><td><strong>2</strong></td><td>Sub-account, phone number, domain, email sending</td><td>Everything else attaches to these</td></tr>
<tr><td><strong>3</strong></td><td>Calendar — availability, duration, buffers</td><td>The appointment is the product. It gets defined before anything that books into it</td></tr>
<tr><td><strong>4</strong></td><td>Pipeline stages</td><td>Automations move contacts between stages, so the stages must exist first</td></tr>
<tr><td><strong>5</strong></td><td>Intake — forms, landing page, tracking number</td><td>The front door. Consent language lives here</td></tr>
<tr><td><strong>6</strong></td><td>Speed-to-lead automation</td><td>The single highest-impact automation. Built before the nurture sequences</td></tr>
<tr><td><strong>7</strong></td><td>Appointment reminders</td><td>Protects the show rate, which is what you're actually selling</td></tr>
<tr><td><strong>8</strong></td><td>Long-term nurture</td><td>Matters most later; least urgent on day one</td></tr>
<tr><td><strong>9</strong></td><td>Reporting view</td><td>The one screen the client looks at. Chapter 14</td></tr>
<tr><td><strong>10</strong></td><td>Test the whole path as a fake lead</td><td>Never skip. Never</td></tr>
</tbody>
</table>

### The client-side pipeline

This is the client's pipeline for *their* customers — different from your outreach pipeline in Chapter 7.

<div class="script">NEW              lead just arrived, not yet contacted
CONTACTED        first touch out, no response yet
ENGAGED          they replied
APPOINTMENT SET  time on the calendar
SHOWED           they turned up
WON              client closed the job
LOST             disqualified, or gone cold after full follow-up</div>

<div class="storyslot"><b>Replace with Isaiah's actual stage names</b>
The stages above are a sound generic architecture. Isaiah's real stage names, and any stage he added that isn't here, should replace them — including anything vertical-specific.</div>

Two things about this pipeline matter more than the names.

**SHOWED is its own stage.** Not folded into WON. The gap between APPOINTMENT SET and SHOWED is your show rate, and show rate is the number you're actually being paid to move. If you can't see it, you can't defend your invoice.

**LOST needs a reason field.** Six weeks in, the pattern in the lost reasons tells you more about what to fix than any other data in the account.

### Speed to lead is the whole game

If you build one automation properly, build this one.

The research here is solid and it's old enough to have been re-confirmed many times. A Harvard Business Review study of 2,241 US companies — Oldroyd, McElheran and Elkington, published in 2011 — found that firms attempting contact within an hour of an inquiry were about **seven times** more likely to qualify the lead than those trying an hour later, and more than **sixty times** more likely than those who waited a day.

That study is from 2011, which means it describes a world with less competition for attention than yours. The direction of the finding has not softened since.

So the first automation fires **immediately**. Not in five minutes. On submission.

<p class="script-label">Speed-to-lead — the shape</p>
<div class="script">TRIGGER   form submitted / call missed / message received

  0 min    SMS to lead, from the business, personalized
           with what they asked about
  0 min    Notify the owner - push and SMS
  2 min    Email to lead with the booking link
  5 min    If no reply: automated call attempt to the lead
 15 min    If still nothing: task assigned to a human
  1 hr     Second SMS, different angle
  1 day    Follow-up
  3 day    Final touch, then move to long-term nurture

STOP RULE  any reply from the lead halts the sequence
           immediately and hands to a human</div>

That stop rule is not optional. A lead who replies and keeps receiving automated messages knows exactly what happened, and it costs you the goodwill the speed just bought.

<div class="storyslot"><b>Replace with Isaiah's actual triggers and timings</b>
The cadence above is a reasonable architecture. His real intervals, channels, and branch conditions should replace it.</div>

### Conversation AI, and where it stops

Automated conversation handling is genuinely useful for the first exchange — answering at 11pm, qualifying, offering times. It is not useful for closing, for anything emotional, or for anything where being wrong is expensive.

Three rules worth building in:

**Hand off on any signal of confusion, frustration, or complexity.** If the lead asks something the AI can't answer confidently, it goes to a person. Build the escalation trigger before you build the conversation.

**Never let it invent specifics.** Prices, availability, guarantees, and timelines come from real data or they don't get said. An AI that improvises a price has created a problem your client will hear about.

**Disclose appropriately.** Rules on AI disclosure in customer messaging are tightening. Beyond the legal question, a customer who discovers they were misled about talking to a person is a review problem for your client.

<div class="storyslot"><b>Needs Isaiah's actual Conversation AI setup</b>
His prompt structure, his qualifying questions, his handoff triggers, and what he learned about where it breaks. This is one of the most valuable sections in the book and it can only come from him.</div>

### Snapshot it

Once you've built one account you're happy with, save it as a reusable template.

Every client after that starts from the snapshot and gets customized, rather than being built from nothing. That's the difference between a four-day build and a four-hour one — and it's the operational version of the same domino principle the whole book runs on. The first one costs everything; the tenth costs almost nothing.

<div class="storyslot"><b>Needs the contents of Isaiah's snapshot</b>
What's actually in it, what he leaves out on purpose, and what he learned to customize per client rather than templating.</div>

## Failure modes

<dl class="failure" markdown="1">
<dt>You build automations before registration is submitted.</dt>
<dd>Submit on day one and build while it processes. Reordering these two costs a week of the client's patience.</dd>
<dt>The speed-to-lead automation has a delay in it.</dt>
<dd>Fire on submission. Any delay you add is measurable money, and the first five minutes are worth more than the next five hours.</dd>
<dt>Automated messages keep sending after a lead replies.</dt>
<dd>Build the stop rule into every sequence and test it by replying to your own test lead. Assume it's broken until you've seen it stop.</dd>
<dt>There's no SHOWED stage.</dt>
<dd>Add it. Without it you cannot report on show rate, which is the number that justifies your fee.</dd>
<dt>You go live without testing as a real lead.</dt>
<dd>Submit the form from your own phone, on cellular, not on your desk. Follow it the whole way through and watch every message arrive.</dd>
<dt>The build is too complex for the client to read.</dt>
<dd>If explaining where a lead sits takes more than one sentence, simplify. You'll pay for the complexity in support calls forever.</dd>
</dl>

## The metric

<div class="metric" markdown="1">
### What to track in this stage
**Time from signature to first live lead.** The build's real output. Everything in this chapter exists to shorten it.

**Median speed to first contact.** Measured in seconds, not minutes. If it's creeping up, something in the automation is failing quietly.

**What "good" looks like:** first contact effectively instant, and a build you can reproduce from a snapshot in hours rather than days. The absolute time-to-live depends on how fast registration clears, which isn't yours to control — the part you own is that nothing else is waiting on you.
</div>

<div class="donow" markdown="1">
### Do this now
<span class="time">45 minutes</span>
Build the client-side pipeline in your own sub-account, using the seven stages above. Add a reason field on LOST.

Then build one automation, and only one: **speed to lead.** Trigger on form submission, immediate SMS to the lead, immediate notification to the owner, and the stop rule on reply.

Then test it as a real lead. Take out your phone, off wifi, and fill in the form like a stranger would. Watch what arrives and when.

Whatever you find broken in that test is the thing that would have broken in front of your first client.
</div>

</section>
