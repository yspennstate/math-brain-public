---
name: d10_92_hooks_deterministic_except_trial_arm_and_edit_ledger_2026_11_08
description: "[VERIFIED] Yes, but for two designed exceptions: of 248 hook-payload pairs under two fresh session ids, 246 gave identical output; the show-or-hold trial arm and the shared-edit ledger account for the 2. The audit left 4 harness- rows in instinct_primary_ab.tsv; drop them in analysis"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T04:32:39+04:00
  status: verified
  evidence: "hook_determinism_2026_11_08.py; .json beside it; INSTINCT_PRIMARY_AB=0 rerun 13/13 same; random control flagged, constant not"
---

Are the worker machine's hooks deterministic, so a hook's output depends only on its input? Yes, apart from two designed exceptions. Measured 8 Nov 2026 by an agent (1000-ways D10 #92).

How: hook_determinism_2026_11_08.py runs every hook in hook_dispatch_list.json twice on the same payload, each time under a fresh session id. It uses two ids rather than one so that once-per-session suppression doesn't count as a difference. Before comparing, it masks session ids, clock times, dates, durations, hex ids and pids. The harness's one bland payload per event made only 8 of 89 hooks print anything, so I added payloads that real work produces: a math prompt, a push-and-delete prompt, a git push, an rm -rf, a heredoc into python, an Edit of MEMORY.md, and a Bash call that ended in a traceback. That came to 248 hook-payload pairs, 32 of which printed something, in 15 s. A planted hook that prints a random number was flagged and a planted constant hook was not. The first draft's hex mask also swallowed plain 9-digit numbers and passed the random control; the mask now needs a letter.

Result: 246 of 248 were identical, byte for byte before masking as well. The 2 that differed are both by design:
- instinct_prime on rm -rf dropped the disk-stall reflex (bulk_io_runs_polite) in one run. That is the show-or-hold trial, which holds one reflex in four per (session, reflex) by sha256 of the session id. With INSTINCT_PRIMARY_AB=0, 13 of 13 instinct_prime rows matched.
- shared_edit_collision_hook warned in the second run because the first run, under the other session id, had logged an edit of MEMORY.md. That is cross-session state working as intended.

Side effects, since the audit is not read-only:
- It wrote 4 harness- rows to ~/.claude/dreaming/instinct_primary_ab.tsv, all at 04:28 on 8 Nov. The trial's registered exclusion names only 0000ab sessions. Any analysis of that log must also drop sessions starting harness-.
- It added one harness Edit of MEMORY.md to the shared-edit ledger, so a real session editing MEMORY.md before about 04:58 could have seen a false collision note naming "claude-harness-".
Brain logs are never deleted, so both are recorded here rather than removed. For the next run, point the Edit payload at a file outside the shared tree, or run with INSTINCT_PRIMARY_AB=0.

How to apply: when a hook's output looks different from the same input, check first whether the hook keys on the session id (the trial arm, the backoff) or on another session's state (the ledger). Only then call it a defect. Rerun the audit with the script above. A count of "deterministic" from the old single payload says little, because 81 of 89 hooks were silent on it.

Related: [[show_or_hold_trial_off_on_mac_allowlist_unported_2026_11_08]] - the trial whose arm is the one designed non-determinism found here.
