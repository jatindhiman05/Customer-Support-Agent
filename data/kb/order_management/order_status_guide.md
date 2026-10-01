# Order Status Guide

> **Category**: order_management  
> **Audience**: customer, agent  
> **Last updated**: 2026-01-15

This guide explains every order status you'll see in your VoltNest 
account, what each one means, and what you should expect next. Use it 
to understand where your order is in the fulfillment process.

## Overview

Your order moves through a series of statuses from the moment you place 
it to the moment it's delivered. Most orders pass through 5–6 statuses 
in 3–10 business days (domestic) or 2–4 weeks (international).

**Statuses never skip ahead** — they always progress in order. If your 
order appears "stuck" at a status, this guide tells you what to expect 
and when to worry.

## Order Statuses at a Glance

| Status | What It Means | Typical Duration |
|---|---|---|
| **Payment Pending** | Payment is being verified | Minutes to 2 hours |
| **Confirmed** | Payment accepted, order received | 0–2 hours |
| **Processing** | Being prepared at our warehouse | 0–24 hours |
| **Packed** | Packaged, waiting for carrier pickup | 1–4 hours |
| **Shipped** | Handed to carrier, has tracking number | 1–2 business days |
| **In Transit** | Moving through carrier network | 3–7 business days (US) |
| **Out for Delivery** | On the delivery vehicle today | Same day |
| **Delivered** | Package delivered | — |
| **Cancelled** | Order cancelled before shipping | — |
| **Returned** | Package returned to sender | — |
| **Refunded** | Refund processed after return/cancel | — |

## Status Details

### Payment Pending

**What it means**: Your payment is being verified by our processor 
(Stripe) or your bank. This is normal for the first few minutes.

**Typical duration**: A few minutes. Rarely up to 2 hours.

**What you should do**: Nothing. Wait for the next status update.

**When to worry**: If it stays "Payment Pending" for more than 
**4 hours**, contact support — the payment may have failed silently.

**Related**: [Payment Failures](../troubleshooting/payment_failures.md)

---

### Confirmed

**What it means**: Payment accepted. Your order is officially in our 
system and moving to fulfillment.

**Typical duration**: 0–2 hours.

**What you should do**: Nothing. You'll receive a confirmation email 
with your order ID (format: `ORD-XXXXXX`).

**When to worry**: If the order stays "Confirmed" for more than 
**24 hours**, contact support — a rare fulfillment hold may have 
occurred.

---

### Processing

**What it means**: Our Memphis warehouse is preparing your order. 
Items are being picked, quality-checked, and staged for packing.

**Typical duration**: 0–24 hours (usually under 8 hours if placed 
before 2 PM EST).

**What you should do**: Nothing. You can still cancel during this 
status.

**When to worry**: If it stays in "Processing" for more than **48 
hours**, contact support — this usually means an item is out of stock.

**Related**: [Cancel Order Guide](./cancel_order_guide.md)

---

### Packed

**What it means**: Your order is boxed, labeled, and waiting for the 
carrier to pick it up. It's physically ready to ship.

**Typical duration**: 1–4 hours, unless the pickup window has closed 
for the day.

**What you should do**: Nothing.

**Important**: **Cancellation is no longer self-service** once your 
order is Packed. You'll need to contact support to attempt an intercept 
(see [Cancel Order Guide](./cancel_order_guide.md)).

**When to worry**: If it stays "Packed" for more than **24 hours**, 
contact support — the carrier may have missed a pickup.

---

### Shipped

**What it means**: The carrier has picked up your package. You now 
have a tracking number.

**Typical duration**: 1–2 business days at this status (before tracking 
updates meaningfully).

**What you should do**: 
- Check your email for the shipping confirmation
- Save your tracking number
- Track via the carrier's website or your account

**When to worry**: If tracking hasn't updated in **7 days** after 
"Shipped" (US) or **14 days** (international), contact support.

**Related**: [Track Shipment Guide](./track_shipment_guide.md)

---

### In Transit

**What it means**: Your package is moving through the carrier's 
network toward you. Tracking should update every 1–2 days.

**Typical duration**: 
- **Domestic Standard**: 3–7 business days
- **Domestic Express**: 1–2 business days
- **International**: 7–18 business days (plus customs)

**What you should do**: Track periodically. No action needed.

**When to worry**: If tracking hasn't updated for **7 days** (US) or 
**14 days** (international) while "In Transit", contact support.

**Related**: [Delivery Issues](./delivery_issues.md)

---

### Out for Delivery

**What it means**: Your package is on the delivery vehicle today. It 
will be delivered before end of day.

**Typical duration**: Same day (usually by 8 PM local time).

**What you should do**: Be available to receive the package. If 
signature is required, someone must be home.

**When to worry**: If it stays "Out for Delivery" past **9 PM local 
time**, contact the carrier directly — the driver may have been 
unable to deliver.

---

### Delivered

**What it means**: The carrier marked the package as delivered. This 
is the final status for successful orders.

**Typical duration**: N/A.

**What you should do**: 
- Verify you received the package
- If **not received but marked delivered**, wait 24 hours (carriers 
  sometimes mark early)
- After 24 hours, contact the carrier first, then support

**When to worry**: If your tracking shows "Delivered" but you don't 
have the package after 24 hours, see 
[Delivery Issues](./delivery_issues.md).

---

### Cancelled

**What it means**: The order was cancelled — either by you or by 
VoltNest (out of stock, fraud flag, etc.).

**Typical duration**: N/A (final status).

**What you should do**: 
- Check your email for the cancellation reason
- Expect a refund within **1–2 business days** if cancelled before 
  packing, **5–7 business days** if after

**When to worry**: If you didn't cancel and the order shows 
"Cancelled", contact support immediately — potential account 
compromise.

**Related**: [Cancellation Policy](../policies/cancellation_policy.md)

---

### Returned

**What it means**: The package was returned to our warehouse — either 
because you refused delivery, the carrier couldn't deliver, or a 
return was initiated.

**Typical duration**: N/A.

**What you should do**: 
- Wait for our warehouse to receive and inspect the package
- Refunds are issued **5–7 business days** after arrival at our 
  Memphis warehouse

**When to worry**: If the status has been "Returned" for more than 
**10 business days** without a refund, contact support.

**Related**: [Return & Refund Policy](../policies/return_refund_policy.md)

---

### Refunded

**What it means**: Your refund has been issued to the original payment 
method. This is the final status.

**Typical duration**: N/A.

**What you should do**: 
- Check your bank/credit card statement within 5–7 business days
- Contact your bank if the refund doesn't appear

**When to worry**: If your bank has no record after **10 business 
days**, contact support with your refund confirmation.

**Related**: [Payment FAQ](../faqs/payment_faq.md)

## Status Timeline — What to Expect

### Domestic Order (Standard Shipping)
Hour 0: Order placed → Payment Pending
Hour 0-1: Payment confirmed → Confirmed
Hour 1-8: Being prepared → Processing
Hour 8-12: Packed & labeled → Packed
Hour 12-24: Handed to carrier → Shipped
Day 2-8: Moving through network → In Transit
Day 8: On delivery vehicle → Out for Delivery
Day 8: Delivered → Delivered


**Total: 5–8 business days from order to delivery.**

### International Order (Standard)
Hour 0: Order placed → Payment Pending
Hour 0-1: Payment confirmed → Confirmed
Hour 1-12: Processing
Hour 12-24: Packed
Day 1-2: Shipped
Day 3-14: In Transit (export)
Day 4-10: Customs clearance
Day 10-20: In Transit (import)
Day 12-20: Out for Delivery
Day 12-20: Delivered


**Total: 12–20 business days from order to delivery (plus customs).**

## Where to Find Your Order Status

### Via voltnest.com
1. Log in to your account
2. Go to **Account → Orders**
3. Click on any order to see its current status
4. Click "Track Package" to see carrier tracking

### Via email
- **Confirmation email** — sent when order is placed (status: Confirmed)
- **Shipping email** — sent when order ships (includes tracking)
- **Delivery email** — sent when order is delivered

### Via the mobile app
Same as website — **Account → Orders**.

### Via carrier website
Use the tracking number from your shipping email. Track directly on 
UPS, USPS, FedEx, or DHL.

## Common Questions About Status

### Why hasn't my status changed in hours?

Status updates aren't real-time. Processing, packing, and shipping 
transitions often happen in batches. It's normal for a status to sit 
for 8–24 hours without update.

### My status says "Shipped" but tracking shows "Label Created"

This means we printed the label but the carrier hasn't scanned the 
package yet. It usually updates within **12–24 hours**. If not, contact 
support.

### My status says "Delivered" but I don't have my package

Wait **24 hours** — carriers sometimes mark packages as delivered 
early. Check with neighbors, building management, or your front desk. 
After 24 hours, contact the carrier, then support. See 
[Delivery Issues](./delivery_issues.md).

### Can I cancel if my order is "Processing"?

Yes — you can self-cancel while status is **Confirmed**, **Processing**, 
or **Packed** (though Packed requires support). Once **Shipped**, you 
must wait for delivery and return.

### Can I change my shipping address if the status is "Shipped"?

No. Once shipped, the address is locked. You can attempt a carrier 
intercept for **$15** (not guaranteed) — see 
[Modify Order Guide](./modify_order_guide.md).

### Why does my order show "Cancelled" when I didn't cancel it?

Possible causes:
- Out of stock (item sold out between order and packing)
- Pricing error
- Fraud flag from our payment processor
- Shipping restriction

Check your email for the cancellation reason. If you have no email, 
contact support.

### My order status is "Refunded" but I never asked for a refund

This means your order was cancelled and refunded. Check your email 
for the reason. If unexplained, contact support.

## When to Contact Support

Contact support if any of the following apply:

- Any status is "stuck" beyond its expected duration (see "When to 
  worry" per status)
- Status shows "Cancelled" or "Refunded" but you didn't request it
- Status shows "Delivered" but package isn't received (after 24 hours)
- Tracking hasn't updated in 7 days (US) or 14 days (international)
- Order was marked "Returned" without a refund within 10 business days

### What to Include

1. **Order ID** (format: `ORD-XXXXXX`)
2. **Current status** as shown in your account
3. **How long** the order has been at that status
4. **What you expected** to happen instead

### How to Contact

- **Email**: support@voltnest.com, subject "Order Status"
- **Live chat**: voltnest.com/chat

### Response Time

- **Standard**: 24 hours
- **Urgent** (delivered but not received, fraud flag): 4 business hours

## For Support Agents

Internal notes for Tier 1 agents.

### Status Verification
Always confirm the customer's status by looking up the order in the 
order management system before troubleshooting. Do not rely on the 
customer's description alone.

### Common Status Questions → Routing

| Question | Route To |
|---|---|
| "Where's my package?" | Track Shipment Guide |
| "Can I cancel?" | Cancel Order Guide |
| "Can I change my address?" | Modify Order Guide |
| "Tracking hasn't updated" | Delivery Issues |
| "Marked delivered but not received" | Delivery Issues |
| "Order cancelled by VoltNest" | Check internal notes for reason |
| "Why pending charge?" | Payment FAQ |

### Status-Specific Escalation

- **Payment Pending > 4 hours** → contact Stripe via dashboard, verify 
  intent status
- **Processing > 48 hours** → check warehouse status for stock issues
- **Packed > 24 hours** → contact carrier, check pickup schedule
- **Shipped with no tracking update > 7 days** → open carrier 
  investigation
- **In Transit > 14 days (int'l)** → open international carrier claim

### Do NOT Tell the Customer
- Do not promise a delivery date unless confirmed by the carrier
- Do not say "It's on its way" if tracking hasn't updated in 7+ days
- Do not blame the carrier without evidence
- Do not confirm a refund until the refund has actually been processed

## Related
- [Cancel Order Guide](./cancel_order_guide.md)
- [Track Shipment Guide](./track_shipment_guide.md)
- [Modify Order Guide](./modify_order_guide.md)
- [Delivery Issues](./delivery_issues.md)
- [Cancellation Policy](../policies/cancellation_policy.md)
- [Shipping Policy](../policies/shipping_policy.md)
- [Return & Refund Policy](../policies/return_refund_policy.md)
- [Payment FAQ](../faqs/payment_faq.md)
- [Contact VoltNest](../company/contact.md)