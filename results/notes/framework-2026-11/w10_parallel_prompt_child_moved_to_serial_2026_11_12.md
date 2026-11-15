---
name: w10_parallel_prompt_child_moved_to_serial_2026_11_12
description: "Moving prompt-only hooks into the fast allowlist can add latency instead of removing it"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:51:29+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The extension tool would have moved fleet_inbox_hook.py and waste_sense.py in-process. Across 5,597 prompts the serial work median was 2.1 s, the slowest child 0.6 s; waste_sense exceeded 5 s 51 times. The changed extension passed 14/14 controls; the old file failed 3 target cases.

Why it happened: Output equality alone was treated as enough to migrate a hook. Prompt, stop, and start child hooks already ran beside serial hooks, so serializing them could add their full runtime to the wait.

**Why:** Fast-list membership is not a speed measurement; event scheduling determines the critical path.

**How to apply:** Inspect event wiring and PARALLEL_SUBPROC_EVENTS before migration, leave prompt-only children alone, and test allowlist changes on a scratch copy.

Input evidence: item 016 (2026-11-12 03:02, T-20261110-113, [an agent]), item 073 (2026-11-12 02:38, T-20261110-113, [an agent]).

Source memories: [[extend_tool_leaves_prompt_only_child_hooks_alone_2026_11_12]] [[rank_prompt_hooks_by_wait_parallel_children_are_off_the_critical_path_2026_11_11]]

Drafted by Codex worker W10 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

