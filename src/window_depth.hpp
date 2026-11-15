#pragma once
// Positive depth is farther from the user. Zero is the workspace plane.
// Push increases depth. Pull decreases it and does not pass the plane.
inline float windowDepth(float current, float delta) {
    const float next = current + delta;
    return next < 0.f ? 0.f : next;
}
