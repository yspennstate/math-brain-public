---
name: p0434_third_atom_branch_past_m_c_stays_under_the_twin_family_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 21:1x: route item 110 (f981a9cf): third-atom sup past first order - b>0, every wide-grid sup < S2, tie window closes at m_c ~ p*^2(K-1)/(4(2-s)); the small-d second branch peaks 1.041 (9/4) / 0.990 (2.2) / 0.968 (2.1) of S2-1, under the twin T ratio 1.0606/1.0079/1.0 - consistent with sup = max(S2,T)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T21:13:51-05:00
  status: provisional
  evidence: ""
---

P0434 (M-SERPT against Gittins on [1, K], 2 < K <= 9/4), route item 110 (an agent, 8 Nov 2026 20:0x-21:1x), pushed in brain-repo f981a9cf under 06_math_research/frontier/P0434/route_agent_2026_11_08 (w3cm2, w3cm2wide, w3cm2probe, w3cm2close, w3cm2br2, each .py with its .out).

The third-atom sup past first order in m, with the atom at 1 + d(K - 1) of mass m and the K mass and load free:
- Small m: S2 - sup = a m + b m^2 with a = c(K, d)(S2 - 1) as in item 109, and b > 0 at every cell (K 2.05 to 9/4, d .05/.5/.95).
- Wide grid to m 0.03: every sup is below S2.
- The tie window closes at m_c ~ p*^2 (K - 1)/(4 (2 - s)), s = 1 + d(K - 1), the root of the discriminant of the downward quadratic f(pk). Past m_c the ratio is 1 exactly on that branch. A grid at 0.8 m_c and 1.25 m_c confirms both sides.
- A second branch at small d keeps R > 1 past m_c. Over d .005 to .3 and m 3e-3 to 0.1 (84 rows), the max of (sup - 1)/(S2 - 1) is 1.041 at 9/4 (d .005, m 1e-2), 0.990 at 2.2 and 0.968 at 2.1. It is at or below the near-twin T ratio of item 47 at every K (1.0606 / 1.0079 / 1.0). So the branch is that family seen at finite d, consistent with the conjecture sup R = max(S2, T).

The mistake to avoid: a value above S2 at K > K* = 2.17583 is not a counterexample. The test there is against T(K), not S2.

Numeric and grid-limited; no constant is bounded for the O(m^2) term.

Links: [[p0434_third_atom_local_result_written_as_one_note_2026_11_08]] [[p0434_third_atom_scan_at_five_d_and_c_is_a_relative_slope_2026_11_08]] [[p0434_tie_limit_closed_form_crossing_k_star_2_1758_2026_11_08]] [[p0434_three_atom_tie_beats_both_bounds_for_k_2_18_to_2_30_2026_11_08]]

