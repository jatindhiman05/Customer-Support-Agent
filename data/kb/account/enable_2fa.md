# Enable 2FA Guide

> **Category**: account  
> **Audience**: customer  
> **Last updated**: 2026-01-15

Step-by-step guide for enabling, managing, and disabling two-factor 
authentication (2FA) on your VoltNest account. Includes backup codes, 
troubleshooting, and security best practices.

## Overview

Two-factor authentication (2FA) adds a second verification step when 
you log in — usually a 6-digit code from your phone. Even if someone 
steals your password, they can't access your account without the code.

**We strongly recommend enabling 2FA** if you:

- Store payment methods on your account
- Have order history or loyalty points worth protecting
- Use the same password across multiple sites
- Have ever been phished or hacked on another account

**What you need to enable 2FA**:

- Your phone (for SMS) OR an authenticator app
- Your VoltNest account password
- About 3 minutes

## Section A: 2FA Methods We Support

VoltNest supports two methods. Choose one:

| Method | How It Works | Security | Recommendation |
|---|---|---|---|
| **Authenticator app** | App generates 6-digit codes every 30 seconds | Highest | ⭐ Recommended |
| **SMS text message** | We text you a 6-digit code | Moderate | Fallback only |

### Why we recommend authenticator apps

- **Immune to SIM-swap attacks** (which defeat SMS 2FA)
- **Works offline** — no signal needed
- **Faster** — no waiting for SMS delivery
- **More reliable** — no dropped texts

### Supported authenticator apps

Any TOTP-compatible app works. Popular options:

- **Google Authenticator** (iOS, Android) — free
- **Authy** (iOS, Android, desktop) — free, syncs across devices
- **1Password** (bundled with the password manager)
- **Microsoft Authenticator** — free
- **Bitwarden Authenticator** — free

Pick one. All generate identical codes.

## Section B: Enable 2FA with Authenticator App (Recommended)

This is the recommended method. Takes about 3 minutes.

### Before you start

1. Install your chosen authenticator app
2. Have your VoltNest password ready (you'll re-enter it)
3. Be on the device where the app is installed

### Steps

1. **Log in** to voltnest.com
2. Go to **Account → Security → Two-Factor Authentication**
3. Click **"Enable 2FA"**
4. Select **"Authenticator App"**
5. A **QR code** appears on screen
6. **Open your authenticator app** and tap "Add account" or the "+" icon
7. Choose **"Scan QR code"** and scan the code on your screen
8. Your app now shows a 6-digit code that changes every 30 seconds
9. **Enter the code** in the field on voltnest.com
10. Click **"Verify"**

**You're now protected by 2FA.** You'll be prompted for a code the 
next time you log in.

### If you can't scan the QR code

Above the QR code, there's a link: **"Can't scan? Enter this code 
manually."** Click it to see a text code. In your authenticator app:

1. Choose "Enter code manually" or "Add account manually"
2. Enter the text code from voltnest.com
3. App generates the 6-digit codes normally

This is useful for desktop apps or if your camera doesn't work.

### Save your backup codes

**Immediately after enabling 2FA**, you'll see **10 backup codes** 
displayed on the screen. These let you log in if you lose your phone 
or authenticator app.

**Save them**:

- Download the text file
- Print them
- Store in a password manager
- Write them down and put them in a safe place

**Do not** store backup codes in:

- Your email inbox (if email is compromised, codes are too)
- A note-taking app on the same phone
- A screenshot on the same phone

Each backup code works **once**. Once used, it's invalid.

## Section C: Enable 2FA with SMS

If you prefer SMS or can't use an authenticator app.

### Before you start

1. Have your phone nearby
2. Have your VoltNest password ready

### Steps

1. **Log in** to voltnest.com
2. Go to **Account → Security → Two-Factor Authentication**
3. Click **"Enable 2FA"**
4. Select **"SMS Text Message"**
5. Enter your **phone number** (with country code)
6. Click **"Send Code"**
7. Check your phone for a 6-digit code
8. Enter the code on voltnest.com
9. Click **"Verify"**

**You're now protected by SMS 2FA.**

### SMS 2FA caveats

- **No signal** = no code (can't log in via this method)
- **SIM-swap attacks** can defeat SMS 2FA
- **Phone number changes** require updating before you lose access 
  to the old number
- **International travel** may delay SMS delivery

If any of these affect you, consider switching to an authenticator 
app.

### Save your backup codes

Same as Section B — 10 backup codes are shown after setup. Save them 
immediately.

## Section D: Save Your Backup Codes (Critical)

Whatever method you choose, **you must save backup codes**.

### What backup codes do
If you lose your phone or authenticator app, backup codes let you log 
in. Without them, you'll need to contact support to reset 2FA — which 
takes **1 business day** and requires identity verification.

### How to save them properly

**Do**:
- Print them and store in a safe (home safe, safety deposit box)
- Store in a password manager (1Password, Bitwarden)
- Write them down and put them somewhere only you can access

**Don't**:
- Email them to yourself
- Take a screenshot on the same phone with the authenticator app
- Store them in a note on the same phone
- Store them in your browser's saved passwords

### Where to find them later
**Account → Security → Two-Factor Authentication → View Backup Codes**

You can generate a fresh set at any time — but this **invalidates the 
previous 10 codes**. Only do this if you've lost your old set.

## Section E: Test 2FA After Enabling

**Test 2FA works** before you rely on it.

### How to test

1. **Log out** of voltnest.com
2. **Log back in** with your email and password
3. You'll be prompted for a **2FA code**
4. Open your authenticator app (or check SMS)
5. Enter the 6-digit code
6. You're logged in

If the code doesn't work, see Section G (Troubleshooting).

## Section F: Manage 2FA

### Change 2FA method

To switch from SMS to authenticator app (or vice versa):

1. Log in
2. Account → Security → Two-Factor Authentication
3. Click **"Change Method"**
4. Follow the setup flow for the new method

Your backup codes remain valid across methods.

### Add a second 2FA method

Currently VoltNest supports **one 2FA method at a time**. To switch, 
see "Change 2FA method" above.

### Regenerate backup codes

If you've lost or used most of your backup codes:

1. Log in
2. Account → Security → Two-Factor Authentication → View Backup Codes
3. Click **"Generate New Backup Codes"**
4. Save the new codes immediately

**Warning**: This invalidates the previous 10 codes.

### Disable 2FA

To disable 2FA entirely:

1. Log in
2. Account → Security → Two-Factor Authentication
3. Click **"Disable 2FA"**
4. Confirm with your **password** and a **current 2FA code**

**We strongly recommend against disabling 2FA.** It removes your 
account's strongest protection.

## Section G: Troubleshooting 2FA

### "The authenticator code is invalid"

Authenticator codes are **time-based** and expire every 30 seconds. 
Common causes:

- **Phone time is off** — Codes fail if your phone's clock is off by 
  more than 30 seconds
  - **Fix (iPhone)**: Settings → General → Date & Time → Set Automatically ON
  - **Fix (Android)**: Settings → System → Date & Time → Automatic ON
- **Wrong account** — If your app has multiple accounts, make sure 
  you're viewing the VoltNest code, not another site's
- **Code expired** — Wait for the next code (they refresh every 30 sec)
- **App needs sync** — In Google Authenticator: Settings → Time 
  correction for codes

### "The SMS code isn't arriving"

- Check your phone has **signal**
- Verify your phone number in Account → Security → Phone
- Wait **60 seconds**, then click "Resend Code"
- Restart your phone — clears SMS delivery issues
- If still no SMS, your carrier may be blocking short-code messages

**SMS codes expire after 5 minutes.**

### "I'm in a loop — can't log in, can't reset"

This can happen if you:
- Lost your phone
- Have no backup codes

**Recovery options**:

1. **Use a backup code** — enter one of your 10 saved codes
2. **If backup codes are lost** — contact support@voltnest.com with 
   subject "Lost 2FA Device — Reset Request"
   - Include: full name, last order ID, billing address, last 4 digits 
     of a payment method
   - We'll disable 2FA within **1 business day**
3. **After 2FA reset** — you'll be prompted to set up 2FA again on 
   next login

### "I lost my phone with the authenticator app"

Same as above — use backup codes, or contact support for a 2FA reset.

### "I changed my phone number"

If you still have access to your account:

1. Log in (2FA via the old method still works)
2. Account → Security → Phone → Update phone number
3. Verify the new number via SMS
4. Future SMS 2FA codes go to the new number

If you **lost access to the old number** and use SMS 2FA:

1. Use a backup code to log in
2. Update your phone number immediately
3. Generate new backup codes

### "I want to remove 2FA but can't log in"

You must log in to disable 2FA. If you can't log in, use a backup code 
or contact support for a 2FA reset.

### "Someone is asking for my 2FA code"

**This is a phishing attempt.** No legitimate VoltNest employee will 
ever ask for your 2FA code. If someone does:

1. Don't share the code
2. Report to security@voltnest.com
3. Change your password immediately

### "I received a 2FA code I didn't request"

Someone may be attempting to access your account.

1. **Do not approve** or share the code
2. **Change your password immediately**
3. **Review recent account activity** — Account → Orders
4. **Contact security@voltnest.com** — report the incident

## Section H: 2FA Best Practices

### Do:
- Use an **authenticator app** over SMS (more secure)
- Save **backup codes** in a safe place
- Keep your phone's **time synced** automatically
- Enable 2FA on **every account that offers it** (email, banking, 
  social media)
- Use **unique passwords** alongside 2FA

### Don't:
- Share 2FA codes with anyone — even if they claim to be support
- Screenshot codes and store on the same phone
- Use SMS if you're a high-risk target (journalists, execs, etc.)
- Disable 2FA because it's "inconvenient"

## When to Contact Support

Contact support if:

- You've lost your 2FA device and have no backup codes
- Your authenticator app produces invalid codes after time-sync
- You can't update your phone number for SMS 2FA
- You need 2FA reset after losing access
- You received an unexpected 2FA prompt (potential compromise)

### What to Include

1. **Account email**
2. **Full name**
3. **Last order ID** (format: `ORD-XXXXXX`)
4. **Billing address on file**
5. **Last 4 digits of a payment method** (if applicable)
6. **What happened** (lost phone, invalid codes, etc.)

### How to Contact

- **Email**: support@voltnest.com
- **2FA reset request**: subject "Lost 2FA Device — Reset Request"
- **Suspected compromise**: subject "Account Compromise" (URGENT)

### Response Time

- **2FA reset**: 1 business day
- **Suspected compromise**: 4 business hours
- **General 2FA question**: 24 hours

## What NOT to Do

### ❌ Don't share your 2FA code with anyone
Not with "VoltNest support," not with a bank, not with a friend. We 
never ask for 2FA codes.

### ❌ Don't screenshot backup codes on the same phone
If your phone is stolen, both the 2FA app and the codes are gone.

### ❌ Don't email backup codes to yourself
If your email is compromised, the codes are too. Save them offline.

### ❌ Don't disable 2FA because "it's annoying"
It takes 5 seconds per login to prevent account takeover. Keep it on.

### ❌ Don't reuse passwords even with 2FA
If someone has your password AND your 2FA method (e.g., via 
phishing), unique passwords still slow them down. 2FA + unique 
passwords together is best.

### ❌ Don't approve 2FA prompts you didn't trigger
If you get an unexpected "approve login" prompt, deny it and change 
your password. It means someone has your password.

### ❌ Don't store backup codes in a note-taking app on the same device
Same problem as screenshots — if the device is lost, everything is 
lost together.

## For Support Agents

Internal notes for Tier 1 agents handling 2FA requests.

### Triage Questions
- Did you enable 2FA? When?
- Which method — authenticator app or SMS?
- Are you getting a code but it's rejected, or no code at all?
- Do you have backup codes?
- Did you lose your phone or change your number?

### Tier 1 Scope
Tier 1 can resolve:
- Guiding through authenticator app setup
- Guiding through SMS setup
- Time-sync guidance for authenticator apps
- Backup code generation guidance
- Enabling/disabling 2FA while logged in
- Updating phone number while logged in

### Tier 2 Escalation Criteria
Escalate to Tier 2 when:
- Customer lost phone with 2FA and no backup codes
- Customer lost access to email that was used for SMS
- Authenticator app codes consistently invalid after time-sync
- Suspected account compromise

### Identity Verification Required
Before resetting 2FA, verify:

- Full name
- Last order ID
- Billing address on file
- Last 4 digits of a payment method

**Never** reset 2FA based on email alone. 2FA resets are high-risk — 
a bad reset is an account takeover.

### 2FA Reset Protocol

1. Verify identity (all 4 items above)
2. Confirm the request is legitimate (no red flags)
3. Disable 2FA on the account
4. Send a password reset link to the account email
5. Notify customer that 2FA is disabled and they should re-enable
6. Document in CRM with the verification steps completed

### Do NOT Tell the Customer
- Do not share or generate a 2FA code for them — codes are generated 
  only on their device or via SMS to their number
- Do not reset 2FA without full identity verification
- Do not tell them "we'll take care of it" without the verification
- Do not suggest third-party 2FA bypass tools (these don't exist 
  legitimately and are usually malware)

### Red Flags for Social Engineering
Watch for:
- Callers claiming to be "IT" or "VoltNest security" asking to reset 2FA
- Requests with urgency ("I need this now, I'm traveling")
- Slightly-mismatched identity details
- Requests to change the account email as part of a 2FA reset

When in doubt, require a callback or email verification to a known 
good address.

## Related
- [Create Account](./create_account.md)
- [Reset Password](./reset_password.md)
- [Delete Account](./delete_account.md)
- [Account FAQ](../faqs/account_faq.md)
- [Login Issues](../troubleshooting/login_issues.md)
- [Privacy Policy](../policies/privacy_policy.md)
- [Terms of Service](../policies/terms_of_service.md)
- [Contact VoltNest](../company/contact.md)