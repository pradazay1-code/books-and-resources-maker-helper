# SMS & Email Nurture Sequences
> **From The OneVision Playbook** by Isaiah Wright · onevision asset vault
> Fill this in. Do not retype it out of the book.

**Chapter 13 · Stage 5 → 6**

> ⚠️ **Compliance first.** SMS requires A2P 10DLC registration (asset 13) *and* documented consent (asset 21). Those are two different things. Registration gets your messages delivered; consent gives you the right to send them.

### Speed-to-lead — fires on submission

```
[0 min · SMS from the business number]
Hey {{first_name}} — {{business_name}} here. Saw you asked
about {{service}}. Are you looking to get this done in the
next couple weeks or further out?

[0 min · Owner notification — push + SMS]
New lead: {{first_name}}, {{service}}, {{phone}}

[2 min · Email]
Subject: your {{service}} request
Hi {{first_name}} — thanks for reaching out about
{{service}}. Easiest way to get you a quote is a quick
visit. Here are our next openings: {{booking_link}}

[5 min · No reply → automated call attempt]

[15 min · Still nothing → task to a human]

[1 hr · SMS, different angle]
{{first_name}} — one thing that helps us quote accurately:
roughly how big is the {{job_descriptor}}? Happy to give
you a ballpark before anyone comes out.

[Day 1 · SMS]
Still want us to take a look at the {{service}}?

[Day 3 · SMS — final]
No worries if the timing isn't right. I'll stop here —
just reply anytime if you want to pick it back up.
{{business_name}}

→ then long-term nurture
```

**STOP RULE:** any reply halts the whole sequence immediately and hands to a human. Build it, then test it by replying to your own test lead.

### Appointment reminders

```
[On booking · SMS]
You're booked, {{first_name}} — {{day}} {{time}} with
{{rep_name}} from {{business_name}}. We'll be calling from
{{phone_number}}. Reply RESCHEDULE if you need a different time.

[24 hrs out · SMS — automated, and say so]
Automated reminder: {{business_name}} tomorrow at {{time}}.
Reply RESCHEDULE if anything's changed.

[3 hrs out · SMS]
Today at {{time}} — see you then. {{reschedule_link}}

[Day of · from a real number, written like a person]
Hey {{first_name}}, {{rep_name}} here — heading your way at
{{time}}. Anything I should know before I get there?
```

**Two details that matter more than they look:**
1. **Say the number you'll call from.** Pickup on unknown numbers is terrible; this fixes a chunk of it.
2. **Make rescheduling one tap.** Friction converts live opportunities into no-shows.

### Long-term nurture

Monthly, low-pressure, genuinely useful. Seasonal timing does most of the selling.

```
[Monthly · SMS or email]
{{seasonal_hook}} — {{one_useful_thing}}. If you're thinking
about {{service}} this {{season}}, we've got openings.
{{booking_link}}
```

### Compliance checklist before any of this goes live

- [ ] A2P 10DLC brand and campaign approved
- [ ] Consent recorded: what the form said, when, from where
- [ ] Consent checkbox not pre-ticked
- [ ] STOP honored immediately and across **all** sending, not just this sequence
- [ ] HELP returns business name and contact
- [ ] Automated messages identified as automated
- [ ] Client's list interrogated before use — how collected, when, what they agreed to
