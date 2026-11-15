---
name: prompt_child_moved_onto_serial_path_2026_11_12
description: "hook_dispatch_extend moves prompt-only parallel children in-process and adds wait"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:08:36+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: Before the 12 Nov selection fix, an unnamed extension pass could promote prompt-only children. Across 5597 prompts the in-process median was 2.1 s versus a slowest child of 0.6 s; waste_sense exceeded 5 s on 51 runs.

Why it happened: Same-output testing ignored event scheduling: prompt, Stop and SessionStart children run in parallel with in-process work. Moving them serially adds their full runtime to the prompt path.

**Why:** Removing process startup can increase the time the user waits.

**How to apply:** Inspect event wiring and critical-path time; test default selection on a copied allowlist with dry-run and a launch recorder. The full control tool has its own selection rule.

[[extend_tool_leaves_prompt_only_child_hooks_alone_2026_11_12]]

Drafted by Codex worker W04 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

