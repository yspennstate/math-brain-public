---
name: prompt_child_promotion_adds_wait_instead_of_removing_it_2026_11_12
description: "hook_dispatch_extend waste_sense fleet_inbox_hook in-process promotion critical path latency"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:13:19+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The liveness report recommended moving waste_sense.py and fleet_inbox_hook.py into the in-process list. On 5,597 prompts the in-process chain median was 2,135 ms, versus 644 ms for the slowest child; a child outlasted the chain on 467 prompts. waste_sense exceeded 5 s on 51 calls. The report was corrected, but hook_dispatch_extend.py --only waste_sense.py could still admit it. This is a recorded bad recommendation and near miss, not a measured slowdown after promotion.

Why it happened: The recommendation counted a saved interpreter launch without accounting for prompt-only children already running beside the chain. fleet_inbox_hook also gives different output on repeated runs. An exact-output admission test alone does not establish a latency improvement.

**Why:** Moving overlapping work onto the serial path can add the whole child runtime and its tail to the wait.

**How to apply:** Profile wait and overlap before promotion, keep these children separate on this evidence, and compare old/new outputs on the same real inputs for any optimization; the method note reports 3,255/3,255 identical canonical_route outputs and 0 differences on 3,413 proof_sense texts.

[[liveness_stop_order_alarm_was_the_loop_keeper_entries_2026_11_12]]
[[method_cut_a_hooks_latency_by_skipping_known_work_2026_11_12]]

Drafted by Codex worker W05 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

