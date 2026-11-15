---
name: fleet_scaled_before_any_end_to_end_pass_2026_11_12
description: "Primary Directive fleet burns both Claude windows before one worker passes the gate"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:36:44+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 7 Oct the author asked what had been learned and called the fleet a big mistake. The existing mistake ledger records about 100 workers, 0 two-keep items, 281 landed edges in nine hours, 1.13B input tokens with 97-98% context rereads and 8.5M output; these numbers come from the existing memory, not from re-fired prompt counts.

Why it happened: The fleet scaled before a full gate pass; changing the record specification and copying account load produced rework and rereads.

**Why:** More parallel sessions multiply an unproven workflow and burn its allowance.

**How to apply:** Pilot a worker end to end, freeze the working specification, pace each account, track landed yield and enforce a real dispatch brake.

Sources: [[owner_prompt_2026_10_07_04_06_agent]], [[owner_prompt_2026_10_07_04_03_agent]], [[owner_prompt_2026_10_07_04_10_agent]], [[owner_prompt_2026_10_07_04_09_agent]], [[a_hundred_workers_burned_both_windows_and_learned_little_2026_10_07]]

Drafted by Codex worker W18 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

