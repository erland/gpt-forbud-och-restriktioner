"""Kontroller för OpenCode-dokumentation i källmall och genererad distribution."""
from pathlib import Path
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = (
    "OpenCode-workspace för GPT Byggaren",
    "gpt_build_distributions",
    "gpt_lint_project",
    "lägg det GPT-projekt",
    "projektlokala custom tools under `.opencode/tools/`",
)

class RuntimeDocumentationTests(unittest.TestCase):
    def check_text(self, text):
        self.assertIn("Förbud och Restriktioner", text)
        self.assertIn("regelverksanalys", text)
        self.assertIn("rapportpublicering", text)
        self.assertIn("förändringsbevakning", text)
        for phrase in FORBIDDEN:
            self.assertNotIn(phrase, text)

    def test_opencode_template(self):
        self.check_text((ROOT / "templates/README.opencode.md.tpl").read_text(encoding="utf-8"))

    def test_generated_opencode_readme_when_built(self):
        zips = sorted((ROOT / "dist").glob("*-opencode-*.zip"))
        if not zips:
            self.skipTest("Bygg först; kör testet igen efter distributionsbygget")
        with zipfile.ZipFile(zips[-1]) as archive:
            self.assertEqual(archive.testzip(), None)
            self.check_text(archive.read("README.md").decode("utf-8"))

if __name__ == "__main__":
    unittest.main()
