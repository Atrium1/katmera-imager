# Follow-ups when real images + downloads host arrive

1. **BSP artifacts** — raw `.img.xz` for:
   - Nexus Hub + OctaPower 3566 AI
   - Nexus Hub + Omnicore 1126B
   - Nexus Base + OctaPower 3566 AI
   - Nexus Base + Omnicore 1126B
   Confirm **not** Rockchip `update.img`.

2. **Catalog fields** — replace stubs with real:
   - `url`, `extract_size`, `extract_sha256`
   - `image_download_size`, `image_download_sha256`

3. **Hosting** — publish `os_list_v4.json` (+ optional icons) at
   `https://downloads.katmera.com/imager/…`.  
   Checklist ready: [`CATALOG_PUBLISH.md`](CATALOG_PUBLISH.md). Ops upload still
   required until `OSLIST_URL` returns 200.

4. **M3 unlock** — App Options token + `osListUrl()` `?token=` (see
   [`DOWNLOAD_API.md`](DOWNLOAD_API.md)). Backend unlock service is external.

5. **Icons** — optionally host device/OS icons on CDN (app currently ships
   bundled `icons/katmera-mark.png`).

6. **Hardware QA** — complete `QA_MATRIX.md` (Hub boots both SoMs).

7. **M6 signing** — Authenticode + Apple notarization; publish installers
   ([`RELEASE.md`](RELEASE.md)).

8. **Site/wiki** — Quick Start links (separate `web_katmera` change, later).
