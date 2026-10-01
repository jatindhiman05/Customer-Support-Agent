# Payment Terms Glossary

> **Category**: glossary  
> **Audience**: customer, agent  
> **Last updated**: 2026-01-15

Definitions of payment and billing terms used across VoltNest's 
knowledge base. Terms are listed alphabetically. Each definition is 
1–3 sentences and links to the source document where the term is used.

## 3

### 3D Secure (3DS)

A security protocol required by many banks for online card payments. 
When you check out, your bank may redirect you to enter a code sent 
by SMS or approve via their app. VoltNest cannot bypass 3D Secure — 
it's controlled entirely by your bank.

*Also known as*: Verified by Visa, Mastercard SecureCode, American 
Express SafeKey.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Payment Failures](../troubleshooting/payment_failures.md)

## A

### Acquiring Bank

The bank that processes card payments on behalf of the merchant 
(VoltNest). Handles the technical side of moving money from the 
customer's issuing bank to VoltNest. VoltNest's acquiring bank works 
with Stripe.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

### Afterpay

A "Buy Now, Pay Later" (BNPL) service that lets customers split 
purchases into **4 interest-free installments**. VoltNest accepts 
Afterpay for orders between **$50 and $1,500**.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Promo & Gift Card FAQ](../faqs/promo_giftcard_faq.md)

### Authorization

The first step of a card payment — the bank confirms the card has 
sufficient funds and approves the transaction. The charge appears as 
"pending" until it's captured. Authorizations typically expire in 
**3–5 business days** if not captured.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Payment Failures](../troubleshooting/payment_failures.md)

## B

### Billing Address

The address on file with your bank for a credit or debit card. Must 
match **exactly** at checkout or the payment will fail. Includes 
street, apartment/suite number, city, state, ZIP, and country. 
Common mismatches: apartment number missing, ZIP+4 required, old 
address on file.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Payment Failures](../troubleshooting/payment_failures.md)

### BNPL (Buy Now, Pay Later)

A payment model where the customer receives the product immediately 
but pays in installments. VoltNest offers **Klarna** and **Afterpay** 
as BNPL options. Typically 4 interest-free payments over 6 weeks.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

## C

### Capture

The second step of a card payment — the authorized amount is 
finalized and moved to settlement. Once captured, the charge is 
"posted" (no longer pending). VoltNest captures payment when the 
order ships.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

### Card on File (COF)

A saved payment method that can be charged for future orders without 
re-entering card details. VoltNest stores cards via **Stripe tokens** 
— we never see or store the full card number. You can remove saved 
cards at **Account → Payment Methods**.

*Used in*: [Manage Account Settings](../account/manage_account_settings.md)

### Chargeback

A forced reversal of a card charge initiated by the customer's bank. 
Unlike a refund (which is voluntary), a chargeback is a dispute. 
Chargebacks carry fees and are investigated by the bank. Customers 
should contact support **before** filing a chargeback.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Sensitive Topics — Section K](../escalation/sensitive_topics.md)

### Checkout

The final step of an online purchase where the customer confirms 
items, shipping, and payment. VoltNest's checkout requires an account 
(no guest checkout).

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

### Credit Card

A card that borrows money from the issuing bank, repaid monthly. 
VoltNest accepts **Visa, Mastercard, American Express, and Discover** 
credit cards.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

### Currency Conversion

The process where your bank converts a charge in USD to your local 
currency. Your bank applies its own exchange rate and may charge a 
**foreign transaction fee** (typically 0–3%). VoltNest charges in 
USD only.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[International FAQ](../faqs/international_faq.md)

### CVV / CVC

The security code on a card. **Visa, Mastercard, Discover**: 3 digits 
on the back. **American Express**: 4 digits on the front. Required 
for all online card payments.

*Also known as*: CVV2, CVC2, CID.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Payment Failures](../troubleshooting/payment_failures.md)

## D

### Debit Card

A card that draws directly from a bank account (not borrowed). 
VoltNest accepts **Visa and Mastercard debit cards**. Debit cards 
sometimes decline where credit cards succeed because of bank 
security rules.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

### Decline

When a card issuer rejects a payment. Common reasons: insufficient 
funds, billing address mismatch, expired card, or fraud flag. 
VoltNest cannot see why a bank declined a charge — only your bank 
knows.

*Used in*: [Payment Failures](../troubleshooting/payment_failures.md), 
[Payment FAQ](../faqs/payment_faq.md)

### Dispute

A disagreement about a charge — either initiated by the customer 
(chargeback) or by VoltNest (e.g., disputed delivery). Different 
from a refund.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

## E

### Expired Card

A card past its expiry date (MM/YY shown on the front). Expired 
cards are automatically declined. Update your saved card at 
**Account → Payment Methods** or use a different card.

*Used in*: [Payment Failures](../troubleshooting/payment_failures.md), 
[Manage Account Settings](../account/manage_account_settings.md)

## F

### Foreign Transaction Fee

A fee charged by some banks for purchases made in a foreign currency 
or with a foreign merchant. Typically **0–3%**. Charged by your bank, 
not by VoltNest.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[International FAQ](../faqs/international_faq.md)

## G

### Gateway

The technology that transmits payment data between the customer, 
VoltNest, and the banks. VoltNest uses **Stripe** as its payment 
gateway.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Privacy Policy](../policies/privacy_policy.md)

### Gift Card

A prepaid card that can be applied to VoltNest purchases. Gift cards 
never expire, have no fees, and can be combined with promo codes. 
Available in $25, $50, $100, $200, or custom amounts ($25–$500).

*Used in*: [Promo & Gift Card FAQ](../faqs/promo_giftcard_faq.md)

## I

### Installment Plan

See **BNPL** above. VoltNest offers installment plans through Klarna 
and Afterpay — typically 4 payments over 6 weeks, interest-free if 
paid on time.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

### Issuing Bank

The bank that issued a customer's credit or debit card. The issuing 
bank approves or declines each transaction, sets spending limits, and 
handles disputes.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

## K

### Klarna

A "Buy Now, Pay Later" service that lets customers split purchases 
into **4 interest-free installments**. VoltNest accepts Klarna for 
orders between **$50 and $1,000**.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

## M

### Merchant

The business accepting payment — in VoltNest's case, VoltNest Inc. 
Appears on card statements as **VOLTNEST** or **VOLTNEST INC**.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

## P

### PayPal

An online payment platform that lets customers pay using a PayPal 
balance, linked bank account, or linked card. VoltNest accepts PayPal 
for all orders. PayPal payments don't require 3D Secure.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Payment Failures](../troubleshooting/payment_failures.md)

### PCI-DSS (Payment Card Industry Data Security Standard)

A security standard for any business that handles card data. **PCI-DSS 
Level 1** is the highest certification. VoltNest uses Stripe, which 
is PCI-DSS Level 1 certified — meaning we never store full card 
numbers.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Privacy Policy](../policies/privacy_policy.md)

### Pending Charge

A temporary authorization on your card that reduces your available 
balance but hasn't been captured yet. Pending charges typically 
resolve (either captured or released) within **3–5 business days**. 
Commonly mistaken for a double charge.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Payment Failures](../troubleshooting/payment_failures.md)

### Posted Charge

A charge that has been captured and finalized. Shows as "Posted" or 
"Completed" in your bank account (vs. "Pending"). Posted charges are 
final and require a refund to reverse.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

### Prepaid Card

A card pre-loaded with a set amount. VoltNest accepts prepaid cards 
(Visa, Mastercard, Amex) if they have a registered billing address. 
Some prepaid cards without billing addresses are declined.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

### Promo Code

A short alphanumeric code applied at checkout for a discount. Also 
called a coupon, discount code, or voucher. **One promo code per 
order.** Promo codes expire on the date stated when issued.

*Used in*: [Promo & Gift Card FAQ](../faqs/promo_giftcard_faq.md), 
[General FAQ](../faqs/general_faq.md)

## R

### Refund

A voluntary return of funds to the original payment method. Different 
from a chargeback. VoltNest refunds are issued within **1–2 business 
days** of approval and appear on your statement within **5–7 business 
days** (card) or **3–5 business days** (PayPal).

*Used in*: [Return & Refund Policy](../policies/return_refund_policy.md), 
[Payment FAQ](../faqs/payment_faq.md)

### Reversal

A cancellation of a pending (uncaptured) authorization. Reversals 
are instant and don't involve money actually moving. Different from 
a refund (which reverses a posted charge).

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

## S

### Settlement

The final stage of a card transaction, where funds actually transfer 
from the customer's bank to VoltNest's bank. Settlement typically 
occurs 1–2 business days after capture.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

### Stripe

VoltNest's payment processor and gateway. Handles all card 
transactions and stores card tokens. **PCI-DSS Level 1** certified. 
VoltNest never sees or stores full card numbers.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Privacy Policy](../policies/privacy_policy.md)

## T

### Test Charge

A small ($1) authorization some banks place when you save a card for 
future use. Not a real charge — auto-releases within **3–5 business 
days**. Not initiated by VoltNest.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

### Token

An encrypted reference to a saved card. Tokens allow VoltNest to 
charge your saved card without storing the full card number. Created 
by Stripe. If a token is compromised, the actual card is still safe.

*Used in*: [Payment FAQ](../faqs/payment_faq.md), 
[Privacy Policy](../policies/privacy_policy.md)

### Tokenization

The process of replacing sensitive card data with a token. Allows 
secure storage of payment methods. VoltNest uses **Stripe 
tokenization** — the standard used by Amazon, Shopify, and most 
major retailers.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

## V

### Void

A cancellation of a transaction before settlement. Similar to a 
reversal. Void is used when the transaction hasn't been captured yet.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

## W

### Wallet (Digital Wallet)

A payment method that stores cards in a digital format for fast 
checkout. VoltNest accepts **Apple Pay** (iOS, macOS) and **Google 
Pay** (Android, Chrome). Wallet payments don't require 3D Secure.

*Used in*: [Payment FAQ](../faqs/payment_faq.md)

## Related
- [Shipping Terms](./shipping_terms.md)
- [Product Terms](./product_terms.md)
- [Payment FAQ](../faqs/payment_faq.md)
- [Payment Failures](../troubleshooting/payment_failures.md)
- [Return & Refund Policy](../policies/return_refund_policy.md)
- [Promo & Gift Card FAQ](../faqs/promo_giftcard_faq.md)
- [Privacy Policy](../policies/privacy_policy.md)
- [Contact VoltNest](../company/contact.md)