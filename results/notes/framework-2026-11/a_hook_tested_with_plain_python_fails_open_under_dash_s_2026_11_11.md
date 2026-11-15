---
name: a_hook_tested_with_plain_python_fails_open_under_dash_s_2026_11_11
description: "[VERIFIED] Hook guard passes its tests but never refuses live? Hooks run python -s (no user site); psutil lives only in the user site, so the import fails and a fail-open handler hides it. Test hooks under python -s; log the fail-open."
metadata:
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T06:46:31+02:00
  status: verified
  evidence: "11 Nov 06:0x: test_rseg.sh 11/11 under python -s; rseg_replay.py deny=True through hook_dispatch.py; a real Edit of a running script refused by the harness; brain commit 35e6e1d"
  lesson: true
---

A PreToolUse guard (running_script_edit_guard.py, meant to refuse an Edit/Write of a bash script that is running right now) passed its 11 tests and still let every live edit through. The hooks run as `python -s`, which drops the user site-packages, and psutil on this laptop lives only there (AppData/Roaming/Python/Python314/site-packages). Under `-s` the `import psutil` raised, the guard's top-level handler failed open, and nothing was logged. The tests ran plain `python`, so they imported psutil fine and passed.

Fix (11 Nov 06:0x, sha256 29dddb50412f): a `_psutil()` helper imports psutil and, on ModuleNotFoundError, appends `site.getusersitepackages()` to sys.path and retries (the same pattern as math_sense._ensure_user_site); the fail-open handler now appends a traceback to running_script_edit_guard.err (capped at 200 KB). The tests now run `python -s`. Verified three ways: 11/11 tests under -s, a replayed real-shaped Edit event through hook_dispatch.py returned deny, and a real Edit tool call on a running script was refused by the harness.

How to apply: any hook that imports a third-party module (psutil, numpy, yaml) must be tested the way the dispatcher runs it, `python -s`, and a fail-open handler must leave a trace somewhere. A guard that is green in its tests but never refuses in the wild is the first thing to suspect. Pushed in brain commit 35e6e1d (12_cognitive_architecture/dreaming/running_script_edit_guard.py and test_running_script_edit_guard.sh). Related: [[editing_a_running_bash_script_shifts_its_lines_2026_10_30]], [[core_steer_selftest_two_failures_stale_check_and_silent_no_psutil_2026_11_11]].

