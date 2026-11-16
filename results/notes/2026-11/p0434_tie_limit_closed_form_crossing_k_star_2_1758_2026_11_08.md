---
name: p0434_tie_limit_closed_form_crossing_k_star_2_1758_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 08:0x: on {1, 1+, K} at the M-SERPT tie the ratio is one degree-10 rational R(K,p,eps); it beats S2 exactly for K > K* = 2.175833 (root of a degree-12 P12), not 2.2005"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T08:07:41-05:00
  status: provisional
  evidence: ""
---

P0434 (M-SERPT vs Gittins). Route item 47, the private repository main 49d03bbe, 06_math_research/frontier/P0434/route_agent_2026_11_08/w3tiecf_agent.py/.out/_R.txt.

- On the tie r(1) = r(0) with m -> 1, the tie p(K-1)(1-w-p) = w+p is LINEAR in w: w = p((K-1)(1-p)-1)/(1+p(K-1)). Parametrising by p instead of solving for p removed a two-root ambiguity.
- soapsym at five tie points (K 2.18 to 9/4) gives one rational; at m=1 and w=w(K,p) it is R_tie(K,p,eps), degree 10 over 10. Matches soap.ratio to 1e-9 at those points and at every new maximiser.
- Measured gap of the sup to S2: +3.32e-3 at 9/4, +1.27e-3 at 2.22, +4.07e-4 at 2.2, +1.35e-5 at 2.18, 0 (1e-14) at 2.175 and below.
- S2's own maximiser lies ON the tie (w=0 gives p0=(K-2)/(K-1); at K=2.16 the sup sits at p=0.137931=p0). The crossing is where leaving w=0 pays: resultant 4(K-2)^6(K-1)^12(K^2-K-1)P12(K), P12 = K^12-15K^11+106K^10-467K^9+1397K^8-2854K^7+3780K^6-2758K^5+317K^4+1115K^3-782K^2+181K-25, root K* = 2.175833294892. Bisection on soap.ratio gave 2.17585 (the 1e-9 tie offset swamps a quadratic gap near K*).
- Scar: item 46 (w3tielim) solved the tie for the smallest p root only and reported crossing 2.2005; its sups below 2.24 were too low. When a constraint is linear in another variable, parametrise by that one.
- Still a lower bound on the three-atom sup; other near-tie families and more atoms are open. Qualifies [[p0434_s2_is_a_first_order_local_max_against_a_third_atom_2026_11_08]]; extends [[p0434_three_atom_peak_beats_s2_and_2u_over_1_plus_u_at_9_4_2026_11_08]].

- 8 Nov 08:11 (route item 48, 6b705414): the age-m M-SERPT tie K - m = max(E S, E[S-1|S>1]) with m interior stays near 1.044 on the grid; polished points collapse to m -> 1 and give S2 itself. Item 47 is still the only family seen beating S2.

Update 8 Nov 08:2x (route item 49, commit cf12b4b6): seven Gittins-side tie families on {1, m, K} (inside the age-0 and age-1 index mins, and rank(1)/rank(m) against rank(0)/rank(1)) never beat S2 (largest gap -2.5e-11; polished points all run to a two-atom edge). With items 48 and 49, the M-SERPT tie r(1) = r(0), m -> 1 is the only three-atom family seen to beat S2. Local search, not a bound.
Update 8 Nov 08:2x (route item 50, commit 1ae052c8): a fourth atom m2 with mass u, held on the same tie, never lifts the sup at K = 9/4 or 2.2 (loss linear in m2 - 1 and u; Nelder-Mead from three starts merges m2 into 1 or K or sends u -> 0, back to item 47's value to 1e-10). Local max among four-atom laws on its tie; far-away four-atom laws and double ties untested.
Update 8 Nov 08:2x (route item 51, commit 55ad7b90): four atoms on two M-SERPT ties at once (item 47's plus K - m2 = r(0)) peak at 1.057929 at 9/4, 1.44e-4 below item 47; the second tie forces p down. Item 47 remains the best law found on three or four atoms (local searches).
Update 8 Nov 08:3x (route item 52, commit 8d30da11): 4000 random four-atom laws per K (9/4, 2.2), unseeded, none above item 47; polished bests 1.0579964 at 9/4 (-7.6e-5) and every good draw is item 47's {1, 1+, K} shape with the near atom split. Item 47 is the conjectured sup on (K*, 9/4] for three and four atoms; unproved.

Update 8 Nov 08:4x (route item 53, commit a71d16d5): corrected conjecture written up as conjecture_agent.md in the route folder. sup R = T(K) := max R_tie on 2 < K <= 9/4 (S2 up to K*, tie face beyond); 2u/(1+u) overtakes S2 only at K = 2.2431743, where T is 2.8e-3 higher, so it is never the max there. Table on 20 K in w3table_agent.out. Unproved; next independent check is a simulation at K = 2.2 on T's maximiser (gap 4e-4, needs about 1e7 jobs).

Update 8 Nov 08:5x (route item 54, commit cc832523): inside the tie region, sampled at K = 2.18/2.2/2.25 (144 lines each way), the max over w at m = 1+ is always at an endpoint (w = 0 or the tie), with a 0.01-0.05 drop just off w = 0 and then a near-linear rise; along the tie the max over m is always at m -> 1. Supports sup = max(S2, T). Next: check symbolically that at m = 1 the region rational is affine over affine in w (which would make the w step automatic).

Update 8 Nov 08:5x (route item 55): at m = 1+ the tie region's ratio is affine over affine in w (fit residual 1.9e-15 on 72 lines, strictly rising), so the sup over the open demoted line is at the tie. Owed: the Mobius determinant's sign in closed form, and the m -> 1 step (sampled only).

Update 8 Nov 09:0x (route item 56): PROVED on the m = 1 face of the tie region: R = (N0 + N1 w)/D0 is affine in w and dR/dw > 0 for all 2 < K <= 9/4, 0 < p < (K-2)/(K-1), 0 < eps < 1 (det factors; Q's eps-coefficients c0, c2 < 0 always, c1 <= -3/4 because p <= 1/5). Assumes the region's decision sequence holds on the whole line (checked at 192 points). Still owed: the m -> 1 step along the tie.

Update 8 Nov 09:1x (route items 57-58, commit dbb78438): the m -> 1 step along the tie is proved at first order. The tie curve is m(w) = 1 + a(w), rational in w; d R/dm along it at m = 1 has the sign of F16(K, p, eps), and with K = 2 + q/4, p = s k/(1+k) the tensor Bernstein form on [0,1]^3 (495 exact coefficients) has no positive entry, so F16 < 0. The region's rational matches soap.ratio to m - 1 = 0.01 on 64 lines (signature changes at once but the value does not: compare values, not signatures). Still assumed: the region's rational holds near m = 1 on the whole range (sampled).

Update 8 Nov 09:25 (route items 59-62, commits 376465e3, 1230838e): on the m = 1+ face (0 < w < w_tie) the region's rational is the exact SOAP ratio everywhere, proved: 49 non-constant decisions signed by exact Bernstein forms, identically zero comparisons re-decided exactly (5 path changes, same rational), and 7 tolerance tests shown never to merge. So item 56's w step is a full proof. Still sampled: the region along the tie for m - 1 > 0. Lesson: float rounding decided 6 exact ties the wrong way in soapsym without changing the formula.
- 8 Nov 09:4x update (route item 63, commit 707814c5): along the tie near m = 1 the same 49 decisions keep their sign as m - 1 -> 0+ on the whole open range (exact Bernstein in box coordinates q, s, eps; 2 decisions vanish on the tie and were signed after dividing by the tie function g > 0); 7 tolerance tests never merge. So the region's rational is the SOAP ratio on the demoted side of the tie for 0 < m - 1 < delta(K, p, eps), and item 58's dR/dm < 0 is about the true ratio. Not uniform in delta; beyond first order along the tie and off-tie interior points still sampled only.
