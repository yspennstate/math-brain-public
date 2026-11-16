---
name: p0434_s2_is_a_first_order_local_max_against_a_third_atom_2026_11_08
description: "P0434 8 Nov: for 2<K<=9/4 the two-atom sup S2 is a strict first-order local max against a small third atom anywhere in [1,K); the tie moves where E X = e(1), and two end resultants prove the slope negative"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:42:47-05:00
  status: provisional
  evidence: ""
---

P0434 (M-SERPT vs Gittins mean response ratio on laws in [1, K]). For 2 < K <= 9/4, S2(K), the two-atom sup, is a strict
first-order local max against a small third atom of mass w at any size m in [1, K). Route items 28-29, the private repository main
8c6ebec5, 06_math_research/frontier/P0434/route_agent_2026_11_08/ (w3sym, w3tie, w3T, w3Q, w3res).

- The three-atom branch ends where M-SERPT's age-0 value E X meets its age-1 value e(1) (checked with exact soap.ratio
  at 24 (K, m): R = 1 just past it), so the tie moves at dp*/dw = -(K - 1 - (m - 1)/(K - 1))/(K - 2).
- The first-order change of the sup is T = R_w + R_p dp*/dw = eps(eps - 1)(m - K) Q / (positive), with Q linear in m.
  Its sign is fixed by Q at m = 1 and m = K at eps = e2(K). The resultants of those two end quadratics with e2's defining
  quadratic vanish on [2, 9/4] only at K = 2, so both ends stay negative. T matches measured slopes at 12 points.
- The reusable moves: the moving boundary of the branch can be found in closed form from the policy's own rank values,
  and once a first-order coefficient is linear in one variable, two resultants at its ends do the whole sign proof.
  Q alone changes sign on the full eps box, so the bound has to be taken at the optimizer eps = e2, not uniformly.

Rests on: the SOAP mean formula; one branch rational (built at K = 2.2, m = 2.1) covering all m to first order, matched
numerically but not proved; the envelope step. Global three-atom optimality is still open.
Related: [[p0434_two_atom_finite_load_sup_is_s2_by_a_resultant_2026_11_08]],
[[p0434_prefix_lemmas_fail_because_mserpt_jumps_at_near_equal_sizes_2026_11_08]].


Update: route item 30 (a4b0324a) - the branch rational is identical at 7 more (K, m) samples; for K near 2 "small w" means w << (K - 2)^2 (at K = 2.01, w = 1e-4 the tie disappears).
Update: route item 31 (e9e7b3bf) - all 45 distinct branch decisions of the three-atom build keep their sign on 512 box points (K 2.02-2.25, m 1.01-K, eps 0.02-0.98).
Update: route item 32 (91619d5e) - the branch lemma is proved: with every decision recorded (586 order, 24 equality; item 31 had missed pos() and the cut sort), 40 of 47 differences are strictly signed at w -> 0, p = q by Bernstein certificates on the open cube for all eps in (0,1), and the other 7 are the tie polynomial N = (w+p)(1+A) - A over signed denominators, negative on the branch side. The first-order local max is now a proof for 2 < K < 9/4, conditional only on soapsym transcribing the SOAP mean formula (soap.ratio agrees to 1e-11). K = 9/4 itself not covered.
Update: route item 33 (be3fb5e9) - K = 9/4 closed: the certificate on K in (2, 2.3) gives the same 40 + 7, and item 30's end values at 9/4 are -0.640/-0.341, so the first-order local max holds for all 2 < K <= 9/4.
Update: route item 34 - finite masses scanned (14,700 three-atom laws a K at 5 K values): grid best below S2 by 1e-3 to 1.5e-2; polishing merges the third atom into K and stops at S2, never above. Scan, not proof.

Update 8 Nov 11:2xZ (item 35, commit 1a701946): moving the middle atom m is NOT monotone toward the ends. At fixed (K, w, p, eps) the ratio is continuous as m merges into 1 or K (2000 of 2000 end checks match the two-atom law to 1e-6), but 185 of 1000 scanned cases have an interior max in m above both ends (worst +1.24e-3 at K 2.25, w 0.1, p 0.02, eps 0.15). None reached S2. A finite-w proof must bound the bump by the margin S2 minus the larger two-atom end, not reduce pointwise.

Update 8 Nov 11:3xZ (item 36, commit 26a7dad9): 2400 grid points on {1, m, K} fall into 84 decision regions; 68 (2244 points) have ratio exactly 1 at every point (M-SERPT = Gittins), only 16 (156 points) exceed 1, all 1e-3 to 4.2e-2 below S2. A finite-mass computer proof = 68 identities + 16 rational bounds (grid-based census). Files: codex_fleet/runs/own_p0434/w3regions_agent.py/.out, route item 36.

Update 8 Nov 11:5xZ (item 37, commit 6c6ae4ab, w3ident_agent.py/.jsonl): all 68 tied regions of item 36 are exact identities. The symbolic run at each region's first grid point reproduced the region's decision sequence; M-SERPT minus Gittins mean response was 0 at 204 of 204 random rational points, and its expanded numerator was 0 in all 68. Negative control: 4 ratio-above-1 regions give a difference of about +0.27 at a rational point. What remains for finite masses: bound the 16 ratio-above-1 regions by S2, plus the grid caveat.

Update 8 Nov 12:0xZ (item 38, commit 27d4d687): a Nelder-Mead search kept inside each of the 16 above-1 regions got no closer to S2 than -4.0e-4. That point is at m = K = 2.139, nearly the two-atom law the resultant already bounds; next is the near-tie region at -9.3e-4. A local search, not a bound: S2*Gittins - M-SERPT still has to be signed on each region.

- Qualified 8 Nov 08:0x (route item 47, the private repository 49d03bbe): this holds on the branch followed here, but the joint limit w -> 0, m -> 1 on the demoted side of the M-SERPT tie beats S2 for every K in (K* = 2.175833, 9/4]; see [[p0434_tie_limit_closed_form_crossing_k_star_2_1758_2026_11_08]]. Not a strict local max over all three-atom perturbations there.
