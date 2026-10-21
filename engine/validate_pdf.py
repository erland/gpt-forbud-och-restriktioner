#!/usr/bin/env python3
"""Technical PDF checks; no assertion of legal correctness."""
import argparse
import json
from pathlib import Path

def validate(path):
    from pypdf import PdfReader
    reader = PdfReader(str(path))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    ai = "AI-genererat" in text or "AI-generated" in text
    references = ("http" in text) or any(page.get("/Annots") for page in reader.pages)
    return {"ok": bool(reader.pages) and ai and bool(references), "pages": len(reader.pages),
            "ai_marking": ai, "source_references": bool(references)}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("pdf", type=Path)
    args = p.parse_args()
    result = validate(args.pdf)
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(not result["ok"])
