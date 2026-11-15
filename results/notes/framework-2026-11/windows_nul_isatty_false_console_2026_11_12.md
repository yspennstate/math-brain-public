---
name: windows_nul_isatty_false_console_2026_11_12
description: "Windows owner-only installer stdin DEVNULL passes isatty console gate"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:41:02+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 12 Nov one headless install_codex_dispatch.py case passed isatty and reached input(), which refused at EOF with the wrong message. Nothing was written; after the fix all three headless forms, NUL, redirected file and piped word, were refused by the console gate.

Why it happened: Windows NUL is a character device, so isatty alone does not establish a real console.

**Why:** A character-device check cannot enforce an owner-only console requirement.

**How to apply:** Combine isatty with GetConsoleMode on the stdin handle, retain typed confirmation, and exercise all three headless cases.

[[isatty_is_true_for_nul_on_windows_use_getconsolemode_2026_11_12]]

Drafted by Codex worker W08 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

