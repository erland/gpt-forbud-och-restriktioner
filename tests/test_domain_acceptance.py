import json
from pathlib import Path
import unittest
import yaml

ROOT=Path(__file__).resolve().parents[1]

class DomainAcceptanceFixtureTests(unittest.TestCase):
    def test_complete_domain_coverage_and_uncertainty(self):
        data=json.loads((ROOT/"tests/domain_acceptance_cases.json").read_text(encoding="utf-8"))
        self.assertEqual(data["coverage_kind"], "functional_acceptance_prompts_not_executed")
        cases=data["cases"]
        self.assertEqual(len(cases),6)
        self.assertEqual(len({x["id"] for x in cases}),6)
        for domain in ("cites","cbam","sanktioner"):
            members=[x for x in cases if x["domain"]==domain]
            self.assertEqual(len(members),2)
            self.assertEqual({x["verdict"] for x in members},{"PARTIAL","CONDITIONAL"})
            self.assertTrue(all(len(x["expect"])>=3 and x["case"] for x in members))
            self.assertTrue((ROOT/f"knowledge/regulatory-profiles/{domain}.md").exists())

    def test_scenarios_registered_for_installed_runtime(self):
        manifest=json.loads((ROOT/"tests/test-manifest.json").read_text(encoding="utf-8"))
        ids={x["id"] for x in manifest["acceptance_scenarios"]}
        for domain in ("CITES","CBAM","SANCTIONS"):
            self.assertTrue(any(x.startswith(domain+"-") for x in ids))
        self.assertIn("test_domain_acceptance.py",manifest["test_modules"])
        self.assertIn("installed_plugin_execution",manifest["excluded"])

if __name__=="__main__":
    unittest.main()
