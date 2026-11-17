---
name: cn0986_torus_hitting_robustness_ratio_theorem_2026_11_17
description: "[PROVISIONAL] CN0986 (Zuckerman robustness of hitting times on the torus): proved on Z_L^D, L even, D>=3, eps=c/L: t_hit^+(c/L)/t_hit -> ((e^c-1)/c)^D; paper in private repo yspennstate/torus-hitting-robustness 49800ef, audit pending"
metadata:
  type: project
  created: 2026-11-17
  created_at: 2026-11-17T00:52:42+02:00
  status: provisional
  evidence: ""
---

Result (an agent loop, 16-17 Nov 2026). On the torus Z_L^D with L even and D>=3, perturbing the walk at scale eps=c/L, the ratio of the perturbed to the plain hitting time converges to ((e^c-1)/c)^D; corollary L*rho_hit(C) -> r_D(C). This closes the gap Zuckerman left on the torus (Zuc26, Def 1.9, Thms 1.10-1.11).

Key steps: half-line lemma, Lemma A', Lemma B and the reduction are new. The heat-kernel bound uses Delmotte 1999 Thm 1.7 applied to the PERIODIC LIFT of the cycle chain to Z (Delmotte needs an infinite graph; sum over images y+zL gives C(1 ^ s^{-1/2} + L^{-1})). Numerical checks in the repo: grid_rho, product_check, halfline_check, schur_check, dmax, gate.

Status: provisional until the paper_audit editor read comes back (queued 17 Nov; queue was full). Paper: loops/72de1487_loop_1115/cn0986/paper/main.tex, CREDITS.md. Private repo yspennstate/torus-hitting-robustness at 49800ef; goes public only on his click. Scar from this one: Delmotte's infinite-vertex hypothesis was missed in the first draft - check the hypotheses of every heat-kernel theorem against a finite graph. Related: [[open_problem_catalogue_1128_probability_networks_computation_2026_11_16]].
