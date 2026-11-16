---
name: t254_collapse_rate_identity_2026_11_01
description: [PROVISIONAL] T254: attention rank-collapse rate on exchangeable Gram is exactly 1 - p0 + r v (two O(1/T) terms that nearly cancel), so l2/l1 -> e^-tau as tokens grow
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T00:19:53+04:00
  status: provisional
  evidence: ""
---



T254 (1 Nov, an agent), pushed 7bbeb15 to research-repo (research_pushes/2026-11-01-loop-T254-kappa-identity), card claim_03213419338c4df4998c23eac6d7ef46, move 2749a27c.

kappa = 1 - p0 + r v, where p0 = (1/2)E|A_1 - A_2|^2 and v is the column-sum variance. Two exact facts make it work: rows of the softmax sum to 1, and the sum of squared column sums is 1^T A A^T 1. Lower bound kappa >= 1 - e^(2 sigma^2)/T, by Jensen. It matched agent's measured kappa(c) to 3e-4.

Trap: my first "direct drift" check used E[AA^T] where it needed E[AGA^T] and gave 1.4-1.6. Fixed in the note and stated once. Also, a refused shell command silently dropped a cp, so a referenced file was missing from the first push. Re-pushed with landed.json kept.

Related: [[t252_hessian_bulk_is_plugin_mp_law_2026_11_01]] (also softmax second moments).
