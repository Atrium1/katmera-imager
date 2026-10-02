# Release notes

## Versioning

Product version is independent of upstream. Foundation / internal builds use
git describe (e.g. `0.1.0-dev`). First public MVP target: **1.0.0**.

Always note: “Based on Raspberry Pi Imager v2.0.11.1 (Apache-2.0).”

## Unsigned test builds (now)

Ship internal artifacts without Authenticode / notarization. Label clearly as
**unsigned test builds**. Suitable for lab SD flashing with **Use custom**.

## Signed releases (M6)

| Platform | Artifact | Signing |
|----------|----------|---------|
| Windows | `Katmera-Imager-Setup-{version}.exe` | Authenticode when cert available |
| macOS | `Katmera-Imager-{version}.dmg` | Developer ID + notarization |
| Linux | `katmera-imager_{version}_amd64.deb` | Optional package signing |

Publish SHA256 checksums on GitHub Releases.
