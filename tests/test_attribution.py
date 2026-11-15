"""The local tree keeps credit for the original Omarchy XR developer."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AttributionTests(unittest.TestCase):
    def test_readme_names_andreas_fruth_as_original_developer(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Andreas Fruth", text)
        self.assertIn("original developer", text)
        self.assertIn("omarchy-xr", text)
        self.assertIn("original creator of", text)
        self.assertIn("https://github.com/afruth/omarchy-xr", text)

    def test_license_keeps_the_reserved_rights_copyright(self):
        text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 Andreas Fruth", text)
        self.assertIn("No other rights to modify, sublicense, sell, or redistribute", text)
