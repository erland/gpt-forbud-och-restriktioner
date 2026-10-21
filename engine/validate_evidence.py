#!/usr/bin/env python3
"""Deterministic structural verification of evidence claims; not a legal opinion."""
import argparse
import json
from pathlib import Path

REQUIRED = ("claim_id", "assertion", "source_kind", "instrument_id", "source_url", "checked_at", "status")
VALID = {"verified", "partially_verified", "unverified", "superseded"}

def validate(payload):
    claims = payload if isinstance(payload, list) else payload.get("claims", [])
    if not isinstance(claims, list):
        return ["claims must be an array"]
    errors = []
    for n, claim in enumerate(claims, 1):
        if not isinstance(claim, dict):
            errors.append(f"claim {n}: object expected")
            continue
        for key in REQUIRED:
            if not isinstance(claim.get(key), str) or not claim[key].strip():
                errors.append(f"claim {n}: missing {key}")
        if claim.get("status") not in VALID:
            errors.append(f"claim {n}: invalid status")
        if claim.get("status") == "verified" and not any(claim.get(key) for key in ("article", "paragraph", "annex")):
            errors.append(f"claim {n}: verified claim lacks legal pinpoint")
        if claim.get("source_url") and not str(claim["source_url"]).startswith("https://"):
            errors.append(f"claim {n}: source_url must be https")
    return errors

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    args = p.parse_args()
    errors = validate(json.loads(args.input.read_text(encoding="utf-8")))
    print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False))
    raise SystemExit(bool(errors))
