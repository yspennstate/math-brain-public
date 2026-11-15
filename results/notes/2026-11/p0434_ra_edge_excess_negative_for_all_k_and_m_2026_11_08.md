---
name: p0434_ra_edge_excess_negative_for_all_k_and_m_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 14:3x: route items 75-77, at S2's maximiser RA's first-order excess along its edge decision is negative for every K in (2,9/4] and m in (1,K), by an exact factoring plus two resultants"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T14:33:38-05:00
  status: provisional
  evidence: ""
---

Route items 75-77 (an agent; files under 06_math_research/frontier/P0434/route_agent_2026_11_08, pushed 43da02ad and 4e8a66dd). RA's region edge near p* = (K-2)/(K-1) is decision 0 of the run, numerator G free of eps and zero at p* when w = 0; dp/dw = -(K+m-2)/(K-1) + (m-2)/(K-2). The first-order excess on the edge, E = L_A + B_p dp/dw at p*, factors exactly as eps(eps-1)(m-K)P(K,m,eps) over a positive denominator, so sign E = sign P, and P is linear in m. At eps*(K) both ends P(m=1), P(m=K) are negative on all of (2, 9/4]: the resultants against eps*'s quadratic have no real root there except K = 2, and the values at K = 2.1 are -0.284 and -0.239. Near K = 2 both are -sqrt((K-2)/2). E = 0 on the face m = K, where RA is the two-atom ratio B(w+p) (symbolic). Caveats: decision 0 was read as the edge at one test point only; this is first order in w at eps*; the eps window below 0.093 has E > 0 but B is at least 28 pct of the room under S2. How to apply: when a positive first-order slope meets a moving region edge, add the edge's pull-back, factor the combined slope, and settle the remaining one-variable sign with a resultant rather than a grid. Links: [[p0434_s2_is_a_first_order_local_max_against_a_third_atom_2026_11_08]] [[p0434_two_atom_finite_load_sup_is_s2_by_a_resultant_2026_11_08]] [[p0434_absolute_membership_tolerance_faked_a_corner_excess_2026_11_08]]
