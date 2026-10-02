# Release notes

## Versioning

Product version is independent of upstream. Foundation / internal builds use
git describe (e.g. `0.1.0-dev`). First public MVP target: **1.0.0**.

Always note: “Based on Raspberry Pi Imager v2.0.11.1 (Apache-2.0).”

## Unsigned test builds (Priority 2)

Ship internal artifacts without Authenticode / notarization. Label clearly as
**unsigned test builds**. Suitable for lab SD flashing with **Use custom**.

| Platform | Artifact |
|----------|----------|
| Windows | `Katmera-Imager-{version}-windows-unsigned.zip` |
| macOS | `Katmera-Imager-{version}-macos-unsigned.zip` |
| Linux | `katmera-imager-{version}-linux-x86_64-unsigned.tar.gz` or unsigned `.deb` |

Build recipes: [`BUILD.md`](BUILD.md). CI documents the expected flags in
`.github/workflows/ci.yml` (packaging-stub job) until Qt runners are provisioned.

## Signed releases (M6 / Priority 5)

| Platform | Artifact | CMake / pipeline | Signing |
|----------|----------|------------------|---------|
| Windows | `Katmera-Imager-Setup-{version}.exe` | `-DENABLE_INNO_INSTALLER=ON -DIMAGER_SIGNED_APP=ON -DENABLE_TELEMETRY=OFF` | Authenticode (`signtool`, cert secrets) |
| macOS | `Katmera-Imager-{version}.dmg` | `-DIMAGER_SIGNED_APP=ON -DIMAGER_SIGNING_IDENTITY=… -DIMAGER_NOTARIZE_APP=ON` | Developer ID + notarization |
| Linux | `katmera-imager_{version}_amd64.deb` | `debian/` pipeline | Optional package signing |

### Required secrets (CI / signed builders)

| Secret | Use |
|--------|-----|
| `WINDOWS_CERT_PFX` / `WINDOWS_CERT_PASSWORD` | Authenticode |
| `APPLE_DEVELOPER_ID_CERT` / related keychain profile | macOS sign |
| `APPLE_NOTARY_PROFILE` / App Store Connect API key | Notarization |
| Optional Linux package signing key | `.deb` |

Publish **SHA256SUMS** (or per-file `.sha256`) on the GitHub Release alongside
installers. Tag-triggered draft release: `.github/workflows/draft-release.yml`.

Full signing runbook: [`SIGNING.md`](SIGNING.md).

Unsigned lab path remains documented in [`BUILD.md`](BUILD.md) after M6.
