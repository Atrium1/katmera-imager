# Phase 2 — Internal eMMC (deferred)

## Goal

Add a Gemstone-style storage option **“Internal eMMC via Rockchip USB
(Maskrom)”** that invokes **rkdeveloptool** (open-source Rockchip CLI).
Do not invent the USB protocol.

## UX sketch

1. Choose OS (same catalog / signed URLs as Phase 1).
2. Choose Storage → synthetic destination (not a block device):
   `Internal eMMC via Rockchip USB (Maskrom)`.
3. App detects Maskrom/Rockusb device; Write enabled when present.
4. Write path:
   - `rkdeveloptool db <board_loader.bin>`
   - `rkdeveloptool wl 0 <raw.img>`
   - `rkdeveloptool rd`

Reference: T3 Gemstone `gem-imager` UniFlash destination pattern
(`setDst("uniflash", …)` + external tool thread).

## Hardware / docs needed from Katmera

- Nexus Hub Maskrom entry per SoM (buttons/jumpers, OTG vs host ports)
- Windows USB driver / Zadig notes if required
- Loader binaries for OctaPower 3566 AI and Omnicore 1126B (board-specific)
- Confirm eMMC artifact equals SD **raw `.img`**

## Format risk (critical)

| Format | SD (Imager) | rkdeveloptool eMMC | upgrade_tool |
|--------|-------------|--------------------|--------------|
| Raw GPT `.img` | Yes | Yes (`wl 0`) | Possible |
| Rockchip `update.img` | No | **No** | Yes (`uf`) |

**Policy:** standardize on raw disk images for SD and eMMC. If BSP only
ships `update.img`, either publish raw images or accept bundling closed
`upgrade_tool` (worse license/support).

## Do not start Phase 2 coding until

1. Maskrom procedure documented for Hub + both Phase 1 SoMs
2. Loader binaries available under a redistributable license
3. BSP confirms raw `.img` for eMMC
