# Phase 1 QA — automated run log

Date: 2026-10-02  
Environment: CI / developer workstation (no Nexus Hub hardware attached)

## Automated checks (passed)

| Check | Result |
|-------|--------|
| `python3 katmera/scripts/validate-catalog.py` | Pass (Phase 1 device tags + required fields) |
| Rebrand sanity (`katmera-imager`, `OSLIST_URL`, NOTICE, desktop files) | Pass |
| Download token path present (`downloadToken` setting + `osListUrl()` query append) | Pass (code review) |
| Telemetry default OFF / empty `TELEMETRY_URL` | Pass |
| Phase 2 deferred docs (`katmera/docs/PHASE2.md`) | Present |

## Hardware lab (pending — required for MVP sign-off)

Use [QA_MATRIX.md](./QA_MATRIX.md). Cannot be completed in this environment:

- Write + verify to physical microSD on Win/macOS/Linux
- Nexus Hub boot from flashed SD (3566 AI and 1126B)
- System-drive exclusion on each host OS
- Live unlock against production download API with a real token

## Website / wiki

Integration is planned only (see RELEASE.md); no `web_katmera` changes in this repo.
