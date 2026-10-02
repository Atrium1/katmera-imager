# Release notes (Katmera Imager)

## Versioning

Product version is independent of upstream. First public MVP: **1.0.0**.
Release notes must state: “Based on Raspberry Pi Imager v2.0.11.1 (Apache-2.0).”

## Artifacts

| Platform | Filename pattern |
|----------|------------------|
| Windows | `Katmera-Imager-Setup-{version}.exe` |
| macOS | `Katmera-Imager-{version}.dmg` |
| Linux | `katmera-imager_{version}_amd64.deb` |

Publish checksums (SHA256) beside each artifact on GitHub Releases.

## Signing

- macOS: Developer ID + notarization when certs available
- Windows: Authenticode when cert available
- Unsigned builds are OK for internal beta; document clearly

## Website / wiki (later)

- katmera.com Quick Start: prefer Katmera Imager; keep balenaEtcher as fallback
- Keep RKDevelopTool for eMMC until Phase 2
- wiki.katmera.com Hub QS: add Imager steps + token help
- Post-purchase portal: issue download tokens
