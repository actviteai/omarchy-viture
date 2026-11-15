import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "studio"))
from window_depth import move


class WindowDepthTests(unittest.TestCase):
    def test_push_and_pull_stay_on_the_same_address(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "depth.json"
            self.assertEqual(move(path, "0xabc", 2), 2)
            self.assertEqual(move(path, "0xabc", -5), 0)
            text = path.read_text(encoding="utf-8")
            self.assertIn("0xabc", text)
            self.assertNotIn("workspace", text)
