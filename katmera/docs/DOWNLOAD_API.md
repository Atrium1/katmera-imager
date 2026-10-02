# Download API contract (M3 — not implemented yet)

Phase 1 foundation ships **catalog stubs only**. There is **no** unlock UI and
**no** signed-URL fetch in the app yet.

When real BSP images exist, implement:

```text
User enters download token (App Options)
        │
        ▼
GET {OSLIST_URL}?token={token}
        │
        ├─ 200 → Repository JSON V4 with signed image `url` fields (TTL ~4h)
        ├─ 401/403 → invalid/expired token
        └─ …
        │
        ▼
Imager downloads via plain HTTPS GET (upstream writer unchanged)
```

## Code hooks (already noted in tree)

- `ImageWriter::osListUrl()` — comment marks where to append `?token=`
- `AppOptionsDialog.qml` — comment marks where to add the token field
- Do **not** patch `DownloadThread` Authorization headers; prefer signed URLs

## Until M3

- Test SD writing with **Use custom** + local `.img` / `.img.xz`
- Keep stub catalog entries without real download URLs
