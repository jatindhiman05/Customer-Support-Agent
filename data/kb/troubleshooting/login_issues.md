# Login Issues (Troubleshooting)

> **Category**: troubleshooting  
> **Audience**: customer, agent  
> **Last updated**: 2026-01-15

Diagnostic guide for problems signing in to your VoltNest account — 
forgotten passwords, invalid credentials, 2FA codes not arriving, 
account lockouts, and browser-specific login failures. Follow the 
steps in order.

## Symptoms This Guide Covers

Use this guide if you're experiencing any of the following:

- "Invalid email or password" error when you know your credentials are correct
- Password reset email never arrives
- Password reset link says "expired"
- 2FA code doesn't arrive by SMS
- 2FA code from authenticator app is "invalid"
- Account is locked after too many failed attempts
- You're logged out immediately after logging in
- Login works on one browser but not another
- Login works on mobile but not desktop (or vice versa)
- You see "Your session has expired" repeatedly

If the app won't open at all, see 
[App Not Loading](./app_not_loading.md) instead.

If you suspect your account was compromised (someone else accessed it), 
see the **Compromised Account** section below.

## Before You Start

Quick facts:

- Passwords are **case-sensitive**
- Reset links are valid for **1 hour**
- Accounts lock after **5 failed login attempts** in 15 minutes
- Sessions expire after **30 days of inactivity**
- 2FA codes expire after **30 seconds** (authenticator apps)

Check these before continuing:
- **Caps Lock** is off
- You're using the correct email (the one on your account)
- Your internet connection is working

## Step 1: Confirm You're Using the Right Email

Most "invalid credentials" errors are because the customer is using a 
different email than what's on their account.

Try these:

- **Check your order confirmation emails** — the "from" address is 
  support@voltnest.com, but the "to" address is your account email
- **Search your inbox for "VoltNest"** — see which address received 
  our emails
- **Try alternate emails** — personal, work, or old email addresses 
  you may have used

If you're still not sure which email is on your account, contact 
support@voltnest.com and we'll help identify it (you'll need to verify 
your identity — see below).

## Step 2: Reset Your Password

If you know your account email but not the password, use the reset 
flow.

### Steps
1. Go to **voltnest.com/login**
2. Click **"Forgot password?"**
3. Enter the email address on your account
4. Check your inbox for the reset email (arrives within 5 minutes)
5. Click the reset link
6. Enter a new password twice to confirm

### Password requirements
- At least **8 characters**
- At least **1 uppercase letter**
- At least **1 number**
- No spaces

### Reset link validity
Reset links expire after **1 hour**. If yours expired, repeat Step 2 
to generate a new one.

## Step 3: Password Reset Email Not Arriving

If the reset email doesn't arrive within 15 minutes:

### 3a. Check your spam/junk folder
System emails sometimes get flagged. Search spam for "VoltNest" or 
"noreply@voltnest.com."

### 3b. Check for typos
Did you enter the email correctly? Check for missing letters, 
misplaced dots, or missing domain parts (e.g., "gmial.com" vs. 
"gmail.com").

### 3c. Wait longer — provider delays
Some email providers (especially Outlook, Hotmail, and Yahoo) delay 
system emails by 5–15 minutes. Wait 15 minutes, then re-check.

### 3d. Check email filters
Some users have filters that route emails from unknown senders to 
specific folders. Search for "VoltNest" in all folders.

### 3e. Try a different email address
If you have multiple emails, try the reset with each. The correct 
email will produce the reset email.

### 3f. Whitelist our sender
Add **noreply@voltnest.com** to your contacts or safe-senders list, 
then try again.

If none of these work, contact support@voltnest.com with subject 
"Password Reset Email Not Arriving." Include:

- The email address you're trying to reset
- Which provider it is (Gmail, Outlook, etc.)
- Steps you've already tried

We can trigger a manual reset within **4 business hours**.

## Step 4: Account Locked After Failed Attempts

After **5 failed login attempts within 15 minutes**, your account is 
temporarily locked for **30 minutes**.

### What to do
1. **Wait 30 minutes** without trying again
2. After 30 minutes, the lock auto-releases
3. Reset your password (Step 2) — don't try the old password again
4. Log in with the new password

### Important: Don't keep trying
Each failed attempt during the lockout period **resets the 30-minute 
timer**. If you keep trying every few minutes, the lock will keep 
extending. Wait the full 30 minutes without any attempts.

### If the lock persists beyond 30 minutes
Contact support@voltnest.com with subject "Account Locked." We can 
manually unlock within **1 business day** after verifying your identity.

## Step 5: 2FA Code Issues

### 5a. SMS code not arriving
- Check your phone has signal
- Verify the phone number on your account (**Account → Security → Phone**)
- Wait 60 seconds, then request a new code
- Restart your phone — clears SMS delivery issues

SMS codes expire after **5 minutes**. If yours expired, request a new 
one.

### 5b. Authenticator app code says "invalid"
Authenticator codes are time-based and expire after **30 seconds**. 
If your code is rejected:

- **Check your phone's time** — the app must be in sync. If your 
  phone's clock is off by more than 30 seconds, codes will fail
- **Sync the app** — in Google Authenticator, tap Settings → 
  "Time correction for codes"
- **Try the next code** — wait for the current code to refresh, then 
  use the fresh one
- **Reinstall the authenticator** — only as a last resort, using your 
  backup codes first

### 5c. Lost phone with authenticator app
Use your **backup codes**. When you enabled 2FA, you received 
10 one-time backup codes. Each works once.

If you've lost your backup codes:

1. Email support@voltnest.com from the email on your account
2. Subject: "Lost 2FA Device — Reset Request"
3. Provide verification:
   - Full name
   - Last order ID (format: `ORD-XXXXXX`)
   - Billing address on file
   - Last 4 digits of a payment method
4. We'll disable 2FA within **1 business day**

### 5d. Backup codes not working
Backup codes are **single-use**. If you've used all 10, you'll need 
to reset 2FA through support (see 5c). 

You can generate a fresh set of backup codes at **Account → Security → 
Two-Factor Authentication → Generate New Backup Codes**, but only 
while you're logged in. Do this now if you haven't.

## Step 6: You Log In But Get Logged Out Immediately

### 6a. Check "Keep me signed in"
If you don't check **"Keep me signed in"** at login, your session 
expires quickly. Check the box next time you log in.

### 6b. Browser cookie settings
If your browser blocks cookies from voltnest.com, you can't stay 
logged in.

- **Chrome**: Settings → Privacy → Cookies → Allow voltnest.com
- **Safari**: Preferences → Privacy → Manage Website Data → Add 
  voltnest.com
- **Firefox**: Settings → Privacy → Cookies and Site Data → Manage 
  Exceptions

### 6c. Private/Incognito mode
Browsing in incognito mode clears cookies when the window closes. Log 
in using a regular browser window.

### 6d. VPN or unusual IP
If you're using a VPN, our security system may require re-verification 
each time your IP changes. Try disabling the VPN and logging in.

## Step 7: Login Works in One Place But Not Another

### Works on mobile but not desktop (or vice versa)
This is usually a browser cache issue on the failing device. Try:

- **Clear browser cache** for voltnest.com
- **Try a different browser** (Chrome, Firefox, Safari, Edge)
- **Disable browser extensions** — especially ad blockers and 
  privacy tools

### Works in one browser but not another
- The failing browser may have an outdated version — update it
- A browser extension may be interfering — test in a fresh profile 
  or incognito mode
- Cookie settings differ between browsers — check per Step 6b

### Works on Wi-Fi but not cellular (or vice versa)
- Some corporate/network firewalls block certain sites — try on a 
  different network
- Mobile carriers rarely block sites, but check your data connection

## Compromised Account

If you suspect someone else accessed your account:

### Immediate steps
1. **Change your password** at voltnest.com/login
2. **Log out of all devices** at Account → Security
3. **Enable 2FA** if it's not already on
4. **Review recent orders** at Account → Orders for unauthorized purchases
5. **Check saved payment methods** — remove any you don't recognize

### Then contact support
Email support@voltnest.com with subject **"Account Compromise"**:

- Your account email
- Description of what you noticed
- Screenshots of suspicious activity

We respond within **4 business hours** for verified account 
compromises and will:

- Lock the account temporarily
- Reverse any unauthorized orders
- Reverse any unauthorized point redemptions
- Issue a new password reset link from a trusted email

## When to Escalate to Support

Contact support if you've completed Steps 1–7 and still can't log in.

### What to Include

1. **Account email** (the one you're trying to log in with)
2. **Device and browser** (e.g., "iPhone 14 Safari", "Windows 11 Chrome")
3. **What happens** when you try (error message, blank page, etc.)
4. **A screenshot** of the error, if any
5. **Steps you've already tried** (Steps 1–7)
6. **Whether the issue is on one device or all**

### How to Contact

- **Email**: support@voltnest.com, subject "Login Issue"
- **Live chat**: voltnest.com/chat (mention login issue)

### Response Time

- **Standard login issue**: Within 24 hours
- **Account lockout**: Within 1 business day
- **Suspected compromise**: Within 4 business hours (mark URGENT)
- **2FA reset request**: Within 1 business day

## What NOT to Do

### ❌ Don't share your password with anyone
Not with "VoltNest support" (we never ask), not with a "friend who 
can help," not in a chat or email. VoltNest staff will never ask for 
your password.

### ❌ Don't click login links from emails or texts
Legitimate VoltNest emails only link to password reset pages, and 
only when you requested one. If you receive a login link you didn't 
request, it's phishing — forward to security@voltnest.com.

### ❌ Don't keep trying the wrong password
5 failed attempts locks your account for 30 minutes, and each new 
attempt during the lockout **resets the timer**. Wait the full 30 
minutes without trying.

### ❌ Don't disable 2FA to "fix" login issues
This doesn't fix login problems and removes your account's best 
security protection. Fix the underlying issue instead.

### ❌ Don't use the same password across sites
If another site is breached, your VoltNest account becomes vulnerable. 
Use a unique password or a password manager.

### ❌ Don't post your email publicly when asking for help
Social media questions should include only the general nature of the 
issue. Send account-specific details to support@voltnest.com only.

## For Support Agents

Internal notes for Tier 1 and Tier 2 agents handling login issues.

### Triage Questions
- What email are you trying to log in with?
- Have you successfully logged in with this account before?
- Do you see an error message? What does it say?
- Have you tried resetting your password?
- Are you using 2FA? Which method (SMS or app)?
- Have you successfully logged in before from this device/browser?

### Tier 1 Scope
Tier 1 can resolve:
- Password reset flow guidance
- Session/keep-me-signed-in confusion
- Browser cookie settings guidance
- 2FA code timing guidance
- Password requirements clarification

### Tier 2 Escalation Criteria
Escalate to Tier 2 when:
- Password reset email not arriving after 3 attempts
- 2FA device lost and backup codes unavailable
- Account lockout persisting beyond 30 minutes
- Suspected account compromise
- Login works for us (backend) but not for customer after all steps

### Identity Verification Required
Before resetting 2FA or unlocking accounts, verify:

- Full name
- Last order ID
- Billing address on file
- Last 4 digits of a payment method

**Never** reset 2FA or unlock accounts based on email alone.

### Do NOT Tell the Customer
- Do not ask for their password — ever
- Do not promise a fix time unless it's within our stated SLA
- Do not suggest disabling 2FA
- Do not ask them to click login links you generate manually

### Compromised Account Escalation
Account compromise is a **4 business hour SLA**. Flag the ticket 
URGENT. Reverse orders and point redemptions the same business day.

## Related
- [App Not Loading](./app_not_loading.md)
- [Account FAQ](../faqs/account_faq.md)
- [Enable 2FA Guide](../account/enable_2fa.md)
- [Reset Password Guide](../account/reset_password.md)
- [Terms of Service](../policies/terms_of_service.md)
- [Contact VoltNest](../company/contact.md)