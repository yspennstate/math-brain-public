# T354: a residual theorem for Adam with reshuffling on a smooth nonconvex finite sum (vanishing step)

claude-99aebc7f, 21 Oct 2026. Status: Proposition 1 proved below, re-derived line by line by its author (the audit section
at the end; an independent audit is still owed). Theorem 2 rests on the ODE method with state-dependent Markov noise; the
reduction is written out, but the check of the averaging hypothesis is a sketch; Theorem 3 (end of the file) gives a rate
for min_k E||grad f(x_k)|| by a direct coupling and does not need it (written, not yet audited). Numerical checks: drift_bound_check.py
(dbc_*_run1.txt), kappa_exact.py (kappa_exact_run1.txt).

## Setting
f = (1/n) sum_i f_i on R^d, f_i of class C^2. Adam in the PyTorch form with reshuffling (a fresh uniform permutation each
epoch), coordinatewise
    m_k = b1 m_{k-1} + (1 - b1) g_k,   v_k = b2 v_{k-1} + (1 - b2) g_k^2,   g_k = grad f_{pi(k)}(x_{k-1}),
    x_k = x_{k-1} - eta_k mhat_k / (sqrt(vhat_k) + eps),   mhat_k = m_k/(1 - b1^k),  vhat_k = v_k/(1 - b2^k),
with 0 <= b1 < 1, 0 < b2 < 1, eps >= 0. Write g_ij(x) for coordinate j of grad f_i(x), and for x fixed
    B2_j = (1/n) sum_i g_ij^2,   C_j = (1/n) sum_i (g_ij - d_j f)(g_ij^2 - B2_j),   G_j = max_i |g_ij|,
    phi_j = 1/(sqrt(B2_j) + eps),   phi'_j = -1/(2 sqrt(B2_j) (sqrt(B2_j) + eps)^2).
At the minimiser of a model with mean-zero per-example gradients, C_j is the third moment B3_j of the earlier sections.

## The frozen-x drift
Fix x. Under reshuffling the gradient stream g_{pi(t)}(x) is stationary once the epoch phase is uniform, and m_t, v_t are
the linear filters m = sum_s a_s g_{t-s}, v = sum_s w_s g_{t-s}^2 with a_s = (1 - b1) b1^s, w_s = (1 - b2) b2^s. Let
    h(x) = E[m / (sqrt(v) + eps)]
under the stationary law (phase averaged). The bias-correction factors tend to 1 geometrically and do not enter h.

### Proposition 1
Assume B2_j(x) > 0. Then
    h_j(x) = d_j f(x) phi_j + phi'_j Cov(m_j, v_j) + R_j,
    Cov(m_j, v_j) = (1 - b2) kappa C_j,   kappa in [K - 1, K],   K = (1 - b1)/(1 - b1 b2),   so |Cov(m_j, v_j)| <= (1 - b2) |C_j|,
    |R_j| <= G_j [ c2_j (1 - b2)/(1 + b2) Var_i(g_ij^2) + D_j exp( -(9/8)(1 + b2) B2_j^2 / ((1 - b2) G_j^4) ) ],
where c2_j = (1/2) sup_{v >= B2_j/4} |phi''(v)| and D_j = min(1/eps, 1/sqrt(v_lo)) + phi_j + |phi'_j| B2_j with
v_lo = (1 - b2) b2^(2n) n B2_j.

Proof. Each g_{t-s} has the uniform marginal over the n examples whatever the phase, and sum a_s = sum w_s = 1, so
E m = d_j f and E v = B2_j. Write phi(v) = phi(B2) + phi'(B2)(v - B2) + R(v); then E[m phi(v)] = d_j f phi_j +
phi'_j Cov(m, v) + E[m R(v)].
Covariance. Two slots in the same epoch carry distinct examples of one uniform permutation, so Cov(g_{pi(a)}, g_{pi(b)}^2) is
C_j when a = b, -C_j/(n - 1) when a != b, and 0 across epochs (independent permutations). Hence
    Cov(m, v) = C_j [ sum_s a_s w_s - (1/(n - 1)) sum_s a_s sum_{s' != s, same epoch} w_{s'} ],
and since w_{s'} <= 1 - b2 with at most n - 1 such s', the second sum lies in [0, (n - 1)(1 - b2)], while
sum_s a_s w_s = (1 - b1)(1 - b2)/(1 - b1 b2) = (1 - b2) K. So Cov/((1 - b2) C_j) lies in [K - 1, K], inside [-1, 1] as
0 < K <= 1.
Remainder. On v >= B2/4, |R(v)| <= c2 (v - B2)^2. On v < B2/4, |R(v)| <= phi(v) + phi(B2) + |phi'(B2)| B2 <= D, since every
window of 2n consecutive slots contains a whole epoch, so v >= (1 - b2) b2^(2n) n B2 = v_lo (and phi <= 1/eps). With |m| <= G,
    |E m R| <= G [ c2 E(v - B2)^2 + D P(v < B2/4) ].
The coordinates of a uniform random permutation are negatively associated (Joag-Dev and Proschan 1983), independent epochs keep
the family negatively associated, and nonnegative weights preserve it; by Shao's comparison theorem (2000) E F(v) for convex F is
at most its value for independent draws. (Shao's theorem is stated for finite sums; apply it to the sum over s < S and let
S -> infinity, which is legitimate because the summands are bounded by G^2 and the weights are summable, so both sides
converge by dominated convergence for the two F used.) With F(v) = (v - B2)^2 this gives Var v <= (sum_s w_s^2) Var_i(g^2) = (1 - b2)/(1 + b2)
Var_i(g^2); with F = exp(-lambda v) and Hoeffding's lemma (summands in [0, G^2]) it gives
P(v - B2 <= -3B2/4) <= exp(-2 (3B2/4)^2 / (sum_s w_s^2 G^4)), which is the exponential term. QED.

### Consequences
1. First order. The remainder is O((1 - b2) |d_j f| + (1 - b2)^2) plus the exponential term: E[m (v - B2)^2] = d_j f Var v +
   E[(m - Em)(v - Ev)^2], and the last is a third joint cumulant of order sum_s a_s w_s^2 = O((1 - b2)^2). So at a zero of h
       d_j f = (1 - b2) kappa_j C_j r_j / (2 B2_j) + O((1 - b2)^2),   r_j = sqrt(B2_j)/(sqrt(B2_j) + eps),
   (the O((1 - b2)^2) order of the cumulant is read off the expansion, not bounded here; the bound used below is item 2)
   with kappa_j = Cov(m_j, v_j)/((1 - b2) C_j) in [K - 1, K], K = (1 - b1)/(1 - b1 b2), because the within-epoch cross term
   is nonnegative and at most 1 - b2 (at b1 = 0 and small n(1 - b2) it is (1 - b2)/2, so kappa = 1/2 = K_rr): for one coordinate
   and a quadratic model this is the scalar law x* = (1 - b2) K r B3/(2 abar B2) of the earlier sections, with kappa = K
   (K_rr under reshuffling, K = (1 - b1)/(1 - b1 b2) with replacement).
2. A crude uniform bound. With rho_j(x) = |phi'_j Cov(m_j, v_j) + R_j|,
       rho_j <= (1 - b2) [ |phi'_j| |C_j| + G_j c2_j Var_i(g_ij^2)/(1 + b2) ] + G_j D_j exp(...).

## Theorem 2 (vanishing step)
Assume (a) the iterates stay a.s. in a compact set K on which B2_j > 0 for every j; (b) eta_k > 0, eta_k -> 0,
sum eta_k = infinity (eta/sqrt(k) qualifies); (c) eps > 0 or the bound v >= v_lo above. Then almost surely
    liminf_k  || grad f(x_k) ||_phi  <=  sup_{x in K} ( sum_j rho_j(x)^2 / phi_j(x) )^(1/2),   ||u||_phi^2 = sum_j phi_j u_j^2,
so liminf_k ||grad f(x_k)|| = O(1 - b2) + O(exp(-c/(1 - b2))) with constants from Proposition 1, for any smooth nonconvex finite
sum, any b1 < 1 and any n. The quadratic scalar class shows the order is attained: there every limit point has
f'(x) = (1 - b2) K r B3/(2 B2)(1 + O(1 - b2)) != 0 when B3 != 0 (STATUS, two audits).

Proof. (i) Tracking. The pair (m, v) is a uniformly contracting filter (memory about 1/(1 - b2) steps) of the reshuffled
gradient stream, whose dependence on x is Lipschitz on K; x moves O(eta_k) per step. The ODE method for state-dependent Markov
noise (Kushner and Yin 2003, ch. 8; Benaim 1999) then makes the interpolated iterates an asymptotic pseudotrajectory of
x' = -h(x), h Lipschitz on K (eps > 0, or v >= v_lo). [Sketch: the averaging hypothesis is the ergodic average of
m/(sqrt v + eps) at frozen x converging to h(x) uniformly on K, which holds because the frozen chain forgets its start
geometrically and the epoch structure is periodic.]
(ii) Lyapunov. Along x' = -h(x), with Proposition 1,
    d f/dt = -grad f . h <= -sum_j phi_j (d_j f)^2 + sum_j |d_j f| rho_j =: -W(x).
The limit set L of (x_k) is compact, invariant and internally chain transitive. If W >= delta > 0 on L, f would fall by delta per
unit time along an orbit that stays in L, which is impossible for longer than (max_L f - min_L f)/delta. So W(xbar) <= 0 for some
limit point xbar, and Cauchy-Schwarz on sum_j |d_j f| rho_j gives ||grad f(xbar)||_phi <= (sum_j rho_j^2/phi_j)^(1/2). QED.

## What this does and does not give
It answers the STATEMENT's upper half in the vanishing-step regime with the order the lower bound shows to be sharp: residual
linear in 1 - b2, proportional to the per-coordinate third moment C_j of the per-example gradients, zero for symmetric noise, with
no condition linking b2 to n (the n-dependence enters only through kappa_j in [K - 1, K] and v_lo). It is an a.s. liminf
statement, not a rate for min_k E||grad f(x_k)|| at eta/sqrt(k); a rate needs the tracking error quantified (the
O(eta_k/(1 - b2)) lag of the filter against the frozen chain), which is the next step. Assumption (a) is the usual one of the ODE
method; removing it needs a coercivity condition on f.

## Audit of Proposition 1 and the Lyapunov step (author's line-by-line pass, 21 Oct)
- E m = d_j f, E v = B2_j: each slot's marginal is uniform over the n examples for every phase, and the weights sum to 1. Holds.
- Covariance: same slot C_j, same epoch -C_j/(n - 1) (one uniform permutation), different epochs 0. The past slots of the
  current epoch number p (position of slot t), so the cross sum is phase dependent; the bound uses only that it lies in
  [0, (n - 1)(1 - b2)] for every phase. kappa_exact.py evaluates the phase-averaged sum exactly and matches a Monte Carlo of
  the two filters (4e6 reshuffled steps) to 0.1-0.5 pct in seven settings, all inside [K - 1, K]; at b1 0 and n(1 - b2) 0.16
  kappa is 0.527, near the 1/2 of Consequence 1. The earlier constant K + 1 is replaced by 1, which is what the interval gives.
- Taylor remainder on v >= B2/4 with c2 = (1/2) sup |phi''| there; on v < B2/4 the three-term bound and v >= v_lo (any 2n - 1
  consecutive slots contain a whole aligned epoch, whose squared gradients sum to n B2). Holds.
- Negative association: permutation distributions are NA (Joag-Dev and Proschan 1983, Thm 2.11); disjoint independent NA
  families are NA; nonnegative multiples are increasing functions of single coordinates. Shao's comparison for convex F is for
  finite sums; the truncation argument is added to the proof. The Chernoff/Hoeffding computation gives exactly
  exp(-(9/8)(1 + b2) B2^2/((1 - b2) G^4)), with sum w_s^2 = (1 - b2)/(1 + b2). Holds.
- Lyapunov step: with rho_j(x) := |h_j - d_j f phi_j|, continuous on K, W is continuous; if inf_L W > 0 an orbit inside the
  invariant set L loses f at a fixed rate forever, so min_L W <= 0 and Cauchy-Schwarz gives the bound at that limit point. Holds.
- Not checked here: the tracking step (i), which stays a sketch; the size of the third joint cumulant in Consequence 1, which
  is read off the expansion and not bounded.
- Numerics against the statement (dbc_*_run1.txt): every measured Cov and Var v under its bound, every |h - first order| under
  the remainder bound. The remainder bound is valid but crude: 1e-1 against 1e-4 measured at n 16, and above 1 at n 200
  where (1 - b2) G^4/B2^2 is not small and the exponential tail term dominates.

## Theorem 3 (rate for min_k E||grad f(x_k)||, step eta/sqrt(k))
Assume (A1) each grad f_i is Lg-Lipschitz and |g_ij(x)| <= G for all i, j, x, and f >= f_* ; (A2) B2_j(x) >= beta > 0 for
all j and x; (A3) eps > 0; eta_k = eta/sqrt(k) with eta <= eta_0 = beta/(8 n G Lg sqrt(d) U), U = G/eps. Let b = max(b1, b2),
rho_* = sup_x (sum_j rho_j(x)^2/phi_j(x))^(1/2) (finite under (A1)-(A3) by Proposition 1, and O(1 - b2) + O(exp(-c/(1 - b2)))
with c = (9/8)(1 + b2) beta^2/G^4). Let l = ceil(log(1/eta_T)/(n |log b|)) and let T_0 be the least T with
sqrt(T + 1) - 1 >= 2 sqrt((2l + 3) n), roughly 4 (2l + 3) n (l grows only like log T/(1 - b), so T_0 exists). Then for every
horizon T >= T_0,
    min_{k <= T} E || grad f(x_k) ||_{phi(x_k)}  <=  rho_* + sqrt(B_T),
    B_T = 2 [ f(x_0) - f_* + K_0 + K_1 (2n + log(1/eta_T)/(1 - b)) sum_{k <= T} eta_k^2 ] / sum_{k <= T} eta_k
        = O( (f(x_0) - f_* + K_0)/(eta sqrt(T)) + K_1 eta (n + log(T)/(1 - b)) log(T)/sqrt(T) ),
with K_1 = sqrt(2) [ d U^2 Lg + d^(3/2) G U Lam Lg (1 + 2G) ] + Lg d U^2/2 + 4 d G Lam (G + G^2),
K_0 = O(eta d G U (n + log(T)/(1 - b)) + eta d G Lam (G + G^2) b/(1 - b)^2) (it depends on T through l), and Lam = 1/eps + G/(2 eps^2 sqrt(v_lo/2)), v_lo = (1 - b2) b2^(2n) n beta, the
Lipschitz constant of (m, v) -> m/(sqrt(v) + eps) on [-G, G] x [v_lo/2, inf). So the residual neighbourhood is reached at rate
T^(-1/4) up to logarithms, with no condition linking b2 to n and any b1 < 1.

Proof. Write u_k = mhat_k/(sqrt(vhat_k) + eps), so |u_kj| <= U and the descent lemma gives
    f(x_k) <= f(x_{k-1}) - eta_k grad f(x_{k-1}) . u_k + (Lg/2) eta_k^2 d U^2.                                   (1)
Lower bound on v. For k >= 2n the last 2n - 1 slots contain a whole epoch; along it the iterates move by at most
2n sqrt(d) U eta (each step is at most sqrt(d) U eta_s <= sqrt(d) U eta; eta_k would be wrong here, since the window's first
steps are larger than eta_k when k is close to 2n), so sum over that epoch of g_ij(x_.)^2 >= n beta - 4 n^2 G Lg sqrt(d) U eta >= n beta/2 for eta <= eta_0, and
v_kj >= v_lo/2; vhat >= v. (For n <= k < 2n epoch 1 lies wholly in the past with weight at least b2^(2n), so the floor
holds there too.)
Blocks and the frozen chain. With l as in the statement, the first 2l + 2 epochs are bounded crudely: there
-eta_k grad f(x_{k-1}) . u_k <= eta_k d G U, a total of at most 2 eta d G U sqrt((2l + 2) n), which is inside K_0 since
(2l + 2) n >= 1. (These epochs cannot be coupled with a bounded step ratio: for e = l + 1 the point tau is slot 1 and
eta_tau/eta_k is of order sqrt(l n).) Take an epoch e >= 2l + 2 with first slot E_e; then tau >= k/2 for every slot k of e,
so eta_tau <= sqrt(2) eta_k. Let tau = E_{e-l}
(an epoch start), y = x_{tau - 1}, and F the sigma-field of the permutations of the epochs before e - l, so y is F-measurable
and the permutations of epochs e - l, ..., e are independent of F and uniform. For a slot k of epoch e, let (mt_k, vt_k) be
the stationary filters at the frozen point y over the actual permutation stream, and ut_k = mt_k/(sqrt(vt_k) + eps). Since
|x_{j-1} - y| <= sqrt(d) U (l + 1) n eta_tau =: r for tau <= j <= k, the filters differ by
    |m_kj - mt_kj| <= Lg r + 2G b1^(k - tau) + G b1^k/(1 - b1^k),   |v_kj - vt_kj| <= 2G Lg r + 2G^2 b2^(k - tau) + G^2 b2^k/(1 - b2^k),
(slots before tau carry weight at most b^(k - tau); the last terms are the bias correction), and both v's are >= v_lo/2, so
|u_kj - ut_kj| <= Lam [ (1 + 2G) Lg r + 2(G + G^2) b^(ln) + (G + G^2) b^k/(1 - b^k) ]. With |grad f(x_{k-1}) - grad f(y)| <= Lg r,
    grad f(x_{k-1}) . u_k >= grad f(y) . ut_k - sqrt(d) U Lg r - d G max_j |u_kj - ut_kj|                               (2)
(the last term by Hoelder, |grad f(y)|_1 <= d G; with r = sqrt(d) U (l + 1) n eta_tau it is d^(3/2) G U Lam Lg (1 + 2G) (l + 1) n eta_tau
plus the b-terms).
Conditional mean. Replace the slots before tau in ut_k by an independent stationary past; this changes ut_k by at most
Lam 2(G + G^2) b^(ln). The result, given F, is the frozen drift at phase p(k) = k - E_e; summing over the n slots of epoch e
gives sum_p h_p(y) = n h(y) exactly (h is the phase average). Proposition 1 gives grad f(y) . h(y) >= W(y). So
    E[ sum_{k in e} grad f(y) . ut_k | F ] >= n W(y) - 2 n d G Lam (G + G^2) b^(ln).                                  (3)
Sum. Put eta_e = eta at the last slot of epoch e; the variation of eta_k inside a block costs at most n (eta_{E_e} - eta_e) d G U,
summable to O(eta n d G U). Summing (1) over k, inserting (2) and (3), using b^(ln) <= eta_T <= eta_k and r <= sqrt(d) U (l + 1) n eta_k
(eta_tau <= sqrt(2) eta_k for e >= 2l + 2, which is the sqrt(2) in K_1; the two b^(ln) pieces, one from (2) and one from (3), give
4 d G Lam (G + G^2) eta_k^2), and telescoping,
    sum_{e >= 2l + 2} n eta_e E W(y_e) <= f(x_0) - f_* + K_0 + K_1 (l + 1) n sum_{k <= T} eta_k^2,
with (l + 1) n <= 2n + log(1/eta_T)/(1 - b). If T is not a multiple of n, the last partial epoch has no phase sum and is bounded
crudely by n eta_T d G U, inside K_0. Divide by sum_{e >= 2l + 2} n eta_e, which is sum_k eta_k less at most 2 eta sqrt((2l + 3) n);
for T >= T_0 that loss is at most half of sum_k eta_k >= 2 eta (sqrt(T + 1) - 1), which is the factor 2 in B_T.
From norms to the bound. With a = ||grad f(y)||_phi, W(y) >= a^2 - a rho_* by Cauchy-Schwarz, so a <= rho_*/2 + sqrt(W(y) +
rho_*^2/4); Jensen on the weighted average gives avg E a <= rho_*/2 + sqrt(B_T + rho_*^2/4) <= rho_* + sqrt(B_T), and the
minimum over the y_e (which are iterates) is at most the average. With eta_k = eta/sqrt(k): sum eta_k >= 2 eta (sqrt(T + 1) - 1),
sum eta_k^2 <= eta^2 (1 + log T). QED.

Remarks. (a) This replaces the sketched tracking step of Theorem 2: the coupling at y = x_{tau-1} with fresh, F-independent epochs
is what the averaging hypothesis needed, and l epochs of lookback (about log(1/eta_T)/(n(1 - b)) of them) cost the log T/(1 - b)
factor. (b) (A2) excludes interpolation (all g_i -> 0 together), where the residual is a different question. (c) The constant
Lam carries b2^(2n) through v_lo; it enters the rate, not the residual. (d) The residual rho_* is the O(1 - b2) of Proposition 1,
attained in order by the scalar class, so the bound is sharp in (1 - b2) as T -> inf. (e) Status: proof written by its author.
A second pass by the author (21 Oct 05:4x) rechecked each step: the conditional mean (y and F are fixed by the permutations
before epoch e - l; epochs e - l..e together with an independent stationary past are an iid permutation stream at phase p, so
the conditional mean is h_p(y) and the phases average to h(y)), the filter differences, both lower bounds on v (v_k >= v_lo/2,
vt >= v_lo), Lam, the bias-correction sum (at most b/(1 - b)^2), and the Jensen step. Two fixes were made: the coupled epochs
now start at 2l + 2 rather than l + 1, because for l < e <= 2l + 1 the ratio eta_tau/eta_k is unbounded (the early epochs are
bounded crudely and fit in K_0, so the stated bound is unchanged), and a spurious sqrt(d) was removed from (2). A third pass
by the author (21 Oct 09:5x) rechecked the Cauchy-Schwarz step W >= a^2 - a rho_* (with W possibly negative, (a - rho_*/2)^2 >= 0
keeps the square root real), F-measurability of y = x_{tau-1}, the radius r, the choice of l (b^(ln) <= eta_T and
(l + 1) n <= 2n + log(1/eta_T)/(1 - b) since |log b| >= 1 - b), |mhat| <= G, and both v floors. One fix: the v floor's
movement bound used eta_k where the window's earliest steps can exceed it; with eta in its place the condition eta <= eta_0 is
exactly what is needed, so the statement is unchanged. Independent audit by claude-738954b6 (rows/T354/audit_738954b6/AUDIT.md, ee7575d3, 21 Oct): pass with corrections; C1 (T >= T_0 and the factor 2 in B_T), C2 (K_1: the sqrt(d) on the Lam term, the sqrt(2), 4 d G Lam (G + G^2)) and C3 (K_0 bias piece d, not sqrt(d)) are folded in above, with the stray factor 2 in (3) and the partial last epoch. The order of rate and residual is unchanged. The constants are crude.

### Empirical rate test (rate_check.py, 21 Oct 07:0x)
Same d = 2 nonconvex sum as drift_bound_check.py (n 16, seed 7, eps 1e-8, b1 0.9), 64 independent reshuffling streams,
eta_k = 0.05/sqrt(k), T = 2^22, E||grad f(x_k)||_phi at checkpoints 2^(q/4); files rc_b*_n16_run1.txt.

    b2      plateau (last 8 checkpoints)   plateau/(1 - b2)   (running min - plateau) ~ k^s, fitted on the transient
    0.99    6.85e-4 +- 6.5e-6              0.0685             s = -1.38 (k 64..3.9e4)
    0.995   3.40e-4 +- 5.8e-6              0.0680             s = -1.17 (k 64..2.2e5)
    0.999   9.3e-5  +- 1.2e-5              0.093              s = -0.96 (k 64..7.4e5); still falling at 2^22 (7.5e-5)

The plateau is linear in 1 - b2 to within one percent between 0.99 and 0.995, as Proposition 1 says. At 0.999 the run has not
reached its plateau by 2^22: the filter's tracking error eta_k/(1 - b2) is still 0.025 there, so 0.093 is an upper reading
of a ratio that the two longer-settled runs put near 0.068. Every fitted gap decays faster than T^(-1/4), so nothing here
contradicts Theorem 3. The test can only falsify the rate: T^(-1/4) is a worst-case bound and this problem's transient is
faster. The running min sits 1-2e-5 under the plateau at the end, the low bias of a minimum over many noisy checkpoints
(standard error 5e-6 per checkpoint). This is not a substitute for the independent audit (done since: see remark (e)).

Longer runs, T = 2^24 (rc_b0.999_n16_T24_run1.txt, rc_b0.998_n16_T24_run1.txt; same problem and streams):

    b2      plateau (last 9 checkpoints)   plateau/(1 - b2)   last two checkpoints (2^23, 2^24)   gap slope s
    0.998   1.365e-4 +- 3.3e-6             0.0682             1.324e-4, 1.344e-4  -> 0.066, 0.067   -1.00 (k 64..7.4e5)
    0.999   7.34e-5  +- 4.3e-6             0.0734             6.87e-5,  6.94e-5   -> 0.069, 0.069   -0.91 (k 64..1.8e6)

At 0.999 the last-eighth window still holds checkpoints from before the run settled (7.5e-5 at 2^22), which lifts the
printed plateau to 0.0734; the last two checkpoints are flat at 0.069. Across 1 - b2 from 0.01 to 0.001 the ratio
plateau/(1 - b2) stays in 0.066..0.073, so on this problem rho_* is linear in 1 - b2 with a constant near 0.068, and every
gap decays like k^-0.9 or faster. Nothing in the four runs contradicts Theorem 3; the audit has since passed (remark (e)).

