#!/usr/bin/env python3
"""Validate Katmera Repository JSON V4 stub catalog (Phase 1 foundation)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "katmera" / "catalog" / "os_list_v4.json"
SCHEMA = ROOT / "doc" / "json-schema" / "os-list-schema.json"

PHASE1_TAGS = {
    "nexus-hub-octapower-3566-ai",
    "nexus-hub-omnicore-1126b",
}

# Stub OS entries (images not published yet) may omit download URL fields.
STUB_REQUIRED = {
    "name",
    "description",
    "icon",
    "release_date",
    "devices",
}


def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    if "os_list" not in data or not isinstance(data["os_list"], list):
        print("error: missing os_list", file=sys.stderr)
        return 1
    if "imager" not in data or "devices" not in data["imager"]:
        print("error: missing imager.devices", file=sys.stderr)
        return 1

    device_tags = set()
    for d in data["imager"]["devices"]:
        for t in d.get("tags", []):
            device_tags.add(t)
    if device_tags != PHASE1_TAGS:
        print(f"error: device tags {device_tags} != {PHASE1_TAGS}", file=sys.stderr)
        return 1

    for entry in data["os_list"]:
        missing = STUB_REQUIRED - set(entry)
        if missing:
            print(f"error: {entry.get('name')}: missing {missing}", file=sys.stderr)
            return 1
        if entry.get("init_format") != "none":
            print(f"error: {entry.get('name')}: init_format must be 'none'", file=sys.stderr)
            return 1
        if not set(entry.get("devices", [])) & PHASE1_TAGS:
            print(f"error: {entry.get('name')}: devices must include a Phase 1 tag", file=sys.stderr)
            return 1
        desc = (entry.get("description") or "").lower()
        if "url" in entry and entry["url"]:
            print(
                f"warn: {entry.get('name')}: has url — ok once real images publish; "
                "stubs should omit url until then"
            )
        elif "not published" not in desc and "not available" not in desc:
            print(
                f"error: {entry.get('name')}: stub without url must say image not published",
                file=sys.stderr,
            )
            return 1

    if SCHEMA.exists():
        try:
            import jsonschema  # type: ignore
        except ImportError:
            print("warn: jsonschema not installed; skipped formal schema check")
        else:
            # Formal schema may require url; stubs intentionally omit it until M3.
            print("warn: stub catalog may not pass full upstream schema until real urls exist")

    print(f"ok: {CATALOG.relative_to(ROOT)} ({len(data['os_list'])} stub images)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
