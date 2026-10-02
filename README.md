# Katmera Imager

First-party imaging utility for writing Katmera Linux BSP images to microSD cards
for [Katmera](https://katmera.com) Nexus Hub System-on-Module combinations.

**Phase 1 focus (this milestone):** Nexus Hub + OctaPower 3566 AI, and Nexus Hub +
Omnicore 1126B — **microSD only**. UI language: **English**.

Internal eMMC via `rkdeveloptool` is **Phase 2** (not started).

## Based on Raspberry Pi Imager

Katmera Imager is a fork of [Raspberry Pi Imager](https://github.com/raspberrypi/rpi-imager)
tag **v2.0.11.1**, licensed under the **Apache License 2.0**.

See [license.txt](./license.txt) and [katmera/NOTICE](./katmera/NOTICE).

Upstream remote: `https://github.com/raspberrypi/rpi-imager.git` (kept for cherry-picks).

## Current status (M0–M1 / early M2)

| Item | Status |
|------|--------|
| Upstream import v2.0.11.1 | Done |
| Katmera branding / IDs | Done |
| Telemetry disabled | Done |
| Stub catalog (two Hub combos) | Done — **images not published yet** |
| SD write path (upstream writer) | Ready — test via **Use custom** |
| Private unlock / signed CDN URLs | **Deferred to M3** (hooks only) |
| Signed / notarized installers | **Deferred to M6** (unsigned test builds only) |
| eMMC / rkdeveloptool | **Deferred to Phase 2** |

## Local build (unsigned test builds)

Requires **Qt 6.9+** and **CMake ≥ 3.22**. See also [CONTRIBUTING.md](./CONTRIBUTING.md)
and [katmera/docs/BUILD.md](./katmera/docs/BUILD.md).

```bash
git submodule update --init --recursive

# Example (adjust Qt6_ROOT for your machine)
cmake -S src -B build \
  -DCMAKE_BUILD_TYPE=MinSizeRel \
  -DENABLE_TELEMETRY=OFF \
  -DQt6_ROOT=/path/to/Qt/6.9.x/<arch>

cmake --build build -j
```

First builds are **unsigned internal test builds**. Do not distribute as production
installers until code signing / notarization (M6). Packaging outlines:

- Windows: Inno Setup (`-DENABLE_INNO_INSTALLER=ON`) → `Katmera-Imager-Setup-{ver}.exe`
- macOS: DMG via macdeployqt → `Katmera-Imager-{ver}.dmg` (notarize later)
- Linux: `katmera-imager_{ver}_amd64.deb`

## Testing without Katmera BSP images

Real Hub BSP `.img` files are **not available yet**. Catalog stubs say
“Image not published yet.”

**Test the SD write path with a local image:**

1. Build and run `katmera-imager` (or use `--repo` below).
2. Prefer loading the stub catalog from the repo:

   ```bash
   ./build/katmera-imager --repo "$(pwd)/katmera/catalog/os_list_v4.json"
   ```

3. Choose a Nexus Hub device, then choose **Use custom**.
4. Select any local `.img` / `.img.xz` / `.img.zip` large enough for your card.
5. Choose storage (keep **Exclude system drives** ON) and write.

This exercises the upstream download/write/verify path without Katmera CDN images.

## Catalog

- Stub Repository JSON V4: [katmera/catalog/os_list_v4.json](./katmera/catalog/os_list_v4.json)
- Default `OSLIST_URL` in `src/config.h` points at the future host
  `https://downloads.katmera.com/imager/os_list_v4.json` (not required until hosted).
- Device tags: `nexus-hub-octapower-3566-ai`, `nexus-hub-omnicore-1126b`
- `init_format`: `none`

Validate stubs:

```bash
python3 katmera/scripts/validate-catalog.py
```

## Telemetry

Disabled by default (`ENABLE_TELEMETRY=OFF`, empty `TELEMETRY_URL`). No phone-home
to raspberrypi.com.

## Follow-ups (when real images arrive)

1. Publish raw `.img.xz` for both Hub combos (not Rockchip `update.img`).
2. Fill real `extract_size`, `extract_sha256`, `image_download_size`, `image_download_sha256`, `url`.
3. Host catalog + images on `downloads.katmera.com` (or equivalent).
4. Implement M3 unlock API + App Options token field (see `katmera/docs/DOWNLOAD_API.md`).
5. Hardware QA: Hub boots from flashed SD (both SoMs) — `katmera/docs/QA_MATRIX.md`.
6. M6: signed Windows / notarized macOS / published Linux packages.

## Docs

- [katmera/docs/BUILD.md](./katmera/docs/BUILD.md) — build & custom-image testing
- [katmera/docs/PHASE1.md](./katmera/docs/PHASE1.md) — Phase 1 scope
- [katmera/docs/PHASE2.md](./katmera/docs/PHASE2.md) — eMMC later
- [katmera/docs/DOWNLOAD_API.md](./katmera/docs/DOWNLOAD_API.md) — M3 unlock contract (stub)
- [katmera/docs/RELEASE.md](./katmera/docs/RELEASE.md) — unsigned now, signed later
