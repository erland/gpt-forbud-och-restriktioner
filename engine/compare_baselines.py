#!/usr/bin/env python3
"""Compare claim snapshots; changes do not prove that the underlying law changed."""
import argparse
import json
from pathlib import Path

def index(obj):
    rows = obj if isinstance(obj, list) else obj.get("claims", [])
    if not isinstance(rows, list):
        raise ValueError("claims must be an array")
    ids = [r["claim_id"] for r in rows]
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate claim_id")
    return {r["claim_id"]: r for r in rows}

def compare(before, after):
    old, new = index(before), index(after)
    return {"added": sorted(new.keys()-old.keys()), "removed": sorted(old.keys()-new.keys()),
            "changed": sorted(k for k in old.keys() & new.keys() if old[k] != new[k]),
            "note": "Changes in stored evidence; verify legal effects against primary sources."}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("before", type=Path)
    p.add_argument("after", type=Path)
    args = p.parse_args()
    print(json.dumps(compare(json.loads(args.before.read_text()), json.loads(args.after.read_text())), ensure_ascii=False, indent=2))
