"""Per-window depth on the Hyprland workspace that already owns the window."""
import json
from pathlib import Path


def load(path):
    file = Path(path)
    if not file.exists():
        return {}
    data = json.loads(file.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Depth file must be an object of window addresses")
    return {str(key): float(value) for key, value in data.items()}


def save(path, depths):
    Path(path).write_text(json.dumps(depths, indent=2) + "\n", encoding="utf-8")


def move(path, address, delta):
    """Push (positive delta) or pull (negative). The Hyprland workspace is untouched."""
    if not isinstance(address, str) or not address.startswith("0x"):
        raise ValueError("Window address must be a Hyprland address")
    depths = load(path)
    current = float(depths.get(address, 0))
    depths[address] = 0.0 if current + delta < 0 else current + delta
    save(path, depths)
    return depths[address]
