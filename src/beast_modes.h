#pragma once
// Native display modes for VITURE Beast while native mode is 1.
// Host mode 0x32 is a different table: in bypass it means side-by-side
// 3840x1080 at 60 Hz. In this native table 0x32 is 1920x1080 at 90 Hz.
#define VITURE_NATIVE_DISPLAY_MODE_1920_1080_60HZ 0x31
#define VITURE_NATIVE_DISPLAY_MODE_3D_SBS_3840_1080_60HZ 0x37
