# Phase 1 QA — foundation run log

Date: 2026-10-02

## Automated / repo checks

| Check | Result |
|-------|--------|
| Upstream tag v2.0.11.1 imported; `upstream` remote present | Pass |
| Katmera branding / IDs / telemetry off | Pass |
| Stub catalog validates (`validate-catalog.py`) | Pass |
| Unlock UI deferred (M3 hooks only) | Pass |
| eMMC / rkdeveloptool not implemented | Pass |
| Qt 6.9 + CMake configure/build on this machine | **Blocked** — cmake/Qt not installed in agent environment |

## Manual (when Qt available)

1. Build unsigned binary per `BUILD.md`
2. `katmera-imager --repo …/katmera/catalog/os_list_v4.json`
3. Confirm both Hub devices appear
4. **Use custom** → write a local `.img.xz` to microSD with Exclude system drives ON

## Hardware (blocked on real BSP images)

Hub boot for 3566 AI / 1126B — see `QA_MATRIX.md` after images publish.
