---
name: p0434_region_ratio_rises_in_w_below_the_tie_exactly_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 12:3x: route items 66-67, in T's region the rational rises strictly in w up to the tie (dR/dw = (eps-1)eps(p-1)H, H>0 exact Bernstein on a fitted box) and the region lies below the tie inside that box exactly; so T's region has R < R_tie everywhere"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T12:30:30-05:00
  status: provisional
  evidence: "brain repo 2ce7a489 and e0ab6aa5, w3int3/w3int5_agent.out"
---

P0434 route item 66 (an agent, 8 Nov 12:1x, brain repo commit 2ce7a489, route_agent_2026_11_08/).

Off the tie, in the region that holds T's maximiser, the region's rational R5 rises strictly in w up to the tie
point of its m. dR5/dw = (eps - 1) eps (p - 1) H / d5^2 with H of degrees (4, 6, 4, 6, 4) in (K, m, w, p, eps);
H > 0 by an exact Bernstein form on K in [2, 9/4], m - 1 in [0, 13/20], w in [0, 1/40], p in [0, 1/5], eps in [0, 1]
(16 s). The first box tried, w up to 1/2 and m - 1 up to 5/4, did not prove: fit the box to where the region can be
(the tie stretch has w <= 0.0201, m - 1 <= 0.61) before giving up on a Bernstein form.
With item 64 (R5 < R_tie on the tie, t in (0, 1)) and a(w0 + tU) rising in t, R5(m, w) < R5(m, w_t) < R_tie.
Sampled, not proved: the region lies below the tie and inside the box (1434 of 1434 region points out of 6000).

Lesson worth keeping: the derivative's numerator factored into eps^2-type linear pieces times one modest H, so a
5-variable claim cost a 6125-entry Bernstein form instead of a homogenised substitution. Factor before substituting.
Related: [[p0434_tie_region_ends_before_u_max_exactly_2026_11_08]], [[p0434_tie_region_ratio_below_tie_value_exactly_along_the_tie_2026_11_08]].

Item 67 (12:2x, commit e0ab6aa5): the containment is exact too, so the region holding T's maximiser is closed:
wherever the run takes its path, R < R_tie. Three decisions suffice: D2 = -F2 exactly (so m - 1 < k(1 - s)), D0 and D7
are the tie function g over a positive denominator (so w is below the tie), plus a(w0 + U) > k(1 - s) and
w0 + U < 1/40 on the (q, s) square. Mistake caught on the way: signing the other factors of a decision on a box that
the region is only later shown to lie in is circular; it was harmless here because the decisions used had no other
factors. Also: w3faceprove's Bernstein helper subdivides only four axes (range(4)); patch it for other dimensions.

