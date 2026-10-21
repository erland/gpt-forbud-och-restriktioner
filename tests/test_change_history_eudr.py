"""Regression contract for documented EUDR 2025-2026 delta; not a live legal verifier."""
import json, unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class EUDRHistory(unittest.TestCase):
 def test_official_change_baseline(self):
  d=json.loads((R/'evals/eudr-change-baseline.json').read_text())
  self.assertEqual(d['baseline_date'],'2025-01-01')
  self.assertEqual(d['comparison_date'],'2026-10-21')
  self.assertEqual({v['id'] for v in d['changes']},{'EUDR-01','EUDR-02','EUDR-03','EUDR-04'})
  for x in d['changes']:
   self.assertTrue(x['article']);self.assertTrue(x['official_url'].startswith('https://eur-lex.europa.eu/'))
 def test_critical_monitoring_guards(self):
  s=(R/'src/instructions/skills/forandringsbevakning/behavior.md').read_text().lower()
  for marker in ['övergång','före/efter','konsoliderad','schemalagd','ingen förändring']:
   self.assertIn(marker,s)
if __name__=='__main__':unittest.main()
