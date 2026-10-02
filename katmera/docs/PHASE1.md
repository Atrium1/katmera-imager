# Phase 1 — foundation (M0–M2 stubs)

## Scope (this milestone)

- Fork rpi-imager **v2.0.11.1**, Katmera branding, EN UI
- microSD only; Nexus Hub + 3566 AI / 1126B device tags
- Catalog **stubs** (“image not published yet”)
- Test write path via **Use custom**
- Unsigned builds only

## Explicitly deferred

- M3: download token + signed CDN URLs
- M6: signed/notarized installers
- Phase 2: eMMC / rkdeveloptool
- Website / wiki (`web_katmera`)

## Device tags

- `nexus-hub-octapower-3566-ai`
- `nexus-hub-omnicore-1126b`

## Definition of Done (foundation)

- [x] Upstream import + NOTICE
- [x] Katmera naming / telemetry off
- [x] Stub V4 catalog for both Hub combos
- [x] Docs for build + Use custom testing
- [ ] First unsigned binary built on a Qt 6.9 machine
- [ ] Hardware QA when real images exist
