# Building Katmera Imager (unsigned test builds)

## Requirements

- CMake ≥ 3.22
- Qt **6.9+** (Core, Gui, Quick, Svg, Network; DBus on Linux)
- Git submodules initialized (`src/dependencies/vendor/*`)
- Host tools: C++20 compiler; on Linux `lsblk --json`

This environment may not have Qt/CMake installed. Install Qt from
https://www.qt.io/download or use the upstream scripts under `qt/`.

## Configure & build

```bash
cd /path/to/katmera-imager
git submodule update --init --recursive

cmake -S src -B build \
  -DCMAKE_BUILD_TYPE=MinSizeRel \
  -DENABLE_TELEMETRY=OFF \
  -DQt6_ROOT=/path/to/Qt/6.9.x/<kit>

cmake --build build -j
```

Binary name: `katmera-imager` (macOS bundle: `Katmera Imager.app`).

## Unsigned vs signed

| Milestone | Signing |
|-----------|---------|
| Now (M0–M2) | **Unsigned** internal test builds only |
| M6 | Windows Authenticode, macOS Developer ID + notarization |

Do not Gatekeeper-distribute unsigned macOS builds outside the team.

## Test microSD write without Katmera BSP images

BSP images are not published yet. Use a local file:

```bash
./build/katmera-imager --repo "$(pwd)/katmera/catalog/os_list_v4.json"
```

1. Select **Nexus Hub + OctaPower 3566 AI** or **Nexus Hub + Omnicore 1126B**.
2. Select **Use custom**.
3. Pick a local `.img` / `.img.xz` / `.img.zip`.
4. Select a removable drive (leave **Exclude system drives** checked).
5. Write and verify.

Stub OS rows in the catalog are informational (“Image not published yet”) and
must not be used as if they were real Hub downloads.

## Default catalog URL

`src/config.h` → `OSLIST_URL` =
`https://downloads.katmera.com/imager/os_list_v4.json`

Until that host exists, always pass `--repo` to the repo-local stub JSON.
