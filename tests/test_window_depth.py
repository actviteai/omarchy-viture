import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "studio"))
from window_depth import load, move, opacity, view_offset


class WindowDepthTests(unittest.TestCase):
    def test_push_increases_depth_and_lowers_opacity(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "depth.json"
            self.assertEqual(move(path, "0xabc", 1), 1)
            self.assertAlmostEqual(opacity(1), 0.84)
            self.assertAlmostEqual(view_offset(1), 0.35)

    def test_pull_stops_at_the_front(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "depth.json"
            move(path, "0xabc", 1)
            self.assertEqual(move(path, "0xabc", -5), 0)
            self.assertEqual(opacity(0), 1.0)
            self.assertEqual(view_offset(0), 0.0)

    def test_a_non_address_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "depth.json"
            with self.assertRaises(ValueError):
                move(path, "foot", 1)

    def test_a_missing_file_has_no_windows(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(load(Path(folder) / "missing.json"), {})
