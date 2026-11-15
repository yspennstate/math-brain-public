---
name: math_test_prompt_denied_tools_2026_11_12
description: "Math brain wins a benchmark while documents plus recall refuses to compute"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:44:32+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: Input line 81 (2026-10-05 12:00 [agent]) orders identical tool freedom. The verified hard1k audit found documents+recall 149, documents 168 and brain 246 on the first 300 problems. Of 122 UNKNOWNs in documents+recall, 93 cited tool limits; 21 of its 28 losses against documents cited that limit.

Why it happened: The prompt named one allowed recall command. The solver treated it as the only permitted command, so the comparison changed computational access as well as memory.

**Why:** Different tool instructions confound the claimed memory comparison.

**How to apply:** Use the same tools paragraph and prove real execution in every arm; inspect UNKNOWN reasons before interpreting scores.

[[one_named_command_made_the_solver_refuse_to_compute_2026_10_05]] [[the_brains_hard1k_lead_was_a_working_calculator_2026_10_05]]

Drafted by Codex worker W19 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

