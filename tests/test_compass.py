import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "studio"))
from backend import validate
from workspace_presets import built_in_setups


def angles(layout):
    monitors = layout["monitors"]
    left = min(m["x"] for m in monitors)
    right = max(m["x"] + m["width"] for m in monitors)
    span = right - left
    center = (left + right) / 2
    return [((m["x"] + m["width"] / 2) - center) / span * layout["workspaceDegrees"] for m in monitors]


class CompassTests(unittest.TestCase):
    def test_four_monitors_are_a_quarter_turn_apart(self):
        layout = next(item["layout"] for item in built_in_setups() if item["id"] == "builtin:compass")
        validate(layout)
        self.assertEqual([m["id"] for m in layout["monitors"]], ["west", "north", "east", "south"])
        self.assertEqual(layout["workspaceDegrees"], 360)
        self.assertTrue(layout["workspaceFollow"])
        found = angles(layout)
        gaps = [found[i + 1] - found[i] for i in range(3)]
        self.assertTrue(all(abs(gap - 90) < 1 for gap in gaps), found)
