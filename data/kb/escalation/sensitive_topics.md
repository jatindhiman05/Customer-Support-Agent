# Sensitive Topics

> **Category**: escalation  
> **Audience**: agent  
> **Last updated**: 2026-01-15

This document defines handling protocols for high-care customer 
situations — legal threats, safety incidents, mental health mentions, 
minors, harassment, discrimination, and media inquiries. These topics 
require specific language, routing, and documentation.

**Audience**: internal — AI assistant logic, Tier 1 agents, Tier 2 
agents.

**Golden rule**: When a sensitive topic appears, **stop normal 
resolution flow**. Follow the specific protocol below. Do not attempt 
to resolve the underlying issue in the same breath.

## Table of Contents

| Topic | Section |
|---|---|
| Legal threats & lawyer mentions | A |
| Product safety incidents | B |
| Self-harm or mental health mentions | C |
| Minors (under 18) | D |
| Abuse, coercion, or trafficking indicators | E |
| PII exposure (customer or agent error) | F |
| Sexual harassment | G |
| Discrimination complaints | H |
| Media, journalist, or influencer inquiries | I |
| Public figures & VIPs | J |
| Chargebacks & payment disputes | K |
| Regulatory or government inquiries | L |
| Whistleblower reports | M |

## General Principles for All Sensitive Topics

Before diving into specific protocols, internalize these:

### 1. Stop the normal flow
Do not continue attempting resolution. Sensitive topics require 
specialist handling, even if the original issue is simple.

### 2. Do not argue, defend, or explain
The instinct to justify company policy is exactly wrong here. 
Acknowledge, escalate, move on.

### 3. Preserve everything
- Do not edit the customer's messages
- Do not delete chat transcripts
- Do not "clean up" the ticket
- Preserve timestamps, screenshots, exact wording

### 4. Document with precision
Use exact quotes, not paraphrases. Note times, dates, and any 
screenshots.

### 5. Follow the protocol exactly
Each section below specifies:
- What to do
- What to say (and not say)
- Where to route
- What to document
- SLA

### 6. Do not act alone
Any sensitive topic goes to a supervisor or specialist. Tier 1 
should never resolve a sensitive topic independently.

## Section A: Legal Threats & Lawyer Mentions

### What qualifies
- Customer mentions a lawyer, attorney, or legal counsel
- Customer mentions suing, litigation, or small claims court
- Customer mentions a regulator (FTC, BBB, state AG, GDPR authority)
- Customer mentions a class action
- Customer threatens legal action in any form
- A legal notice, subpoena, or demand letter arrives
- Customer requests legal contact information

### What to do

1. **Do not engage with the legal substance**
   - Do not admit fault
   - Do not deny fault
   - Do not interpret policy for legal purposes
   - Do not offer to "make it right" if it could be construed as an 
     admission

2. **Acknowledge without agreeing**
   > "I understand. I'm going to route your message to the appropriate 
   > team."

3. **Escalate as URGENT** (4 business hours)
   - Trigger: A7 (from escalation_criteria.md) or B5
   - Priority: URGENT
   - Route: Tier 2 → legal@voltnest.com

4. **Preserve exact wording**
   - Copy the customer's message verbatim into the ticket
   - Do not paraphrase or summarize legal language
   - Note the timestamp

5. **Do not delete or edit anything**
   - Chat transcripts
   - Emails
   - Notes
   - Screenshots

### What NOT to say
- ❌ "I'm sure we can resolve this without lawyers"
- ❌ "That won't be necessary"
- ❌ "We're not liable for..."
- ❌ "Our policy says..."
- ❌ "You have no case"
- ❌ Any legal opinion

### What to say
- ✅ "I understand."
- ✅ "I'm routing this to the appropriate team."
- ✅ "You'll hear back within 4 business hours."
- ✅ "Your case number is [case #]."

### SLA
- **URGENT**: Response within 4 business hours
- **Legal review**: Within 1 business day
- **Response to customer**: Coordinated by legal team

### Documentation requirements
- Exact wording of the legal statement
- Timestamp
- All prior communication with customer
- Order/history context
- Any media the customer referenced

## Section B: Product Safety Incidents

### What qualifies
- Product caused injury (cut, burn, shock, etc.)
- Product caught fire or emitted smoke
- Product overheated to the point of danger
- Battery swelling, leaking, or rupture
- Child injury or near-injury involving a product
- Any product-related harm to a person or property
- Electrical shock from any VoltNest product

### What to do

1. **Prioritize the customer's safety**
   First message must instruct:
   > "Please stop using the product immediately and unplug it if safe 
   > to do so. Do not attempt to use it again."

2. **Do not diagnose the issue**
   - Do not ask "how did it happen?"
   - Do not discuss possible causes
   - Do not offer troubleshooting

3. **Escalate as URGENT — same day, direct to Tier 2**
   - Trigger: A6 or B9
   - Priority: URGENT
   - Route: Tier 2 immediately
   - **Notify Tier 2 lead via Slack (#safety-escalations)** 
     simultaneously

4. **Gather information (for the safety team)**
   - Customer name and contact
   - Product SKU and purchase date
   - Order ID
   - Description of incident
   - Photos or video if customer offers
   - Any medical treatment sought (do not ask for details)

5. **Offer replacement only through the safety process**
   - Do not commit to a refund, replacement, or compensation
   - The safety team determines resolution

### What NOT to say
- ❌ "That shouldn't happen"
- ❌ "You must have used it wrong"
- ❌ "The warranty doesn't cover..."
- ❌ "How did you break it?"
- ❌ "This is unusual" (implies fault)
- ❌ Any speculation about cause

### What to say
- ✅ "Please stop using the product immediately."
- ✅ "I'm escalating this to our safety team right now as a priority."
- ✅ "They'll reach out within 4 business hours."
- ✅ "Please keep the product and any packaging — our team may ask 
   for photos or for the item to be examined."

### SLA
- **URGENT**: Response within 4 business hours
- **Tier 2 involvement**: Same-day
- **Safety team contact**: Within 24 hours
- **Formal response**: Within 2 business days

### Documentation requirements
- Incident description (customer's words verbatim)
- Product SKU, purchase date, order ID
- Photos/video if provided
- Any injuries mentioned
- Whether medical attention was sought
- Any statements that could indicate fault (either way)

### If a customer claims injury
- Do NOT admit fault
- Do NOT offer medical advice
- Do NOT say "we'll cover medical costs"
- Do NOT say "we won't cover medical costs"
- Route to safety team + legal@voltnest.com simultaneously

## Section C: Self-Harm or Mental Health Mentions

### What qualifies
- Customer mentions self-harm or suicidal thoughts
- Customer mentions depression or a mental health crisis
- Customer mentions a recent loss, trauma, or emotional distress 
  (in a way that suggests acute distress)
- Customer's language suggests they are in crisis

### What to do

1. **Immediate response with empathy**
   > "I'm really glad you reached out. What you're going through 
   > sounds incredibly difficult. I'm going to connect you with a 
   > specialist who can support you and help with your VoltNest 
   > account."

2. **Do NOT attempt to counsel**
   - You are not a therapist
   - Do not give mental health advice
   - Do not ask probing questions about mental state
   - Do not suggest coping strategies

3. **Provide crisis resources** (in the US)
   > "If you're in crisis or thinking about harming yourself, please 
   > reach out to the 988 Suicide & Crisis Lifeline by calling or 
   > texting 988 (US). For emergencies, call 911."

   **Outside the US**: Direct to local emergency services or 
   https://www.befrienders.org

4. **Escalate to Tier 1 immediately, then Tier 2**
   - Priority: URGENT
   - Route: Senior Tier 1 agent → Tier 2
   - Note: Vulnerability flag on the case

5. **Do not abandon the conversation abruptly**
   - If in live chat, stay with the customer until they acknowledge 
     receipt of crisis resources
   - Do not close the chat abruptly
   - Hand off with warmth

### What NOT to say
- ❌ "Everything will be okay"
- ❌ "I'm sure things aren't that bad"
- ❌ "Have you tried..."
- ❌ "Let's focus on your order"
- ❌ Anything minimizing or problem-solving the emotion

### What to say
- ✅ "Thank you for telling me."
- ✅ "I'm here to help."
- ✅ "Let me connect you with a specialist."
- ✅ "Please reach out to 988 (US) if you need immediate support."

### SLA
- **URGENT**: Response within 4 business hours
- **Live chat**: Stay with the customer
- **Follow-up**: Within 1 business day

### Documentation requirements
- Note the vulnerability flag
- Do not over-document mental health details
- Note that crisis resources were provided
- Note the handoff to Tier 2

### After the interaction
If the conversation was distressing to the agent:
- Reach out to your team lead
- Take a break before the next case
- Support resources are available (see employee handbook)

## Section D: Minors (Under 18)

### What qualifies
- Customer identifies as under 18
- Customer's language or context suggests minor status
- Account appears to belong to a minor
- A parent contacts on behalf of a minor
- Orders placed by or for minors

### What to do

1. **Verify age policy**
   VoltNest requires users to be at least **13 years old**. Customers 
   under 18 require parental or guardian consent to place orders. 
   (See [Terms of Service](../policies/terms_of_service.md).)

2. **If the customer is 13–17**
   - Continue normal service
   - Do not ask intrusive personal questions
   - Do not lecture
   - Escalate to Tier 1 if account deletion or refund is requested 
     (parental rights involved)

3. **If the customer is under 13**
   - COPPA compliance issue
   - Do NOT continue the interaction
   - Escalate to Tier 2 immediately with subject "Minor Under 13 — 
     COPPA"
   - Route to privacy@voltnest.com

4. **If a parent contacts about a minor's account**
   - Verify parent identity (name, order ID, billing address)
   - Escalate to Tier 2 with verification
   - Do NOT disclose account information without verification
   - Route to privacy@voltnest.com

### What NOT to say
- ❌ "Where are your parents?"
- ❌ "You shouldn't be here"
- ❌ "You're too young for this"
- ❌ Anything condescending

### What to say
- ✅ "Thanks for reaching out. Let me help you."
- ✅ (If parent): "I'll need to verify some details before I can 
   discuss this account."

### SLA
- **COPPA cases**: 1 business day
- **Parental inquiries**: 2 business days
- **General minor support**: Standard SLAs

### Documentation requirements
- Note minor status (do not over-document)
- Note parental contact if applicable
- Note verification for parental requests
- Route to privacy@ if account deletion is involved

## Section E: Abuse, Coercion, or Trafficking Indicators

### What qualifies
- Customer's messages suggest they're being monitored or controlled
- Customer mentions a partner or family member managing their money 
  without consent
- Customer asks to hide communications from someone
- Customer's shipping address is being controlled by another party
- Customer shows signs of coercion or fear

### What to do

1. **Do not comment on the relationship**
   - Do not ask "is someone hurting you?"
   - Do not advise leaving
   - Do not offer to hide the order (could escalate danger)

2. **Escalate to Tier 2 immediately**
   - Priority: URGENT
   - Route: Tier 2 with a vulnerability flag
   - Note: Any indicators described, without interpretation

3. **Follow Tier 2 guidance for communication**
   - Tier 2 may move the conversation to a private channel
   - Do not override their instructions

4. **For orders being shipped to unsafe addresses**
   - Tier 2 decides. Do not attempt to intercept on your own.

### What NOT to say
- ❌ "Are you safe?"
- ❌ "Do you need me to call someone?"
- ❌ Anything that could be seen by an abuser
- ❌ Anything that could escalate risk

### What to say
- ✅ "I've noted your concern and I'm connecting you with a 
   specialist."
- ✅ "They'll follow up on the next step."

### SLA
- **URGENT**: Response within 4 business hours
- **Tier 2 lead notification**: Same day

### Documentation requirements
- Describe indicators factually (e.g., "customer asked to send 
  confirmation to a different email for safety reasons")
- Do not speculate or diagnose
- Do not share the case notes with the customer
- Flag case for restricted access

## Section F: PII Exposure (Customer or Agent Error)

### What qualifies
- A customer message includes another customer's data
- An agent accidentally sent PII to the wrong recipient
- A system error exposed personal data
- A customer received another customer's order confirmation
- Any accidental exposure of names, emails, addresses, payment info

### What to do

1. **Do not repeat the exposed data**
   - Never quote back the PII
   - Never forward it to another system
   - Do not screenshot it

2. **Escalate to Tier 2 immediately**
   - Priority: URGENT
   - Route: Tier 2 → privacy@voltnest.com
   - Note: "PII exposure"

3. **Ask the customer to delete the message** (if in their control)
   > "Thank you for letting us know. I'm escalating this immediately. 
   > Please delete the message you received for your own privacy."

4. **Do not confirm what was exposed**
   - Do not speculate about what the customer saw
   - Do not explain why it happened

### SLA
- **URGENT**: Response within 4 business hours
- **Privacy team**: Same day
- **Breach notification** (if applicable): Within 72 hours per 
  [Privacy Policy](../policies/privacy_policy.md)

### Documentation requirements
- What was exposed (specific categories: name, email, order ID, etc.)
- How it was exposed (customer message, agent error, system error)
- Who may have seen it
- Timestamp
- Immediate mitigation taken

## Section G: Sexual Harassment

### What qualifies
- Sexual comments, jokes, or advances toward an agent
- Unsolicited sexual images or descriptions
- Repeated inappropriate contact after being asked to stop
- Threats of a sexual nature

### What to do

1. **Do not engage with the content**
   - Do not comment on it
   - Do not laugh, joke back, or "play along"
   - Do not defend yourself

2. **Set a boundary once, professionally**
   > "I'm here to help with your VoltNest order. Let's continue 
   > with that, or I'll need to end this conversation."

3. **If behavior continues**
   - Escalate to Tier 2 with "harassment" flag
   - Tier 2 may end the conversation
   - Document everything

4. **If behavior is directed at a colleague**
   - Report to team lead immediately
   - Do not intervene with the customer

### What NOT to say
- ❌ "That's inappropriate"
- ❌ "How dare you"
- ❌ Anything matching the tone

### What to say
- ✅ "Let's keep this focused on your account."
- ✅ "I'll need to end this conversation if that continues."

### SLA
- **End the conversation** at Tier 2 discretion
- **Internal report**: Same day
- **Escalation**: URGENT if threatening

### Documentation requirements
- Exact quotes (necessary for HR/legal)
- Timestamp
- Whether the customer was warned once
- Team lead notified

### Support for the agent
- Report to team lead same day
- Access to employee assistance resources
- Case reassignment available on request

## Section H: Discrimination Complaints

### What qualifies
- Customer alleges they were discriminated against by VoltNest
- Customer alleges an agent treated them unfairly based on a 
  protected characteristic
- Customer's complaint involves race, gender, religion, disability, 
  national origin, age, sexual orientation, etc.
- Customer alleges differential pricing, service, or treatment

### What to do

1. **Do not dismiss or minimize**
   - Take every complaint seriously
   - Do not argue
   - Do not ask "are you sure?"

2. **Acknowledge professionally**
   > "Thank you for telling us. I'm escalating this to our team for 
   > review."

3. **Escalate to Tier 2 immediately**
   - Priority: URGENT
   - Route: Tier 2 → HR + Legal (via privacy@voltnest.com)
   - Note: "Discrimination complaint"

4. **Preserve all communication**
   - Do not edit
   - Do not delete
   - Screenshots, timestamps, exact wording

### What NOT to say
- ❌ "We don't discriminate"
- ❌ "I'm sure that wasn't the intent"
- ❌ "Our agents are trained to..."
- ❌ Any defensive language

### What to say
- ✅ "Thank you for telling us."
- ✅ "I'm escalating this to our team for review."
- ✅ "You'll hear back within 4 business hours."

### SLA
- **URGENT**: Response within 4 business hours
- **HR/Legal review**: Within 1 business day

### Documentation requirements
- Exact complaint wording
- Any specific incidents described
- Agent(s) involved (if identified)
- Timestamps
- Preservation of all communications

## Section I: Media, Journalist, or Influencer Inquiries

### What qualifies
- Someone identifies as a journalist, reporter, or media
- Someone requests an interview or comment
- Someone identifies as an influencer requesting partnership
- A blogger or YouTuber asking for review units
- A content creator asking for details about VoltNest practices

### What to do

1. **Do not answer on-the-record**
   - Do not confirm or deny anything
   - Do not provide quotes
   - Do not share internal processes

2. **Acknowledge and route**
   > "Thanks for reaching out. Media and partnership inquiries are 
   > handled by our communications team. I'll route this to them."

3. **Escalate to Tier 2**
   - Priority: HIGH (not URGENT unless safety-related)
   - Route: press@voltnest.com
   - Note: "Media inquiry — [outlet]"

4. **If the inquiry is about a sensitive incident**
   - Treat as URGENT
   - Route to Tier 2 + legal@voltnest.com
   - Do not comment

### What NOT to say
- ❌ "No comment" (implies something to hide)
- ❌ "I can't talk to you"
- ❌ Any substantive answer
- ❌ Confirmation of internal policies

### What to say
- ✅ "Thanks for reaching out."
- ✅ "I'll route your inquiry to the right team."
- ✅ "You'll hear back from our communications team."

### SLA
- **HIGH**: Response within 1 business day
- **Safety-related media**: URGENT

### Documentation requirements
- Outlet / publication
- Reporter name
- Specific topic
- Deadline mentioned (if any)
- Whether sensitive topic is involved

## Section J: Public Figures & VIPs

### What qualifies
- Customer identifies as a public figure
- Account shows unusual order patterns (very high value, PR 
  sensitivity)
- Customer is a known journalist, politician, or celebrity
- Customer's order could attract media attention

### What to do

1. **Continue normal service**
   - Do not treat differently unless verification of VIP status is 
     confirmed
   - Do not offer special treatment
   - Do not ask for autographs or photos

2. **If VIP status is confirmed or suspected**
   - Note in the case: "Potential public figure"
   - Escalate to Tier 2 for awareness
   - Do not disclose to other customers or externally

3. **If a VIP has a complaint**
   - Escalate as HIGH priority
   - Route to Tier 2 + communications team
   - Do not discuss publicly

### What NOT to say
- ❌ "I'm a huge fan"
- ❌ "Can I get a photo?"
- ❌ Anything unprofessional

### SLA
- **HIGH**: Response within 1 business day
- **Complaints**: Escalate to Tier 2 within 4 business hours

### Documentation requirements
- Nature of VIP status (confirmed or suspected)
- Any sensitivity
- Route to communications

## Section K: Chargebacks & Payment Disputes

### What qualifies
- Customer indicates they will file a chargeback
- Customer says they filed a chargeback
- Bank notifies us of a dispute
- Customer disputes a charge through their bank

### What to do

1. **Do not attempt to dissuade**
   - Do not say "you don't need to do that"
   - Do not offer deals to prevent a chargeback
   - Do not argue about the transaction

2. **Acknowledge**
   > "I understand. I'm routing this to the team that handles payment 
   > disputes."

3. **Escalate to Tier 2**
   - Priority: HIGH
   - Route: Tier 2 → finance@voltnest.com
   - Note: "Chargeback risk" or "Chargeback filed"

4. **Preserve all documentation**
   - Orders
   - Communications
   - Delivery confirmations
   - Tracking

### SLA
- **HIGH**: Response within 1 business day
- **Finance team**: Same day notification

### Documentation requirements
- Chargeback reason (if known)
- Order details
- Customer communications
- Delivery or service evidence

## Section L: Regulatory or Government Inquiries

### What qualifies
- Contact from any government agency
- Contact from a regulator (FTC, BBB, state AG, DPA)
- Subpoena or court order
- Tax authority inquiry
- Customs inquiry (international)
- Police inquiry

### What to do

1. **Do not answer any substantive questions**
   - Do not confirm or deny anything
   - Do not provide documents
   - Do not discuss the case

2. **Acknowledge professionally**
   > "I'm routing your inquiry to our legal team, who will respond 
   > through the appropriate channels."

3. **Escalate to Tier 2 immediately**
   - Priority: URGENT
   - Route: Tier 2 → legal@voltnest.com (direct)
   - Note: "Regulatory/government inquiry"

4. **Preserve everything**
   - All communications
   - Identity of the requester
   - Nature of inquiry
   - Timestamps

### What NOT to say
- ❌ Anything about the case
- ❌ "We'll cooperate fully" (implies commitment)
- ❌ "Our lawyer will call you" (route through legal, not direct)

### SLA
- **URGENT**: Legal team notified same day
- **Response**: Determined by legal team

### Documentation requirements
- Requester identity and agency
- Nature of inquiry
- Any deadlines mentioned
- All communications preserved

## Section M: Whistleblower Reports

### What qualifies
- Someone reports internal misconduct
- Someone reports fraud, safety, or ethical violations by VoltNest
- Someone reports policy violations by employees
- Someone reports environmental or labor issues

### What to do

1. **Take the report seriously**
   - Do not dismiss
   - Do not question motive
   - Do not promise anything

2. **Acknowledge**
   > "Thank you for reporting this. I'm routing it to the appropriate 
   > team."

3. **Escalate to Tier 2 immediately**
   - Priority: URGENT
   - Route: Tier 2 → legal@voltnest.com + HR
   - Note: "Whistleblower report"

4. **Preserve confidentiality**
   - Do not discuss with colleagues
   - Do not speculate
   - Do not share details outside the escalation chain

### SLA
- **URGENT**: Legal notified same day
- **Acknowledgment to reporter**: Within 2 business days

### Documentation requirements
- Reporter's identity (if provided — may be anonymous)
- Nature of report (verbatim if possible)
- Any evidence provided
- All communications preserved

## Cross-Cutting Rules

### When multiple sensitive topics overlap
Escalate at the **highest** applicable priority. Example: A legal 
threat + safety incident = URGENT with both flags.

### When unsure
**Always escalate.** A sensitive topic handled badly is worse than a 
sensitive topic handled slowly.

### Language and tone
Across all sensitive topics:
- Be calm
- Be brief
- Be specific
- Do not argue
- Do not explain
- Do not promise

### Preservation
- Never delete or edit sensitive communications
- Note timestamps exactly
- Screenshot where needed
- Store in restricted-access tickets

### Self-care (for agents)
Sensitive topics can be distressing:
- Take a break after difficult cases
- Talk to your team lead
- Use employee support resources
- Request case reassignment if needed

## Related
- [Escalation Criteria](./escalation_criteria.md) — when to escalate
- [Escalation Playbook](./escalation_playbook.md) — how to escalate
- [Support Hours](../company/support_hours.md) — SLA windows
- [Contact VoltNest](../company/contact.md) — support channels
- [Privacy Policy](../policies/privacy_policy.md) — data handling
- [Terms of Service](../policies/terms_of_service.md) — legal framework
- [Mission & Values](../company/mission_values.md) — decision philosophy