import json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class ChangeMonitoring(unittest.TestCase):
 def test_skill_contract(self):
  x=(R/'src/instructions/skills/forandringsbevakning/behavior.md').read_text()
  for marker in ['Ändrad genom','artikel/paragraf','baslinje','schemalagd','initial inventering','EU-kommissionens','före/efter']:
   self.assertIn(marker.lower(),x.lower())
 def test_core_contract(self):
  x=(R/'src/instructions/core.md').read_text();self.assertIn('förändringskontroll A-05',x);self.assertIn('ej aktiverad',x)
 def test_schema(self):
  j=json.loads((R/'knowledge/change-report-schema.json').read_text());self.assertIn('changes',j['required']);self.assertIn('coverage',j['required'])
 def test_sources(self):
  s=(R/'knowledge/change-monitoring-sources.md').read_text();self.assertIn('eur-lex.europa.eu',s);self.assertIn('riksdagen.se',s)
if __name__=='__main__':unittest.main()
