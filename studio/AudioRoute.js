.pragma library

// Prefer the HDMI port's product name. A nickname such as "HDMI 3" hides it.
function sinkLabel(description, productName) {
    var product = String(productName || "").trim()
    if (product.length) return product
    return String(description || "").trim()
}
