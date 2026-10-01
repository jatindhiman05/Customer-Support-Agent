# App Not Loading (Troubleshooting)

> **Category**: troubleshooting  
> **Audience**: customer, agent  
> **Last updated**: 2026-01-15

Diagnostic guide for the VoltNest mobile app when it won't open, gets 
stuck on the splash screen, crashes on launch, or freezes shortly 
after opening. Follow the steps in order — most issues resolve at 
Step 1 or 2.

## Symptoms This Guide Covers

Use this guide if you're experiencing any of the following:

- App icon taps but nothing happens
- App gets stuck on the VoltNest splash screen (logo showing)
- App crashes immediately after opening
- App freezes within 10 seconds of opening
- App opens but shows a blank white or black screen
- App displays "Something went wrong" on launch
- App opens but won't load product pages

If your issue is **login-related** (app opens, but you can't log in), 
see [Login Issues](./login_issues.md) instead.

## Before You Start

Quick facts:

- The VoltNest app is available on **iOS 14+** and **Android 9+**
- Latest app version is **3.4.0** (as of January 2026)
- If you're on an older OS or older app version, that's likely the cause

## Step 1: Confirm the Basics

Before diving into fixes, check these four things. They resolve most 
issues.

### 1a. Is your operating system supported?

- **iOS**: 14.0 or later
- **Android**: 9.0 (Pie) or later

To check:
- **iPhone**: Settings → General → About → iOS Version
- **Android**: Settings → About Phone → Android Version

If your OS is older than the minimum, the app will not run. Update 
your OS or use **m.nimbustech.com** in your mobile browser instead.

### 1b. Is the app updated to the latest version?

Latest version: **3.4.0**

To check:
- **iPhone**: Open App Store → search "VoltNest" → if it says "Update," tap it
- **Android**: Open Play Store → search "VoltNest" → if it says "Update," tap it

Update the app and try opening it again.

### 1c. Is your device connected to the internet?

The app requires an internet connection to launch. Check:

- Wi-Fi is connected
- Or cellular data is enabled
- Try loading a website in your browser to confirm connectivity

### 1d. Has the app ever worked on this device?

- **Yes, worked before** → Continue to Step 2
- **No, never worked** → Skip to Step 4 (Known Issues)

## Step 2: Force Close and Reopen

This clears any temporary glitch in the app's memory.

### iPhone
1. Swipe up from the bottom of the screen and pause
2. Swipe the VoltNest app card up to close it
3. Wait 5 seconds
4. Tap the app icon to reopen

### Android
1. Open Settings → Apps → VoltNest
2. Tap "Force Stop"
3. Wait 5 seconds
4. Tap the app icon to reopen

If the app opens normally after this, the issue is resolved. If not, 
continue to Step 3.

## Step 3: Clear the App Cache

Cached data can become corrupted after updates and cause launch 
failures.

### Android
1. Settings → Apps → VoltNest → Storage
2. Tap **"Clear Cache"** (NOT "Clear Data" — see warning below)
3. Reopen the app

⚠️ **Do not tap "Clear Data"** — that logs you out and deletes your 
locally saved preferences (saved addresses, payment methods, loyalty 
display). Clearing cache is safe and won't log you out.

### iPhone
iOS does not expose a cache-clearing option. Skip to Step 4.

After clearing the cache, reopen the app. If the problem persists, 
continue.

## Step 4: Reinstall the App

A fresh install fixes most remaining issues.

### Steps
1. **Uninstall** the VoltNest app from your device
2. **Restart your device** (important — don't skip)
3. **Reinstall** the app from the App Store or Play Store
4. **Log in** with the same account email and password

### Will I lose anything?
No. Your account, orders, loyalty points, and saved addresses are 
stored on our servers — not on your phone. Everything returns after 
you log in.

**Do not** reinstall if you don't remember your password. Reset your 
password first via **voltnest.com/login**.

## Step 5: Try the Web App

While diagnosing the mobile app, you can use **m.voltnest.com** in 
your mobile browser. It has most of the same features:

- Shop and checkout
- View orders and tracking
- Contact support
- View loyalty points

This isn't a fix, but it lets you place orders while we resolve the 
app issue.

## Step 6: Check for Known Issues

Known active issues (as of **2026-01-15**):

### iOS 17.2 crash on launch
- **Affected**: iPhone users on iOS 17.2 (released Dec 2025)
- **Symptom**: App crashes immediately after tapping the icon
- **Status**: Fix in v3.4.1, releasing **2026-01-20**
- **Workaround**: Use m.voltnest.com, or update your iOS to 17.3 when 
  available

### Android 14 + Samsung One UI 6 splash hang
- **Affected**: Samsung devices on Android 14 with One UI 6
- **Symptom**: First launch after install hangs on splash screen for 
  up to 30 seconds
- **Status**: Under investigation with Samsung
- **Workaround**: Wait it out — subsequent launches are normal

### Android "Something went wrong" on Pixel 8
- **Affected**: Pixel 8 and 8 Pro on Android 14
- **Symptom**: Error message appears within 5 seconds of launch
- **Status**: Fix in v3.4.1
- **Workaround**: Clear app cache (Step 3), then reopen

If you're affected by a known issue, you don't need to contact 
support — we're already working on it. Check back after the fix date.

## Step 7: When to Escalate to Support

If you've completed Steps 1–6 and the app still won't open, contact 
support with the following details.

### What to Include

1. **Device model** (e.g., "iPhone 14 Pro", "Samsung Galaxy S23")
2. **OS version** (e.g., "iOS 17.2", "Android 14, One UI 6.0")
3. **App version** (find in the app's settings or about page)
4. **A screenshot or screen recording** of the issue
5. **Steps you've already tried** (Steps 1–6)
6. **Whether the app ever worked** on this device

### How to Contact

- **Email**: support@voltnest.com, subject "App Not Loading"
- **Live chat**: voltnest.com/chat (mention the app issue)
- **In-app**: If the app opens briefly, use Help → Contact Support

### Response Time

- **Standard**: Within 24 hours
- **If your issue is blocking an urgent order**: Mark your email 
  **URGENT** for a 4 business hour response

Tier 2 app specialists respond within **4 business hours** for 
escalated app issues.

## What NOT to Do

Avoid these — they make things worse and can cause data loss.

### ❌ Don't tap "Clear Data" on Android
Clearing data (not cache) logs you out, deletes local preferences, 
and doesn't fix app launch issues. Only "Clear Cache" is safe.

### ❌ Don't reinstall if you don't know your password
Reset your password first at **voltnest.com/login**. Otherwise you'll 
be locked out of your account with no way to log in.

### ❌ Don't install "cache cleaner" apps from third parties
These apps can damage your device, request unnecessary permissions, 
and don't fix VoltNest-specific issues. Only use the built-in Android 
settings.

### ❌ Don't factory reset your phone
This is never necessary for an app issue and will delete everything 
on your device. No VoltNest support agent will ask you to do this.

### ❌ Don't sideload the app from third-party sites
Only download the VoltNest app from the **official App Store** (iOS) 
or **Google Play Store** (Android). Third-party APKs may contain 
malware and are not supported.

### ❌ Don't post your password or order IDs in public forums
If you're asking for help on social media, share only your device 
model and OS version. Send sensitive details only to 
support@voltnest.com.

## For Support Agents

Internal notes for Tier 1 and Tier 2 agents handling app-launch issues.

### Triage Questions
Ask the customer:
- What device and OS version?
- What app version?
- Does the app crash, freeze, or show an error?
- Has it ever worked?
- What have you already tried?

### Tier 1 Scope
Tier 1 can resolve:
- OS below minimum → advise update or web app
- App outdated → advise update
- Temporary glitch → Step 2 (force close)
- Android cache corruption → Step 3 (clear cache)
- iOS 17.2 crash → confirm known issue, provide workaround

### Tier 2 Escalation Criteria
Escalate to Tier 2 when:
- Customer completed Steps 1–6 and app still fails
- Customer provides device model + OS + app version
- A crash log or screen recording is available
- Issue affects a specific device/OS combo not yet in Known Issues

### Do NOT Tell the Customer
- Do not promise a fix date unless the issue is in Known Issues with 
  a stated date
- Do not ask them to "clear data"
- Do not suggest third-party cache cleaners or VPNs
- Do not ask them to factory reset their device

### Known Issue Verification
Before escalating, verify the customer's issue isn't already listed 
in Step 6. If it is, share the workaround and close the ticket.

## Related
- [Login Issues](./login_issues.md)
- [Payment Failures](./payment_failures.md)
- [Account FAQ](../faqs/account_faq.md)
- [Support Hours](../company/support_hours.md)
- [Contact VoltNest](../company/contact.md)