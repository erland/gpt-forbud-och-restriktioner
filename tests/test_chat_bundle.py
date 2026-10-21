"""Engine 1.6.27: verify that regulatory Chat ZIP excludes the offline generator."""
import unittest
from pathlib import Path
import zipfile
import yaml

ROOT = Path(__file__).resolve().parents[1]

class ChatBundleTests(unittest.TestCase):
    def test_chat_opt_out_config(self):
        cfg = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
        self.assertIs(cfg["runtime"]["chat_zip"]["bundle_distribution_engine"], False)

    def test_generated_chat_zip_has_no_engine(self):
        outputs = sorted((ROOT / "dist").glob("forbud-och-restriktioner-chat-*.zip"))
        if not outputs:
            self.skipTest("Build Chat ZIP before asserting generated package")
        with zipfile.ZipFile(outputs[-1]) as archive:
            self.assertIsNone(archive.testzip())
            names = archive.namelist()
            self.assertFalse(any(n.startswith("distribution-engine/") for n in names))
            self.assertIn("assistant/instructions.md", names)
            self.assertIn("MANIFEST.json", names)

if __name__ == "__main__":
    unittest.main()
