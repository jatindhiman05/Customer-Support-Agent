# Payment Failures (Troubleshooting)

> **Category**: troubleshooting  
> **Audience**: customer, agent  
> **Last updated**: 2026-01-15

Diagnostic guide for failed payments on voltnest.com — declined cards, 
3D Secure errors, PayPal failures, Klarna/Afterpay rejections, and 
checkout errors. Follow the steps in order based on your payment method.

## Symptoms This Guide Covers

Use this guide if you're experiencing any of the following:

- Card declined with no clear reason
- "Payment could not be processed" at checkout
- 3D Secure verification fails or loops
- Billing address mismatch error
- CVV error even though the code is correct
- PayPal redirects back to checkout without completing
- Klarna or Afterpay application is rejected
- Checkout hangs or times out during payment
- Payment succeeds but order isn't created
- "This payment method is not accepted" for a valid card

If your issue is **not about the payment failing**, but about a 
**pending or double charge**, see the 
[Payment FAQ](../faqs/payment_faq.md) instead.

## Before You Start

Quick facts:

- All cards are processed by **Stripe** (PCI-DSS Level 1)
- We accept Visa, Mastercard, Amex, Discover, PayPal, Apple Pay, 
  Google Pay, Klarna, Afterpay
- We charge in **USD only**
- Cards decline for reasons **only your bank** can see
- Most failures are billing address mismatches

Run these three quick checks before continuing:

1. **Card not expired?** Check the date on the card itself
2. **Billing address correct?** It must match your bank's records exactly
3. **Sufficient funds?** Include a small buffer for currency conversion

If all three are fine, continue to Step 1.

## Step 1: Identify the Exact Error Message

The error message tells you which step to focus on.

| Error Message | Go To |
|---|---|
| "Your card was declined" | Step 2 |
| "Billing address does not match" | Step 3 |
| "CVV is incorrect" | Step 4 |
| "3D Secure verification failed" | Step 5 |
| "Payment method not accepted" | Step 6 |
| "Something went wrong. Try again." | Step 7 |
| PayPal-specific error | Step 8 |
| Klarna / Afterpay rejection | Step 9 |

## Step 2: "Your Card Was Declined"

Card declines come from your bank, not from VoltNest. We see only the 
decline; your bank sees the reason.

### Common decline reasons

**Insufficient funds**
- Check your balance
- Include a small buffer for pending charges
- Try a different card

**Daily spending limit**
- You may have hit your card's daily cap
- Wait 24 hours or use a different card

**Card reported lost or stolen**
- The bank has blocked the card
- Contact your bank, then use a different card

**International transaction block**
- Some US banks block online merchants from certain regions
- Contact your bank to authorize the transaction
- Try again

**Card flagged for fraud**
- Banks sometimes flag unusual purchases
- Call the number on the back of the card to verify
- Try again after the bank clears the flag

### What to do next

1. **Try a different card** — most declines are card-specific
2. **Contact your bank** — they can tell you the exact reason
3. **Try PayPal, Apple Pay, or Google Pay** — alternative methods often 
   work when a card is blocked

VoltNest cannot override a bank decline. If your bank says the card 
should work, contact support@voltnest.com.

## Step 3: "Billing Address Does Not Match"

This is the **#1 cause** of checkout failures. The billing address you 
enter must match the address your bank has on file.

### How to fix

1. Log in to your bank's website or app
2. Find the billing address on file for the card
3. Enter that address at checkout — **character for character**
4. Common mismatches:
   - **Apt/Suite number missing or in the wrong field**
   - **Street abbreviation** — "St" vs. "Street", "Ave" vs. "Avenue"
   - **ZIP+4** — sometimes banks require the extra 4 digits
   - **Old address** — banks may not have updated your address
   - **Business vs. residential** — some banks use the business address

### If the address is correct but still fails

- **Try a shorter version** — some systems reject addresses over 
  30 characters
- **Remove punctuation** — commas, periods, and hyphens can cause 
  failures
- **Update your bank** — if your billing address changed recently, 
  update it with your bank first

## Step 4: "CVV Is Incorrect"

The CVV (Card Verification Value) is the 3 or 4 digit code on your card.

### Where to find it
- **Visa, Mastercard, Discover**: 3 digits on the **back**
- **American Express**: 4 digits on the **front**, above the card number

### If the CVV keeps failing

- **Re-enter the full card number** — a wrong digit may be hiding 
  elsewhere
- **Check for zeros vs. letter O** — some cards use 0 (zero), not O
- **Card damaged** — if the CVV is faded, try a different card
- **Wrong card type** — Amex codes are on the front, not the back

## Step 5: 3D Secure Verification Failed

3D Secure ("Verified by Visa," "Mastercard SecureCode," etc.) is a 
bank-mandated security step. Your bank controls this — VoltNest cannot 
bypass it.

### Common 3D Secure issues

**Code not arriving by SMS**
- Check your phone has signal
- Verify your phone number with your bank
- Wait 60 seconds, then request a new code
- Try your bank's app — many banks now verify via app instead of SMS

**Verification loop**
- Browser cookies are blocking the redirect
- Enable cookies for both voltnest.com and your bank's domain
- Try a different browser
- Disable browser extensions and VPNs

**Verification fails**
- The code expired (they last ~5 minutes)
- Wrong code entered
- Your bank has a system issue — try again in 30 minutes

**No prompt appears**
- Your bank may not require 3D Secure for this card
- The redirect may have been blocked
- Try a different browser

### If 3D Secure won't complete

1. **Try a different card** — your other card may not require 3D Secure
2. **Try PayPal** — bypasses 3D Secure entirely
3. **Contact your bank** — they can temporarily whitelist or fix the 
   issue
4. **Try again in 30 minutes** — bank systems sometimes have transient 
   issues

## Step 6: "Payment Method Not Accepted"

If a card that should work is being rejected:

### Check these first
- **Card type**: We accept Visa, MC, Amex, Discover
- **Not accepted**: Diners Club, JCB, UnionPay, Maestro, prepaid 
  cards without a billing address
- **Card origin**: Cards from certain countries may be blocked for 
  fraud prevention
- **Prepaid cards**: Some prepaid cards don't support online 
  verification — try registering the card with the issuer first

### If the card should work
- Try a different browser or device
- Clear cookies for voltnest.com
- Try PayPal as a fallback
- Contact support@voltnest.com with the card type and last 4 digits

## Step 7: "Something Went Wrong. Try Again."

This is a generic error that usually indicates a **transient** issue 
on the payment processor's end.

### Steps to try

1. **Wait 60 seconds** and try again
2. **Refresh the checkout page** — don't refresh during a payment 
   submission, only before
3. **Try a different browser** — Chrome, Firefox, Safari, Edge
4. **Clear cookies** for voltnest.com
5. **Disable VPN** — some VPNs are blocked
6. **Try on mobile data** — some Wi-Fi networks block payment redirects
7. **Try a different payment method** — PayPal or Apple/Google Pay

### If the error persists

The issue is likely on our side or Stripe's. Email 
support@voltnest.com with:

- Your order ID (if created) or a screenshot of the cart
- The exact error message
- The time of the attempt
- The payment method used

We investigate payment processing issues within **4 business hours**.

## Step 8: PayPal Issues

### PayPal redirects back without completing

- **PayPal session expired** — start over and complete within 5 minutes
- **Browser blocking redirects** — allow popups and redirects for 
  voltnest.com and paypal.com
- **PayPal account issues** — log in to PayPal directly to verify 
  your account is in good standing

### "We can't complete this payment"

- Your PayPal balance or linked card may be insufficient
- PayPal may require additional verification
- Log in to PayPal → Resolution Center to see any issues

### Order paid but not showing on VoltNest

PayPal sometimes delays confirmation. Wait **5 minutes** and refresh 
your order history. If the order still doesn't appear after 30 minutes, 
contact support with:

- PayPal transaction ID
- Order amount and date
- Items purchased

We reconcile PayPal transactions within **1 business day**.

## Step 9: Klarna & Afterpay Rejections

Klarna and Afterpay are separate companies that approve or decline 
**independently of VoltNest**. Their decisions are based on:

- Credit history (soft check, no impact on score)
- Order size
- Account history with them
- Location

### Common reasons for rejection

- **First-time use** — first-time users are more likely to be declined
- **Order too high** — over your personal limit with that provider
- **Order too low** — Klarna and Afterpay require $50 minimum
- **Existing overdue balance** — pay off prior installments first
- **Account restrictions** — check your account in the Klarna or 
  Afterpay app
- **Region not supported** — availability varies by country

### If you're rejected

VoltNest cannot override Klarna or Afterpay decisions. Options:

1. **Pay in full** — with a card, PayPal, or Apple/Google Pay
2. **Try the other provider** — Afterpay may approve where Klarna 
   doesn't (or vice versa)
3. **Contact the provider** — Klarna and Afterpay support can explain 
   the specific reason

## Step 10: Payment Succeeds But Order Doesn't Appear

Rare, but happens. The payment went through but the order wasn't 
created in our system.

### What to do

1. **Wait 5 minutes** and refresh **Account → Orders**
2. **Check your email** for an order confirmation (may arrive with delay)
3. **Check your bank statement** — is the charge **posted** or **pending**?
   - **Pending**: The order likely failed and the charge will release 
     in 3–5 business days
   - **Posted**: The order was created — check your spam folder for 
     the confirmation

### If a posted charge has no matching order

Contact support@voltnest.com with subject **"Charged But No Order"**:

- Bank statement screenshot showing the posted charge
- Date and amount of the charge
- Payment method used (card ending in XXXX)
- Time you placed the order

We investigate within **4 business hours** and either:

- Recreate the order and ship it, or
- Refund the charge in full

## Step 11: Test with a Different Method

The fastest way to complete your order while troubleshooting is to 
try a different payment method.

| Method | Best for | Notes |
|---|---|---|
| **PayPal** | Bypasses card issues | No 3D Secure |
| **Apple Pay** | iOS users | Bypasses card entry |
| **Google Pay** | Android users | Bypasses card entry |
| **Different card** | Bank-side decline | Try a second card |
| **Klarna / Afterpay** | Split payment | Requires $50+ |

If your order is time-sensitive, don't wait for troubleshooting — 
try a different method and place the order.

## When to Escalate to Support

Contact support if:

- You've tried Steps 1–11 and still can't complete payment
- A posted charge has no matching order
- You've been charged but no order confirmation arrived
- Your card was declined with no clear reason after contacting your bank

### What to Include

1. **Order ID** if it exists (format: `ORD-XXXXXX`)
2. **Payment method** (card type + last 4 digits, or PayPal/Klarna/etc.)
3. **Exact error message** (screenshot preferred)
4. **Time and date** of the attempt
5. **Device and browser** used
6. **Steps you've tried** (1–11)

### How to Contact

- **Email**: support@voltnest.com, subject "Payment Failed"
- **Live chat**: voltnest.com/chat

### Response Time

- **Payment issue**: Within 24 hours
- **Charged but no order** (URGENT): Within 4 business hours

## What NOT to Do

### ❌ Don't refresh during payment submission
Refreshing while a payment is processing can create a duplicate charge 
or corrupt the transaction. Wait for the page to respond before 
refreshing.

### ❌ Don't retry more than 5 times
Repeated failed attempts can trigger fraud locks on your card or 
account. After 3 failures, try a different method or contact support.

### ❌ Don't use a VPN during checkout
VPNs are commonly flagged for fraud. Disable VPN and try again.

### ❌ Don't use the same card that's expired
Even if your bank says it's fine, an expired card won't work online. 
Check the date.

### ❌ Don't send card numbers over email
Support will **never** ask you to email your card number, CVV, or 
full details. Only the last 4 digits are needed for support purposes.

### ❌ Don't ignore a pending charge
If a charge shows as pending but the order failed, it will release 
automatically in 3–5 business days. If it doesn't release, contact 
support.

### ❌ Don't click payment links from emails or texts
VoltNest never sends payment links by email or SMS. If you receive 
one, it's phishing — forward to security@voltnest.com.

## For Support Agents

Internal notes for Tier 1 and Tier 2 agents handling payment failures.

### Triage Questions
- What payment method were you using?
- What error message appeared? (screenshot preferred)
- Have you successfully paid on voltnest.com before?
- Is the card expired?
- Does the billing address match your bank's records?
- Is the charge pending or posted in your banking app?
- Did you try a different payment method?

### Tier 1 Scope
Tier 1 can resolve:
- Billing address mismatch guidance (Step 3)
- CVV error guidance (Step 4)
- 3D Secure troubleshooting (Step 5)
- Payment method compatibility (Step 6)
- Transient error retry (Step 7)
- PayPal guidance (Step 8)
- Klarna/Afterpay rejection explanation (Step 9)

### Tier 2 Escalation Criteria
Escalate to Tier 2 when:
- Customer's card was declined by the bank but bank says it's fine
- Posted charge has no matching order (URGENT)
- Multiple payment methods fail on same account (potential account 
  flag)
- Suspected fraud or account compromise
- Payment processor errors persist across retries

### Stripe Investigation
For Tier 2, check Stripe Dashboard for:
- **Charge status** — succeeded, failed, disputed
- **Failure code** — Stripe provides a specific decline reason
- **Radar risk score** — high-risk charges may be blocked by Stripe's 
  fraud system

If Stripe blocked the charge (not the bank), we can manually review 
and re-enable.

### Do NOT Tell the Customer
- Do not tell them which specific bank reason caused the decline 
  (Stripe doesn't always share it)
- Do not promise the charge will clear — pending charges are bank-side
- Do not ask for full card details — only last 4 digits
- Do not suggest they reinstall the app or reset their device

### Charged But No Order — SLA
This is a **4 business hour SLA**. Confirm the charge is posted, then:

1. Check Stripe for the payment intent
2. If payment succeeded but order failed, either recreate the order 
   or refund
3. Notify customer within 4 business hours with the resolution

## Related
- [Payment FAQ](../faqs/payment_faq.md)
- [Return & Refund Policy](../policies/return_refund_policy.md)
- [Cancellation Policy](../policies/cancellation_policy.md)
- [Privacy Policy](../policies/privacy_policy.md)
- [Contact VoltNest](../company/contact.md)