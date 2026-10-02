# Building Katmera Imager (unsigned test builds)

## Requirements

- CMake ≥ 3.22
- Qt **6.9+** (Core, Gui, Quick, Svg, Network; DBus on Linux)
- Git submodules initialized (`src/dependencies/vendor/*`)
- Host tools: C++20 compiler; on Linux `lsblk --json`

Install Qt from https://www.qt.io/download or use the upstream scripts under `qt/`.

## Configure & build (all platforms)

```bash
cd /path/to/katmera-imager
git submodule update --init --recursive

cmake -S src -B build \
  -DCMAKE_BUILD_TYPE=MinSizeRel \
  -DENABLE_TELEMETRY=OFF \
  -DQt6_ROOT=/path/to/Qt/6.9.x/<kit>

cmake --build build -j
```

Binary name: `katmera-imager`.

### macOS (arm64 Homebrew example)

```bash
export PATH="/opt/homebrew/bin:$PATH"
cmake -S src -B build \
  -G Ninja \
  -DCMAKE_BUILD_TYPE=MinSizeRel \
  -DENABLE_TELEMETRY=OFF \
  -DCMAKE_OSX_ARCHITECTURES=arm64 \
  -DCMAKE_PREFIX_PATH="/opt/homebrew;/opt/homebrew/opt/qtbase;/opt/homebrew/opt/qtdeclarative;/opt/homebrew/opt/qtsvg;/opt/homebrew/opt/qttools;/opt/homebrew/opt/qtimageformats"
cmake --build build -j
# Bundle: build/katmera-imager.app
codesign --force --deep --sign - build/katmera-imager.app   # ad-hoc, unsigned distribution
```

Internal artifact name: `Katmera-Imager-{ver}-macos-unsigned.zip` (zip the `.app`).

### Windows (MSVC or Ninja + Qt 6.9+)

```bat
cmake -S src -B build ^
  -G Ninja ^
  -DCMAKE_BUILD_TYPE=MinSizeRel ^
  -DENABLE_TELEMETRY=OFF ^
  -DQt6_ROOT=C:\Qt\6.9.x\msvc2022_64

cmake --build build -j
```

Output: `build\katmera-imager.exe`. Deploy Qt runtime with `windeployqt` for a
portable folder (packaging CMake does this when building installers; for lab
zips run `windeployqt` manually on the exe).

Do **not** set `ENABLE_INNO_INSTALLER` or `IMAGER_SIGNED_APP` for unsigned
internals (those are M6).

Internal artifact name: `Katmera-Imager-{ver}-windows-unsigned.zip`.

### Linux (x86_64)

Plain CMake (distro or vendor Qt 6.9+):

```bash
cmake -S src -B build \
  -G Ninja \
  -DCMAKE_BUILD_TYPE=MinSizeRel \
  -DENABLE_TELEMETRY=OFF \
  -DQt6_ROOT=/path/to/Qt/6.9.x/gcc_64
cmake --build build -j
# Binary: build/katmera-imager
```

Optional unsigned `.deb` via [`debian/`](../../debian/) (see `debian/build-binary-chroot.sh`
and related scripts). Label clearly as unsigned.

Internal artifact names:

- `katmera-imager-{ver}-linux-x86_64-unsigned.tar.gz`
- or `katmera-imager_{ver}_amd64.deb` (unsigned)

## Unsigned vs signed

| Milestone | Signing |
|-----------|---------|
| Now (foundation / Priority 2) | **Unsigned** internal test builds only |
| M6 (Priority 5) | Windows Authenticode, macOS Developer ID + notarization |

Do not Gatekeeper-distribute unsigned macOS builds outside the team.

## Default catalog URL

`src/config.h` → `OSLIST_URL` =
`https://downloads.katmera.com/imager/os_list_v4.json`

Publish steps: [`CATALOG_PUBLISH.md`](CATALOG_PUBLISH.md).

Until that URL returns 200, pass a local stub for lab work:

```bash
./build/katmera-imager --repo "$(pwd)/katmera/catalog/os_list_v4.json"
```

## Test microSD write without Katmera BSP images

1. Select **Nexus Hub** or **Nexus Base** with **OctaPower 3566 AI** or **Omnicore 1126B**.
2. Select **Use custom**.
3. Pick a local `.img` / `.img.xz` / `.img.zip`.
4. Select a removable drive (leave **Exclude system drives** checked).
5. Write and verify.

Stub OS rows are informational (“Image not published yet”) and must not be used
as if they were real Hub downloads.
