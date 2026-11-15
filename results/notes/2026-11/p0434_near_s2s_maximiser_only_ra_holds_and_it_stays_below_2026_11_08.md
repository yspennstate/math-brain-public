---
name: p0434_near_s2s_maximiser_only_ra_holds_and_it_stays_below_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 14:4x: route items 78-80, near S2's maximiser only RA is the ratio, its edge is decision 0 on a 4x4 (K, m) grid, above p* the ratio is 1, and the edge excess carries K-m with a negative w-slope"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T14:43:17-05:00
  status: provisional
  evidence: ""
---

Route items 78-80 (an agent; files under 06_math_research/frontier/P0434/route_agent_2026_11_08). Follows [[p0434_ra_edge_excess_negative_for_all_k_and_m_2026_11_08]]. (78) At eps*, w = 1e-4, laws at p* + w dp/dw -/+ d: the lower one is an RA member, the upper one is not, and decision 0 is the first flip at all 16 grid points, K = 2.03..2.25, m at 0.05..0.9 of (1,K). (79) A scan down to 0.6 p* never finds RC as the ratio; RA's bisected edge matches the predicted slope (for example -1.400 against -1.400 at K = 2.25, m 0.9). From p* up to 1.5 p* the SOAP ratio is exactly 1, even though the formula B keeps rising past p*: p* ends B's band. (80) On m = K, G = s((K-2) - s(K-1)) with s = p + w, so that face's edge is s = p* exactly and the whole edge excess vanishes there. Ex/((K-m)/(K-1))/w tends to -7.38, -1.100, -0.3448 at K = 2.05, 2.15, 2.25, so it is bounded away from 0. Local conclusion: for small w, three-atom laws near (p*, eps*) stay strictly under S2. Open: RB's m -> 1 limit, laws far from the maximiser, five or more atoms. Scar from the same round: a membership tally used 'is True' on a numpy bool and reported 0 of 16 ok while every row was right; wrap numpy comparisons in bool() before identity tests. Links: [[p0434_two_atom_finite_load_sup_is_s2_by_a_resultant_2026_11_08]] [[p0434_s2_is_a_first_order_local_max_against_a_third_atom_2026_11_08]]
