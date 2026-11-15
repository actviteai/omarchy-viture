#pragma once
// A display target is fullscreen only when the caller asked to take that
// output. The windowed preview leaves the keyboard on the desk display.
inline bool fullscreenDisplay(bool hasDisplay, bool windowed) {
    return hasDisplay && !windowed;
}
