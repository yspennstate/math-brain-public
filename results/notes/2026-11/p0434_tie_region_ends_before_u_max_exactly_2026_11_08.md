---
name: p0434_tie_region_ends_before_u_max_exactly_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 11:5x: route item 65, the tie region's path ends before u = U at every (K,p,eps): decision D2 = c*F2, F2=(m-1)(1+w)-((K-1)(1-p)-1) goes - to + on [0,U], exact Bernstein; with item 64 the region stays below R_tie on its whole tie stretch"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:52:36-05:00
  status: provisional
  evidence: "brain repo e5c35f35, w3uexact_agent.out"
---

P0434 route item 65 (an agent, 8 Nov 11:5x, commit e5c35f35 in the brain repo, route_agent_2026_11_08/).

Along the M-SERPT tie of the region that holds T's maximiser, the run's decision path ends before u = U, at every
(K, p, eps) of 2 < K <= 9/4. The end is where F2 = (m - 1)(1 + w) - ((K - 1)(1 - p) - 1) changes sign; decision D2 of
the item 63 census is a constant times F2. In box coordinates F2 = -(q/4)(1 - s) at t = 0 and F2 at t = 1 is four
factors in (q, s), each with a positive Bernstein form, so by continuity F2 vanishes at some t* in (0, 1).
Combined with item 64 (region rational < R_tie for all 0 < u < U), the region's rational is below R_tie on the whole
tie stretch where the run takes this path.

Measurement: 1000-point walk, end t 6e-5 to 0.40; 200-point factor scan, F2 among the factors changing sign at 189 of
the 195 points in the eight largest groups; float audit t* 2e-4 to 0.30. At 9 of 200 points the closed form still
matched soap.ratio just past t* (another path, same rational), so the ratio past t* belongs to the next region.

How it was found: when about 30 decisions flip at the same t, factor them and look for the shared factor; one
decision was the factor itself, which made the exact step a two-variable Bernstein check (9 s) instead of a
four-variable one. Related: [[p0434_tie_region_ratio_below_tie_value_exactly_along_the_tie_2026_11_08]].
Still open: interior points off the tie, the other 15 regions.

