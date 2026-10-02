# Phase 1 — Katmera Imager MVP

## Scope

- Host OS: Windows, macOS, Linux
- Storage: microSD / USB mass-storage only
- Hardware: Nexus Hub only
- Combos:
  - `nexus-hub` + `octapower-3566-ai` → device tag `nexus-hub-octapower-3566-ai`
  - `nexus-hub` + `omnicore-1126b` → device tag `nexus-hub-omnicore-1126b`

## Out of scope

- Internal eMMC / Maskrom / rkdeveloptool (see PHASE2.md)
- Nexus Base, Vision Kit, other SoMs
- Building BSP images

## Private downloads

See [DOWNLOAD_API.md](./DOWNLOAD_API.md). Users enter a post-purchase
download token in App Options. The app requests the catalog with
`?token=…`; the server returns Repository JSON V4 with short-lived signed
image URLs.

## QA matrix

See [QA_MATRIX.md](./QA_MATRIX.md).

## Definition of Done

- [x] Fork of rpi-imager v2.0.11.1 with Apache-2.0 attribution
- [x] Branded Katmera Imager naming / IDs
- [x] Catalog for Hub+3566 and Hub+1126B
- [x] Token → signed-URL unlock path in app + API contract
- [ ] Installers published for Win/macOS/Linux
- [ ] Hardware lab verifies Hub boots both SoMs from flashed SD
- [x] eMMC deferred to Phase 2
