---
name: p0434_small_d_branch_tends_to_the_twin_ratio_from_below_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 21:2x: route item 111 (43ee4010): as d -> 0 the small-d third-atom branch climbs to 1.0599 (9/4) and 1.0068 (2.2) of S2-1, linear in d, limits ~1.0603/1.0071 under the T ratios 1.0606/1.0079; no row passes max(S2,T)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T21:30:10-05:00
  status: provisional
  evidence: ""
---

P0434 (M-SERPT against Gittins on [1, K], 2 < K <= 9/4), route item 111 (an agent, 8 Nov 2026 21:1x-21:2x), pushed in the private repository 43ee4010 under 06_math_research/frontier/P0434/route_agent_2026_11_08 (w3cm2tw_agent.py/.out).

The small-d branch of item 110 (a third atom at 1 + d(K - 1), mass m, past m_c) pushed to d 1e-3 / 3e-4 / 1e-4 at K 9/4 and 2.2:
- (sup - 1)/(S2 - 1) climbs toward the near-twin T ratio and stays below it: 1.05643 / 1.05912 / 1.05989 at 9/4 (m 1e-2), T ratio 1.0606; 1.00405 / 1.00620 / 1.00682 at 2.2 (m 5e-3), T ratio 1.0079.
- The steps are linear in d (slope 3.9 at 9/4, 3.07 at 2.2), so the d = 0 limits on this m grid are about 1.0603 and 1.0071. The rest of the gap is the coarse m grid: at d = 0 the middle atom is a twin of 1 and the sup is item 47's family, whose sup is T.
- No row passes T. Every three-atom sup scanned is at or below max(S2, T), the conjecture.

Numeric, five-value m grid; the limit 1.0606 itself is not resolved.

Links: [[p0434_third_atom_branch_past_m_c_stays_under_the_twin_family_2026_11_08]] [[p0434_tie_limit_closed_form_crossing_k_star_2_1758_2026_11_08]] [[p0434_three_atom_tie_beats_both_bounds_for_k_2_18_to_2_30_2026_11_08]]


Item 112 (db310626): fine m at K 9/4, d 1e-4, m 6e-3..1.3e-2 - the branch peaks at m ~1e-2 (1.0599) and ends between 1.1e-2 and 1.2e-2 (near m_c), so the coarse m grid was not hiding a higher value; d = 0 estimate ~1.0603 < 1.0606.

Item 113 (8 Nov 21:4x, da45b202): at d 1e-5 and 1e-6, m 9.5e-3 to 1.15e-2, the best row is m 1.05e-2 with 1.060675 at d 1e-6 (K mass 0.0707, eps 0.1053). The T ratio itself is 1.0606827 (1.058072846 over S2 1.054750441; the 1.0606 in 110-112 was rounded), reached at w 0.01046, K mass 0.0700, eps 0.1042. So the branch's maximiser lands on the twin maximiser in all four coordinates, 8e-6 under T. Item 112's d = 0 estimate of 1.0603 was low because its m grid missed 1.05e-2. A break test at m = w (item 114) is running.

Item 114 (8 Nov 21:5x, 19c14c1b), the break test: d 1e-6, m = w 0.01046 gives 1.0606790 at K mass 0.0700, eps 0.1042 (item 47's maximiser), 3.7e-6 under T = 1.0606827; m 1.02e-2 and 1.07e-2 are lower. No row passes T. The gap is d times the slope of about 3.7, so the open step is to prove that the first-order term in d at the twin tie is negative.

Item 115 (8 Nov 22:0x): at item 47's twin maximiser, (sup - T)/d is -0.2032 at K 9/4 and -0.1654 at 2.2, constant for d 1e-7 to 1e-4 (-3.71 and -3.22 in units of S2 - 1). The first-order term in d is negative, numerically. The maximiser sits on the tie boundary, so fixed-point and re-optimised slopes differ (-0.2328 against -0.2032). Proof of the sign from the closed form is open.

Item 116 (8 Nov 22:1x, 04f3f478): the d-slope at the twin maximiser is negative at seven K across (K*, 9/4]: -0.150 / -0.158 / -0.165 / -0.173 / -0.187 / -0.195 / -0.203 at K 2.18 / 2.19 / 2.2 / 2.21 / 2.23 / 2.24 / 2.25, equal at d 1e-6 and 1e-5, and about -0.15 as K -> K* while w -> 0. T matches w3tielim. The sign is numerical; no analytic proof yet.

Item 117 (8 Nov 22:4x, the private repository 7afcf357, w4tw_agent): a fourth atom at t in [1.01, 2.245], mass q 1e-4/1e-3/1e-2, on item 47's twin maximiser at K 9/4 (d 1e-6), re-optimised: all 33 rows below T 1.0606827 (top 1.0606610 at t 2.245, q 1e-4). Loss in R per unit q at q 1e-4 is about 2.0-2.4 (K - t), 2.82 at t 1.01 down to 0.012 at 2.245. T is a first-order local max against a fourth atom on this grid; three nearby starts per row, K 9/4 only.

Items 117-118b (8 Nov 22:2x-23:4x): against a fourth atom at t in (1,K), mass q, T stays a first-order local max at K 9/4 (33 rows, max 1.0606610 vs T 1.0606827) and at K 2.2 (two independent searches, 33 rows: max 1.0078501 vs T 1.0079243). Loss per unit q is about 2.2 (K - t) at 9/4 and 1.1-1.3 (K - t) at 2.2. Pushed to the P0434 route folder, commits 47f4bca1..b918dd34. Numeric only; analytic sign open.

Item 119 (9 Nov 00:0x, commits e628caae..0cc8b5c6): a HEAVY fourth atom (q 0.05/0.2/0.5, t 1.05..2.18) at K 2.2 tops out at 0.9765 vs T 1.0079243. Ten of 15 rows are exactly 1 in ratio: on every grid cell checked (1200-1800 each) M-SERPT and Gittins agree to 12 places, and at t 1.3 the excess drops from 0.646 at q 1e-2 to exactly 0 by q 2e-2. A few percent of mass on a middle atom switches the twin effect off. Grid-limited, not a proof.
