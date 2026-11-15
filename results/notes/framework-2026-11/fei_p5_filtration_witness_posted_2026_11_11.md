---
name: fei_p5_filtration_witness_posted_2026_11_11
description: "[PROVISIONAL] FEI P5 'A filtration bound for the erasure entropies' posted? Yes, github.com/yspennstate/fei-filtration-witness (11 Nov): witness L^pi_i, two-sequence lemma, resampling condition, private AND, bent point shows the coordinate matters"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T00:49:32+02:00
  status: provisional
  evidence: ""
---

FEI paper 5, "A filtration bound for the erasure entropies of Boolean functions", is public at
github.com/yspennstate/fei-filtration-witness (commit f64dad5, 11 Nov 00:4x). Brain copy:
06_math_research/fei_papers_agent/p5 (main.tex, code/check_witness.py, code/bent_point.py). P1-P4 READMEs link it
(d85763b, 2c626b2, 33aa1ef, 211d8cf). Refereed by an agent with independent code
(fei_solve_2026_11_09/referee_p5_51f2.md): maths correct, 13,720 coordinate-order pairs reproduced.

What it proves (g = E_i f, h = D_i f, U ~ fhat^2, delta = Inf_i):
- Witness L^pi_i = H(1[i in U] | position of the last revealed element of U - i): E_i <= L <= h2(delta); it is a sum of
  Phi(A_k, B_k) over the squared Doob increments of g and h; min over orders = shortest path over subsets.
- Two-sequence lemma: A_{>=K} B_{<=K} <= M delta^2 for all K gives L <= (1/ln2 + 4 + 2 log2(1+2M)) delta.
- Resampling form: W(R) = E h(x)h(x^R), V(R) = (1/2) E (g(x)-g(x^R))^2; W(R_k) V(R_{k-1}) <= M delta^2 suffices; a coarser
  chain suffices. Tribes: chain R_* > mates > 0 gives M = 1/P0 (P0 = Pr[no other tribe satisfied]).
- Exact E_i under block composition; private AND of k+1 variables: L/delta <= 2 + 2^-k (2k + log2(1/rho)).
- Windows r = 1..n-1 interpolate L down to E_i. Filtration conjecture (exists i, pi with L <= c Inf) implies FEI.
- Bent point replacement: E_i/Inf_i at the new coordinate grows ~linearly in k (11.44 at k=10) while every other
  coordinate stays below 2: the choice of coordinate cannot be dropped.

Scars: (1) I first called the bent-point example unreproduced after testing the wrong construction (a flipped inner
product); our own audit/check_sec7.py already had the right one - read our earlier audit code before calling a claim
unreproduced. (2) An abstract phrase "the probability that resampling preserves pivotality" reads as a conditional
probability and is off by a factor delta; the theorem uses the joint W. (3) git commit segfaulted in the brain repo while
another agent's repack ran for 3 h; the 0-byte .git/index.lock it left was removed after checking no git process held
the index, then the push was retried.

Related: [[fei_p4_equivalent_forms_posted_2026_11_10]], [[fei_p3_variance_han_bound_posted_2026_11_10]],
[[fei_p2_good_coordinates_posted_2026_11_10]].

