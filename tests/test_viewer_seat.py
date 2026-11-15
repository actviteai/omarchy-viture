import unittest
from pathlib import Path

HEADER = Path(__file__).resolve().parents[1] / "src" / "viewer_seat.hpp"


class ViewerSeatTests(unittest.TestCase):
    def test_windowed_preview_does_not_take_the_display(self):
        text = HEADER.read_text(encoding="utf-8")
        self.assertIn("return hasDisplay && !windowed;", text)
