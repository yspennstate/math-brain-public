---
name: p0434_absolute_membership_tolerance_faked_a_corner_excess_2026_11_08
description: "P0434 8 Nov 13:2x: |R-soap|<=1e-9 passed at K-2=1e-11 on noise and showed RD 2.8x S2; use a relative test and climb q=(R-1)/(S2-1); RA/RB/RC/RD stay below S2 (q<=0.9995)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:24:17-05:00
  status: provisional
  evidence: "codex_fleet/runs/own_p0434/w3rdcorner_agent.out; w3norm_agent.out; commit 63beb3a4"
---

P0434, 8 Nov 13:2x, route item 70 (pushed 63beb3a4, route_agent_2026_11_08).

An absolute membership tolerance faked a counterexample. Region rationals were tested as "R holds here" by
|R - soap.ratio| <= 1e-9. A climb on R - S2(K) for the rational RD ended at K - 2 = 1.3e-11, where RD in exact
arithmetic is 2.3e-11 above S2 (q = (R-1)/(S2-1) = 2.79). The float ratio there was 1 to the last digit, so the
test passed only because both values sat within 4e-11 of 1. Scaling K - 2, m - 1, w, p up together (w3rdcorner)
kept RD at 2.8-3.5 times S2's excess while the float ratio stayed exactly 1 up to 1e-4: RD is not the ratio there.

How to apply: near a degenerate corner where every ratio tends to 1 (here K -> 2), test membership relative to
R - 1 (e.g. |R - soap| <= 1e-3 (R - 1)) and keep R - 1 well above float resolution. Climb a normalised excess
(q above) rather than a difference, because a difference climb runs into the corner where it means nothing.
All four w3bind difference climbs ended there.

Result under the fixed test (w3norm, K - 2 >= 1e-4, 8000 draws): climbed q is 0.9995 for RA, 0.9993 for RB,
0.9957 for RC and 0.459 for RD, so all four stay below S2. R5 reaches 1.0038 at K = 2.24, which is T's known excess.
RA, RB and RC approach S2 only as the middle atom vanishes (w -> 0 or m -> 1), which is the {1, K} limit. This is
sampled, not proved. Evidence: w3norm_agent.out, w3rdcorner_agent.out.


Related: [[p0434_region_rationals_miss_the_faces_2026_11_08]], [[p0434_three_atom_tie_beats_both_bounds_for_k_2_18_to_2_30_2026_11_08]], [[p0434_two_atom_finite_load_sup_is_s2_by_a_resultant_2026_11_08]].
