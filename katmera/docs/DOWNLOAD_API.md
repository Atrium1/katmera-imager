# Download API contract (private images)

Katmera BSP images are **not** public. Katmera Imager uses short-lived
**signed CDN URLs** embedded in a personalized Repository JSON V4 catalog.

## Recommended flow

```text
User enters download token in App Options
        │
        ▼
GET {OSLIST_URL}?token={token}
        │
        ├─ 200 → Repository JSON V4 with signed image `url` fields (TTL ~4h)
        ├─ 401/403 → invalid/expired token (Imager shows fetch error)
        └─ 404 → unknown catalog
        │
        ▼
Imager downloads image via plain HTTPS GET on signed URL
(SHA256 from JSON verifies integrity — no Authorization header needed)
```

## Endpoints

### Catalog

- **Public metadata (optional):** `GET https://downloads.katmera.com/imager/os_list_v4.json`
  May list devices/OS names; image `url`s may 403 without unlock.
- **Unlocked catalog:** `GET https://downloads.katmera.com/imager/os_list_v4.json?token=<TOKEN>`
  Returns full V4 JSON with valid signed `url`s.

### Token

- Issued post-purchase (same system as existing private BSP delivery).
- Opaque string; treat as secret; do not log in full.
- Recommended TTL for signed image URLs: **4 hours** (range 1–24h).

## Catalog requirements

Must conform to upstream `doc/json-schema/os-list-schema.json` (Repository JSON V4).

Required per installable OS entry:

- `name`, `description`, `icon`, `url`
- `extract_size`, `extract_sha256`
- `image_download_size`, `image_download_sha256` (recommended)
- `release_date`, `devices`, `init_format` (`none` for Katmera Phase 1)

Device tags (Phase 1):

- `nexus-hub-octapower-3566-ai`
- `nexus-hub-omnicore-1126b`

## Why not Bearer headers on image download?

Upstream `DownloadThread` (libcurl) does not expose Authorization headers.
Signed URLs maximize reuse and keep the writer path stock.

## Local development

```bash
katmera-imager --repo "$(pwd)/katmera/catalog/os_list_v4.json"
```

Replace placeholder sizes/hashes/URLs before production hosting.
