---
name: p0434_two_atom_tie_is_a_one_sided_peak_exactly_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 18:3x: route item 106 (bc160cdd): on {1,K} the ratio climbs into the tie (b > 0 exactly for all K in (2,9/4]) and is identically 1 past it, so the K-mass sup sits on the tie; item 104 exact at first order"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:40:41-05:00
  status: provisional
  evidence: ""
---

P0434 route item 106 (8 Nov 18:3x, pushed bc160cdd; w3ctieside_agent.py/.out in route_agent_2026_11_08).

On two atoms {1, K}, 2 < K <= 9/4, the tie p* = (K-2)/(K-1) is a one-sided peak, exactly.
- Below the tie, dR/dp at p* is item 101's b, and b > 0 at eps* for every K in (2, 9/4]. The numerator factor F(K, eps) has C^2 F(eps*) = P + Q sqrt B with P = -2(K-2)^2(K-1)^2(2K^4-9K^3+14K^2-4K-5) < 0, Q (degree 7) > 0, and P^2 - Q^2 B < 0, decided by exact real-root isolation. Values 0.373 at K 2.05 and 0.125 at 9/4; finite differences agree.
- Above the tie the soapsym branch formula is identically 1: once the K mass passes the tie, M-SERPT and Gittins make the same choices. soap.ratio gives exactly 1 at sample points, eps up to 0.8.

Consequence: a third atom of small mass m moves both branch formulas by O(m). So the slope in pk stays positive below the three-atom tie and the ratio stays 1 + O(m) < S2 above it, which puts the sup over the K mass on the tie at every K. That was the assumption behind item 104 (c(K, d) > 0), so item 104 is now exact at first order in m. Still local: branches with pk far from p* are not covered, and the O(m) constants are not bounded. Not the global bound (L+/T_G -> 2, Scully et al. lower bound 2).

Related: [[p0434_third_atom_slope_positive_for_every_k_and_d_exactly_2026_11_08]], [[p0434_s2_increasing_on_2_to_9_4_proved_exactly_2026_11_08]], [[p0434_third_atom_slope_formula_matches_direct_sup_on_a_k_grid_2026_11_08]].

