# T240 phase (b) and the glue (G): plan of proof

Draft, agent H, 18 Oct 2026. Not a proof. States what is to be proved after C8 (deterministic entry over the
eta cell) and C9 (deterministic post-exit recovery), the structure that should make it tractable, and the lemmas each
step needs. Notation as in C9_post_exit_DRAFT.md: X^N_t the seven overlaps at time t = steps/N, F the drift, x*(eta)
the symmetric plateau, P the teacher-swap-adapted eigenframe at x*, z = P^{-1}(x - x*) = (u, s).

## 1. The odd sector

Let tau swap the teacher indices. F(tau x) = tau F(x), x* is tau-fixed, and every column of P is tau-even or tau-odd
(parities -1, 1, 1, 1, -1, 1, 1; the unstable column 0 and the stable column 4 are odd). Write z = (o, e) with
o = (u, s_4) the odd coordinates and e the five even ones. In these coordinates tau acts as (o, e) -> (-o, e), so

    F_o(-o, e) = -F_o(o, e),   F_e(-o, e) = F_e(o, e).

Consequences, all exact:
- o = 0 is invariant for the ODE (the symmetric slice). The ODE solution from a symmetric start has o = 0 for all time.
- F_o(o, e) = M(e) o with M(e) a 2x2 matrix depending smoothly on e and on o only through even powers; M(0) =
  diag(lambda, -nu_4) up to the frame's float error (P is an eigenframe at the float plateau).
- F_e(o, e) = A_e e + Q(o, o) + O(|e|^2 + |o|^2 |e|): the odd sector forces the even one only quadratically.
- There is no linear coupling from e into u at all, at any e: the escape coordinate is driven only through the odd
  sector. A generic saddle would have du/dt containing a term linear in the stable coordinates; here that term is
  M(e)_{u s4} s_4, odd times smooth.

So near x* the escape is a two-dimensional linear saddle in o with coefficients modulated by e, with e relaxing to 0
and fed back only quadratically by o.

Checked in floats (18 Oct 06:3x): on states x* + P(0, e) with |e| ~ 1e-3 and 1e-4, |F_o| <= 1.2e-19 while |F_e| ~ 6e-4;
dF_u/de is 1.6e-16 at o = 0 and 2.2e-4 at |o| = 1e-3. Plateau spectrum: -0.70532, -0.4658, -0.4476, -0.29011, -0.00383,
-0.00192, +0.03162; the adapted frame diagonalizes J to 4e-11.

## 2. Steps

Fix eta in E (C9's interval; C8 covers a wider cell with q0 = 1). Constants: lambda >= 0.0315, U_c = 1/100000,
kappa = 1/500 (the cone lemma's margins hold on the whole box N, not only in the cone).

Step 1 (fixed horizon, from the start to T_2). By C8 the symmetric ODE solution y(t) from (1, 0, 0) converges to x*
with a certified exponential rate (trap ball radius 2e-4, mu* <= -7.534e-4 in C8's trap frame). Choose T_2 with
|P^{-1}(y(T_2) - x*)| <= kappa U_c / 8; T_2 is a constant (no N). The fixed-horizon theorem (Goldt et al.; any of the
standard ODE-limit theorems for online SGD) gives sup_{t <= T_2} |X^N_t - y(t)| = O_P(N^{-1/2} log N), with the random
asymmetric initial data entering as an O(N^{-1/2}) perturbation. Linearizing around y on [0, T_2]:
    o(T_2) = Phi_o(T_2) o(0) + N^{-1/2} G_N + o_P(N^{-1/2}),
with Phi_o the variational flow of the odd sector along y (invertible) and G_N the accumulated noise, asymptotically
Gaussian. Output: at T_2, |e| <= kappa U_c / 4 and o = N^{-1/2} Z_N with Z_N converging in law to a nondegenerate
Gaussian vector (nondegenerate already from the initial condition: the uniform-on-sphere start gives R_11 - R_12 of
order N^{-1/2} with a Gaussian limit).
  Needed: (L1) the u-component of Phi_o(T_2) o(0) has a nondegenerate limit law. Phi_o is a 2x2 invertible matrix and
  o(0)'s limit law is a nondegenerate Gaussian in the plane, so this holds. Short.

Step 2 (linear escape, |u| from N^{-1/2} to N^{-1/2} log^2 N). On the box N, with the noise martingale's quadratic
variation at most C t / N, compare o with the linear SDE do = M(0) o dt + N^{-1/2} dW. Over a time of order log log N
the even sector stays within kappa U_c / 4 (it contracts at the stable rates, and the quadratic feedback is
O(N^{-1} log^4 N)), and u(t) = e^{lambda t} (u(T_2) + O_P(N^{-1/2} e^{-lambda (t - T_2)}) ...), so u reaches
N^{-1/2} log^2 N at a time T_2 + (2/lambda) log log N + O_P(1), with s_4 = O_P(N^{-1/2} log N).
  Needed: (L2) a Gronwall bound for the difference between o and its linearization while |o| <= N^{-1/2} log^2 N and
  |e| <= kappa U_c / 4, using M(e) = M(0) + O(|e|) and F_o = M(e) o exactly (the odd form of section 1). The error is
  relative, O(|e| + |o|^2) times |o|, so it cannot change the sign or the growth rate of u.

Step 3 (cone phase, |u| from N^{-1/2} log^2 N to U_c / 2). At the start |s_4| = O_P(N^{-1/2} log N) and
|e| <= kappa U_c / 4 but e may still be far larger than kappa |u|. Two sub-steps:
  3a. While |u| <= U_c / 4: e contracts like e^{mu_ss t} up to the noise floor O(N^{-1/2}) and the quadratic forcing
      O(|o|^2); u grows like e^{m_uu t}. After the constant time (1/|mu_ss|) log(2 kappa U_c / (kappa N^{-1/2} log^2 N))
      ... the ratio |e| / |u| falls below kappa / 4 well before |u| reaches U_c / 4, because e decays and u grows. In
      numbers: e needs a time of order log N / |mu_ss| to fall from kappa U_c / 4 to below kappa N^{-1/2} log^2 N, while u
      needs log N / (2 lambda) to grow from N^{-1/2} to U_c. The race is won by u's arrival only if e has caught up:
      what is actually needed is |e(t)| <= kappa |u(t)| / 4 at the moment |u| = U_c / 4, and since
      |e(t)| <= (kappa U_c / 4) e^{mu_ss (t - T_2)} + O(N^{-1/2} log N) + O(U_c^2) while |u(t)| grows to U_c / 4, this holds
      for N large exactly when the decay over the escape window, e^{mu_ss log N / (2 lambda)} = N^{mu_ss / (2 lambda)},
      beats the constant 4: always true since mu_ss < 0, but the convergence is only like N^{-|mu_ss| / (2 lambda)}.
  3b. From |u| = U_c / 4 to U_c / 2 inside the halved cone: the deterministic cone lemma's margin (4.3e-5 in the cone
      inequality) absorbs the noise once kappa |u| / 4 >> N^{-1/2} log N, which holds since |u| >= U_c / 4.
  Needed: (L3) a stochastic cone lemma: if the cone inequality holds with margin m on N, a solution of the perturbed
  equation with noise of size N^{-1/2} log N stays in the cone |s| <= kappa |u| / 2 once it enters |s| <= kappa |u| / 4
  with |u| >= U_c / 4, until |u| = U_c / 2, with probability tending to 1. (L4) the O(U_c^2) quadratic forcing of e is
  below kappa U_c / 16: this is a computable bound on Q over N, and the cone lemma already contains it (the Jacobian
  hull covers it); state it separately.
  Output: (G) at tau_N = first time |u| = U_c / 2, with probability tending to 1, X^N lies in N with |s| <= kappa |u| / 2.

Step 4 (the escape time). From steps 1-3, u(t) = e^{lambda (t - T_2)} N^{-1/2} (Z_N^u + o_P(1)) up to the cone phase,
so tau_N = T_2 + (1/lambda) log(U_c sqrt N / (2 |Z_N^u|)) + O_P(1) and tau_N / log N -> 1 / (2 lambda) in probability.
The specialization time of the statement (|R_11 - R_12| > delta) differs from tau_N by the O(1) time C9's tube needs to
carry |R_11 - R_12| from about U_c to delta, so it has the same limit.

Step 5 (after the escape). C9 from the section, with the fixed-horizon theorem over the window [tau_N, tau_N + 820 +
T_trap], as in C9's last section.

## 3. Where this is thin

- REVISION of 3a (06:3x, after the spectrum): two stable modes are slow (-0.00383, -0.00192 against lambda = 0.0316), so a
  race between e's decay and u's growth would converge like N^{-0.03}: useless. Do not race. Choose T_2 (a constant)
  so that |e(T_2)| <= kappa U_c / 64 already (C8's exponential convergence; at rate 0.0019 this costs T_2 of order a few
  thousand, still a constant). Then during the escape bound e's growth instead of relying on its decay:
      d|e| <= mu_ss |e| + |m_su| |u| + noise,   so   |e(t)| <= |e(T_2)| + |m_su| |u(t)| / (lambda_eff - mu_ss) + O_P(N^{-1/2} log N)
  while u grows at least like e^{(m_uu - kappa |m_us|) t}. The cone lemma's first inequality bounds |m_su| below
  kappa (m_uu - mu_ss), so at |u| = U_c / 4 this gives |e| <= kappa U_c / 64 + (about) kappa U_c / 4 times a ratio below 1
  set by the lemma's margin. (L3') compute that ratio over N; it must leave |e| <= kappa |u| / 2 at |u| = U_c / 4.
  If it does not, shrink U_c (the margin improves as U_c falls) or split the escape in two cones.
  COMPUTED (18 Oct 06:41, c9_cone.cone over N in 4 u-cells, exact interval bounds, C9_ARB=1): at U_c = 1e-5, kappa =
  1/500: m_uu >= 3.1617e-2, |m_us| <= 5.109e-6, |m_su| <= 7.382e-6, mu_ss <= -1.894e-3 (negative on all of N), grow >=
  3.1617e-2, so r = |m_su| / (kappa (grow - mu_ss)) <= 0.111. Derivation, with s all six stable coordinates and |u|
  growing at least at rate grow inside the cone: |s(t)| <= |s(t0)| + |m_su| |u(t)| / (grow - mu_ss), hence
  |s| / |u| <= |s(t0)| / |u| + r kappa. At |u| = U_c / 4 this is <= kappa / 2 whenever |s(t0)| <= (1/2 - r) kappa U_c / 4,
  i.e. |s(t0)| <= 0.097 kappa U_c; take T_2 with |s(T_2)| <= kappa U_c / 16. Halving U_c halves r (0.055 at 5e-6);
  kappa = 1/250 gives 0.060. So (L3') holds with room; what remains is the noise term and the early phase.
  Early phase caveat: the growth rate grow is proved only inside the cone. Before u enters it (|s| > kappa |u|) use the
  odd structure of section 1 instead: du/dt = (lambda + O(|e|)) u + O(|e|) s_4 exactly, with s_4 = O_P(N^{-1/2} log N),
  so u still grows at rate lambda - O(kappa U_c) until |u| >> |s_4| / kappa, after which |e| <= kappa U_c / 16 + r kappa |u|
  carries it into the cone by |u| = U_c / 8.
- The old 3a rate N^{-|mu_ss| / (2 lambda)} is the reason for the revision. The slowest stable rate at the plateau sets it; if |mu_ss| is small
  compared with lambda the statement is true but holds only for astronomically large N. Record the plateau's stable
  spectrum (not in the files yet) before writing 3a.
- mu_ss in the cone lemma is a log norm over the whole box N in the adapted frame, an upper bound for the slowest
  stable rate; the 3a argument needs it negative on N, which the cone lemma's margin implies (kappa (m_uu - mu_ss) >
  |m_su| + ...) only if m_uu > |m_su| / kappa - which is not the same statement. Check mu_ss < 0 on N directly.
- Step 1's fixed-horizon theorem is quoted for the committee machine with the erf activation at learning rate eta / N;
  Goldt et al. 2019 Theorem 1.1 is that statement, with constant e^{L T_2}. T_2 is a constant, so this is fine, but the
  theorem's hypotheses (bounded moments of the increments along the trajectory) must be checked for erf, which is
  bounded with bounded derivatives - routine.
- (L1) relies on the initial law. A start exactly on the symmetric slice (not the statement's random start) would
  escape by noise alone; then Z_N^u is the noise integral, nondegenerate if the noise covariance has a nonzero
  u-component somewhere along y. Not needed for the statement as written.

## 4. (L2) in detail: the odd sector stays linear while it is small

Setting. On the box B = {|o| <= rho_o, |e| <= rho_e} (rho_o = N^{-1/2} log^2 N, rho_e = kappa U_c / 16), the drift in
the frame P reads exactly (section 1)

    F_o(o, e) = M(e) o + C(o, e)[o, o, o],     F_e(o, e) = A e + Q(e)[e, e] + S(e)[o, o],

with M(e) = M(0) + M_1(e) e, M(0) = diag(lambda, -nu_4) + E_0, |E_0| <= 4e-11 (the frame's float error), and C, Q, S, M_1
bounded on B by interval constants c_C, c_Q, c_S, c_M (computable: third derivatives of F in the frame over B; B sits
inside the cone lemma's box N, whose Jacobian hull is already enclosed). Write the SGD increment in time units of N steps
as dX = F(X) dt + dmart + O(N^{-1}) dt, the martingale having conditional covariance Sigma(X) / N with Sigma bounded on N.

Claim. Let o_lin solve do = M(0) o dt + P_o^{-1} dmart from o(T_2). Then on the event that the process stays in B up to
time T_2 + t,

    |o(t) - o_lin(t)| <= (c_M rho_e + c_C rho_o^2 + |E_0|) * integral_0^t e^{lambda (t - r)} |o(r)| dr + O(N^{-1}) e^{lambda t}.

Proof. Subtract: d(o - o_lin) = M(0)(o - o_lin) dt + (M(e) - M(0)) o dt + C[o, o, o] dt + O(N^{-1}) dt; the martingale
parts cancel exactly because both equations carry the same noise. Variation of constants with |e^{M(0) r}| <= e^{lambda r}
(M(0) is diagonal up to E_0, absorbed). No stochastic integral remains, so the bound is pathwise.
  Consequence: with |o(r)| <= 2 |o_lin(r)| (bootstrap), the relative error |o - o_lin| / |o_lin| is at most
  2 (c_M rho_e + c_C rho_o^2 + |E_0|) t, which over the escape window t <= (2 / lambda) log log N + O(1) is
  O(kappa U_c log log N): small, but it must be below 1/2, which ties U_c to the escape window only through log log N.
  That is where the statement is asymptotic in a mild way. The constant c_M is the one number to compute: the largest
  entry of dM/de over N in the frame; the cone lemma's |m_su| <= 7.4e-6 at U_c = 1e-5 says c_M rho_e-type terms are of
  that order, i.e. c_M ~ 7.4e-6 / (kappa U_c) ~ 0.37. COMPUTED instead (18 Oct 06:54, interval Jacobian in the frame over
  {o = 0, |e_i| <= rho_e} about X*): the odd block's half-width is at most 4.25 rho_e (rho_e = 1e-7), 4.34 rho_e (1e-8);
  at 1e-9 the X* width (1.2e-9) dominates. So c_M <= 4.4, ten times the estimate, and the relative error is at most
  2 * 4.4 * (kappa U_c / 16) * t = 1.1e-8 t: about 1e-6 over a window of t = 100. Not binding.

What the claim does NOT give: control of e during the window. That is separate and easy: e contracts at rate at least
|mu_ss| on B (computed: mu_ss <= -1.894e-3 on N) and is forced by S[o, o] = O(rho_o^2) and by noise O(N^{-1/2}), so
|e(t)| <= |e(T_2)| + c_S rho_o^2 / |mu_ss| + O_P(N^{-1/2} log N / sqrt|mu_ss|) stays below rho_e. The slow rate enters
only as the 1/|mu_ss| ~ 530 factor on terms that are O(N^{-1} log^4 N) and O(N^{-1/2} log N).
