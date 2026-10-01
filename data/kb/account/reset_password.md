# Reset Password Guide

> **Category**: account  
> **Audience**: customer  
> **Last updated**: 2026-01-15

Step-by-step guide for resetting your VoltNest account password — 
whether you forgot it, want to change it voluntarily, or need to reset 
it after a security concern. Includes troubleshooting for common 
reset failures.

## Overview

There are **4 scenarios** for password reset. Find yours below:

| Scenario | Section |
|---|---|
| Forgot password — can't log in | A |
| Want to change password (logged in) | B |
| Reset email not arriving | C |
| Reset after account compromise | D |

**Related**: [Login Issues](../troubleshooting/login_issues.md) — for 
broader login troubleshooting.

## Before You Start

Quick checks:

- **Know your account email** — the one you used at signup. If not, 
  see Section C (Finding your account email).
- **Have access to that email inbox** — the reset link is sent there.
- **Don't have more than 5 failed logins in the last 15 minutes** — 
  account lockouts block password resets for 30 minutes. See 
  [Login Issues](../troubleshooting/login_issues.md) Step 4.
- **Use a private/trusted device** — don't reset on a shared computer.

## Section A: Forgot Password (Can't Log In)

The standard reset flow. Takes about 2 minutes.

### Steps

1. Go to **voltnest.com/login**
2. Click **"Forgot password?"** (below the password field)
3. Enter the email address on your account
4. Click **"Send Reset Link"**
5. Check your email — the reset message arrives within **5 minutes**
6. Open the email from **noreply@voltnest.com** with subject 
   "Reset your VoltNest password"
7. Click the **"Reset Password"** button
8. Enter your new password **twice** (must match)
9. Click **"Save Password"**
10. You'll be redirected to the login page — log in with your new 
    password

### Reset link validity
Reset links are valid for **1 hour**. If yours expires, return to 
Step 1 and request a new link.

### Password requirements
- At least **8 characters**
- At least **1 uppercase** letter
- At least **1 lowercase** letter
- At least **1 number**
- **No spaces**

### After reset
- All other sessions are **logged out** automatically (for security)
- You'll need to log in again on all devices
- Your password is changed immediately

### What if my email doesn't arrive?
See Section C (Reset Email Not Arriving).

## Section B: Change Password (Logged In)

If you can log in but want to change your password proactively:

### Steps

1. Log in to voltnest.com
2. Go to **Account → Security → Change Password**
3. Enter your **current password**
4. Enter your **new password** twice
5. Click **"Update Password"**

### You'll be asked to
- Enter the current password (proves it's you)
- Confirm the new password (twice)

### After changing
- All **other** sessions are logged out (except your current one)
- Your password is updated immediately
- A confirmation email is sent to your account email

### Common issues

**"Current password is incorrect"**
- Check caps lock
- Try typing the password in a text editor first, then paste
- If truly forgotten, use Section A instead

**"New password doesn't meet requirements"**
- See password rules above — the most common miss is the uppercase 
  or number requirement

**"New password can't be the same as the old one"**
- You must choose a genuinely new password

## Section C: Reset Email Not Arriving

If the reset email doesn't arrive within **15 minutes**:

### Step C1: Check spam/junk folder
System emails often get flagged. Search spam/junk for:
- "VoltNest"
- "noreply@voltnest.com"
- "Reset your password"

### Step C2: Check for typos in the email address
Did you enter the email correctly? Common issues:
- Missing a letter or dot
- Wrong domain (gmial.com vs. gmail.com)
- Old email you no longer use

### Step C3: Wait for provider delays
Some email providers (Outlook, Hotmail, Yahoo) delay system emails 
by **5–15 minutes**. Wait 15 minutes and re-check.

### Step C4: Check email filters
Custom filters may route unknown senders to specific folders. Search 
**all folders** for "VoltNest."

### Step C5: Whitelist our sender
Add **noreply@voltnest.com** to your contacts or safe-senders list, 
then request another reset email.

### Step C6: Try alternate email addresses
If you have multiple emails, try the reset with each one you may have 
used. The correct email will produce the reset email.

### Finding your account email
Not sure which email is on your account? Try:

1. **Search your inbox for "VoltNest"** — see which email received 
   our order confirmations
2. **Check your order confirmation emails** — the "to" field shows 
   your account email
3. **Search for "ORD-"** in your inbox — order IDs are unique to 
   VoltNest
4. **Check your browser's password manager** — may have saved the 
   email/password combo

### If nothing works
Contact support@voltnest.com with subject **"Password Reset Email Not 
Arriving"** and include:

- The email address you're trying to reset
- Which email provider it uses (Gmail, Outlook, etc.)
- Steps you've already tried
- Any order IDs you can find (helps verify identity)

**Response time**: Support can manually trigger a reset within **4 
business hours**.

## Section D: Reset After Account Compromise

If you believe someone else accessed your account:

### Immediate steps

1. **Reset your password immediately** using Section A
2. **Log out of all devices** — Account → Security → "Log out of all 
   devices"
3. **Enable 2FA** if not already on — see [Enable 2FA](./enable_2fa.md)
4. **Review recent orders** — Account → Orders → check for 
   unauthorized purchases
5. **Review saved payment methods** — remove any you don't recognize
6. **Check loyalty points** — Account → VoltNest Rewards → view 
   history

### Then contact support
Email support@voltnest.com with subject **"Account Compromise"**:

- Your account email
- Description of what you noticed
- Screenshots of suspicious activity
- Any unauthorized orders or point redemptions

**Response time**: **4 business hours** — this is an urgent case.

### What we do
- Lock the account temporarily
- Reverse unauthorized orders
- Reverse unauthorized point redemptions
- Issue a fresh password reset link from a trusted email
- Investigate the source of the compromise

**Related**: [Login Issues](../troubleshooting/login_issues.md), 
[Account FAQ](../faqs/account_faq.md)

## Section E: Password Reset Link Issues

### "The link says expired"

Reset links are valid for **1 hour**. If yours expired:

1. Return to **voltnest.com/login**
2. Click "Forgot password?" again
3. Request a new reset link
4. Use the new link **within 1 hour**

Don't use an old link — it will always fail.

### "The link says 'already used'"

Reset links are **single-use**. If you already reset your password 
with this link:

- Try logging in with the new password
- If you don't remember it, request a fresh reset link

### "The link opens a blank page"

Try:

- **Different browser** — Chrome, Firefox, Safari, Edge
- **Clear browser cookies** for voltnest.com
- **Disable extensions** — ad blockers and privacy tools can block 
  the redirect
- **Try incognito mode**
- **Copy the link** and paste it into a new browser tab

### "The link opens but shows a form error"

- **Fill both password fields** — the form requires both
- **Match the passwords** — they must be identical
- **Meet all requirements** — see password rules above
- **Check for trailing spaces** — copy-pasting sometimes includes them

## Section F: Reset on a New Device

You can reset your password from any device — laptop, phone, tablet.

### What to know
- You **don't need to be logged in** to reset
- The reset link works on any device
- The new password applies to all devices immediately
- All other sessions are logged out after reset

### Security tip
Use a **private network** (not public Wi-Fi) when resetting your 
password. Public Wi-Fi can be intercepted.

## Section G: Reset While Account is Locked

If your account was locked after **5 failed login attempts**, you 
cannot reset the password until the lock releases.

### What to do
1. **Wait 30 minutes** without any login attempts (attempts during 
   lockout reset the timer)
2. After 30 minutes, the lock auto-releases
3. Use Section A to reset your password
4. Log in with the new password

See [Login Issues](../troubleshooting/login_issues.md) Step 4 for 
full lockout troubleshooting.

## Section H: Prevent Future Password Issues

### Use a password manager
Recommendations:
- **1Password** (paid, excellent)
- **Bitwarden** (free, open source)
- **Dashlane** (paid)
- **Your browser's built-in manager** (Chrome, Safari, Firefox)

### Enable 2FA
Two-factor authentication prevents password theft from becoming 
account theft. See [Enable 2FA](./enable_2fa.md).

### Set up email account recovery
If you lose access to your email, you lose access to your VoltNest 
account. Ensure your email provider has backup recovery options.

### Don't reuse passwords
Use a unique password for VoltNest. If another site is breached, 
your VoltNest account stays safe.

## When to Contact Support

Contact support if:

- You've tried Sections A–G and still can't reset your password
- You don't know which email is on your account
- Reset emails aren't arriving after 30 minutes
- You've lost access to your account email inbox
- You suspect account compromise
- Your account is locked and the 30-minute wait doesn't help

### What to Include

1. **The email** you're trying to reset
2. **What happens** at each step
3. **Screenshots** of any errors
4. **Order ID** if you have one (helps verify identity — format: 
   `ORD-XXXXXX`)
5. **Full name** on the account

### How to Contact

- **Email**: support@voltnest.com, subject "Password Reset Issue"
- **Live chat**: voltnest.com/chat
- **Account compromise**: subject "Account Compromise" (URGENT)

### Response Time

- **Password reset issue**: 24 hours
- **Manual reset trigger**: 4 business hours
- **Account compromise**: 4 business hours
- **Lost email access**: 1 business day (requires identity verification)

## What NOT to Do

### ❌ Don't share your password or reset link with anyone
Not with "VoltNest support" (we never ask), not with a friend, not 
in an email or chat. Reset links are single-use and personal.

### ❌ Don't click reset links from emails you didn't request
If you didn't request a reset, someone may be attempting account 
access. Don't click — forward to security@voltnest.com.

### ❌ Don't reset on public Wi-Fi
Public networks can be intercepted. Use your home network or mobile 
data.

### ❌ Don't reuse your old password
You can't set the new password to match the old one. Choose something 
genuinely new.

### ❌ Don't reuse passwords from other sites
If another site is breached, your VoltNest account becomes vulnerable.

### ❌ Don't disable 2FA to "fix" password issues
This removes your strongest protection. Fix the underlying issue 
instead.

### ❌ Don't create a new account to avoid resetting
You'll lose order history, loyalty points, and warranty coverage. 
Always reset instead.

## For Support Agents

Internal notes for Tier 1 agents handling password reset requests.

### Triage Questions
- What email are you trying to reset?
- Have you checked spam/junk?
- Did you receive the reset email? What happens when you click?
- Have you requested a reset more than once?
- Are you locked out from failed attempts?
- Is this a suspected compromise?

### Tier 1 Scope
Tier 1 can resolve:
- Guiding through the standard reset flow
- Spam folder / whitelist guidance
- Link expiry explanation
- Basic browser troubleshooting
- Password rule clarification
- Manual reset trigger (if emails aren't arriving)

### Tier 2 Escalation Criteria
Escalate to Tier 2 when:
- Customer doesn't know the account email
- Customer lost access to the account email inbox
- Suspected account compromise
- Multiple manual reset attempts fail
- Account is locked beyond 30 minutes

### Manual Reset Trigger
If emails aren't arriving after 3+ attempts:

1. Verify identity (order ID, full name, billing address)
2. Trigger manual reset from backend
3. Send confirmation to customer
4. Do NOT share the new password — customer creates it

### Lost Email Access Protocol
If customer lost access to their account email:

1. Verify identity strongly:
   - Full name
   - Last order ID
   - Billing address
   - Last 4 digits of a payment method
2. If verified → change account email to a new one
3. Send password reset to the new email
4. Document in CRM

**Never** change an account email based on email alone.

### Do NOT Tell the Customer
- Do not share or generate a password for them — customer creates it
- Do not bypass identity verification
- Do not promise a specific fix time for compromised accounts
- Do not confirm the account email if the customer can't verify identity
- Do not tell them to create a new account — always reset instead

## Related
- [Create Account](./create_account.md)
- [Enable 2FA](./enable_2fa.md)
- [Delete Account](./delete_account.md)
- [Account FAQ](../faqs/account_faq.md)
- [Login Issues](../troubleshooting/login_issues.md)
- [Privacy Policy](../policies/privacy_policy.md)
- [Contact VoltNest](../company/contact.md)