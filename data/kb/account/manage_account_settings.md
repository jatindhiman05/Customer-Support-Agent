# Manage Account Settings

> **Category**: account  
> **Audience**: customer  
> **Last updated**: 2026-01-15

Step-by-step guide for managing your VoltNest account settings — saved 
payment methods, addresses, email preferences, security settings, 
language, accessibility, and connected devices.

## Overview

Everything you can customize in your VoltNest account is controlled 
from **Account → Settings**. This guide walks through each section.

| Setting | Where | Section |
|---|---|---|
| Saved payment methods | Account → Payment Methods | A |
| Saved addresses | Account → Addresses | B |
| Email preferences | Account → Preferences → Email | C |
| Language | Account → Preferences → Language | D |
| Accessibility | Account → Preferences → Accessibility | E |
| Notification settings | Account → Preferences → Notifications | F |
| Connected devices | Account → Security → Sessions | G |
| Account email | Account → Settings → Email | H |
| Phone number | Account → Settings → Phone | I |

**Related**: [Create Account](./create_account.md), 
[Reset Password](./reset_password.md), [Enable 2FA](./enable_2fa.md), 
[Delete Account](./delete_account.md)

## Section A: Payment Methods

Manage cards, PayPal, Apple Pay, and Google Pay on your account.

### A1. Add a payment method

1. Log in to voltnest.com
2. Go to **Account → Payment Methods**
3. Click **"Add Payment Method"**
4. Choose the type:
   - **Card** — enter card number, expiry, CVV, billing address
   - **PayPal** — you'll be redirected to log in to PayPal
   - **Apple Pay / Google Pay** — follow the device prompt
5. Click **"Save"**
6. You may see a **$1 temporary authorization** (auto-releases in 
   3–5 business days — see [Payment FAQ](../faqs/payment_faq.md))

**Security note**: We never store your full card number. Payment 
details are tokenized by Stripe (PCI-DSS Level 1).

### A2. Set a default payment method

1. Go to **Account → Payment Methods**
2. Find the method you want as default
3. Click **"Set as Default"**

The default is pre-selected at checkout. You can always choose a 
different method at checkout.

### A3. Remove a payment method

1. Go to **Account → Payment Methods**
2. Find the method
3. Click **"Remove"**
4. Confirm

**Note**: You cannot remove a payment method that's being used on a 
pending order. Wait for the order to complete first.

### A4. Update an expiring card

When your card is near expiry, we'll email you a reminder. To update:

1. Go to **Account → Payment Methods**
2. Click the card
3. Click **"Update Card"**
4. Enter new expiry, and re-verify with the CVV
5. Save

If the card has already expired, remove it and add the new one.

### A5. What if a payment method is declined?

Declines happen on your bank's side — see 
[Payment Failures](../troubleshooting/payment_failures.md) for 
troubleshooting.

### A6. Saved payment method limits

- Up to **5 saved cards** per account
- **1 PayPal** account link
- Apple Pay and Google Pay methods are managed by your device, not by 
  us

## Section B: Addresses

Save shipping addresses for faster checkout.

### B1. Add a shipping address

1. Go to **Account → Addresses**
2. Click **"Add New Address"**
3. Enter:
   - Full name
   - Street address (line 1 and line 2 if needed)
   - City, state/province, postal code
   - Country
   - Phone number (for carrier contact)
4. Check **"Set as default"** if you want this to be the default 
   shipping address
5. Click **"Save"**

### B2. Set a default address

1. Go to **Account → Addresses**
2. Find the address
3. Click **"Set as Default"**

The default address is auto-selected at checkout.

### B3. Edit an address

1. Go to **Account → Addresses**
2. Click the address
3. Click **"Edit"**
4. Change any field
5. Save

**Note**: Editing an address does **not** change orders already 
placed. See [Modify Order Guide](../order_management/modify_order_guide.md) 
for changing the address on an existing order.

### B4. Delete an address

1. Go to **Account → Addresses**
2. Find the address
3. Click **"Delete"**
4. Confirm

You cannot delete an address that's currently the default. Set a new 
default first.

### B5. Address limits

- Up to **10 saved addresses** per account

### B6. Billing vs. shipping addresses

These are **separate**:

- **Shipping address** — where orders are delivered
- **Billing address** — must match your bank's records for the card to 
  work

You can have different billing and shipping addresses. The billing 
address is set per payment method, not per account.

## Section C: Email Preferences

Control which emails you receive.

### C1. Manage marketing emails

1. Go to **Account → Preferences → Email**
2. Toggle each category on or off:
   - **Promotional offers** — sales, discounts, coupons
   - **Product launches** — new product announcements
   - **Loyalty program updates** — points, tiers, rewards
   - **Newsletter** — monthly digest
   - **Refer-a-friend reminders** — nudges to share your referral link
3. Save

### C2. Transactional emails (cannot be disabled)

These are required for the order to function:

- Order confirmations
- Shipping notifications
- Delivery confirmations
- Refund confirmations
- Warranty claim updates
- Password reset emails
- Account security alerts

You **cannot** unsubscribe from transactional emails while you have 
an active account. Deleting your account removes you from all emails.

### C3. Change the email on your account

See Section H (Account Email).

### C4. Unsubscribe from all marketing in one click

Every marketing email has an **"Unsubscribe"** link at the bottom. 
Click it to opt out of that category (or all marketing).

Clicking unsubscribe in one email doesn't affect transactional emails.

## Section D: Language & Region

### D1. Change the display language

Currently supported languages:

- **English** (default)
- Spanish and French are planned for late 2026

To change (when available):

1. Go to **Account → Preferences → Language**
2. Select your language
3. Save

### D2. Change currency display

VoltNest prices are shown in **USD only**. We do not support other 
currencies.

Your bank converts USD to your local currency. See 
[International FAQ](../faqs/international_faq.md).

### D3. Change time zone

Used for order notifications and support hours display.

1. Go to **Account → Preferences → Region**
2. Select your time zone
3. Save

## Section E: Accessibility

VoltNest supports accessibility preferences for all customers.

### E1. Enable high-contrast mode

1. Go to **Account → Preferences → Accessibility**
2. Toggle **"High-Contrast Mode"**
3. Save

### E2. Enlarge text

1. Go to **Account → Preferences → Accessibility**
2. Choose text size: **Small / Medium / Large / Extra-Large**
3. Save

### E3. Reduce motion

For users sensitive to animations:

1. Go to **Account → Preferences → Accessibility**
2. Toggle **"Reduce Motion"**
3. Save

This minimizes animated transitions and auto-playing videos.

### E4. Screen reader optimizations

Our site follows **WCAG 2.1 AA** guidelines and works with screen 
readers (VoiceOver, NVDA, JAWS, TalkBack).

For screen-reader-specific issues:

- Email **accessibility@voltnest.com**
- Response within **5 business days**
- See [General FAQ](../faqs/general_faq.md) for details

### E5. Keyboard navigation

All site functions are keyboard-accessible. Use **Tab** to move 
between fields, **Enter** to activate buttons, and **Esc** to close 
modals.

## Section F: Notification Settings

Control **how** and **when** we notify you (separate from email 
preferences).

### F1. Order updates

- **Email** — on by default, cannot be disabled
- **SMS** — opt-in (requires phone number on account)
- **Push (mobile app)** — opt-in via app settings

### F2. Shipment notifications

- **Email** — on by default
- **SMS** — opt-in, includes delivery-day alerts
- **Push** — opt-in via app

### F3. Price drop notifications

Get notified when a product on your wishlist drops in price:

1. Account → Preferences → Notifications
2. Toggle **"Price Drop Alerts"** on

### F4. Back-in-stock notifications

Get notified when an out-of-stock item returns:

1. Go to the product page
2. Click **"Notify Me When Available"**
3. Notifications come via email

### F5. Referral reminders

Occasional nudges to share your referral link. Toggle off in 
Section C1.

## Section G: Security & Sessions

### G1. View active sessions

See every device currently logged into your account:

1. Go to **Account → Security → Sessions**
2. Each session shows:
   - Device / browser
   - Approximate location
   - Last activity time

### G2. Log out of a specific session

1. Go to **Account → Security → Sessions**
2. Find the session
3. Click **"Log Out"**

### G3. Log out of all other sessions

For security after suspected compromise:

1. Go to **Account → Security → Sessions**
2. Click **"Log Out of All Other Devices"**
3. All sessions except the current one are ended

### G4. Change password

See [Reset Password Guide](./reset_password.md) Section B.

### G5. Enable or manage 2FA

See [Enable 2FA Guide](./enable_2fa.md).

### G6. Session expiry

Sessions expire after **30 days of inactivity**. Trusted devices can 
stay logged in longer if you checked **"Keep me signed in"** at login.

### G7. Trusted devices

If you log in from a new device, you may be asked to verify via email. 
Trusted devices skip this step. Manage trusted devices:

1. Account → Security → Trusted Devices
2. Remove any you don't recognize

## Section H: Account Email

### H1. Change the email on your account

1. Log in to voltnest.com
2. Go to **Account → Settings → Email**
3. Click **"Change Email"**
4. Enter the new email address
5. Verify via link sent to your **new** email
6. Then verify via link sent to your **old** email
7. The change is completed within **1 business day**

Both emails must be verified for the change to take effect — this 
prevents account takeover via email change.

**Note**: Changing your account email does **not** change the email 
on existing orders. See 
[Modify Order Guide](../order_management/modify_order_guide.md).

### H2. If you can't access your old email

You cannot change the email without access to both. Options:

1. Recover access to the old email (contact your email provider)
2. Contact support@voltnest.com for assistance with strong identity 
   verification (order ID, billing address, payment method)

We never change account email based on a new email alone.

## Section I: Phone Number

### I1. Add or change your phone number

1. Go to **Account → Settings → Phone**
2. Enter or edit your phone number
3. Verify via a 6-digit SMS code
4. Save

The phone number is used for:

- SMS 2FA (if enabled — see [Enable 2FA](./enable_2fa.md))
- Delivery notifications from the carrier
- Urgent support contact

### I2. Remove your phone number

1. Account → Settings → Phone
2. Click **"Remove"**
3. Confirm

**Note**: If you use **SMS 2FA**, removing your phone number disables 
SMS 2FA. You'll need to switch to an authenticator app or re-enable 
2FA with a new number.

### I3. Phone number format

Include country code (e.g., +1 for US). We support numbers in all 
countries we ship to.

## Section J: Privacy & Data

### J1. Download your data

Request a copy of all personal data we hold:

1. Go to **Account → Privacy → Download Data**
2. Click **"Request Data Export"**
3. Receive an email within **30 days** with a download link

See [Privacy Policy](../policies/privacy_policy.md) for full details.

### J2. Delete your account

See [Delete Account Guide](./delete_account.md).

### J3. Delete chat history

Email privacy@voltnest.com with subject "Delete Chat History."

### J4. Cookie preferences

Manage cookies at any time:

1. Go to **Account → Privacy → Cookies**
2. Adjust categories (essential cannot be disabled)
3. Save

For first-time visitors, a cookie banner appears on the site.

## Section K: Referral Program

Manage your refer-a-friend link and settings.

### K1. Find your referral link

1. Go to **Account → Refer a Friend**
2. Copy your unique link
3. Share it

### K2. Track referral earnings

1. Account → Refer a Friend → History
2. See pending, confirmed, and expired referrals

See [Promo & Gift Card FAQ](../faqs/promo_giftcard_faq.md) for 
details on how referral rewards work.

## When to Contact Support

Contact support if:

- A setting won't save
- You can't remove a payment method or address
- You can't change your email (lost access to old email)
- Accessibility features aren't working as expected
- You suspect unauthorized changes to your account
- You need a setting that isn't available in your account

### What to Include

1. **Account email**
2. **Which setting** you're trying to change
3. **What happens** when you try
4. **Screenshots** if helpful

### How to Contact

- **Email**: support@voltnest.com, subject "Account Settings Issue"
- **Accessibility**: accessibility@voltnest.com
- **Privacy**: privacy@voltnest.com
- **Live chat**: voltnest.com/chat

### Response Time

- **General settings issues**: 24 hours
- **Accessibility issues**: 5 business days
- **Email change (verification)**: 1 business day
- **Data export**: 30 days

## What NOT to Do

### ❌ Don't share your password or 2FA codes when changing settings
We never ask for either. Only email verification or order ID are used 
for sensitive changes.

### ❌ Don't ignore suspicious session activity
If you see an unfamiliar device in **Account → Security → Sessions**, 
log it out and change your password immediately.

### ❌ Don't save the same card on multiple accounts
Card saving is per-account. If you want a card available everywhere, 
use PayPal or Apple/Google Pay instead.

### ❌ Don't remove your phone number if you use SMS 2FA
This disables SMS 2FA and may lock you out. Switch to an authenticator 
app first.

### ❌ Don't change your email without verifying both addresses
Skipping verification can lock you out of your account.

### ❌ Don't delete an address that's on a pending order
The order will fail to process. Wait for the order to ship or cancel 
it first.

### ❌ Don't disable transactional emails
You can't. They're required for orders to function. If you want no 
emails at all, delete your account.

## For Support Agents

Internal notes for Tier 1 agents handling account settings requests.

### Triage Questions
- Which setting are you trying to change?
- What happens when you try?
- Are you seeing an error message? (screenshot)
- Have you tried a different browser or device?
- Is this about payments, addresses, email, security, or preferences?

### Tier 1 Scope
Tier 1 can resolve:
- Guiding through each settings section
- Explaining limits (5 cards, 10 addresses)
- Transactional email clarification
- Session management guidance
- Accessibility preference guidance
- Cookie preference guidance

### Tier 2 Escalation Criteria
Escalate to Tier 2 when:
- Email change requires assistance (lost old email access)
- Suspected unauthorized changes to account
- Data export requests (route to privacy@)
- Bug preventing settings changes from saving
- Accessibility bug reports

### Do NOT Tell the Customer
- Do not change account email without full verification (both 
  addresses)
- Do not disable transactional emails for a customer
- Do not remove a payment method that's on a pending order
- Do not share saved payment method details (last 4 digits only)
- Do not process DSAR requests directly — route to privacy@

### Privacy Request Routing

| Request | Route To |
|---|---|
| Delete account | privacy@voltnest.com |
| Data export (DSAR) | privacy@voltnest.com |
| Delete chat history | privacy@voltnest.com |
| Accessibility bug | accessibility@voltnest.com |
| General settings | support@voltnest.com |

### Address Change Rules
Address changes **do not affect** existing orders. If a customer 
wants to change an order's address:

1. Check order status (see [Order Status Guide](../order_management/order_status_guide.md))
2. If not shipped → use [Modify Order Guide](../order_management/modify_order_guide.md)
3. If shipped → carrier intercept ($15, not guaranteed)

## Related
- [Create Account](./create_account.md)
- [Reset Password](./reset_password.md)
- [Enable 2FA](./enable_2fa.md)
- [Delete Account](./delete_account.md)
- [Account FAQ](../faqs/account_faq.md)
- [Payment FAQ](../faqs/payment_faq.md)
- [International FAQ](../faqs/international_faq.md)
- [Privacy Policy](../policies/privacy_policy.md)
- [Contact VoltNest](../company/contact.md)