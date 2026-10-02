# Katmera Imager

First-party imaging utility for writing Katmera Linux BSP images to microSD cards
for [Katmera](https://katmera.com) Nexus Hub System-on-Module combinations.

**Phase 1 focus:** Nexus Hub + OctaPower 3566 AI, and Nexus Hub + Omnicore 1126B
(microSD only). Internal eMMC via `rkdeveloptool` is planned for Phase 2.

## Based on Raspberry Pi Imager

Katmera Imager is a fork of [Raspberry Pi Imager](https://github.com/raspberrypi/rpi-imager)
tag **v2.0.11.1**, licensed under the **Apache License 2.0**.

See [license.txt](./license.txt) and [katmera/NOTICE](./katmera/NOTICE) for
attribution and third-party notices.

Upstream remote: `https://github.com/raspberrypi/rpi-imager.git`

## Downloads

Release installers (Windows / macOS / Linux) will be published on the
[GitHub Releases](https://github.com/Atrium1/katmera-imager/releases) page and
linked from katmera.com Quick Start docs.

Private BSP images require a post-purchase **download token**. Enter it under
App Options → Download token, or append `?token=…` to the catalog URL.

## Development

Build instructions follow upstream: see [CONTRIBUTING.md](./CONTRIBUTING.md)
(Qt 6.9+, CMake). Product-specific notes:

- Catalog (Repository JSON V4): [katmera/catalog/os_list_v4.json](./katmera/catalog/os_list_v4.json)
- Phase 1 / Phase 2 docs: [katmera/docs/](./katmera/docs/)
- Default catalog URL is set in `src/config.h` (`OSLIST_URL`)
- Override at runtime: `katmera-imager --repo /path/to/os_list_v4.json`

```bash
# Linux example
cmake -S src -B build -DCMAKE_BUILD_TYPE=MinSizeRel -DENABLE_TELEMETRY=OFF
cmake --build build -j
```

## Custom repository

`--repo [URL-or-file]` selects a custom Repository JSON V4 manifest (same as upstream).

## Telemetry

Anonymous telemetry is **disabled by default** in Katmera builds
(`ENABLE_TELEMETRY=OFF`, empty `TELEMETRY_URL`).
