---
name: p0434_s2_increasing_on_2_to_9_4_proved_exactly_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 17:2x: route item 101 (3916b95e) proves S2(K) increasing on (2,9/4] from item 22's closed form; S2'>0 iff P+Q sqrt B<0, decided by exact root isolation"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T17:36:29-05:00
  status: provisional
  evidence: ""
---

P0434 (M-SERPT against Gittins), route item 101, 8 Nov 17:2x, pushed 3916b95e (route_agent_2026_11_08, w3cpartsym_agent.py/.out).

The two-atom value S2(K) on {1, K} is strictly increasing on (2, 9/4], now by exact algebra rather than item 99's 2000-point float grid. From item 22's closed form R(p, eps) at the tie p* = (K-2)/(K-1), S2' = dRt/dK at eps* (envelope). Its numerator is eps (eps-1) M(K, eps) over a square, so S2' > 0 iff M(K, eps*) < 0. With eps* = (A + sqrt B)/C, C^2 M = P + Q sqrt B:
- P = 2 (K-2)^2 (K-1)^3 (4K^3 - 15K^2 + 21K - 11), positive on (2, 9/4]
- Q = (K-1)^2 (K^5 - 7K^4 + 18K^3 - 19K^2 + K + 8), negative there (no real root in [2, 9/4])
- P^2 - Q^2 B (degree 20) has only the root K = 2 and is negative inside.
Exact real-root isolation in sympy decides all three.

Item 100's partials have closed forms too: a = dR/dK|p is negative and b = dR/dp|K positive at the tie, a + b/(K-1)^2 = dRt/dK identically, values match the finite differences to 6 digits. The whole slope comes from the tie letting mass into the large class.

Caveats: holds on the branch just below the tie (item 22's setting) with eps* the maximiser there. M(K, 0) = (K-2)^2 (K^2-2K+2) > 0, so the sign depends on eps* sitting high enough, not on K alone. The K-end third-atom slope (item 98) is positive up to its measured g re-weighting gap, which is still unbounded; the near-1 end (item 97) is a separate rank-jump effect.

Related: [[p0434_third_atom_slope_positive_least_6_26_at_k_nine_quarters_2026_11_08]], [[p0434_two_atom_finite_load_sup_is_s2_by_a_resultant_2026_11_08]], [[p0434_s2_is_a_first_order_local_max_against_a_third_atom_2026_11_08]].

