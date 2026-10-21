"""Regression: every generated Plugin Skill exposes the release version."""
import json
from pathlib import Path
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PROJECT_ID = "forbud-och-restriktioner"

class PluginVersionTests(unittest.TestCase):
    def test_generated_plugin_skill_versions_match_manifest(self):
        archives = sorted((ROOT / "dist").glob(f"{PROJECT_ID}-plugin-*.zip"))
        if not archives:
            self.skipTest("Distributionsbygge krävs innan paketkontroll")
        with zipfile.ZipFile(archives[-1]) as z:
            self.assertIsNone(z.testzip())
            manifest = json.loads(z.read("plugin.json"))
            version = manifest["version"]
            self.assertEqual(manifest["name"], PROJECT_ID)
            skills = sorted(n for n in z.namelist() if n.startswith("skills/") and n.endswith("/SKILL.md"))
            self.assertEqual(len(skills), 3)
            for skill in skills:
                text = z.read(skill).decode("utf-8")
                frontmatter = text.split("---", 2)[1]
                self.assertIn(f"  plugin_id: {PROJECT_ID}\n", frontmatter)
                self.assertIn(f"  plugin_version: {version}\n", frontmatter)

if __name__ == "__main__":
    unittest.main()
