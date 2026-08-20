# Build Checklist
> **From The OneVision Playbook** by Isaiah Wright · onevision asset vault
> Fill this in. Do not retype it out of the book.

**Chapter 12 · Stage 5 — Build**

Build in order of dependency, not order of visibility.

### Build order

- [ ] **1 · A2P 10DLC brand + campaign submitted** — day one, blocks all SMS
- [ ] **2 · Sub-account, phone number, domain, email sending** — everything attaches here
- [ ] **3 · Calendar** — availability, duration, buffers. The appointment is the product
- [ ] **4 · Pipeline stages** — automations move contacts between them, so they exist first
- [ ] **5 · Intake** — forms, landing page, tracking number. Consent language lives here
- [ ] **6 · Speed-to-lead automation** — the highest-impact one
- [ ] **7 · Appointment reminders** — protects the show rate you're being paid for
- [ ] **8 · Long-term nurture** — matters later, least urgent now
- [ ] **9 · Reporting view** — the one screen the client looks at
- [ ] **10 · Test the whole path as a fake lead** — never skip

### Client-side pipeline

```
NEW              lead arrived, not yet contacted
CONTACTED        first touch out, no response
ENGAGED          they replied
APPOINTMENT SET  time on the calendar
SHOWED           they turned up
WON              client closed the job
LOST             disqualified, or gone cold  [+ REASON FIELD]
```

- [ ] **SHOWED is its own stage** — the gap between SET and SHOWED is your show rate
- [ ] **LOST has a reason field** — the pattern tells you more than anything else in the account

### Speed to lead

```
TRIGGER   form submitted / call missed / message received

  0 min    SMS to lead, from the business, personalized
  0 min    Notify owner — push and SMS
  2 min    Email to lead with the booking link
  5 min    No reply → automated call attempt
 15 min    Still nothing → task assigned to a human
  1 hr     Second SMS, different angle
  1 day    Follow-up
  3 day    Final touch → long-term nurture

STOP RULE  any reply halts the sequence immediately
           and hands to a human
```

- [ ] Fires **on submission**, not after a delay
- [ ] **Stop rule built and tested** by replying to your own test lead

### Conversation AI limits

- [ ] Escalation trigger built **before** the conversation flow
- [ ] Hands off on confusion, frustration, or complexity
- [ ] Never invents prices, availability, guarantees, or timelines
- [ ] Disclosure appropriate to current rules

### Test as a real lead

- [ ] Submit the form from your own phone, **on cellular, not at your desk**
- [ ] Every message arrived, and on time
- [ ] Reply mid-sequence → automation stopped
- [ ] STOP works
- [ ] Booking link produces a real calendar entry
- [ ] Owner notification arrived

### Then

- [ ] Save as a snapshot so the next build takes hours, not days
