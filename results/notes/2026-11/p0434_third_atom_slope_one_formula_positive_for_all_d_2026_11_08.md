---
name: p0434_third_atom_slope_one_formula_positive_for_all_d_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 17:5x: route item 103 (7da3eb87): exact first-order tie slope c(K,d) is one branch over d in (0,1), numerator degree 2-3 with only root d=1, so c>0 on [0,1) at K 9/4, 2.2, 2.1; near-1 end (item 97) is the same tie"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:00:32-05:00
  status: provisional
  evidence: ""
---

Route item 103, w3ctied_agent.py/.out. Same tie as item 102 (pk = p* - m (d + (1-d)/p*)), with delta symbolic; formulas built at d0 0.1, 0.5, 0.95 agree exactly on a 999-point grid. c/(d(1-d)) least at the K end (6.309 at 9/4). c(K, 0+) = 11.82, 18.11, 73.2 at K 9/4, 2.2, 2.1 matches item 97's numeric 11.84, 18.14, 73.3, so the near-1 rank jump is the same tie mechanism (dpk/dm -> -1/p*), superseding item 100's reading that it needs its own formula. Open: K symbolic, and proving the sup over g sits on the tie. Related: [[p0434_k_end_slope_is_exactly_l_pred_and_the_gap_was_a_reference_offset_2026_11_08]], [[p0434_s2_increasing_on_2_to_9_4_proved_exactly_2026_11_08]].
