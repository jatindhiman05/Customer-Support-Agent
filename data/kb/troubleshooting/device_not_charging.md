# Device Not Charging (Troubleshooting)

> **Category**: troubleshooting  
> **Audience**: customer, agent  
> **Last updated**: 2026-01-15

Diagnostic guide for charging problems with any VoltNest product — 
VoltBuds Pro, VoltBoom, VoltCharge 65W, or VoltBank 20K. Covers "won't 
charge at all," "charges slowly," "charges for a moment then stops," 
and overheating during charge.

## Symptoms This Guide Covers

Use this guide if you're experiencing any of the following:

- Product won't charge at all (no LED, no response)
- Product charges but very slowly
- Product charges for a few seconds then stops
- VoltCharge 65W won't charge a laptop, phone, or tablet
- VoltBank 20K won't charge a device from its USB-C port
- VoltBank 20K won't recharge from a wall charger
- VoltBuds Pro earbud doesn't charge in the case
- VoltBoom LED doesn't indicate charging when plugged in
- Device gets unusually hot during charge
- Intermittent charging (stops and starts repeatedly)

If your issue is **pairing or audio**, see 
[Bluetooth Pairing Issues](./bluetooth_pairing.md) or 
[Audio Quality Issues](./audio_quality_issues.md) instead.

## Before You Start

### Which product is having the charging issue?

| Product | What it charges | What it recharges from |
|---|---|---|
| **VoltBuds Pro** | Nothing (charges itself in case) | USB-C cable → case |
| **VoltBoom** | Nothing (charges itself) | USB-C cable → speaker |
| **VoltCharge 65W** | Other devices (phone, laptop) | Wall outlet (AC) |
| **VoltBank 20K** | Other devices (via USB-C/USB-A) | USB-C charger |

Identify which product is failing — the fix differs.

### Quick checks (2 minutes)

Before continuing:

1. **Is the wall outlet working?** Test with another device
2. **Is the cable intact?** Look for kinks, exposed wire, or bent connectors
3. **Is the cable plugged in fully?** USB-C requires a firm push
4. **Is the product's charging port clean?** Dust and lint block connections
5. **Has this exact setup ever worked before?**

If yes to all, continue to the correct section.

## Section A: VoltBuds Pro Won't Charge

The earbuds charge inside the case; the case charges from USB-C.

### A1. Earbuds don't charge in the case

**Check the case battery first.**
- Open the case — check the LED on the front
- **No LED** = case has no charge. Plug the case into USB-C and check 
  again after 15 minutes.
- **Amber/red LED** = case is low. Charge the case fully (about 
  2 hours).
- **White/green LED** = case is charged. If earbuds still don't charge, 
  continue.

**Check earbud seating.**
- Remove both earbuds and inspect the charging contacts (small gold 
  dots on earbud stem and inside case)
- Wipe both with a dry cotton swab
- Re-seat both earbuds — they should click magnetically into place
- Close the case for 10 seconds, then reopen

**Check earbud battery individually.**
- Place only the left earbud in the case — does the LED respond?
- Repeat with the right earbud
- If one charges but the other doesn't → the non-charging earbud may 
  be faulty → continue to warranty

### A2. Case doesn't charge from USB-C

- Try a **different USB-C cable** (data + power cable, not charge-only)
- Try a **different wall charger** (at least 5W; any USB-A or USB-C 
  brick works)
- Try a **different wall outlet**
- Clean the case's USB-C port with a dry cotton swab

If the case still doesn't charge, it may be faulty → contact support 
for warranty.

### A3. Case LED flashing repeatedly

A rapidly flashing LED indicates a fault. Try:

1. Reset the earbuds (see [Bluetooth Pairing Step 3](./bluetooth_pairing.md))
2. If flashing persists after reset and charge, contact support

### A4. Charging time expectations

- **Earbuds from 0–100%**: ~90 minutes
- **Case from 0–100%**: ~2 hours
- **Total (both from empty)**: ~3 hours

If charging takes longer than **3 hours**, see Section E (slow 
charging).

## Section B: VoltBoom Won't Charge

### B1. Speaker doesn't respond when plugged in

1. **Use a different cable** — USB-C to USB-C or USB-C to USB-A both work
2. **Use a different wall charger** — 5W minimum; 10W+ is faster
3. **Check the LED** — should show amber (charging) or white (full)
4. **Try a different outlet**

### B2. Charging LED flashes but doesn't charge

- **Low-voltage source** — Some USB ports on laptops output less 
  power than the speaker needs. Try a wall charger instead.
- **Faulty cable** — Swap to a new cable
- **Damaged USB-C port** — Inspect the port for bent pins or debris

### B3. Speaker turns on but won't charge

- Turn the speaker **off** while charging for the fastest charge
- Using the speaker while charging slows the charge but doesn't stop it
- If it truly won't charge while on, try turning off first

### B4. Charging time expectations

- **Full charge (0–100%)**: ~2.5 hours
- **Quick charge (10 min)**: ~1 hour of playback

If charging takes longer than **4 hours**, see Section E.

## Section C: VoltCharge 65W Won't Charge a Device

The charger plugs into a wall outlet and outputs power to devices via 
USB-C or USB-A.

### C1. Nothing charges from any port

1. **Check the wall outlet** — plug a lamp or other device into the 
   same outlet
2. **Check the charger's LED** — VoltCharge has no LED; skip this
3. **Try a different cable** — the cable is the most common failure
4. **Try a different device** — does the charger work with anything?

If the charger works with a phone but not a laptop, that's normal — 
see C4.

### C2. Phone charges but very slowly

- **Use a USB-C to USB-C cable** — USB-A to USB-C is limited to 18W
- **Check the phone's charging indicator** — "Fast charging" should 
  appear
- **Use a 100W-rated cable** for full 65W (60W cables cap at 60W)
- **Try the other USB-C port** — both ports support 65W independently

### C3. Laptop doesn't charge

Common cause: the laptop requires more than 65W.

| Laptop | Wattage Needed | VoltCharge 65W Works? |
|---|---|---|
| MacBook Air (M1/M2/M3) | 30W | ✅ Yes, fast |
| MacBook Pro 13" (Intel) | 61W | ✅ Yes, full speed |
| MacBook Pro 14" | 67W | ⚠️ Charges slowly, won't keep up |
| MacBook Pro 16" | 96W+ | ❌ Won't keep up under load |
| Dell XPS 13 | 45W | ✅ Yes |
| Dell XPS 15 | 90W | ❌ Won't keep up |
| HP Spectre x360 | 65W | ✅ Yes |
| Lenovo ThinkPad X1 Carbon | 65W | ✅ Yes |

**Test:** plug the laptop in and check if the charging light appears. 
If it charges but slowly, that's expected for high-wattage laptops.

### C4. Only one port works

- Try the same device in the other USB-C port
- Both USB-C ports support 65W **when used alone**
- When both are used, power splits: **45W + 20W**
- Try a USB-A device in the USB-A port to test independently

### C5. Charger gets very hot

- Normal warmth is expected during high-power charging
- **Hot to the touch** (can't hold for 5 seconds) = too hot
- Unplug immediately and let it cool
- If it happens again, contact support — potential internal fault

### C6. Charger trips a circuit breaker

- Do not use with extension cords or power strips that can't handle 
  the total wattage
- Plug directly into a wall outlet
- If a breaker trips, unplug, reset the breaker, and try again
- If it trips again, stop using and contact support

## Section D: VoltBank 20K Won't Charge Devices

### D1. Nothing charges from any port

1. **Check the power bank has charge** — press the power button; the 
   LED display shows the percentage
2. **If display shows 0%**, recharge the power bank first (Section E)
3. **Try a different cable** — the most common failure
4. **Try a different device** — confirm the bank works with anything
5. **Press the power button** on the bank to wake it from sleep mode

### D2. USB-C port won't charge a laptop

- **USB-C 1 supports 65W** — use the top USB-C port
- **USB-C 2 supports 30W** — may not charge a laptop
- **USB-A supports 18W** — for phones only
- Use a **100W-rated USB-C cable** for full power
- Check the LED display — if the bank is under 20%, it may not output 
  full 65W

### D3. Charges for a moment then stops

This is usually the **power bank going to sleep** because the device 
draws very little power (e.g., a smartwatch).

**Fix:** Press the power button to keep the bank awake, or use a 
device that draws more power.

Some very low-power devices (fitness trackers, some wireless earbuds) 
will trigger the auto-sleep. This is normal.

### D4. VoltBank shuts off after 30 minutes

Auto-shutdown is a safety feature that triggers when:

- The bank is nearly empty (under 5%)
- The bank is overheating (see D5)
- No device is drawing power

If it shuts off while charging a device, contact support.

### D5. Power bank gets hot while charging

- Warm is normal during high-power output
- **Very hot** = stop using immediately, unplug everything
- Let it cool for 30 minutes
- Try again with a lower-power device (phone instead of laptop)
- If it overheats again, contact support — lithium battery faults 
  are safety-critical

## Section E: VoltBank 20K Won't Recharge

### E1. Bank doesn't recharge from wall charger

1. **Use USB-C 1 (top port)** — this is the recharge port
2. **Use the VoltCharge 65W** for fastest charge, or any USB-C charger 
   at 30W or higher
3. **Use a 100W-rated cable** for full speed (60W cable caps at 60W)
4. **Wait 15 minutes** — the LED may not light immediately at low 
   charge
5. **Try a different wall outlet**

### E2. Bank recharges very slowly

- **Under 30W charger** → 6+ hours
- **30W charger** → ~4 hours
- **65W charger (recommended)** → ~2 hours
- **Using a USB-A charger** → will not recharge (USB-C only)

Check your charger's wattage — the bank recharges at the speed of 
the source.

### E3. Bank recharges but stops at a certain percentage

- **Stops at 80%**: Some chargers throttle power at high charge. Normal.
- **Stops at 100% but doesn't hold**: Battery cell degradation. If 
  under warranty, contact support.
- **Stops at random %**: Possibly cable or port issue. Try a new cable.

### E4. Recharge time expectations

| Charger | Time to Full |
|---|---|
| VoltCharge 65W | ~2 hours |
| 45W charger | ~2.5 hours |
| 30W charger | ~4 hours |
| Under 30W | 6+ hours |

## Section F: General Charging Issues

### F1. Charging stops and starts repeatedly

**Cause**: Usually a loose connection or a cable going bad.

**Fix:**
1. Try a different cable
2. Try a different charger (if using VoltCharge)
3. Clean both ports with a dry cotton swab
4. Ensure the connector is fully seated

### F2. Device charges in one outlet but not another

The outlet or wiring is the issue. Try:

- A different outlet in the same room
- A different room entirely
- A different home or office to rule out electrical issues

### F3. Charging is slow at night but fast during the day

Not a product issue — this is often due to:

- Other appliances drawing power (heater, AC)
- Voltage drops during peak hours on the grid
- Smart power strips limiting output

Not a Warranty claim. No fix needed.

### F4. Device gets very hot during charge

Normal warmth:
- **Cool to touch**: Normal
- **Warm to touch**: Normal
- **Hot to touch** (can't hold for 5 sec): Stop and cool
- **Burning smell or smoke**: Unplug immediately, contact support

## When to Escalate to Support

Contact support if:

- You've completed the relevant section (A–F) and the issue persists
- A product gets very hot or smells like burning
- A product won't charge with multiple cables and chargers
- A cable or charger is visibly damaged (exposed wire, bent connector)
- You suspect a warranty issue (see below)

### What to Include

1. **Which product** has the issue
2. **Order ID** (format: `ORD-XXXXXX`)
3. **Which cable and charger** you're using
4. **What you've tested** (Steps tried)
5. **Symptom specifics** — no charge, slow, intermittent, hot, etc.
6. **A photo** of the port / cable / LED if relevant

### How to Contact

- **Email**: support@voltnest.com, subject "Charging Issue"
- **Live chat**: voltnest.com/chat

### Response Time

- Standard: **24 hours**
- Warranty-related: initial response within 24 hours, resolution in 
  **5–8 business days** (see [Warranty Policy](../policies/warranty_policy.md))

## What NOT to Do

### ❌ Don't use a damaged cable
Exposed wire, bent connectors, or kinked cables can short, damage 
your product, or cause a fire. Replace damaged cables immediately.

### ❌ Don't use a charger with higher voltage than the device supports
VoltNest chargers are 100–240V compatible. Do not use chargers rated 
for other voltages.

### ❌ Don't submerge the power bank or charger
Only the VoltBoom has an IP67 rating. VoltBuds (IPX5) should not be 
submerged. VoltCharge and VoltBank are not water-resistant at all.

### ❌ Don't charge in extreme heat or cold
Below 0°C (32°F) or above 45°C (113°F) can damage batteries. Don't 
leave products in hot cars.

### ❌ Don't leave a hot device plugged in
If a product is hot to the touch, unplug it and let it cool before 
continuing.

### ❌ Don't open or disassemble a VoltNest product
Lithium batteries are dangerous if punctured. Opening the product 
voids the warranty and creates a fire hazard.

### ❌ Don't use third-party "fast charger" adapters not rated for USB-PD
Only use chargers that support USB Power Delivery (USB-PD). Cheap 
"fast chargers" without PD can damage devices.

## For Support Agents

Internal notes for Tier 1 and Tier 2 agents handling charging issues.

### Triage Questions
- Which product has the issue?
- What cable and charger are you using?
- Have you tried a different cable? Different charger? Different outlet?
- Is the device hot to the touch?
- Does the LED show charging?
- Has the setup ever worked before?

### Tier 1 Scope
Tier 1 can resolve:
- Cable swaps
- Charger swaps
- Outlet swaps
- Cleaning ports
- Sleep mode explanation (VoltBank auto-sleep)
- USB-C port selection (VoltBank USB-C 1 vs 2)
- Wattage compatibility explanation (VoltCharge + laptop)

### Tier 2 Escalation Criteria
Escalate to Tier 2 when:
- Customer completed the section and product still fails
- Product overheats (safety concern — escalate same day)
- Warranty claim likely
- Multiple cables and chargers fail

### Warranty Routing
If the product is defective (won't charge with multiple cables and 
chargers), route to warranty:

1. Confirm order ID and purchase date
2. Verify within 12-month warranty
3. Open warranty claim per [Warranty Policy](../policies/warranty_policy.md)

### Do NOT Tell the Customer
- Do not suggest opening or repairing the product
- Do not suggest third-party "fast chargers" without USB-PD
- Do not confirm a hardware fault without multi-cable testing
- Do not ask them to use a device that's hot to the touch — first 
  cool-down, then diagnose

### Overheating Safety Protocol
If a customer reports **hot to the touch** or **burning smell**:

1. Tell them to unplug immediately
2. Do not continue using the product
3. Open a **Tier 2 case within the same business day**
4. Process as a warranty replacement — even if the diagnosis is 
   unclear — for safety

## Related
- [Bluetooth Pairing Issues](./bluetooth_pairing.md)
- [Audio Quality Issues](./audio_quality_issues.md)
- [VoltBuds Pro Product Page](../products/wireless_earbuds.md)
- [VoltBoom Product Page](../products/bluetooth_speaker.md)
- [VoltCharge 65W Product Page](../products/usb_c_charger.md)
- [VoltBank 20K Product Page](../products/power_bank.md)
- [Warranty Policy](../policies/warranty_policy.md)
- [Contact VoltNest](../company/contact.md)