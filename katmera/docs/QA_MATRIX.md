# Phase 1 QA matrix

Hardware lab needs: Nexus Hub and Nexus Base, each with OctaPower 3566 AI /
Omnicore 1126B, known-good microSD (≥ image size), USB SD readers, Win/macOS/Linux hosts.

| Case | Windows | macOS | Linux | Notes |
|------|---------|-------|-------|-------|
| Device list shows Hub+3566, Hub+1126B, Base+3566, Base+1126B | | | | |
| Unlock with valid token → catalog includes signed URLs | | | | |
| Invalid/expired token → clear error | | | | |
| Write + verify to USB SD reader | | | | |
| System disk hidden by default (“Exclude system drives”) | | | | |
| Write-protected card rejected | | | | |
| Undersized card rejected | | | | |
| Local custom `.img.xz` (“Use custom”) | | | | |
| Hub boots from flashed SD (3566 AI) | | | | Prefer one host OS for boot check |
| Hub boots from flashed SD (1126B) | | | | |
| Base boots from flashed SD (3566 AI) | | | | |
| Base boots from flashed SD (1126B) | | | | |
| Cancel mid-write recovers safely | | | | |
| App Options: no Pi Connect for Organisations (Katmera) | | | | Priority 3 |
| Stub OS: no Secure Boot / Connect customization steps | | | | Priority 3 |

### M3 token harness (no real BSP required)

- Mock unlocked catalog: `katmera/catalog/os_list_v4_unlocked.example.json` via `--repo`
- Token UI: App Options → Download token → Save (refreshes default HTTPS catalog)
- Force 401/403 against unlock API when available; confirm `osListError` text

## Sign-off

- Engineer: _______________ Date: ________
- Hardware: _______________ Date: ________
