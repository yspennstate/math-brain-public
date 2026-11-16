---
name: c0033_lyons_determinantal_entropy_concavity_open_two_point_posted_codex_abc_partial_2026_11_13
description: "C0033 (Lyons ICM 2014 arXiv 1406.2707, Conjecture 2.6 = Lyons 2003 Conjecture 9.2: entropy of the determinantal measure P_Q is concave in the kernel Q on a finite set; implies Conjecture 5.3 on entropy-rate concavity) is open on 13 Nov 2026, nothing new on arXiv. Ours: the |E| = 2 case is posted (github.com/yspennstate/lyons-determinantal-entropy-two-points, public, head 67dd302a, 11 Nov). Three unrefereed Codex runs on 13 Nov, all PARTIAL: C0033A (two-point, conditional lifting, product-kernel Hessian and fourth variation), C0033B (one row and column jointly concave; indefinite rank-two on three points; the PSD certificate does NOT extend to the second compound at order five), C0033C (coordinate + rank-one jointly concave in every dimension, D^2H <= -4 alpha^2; singular three-point stratum). Full three points and general rank two stay open; no counterexample. C0033D (14 Nov, PARTIAL): exact 7x7 criterion in seven parameters; family Q_r shows no uniform margin, Hessian sign checked independently"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T19:00:05.213Z
---

C0033, rank 59 on the 200 list. Source: Russell Lyons, "Determinantal probability: basic properties and conjectures",
ICM 2014, arXiv 1406.2707, Conjecture 2.6 p.5 and Conjecture 5.3 p.22. For positive contractions Q_1, Q_2 on l^2(E), E
finite, is Ent(P_{(Q_1+Q_2)/2}) >= (Ent(P_{Q_1}) + Ent(P_{Q_2}))/2? By finite restrictions this gives concavity in f
of the entropy rate of stationary determinantal processes (Conjecture 5.3). The C0033A log notes that the finite
conjecture first appears as Conjecture 9.2 in Lyons 2003.

Status 13 Nov 2026: open.
- My arXiv check on 13 Nov (determinantal with entropy and concave; "determinantal point process" with entropy):
  nothing on the conjecture. The hits are machine learning and fermionic Gaussian states. Yuzhou Gu's unrefereed report
  "Entropy of determinantal point processes" (sevenkplus.com/data/dpp.pdf) is the prior partial result named in the
  Codex prompts.
- Ours, posted: "Concavity of the entropy of determinantal measures on two points", public repo
  github.com/yspennstate/lyons-determinantal-entropy-two-points (head 67dd302a, 11 Nov, "Cite Meszaros on limiting
  entropy"). The |E| = 2 case of the conjecture.
- Three Codex runs, referee_reports/2026-11-13/C0033A, C0033B, C0033C (13 Nov 01:37-03:xx, gpt-6.1-sol, unrefereed,
  each PARTIAL). Each builds on the one before with attribution.
  - C0033A: complex two-point theorem (attributed to our posted paper); conditional-coordinate lifting (conditional kernels
    are affine in an updated coordinate block, so any m-point concavity lifts to m-coordinate changes in every dimension);
    Hessian decomposition at block-diagonal kernels; sharp fourth-order formula at product kernels.
  - C0033B: for Q = [[a, v*], [v, C]] with C fixed, entropy is jointly concave in (a, v), in any dimension. On three points
    the matrix R_Q = D - gamma Q is PSD, so the Hessian is -Fisher + 2 tr(adj(A) R) and is nonpositive for every
    indefinite rank-two direction; its positive index is at most one. Scar recorded there: the PSD certificate does not
    extend to the second compound in general dimension. Order-five kernels give exterior Rayleigh quotient about
    -0.0258 (interval-validated). The bivector is not decomposable, so this is not an entropy counterexample.
  - C0033C: R_Q is singular exactly when the support graph is disconnected, and there the Hessian is NSD. (s, t) ->
    H(Q_0 + s e_i e_i* + t b b*) is jointly concave in every finite dimension, with D^2 H(Q)[A, A] <= -4 alpha^2 for
    A = alpha e_i e_i* + b b*. So concavity holds along every rank-two direction whose range contains a coordinate
    vector.
- Still open: full concavity on three points (inequality (17) of C0033B on the connected strict domain), PSD rank-two
  directions on three points, general rank two in higher dimension, and the conjecture itself. No counterexample.
- Next step if anyone picks it up: an independent referee pass on C0033B/C0033C (the code is in each folder) before
  any of it goes into a paper. Then a three-point paper extending the posted two-point one, citing Gu.

Update 14 Nov 00:4x: C0033D (Codex fourth attempt, mini1, report sha256 a566b9bf, archived to
06_math_research/referee_reports/2026-11-14/C0033D) is PARTIAL. Proved there: (21) is exactly b*^T M^{-1} b* >= 2 for an
explicit 7x7 positive matrix M in the seven parameters (a,b,c,|Q12|,|Q13|,|Q23|, phase of Q12 Q23 Q31), with all nine
ambient directions kept; the exact family Q_r (diagonal 1/2, off-diagonals +-ir, 0<r<1/(2 sqrt 3)) has a negative definite
Hessian but margin 4/(L+4) -> 0 as its eigenvalues approach 0, 1/2, 1, so no uniform positive margin exists and a plain
compact cover cannot close the problem; two boundary expansions (small perturbation of a diagonal kernel, and tK / I-tK);
an interval cover proves margin > 0.0247 on one small box only. My independent check (agent_run/c0033d_check/hess_qr.py,
mpmath finite differences from the atom formula alone): the Hessian at Q_r is negative definite at r = 0.05 .. 0.2885
(largest eigenvalue -0.04 down to about -3.96), so the sign half of its Theorem 2 holds. The margin formula was re-derived the same night (below).
re-derived. Second check 14 Nov 01:1x (c0033d_check/margin_qr.py, 80 digits): on the plane alpha I + beta(J3-I) the Hessian equals -(F + L tr T^2) + L (tr T)^2 to 1e-27 and the margin from it matches (12)-(13) to 12 digits, tending to 4/(L+4); Theorem 2 is confirmed in full (pushed to referee_reports/2026-11-14/C0033D_check). Still open: the mixed spectral/graph boundary, i.e. kernels near eigenvalue 0 or 1 with one edge going to zero.
A fifth attempt should start from the Q_r family and estimate the margin in a neighbourhood of its limit.


Related: [[c0035_trig_determinantal_block_factor_open_m_ge_2_broman_m1_2026_11_13]] (Lyons, same survey family);
[[p0010_biased_random_orientations_z2_infinite_path_open_dp_comparison_only_2026_11_13]] (previous item in this loop).

Update 2026-11-14 03:10 (an agent): C0033E (Codex, mini1) PARTIAL - exact margin on the cyclic family m = 4A/B, uniform bound m >= 1/(4 Lambda + 2) on a RESTRICTED mixed collar (equal real connections, balanced block), and Lambda m -> 1/2 along Q(1/2,h,h^6) so a global m >= c/(Lambda+C) needs c <= 1/2. Second check (mpmath 300 digits, exact polynomial derivatives, independent of the run's code): Thm 1 to 1e-140, collar to 1e-50, inherited identity -D2H = J - d z z^T to 6e-142, Lambda m = 0.567, 0.533 at h = 1e-3, 1e-6. Archive referee_reports/2026-11-14/C0033E (718cfa11), check C0033E_check. C0033F queued on mini1 (general mixed collar, global constant, face classification).
- 14 Nov 05:3x (an agent): C0033F (general mixed collar, m0 = (1 + K/det W eta^T N^-1 eta)^-1 >= 1/(2K+3)) second-checked: formula (4) agrees with the true margin to 1e-13 in six cases (independent of a, complex block, one connection zero); bound (5) holds on 4000 blocks, smallest m0(2K+3) = 1.53, so the constant is not sharp. Still PARTIAL: spectral collars and the compact remainder are open. Check: referee_reports/2026-11-14/C0033F_check. C0033G (spectral collars, compact interval cover, sharper (5)) queued on mini1 batch12.
