import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

class EngineTests(unittest.TestCase):
    def test_packaged_engine_and_checksums(self):
        packager = load(ROOT / "scripts/package_optional_engine.py")
        verifier = load(ROOT / "engine/selftest.py")
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            (base / "engine").mkdir()
            for name in packager.FILES:
                (base / "engine" / name).write_bytes((ROOT / "engine" / name).read_bytes())
            path = packager.build(base, "0.5.8")
            original = path.read_bytes()
            self.assertEqual(original, packager.build(base, "0.5.8").read_bytes())
            with zipfile.ZipFile(path) as z:
                self.assertIsNone(z.testzip())
                z.extractall(base / "unpacked")
                self.assertEqual(len(z.namelist()), len(packager.FILES) + 1)
            self.assertTrue(verifier.verify(base / "unpacked", "0.5.8"))
            with self.assertRaises(ValueError):
                verifier.verify(base / "unpacked", "0.5.9")
            (base / "unpacked/scripts/validate_pdf.py").write_text("tampered")
            with self.assertRaises(ValueError):
                verifier.verify(base / "unpacked", "0.5.8")

    def test_evidence_and_snapshot_helpers(self):
        evidence = load(ROOT / "engine/validate_evidence.py")
        compare = load(ROOT / "engine/compare_baselines.py")
        valid = [{"claim_id": "A", "assertion": "Example", "source_kind": "regulation",
                  "instrument_id": "EU/example", "source_url": "https://example.org",
                  "checked_at": "2026-10-21", "article": "3", "status": "verified"}]
        self.assertEqual(evidence.validate(valid), [])
        self.assertTrue(evidence.validate([{"claim_id": "A", "status": "verified"}]))
        self.assertEqual(compare.compare(valid, valid)["changed"], [])
        with self.assertRaises(ValueError):
            compare.index(valid + valid)

if __name__ == "__main__":
    unittest.main()
