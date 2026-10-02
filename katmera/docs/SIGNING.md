# Code signing & installers (M6 / Priority 5)

Foundation path: unsigned internals ([`BUILD.md`](BUILD.md), [`RELEASE.md`](RELEASE.md)).
This document is the signed-release runbook once certificates exist.

## Windows

```bat
cmake -S src -B build ^
  -DCMAKE_BUILD_TYPE=MinSizeRel ^
  -DENABLE_TELEMETRY=OFF ^
  -DENABLE_INNO_INSTALLER=ON ^
  -DIMAGER_SIGNED_APP=ON ^
  -DQt6_ROOT=C:\Qt\6.9.x\msvc2022_64
cmake --build build -j
```

- Output: `Katmera-Imager-Setup-{version}.exe`
- Signing: `signtool` via packaging CMake when `IMAGER_SIGNED_APP=ON`
- CI secrets: `WINDOWS_CERT_PFX`, `WINDOWS_CERT_PASSWORD`

## macOS

```bash
cmake -S src -B build \
  -DCMAKE_BUILD_TYPE=MinSizeRel \
  -DENABLE_TELEMETRY=OFF \
  -DIMAGER_SIGNED_APP=ON \
  -DIMAGER_SIGNING_IDENTITY="Developer ID Application: …" \
  -DIMAGER_NOTARIZE_APP=ON \
  -DIMAGER_NOTARIZE_KEYCHAIN_PROFILE="notary-profile"
cmake --build build -j
cmake --build build --target dmg
```

- Output: `Katmera-Imager-{version}.dmg`
- See `src/mac/PlatformPackaging.cmake`
- CI secrets: Developer ID identity material + notary keychain profile / API key

## Linux

```bash
# Produce amd64 .deb via debian/ pipeline (see debian/build-binary-chroot.sh)
# Optional: debsign with team packaging key
```

- Output: `katmera-imager_{version}_amd64.deb`

## GitHub Release

1. Tag `v*` → draft release workflow creates notes ([`.github/workflows/draft-release.yml`](../../.github/workflows/draft-release.yml)).
2. Attach signed artifacts from secure builders.
3. Attach `SHA256SUMS`:

   ```bash
   shasum -a 256 Katmera-Imager-Setup-*.exe Katmera-Imager-*.dmg katmera-imager_*.deb > SHA256SUMS
   ```

## Status

- [x] Docs + CI packaging contract (unsigned + signed flags)
- [ ] Windows Authenticode cert provisioned
- [ ] Apple Developer ID + notarization profile provisioned
- [ ] First tagged release with signed artifacts + SHA256SUMS
