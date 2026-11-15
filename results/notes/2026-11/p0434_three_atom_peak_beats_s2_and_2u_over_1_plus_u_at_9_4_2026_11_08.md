---
name: p0434_three_atom_peak_beats_s2_and_2u_over_1_plus_u_at_9_4_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: on {1, 1+3/40000, 9/4} the exact soap-model ratio is 1.05805 > max(S2 1.05475, 2u/(1+u) 1.05573), so the conjecture sup = max(S2, 2u/(1+u)) fails near K = 9/4; peak at m-1 ~ 1e-4, missed by grids"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:25:22-05:00
  status: provisional
  evidence: "codex_fleet/runs/own_p0434/w3exact_agent.out, w3spike_agent.out; commit 62dec1c1"
---

On {1, m, K} with m just above 1, the M-SERPT/Gittins mean-response ratio (soap model) has a narrow peak that beats both
S2(K), the two-atom sup, and the near-equal-sizes lower bound 2u/(1+u), u = sqrt(K - 1), once K is near 9/4. Exact
rational at K = 9/4, m = 1 + 3/40000, w = 13/1250 (mass at m), p = 69/1000 (mass at K), eps = 511/5000:
1.0580536938, against S2 = 1.0547504406 and 2u/(1+u) = 1.0557280900, so the conjecture sup = max(S2, 2u/(1+u)) fails at
9/4 by 2.3e-3. Polished gaps to S2 by K: -4.5e-5 (2.05), -5.8e-5 (2.1), -1.3e-4 (2.15), +3.3e-4 (2.2), +3.3e-3 (2.25).
The peak lives at m - 1 between about 3e-5 and 2e-2 and vanishes as m -> 1 (end continuity holds), which is why every
grid with m - 1 >= 0.05 (K - 1) missed it.

How it was found: the search had stalled. Nelder-Mead kept inside a decision region never moved, because its first
simplex left the region. SLSQP with the region's decisions written as inequalities walked region 12 to m = 1.
Lesson: an in-region search that ends exactly at its start point has measured nothing. Check that it moved.

Caveat: soap.py and soapsym are both our code. Not yet done: an event simulation, or a hand evaluation of the SOAP class
formulas at this point. Route items 40-42 in route_agent.md, commit 62dec1c1. Related: [[p0434_mserpt_lower_bound_2u_over_1_plus_u_passed_a_second_audit_2026_11_08]], [[p0434_prefix_lemmas_fail_because_mserpt_jumps_at_near_equal_sizes_2026_11_08]], [[p0434_s2_is_a_first_order_local_max_against_a_third_atom_2026_11_08]].


Update 8 Nov 12:4xZ (item 43, commit 3f0710e1): an event simulation sharing no code with soap.py confirms it. At the 9/4 law it gives 1.05740 +- 0.00055 (1e6 jobs; model 1.05805), 3 standard errors above max(S2, 2u/(1+u)) = 1.05573. It also reproduces the model's sharp switch at w=0.01046, p=0.07, eps=0.10422: 1.03017 at m-1=1e-6 (model 1.03013) and 1.05693 at 1e-3 (model 1.05789). The switch is the M-SERPT tie between the age-0 and age-1 ranks: when the age-1 rank is higher, jobs that outlive age 1 are demoted behind new arrivals.


Update 8 Nov 07:5x (route items 44-46, commit 31070528): the peak is a limit on the M-SERPT tie r(1) = r(0) with m -> 1, approached from the demoted side (1.058072 at +1e-9 against 1.029785 at -1e-9). With p fixed by the tie and (w, eps) free, the tie-limit sup beats max(S2, 2u/(1+u)) for K > 2.2005 (bisected to [2.200498, 2.200508]; gap +2.7e-3 at 2.245, +2.6e-4 at 2.205, -3.9e-5 at 2.2, -3.2e-3 at 2.15). Lower bound on the three-atom sup, not the sup. A multi-start search per K (item 44) missed this peak at 2.225, so do not trust per-K random starts on this problem; follow the tie surface.

- Update 8 Nov 08:0x (route item 47, 49d03bbe): item 46 took the smallest-p tie root only; the closed form moves the crossing down from 2.2005 to K* = 2.175833 (degree-12 resultant). [[p0434_tie_limit_closed_form_crossing_k_star_2_1758_2026_11_08]]
