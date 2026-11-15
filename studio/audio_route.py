"""Choose a speaker profile that keeps the Viture HDMI port selectable."""


def sink_label(description, product_name):
    product = (product_name or "").strip()
    if product:
        return product
    return (description or "").strip()


def viture_port(ports):
    for port in ports:
        product = str(port.get("product") or "")
        if "viture" in product.lower() and port.get("available"):
            return port
    return None


def profile_for(profiles, ports):
    """pro-audio keeps every HDMI port. A single extra profile hides the others."""
    if viture_port(ports) is None:
        return None
    if "pro-audio" in profiles:
        return "pro-audio"
    port = viture_port(ports)
    name = str(port.get("name") or "")
    if name == "hdmi-output-0":
        return "output:hdmi-stereo" if "output:hdmi-stereo" in profiles else None
    suffix = name.removeprefix("hdmi-output-")
    candidate = "output:hdmi-stereo" if suffix == "0" else f"output:hdmi-stereo-extra{suffix}"
    return candidate if candidate in profiles else None
