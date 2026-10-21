import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ScoringTests(unittest.TestCase):
    def test_three_dimensions(self):
        manifest = json.loads((ROOT / 'tests/test-manifest.json').read_text())
        self.assertEqual(manifest['acceptance_scoring']['version'], 'LEG-003.1')
        self.assertEqual(len(manifest['acceptance_scoring']['dimensions']), 3)
        self.assertEqual(len(manifest['acceptance_scenarios']), 10)
        self.assertFalse(manifest['acceptance_scoring']['separate_plugin_process_required'])
        self.assertTrue(all('expected_verdict' not in c for c in manifest['acceptance_scenarios']))

if __name__ == '__main__':
    unittest.main()
