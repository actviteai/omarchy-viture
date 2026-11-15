import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "studio"))
from audio_route import profile_for, sink_label


class AudioRouteTests(unittest.TestCase):
    def test_label_uses_the_port_product_name(self):
        self.assertEqual(sink_label("Digital Stereo (HDMI 3)", "VITURE Beast"), "VITURE Beast")
        self.assertEqual(sink_label("Analog", ""), "Analog")

    def test_pro_audio_keeps_the_viture_port_beside_the_monitor(self):
        ports = [
            {"name": "hdmi-output-0", "product": "MAG 276CXF", "available": True},
            {"name": "hdmi-output-2", "product": "VITURE Beast", "available": True},
        ]
        profiles = ["output:hdmi-stereo", "output:hdmi-stereo-extra2", "pro-audio"]
        self.assertEqual(profile_for(profiles, ports), "pro-audio")

    def test_extra_profile_is_the_fallback(self):
        ports = [{"name": "hdmi-output-2", "product": "VITURE Beast", "available": True}]
        self.assertEqual(profile_for(["output:hdmi-stereo-extra2"], ports), "output:hdmi-stereo-extra2")
