---
name: d10_61_hook_dispatch_is_the_failsafe_wrapper_0_of_36_bad_inputs_2026_11_08
description: "[VERIFIED] No, never: hook_dispatch.py already is D10 #61's fail-safe wrapper. 0 of 36 dispatcher calls (6 events x 5 broken inputs + control) exited non-zero; run directly, 13 of 445 hook runs raise rc 1 (never rc 2), only on a JSON list or wrong types"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T04:36:38+04:00
  status: verified
  evidence: "dispatch_bad_input_2026_11_08.py; hook_bad_input_2026_11_08.py and .json; raising control caught 5/5"
---

Does a hook that throws ever block a tool call on this worker machine? No. That makes 1000-ways D10 #61 ("fail-closed hook wrapper") already true, because hook_dispatch.py is that wrapper. Measured 8 Nov 2026 by an agent.

The dispatcher's contract: a hook that raises or exits non-zero is caught and logged, only exit 2 blocks, and a broken dispatcher exits 0. I checked it as settings.json calls it (python3 -s hook_dispatch.py --event EV), for the 6 wired events, on five broken inputs: empty stdin, non-JSON text, a JSON list, an object with every field the wrong type, and the event name alone. All 36 calls exited 0, including a well-formed control call for each event. Every stdout was empty or one JSON object (dispatch_bad_input_2026_11_08.py).

Run directly, outside the dispatcher, 13 of the 445 hook-input runs end in a traceback with rc 1, and none blocks (rc 2). They come only from a JSON list or wrong field types, which Claude Code never sends: instinct_prime, video_job_guard, brain_data_guard, effort_guard, codex_profile_hooks, summary_hook, prompt_archive, brain_switch and crash_breadcrumb do `data.get(...)` or `.strip()` without a type check. All 89 hooks handle empty or non-JSON stdin. A planted hook that raises was caught on 5 of 5 inputs (hook_bad_input_2026_11_08.py).

How to apply: don't build a second wrapper. If a hook is ever wired straight into settings.json instead of through the dispatcher, it loses this protection, so check the wiring first. The 13 type-check gaps are not worth editing shared hooks for unless the input format changes.

Related: [[d10_92_hooks_deterministic_except_trial_arm_and_edit_ledger_2026_11_08]] - the same pass over the hooks, same harness.

