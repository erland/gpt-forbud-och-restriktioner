"""LEG-002: profile resource coverage and Plugin distribution parity."""
from pathlib import Path
import json
import unittest
import zipfile
import yaml

ROOT = Path(__file__).resolve().parents[1]
IDS = ("cites", "cbam", "sanktioner")

class DomainProfilesTests(unittest.TestCase):
    def test_profiles_declared_and_grounded(self):
        cfg = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
        skill = next(x for x in cfg["skills"]["definitions"] if x["id"] == "regelverksanalys")
        for name in IDS:
            path = f"knowledge/regulatory-profiles/{name}.md"
            self.assertIn(path, skill["references"])
            text = (ROOT / path).read_text(encoding="utf-8")
            for marker in ("LEG-002", "LEG-001", "PARTIAL", "Officiella", "primärrätt"):
                self.assertIn(marker, text)

    def test_compiled_plugin_contains_all_profiles(self):
        archives = sorted((ROOT / "dist").glob("forbud-och-restriktioner-plugin-*.zip"))
        if not archives:
            self.skipTest("Build distributions before testing archive")
        with zipfile.ZipFile(archives[-1]) as z:
            self.assertIsNone(z.testzip())
            names = set(z.namelist())
            skill = z.read("skills/regelverksanalys/SKILL.md").decode("utf-8")
            for name in IDS:
                self.assertIn(f"references/{name}.md", names)
                self.assertIn(f"references/{name}.md", skill)

if __name__ == "__main__":
    unittest.main()
