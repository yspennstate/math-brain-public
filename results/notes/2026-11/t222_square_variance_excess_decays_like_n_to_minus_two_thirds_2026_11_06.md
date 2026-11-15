---
name: t222_square_variance_excess_decays_like_n_to_minus_two_thirds_2026_11_06
description: "[PROVISIONAL] T222 Steele TSP variance: anchoring the limit at the torus plateau 0.0366, the unit square's excess decays n^-p with p=0.67 (0.55-0.81); p=1/4 excluded"
metadata:
  type: project
  created: 2026-11-06
  created_at: 2026-11-06T06:45:24+02:00
  status: provisional
  evidence: ""
---

T222 (Steele's variance-limit conjecture, random Euclidean TSP in the unit square). 6 Nov 06:4x, an agent.

What was done: refit the 30 Oct square table (n=100..1600, Var 0.0565, 0.0492, 0.0462, 0.0408, 0.0378) as Var = a + b n^-p with a FIXED at the torus plateau 0.0366 +- 0.0007, instead of leaving a free.

Result: best p = 0.67, b = 0.44, chi2 1.16 on 4 dof; 1-sigma p range 0.55-0.81. p = 1/4 chi2 15.2 (excluded), p = 1/2 chi2 3.0 (allowed), p = 1 chi2 5.8 (disfavoured). Moving a by the solver's +-0.002 puts best p in 0.57-0.80 and p = 1/4 stays excluded (chi2 >= 13).

Why it matters: the square-only fit left the limit anywhere in 0.019-0.040 depending on the assumed p. If square and torus share the limit (assumed, not proved), the low end (0.019 at p = 1/4) is gone, and the decay matches a perimeter count (about sqrt(n) boundary points, fluctuation n^-1/2 each, p = 1/2) within 1.5 sigma.

Status: provisional, an assumption-dependent fit on five points with near-optimal (not optimal) tours. What would change it: an LKH-class solver at n >= 10^4, or a proof that the boundary term's variance is o(1).

Files: brain-repo 06_math_research/frontier/rows/T222/boundary_fit/fixed_a.py and fixed_a.out; frontier move 2026-11-06 06:42 (kind narrowed). Data: research-repo research_pushes/2026-10-30-t222-tsp-variance. Related: [[t222_tsp_variance_is_flat_near_0p037_on_the_torus_2026_10_30]].

**Condition (6 Nov 17:58, profile fit):** the square table alone leaves the limit free (a in 0..0.0377 at 1 sigma, a = 0 costs dchi2 0.30, the torus value 0.67). Everything above is conditional on the torus value being the square limit; the square data are consistent with that but do not test it. A test: the same point sets under square and torus metrics, Var(L_sq - L_tor), or square runs to n = 6400. rows/T222/boundary_fit/profile_a.py.
