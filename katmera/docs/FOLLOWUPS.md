# Follow-ups when real images + downloads host arrive

1. **BSP artifacts** — raw `.img.xz` for:
   - Nexus Hub + OctaPower 3566 AI
   - Nexus Hub + Omnicore 1126B  
   Confirm **not** Rockchip `update.img`.

2. **Catalog fields** — replace stubs with real:
   - `url`, `extract_size`, `extract_sha256`
   - `image_download_size`, `image_download_sha256`

3. **Hosting** — publish `os_list_v4.json` + images at
   `https://downloads.katmera.com/imager/…` (or equivalent).

4. **M3 unlock** — implement token App Options UI + `osListUrl()` `?token=`
   append per `DOWNLOAD_API.md`.

5. **Icons** — host device/OS icons referenced by the catalog (or ship local).

6. **Hardware QA** — complete `QA_MATRIX.md` (Hub boots both SoMs).

7. **M6 signing** — Authenticode + Apple notarization; publish installers.

8. **Site/wiki** — Quick Start links (separate `web_katmera` change, later).
