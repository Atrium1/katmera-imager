# Phase 1 — foundation (M0–M2 stubs)

## Scope (this milestone)

- Fork rpi-imager **v2.0.11.1**, Katmera branding, EN UI
- microSD only; Nexus Hub + Nexus Base with 3566 AI / 1126B device tags
- Catalog **stubs** (“image not published yet”)
- Test write path via **Use custom**
- Unsigned builds only

## Explicitly deferred

- M3: download token + signed CDN URLs (app hooks implemented later in Priority 4)
- M6: signed/notarized installers
- Phase 2: eMMC / rkdeveloptool
- Website / wiki (`web_katmera`)

## Device tags

- `nexus-hub-octapower-3566-ai`
- `nexus-hub-omnicore-1126b`
- `nexus-base-octapower-3566-ai`
- `nexus-base-omnicore-1126b`

## RPi-only UX

With stub `init_format: none`, customization steps stay off. App Options hides
Raspberry Pi Connect for Organisations. Secure Boot UI remains capability-gated
only (debug/CLI force flags still work for upstream parity).

## Definition of Done (foundation)

- [x] Upstream import + NOTICE
- [x] Katmera naming / telemetry off
- [x] Stub V4 catalog for Hub + Base (four device combos)
- [x] Docs for build + Use custom testing
- [x] Catalog publish checklist ([`CATALOG_PUBLISH.md`](CATALOG_PUBLISH.md))
- [x] First unsigned binary built on a Qt 6.9 machine (macOS arm64)
- [ ] CDN live at `OSLIST_URL` (ops — see publish checklist)
- [ ] Hardware QA when real images exist
