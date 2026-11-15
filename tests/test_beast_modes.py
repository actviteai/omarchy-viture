import unittest
from pathlib import Path

HEADER = Path(__file__).resolve().parents[1] / "src" / "beast_modes.h"


class BeastModeTests(unittest.TestCase):
    def test_header_lists_native_1080p_and_side_by_side(self):
        text = HEADER.read_text(encoding="utf-8")
        self.assertIn("#define VITURE_NATIVE_DISPLAY_MODE_1920_1080_60HZ 0x31", text)
        self.assertIn("#define VITURE_NATIVE_DISPLAY_MODE_3D_SBS_3840_1080_60HZ 0x37", text)
