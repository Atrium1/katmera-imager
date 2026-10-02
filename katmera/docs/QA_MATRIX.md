# Phase 1 QA matrix

Hardware lab needs: Nexus Hub + OctaPower 3566 AI, Nexus Hub + Omnicore 1126B,
known-good microSD (≥ image size), USB SD readers, Win/macOS/Linux hosts.

| Case | Windows | macOS | Linux | Notes |
|------|---------|-------|-------|-------|
| Device list shows Hub+3566 and Hub+1126B | | | | |
| Unlock with valid token → catalog includes signed URLs | | | | |
| Invalid/expired token → clear error | | | | |
| Write + verify to USB SD reader | | | | |
| System disk hidden by default (“Exclude system drives”) | | | | |
| Write-protected card rejected | | | | |
| Undersized card rejected | | | | |
| Local custom `.img.xz` (“Use custom”) | | | | |
| Hub boots from flashed SD (3566 AI) | | | | Prefer one host OS for boot check |
| Hub boots from flashed SD (1126B) | | | | |
| Cancel mid-write recovers safely | | | | |

## Sign-off

- Engineer: _______________ Date: ________
- Hardware: _______________ Date: ________
