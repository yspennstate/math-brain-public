---
name: method_one_test_shot_before_any_long_render_2026_03_19
description: Before a render longer than an hour, render ten seconds of the hardest shot and check it - it catches settings drift cheaply
metadata:
  type: feedback
status: verified
---

Render ten seconds of the hardest shot first (darkest gradient, fastest motion, densest titles) and look at it.
Only then start the long render.

**Why:** generalises [[mistake_render_settings_reset_after_update_2026_03_18]]; ten seconds costs a minute, a bad master costs a night.
**How to apply:** every long render starts with a test clip, and the report names the shot that was checked.
