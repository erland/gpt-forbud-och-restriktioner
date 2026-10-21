#!/usr/bin/env python3
"""Verify extracted engine manifest integrity before executing helpers."""
import argparse
import hashlib
import json
from pathlib import Path

def verify(root, expected_version):
    manifest = json.loads((root / "ENGINE-MANIFEST.json").read_text(encoding="utf-8"))
    if manifest.get("version") != expected_version or manifest.get("project_id") != "forbud-och-restriktioner":
        raise ValueError("engine identity/version mismatch")
    names = [entry["path"] for entry in manifest["files"]]
    if len(names) != len(set(names)):
        raise ValueError("duplicate paths")
    for entry in manifest["files"]:
        path = Path(entry["path"])
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("unsafe path")
        data = (root / path).read_bytes()
        if len(data) != entry["size"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise ValueError("integrity failure: " + entry["path"])
    return True

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=Path("."))
    p.add_argument("--version", required=True)
    a = p.parse_args()
    verify(a.root, a.version)
    print("PASS: integrity and version")
