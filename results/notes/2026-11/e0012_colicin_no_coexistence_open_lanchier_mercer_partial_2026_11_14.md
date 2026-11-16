---
name: e0012_colicin_no_coexistence_open_lanchier_mercer_partial_2026_11_14
description: "[PROVISIONAL] E0012 (Durrett 2009 coexistence survey Problem 6: in the Durrett-Levin colicin/allelopathy model with lambda_1 < lambda_2 and equal death rates, coexistence is impossible) still open 14 Nov; Lanchier-Mercer ALEA 21 (2024) arXiv 2305.17016 prove partial results and say no-coexistence is open"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T09:05:41+02:00
  status: provisional
  evidence: ""
---

E0012, from Durrett, Coexistence in stochastic spatial models (Ann. Appl. Probab. 2009), Problem 6, PDF p.14. Conjecture: in the Durrett-Levin colicin model, where type 1 produces the toxin and type 2 dies at rate 1 + gamma * f1, coexistence is impossible when the toxin producer is the weaker breeder (lambda_1 < lambda_2) and both natural death rates are 1. In the mean-field model the interior fixed point is unstable there.

Status 14 Nov 2026: OPEN, with partial results. N. Lanchier and M. Mercer, Durrett-Levin spatial model of allelopathy, ALEA 21 (2024), article 21-14, arXiv 2305.17016. Their notation: beta_1 is the inhibitory species' birth rate, beta_2 the susceptible species', and gamma the toxin strength; neighbourhood range M; beta_c is the contact-process critical value. Results:
- Mean-field: complete phase picture with global stability of the fixed points. The interior point p12 lies in the simplex iff beta_1 < beta_2 < (1+gamma)beta_1 - gamma, and it is unstable there.
- Thm 1: if beta_2 > beta_1 > beta_c, then gamma < gamma_- implies species 2 wins.
- Thm 2: if beta_2 > beta_1 > beta_c, then gamma > gamma_+ implies species 1 survives. Species 1 wins when M = d = 1.
- Thm 3: if beta_1 = beta_2 > beta_c and gamma > 0, species 1 wins in d >= 3 (duality, transience of the first ancestor).
- Thm 4: beta_2 > beta_+ implies species 2 wins.
- Thm 5: with long range M, species 2 survives (coupling with the grass-bush-tree system).
Their page 7, verbatim: 'the absence of a phase of coexistence in the spatial model is still an open problem.' They conjecture a single nondegenerate gamma_c with no coexistence on either side; that is exactly E0012.

Gaps a new attempt could target:
(a) The middle range gamma_- <= gamma <= gamma_+.
(b) Theorem 3 for d = 1, 2, which needs a different method: with gamma = 0, the d <= 2 multitype contact process clusters (Neuhauser), and the open question is whether gamma > 0 pushes the clustering toward species 1.
(c) d = M = 1 with general gamma, where Thm 2 already gives 'species 1 wins' for large gamma; an interface argument might cover every gamma.
The 8 Sep intake attempt (E0012-A001) reduced the problem to the sign of an interface speed under fast stirring. That reduction is heuristic only away from the fast-stirring limit.

Correction for the 200 list: the line 'mean-field behaviour is known' is right, and it is now proved in full (LM Section 2). Related: [[e0007_two_type_contact_unequal_death_rates_open_stover_partial_2026_11_14]]. Work files: scratch area e0012_lm.txt and e0012_dl/lm.pdf of session agent.

Numerics, d = M = 1 (14 Nov, worker machine 1 ~/e0012_20af, dl1d.c in the session agent scratch area).
- Setup: ring of L = 20000, T = 4000, beta_2 = 5. The 1D nearest-neighbour contact threshold is about 3.30, so beta = 3 dies out here.
- Each run below: two seeds, gamma in {0, 0.5, 1, 1.5, 2, 3, 4, 6, 10}.
- beta_1 = 4.0:
  - gamma <= 1.5: species 2 wins.
  - gamma >= 4: species 1 wins.
  - gamma = 2 and gamma = 3: both types still present at T. The densities drift toward 2 (gamma = 2) and toward 1 (gamma = 3), so gamma_c is about 2.5.
- beta_1 = 4.6:
  - gamma = 0: species 2 wins.
  - gamma >= 1: species 1 wins.
  - gamma = 0.5: both types present at T (0.23-0.29 against 0.42-0.49), so gamma_c is about 0.5-1.
- Reading: one transition, with the slow coarsening near gamma_c expected from 1D clustering. There is no sign of a coexistence window.
- Small runs only: not evidence about d = 2.
