---
name: p0452_referee_found_proof_scope_gap_2026_11_12
description: "P0452 iid budget citation used for deterministic arrays and order-dependent chain state"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:08:21+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The outside referee returned GAP despite D=3 simulation 0.885 versus 0.8856. Four repairs covered ordered state, an uncovered deterministic-array case, fixed-point selection and the continuous common cost law; the new array lemma passed 6000 small-instance checks.

Why it happened: Self-review let a cited iid limit theorem cover a broader statement, represented order-dependent arrivals as a set, forgot constant one is a fixed point and omitted a law hypothesis.

**Why:** Agreement with simulations cannot repair missing hypotheses or an insufficient state space.

**How to apply:** Check every statement case against the cited theorem, preserve ordered arrivals, identify the sub-one fixed point by its bound, and state the common continuous law.

[[p0452_p0243_independent_referee_passes_what_they_found_2026_11_12]]

Drafted by Codex worker W04 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

