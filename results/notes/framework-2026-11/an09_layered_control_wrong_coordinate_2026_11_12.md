---
name: an09_layered_control_wrong_coordinate_2026_11_12
description: "AN09 layered search positive control returns zero instead of twelve"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:33:50+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 12 Nov the first positive control returned 0 because the layered search used the wrong coordinate. The corrected controls reached 12; both main finite searches reached a maximum of 10 where 12 were required.

Why it happened: The control set E is a graph over its second coordinate, but the first control used another layering. The main searches had their own precondition checked: no zero of the form (0,v,0).

**Why:** A failing positive control can violate the control algorithm precondition and does not by itself refute the target claim.

**How to apply:** Check the coordinate and graph precondition of each control, then rerun it; keep the unchecked R^2 transfer separate from the finite verdict.

[[an09_fuglede_dim2_finite_sets_in_z60xz12_check_out_2026_11_12]]

Drafted by Codex worker W08 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

