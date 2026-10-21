#!/usr/bin/env python3
"""Build a deterministic, release-versioned and SHA-256 indexed optional engine."""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

PROJECT = "forbud-och-restriktioner"
FILES = ("validate_evidence.py", "compare_baselines.py", "validate_pdf.py", "requirements.txt")
STAMP = (2020, 1, 1, 0, 0, 0)

def build(root, version):
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:[.-][a-zA-Z0-9.-]+)?", version):
        raise ValueError("invalid version")
    engine = root / "engine"
    payload = {f"scripts/{p}": (engine / p).read_bytes() for p in FILES}
    manifest = {"project_id": PROJECT, "version": version, "format_version": 1,
                "files": [{"path": name, "sha256": hashlib.sha256(data).hexdigest(), "size": len(data)}
                          for name, data in sorted(payload.items())]}
    payload["ENGINE-MANIFEST.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    out = root / "dist" / f"{PROJECT}-engine-{version}.zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(name, STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=Path("."))
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    print(build(args.project_root.resolve(), args.version))
