# Escalation Playbook

> **Category**: escalation  
> **Audience**: agent  
> **Last updated**: 2026-01-15

This playbook defines **how** to escalate a customer interaction — what 
information to gather, how to hand off, what to tell the customer, 
and how to document. It complements 
[Escalation Criteria](./escalation_criteria.md) (which defines **when** 
to escalate).

**Audience**: internal — AI assistant logic, Tier 1 agents, Tier 2 
agents.

## Purpose

A well-executed escalation is invisible to the customer. They feel 
heard, informed, and confident their issue is being handled — even 
though they're being handed between systems or teams.

A poorly-executed escalation frustrates the customer twice: once for 
the original issue, again for the handoff.

This playbook ensures every escalation is smooth, complete, and 
traceable.

## The Escalation Process — 6 Steps

Every escalation follows the same 6 steps:

1. **Recognize** — detect the escalation trigger (see 
   [Escalation Criteria](./escalation_criteria.md))
2. **Reassure** — tell the customer what's happening and why
3. **Gather** — collect all information needed for the handoff
4. **Summarize** — write a clear internal summary
5. **Route** — assign priority and route to the correct team
6. **Confirm** — tell the customer what to expect next

Skipping any step causes friction. Do them all.

## Step 1: Recognize

Refer to [Escalation Criteria](./escalation_criteria.md) for the full 
list of triggers. In practice, escalations are recognized in four ways:

### 1a. Explicit request
Customer asks for a human. **Escalate immediately, no questions.**

### 1b. Trigger match
Any of the 15 AI triggers or 14 Tier 1 triggers is met. Check the 
criteria document.

### 1c. AI uncertainty
The AI cannot confidently answer. Rule of thumb:

- 2 consecutive "I don't know" responses → escalate
- Confidence score below threshold → escalate
- Contradictory KB docs → escalate

### 1d. Agent judgment
Tier 1 agent recognizes the case is beyond their authority or 
expertise. Trust your instinct — escalate.

## Step 2: Reassure the Customer

**Never** hand off without telling the customer first.

### The three things to communicate

1. **What's happening**: "I'm connecting you with a specialist who 
   can help with this."
2. **Why**: "This is a case that our [X] team handles directly."
3. **What to expect**: "You'll hear back within [time] via [channel]."

### Sample handoff messages

**AI → Tier 1 (routine)**
> "I want to make sure you get the best help with this. I'm 
> connecting you with a support specialist who can take it from here. 
> You'll receive a response within 24 hours by email."

**AI → Tier 1 (urgent)**
> "This is something we take very seriously. I'm escalating this to 
> our specialist team right now — they'll reach out within 4 business 
> hours. In the meantime, please [safety instruction if applicable]."

**AI → Tier 1 (safety)**
> "Please stop using the product immediately. I'm escalating this to 
> our safety team right now as a priority. They'll reach out within 
> 4 business hours."

**Tier 1 → Tier 2 (internal handoff)**
> Customer isn't told about the tier. To the customer: "I've reviewed 
> your case with our specialist team. Here's what happens next..."

**Handling "why can't you help me?"**
> "Our specialist team has access to systems and authority that I 
> don't. They can resolve this faster than I can."

**Handling "I don't want to be transferred again"**
> "I understand. This is the last handoff — a specialist will own 
> this until it's fully resolved."

### What NOT to say

- ❌ "I can't help with that" → "Let me connect you with someone who can."
- ❌ "That's not my department" → "This is best handled by our [team]."
- ❌ "You'll need to call/email separately" → "I'm forwarding your case."
- ❌ "They might be able to help" → "They will help."
- ❌ "You should have..." → Never blame the customer.

## Step 3: Gather Information

Before handing off, collect everything the next team needs. **A handoff 
without information wastes everyone's time.**

### Required information (all escalations)

- **Customer name** (as on account)
- **Account email**
- **Order ID(s)** if applicable (format: `ORD-XXXXXX`)
- **Issue description** — 1–3 sentences
- **What the customer has already tried**
- **What they're asking for** (specific outcome)
- **Escalation trigger** (which criteria triggered the escalation)

### Additional info by trigger type

| Trigger | Additional info needed |
|---|---|
| Payment dispute (A4) | Order ID, charge amount, date, last 4 of card |
| Account compromise (A5) | Suspicious activity details, timeline |
| Product safety (A6) | Product SKU, purchase date, incident description, photos if available |
| Legal threat (A7) | Exact wording of threat, context |
| Privacy request (A8) | Specific data requested, verification status |
| Bulk/B2B (A9) | Volume, timeline, business name |
| Policy exception (A10) | Specific policy, reason, history |
| Vulnerable customer (A13) | Communication preferences, accommodations |
| Fraud (B6) | IP, account patterns, evidence |
| Reputational (B8) | Platform mentioned, threat content |
| International (B12) | Country, customs status, tracking |

### Information to NEVER collect or share

- Full card numbers (only last 4 digits)
- CVV codes
- Passwords
- 2FA codes
- Full SSN or government IDs
- Full bank account numbers

## Step 4: Summarize

Write a clear, complete, scannable internal summary. The next team 
should understand the entire situation in **under 60 seconds**.

### Summary template
ESCALATION SUMMARY
==================
Customer: [Name] ([email])
Account age: [X months/years]
Order(s): [IDs if relevant]
Priority: [URGENT / HIGH / STANDARD]
Trigger: [A# or B# from criteria]

ISSUE
[1-3 sentence description]

CUSTOMER REQUEST
[What outcome they want]

WHAT'S BEEN TRIED

[Step 1]

[Step 2]

RECOMMENDED RESOLUTION
[Your best guess at the right outcome — helps Tier 2 decide faster]

NOTES
[Any emotional context, vulnerability, prior escalations]


### What makes a good summary

- **Specific** — actual order IDs, dates, amounts
- **Scannable** — bullet points, not paragraphs
- **Complete** — no gaps the next agent has to fill
- **Neutral** — describe the situation, don't editorialize
- **Actionable** — includes a recommendation

### What makes a bad summary

- ❌ "Customer has a problem with their order"
- ❌ "Customer is angry" (without context)
- ❌ "Please help" (vague)
- ❌ Walls of text with no structure
- ❌ Missing order IDs
- ❌ Editorializing ("customer is being difficult")

## Step 5: Route

Assign priority and route to the correct team.

### Priority assignment

Match against [Escalation Criteria](./escalation_criteria.md):

| Priority | Triggers | SLA |
|---|---|---|
| **URGENT** | A2 (threats), A5 (compromise), A6 (safety), A7 (legal) | 4 business hours |
| **HIGH** | A4 (disputes), A11 (multi-issue), B6 (fraud), B8 (reputational) | 1 business day |
| **STANDARD** | All others | 2 business days |

**When in doubt, choose the higher priority.** It's better to 
over-prioritize than to leave a safety or legal case in a standard 
queue.

### Routing table

| Trigger type | Route to |
|---|---|
| Payment, orders, general | Tier 1 → Tier 2 if needed |
| Legal (A7, B5) | Tier 2 → legal@voltnest.com |
| Privacy (A8) | privacy@voltnest.com |
| Accessibility (B14) | accessibility@voltnest.com |
| Business/wholesale (A9) | partners@voltnest.com |
| Safety (A6, B9) | Tier 2 immediately, same-day |
| Security (A5, B4) | Tier 2 with URGENT flag |
| Fraud (B6) | Tier 2 with evidence |

### Channel

Escalations are processed through our **support ticketing system** 
(Zendesk). Every escalation:

- Creates a ticket
- Links to the customer's account
- Links to any related orders
- Tags the trigger category
- Assigns priority
- Notifies the target team

**Never** escalate by forwarding the customer to a new email address. 
The customer stays in their existing thread; the ticket moves 
internally.

## Step 6: Confirm with the Customer

Close the loop. Tell the customer exactly what to expect.

### Confirmation template

> "I've escalated your case to our [team] team. Here's what happens 
> next:
> 
> 1. You'll receive a response within [SLA time].
> 2. The response will come to [email/chat/phone].
> 3. Your case number is [case #].
> 
> If you need to follow up before then, reply to this thread or email 
> support@voltnest.com with your case number."

### What the customer needs to know

- ✅ What's happening (escalated)
- ✅ When they'll hear back (specific time)
- ✅ How they'll hear back (channel)
- ✅ A reference number (case #)
- ✅ How to follow up

### What the customer does NOT need to know

- ❌ Internal team names ("Tier 2", "specialist pod 3")
- ❌ Agent names beyond the first
- ❌ Internal systems (Zendesk, Stripe dashboard)
- ❌ SLA breach risk or internal pressures
- ❌ Why the AI couldn't handle it (technical details)

## Handling Edge Cases During Escalation

### Customer refuses to be escalated
> "I understand. Let me try once more to resolve this directly." 
> Attempt one more resolution path. If it fails, escalate anyway and 
> explain: "I've done everything I can from here — the specialist 
> team has tools I don't have."

### Customer demands a specific person
> "I can't guarantee a specific person, but I can escalate this to 
> the team that handles [issue type]. They'll have full context."
> Do not promise a specific human. Do not give internal names.

### Customer threatens legal action during escalation
- Do NOT discuss the threat
- Do NOT admit or deny fault
- Escalate as URGENT
- Document the exact threat wording
- Route to legal@voltnest.com

### Customer is hostile or abusive
- Stay professional and calm
- Do not match tone
- Escalate to Tier 2 with a note about the interaction
- If abuse continues after escalation, Tier 2 may end the conversation

### Customer provides incorrect information
- Do not argue
- Escalate with what you have
- Note the discrepancies in the summary

### Customer is silent after escalation prompt
- Escalate anyway after 24 hours of no response
- Note "customer unresponsive" in the summary

## Communicating SLAs to the Customer

Use language that matches the SLA but avoids over-promising.

### URGENT (4 business hours)
> "You'll hear back within 4 business hours."

### HIGH (1 business day)
> "You'll hear back within 1 business day."

### STANDARD (2 business days)
> "You'll hear back within 2 business days."

### During peak seasons
> "You'll hear back within [X] — response times are slightly longer 
> during peak season."

Never say "shortly", "soon", or "as soon as possible". Always give a 
specific window.

## Documentation Requirements

Every escalation must be documented in the ticketing system with:

- ✅ Customer name and email
- ✅ Order ID(s) if applicable
- ✅ Trigger category (from criteria)
- ✅ Priority
- ✅ Summary (per template)
- ✅ Customer's desired outcome
- ✅ Recommended resolution
- ✅ Timestamp of escalation
- ✅ Assigned team
- ✅ SLA target

**Tickets without this documentation are rejected by Tier 2.** No 
exceptions.

## Special Handling by Trigger

### Product Safety (A6, B9)
1. **Instruct customer to stop using immediately** (if not already)
2. Escalate as URGENT
3. Include product SKU and purchase date
4. Request photos/video if customer can provide
5. Notify Tier 2 lead directly (Slack: #safety-escalations)
6. Document same-day

### Account Compromise (A5, B4)
1. Confirm suspicious activity (order, point redemption, login)
2. Escalate as URGENT
3. Recommend password reset + 2FA enablement immediately
4. Include timeline of suspicious events
5. Do not reveal account details until verification

### Legal Threats (A7, B5)
1. Do not respond to the legal substance
2. Escalate as URGENT
3. Forward exact wording to legal@voltnest.com
4. Notify Tier 2 lead directly
5. Preserve all communication (do not edit)

### Fraud Indicators (B6)
1. Do not confront the customer
2. Escalate to Tier 2 with evidence
3. Do not process any action on the account
4. Preserve all communication

### Vulnerable Customers (A13)
1. Escalate to Tier 1 immediately
2. Note accommodations needed
3. Do not rush
4. Prefer email over chat if they struggle with live chat
5. Route to a senior Tier 1 agent where possible

## Escalation Follow-Up

Once escalated, the original team **owns** the case until closure.

### Tier 1 responsibilities after escalation
- Monitor the ticket for updates
- Respond to Tier 2 requests for more info
- Do not close the ticket
- Do not re-escalate the same issue

### Tier 2 responsibilities
- Acknowledge the escalation within SLA
- Contact the customer with an interim update
- Resolve and close with documentation

### AI responsibilities (if in chat)
- Do not attempt to re-engage the customer after escalation
- Route any follow-up messages to the case
- Provide the case number if asked

## Metrics & Quality

Escalations are tracked on:

- **Escalation rate** — % of conversations escalated
- **Trigger distribution** — which triggers fire most often
- **Time to first response** — SLA compliance
- **Time to resolution** — total handling time
- **Customer satisfaction** — post-escalation CSAT
- **Re-escalation rate** — % of escalations escalated again
- **AI escalation accuracy** — % that truly needed escalation

Poor metrics trigger reviews:
- Re-escalation > 15% → coaching for Tier 1
- AI escalation > 40% of chats → KB or model tuning
- CSAT < 4/5 after escalation → process review

## Common Escalation Mistakes

### ❌ Escalating without gathering info
The next team has to ask the customer everything again. Wastes time 
and frustrates the customer.

### ❌ Escalating without telling the customer
The customer waits, thinking the AI is still working. Then gets a 
random email.

### ❌ Escalating without a summary
Next agent has no context. Reads the entire chat history. Delays 
resolution.

### ❌ Wrong priority
A legal threat marked STANDARD sits in a queue for 2 days. Escalate 
higher when in doubt.

### ❌ Wrong team
A privacy request routed to support instead of privacy@. Legal 
compliance failure.

### ❌ Over-escalating
Escalating simple questions because they're annoying. Wastes Tier 1 
capacity and delays real escalations.

### ❌ Under-escalating
Trying to solve a legal or safety issue in chat. Risk to customer 
and company.

### ❌ Broken promises
Telling customer "you'll hear back in an hour" when the SLA is 24 
hours. Never over-promise.

## Related
- [Escalation Criteria](./escalation_criteria.md) — when to escalate
- [Sensitive Topics](./sensitive_topics.md) — special handling cases
- [Support Hours](../company/support_hours.md) — SLA windows
- [Contact VoltNest](../company/contact.md) — support channels
- [Mission & Values](../company/mission_values.md) — decision philosophy