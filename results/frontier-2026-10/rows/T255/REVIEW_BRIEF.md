# T255 review brief (for an independent referee)

Object: the covariance SDE of the shaped transformer, Noci et al. 2023 (arXiv 2306.17759), Theorem 4.2, and
Corollary 4.3 with ReLU MLP blocks. Question: is the limit defined for all depths, or can it explode?
Paper: PAPER_DRAFT.md (sections are drafted out of order in the file; the plan is at "Plan of the paper").

Claims to check, in order of what everything else rests on:
1. Section 2: the noise of Thm 4.2 rewritten in congruence form, and positivity up to explosion (Theorem 1).
   Check the congruence form entry by entry against Noci et al.'s Sigma; script paper_sigma.py, cov_check.py;
   orthogonal invariance V -> O V O^T: orth_inv.py.
2. Section 3, m = 2 (Theorem 2): explosion with positive probability iff gamma^2 < 1/2. Lemma 3.1 (scale
   density) and the Feller test at infinity. Scripts m2_check.py, m2_gen.py; M2_EXACT.md has the exact computation.
   Also (3.3), the hypergeometric closed form of P(explosion) and its two limits (erf(w0/(4 tau0)) as gamma^2 -> 0,
   linear vanishing at 1/2); script m2_closed_form.py checks it against quadrature of (3.2).
3. Section 5 (Theorem 4): P(explosion) < 1 always. Lemma 5.1: (tr V)^q is a supermartingale near 0 with
   delta^2 = (1-q)c/(2mC); then ellipticity carries the process near 0 from any start.
4. Section 4, m >= 3 (Theorem 3): explosion with positive probability for every gamma^2 in (0,1]. Schur
   coordinates (a, w, X, Phi_S), Lemma 4.1 asymptotics, Lyapunov function Y = a^-q + |w|^2 + M Phi_S^p,
   then the support theorem. The signs that matter: mu_S < 0 and kappa > 0. Scripts lyapY.py, schur_sym.py,
   trans_sym3.py.
5. Section 6, MLP blocks: arc-cosine kernel keeps positivity; for m >= 3 the transverse coordinate becomes
   psi = Phi_S + 1/a (Lemma 6.1); for m = 2 an Ikeda-Watanabe comparison gives the bracket [0.0801, 0.1339]
   at gamma^2 0.2, Delta 4. Scripts lyapY_mlp.py, mlp_checks.py, feller_closed.py.
6. Section 7: numbers only (sim_mlp.py, mc_m2_g02_D4.out: 44/400 exploded, 7 undecided, inside the bracket).

Also check novelty: lit.json and the Related work section; we found no paper on explosion or global existence of
this SDE. A verdict per numbered claim (PASS / FAIL with the line / UNCLEAR) is what admission needs.
