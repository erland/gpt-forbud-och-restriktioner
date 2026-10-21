from pathlib import Path
import unittest
R=Path(__file__).resolve().parents[1]
class ContractTests(unittest.TestCase):
 def test_core_gates(self):
  s=(R/'src/instructions/core.md').read_text()
  for term in ['evidensmatris','svensk-rätt-kontroll','aktörs- och varukodsprövning','EJ VERIFIERAD','PDF']: self.assertIn(term,s)
 def test_skill_specific(self):
  specs={'regelverksanalys':['TARIC','paragraf','aktörsroll'],'rapportpublicering':['evidensmatris','Svensk kompletterande rätt','AI-märks'],'forandringsbevakning':['schemaläggning','ändrade']}
  for skill,terms in specs.items():
   s=(R/f'src/instructions/skills/{skill}/behavior.md').read_text().lower()
   for term in terms: self.assertIn(term.lower(),s)
 def test_evidence_schema(self):
  s=(R/'docs/evidence-contract.md').read_text()
  for term in ['claim_id','instrument_id','article','checked_at','goods_conditions','partially_verified']: self.assertIn(term,s)
if __name__=='__main__':unittest.main()
