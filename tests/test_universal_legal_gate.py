from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class UniversalLegalGateTests(unittest.TestCase):
    def test_common_gate_across_domains(self):
        core = (ROOT / "src/instructions/core.md").read_text(encoding="utf-8")
        skill = (ROOT / "src/instructions/skills/regelverksanalys/behavior.md").read_text(encoding="utf-8")
        evidence = (ROOT / "docs/evidence-contract.md").read_text(encoding="utf-8")
        for term in ("LEG-001", "CITES", "CBAM", "sanktioner", "kemikalier", "produktsäkerhet", "PAR​TIAL".replace("\u200b", ""), "svensk rätt", "samtidiga regelverk"):
            self.assertIn(term, core)
        for term in ("PASS", "PARTIAL", "FAIL", "primärkälla"):
            self.assertIn(term, evidence)
        self.assertIn("LEG-001", skill)
        self.assertIn("EUDR-regressionskrav", core)

if __name__ == "__main__":
    unittest.main()
