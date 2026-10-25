---
name: mistake_render_settings_reset_after_update_2026_03_18
description: [VERIFIED] An editor update reset the export preset to 8-bit; three masters went out with banding in the sky shots
metadata:
  type: feedback
status: verified
---

After the editing software updated on 17 March, the export preset silently went back to 8-bit. Three masters were
exported that way and showed banding in the dusk sky shots.

**Why:** nobody re-checked the preset after the update; the file names and sizes looked normal.
**How to apply:** after any software update, export ten seconds of the darkest gradient shot and look at it before exporting a master. A green export is not proof the settings held.
