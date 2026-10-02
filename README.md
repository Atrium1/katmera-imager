# Katmera Imager

First-party imaging utility for writing Katmera Linux BSP images to microSD cards
for [Katmera](https://katmera.com) Nexus Hub and Nexus Base System-on-Module combinations.

**Phase 1 focus:** Nexus **Hub** and Nexus **Base**, each with OctaPower 3566 AI or
Omnicore 1126B — **microSD only**. UI language: **English**.

Internal eMMC via `rkdeveloptool` is **Phase 2** (not started).

## Based on Raspberry Pi Imager

Katmera Imager is a fork of [Raspberry Pi Imager](https://github.com/raspberrypi/rpi-imager)
tag **v2.0.11.1**, licensed under the **Apache License 2.0**.

See [license.txt](./license.txt) and [katmera/NOTICE](./katmera/NOTICE).

Upstream remote: `https://github.com/raspberrypi/rpi-imager.git` (kept for cherry-picks).

## Foundation status

| Item | Status |
|------|--------|
| Upstream import v2.0.11.1 | Done |
| Katmera branding, logos, colors (`#F86000` / `#202830`) | Done |
| Telemetry disabled | Done |
| Stub catalog (Hub + Base × two SoMs, bundled mark icons) | Done — **BSP images not published yet** |
| SD write path | Ready — test via **Use custom** |
| RPi-only App Options (Connect for Organisations) | Hidden; Secure Boot capability-gated |
| Catalog publish checklist | Done — ops upload still pending |
| Win / Linux / macOS **unsigned** build recipes | Documented ([BUILD](./katmera/docs/BUILD.md) / [RELEASE](./katmera/docs/RELEASE.md)) |
| M3 download-token UI + `?token=` client | Done in app — unlock **API** is external |
| Signed / notarized installers (M6) | Docs + CI contract — **certs pending** |
| eMMC / rkdeveloptool | **Deferred to Phase 2** |

## Local build (unsigned test builds)

Requires **Qt 6.9+** and **CMake ≥ 3.22**. Platform recipes:
[katmera/docs/BUILD.md](./katmera/docs/BUILD.md).

```bash
git submodule update --init --recursive

cmake -S src -B build \
  -DCMAKE_BUILD_TYPE=MinSizeRel \
  -DENABLE_TELEMETRY=OFF \
  -DQt6_ROOT=/path/to/Qt/6.9.x/<arch>

cmake --build build -j
```

Internal unsigned artifact names (see [RELEASE.md](./katmera/docs/RELEASE.md)):

- Windows: `Katmera-Imager-{ver}-windows-unsigned.zip`
- macOS: `Katmera-Imager-{ver}-macos-unsigned.zip`
- Linux: `katmera-imager-{ver}-linux-x86_64-unsigned.tar.gz` (or unsigned `.deb`)

Do not distribute as production installers until M6 signing ([SIGNING.md](./katmera/docs/SIGNING.md)).

## Testing without Katmera BSP images

Catalog stubs say “Image not published yet.”

1. Build and run `katmera-imager`.
2. Until CDN is live, load the stub catalog:

   ```bash
   ./build/katmera-imager --repo "$(pwd)/katmera/catalog/os_list_v4.json"
   ```

3. Choose a Nexus Hub or Nexus Base device → **Use custom** → local `.img` / `.img.xz` / `.img.zip`.
4. Keep **Exclude system drives** ON, write and verify.

## Catalog & CDN

| Resource | Path / URL |
|----------|------------|
| Stub V4 (source of truth) | [katmera/catalog/os_list_v4.json](./katmera/catalog/os_list_v4.json) |
| Publish checklist | [katmera/docs/CATALOG_PUBLISH.md](./katmera/docs/CATALOG_PUBLISH.md) |
| Default `OSLIST_URL` | `https://downloads.katmera.com/imager/os_list_v4.json` |
| Device tags | `nexus-hub-octapower-3566-ai`, `nexus-hub-omnicore-1126b`, `nexus-base-octapower-3566-ai`, `nexus-base-omnicore-1126b` |
| Stub `init_format` | `none` |
| M3 mock (signed URL placeholders) | [katmera/catalog/os_list_v4_unlocked.example.json](./katmera/catalog/os_list_v4_unlocked.example.json) |

```bash
python3 katmera/scripts/validate-catalog.py
```

## Download token (M3)

App Options → **Download token** persists `download_token` and refreshes the
default catalog as `OSLIST_URL?token=…`. Invalid/expired tokens (HTTP 401/403)
show a clear error. Image downloads use plain HTTPS GET to signed URLs (no
Authorization headers on `DownloadThread`).

Contract: [katmera/docs/DOWNLOAD_API.md](./katmera/docs/DOWNLOAD_API.md).

## Telemetry

Disabled by default (`ENABLE_TELEMETRY=OFF`, empty `TELEMETRY_URL`). No phone-home
to raspberrypi.com.

## Ops still needed (outside this repo)

1. Upload stub `os_list_v4.json` to `downloads.katmera.com` ([CATALOG_PUBLISH.md](./katmera/docs/CATALOG_PUBLISH.md)).
2. Deploy unlock API that returns personalized V4 JSON for valid tokens.
3. Produce/host real Hub BSP `.img.xz` (not Rockchip `update.img`).
4. Provision Authenticode + Apple Developer ID / notarization for M6.
5. Hardware QA: Hub boots from flashed SD — [QA_MATRIX.md](./katmera/docs/QA_MATRIX.md).

## Docs

| Doc | Topic |
|-----|--------|
| [katmera/docs/BUILD.md](./katmera/docs/BUILD.md) | macOS / Windows / Linux unsigned builds |
| [katmera/docs/CATALOG_PUBLISH.md](./katmera/docs/CATALOG_PUBLISH.md) | CDN publish checklist |
| [katmera/docs/DOWNLOAD_API.md](./katmera/docs/DOWNLOAD_API.md) | M3 token unlock contract |
| [katmera/docs/RELEASE.md](./katmera/docs/RELEASE.md) | Artifact names (unsigned + signed) |
| [katmera/docs/SIGNING.md](./katmera/docs/SIGNING.md) | M6 signing runbook |
| [katmera/docs/PHASE1.md](./katmera/docs/PHASE1.md) | Phase 1 scope |
| [katmera/docs/PHASE2.md](./katmera/docs/PHASE2.md) | eMMC later |
| [katmera/docs/FOLLOWUPS.md](./katmera/docs/FOLLOWUPS.md) | When real images arrive |
| [katmera/branding/colors.md](./katmera/branding/colors.md) | Brand tokens & logo assets |
