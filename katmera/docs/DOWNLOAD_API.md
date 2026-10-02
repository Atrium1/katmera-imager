# Download API contract (M3)

## Client behaviour (implemented)

```text
User enters download token (App Options → Download token)
        │
        ▼
Persist settings key "download_token"
        │
        ▼
GET {OSLIST_URL}?token={token}     ← ImageWriter::osListUrl()
        │
        ├─ 200 → Repository JSON V4 with signed image `url` fields (TTL ~4h)
        ├─ 401/403 → osListError: invalid/expired token (shown in App Options + device list)
        └─ …
        │
        ▼
Imager downloads images via plain HTTPS GET to signed URLs
(DownloadThread unchanged — no Authorization headers)
```

### Code

| Piece | Location |
|-------|----------|
| Append `?token=` | `ImageWriter::osListUrl()` in `src/imagewriter.cpp` |
| Persist token | QSettings key `download_token` via App Options Save |
| UI field | `AppOptionsDialog.qml` (password field) |
| Auth errors | `onOsListFetchError` when message contains `HTTP 401` / `HTTP 403` |

Display URL (`osListUrlForDisplay`) never includes the token.

## Request

```http
GET /imager/os_list_v4.json?token=<opaque> HTTP/1.1
Host: downloads.katmera.com
Accept: application/json
```

Omit `token` (or empty) → public stub catalog (no image `url` fields).

## Success response (200)

Same V4 shape as the public catalog, but OS entries include signed download fields:

```json
{
  "imager": {
    "latest_version": "0.1.0-dev",
    "url": "https://github.com/Atrium1/katmera-imager",
    "devices": [ /* same Hub devices as public stub */ ]
  },
  "os_list": [
    {
      "name": "Katmera Linux (Hub + OctaPower 3566 AI)",
      "description": "Unlocked catalog entry (example).",
      "icon": "icons/katmera-mark.png",
      "website": "https://wiki.katmera.com/",
      "release_date": "2026-10-01",
      "init_format": "none",
      "devices": ["nexus-hub-octapower-3566-ai"],
      "url": "https://downloads.katmera.com/imager/images/hub-3566.ai.img.xz?X-Amz-Signature=EXAMPLE",
      "extract_size": 4294967296,
      "extract_sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
      "image_download_size": 1200000000,
      "image_download_sha256": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
    }
  ]
}
```

Signed URL TTL ~4h (server-defined). Placeholders OK until real BSP artifacts exist.
See [`os_list_v4_unlocked.example.json`](../catalog/os_list_v4_unlocked.example.json) for a local mock.

## Error responses

| Status | Client UX |
|--------|-----------|
| 401 / 403 | “Download token is invalid or expired…” |
| Other / network | Generic offline / retry on device list |

## Backend (external)

Unlock service issues personalized V4 JSON. Out of scope for this repo’s BSP
production. Mock locally:

```bash
./build/katmera-imager --repo "$(pwd)/katmera/catalog/os_list_v4_unlocked.example.json"
```

Token UI still refreshes the default HTTPS catalog; use `--repo` only to
exercise download URLs without the unlock API.

## Until real images

- Public stub remains the default catalog (no `url` fields)
- Test SD writing with **Use custom** + local `.img` / `.img.xz`
