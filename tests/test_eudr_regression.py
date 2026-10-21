from pathlib import Path
import unittest,json
R=Path(__file__).resolve().parents[1]
class EUDRTests(unittest.TestCase):
 def test_three_cases(self):
  cases=json.loads((R/'tests/eudr_cases.json').read_text());self.assertEqual({x['id'] for x in cases},{'T1','T2','T3'});self.assertTrue(all(x['refs'] and x['status'] for x in cases))
 def test_legal_verification_gates(self):
  checklist=(R/'docs/eudr-legal-verification-checklist.md').read_text()
  skill=(R/'src/instructions/skills/regelverksanalys/behavior.md').read_text()
  evidence=(R/'docs/evidence-contract.md').read_text()
  for word in ['artikel 5.1–7','SOU 2025:17','SFS','EJ VERIFIERAD','PARTIAL']:
   self.assertIn(word,checklist)
  self.assertIn('Kvalitetssäkring för EUDR',skill)
  self.assertIn('Evidensgrind för juridisk acceptans',evidence)
 def test_core_safety(self):
  s=(R/'src/instructions/core.md').read_text();self.assertIn('automatiskt',s.lower());self.assertIn('ej verifierat',s.lower());self.assertIn('okänd KN/TARIC',s)
if __name__=='__main__':unittest.main()
