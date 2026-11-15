---
name: dg06_large_circle_false_refutation_2026_11_12
description: "Testing the local index of H_k on circles too large for its asymptotics"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:16:34+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 12 Nov 2026 the first k=1 run at radius 0.35 returned index 0.5 and looked like a refutation of the local index 1.5. Radius 0.11 returned 2.5. Small-circle checks by two routes later gave the expected indices 1.5, 2, 2.5 and 3 for k=1..4.

Why it happened: The leading Hessian term dominates only deep in the asymptotic regime (roughly |z|^(-k/2) about 50 for k=1). Larger circles can enclose other singularities.

**Why:** A local index is a limiting statement, so an arbitrary enclosing circle tests a different region.
**How to apply:** Shrink radii, state sampling density and verify convergence by two routes before calling a local-index construction false.

[[dg06_caratheodory_smooth_counterexample_checked_2026_11_12]]

Drafted by Codex worker W06 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

