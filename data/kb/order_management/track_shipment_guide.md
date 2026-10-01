# Track Shipment Guide

> **Category**: order_management  
> **Audience**: customer, agent  
> **Last updated**: 2026-01-15

Step-by-step guide for tracking your VoltNest shipment — where to find 
your tracking number, how to read carrier status updates, what each 
tracking event means, and when to worry about a package that isn't 
moving.

## Overview

Every VoltNest shipment has a **tracking number** issued by the carrier 
handling your package. This guide explains how to find that number and 
how to interpret what the carrier shows.

**Carrier tracking is separate from order status.** Order status (like 
"Processing" or "Shipped") is VoltNest's internal status. Carrier 
tracking (like "Label Created" or "In Transit") comes from the carrier 
directly.

**Related**: [Order Status Guide](./order_status_guide.md) — for 
VoltNest order statuses.

## Carriers We Use

VoltNest ships with these carriers, depending on your region and 
shipping method:

| Carrier | Service Area | Tracking URL |
|---|---|---|
| **UPS** | US domestic, some international | ups.com/track |
| **USPS** | US domestic, APO/FPO, some international | tools.usps.com |
| **FedEx** | US domestic express | fedex.com/tracking |
| **DHL** | International (EU, UK, APAC, India) | dhl.com/track |

Your shipping confirmation email tells you which carrier is handling 
your package.

## Where to Find Your Tracking Number

### Method 1: Shipping confirmation email
Sent within **24 hours** of your order being marked "Shipped." Look 
for an email from **orders@voltnest.com** with subject "Your VoltNest 
order has shipped."

The tracking number is displayed prominently. Click the "Track Package" 
link to go directly to the carrier's tracking page.

### Method 2: Your account
1. Log in to voltnest.com
2. Go to **Account → Orders**
3. Find the order (status: Shipped or later)
4. Click **"Track Package"**

### Method 3: Mobile app
Same as account — **Account → Orders → [Order] → Track Package**.

### Method 4: Directly at the carrier
If you know the carrier but lost the tracking number, you can search 
by reference number. Your **order ID** (format: `ORD-XXXXXX`) works 
as a reference on most carrier sites.

## How to Track Your Package

### Option A: From the shipping email (easiest)
Click the "Track Package" button in the email. Opens the carrier's 
tracking page with your number pre-filled.

### Option B: From your VoltNest account
1. Account → Orders → [Order] → Track Package
2. Opens the carrier's tracking page

### Option C: Manually at the carrier
1. Go to the carrier's website (from the table above)
2. Enter your tracking number
3. Click Track

### Option D: Mobile carrier app
UPS, USPS, FedEx, and DHL all have mobile apps. Once tracking is saved, 
you'll get push notifications on every status change.

### Option E: Text notifications
Most carriers offer SMS tracking updates. Opt in on the carrier's 
tracking page.

## Reading Tracking Statuses

Carriers use their own status labels — different from VoltNest order 
statuses. Here's what they mean:

### "Label Created" / "Shipping Label Created"
**What it means**: We printed the shipping label and notified the 
carrier. The package is packed and waiting for carrier pickup.

**What to expect next**: Within **1–2 business days**, the carrier 
will scan the package and the status will change to "Picked Up" or 
"In Transit."

**When to worry**: If this status persists for more than **3 business 
days**, contact support — the carrier may have missed a pickup.

---

### "Picked Up" / "Accepted" / "Origin Scan"
**What it means**: The carrier has physically received your package 
at their facility.

**What to expect next**: "In Transit" within 1–2 business days.

**When to worry**: Not yet. The package is moving.

---

### "In Transit" / "Departed Facility" / "Arrived at Facility"
**What it means**: Your package is moving through the carrier's 
network. Multiple "In Transit" events appear as the package passes 
through sorting hubs.

**What to expect next**: Continues until "Out for Delivery" or 
"Arrived at Destination Facility."

**When to worry**: If there are **no new events for 7 days** (US) or 
**14 days** (international), contact support.

---

### "Arrived at Destination Facility" / "At Local Facility"
**What it means**: Your package has reached the local delivery hub 
that serves your address.

**What to expect next**: "Out for Delivery" within 1–2 business days.

**When to worry**: If it stays at this status for more than **3 
business days**, contact the carrier directly.

---

### "Out for Delivery"
**What it means**: Your package is on the delivery vehicle today. It 
will be delivered before end of day.

**What to expect next**: "Delivered" today (usually by 8 PM local time).

**When to worry**: If it's past **9 PM local time** and still shows 
"Out for Delivery", contact the carrier.

---

### "Delivered"
**What it means**: The carrier marked the package as delivered. This 
is the final carrier status.

**What to expect next**: Nothing — the package is delivered.

**When to worry**: If tracking says "Delivered" but you don't have 
the package, wait **24 hours** — carriers sometimes mark early. After 
24 hours, see [Delivery Issues](./delivery_issues.md).

---

### "Delivery Attempted" / "Delivery Exception"
**What it means**: The carrier tried to deliver but couldn't. Reasons:

- No one home (signature required)
- Address inaccessible
- Business closed
- Recipient refused
- Package needs customs payment (international)

**What to expect next**: The carrier usually attempts delivery again 
the next business day, or holds the package at a local facility for 
pickup.

**When to worry**: Act immediately — after 2–3 failed attempts, the 
package may be returned to sender.

**What to do**:
1. Contact the carrier directly with your tracking number
2. Schedule redelivery or pickup
3. If signature required, ensure someone is home

---

### "Exception" / "Delay"
**What it means**: Something interrupted normal delivery. Common 
causes:

- Weather (storms, snow)
- Mechanical issue at carrier facility
- Customs hold (international)
- Incorrect address

**What to expect next**: Depends on the exception. Most resolve within 
1–3 business days.

**When to worry**: If the exception lasts more than **5 business 
days** without new updates, contact support.

---

### "Held at Customs" / "Customs Clearance"
**What it means**: (International only) Your package is being reviewed 
by your country's customs agency.

**What to expect next**: 3–10 business days for clearance. You may 
be contacted for payment of duties.

**When to worry**: If held for more than **10 business days**, contact 
your local customs office with your tracking number.

**Related**: [International FAQ](../faqs/international_faq.md)

---

### "Returned to Sender" / "Returned to Shipper"
**What it means**: The package is on its way back to our Memphis 
warehouse. Reasons:

- Multiple failed deliveries
- Refused delivery
- Address undeliverable
- Customs refused

**What to expect next**: Arrives at our warehouse in 3–7 business 
days. Refund is processed within 5–7 business days after arrival.

**When to worry**: If the package hasn't arrived at our warehouse 
within **10 business days** of "Returned to Sender", contact support.

**Related**: [Delivery Issues](./delivery_issues.md)

## International Tracking Quirks

International tracking is **not** the same as domestic. Watch for:

### 1. Tracking goes silent after export
When your package leaves the US, US carrier tracking often stops. It 
resumes when the destination country's postal service scans it — 
usually 3–7 business days later.

**Don't worry** during this gap — it's normal.

### 2. Tracking switches carriers
Your package may start with UPS and hand off to a local postal service 
(e.g., Royal Mail in the UK, Australia Post, India Post). The **same 
tracking number** usually works, but you may need to check the local 
carrier's site.

### 3. Status labels differ
"Handed to customs", "Awaiting customs clearance", and "Import scan" 
are all normal — they mean the same thing: your package is being 
processed at the destination country.

### 4. Updates are slower
Expect updates every **3–5 business days** rather than daily.

### 5. No local tracking
Some countries don't have tracking for final-mile delivery. Your 
package may show "In Transit" until it arrives.

**When to worry internationally**: If tracking hasn't updated in 
**14 business days**, contact support.

## Tracking Number Formats

If you're not sure which carrier you're dealing with, the tracking 
number format gives a clue:

| Format | Carrier |
|---|---|
| 18 digits, starts with "1Z" | UPS |
| 20–22 digits, starts with "92", "93", "94", "95" | USPS |
| 12 digits | FedEx |
| 10 digits, starts with "JD" or 3 letters + 9 digits | DHL |
| Starts with 2 letters, ends with "US" | USPS international |

## When to Worry — Quick Reference

| Situation | Threshold | Action |
|---|---|---|
| "Label Created" not updated | 3 business days | Contact support |
| No update in transit (US) | 7 days | Contact support |
| No update in transit (intl) | 14 days | Contact support |
| "Out for Delivery" past 9 PM | Same day | Contact carrier |
| "Delivered" but not received | 24 hours | Contact carrier, then support |
| "Delivery Attempted" | Same day | Contact carrier to reschedule |
| "Exception" | 5 business days | Contact support |
| Held at customs (intl) | 10 business days | Contact customs |
| "Returned to Sender" no arrival | 10 business days | Contact support |

## Common Tracking Questions

### Why hasn't my tracking updated in 3 days?

Normal. Carrier tracking is not real-time. Updates often pause for 
1–3 business days between scans, especially during peak season or 
weekends.

### My tracking says "Label Created" for 5 days — is something wrong?

Yes, at that point — the carrier hasn't picked up the package. Contact 
support with your order ID.

### Tracking shows "Delivered" but package isn't here

Wait 24 hours. Check with neighbors, building management, or front 
desk. Look in unusual places (porch, garage, behind bushes). After 24 
hours, contact the carrier, then support. See 
[Delivery Issues](./delivery_issues.md).

### Can VoltNest give me a more accurate ETA?

No — carrier estimates are the most accurate available. We can't see 
more than you can on the tracking page.

### Can I change the delivery address after it ships?

No. You can attempt a carrier intercept ($15, not guaranteed) — see 
[Modify Order Guide](./modify_order_guide.md).

### Can I schedule a specific delivery window?

Not through VoltNest. Some carriers offer this through their own 
apps (UPS My Choice, USPS Informed Delivery, FedEx Delivery Manager). 
Sign up directly with the carrier.

### Can I redirect the package to a pickup point?

Not through VoltNest. Some carriers offer this in their apps.

### What if my package is delivered to the wrong address?

Contact the carrier immediately. If the carrier can't recover it, 
contact support — we'll open a case.

## When to Contact Support

Contact support if:

- Tracking hasn't updated in 7 days (US) or 14 days (international)
- "Label Created" persists for more than 3 business days
- "Delivered" but package isn't received (after 24 hours)
- Tracking shows "Returned to Sender"
- Package was delivered to the wrong address
- You suspect the package is lost
- Tracking shows conflicting information

### What to Include

1. **Order ID** (format: `ORD-XXXXXX`)
2. **Tracking number**
3. **Current tracking status**
4. **How long** the tracking has been at that status
5. **Carrier** handling the package

### How to Contact

- **Email**: support@voltnest.com, subject "Tracking Issue"
- **Live chat**: voltnest.com/chat

### Response Time

- **Standard**: 24 hours
- **Missing/lost package (mark URGENT)**: 4 business hours

## For Support Agents

Internal notes for Tier 1 agents handling tracking inquiries.

### Triage Questions
- Do you have your tracking number?
- Which carrier is handling your package?
- What does tracking currently show?
- How long has it been at that status?
- Has tracking ever updated, or has it been stuck since label creation?

### Tier 1 Scope
Tier 1 can resolve:
- Helping customer find tracking number
- Explaining what a status means
- Confirming when customer should worry
- Guiding to carrier for delivery-issue resolution
- Confirming whether to open a support case

### Tier 2 Escalation Criteria
Escalate to Tier 2 when:
- Tracking silent > 7 days (US) or > 14 days (intl)
- Package marked delivered but not received (after 24 hours)
- Carrier reports "Returned to Sender"
- Suspected package loss
- Multiple tickets on same shipment

### Opening a Carrier Investigation
For Tier 2, open an investigation with the carrier via their 
business portal:

1. Gather: order ID, tracking number, ship date, value, contents
2. File investigation with the appropriate carrier
3. Provide customer an interim update within 4 business hours
4. Follow up every 48 hours until resolved

**SLA for resolution**: **10 business days** from investigation open.

### Do NOT Tell the Customer
- Do not provide ETAs the carrier hasn't confirmed
- Do not promise recovery of a "Delivered" package
- Do not blame the carrier unless we have evidence
- Do not confirm a refund until the investigation concludes
- Do not share the carrier's internal tracking system access

### Package Loss Resolution
If a package is confirmed lost:

- **Domestic**: refund or replacement at customer's choice within 
  10 business days
- **International**: refund or replacement at customer's choice, 
  timeline per carrier claim
- See [Shipping Policy](../policies/shipping_policy.md) for the 
  lost-package protocol

## Related
- [Order Status Guide](./order_status_guide.md)
- [Cancel Order Guide](./cancel_order_guide.md)
- [Modify Order Guide](./modify_order_guide.md)
- [Delivery Issues](./delivery_issues.md)
- [Shipping Policy](../policies/shipping_policy.md)
- [International FAQ](../faqs/international_faq.md)
- [Contact VoltNest](../company/contact.md)