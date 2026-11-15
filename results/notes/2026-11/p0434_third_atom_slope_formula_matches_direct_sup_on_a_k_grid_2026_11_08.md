---
name: p0434_third_atom_slope_formula_matches_direct_sup_on_a_k_grid_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 18:2x: route item 105 (90af7176): item 104's slope c(K,d) matches a direct float sup at 32 grid points K 2.01-2.25; best K mass always on the tie; error linear in m"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:40:25-05:00
  status: provisional
  evidence: ""
---

P0434 route item 105 (8 Nov 18:2x, pushed 90af7176; w3ctiegrid_agent.py/.out in route_agent_2026_11_08).

Item 104's closed-form third-atom slope c(K, d) checked against a direct float sup on a grid away from its three sample K: K 2.01, 2.03, 2.06, 2.1, 2.14, 2.18, 2.22, 2.25 by d 0.05, 0.3, 0.6, 0.9. Mass m at 1 + d(K-1), pk scanned across the three-atom tie (offsets up to 1e-2 relative both sides), eps = eps*.
- At all 32 points the best pk sits on the tie to the scan's resolution (1e-10 relative).
- c_num(m) converges to the formula with an error linear in m: gaps up to 1.1e-2 at m 1e-6 (K 2.01, where c is about 8300) and under 4e-5 for K >= 2.14. Richardson from m 1e-5 and 1e-6 leaves at most 2.9e-3.

So the two assumptions item 104 rests on (one soapsym branch over the K range; the sup over the K mass on the tie) hold on the grid. It is still numeric, not a proof of sup-on-the-tie for every K. The second-order term in m grows as K -> 2 (c itself grows like 1/(K-2)), so a finite-m check near K = 2 needs m well below K - 2.

Related: [[p0434_third_atom_slope_positive_for_every_k_and_d_exactly_2026_11_08]], [[p0434_k_end_slope_is_exactly_l_pred_and_the_gap_was_a_reference_offset_2026_11_08]].

