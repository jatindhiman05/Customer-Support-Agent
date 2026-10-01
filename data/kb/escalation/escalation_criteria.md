# Escalation Criteria

> **Category**: escalation  
> **Audience**: agent  
> **Last updated**: 2026-01-15

This document defines **when** to escalate a customer interaction from 
the VoltNest AI assistant to a human agent, and from Tier 1 to Tier 2 
support. Escalation criteria are non-negotiable — when any trigger in 
this document is met, escalation happens.

**Audience**: internal — AI assistant logic, Tier 1 agents, Tier 2 
agents.

## Purpose

Escalation exists to protect:

1. **The customer** — complex issues deserve human judgment
2. **The business** — sensitive situations require trained handling
3. **Compliance** — legal, safety, and regulatory issues need oversight
4. **Quality** — the AI should not attempt what it can't do well

**Rule**: When in doubt, escalate. A false positive costs minutes; a 
false negative can cost a customer or a legal case.

## Escalation Levels

VoltNest has three support levels:

| Level | Who | Handles |
|---|---|---|
| **AI Assistant** | AI (24/7) | Routine questions, order status, policies, tracking |
| **Tier 1** | Human agent | Complex issues, ambiguity, first-level problem solving |
| **Tier 2** | Specialist agent | Investigations, approvals, sensitive cases, system access |

Escalation moves **upward**: AI → Tier 1 → Tier 2.

De-escalation (Tier 2 → Tier 1) is rare and requires Tier 2 approval.

## AI → Tier 1 Escalation Triggers

The AI must escalate when **any** of the following is true.

### Trigger A1: Explicit Request for a Human

The customer asks for a human in any phrasing:

- "Talk to a human"
- "I want to speak to a real person"
- "Agent"
- "Representative"
- "Supervisor"
- "Manager"
- "Get me someone who can actually help"
- "You're not helping — is there a real person?"

**Action**: Escalate immediately, no further questions. Do not 
attempt to solve the problem first.

### Trigger A2: Customer Emotion Signals

The customer is expressing strong emotion:

- Anger or frustration ("This is ridiculous", "I'm furious")
- Repeated all-caps or profanity
- Threats of legal action ("I'll sue")
- Threats to post on social media or review sites
- Threats to contact a regulator or consumer protection agency
- Statements suggesting emotional distress
- Excessive messaging (5+ messages in a row on the same issue)

**Action**: Escalate. Do not argue, do not defend policy, do not 
attempt to "calm down" the customer — hand off.

### Trigger A3: AI Confidence Too Low

The AI cannot find a reliable answer:

- No relevant KB documents found for the question
- KB documents contradict each other
- The customer's question is outside the KB scope
- The AI has said "I don't know" more than twice in the conversation
- The AI would need to make an assumption to answer

**Action**: Escalate with a summary of what was searched.

### Trigger A4: Payment or Financial Disputes

Any of the following requires human review:

- Customer disputes a charge
- Customer claims unauthorized charges
- Customer claims a refund was promised but not received
- Customer has been charged twice (posted, not pending)
- Customer requests a refund outside policy
- Customer disputes the amount of a refund
- Customer disputes currency conversion or customs charges
- Customer requests a partial refund or goodwill credit
- Customer reports they were charged after cancellation

**Action**: Escalate to Tier 1 with full order and payment details.

### Trigger A5: Account Security or Access Issues

Any of the following require human handling:

- Suspected account compromise
- Unauthorized order placed
- Unauthorized loyalty point redemption
- Lost 2FA device AND lost backup codes
- Lost access to account email
- Deletion request from a customer who can't verify identity
- Multiple failed login attempts beyond a lockout
- Customer reporting they received a 2FA code they didn't request

**Action**: Escalate to Tier 1 immediately. If compromise is 
confirmed or suspected, flag as **URGENT** (4-business-hour SLA).

### Trigger A6: Product Safety Concerns

Any of the following are safety-critical:

- Product overheating (hot to the touch)
- Burning smell or smoke from any product
- Product swelling or deformation (especially batteries)
- Electrical shock or spark from a product
- Any injury allegedly caused by a VoltNest product
- Child safety concern (e.g., small parts, choking)
- Product catching fire (or nearly catching fire)

**Action**: Escalate to Tier 1 **and** flag as **URGENT** 
(immediate Tier 2 handoff). Do not attempt to diagnose. Instruct the 
customer to stop using the product immediately.

### Trigger A7: Legal or Regulatory Threats

Any of the following require legal-aware handling:

- Customer mentions a lawyer or attorney
- Customer mentions filing a lawsuit
- Customer mentions a regulator (FTC, BBB, consumer protection, GDPR 
  authority)
- Customer mentions small claims court
- Subpoena, court order, or legal notice received
- Customer asks for legal contact
- Customer mentions a class action
- Customer requests a formal legal response

**Action**: Escalate immediately to Tier 2. Do not respond to legal 
claims. Do not admit fault. Do not discuss legal matters.

### Trigger A8: Data Privacy Requests

Any of the following require privacy-team handling:

- GDPR/CCPA data access request (DSAR)
- Data deletion request where identity can't be verified
- Request to correct personal data
- Request to restrict processing
- Request to export data in a specific format
- Complaint about data handling
- Breach inquiry

**Action**: Escalate to Tier 1 → route to privacy@voltnest.com.

### Trigger A9: Bulk or Business Requests

Any of the following:

- Order of 10+ items or $500+ value with questions
- Wholesale or B2B inquiry
- Corporate gifting request
- Custom packaging request
- Bulk pricing negotiation
- Reseller authorization request

**Action**: Escalate to Tier 1 → route to partners@voltnest.com.

### Trigger A10: Policy Exceptions

Customer requests something outside published policy:

- Return after 30-day window (exceptional circumstance claimed)
- Warranty claim after 12 months
- Refund to a different payment method
- Refund for gift-card-purchased item as cash
- Address change after delivery
- Late cancellation after shipping
- Price match outside 14-day window
- Custom or altered product replacement

**Action**: Escalate to Tier 1. Only Tier 2 can approve policy 
exceptions.

### Trigger A11: Multi-Issue Complexity

The conversation involves multiple complex issues:

- Customer has 3+ distinct issues in one conversation
- Issues span multiple categories (payment + shipping + warranty)
- Issues require coordinated resolution across teams
- Customer has been escalated before on a related issue

**Action**: Escalate to Tier 1 with a summary of all issues.

### Trigger A12: Technical Failures in the AI System

The AI itself encounters problems:

- Unable to complete an order lookup
- Unable to retrieve tracking
- Unable to access policy documents
- Repeated errors or timeouts
- Output quality degraded (hallucination suspected)

**Action**: Escalate to Tier 1 with an error summary. Flag for system 
review.

### Trigger A13: Vulnerable Customers

Any indication the customer may be vulnerable:

- Customer mentions being elderly or having difficulty with technology
- Customer mentions a disability affecting communication
- Customer appears confused about basic account concepts
- Customer indicates language barrier (limited English)
- Customer indicates they are a minor (under 18)
- Customer appears to be in distress (see Trigger A2 for emotional 
  signals)
- Customer indicates they are being impersonated or coerced

**Action**: Escalate to Tier 1. Handle with extra care. Do not rush.

### Trigger A14: Ambiguous or Contradictory Requests

The customer's request is unclear or contradictory:

- Multiple conflicting requests in one message
- Request conflicts with previous statements
- Request that could be interpreted multiple ways
- Request that requires clarification the AI can't provide

**Action**: Escalate to Tier 1 rather than guessing.

### Trigger A15: Sensitive Personal Situations

Customer mentions:

- Death in the family (relevant to an order)
- Hospitalization
- Natural disaster
- Domestic violence situation
- Mental health crisis
- Any other traumatic event

**Action**: Escalate to Tier 1 immediately. Handle with empathy. Do 
not focus on policy — focus on the customer.

## Tier 1 → Tier 2 Escalation Triggers

Tier 1 must escalate to Tier 2 when **any** of the following applies.

### Trigger B1: Policy Exceptions Requiring Approval
Any exception to published policy requires Tier 2 approval:

- Refunds over **$100**
- Goodwill credits over **$50**
- Replacements over **$200**
- Waived fees (intercept, restocking)
- Extended return windows
- Extended warranty coverage

**Action**: Escalate with a recommended resolution and reasoning.

### Trigger B2: Refund/Replacement Authority Exceeded
Tier 1 cannot process refunds or replacements above the tier authority 
table:

| Action | Tier 1 | Tier 2 |
|---|---|---|
| Goodwill credit | Up to $10 | Up to $50 |
| Refund | ❌ | ✅ |
| Replacement | ❌ | ✅ Up to $200 |
| Waived fee | ❌ | ✅ |
| Investigation | ❌ | ✅ |

**Action**: Escalate with full order history and customer context.

### Trigger B3: System-Level Investigations
Any investigation requiring system access:

- Carrier investigation for lost packages
- Payment processor (Stripe) investigation
- Fraud investigation
- Multiple failed transactions on same card
- Warehouse/fulfillment investigation
- Inventory investigation

**Action**: Escalate with order ID, tracking, and case notes.

### Trigger B4: Security or Identity Issues Beyond Tier 1 Authority
Tier 1 cannot:

- Reset 2FA without full identity verification (escalate if 
  verification fails)
- Change account email without both-email verification
- Delete account without identity verification
- Merge accounts
- Unlock accounts beyond standard timeout

**Action**: Escalate to Tier 2 with verification attempts documented.

### Trigger B5: Legal, Regulatory, or Compliance
Any legal-adjacent case:

- Subpoena or court order
- Regulator inquiry (FTC, BBB, GDPR authority)
- Legal letter received
- Customer claims they will sue
- Insurance claim (product damage)

**Action**: Escalate to Tier 2 immediately. Route to legal@voltnest.com.

### Trigger B6: Fraud or Abuse Indicators
Any of the following:

- Multiple accounts from same IP/device
- Unusual order patterns (large orders, unusual timing)
- Customer claiming multiple unauthorized orders
- Payment method abuse signals
- Return abuse (repeated returns of "defective" items)
- Coupon/promo abuse patterns
- Loyalty point theft
- Price match abuse (3+ requests in 90 days)

**Action**: Escalate to Tier 2. Do not confront the customer. 
Document and hand off.

### Trigger B7: Repeated Contact on Same Issue
If a customer has contacted us **3+ times** on the same issue:

- First contact: Tier 1 handles
- Second contact: Tier 1 handles, notes pattern
- Third contact: escalate to Tier 2 for review

**Action**: Escalate with a summary of all prior contacts.

### Trigger B8: Public or Reputational Risk
Customer indicates they will:

- Post negative reviews on Trustpilot, Google, etc.
- Contact a journalist or media
- Post on social media (Twitter/X, Reddit, TikTok)
- File a BBB complaint
- Start a chargeback

**Action**: Escalate to Tier 2 immediately. Do not argue or defend. 
Focus on resolution.

### Trigger B9: Product Safety (Tier 1 → Tier 2 Same-Day)
Any safety concern from Trigger A6 requires same-day Tier 2 handoff:

- Overheating, smoke, fire
- Injury claims
- Electrical issues
- Battery swelling
- Child safety

**Action**: Escalate immediately with urgency flag. Do not wait for 
standard queue.

### Trigger B10: Complex Refund Scenarios
Refunds involving:

- Multiple orders combined
- Refunds split across payment methods
- Refunds after a card has expired or been cancelled
- Refunds with a gift-card split
- Refunds after account deletion
- Refunds outside standard timelines

**Action**: Escalate to Tier 2 for calculation and approval.

### Trigger B11: Warehouse or Fulfillment Issues
Any issue attributed to our operations:

- Wrong item shipped (verified)
- Missing item from order
- Order cancelled incorrectly by our system
- Packaging failure
- Return received but not processed
- Warehouse error on condition assessment

**Action**: Escalate to Tier 2 with warehouse ticket.

### Trigger B12: International Complexity
International cases involving:

- Customs seizure
- Import restrictions
- International warranty reimbursement over $30
- Cross-border intercept
- Currency conversion disputes
- Multi-country orders

**Action**: Escalate to Tier 2 with country details.

### Trigger B13: Data Accuracy Issues
Customer reports:

- Account data incorrect and can't be fixed at Tier 1
- Order data mismatch
- Payment history discrepancy
- Loyalty points balance incorrect
- Warranty coverage discrepancy

**Action**: Escalate to Tier 2 with data review.

### Trigger B14: Accessibility Failures
Customer reports accessibility barriers that can't be resolved at 
Tier 1:

- Screen reader incompatibility
- Keyboard navigation failure
- WCAG violation
- Assistive tech issues

**Action**: Escalate to Tier 2 → route to accessibility@voltnest.com.

## Non-Escalation Cases (AI Should Handle)

Not everything escalates. The AI should handle these directly:

### ✅ Handle Without Escalation

- Order status lookup
- Tracking lookup
- Policy explanations
- Product specs and FAQs
- Return initiation (within policy)
- Cancellation (before shipping)
- Password reset guidance
- Basic troubleshooting (see troubleshooting folder)
- Address changes (before packing)
- Gift message addition
- Loyalty points balance

### ⚠️ Escalate Even If Simple

Some simple-looking questions escalate:

- Any refund (financial authority)
- Any exception to policy
- Any emotion signal
- Any "human" request
- Any legal mention

**Rule**: When in doubt, escalate.

## Escalation Priority Levels

Once escalating, assign a priority:

| Priority | Triggers | SLA |
|---|---|---|
| **URGENT** | A6 (safety), A5 (compromise), A7 (legal), A2 (threats) | 4 business hours |
| **HIGH** | A4 (disputes), A11 (multi-issue), B6 (fraud), B8 (reputational) | 1 business day |
| **STANDARD** | All other escalations | 2 business days |

Priority determines routing queue and response time.

## What Escalation Is Not

Escalation is **not**:

- A way to avoid a difficult question
- A way to delay an answer
- A way to end a conversation abruptly
- A tool to silence frustrated customers
- A substitute for good AI answers

Escalation is a **quality guarantee** — it means the customer's issue 
is complex or sensitive enough that a human will serve them better.

## Related
- [Escalation Playbook](./escalation_playbook.md) — how to escalate
- [Sensitive Topics](./sensitive_topics.md) — special cases requiring 
  careful handling
- [Support Hours](../company/support_hours.md) — SLA windows
- [Contact VoltNest](../company/contact.md) — escalation channels
- [Mission & Values](../company/mission_values.md) — decision philosophy