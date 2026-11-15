#pragma once
// Positive depth is farther from the user. Zero is the workspace plane.
// Push increases depth. Pull decreases it and does not pass the plane.
inline float windowDepth(float current, float delta) {
    const float next = current + delta;
    return next < 0.f ? 0.f : next;
}
// One step is 0.35 world units farther from the eye, and a little more transparent.
inline float depthOffset(float depth) {
    return depth > 0.f ? depth * 0.35f : 0.f;
}
inline float depthOpacity(float depth) {
    if (!(depth > 0.f)) return 1.f;
    const float value = 1.f - 0.16f * depth;
    return value < 0.35f ? 0.35f : value;
}
