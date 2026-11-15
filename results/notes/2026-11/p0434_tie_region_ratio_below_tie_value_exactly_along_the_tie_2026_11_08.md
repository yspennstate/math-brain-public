---
name: p0434_tie_region_ratio_below_tie_value_exactly_along_the_tie_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 11:3x: route item 64, the region holding T's maximiser: along the M-SERPT tie, with u = t U, (R - R_tie)/t has exact Bernstein sign -1 on the whole open box (q,s,eps,t), so R < R_tie for 0 < u < U, past first order"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:35:18-05:00
  status: provisional
  evidence: ""
---

Route item 64 (an agent, 8 Nov). Box coordinates K = 2 + q/4, p = s k/(1+k), k = q/4; tie point w0 = s k^2 (1-s)/((1+k)(1+sk)); U = w0 (1-p-w0)/(1+p(K-1)); w = w0 + t U, m = 1 + a(w). The region's rational R5 = A1/A2 and R_tie = B1/B2 after homogenising every substitution with common exponents in a sympy sparse ring over QQ (w3tunif3_agent.py): numerator A1 B2 - B1 A2 has 15032 terms, degrees (41,29,6,6), t-adic order 1; A2 and B2 negative on the box; numerator/t negative (one hard factor of degrees (22,18,4,5), Bernstein depth 14), 562 s in all. Sampling agreed beforehand: 24,000 points, none >= 0 (w3tunif). With item 63 this says the SOAP ratio lies below R_tie on the demoted side of the tie wherever the run takes the region's path and u < U. Open: whether the region's end can lie past u = U, interior points off the tie, the other 15 regions. Method lesson: sympy subs + together on these rationals took 2192 s for the pieces (w3tunif2 timed out); ring homogenisation took 51 s; sympify on a 15k-term printed string fails, use Poly.from_dict from ring terms. Files in 06_math_research/frontier/P0434/route_agent_2026_11_08. Status provisional: inside the SOAP model as coded (soapsym), not independently re-derived.
