# T255 The covariance SDE of the shaped transformer: global existence

Lead: unassigned. Dossier written 2026-10-16 by agent A from the auditor's record (worker L, TRIAGE 02:5x), the
text of Noci, Li, Li, He, Hofmann, Maddison, Roy arXiv:2306.17759 v2 (Eq. 1, 2, 8, 9; Definition 4.1; Theorem 4.2 pp 9-10;
Corollary 4.3; Section 4.4 pp 10-11; read 16 Oct 04:0x) and computations in this folder.

## STATEMENT
The list row asked to "prove this convergence rigorously, including the attention contribution, and determine whether
the SDE has a non-degenerate solution for all finite t". The first half is DONE in the source (auditor; checked here):
Theorem 4.2 proves, for shaped attention A = I + Softmax(Y/tau) - 11^T/m, tau = tau0 sqrt(n n_k), lambda^2 + gamma^2 = 1,
LOCAL convergence (Definition 4.1: the processes stopped at T_r = inf{t : |V_t| >= r} converge weakly in Skorohod) of the
token covariance V_l = X_l X_l^T/n, in the clock t = l/n, to dV = b(V) dt + Sigma(V)^(1/2) dB; Corollary 4.3 adds shaped
MLP blocks. Section 4.4 leaves global existence open (cubic drift, no general guarantee; instability seen numerically
only from adversarially large initial covariance).
Repaired statement (the open half): for the shaped-attention SDE of Theorem 4.2 with m tokens, decide whether the
solution exists for all t (no explosion) and stays positive definite, as a function of m, gamma, tau0 and V_0. The
computations below say NO for m >= 3: explosion in finite time with positive probability (not probability one). The
targets are to prove that, and to settle m = 2.

## FRONTIER
- 2306.17759 Theorem 4.2 / Corollary 4.3: local convergence; Section 4.4: global existence open; Figure 5: instability
  from initial eigenvalues of order 100, delayed by smaller gamma.
- Li, Nica, Roy arXiv:2206.02768: the covariance SDE for shaped MLPs (ReLU: degree-1 drift, global solutions; smooth
  activations: non-Lipschitz drift, local convergence only).
- Agazzi, Bruno, Mosig Garcia, Saviozzi, Romito arXiv:2604.26898 (Apr 2026): pathwise convergence of tokens in a
  finite-depth finite-width transformer with MLP blocks to an interacting particle SDE, propagation of chaos, synchronization
  by noise. A different token model (abstract only read); not the shaped covariance SDE.
- Hanin, Jiang arXiv:2605.30860: Bayesian inference with shaped MLPs via the covariance SDE; MLPs only.
- arXiv search 16 Oct 04:0x ("shaped transformer", "covariance SDE", "shaped attention", transformer + depth-and-width,
  newest first): no global-existence or explosion result for the attention SDE.

## ARCHITECTURE
Everything is homogeneous. Write P = I - 11^T/m. The drift of Theorem 4.2 is cubic: b(sV) = s^3 b(V); the diffusion is
Sigma = gamma^2 (2 - gamma^2) Sigma_lin (quadratic) + gamma^4 tau0^(-2) A(V) (quartic). Rescaling V = R U, t = R^(-2) u
gives dU = b(U) du + gamma^2 tau0^(-1) A(U)^(1/2) dB + O(1/R): at large scale the drift and the ATTENTION noise are of the
same order, the linear noise drops out. So large-scale behaviour is a scale-invariant SDE, and explosion is decided by a
Lyapunov-type exponent of the log-scale under the clock u (Feller test in one dimension).
On the exchangeable family V = a I + c 11^T (identities checked, sdrift.py / ray_check.py):
  b(V) = kappa a^2 V,  kappa = gamma^2 (m - 1)/(tau0^2 m^2)    (so the noiseless flow keeps the correlation c/(a + c) fixed
                                                               and blows up at t* = 1/(2 kappa a0^2))
  a = tr(P V)/(m - 1):  drift kappa a^3,  variance rate 2 gamma^2 (2 - gamma^2) a^2/(m - 1) + 4 gamma^4 a^4/(tau0^2 m^2 (m - 1)).
For ds = mu s^3 dt + sigma s^2 dW the Feller test gives explosion iff 2 mu/sigma^2 > 1 (scale density s^(-2mu/sigma^2)),
here 2 mu/sigma^2 = (m - 1)^2/(2 gamma^2): explosion along the ray iff (m - 1)^2 > 2 gamma^2, i.e. ALWAYS for m >= 3
(gamma <= 1), and for m = 2 iff gamma^2 < 1/2. At small scale the linear part dominates and the log-scale drifts DOWN
(the diagonal is a martingale under the linear part), so a path can also decay; hence explosion with probability in (0, 1).

## FAILURE POINT
The exchangeable family is not invariant under the noise; the one-dimensional Feller argument is a heuristic until the
angular part (U/|U| on the projectivized cone) is controlled. A proof needs either (i) a Lyapunov function phi with
L phi >= c phi^(1+delta) on a cone around the ray together with a positive probability of staying in the cone (support
theorem plus the scale invariance), or (ii) the ergodic theory of the projectivized scale-invariant process and the sign of
its exponent. A second gap: rank collapse (V -> s 11^T) is invariant and has zero drift and zero attention noise, so the
cone must avoid it. For m = 2 at gamma^2 >= 1/2 the ray heuristic is at or past the boundary and decides nothing.

## SHAPE
Days for target 1 in the form "positive probability of explosion from V_0 = s I for s large" (scale invariance + support
theorem + the ray computation); weeks for every positive-definite V_0 and for the m = 2 boundary.

## OBSTRUCTION
Explosion of a degenerate, scale-critical matrix SDE (drift degree 3, diffusion covariance degree 4) whose explosion is
decided by a competition between the drift and the Ito correction on the projectivized dynamics. Moves: positive
probability of explosion for m >= 3 (from large or all V_0); non-explosion for m = 2, gamma^2 > 1/2 (or explosion); the
same for Corollary 4.3 (the MLP terms are subleading at large scale, so the same criterion should hold).

## SETTLED
- Local convergence (2306.17759 Thm 4.2, Cor 4.3). The list's first half is not a move.
- Computed 16 Oct (sdrift.py): the drift formula of Theorem 4.2, coded from the text, agrees with a Monte Carlo of one
  layer of the finite network (n = 4000, n_k = 64, 2 x 10^5 antithetic pairs) on V = I, the 0.2-correlated V and a random
  V, m = 2 and 4, within the Monte Carlo error (e.g. m = 4 random V, diagonal 0.0493 0.0553 0.3972 0.0413 against
  0.0494 0.0554 0.3979 0.0415). On V = s I it is exactly gamma^2 (m - 1)/(tau0^2 m^2) s^3 I.
- Computed 16 Oct (ray_check.py, n = 10^6, 4 x 10^5 one-step samples of the exact covariance chain): the variance rate of
  a = tr(P V)/(m - 1) on the ray matches the formula above: 116.9 vs 117.3 (m 4, a 8), 2.3 vs 2.3 (m 4, a 2), 273.8 vs
  275.6 (m 3), 1110.8 vs 1120.0 (m 2).
- Exact covariance chain of the finite network (chain_blowup.py): given V = L L^T, one layer needs only an m x m Gaussian Z,
  a Wishart(m, n - m) and the m x n_k query/key Gaussians (X = L Q with Q Q^T = n I; Q W^V/sqrt n is iid; Q G^T = sqrt n Z^T),
  so the network at width n costs O(m^2 n_k) per layer; n_k = 1 already has the limit's second moments.
- First run (m 4, gamma^2 1/2, tau0 1, n 500, V_0 = 0.8 I + 0.2, 200 runs, t <= 10): 28.5 pct reached mean diagonal 100
  (median t 1.77), 65.5 pct decayed below 0.01. Bimodal: explosion with probability strictly between 0 and 1.
- SWEEP (chain_sweep1.txt, finished 16 Oct 05:1x; 400 runs each, n_k 1, tau0 1, V_0 = 0.8 I + 0.2 unless noted).
  P(mean diagonal reaches 100) and its median time, against P(decays below 0.01):
    m 4 gamma^2 0.5, T 10:  n 2000 0.255 (t 1.64) / 0.680;  n 8000 0.247 (t 1.63) / 0.685;  V_0 = I (rho0 0) 0.260 / 0.682
    m 4 gamma^2 0.9, T 10:  0.198 (t 1.02) / 0.777
    gamma^2 0.5, T 20, n 2000:  m 2 0.075 (t 2.44) / 0.917;  m 3 0.193 (t 2.04) / 0.807;  m 8 0.340 (t 1.71) / 0.657
    m 2, T 20, n 2000:  gamma^2 0.2 0.175 (t 4.26) / 0.695;  0.5 0.075 / 0.917;  0.9 0.030 (t 1.37) / 0.965
  The m = 4 numbers do not move from n = 2000 to n = 8000, so they describe the limit SDE, not the finite network.
  Blow-up probability rises with m and falls with gamma^2. For m = 2 at gamma^2 0.9 (above the ray prediction's 1/2),
  3 percent of runs still pass 100 by t = 20 and P(hit 10) stays near 0.17 at all three gamma^2; level 100 cannot
  tell explosion from a large excursion, so the m = 2 threshold is NOT settled by this sweep. That needs level 10^4
  or 10^6 and T 50.

## TARGETS
1. Prove: for m >= 3, every gamma in (0, 1], tau0 > 0, the SDE of Theorem 4.2 explodes in finite time with positive
   probability from V_0 = s I for all large s (then: from every positive-definite V_0).
2. Settle m = 2: explosion iff gamma^2 < 1/2 (the ray prediction), or a counterexample to it.
3. The same for the shaped transformer SDE of Corollary 4.3 (ReLU MLP blocks).
4. Experiment: the probability of explosion against n (convergence), m, gamma^2 and V_0, from the exact chain.
