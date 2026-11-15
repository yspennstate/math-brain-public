---
name: worker_reading_without_results_2026_11_12
description: "Brain workers consume tokens while rereading and produce almost no usable results"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:35:54+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 7 Oct the author challenged 34 workers reading about 110 tokens for every token written; some test builders read about 300k tokens per turn while writing almost nothing. The accompanying measurement card records 2.3B read for 20.8M written across those workers.

Why it happened: Large repeated contexts and weak output supervision let apparent activity substitute for accepted results. Brain delivery was also missing in some headless workers; its causal share was not established.

**Why:** A running worker and high usage do not prove improvement.

**How to apply:** Give the worker a concrete saved deliverable, inspect its first usable output and compare results on an existing test before extending its assignment.

Input evidence: L244, L242, L250, L299.

[[w17_owner_prompt_evidence_2026_11_12]] [[interactive_terminals_and_the_prompts_hook_burned_more_than_the_fleet_2026_10_07]] [[workers_connect_to_the_brain_through_the_stage_block_2026_10_07]]

Drafted by Codex worker W17 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

