---
name: p0434_rb_m_to_1_limit_stays_below_s2_at_first_order_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 14:5x: route items 81-83, RB equals B at m = 1 for every w and rises in m, but its edge (decision 1, linear) pulls back from p*; the first-order excess is negative for all K, w at eps* by resultants"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T14:55:04-05:00
  status: provisional
  evidence: ""
---

Route items 81-83 (an agent; files under 06_math_research/frontier/P0434/route_agent_2026_11_08). RB(m = 1) == B identically, free of w, so it carries S2 at (p*, eps*) for every w; dRB/dm > 0 there (+1.7e-3 to +2.8e-2). RB's region edge near p* is decision 1, G = (K-1)(1-p) - m(1+w) + w, free of eps and linear, so dp/dm = -(1+w)/(K-1) at (m = 1, p*) (-0.87826 predicted against -0.8783 bisected). The first-order edge excess E_B = L_B + B_p dp/dm = -eps(eps-1)P_B/(positive), with P_B linear in w. Both w-ends at eps* are negative on all of (2, 9/4]: the resultants against eps*'s quadratic have no root there except K = 2, and the w = 1/(K-1) end is K(K-1) times RA's face polynomial from item 76. Max E_B at eps* on a 300x300 (K, w) grid is -0.077. Decision 1 is the edge at all 16 (K, w) grid points, and above p* the ratio is exactly 1. With [[p0434_ra_edge_excess_negative_for_all_k_and_m_2026_11_08]] and [[p0434_near_s2s_maximiser_only_ra_holds_and_it_stays_below_2026_11_08]], both two-atom limits (w -> 0 via RA, m -> 1 via RB) stay under S2 at first order at the maximiser. Open: eps below about 0.09, laws away from the limits, five or more atoms. How to apply: the same edge-plus-slope factoring closed both limits; reach for it whenever a rational meets a smaller law's maximum on a region boundary.
