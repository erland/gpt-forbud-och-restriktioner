import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class SourceDiscoveryTests(unittest.TestCase):
    def test_universal_discovery_gate(self):
        core = (ROOT / "src/instructions/core.md").read_text(encoding="utf-8")
        for term in ("SRC-001", "LEG-001", "officiella", "primärverifierad", "parallella regelverk", "ingen Engine-ZIP", "ej kontrollerbar"):
            self.assertIn(term, core)

    def test_analysis_and_monitoring_skills(self):
        analysis = (ROOT / "src/instructions/skills/regelverksanalys/behavior.md").read_text(encoding="utf-8")
        monitoring = (ROOT / "src/instructions/skills/forandringsbevakning/behavior.md").read_text(encoding="utf-8")
        self.assertIn("SRC-001", analysis)
        self.assertIn("Profiler är inte uttömmande", analysis)
        self.assertIn("SRC-001", monitoring)
        self.assertIn("initial inventering", monitoring)
        self.assertIn("Ingen schemalagd bevakning", monitoring)

if __name__ == "__main__":
    unittest.main()
