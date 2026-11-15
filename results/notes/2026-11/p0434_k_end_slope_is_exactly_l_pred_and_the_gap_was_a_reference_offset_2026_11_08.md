---
name: p0434_k_end_slope_is_exactly_l_pred_and_the_gap_was_a_reference_offset_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 17:4x: route item 102 (a9098f59): exact first-order tie slope gives L = L_pred (6.297 at 9/4), K-end slope > 0; item 95's 6.26 was a 1e-10 reference offset biasing c by 1e-10/m"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T17:52:13-05:00
  status: provisional
  evidence: ""
---

P0434 route item 102 (8 Nov 17:4x, pushed a9098f59; w3ctieslope_agent.py/.out in route_agent_2026_11_08).

A third atom at K - delta (delta = (1-d)(K-1), mass m) next to the two-atom maximiser: the sup over the K mass sits on the three-atom M-SERPT tie, pk = p* - m (d + (1-d)/p*) to first order (g/m = 5 at K 9/4, d -> 1). Along it the slope is exact first order, c(K, d) = -(dR3/dm + dR3/dpk dpk/dm)/(S2 - 1) at m = 0, eps*. It reproduces item 94 (c/(d(1-d)) 18.137 at (9/4, 0.5), 6.920 at (9/4, 0.95)). At d = 0.9999, c/(1-d) = 6.2977, 11.5692, 61.6657 at K 9/4, 2.2, 2.1, equal to L_pred = (K-1) S2'/(p*(S2-1)). So L = L_pred, and with item 101 (S2' > 0 exactly) the K-end slope is positive on (2, 9/4]. Open: the sup-on-the-tie step is a numeric scan, not a proof, and c > 0 for every d is still to be shown from the formula.

The least K-end value is 6.297 at K 9/4, not item 95's 6.26. That 0.6 per cent "g gap" in item 98 was a measurement bias. Item 95 normalised by S2 taken at p*(1 - 1e-10), which is b p* 1e-10 = 2.5e-12 below the tie value. That shifts c by -2.5e-12/((S2-1) m): -4.6e-5 at m 1e-6, -4.6e-6 at m 1e-5. Item 95's own two m columns differ by exactly that (0.006258 and 0.006299 against the exact 0.006303).

Scar: a slope per unit mass, normalised by a reference taken a hair inside a kink, carries a bias of order (offset)/m. Take the reference at the kink in closed form, or sweep m and check that the bias falls like 1/m.

Supersedes [[p0434_third_atom_slope_positive_least_6_26_at_k_nine_quarters_2026_11_08]] on the K-end value. Related: [[p0434_s2_increasing_on_2_to_9_4_proved_exactly_2026_11_08]], [[p0434_absolute_membership_tolerance_faked_a_corner_excess_2026_11_08]].

