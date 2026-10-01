# Audio Quality Issues (Troubleshooting)

> **Category**: troubleshooting  
> **Audience**: customer, agent  
> **Last updated**: 2026-01-15

Diagnostic guide for sound quality problems with **VoltBuds Pro** 
wireless earbuds and **VoltBoom** Bluetooth speaker — muffled audio, 
distortion, static, one-sided sound, weak bass, or crackling. Follow 
the steps in order.

## Symptoms This Guide Covers

Use this guide if you're experiencing any of the following:

- Audio sounds muffled or "underwater"
- Sound is distorted or crackly at high volume
- Only one earbud or one side produces sound
- One earbud is quieter than the other
- Bass is weak or absent
- Static or hissing during playback
- Audio cuts out or stutters
- Volume is too low even at max setting
- Audio sounds fine in one app but bad in another
- Sound quality dropped suddenly after a firmware update
- Volume imbalance between left and right channels

**Is the issue pairing, not sound quality?**  
If the device connects but won't play, or won't connect at all, see 
[Bluetooth Pairing Issues](./bluetooth_pairing.md) instead.

## Before You Start

### Which product has the audio issue?

- **VoltBuds Pro** → Section A
- **VoltBoom** → Section B
- **Both products** → Section C (device/phone side issues)

### Quick checks (2 minutes)

1. **Volume** — check both the device volume AND the phone volume. On 
   iOS, in-app volume is separate from system volume.
2. **Audio source** — does the issue happen in every app, or just one? 
   (Spotify vs. YouTube vs. calls)
3. **Content quality** — does it happen with all audio, or only 
   certain tracks/files?
4. **Distance** — are you within the Bluetooth range? (10m for earbuds, 
   30m for speaker)
5. **Interference** — are you near a microwave, router, or USB 3.0 
   hub? Move away and retest.

If audio is still bad after these checks, continue to the relevant 
section.

## Section A: VoltBuds Pro Audio Issues

### A1. Muffled or "underwater" sound

The most common cause is a **bad seal from the ear tips**.

**Fix:**
1. Remove both earbuds
2. Remove the ear tips (twist and pull gently)
3. Clean the ear tips with a dry cloth or replace with new ones
4. Try a **different ear tip size** — most users get the best seal 
   with M or L
5. Reinsert — twist the earbud slightly into your ear canal for a 
   proper seal

**Test:** Play music at 50% volume. If it still sounds muffled, move 
to A2.

### A2. Sound is only coming from one earbud

**Quick fix — reset the L/R pairing:**

1. Place **both** earbuds in the case
2. Close the lid for **10 seconds**
3. Open the lid — both should flash white
4. Remove both earbuds — audio should now be in both

**If that doesn't work:**
1. Return both earbuds to the case, keep lid **open**
2. Press and hold the button on the back of the case for **15 seconds**
3. Forget "VoltBuds Pro" on your phone (see 
   [Bluetooth Pairing Step 2](./bluetooth_pairing.md))
4. Re-pair from scratch

**If one earbud still doesn't work:**
- Test the non-working earbud **alone** (leave the other in the case)
- If silent alone, it's a hardware fault → contact support for warranty

### A3. One earbud is quieter than the other

Volume imbalance is usually a **fit** or **wax** issue.

**Fix:**
1. Clean the mesh grille on both earbuds — use a dry, soft-bristled 
   brush (an old toothbrush works)
2. Do NOT insert anything sharp — you can puncture the driver
3. Swap ear tip sizes — try the same size on both first, then 
   experiment
4. Check your phone's audio balance setting:
   - **iOS**: Settings → Accessibility → Audio/Visual → Balance slider
   - **Android**: Settings → Accessibility → Hearing → Audio balance
5. Reset the earbuds (A2 reset procedure)

If the imbalance persists after cleaning and settings check, the driver 
may be failing → warranty.

### A4. Distortion or crackling at high volume

**Causes:**
- **Volume clipping** — the earbuds are being driven past their 
  clean output limit
- **Bad audio source** — a low-bitrate file (e.g., a 64kbps MP3)
- **Firmware bug** — outdated firmware may over-amplify

**Fix:**
1. Lower the volume to 70–80% — most Bluetooth earbuds distort above 90%
2. Test with a different audio source (a streaming service, not a 
   low-quality file)
3. Update firmware via the VoltNest app (see 
   [Bluetooth Pairing Step 9](./bluetooth_pairing.md))
4. Try a different codec:
   - **iOS**: AAC is used automatically
   - **Android**: In Bluetooth settings, try switching between **AAC** 
     and **SBC** (tap the gear icon next to "VoltBuds Pro")

If distortion persists at moderate volume, contact support — potential 
driver fault.

### A5. Static or hissing during playback

**Static is usually a Bluetooth interference issue**, not a defect.

**Causes:**
- **Wi-Fi interference** — 2.4 GHz routers
- **USB 3.0 devices** — cables and hubs emit 2.4 GHz noise
- **Microwave ovens** — during operation
- **Dense environments** — airports, offices with many Bluetooth devices

**Fix:**
1. Move away from routers, USB hubs, and microwaves
2. Switch your Wi-Fi to the **5 GHz band** if possible
3. Update earbud firmware (see Step 9 in Bluetooth Pairing)
4. Test with a different phone — if static disappears, it's the phone's 
   Bluetooth chip, not the earbuds

If static persists in a quiet environment on multiple phones, contact 
support.

### A6. Bass is weak or missing

Weak bass is often a **seal problem**, not a driver problem.

**Fix:**
1. Ensure a proper ear seal — try larger ear tips
2. Gently twist earbuds into your ear canal when inserting
3. Test in a quiet environment (bass is perceived differently in noisy 
   places)
4. Check if any EQ is enabled:
   - **iOS**: Settings → Music → EQ → set to "Off"
   - **Android**: Spotify/YouTube Music have their own EQ settings
5. Update firmware — newer firmware has improved low-frequency 
   response

If bass is still missing with a proper seal, the driver may be 
failing → warranty.

### A7. Audio sounds fine in one app but bad in another

This is an **app-specific issue**, not a hardware problem.

**Check:**
- **App EQ settings** — Spotify, YouTube, Apple Music all have their 
  own equalizers
- **Audio enhancement features** — some apps apply Dolby, DTS, or 
  spatial audio
- **Bluetooth codec in-app** — some apps (like Tidal) let you choose 
  the codec

Set all app EQs to "flat" or "off" and retest.

### A8. Sound quality dropped after a firmware update

Rare, but happens. Options:

1. **Check for another firmware update** — sometimes a follow-up patch 
   fixes a regression
2. **Reset the earbuds** (see A2)
3. **Forget and re-pair** (see Bluetooth Pairing Step 2)
4. If quality is still worse than before the update, contact 
   support — we track firmware regressions

## Section B: VoltBoom Audio Issues

### B1. Distortion at high volume

**20W RMS output** — the VoltBoom is loud, but it has limits.

**Fix:**
1. Lower the volume — most Bluetooth speakers distort above 85%
2. Test with a different audio source
3. Update firmware (see Bluetooth Pairing Step 9)
4. Move away from walls — the passive radiators need space to work
5. If distortion persists at moderate volume, contact support

### B2. Weak bass

VoltBoom's bass comes from **dual passive radiators** on the sides. 
Obstructions weaken bass.

**Fix:**
1. Move the speaker away from walls, corners, and furniture
2. Place on a **hard surface** (table, counter) — not on carpet or bed
3. Stand it upright — side-firing radiators need clear space
4. Ensure the passive radiators aren't covered
5. Update firmware for the latest DSP tuning

If bass is still weak with proper placement, contact support.

### B3. Only one channel (left or right) plays in Stereo mode

Stereo mode uses 2 speakers.

**Fix:**
1. Verify both speakers are in **Stereo mode** (white LED on both)
2. Both speakers must be on the **same firmware version** — check in 
   the VoltNest app
3. Reset stereo pairing:
   - Power off both speakers
   - Power on both
   - Press Stereo on both within 5 seconds
4. Re-pair from your phone

If one speaker still produces no sound, it may have a driver fault → 
warranty.

### B4. Static or crackling

Same causes as earbuds:

- Wi-Fi interference
- USB 3.0 devices nearby
- Microwaves
- Distance (keep within 30m)

**Fix:**
1. Move away from interference sources
2. Forget and re-pair (Bluetooth Pairing Step 2)
3. Update firmware
4. Test with a different phone — if static disappears, phone-side issue

### B5. Sound is muffled

The VoltBoom grille can accumulate dust or debris, especially outdoors.

**Fix:**
1. Wipe the grille with a dry, soft cloth
2. For deeper cleaning, use a soft brush (an old toothbrush)
3. Do NOT use water pressure — the grille itself isn't sealed, only 
   the electronics
4. Do NOT use compressed air — it can push debris deeper

### B6. Volume is very low even at max

**Check:**
1. Both device volume AND phone volume (iOS separates them)
2. App-specific volume (some apps have their own slider)
3. Speaker firmware is up to date
4. Content quality — some tracks are quieter than others

If the VoltBoom is genuinely quieter than it used to be, it may have 
an amplifier fault → warranty.

## Section C: Cross-Device Issues (Both Products)

### C1. Audio sounds fine on one phone but bad on another

**The phone is the problem, not the VoltNest product.**

Common phone-side causes:

- **Codec mismatch** — some phones default to SBC, others to AAC or 
  aptX
- **Bluetooth version** — older phones (BT 4.0) have narrower 
  bandwidth
- **Phone's EQ/DSP settings** — many phones apply their own audio 
  processing
- **Audio source quality** — some phones resample audio poorly

**Fix:**
- On Android: **Settings → Bluetooth → [VoltBuds/VoltBoom] → gear 
  icon → try AAC or SBC**
- Disable any phone-side audio enhancements (Dolby, DTS, spatial audio)
- Update the phone's OS

### C2. Volume is different between iOS and Android

iOS and Android handle Bluetooth volume differently.

**iOS:**
- Uses absolute volume by default
- iOS may automatically lower max volume to protect hearing

**Android:**
- Uses relative volume — sometimes syncs differently
- Some Androids apply "Media volume limit" in Sound settings

**Fix:**
- **iOS**: Settings → Sounds & Haptics → check "Change with Buttons"
- **Android**: Settings → Sound → Media volume limit → turn off or 
  increase

### C3. Audio is fine for music but bad for calls

Call quality uses a **different Bluetooth profile** (HFP vs. A2DP).

**Causes:**
- **HFP bandwidth is lower** — voice calls are optimized for speech, 
  not music
- **Mic placement** — for VoltBuds Pro, the mic is on the stem; for 
  VoltBoom, on the top
- **Background noise** — ENC reduces noise but can't eliminate it

**Fix:**
- Speak closer to the mic
- Test in a quiet environment
- Ensure the mic isn't covered by your hand or clothing
- For VoltBuds Pro, try the other earbud solo (each has its own mic)

If calls are consistently poor, contact support — potential mic fault.

### C4. Audio has a delay (lip sync issue)

**Bluetooth audio has inherent latency** — usually 100–300 ms.

**Fix:**
- Use **aptX Low Latency** codec if your phone supports it (Android)
- For iOS, latency is minimized with AAC
- Some apps compensate automatically (Netflix, YouTube)
- For gaming, Bluetooth is not ideal — use wired when possible

This is a **limitation of Bluetooth**, not a product defect.

## Section D: Reset and Re-Pair (Both Products)

If audio issues persist through Sections A–C, do a full reset.

### VoltBuds Pro — Full Reset
1. Place both earbuds in the case, keep lid open
2. Press and hold the button on the back of the case for 15 seconds
3. LED flashes red, then white
4. Forget "VoltBuds Pro" on your phone
5. Re-pair from scratch (see Bluetooth Pairing Step 1)

### VoltBoom — Full Reset
1. Power on the speaker
2. Press and hold **Power + Bluetooth** together for 10 seconds
3. LED flashes red, then blue
4. Forget "VoltBoom" on your phone
5. Re-pair from scratch

After reset, retest audio quality. If still bad, continue to Section E.

## Section E: Firmware Updates

Firmware updates frequently include audio DSP improvements.

### VoltBuds Pro — current firmware: 1.4.2
- Improves multipoint switching
- Fixes occasional audio dropout on iOS 17

### VoltBoom — current firmware: 2.1.0
- Improves Stereo mode stability
- Improves bass response in outdoor mode

### How to update
1. Pair the device to your phone
2. Open the VoltNest app
3. Go to **My Devices**
4. Select the product
5. Tap **Check for Updates**
6. Keep the device within 1 meter of the phone
7. Update takes 3–5 minutes

## When to Escalate to Support

Contact support if you've completed the relevant sections and audio 
quality is still poor.

### What to Include

1. **Which product** (VoltBuds Pro or VoltBoom)
2. **Order ID** (format: `ORD-XXXXXX`)
3. **Phone model and OS**
4. **Firmware version** (find in the VoltNest app)
5. **Specific symptom** — muffled, distorted, one-sided, static, etc.
6. **When it started** — always, after update, after drop, after water
7. **Steps you've tried** (which sections)
8. **Whether it happens on other phones**

### How to Contact

- **Email**: support@voltnest.com, subject "Audio Quality Issue"
- **Live chat**: voltnest.com/chat

### Response Time

- Standard: **24 hours**
- Warranty-related: initial response in **24 hours**, resolution in 
  **5–8 business days** (see [Warranty Policy](../policies/warranty_policy.md))

## What NOT to Do

### ❌ Don't insert anything sharp into the earbud grille
You'll puncture the driver. Use only a soft brush.

### ❌ Don't use alcohol, solvents, or cleaning sprays
These damage the mesh, plastics, and driver materials.

### ❌ Don't submerge VoltBuds Pro
IPX5 is splash-resistant only. Submerging voids the warranty.

### ❌ Don't use compressed air
It can push debris deeper into the driver.

### ❌ Don't leave the earbuds at high volume
Continuous high-volume playback can damage drivers over time and 
damages your hearing.

### ❌ Don't assume it's the product — test on another phone first
Most "audio quality" complaints are phone-side codec or EQ issues.

### ❌ Don't try to open the product to "fix" it
Disassembly voids the warranty and risks damaging the drivers.

## For Support Agents

Internal notes for Tier 1 and Tier 2 agents handling audio quality 
issues.

### Triage Questions
- Which product? VoltBuds Pro or VoltBoom?
- What phone and OS version?
- What app were you using?
- Does the issue happen in every app, or just one?
- Does it happen on other devices (another phone, tablet, laptop)?
- When did it start? (Always, after update, after drop, after water?)
- Is the fit good? (For earbuds)
- What firmware version are you on?

### Tier 1 Scope
Tier 1 can resolve:
- Fit/seal guidance (A1)
- Ear tip size guidance (A1)
- Reset procedure (A2)
- Cleaning guidance (A3, B5)
- App EQ guidance (A7)
- Volume and balance settings (A3, C2)
- Firmware update guidance (E)

### Tier 2 Escalation Criteria
Escalate to Tier 2 when:
- Customer completed relevant sections and audio still poor
- Product fails on multiple devices (hardware fault likely)
- Mic issue for calls
- Suspected driver failure
- Post-firmware regression reported

### Warranty Routing
If the product is defective (verified on multiple devices, after reset 
and firmware update), route to warranty:

1. Confirm order ID and purchase date
2. Verify within 12-month warranty
3. Open warranty claim per [Warranty Policy](../policies/warranty_policy.md)

### Do NOT Tell the Customer
- Do not suggest opening the product
- Do not suggest alcohol or solvents for cleaning
- Do not tell them the earbuds pair to each other (they pair to phone)
- Do not confirm a hardware fault without multi-device testing
- Do not blame the phone unless the customer has tested on another 
  device

### Interference vs. Defect Decision Tree
Ask: "Does the audio improve when you move away from routers, USB 
hubs, and microwaves?"

- **Yes** → interference, advise environment changes
- **No** → continue diagnostics

Ask: "Does the audio sound good on a different phone?"

- **Yes** → phone-side issue, not product
- **No** → likely product fault, route to warranty

## Related
- [Bluetooth Pairing Issues](./bluetooth_pairing.md)
- [Device Not Charging](./device_not_charging.md)
- [VoltBuds Pro Product Page](../products/wireless_earbuds.md)
- [VoltBoom Product Page](../products/bluetooth_speaker.md)
- [Warranty Policy](../policies/warranty_policy.md)
- [Return & Refund Policy](../policies/return_refund_policy.md)
- [Contact VoltNest](../company/contact.md)