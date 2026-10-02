# Catalog publish checklist (Priority 1)

Publish the Phase 1 **stub** catalog so the default app URL works without `--repo`.

## Target

| Item | Value |
|------|--------|
| Source of truth | [`katmera/catalog/os_list_v4.json`](../catalog/os_list_v4.json) |
| Public URL | `https://downloads.katmera.com/imager/os_list_v4.json` |
| App constant | `OSLIST_URL` in [`src/config.h`](../../src/config.h) |

Stub entries intentionally omit `url` / sha256 fields. Device/OS icons use
bundled `icons/katmera-mark.png` (resolved inside the app), so the CDN only
needs the JSON for this milestone.

Optional later: mirror icons under `https://downloads.katmera.com/imager/icons/`
and switch catalog `icon` fields to absolute HTTPS URLs.

## Publish steps

1. **Validate**

   ```bash
   python3 katmera/scripts/validate-catalog.py
   ```

2. **Upload** `katmera/catalog/os_list_v4.json` to the object/CDN key:

   `imager/os_list_v4.json` on host `downloads.katmera.com`

   Ensure:

   - HTTPS serves the file (HTTP redirect to HTTPS is fine)
   - `Content-Type: application/json` (or `application/octet-stream` acceptable)
   - Cache: short TTL or purge on each publish (stubs will be replaced by real URLs later)
   - CORS is not required for the desktop Imager (curl/Qt), only for any future web consumers

3. **Smoke test**

   ```bash
   curl -sfI "https://downloads.katmera.com/imager/os_list_v4.json"
   curl -sf "https://downloads.katmera.com/imager/os_list_v4.json" | python3 -m json.tool | head
   ```

   Expect HTTP 200 and JSON with all Phase 1 device tags:
   `nexus-hub-octapower-3566-ai`, `nexus-hub-omnicore-1126b`,
   `nexus-base-octapower-3566-ai`, `nexus-base-omnicore-1126b`.

4. **App check**

   Launch Katmera Imager **without** `--repo`. Device list must show both Hub
   and Base combinations (four devices). Stub OS rows remain “image not published”; use **Use custom**
   for microSD write tests.

5. **Docs**

   After the URL is live, update [`BUILD.md`](BUILD.md) / [`PHASE1.md`](PHASE1.md)
   to note that the default catalog URL works (keep `--repo` as a lab override).

## Ops ownership

CDN/DNS write access for `downloads.katmera.com` is outside this repository.
This checklist is the contract between the Imager repo and whoever operates the
downloads host.

## Status

- [x] Stub JSON ready in-repo (bundled icons)
- [x] Publish checklist documented
- [ ] Ops: file live at `OSLIST_URL` (pending CDN credentials)
