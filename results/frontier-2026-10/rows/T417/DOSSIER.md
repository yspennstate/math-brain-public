# T417 Does momentum accelerate stochastic gradient descent?

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
10:0x-10:1x; items marked 'recalled' were not re-read).

## STATEMENT
Repaired (per the audit of 2026-10-16T05:16, statement_ok NO): realizable streaming least squares y = <w*, x>, covariance H,
fourth-moment bound E[|x|^2 x x^T] <= R^2 H, one fresh sample (or a mini-batch of B) per step. Compare the heavy-ball recursion
w_(t+1) = w_t - eta g_t + beta (w_t - w_(t-1)) with plain SGD, each optimally tuned, for a stated family (Gaussian x with power-law
spectrum): the mean-square rate of heavy ball at optimal (eta, beta), last iterate, separating bias and variance terms and the effect
of B, and decide for which members it beats SGD. Rates depend on the fourth moments (the statistical condition number), not on H
alone. Nesterov momentum and the accelerated stochastic method (ASGD) of Jain et al. are different recursions and are kept apart.
Narrowed by the literature: on power-law random-features models, SGD with heavy-ball momentum at small batch has the same scaling
exponents as SGD, and in large-batch kernel regression Polyak momentum's critical learning rate is about min{1, B(1 - rho)} and it
enlarges the critical batch size; in high dimensions heavy ball accelerates to the full-batch rate once B exceeds an implicit
conditioning ratio.

## FRONTIER
- Kidambi, Netrapalli, Jain, Kakade arXiv:1803.05591: simple, generic instances where HB and NAG cannot outperform SGD at any
  parameter setting; their practical gains attributed to mini-batching; ASGD improves over all three.
- Jain, Kakade, Kidambi, Netrapalli, Sidford arXiv:1704.08227: an accelerated method for stochastic least squares robust to
  statistical errors.
- Lee, Cheng, Paquette, Paquette arXiv:2206.01029: SGD+M on least squares with samples and dimension large: dynamics converge to a
  deterministic Volterra equation; when the batch size exceeds the implicit conditioning ratio, linear convergence at rate
  O(1/sqrt(kappa)), matching full-batch momentum.
- Ferbach, Everett, Gidel, Paquette, Paquette arXiv:2505.16098: power-law random features, small batch: SGD-M has the same scaling-law
  exponents as SGD; dimension-adapted Nesterov acceleration (DANA) improves the exponents.
- Wang, Huang, Li, Wu arXiv:2609.02728: one-pass power-law kernel regression: critical learning rates eta_SGD ~ 1,
  eta_Polyak ~ min{1, B(1-rho)}, eta_Nesterov ~ min{1, B^beta (1-rho)} (beta > 1 the capacity exponent); risk scaling laws; a
  three-regime batch-size phase diagram; Polyak enlarges the critical batch size.

## ARCHITECTURE
For fresh-sample least squares the second moment E[(w_t - w*)(w_t - w*)^T] together with the cross term at lag one evolves by an
exact linear operator on a 3 x (d x d) block state (the audit's moment operator); its spectral radius at optimal (eta, beta) is the
asymptotic rate, and the transient on a power-law spectrum is read from the operator's resolvent in each eigendirection plus the
fourth-moment coupling term.

## FAILURE POINT
The fourth-moment coupling: for Gaussian x it is rank-one-plus-diagonal in the eigenbasis of H, which keeps the operator tractable;
for general x satisfying only the R^2 bound it is not, and the comparison with SGD can change sign.

## SHAPE
Days: Gaussian x, diagonal power-law H, batch B: the stability region in (eta, beta), the rate of the slowest mode at the optimum,
and the risk curve's exponent for HB versus SGD, recovering the equal-exponent statement of 2505.16098 at small B and the
B(1 - rho) critical rate of 2609.02728.

## OBSTRUCTION
A clean statement of 'beats SGD' when the exponents agree and only constants differ; and non-Gaussian fourth moments.

## TARGETS
1. Exact mean-square spectral radius of HB for Gaussian x with H = diag(j^(-alpha)), as a function of (eta, beta, B), and its
   minimum against SGD's.
2. The batch size at which optimally tuned HB first improves the risk exponent or constant over SGD, compared with 2609.02728.

### Result 2026-10-18 02:xx (agent A): Target 1, the exact mean-square radius (hb_ms_radius.py, hb_ms_radius_run1.txt)
For Gaussian x ~ N(0, H) with H diagonal, E[Hhat A Hhat] = H A H + (1/B)(H A H + tr(H A) H) keeps diagonal matrices diagonal, so the
diagonals of E e_t e_t', E e_t e_(t-1)' and E e_(t-1) e_(t-1)' evolve by an exact linear map on R^(3d):
    a' = kb^2 a + (eta^2/B)(h^2 a + (h.a) h) - 2 beta kb x + beta^2 c,   x' = kb a - beta x,   c' = a,     kb = 1 + beta - eta h,
whose spectral radius rho(eta, beta, B) is the mean-square contraction per step (beta = 0 is plain SGD). Started from a diagonal
second moment (e.g. e_0 = e_(-1) with independent coordinates, or w_0 = 0 and w* drawn isotropically) the diagonal stays closed.
Checks: (i) B -> infinity reproduces the deterministic per-mode radii (three (eta, beta) pairs, agreement to 1e-13) and SGD's
((kappa-1)/(kappa+1))^2; at Polyak's exact optimum the map has a Jordan block and its computed eigenvalue is off by 3e-4, which is
eigenvalue sensitivity, not an error. (ii) The noise term against a direct Monte Carlo of the recursion (hb_ms_mc_check.py,
hb_ms_mc_check_b1.txt; h = (1, 0.3, 0.05), 30 steps): B = 2 and 4 agree to 0.2 and 0.7 standard errors; at B = 1, five seeds of
4e5 runs give 0.3115 +- 0.0032 against the map's 0.3103, with single seeds spread 0.305-0.324 (the product of random matrices has
a heavy upper tail, so one seed's standard error understates the spread); T = 1, 2, 5, 10 agree within 1 standard error.
Optimal radii over a (eta, beta) grid, d = 100, h_j = j^(-alpha):

    alpha 1.5 (kappa 1e3, tr H 2.41)       SGD 1 - rho     HB 1 - rho     speedup   HB beta at the optimum
      B = 1                                 1.00e-3         1.18e-3        1.18      0.930
      B = 10                                3.25e-3         1.04e-2        3.21      0.916
      B = 100                               3.84e-3         4.96e-2        12.9      0.916
      B = 1000                              3.92e-3         9.03e-2        23.1      0.900
      B = 1e5                               3.92e-3         1.00e-1        25.5      0.881    (deterministic limit; sqrt(kappa) = 31.6,
                                                                                               the grid misses the defective optimum)

    alpha 2.0 (kappa 1e4, tr H 1.64)       SGD 1 - rho     HB 1 - rho     speedup   HB beta at the optimum
      B = 1                                 1.20e-4         1.63e-4        1.36      0.976
      B = 10                                3.26e-4         1.53e-3        4.68      0.976
      B = 100                               3.92e-4         9.69e-3        24.7      0.976
      B = 1000                              3.92e-4         2.45e-2        62.5      0.965
      B = 1e5                               3.92e-4         3.44e-2        87.8      0.965    (sqrt(kappa) = 100)

Reading: at B = 1 heavy ball buys a constant (1.18 here), which is the instance-level form of Kidambi et al. (1803.05591); the
speedup grows with B and reaches half its deterministic value between B = 100 and 1000. A heuristic for the crossover: the noise
term (eta^2/B) tr(H) h competes with the deterministic contraction once eta is pushed to order 1/h_max and the momentum
amplifies noise by 1/(1 - beta) ~ sqrt(kappa), giving B* ~ sqrt(kappa) tr(H)/h_max (76 for alpha 1.5). This is a heuristic for
the order of magnitude, compared with the data below, not a derivation.
The data: half the deterministic speedup is reached near B = 100 for alpha 1.5 (heuristic 76) and between B = 100 and 1000 for
alpha 2 (heuristic 164); SGD itself saturates by B ~ 100 in both, since its noise term is already small at its own optimal step.
Open for Target 2: a proof of the B* ~ sqrt(kappa) tr(H)/h_max scaling from the 3x3 per-mode block plus the rank-one coupling
(h.a) h, which is a secular equation in one scalar.

### Result 2026-10-18 02:1x (agent A): Target 2, the secular equation and the exact stability edge (hb_ms_secular.py, _run1.txt)
Each mode contributes a 3x3 block M_j and the modes couple only through the rank-one term (eta^2/B) h h' on the a-coordinates. An
eigenvalue mu of the full map that is not an eigenvalue of any block therefore solves
    1 = (eta^2/B) sum_j h_j^2 mu (mu + beta) / p_j(mu),     p_j(mu) = det(mu I - M_j)
(the (1,1) cofactor of M_j - mu is mu (mu + beta)). At mu = 1, with r_1 r_2 = beta and r_1 + r_2 = 1 + beta - eta h_j the roots of
the deterministic per-mode recursion, p_j(1) = (1 - beta) eta h_j (2(1 + beta) - eta h_j) - (eta^2 h_j^2 / B)(1 + beta), so the map is
mean-square stable exactly when every bracket below is positive and
    S = (eta/B) sum_j (1 + beta) h_j / [ (1 - beta)(2(1 + beta) - eta h_j) - (1 + beta) eta h_j / B ]  <  1.
Checks on 3,000 random (h, eta, beta, B): the leading real eigenvalue solves the secular equation (largest residual 1.2e-6, the
equation has poles nearby), and S < 1 agrees with rho < 1 at every point. beta = 0 recovers the familiar SGD condition
(eta/B) sum_j h_j / (2 - eta h_j (1 + 1/B)) < 1.
Where the crossover comes from. When eta h_j is small against 2(1 - beta), S ~ eta tr(H) / (2 B (1 - beta)), so noise caps the
effective step eta/(1 - beta) at about 2B/tr(H). The deterministic optimum wants (1 - beta) ~ 1/sqrt(kappa) at eta ~ 1/h_max, i.e.
an effective step of order sqrt(kappa)/h_max, so the full speedup needs B >~ sqrt(kappa) tr(H)/h_max and below that the speedup is
about the ratio of allowed effective steps, of order B h_max / tr(H). With constant 0.75 the interpolation
1/(1/(0.75 B h_max/tr H) + 1/sqrt(kappa)) gives 4.4 / 31 / 82 at alpha = 2, B = 10 / 100 / 1000 against the measured 4.7 / 24.7 / 62.5 -
the right order, not a fit. A sharp statement needs the rate (mu just below 1), not just the edge; the secular equation is the
tool, and that asymptotic is the next step.

### Check 2026-10-18 03:0x (agent A): does the speedup collapse on x = B h_max / (tr H sqrt(kappa))? (hb_ms_radius_run2_collapse.txt)
Four spectra (power law alpha, d), optimal-tuned speedup S(B) = (1 - rho_HB)/(1 - rho_SGD), divided by sqrt(kappa):

    spectrum (kappa, tr H)        B=10: x / S/sqrt(k)    B=100          B=1000         B=1e5
    a=2.0 d=100 (1e4, 1.635)      0.061 / 0.047          0.61 / 0.247   6.1 / 0.625    - / 0.878
    a=2.0 d=50  (2500, 1.625)     0.123 / 0.087          1.23 / 0.358   12.3 / 0.706   - / 0.893
    a=1.5 d=100 (1000, 2.413)     0.131 / 0.102          1.31 / 0.409   13.1 / 0.730   - / 0.808
    a=1.0 d=100 (100, 5.187)      0.193 / 0.145          1.93 / 0.471   19.3 / 0.707   - / 0.746

Every column is monotone in x and the four curves fall within about 15 pct of one another at matched x, with S/sqrt(kappa) ~ 0.75 x
for small x and saturating past x ~ 10: the crossover batch is B* ~ sqrt(kappa) tr H / h_max, as the stability edge predicted. The
collapse is not exact and the saturation level differs (0.75-0.89), partly because (eta, beta) are tuned on a grid (the B = 1e5 beta
0.9654 against the deterministic optimum 0.9608 at kappa 1e4). Status: numerical support for the scaling only; a proof would come from
the secular equation with mu = 1 - c/sqrt(kappa) inserted, which is the next step.

### Result 2026-10-18 03:2x (agent A): an upper bound on the speedup, with proof (hb_speedup_bound_check.py, _run1.txt)
Model: the mean-square map of hb_ms_secular.full (modes h_1 >= ... >= h_d > 0, batch B, coupling (eta^2/B)(h h' + diag h^2)).
kappa = h_max/h_min. rho_HB = spectral radius of the map at (eta, beta, B); rho_SGD the same at beta = 0.

Lemma A. Every mean-square-stable heavy-ball setting has 1 - rho_HB <= min(8 B h_min / tr H, 4/sqrt(kappa)).
Proof. Jensen (E xx' >= Ex Ex') gives rho_HB >= q^2, q = spectral radius of the mean recursion; per mode the roots of
p_h(r) = r^2 - (1 + beta - eta h) r + beta, with r_1 r_2 = beta and (1 - r_1)(1 - r_2) = p_h(1) = eta h.
(i) Noise part. Each bracket of S is at most 2(1 - beta)(1 + beta), so S < 1 forces eta <= 2B(1 - beta)/tr H. Take h = h_min, s = eta h_min.
If the roots are complex, |r|^2 = beta and s > (1 - sqrt beta)^2, so 1 - beta <= 2(1 - sqrt beta) < 2 sqrt s <= 2 sqrt(2B(1 - beta)h_min/tr H),
i.e. 1 - beta < 8 B h_min/tr H, and 1 - rho_HB <= 1 - beta. If real, r_min <= sqrt beta, so 1 - r_min >= (1 - beta)/2 and
1 - r_max = s/(1 - r_min) <= 2s/(1 - beta) <= 4B h_min/tr H; then 1 - rho_HB <= 1 - r_max^2 <= 2(1 - r_max) <= 8 B h_min/tr H.
(ii) Deterministic part. If every root has modulus <= q < 1 then p_h(-q) = (q + r_1)(q + r_2) >= 0 and p_h(q) >= 0 for every mode;
at h_max the first gives eta h_max <= (1 + q)(q + beta)/q, at h_min the second gives eta h_min >= (1 - q)(q - beta)/q, and beta <= q^2.
Dividing, kappa <= (1 + q)(q + beta)/((1 - q)(q - beta)) <= ((1 + q)/(1 - q))^2 (the middle factor increases in beta), so
q >= (sqrt kappa - 1)/(sqrt kappa + 1) and 1 - rho_HB <= 1 - q^2 = 4 sqrt kappa/(sqrt kappa + 1)^2 < 4/sqrt kappa.  []

Lemma B. Plain SGD with eta_0 = min(B/(4 tr H), 1/(2 h_max)) has 1 - rho_SGD >= (3/4) eta_0 h_min.
Proof. At beta = 0 the map is block triangular and its radius is that of the nonnegative block on the second moments m_j >= 0:
m_j' = (1 - eta h_j)^2 m_j + (eta^2/B)(h_j^2 m_j + h_j sum_k h_k m_k). Summing, sum m_j' = sum_j m_j [1 - eta h_j (2 - eta h_j (1 + 1/B)
- eta tr H/B)] <= (1 - (3/4) eta_0 h_min) sum m_j, since eta_0 h_j (1 + 1/B) <= 1 and eta_0 tr H/B <= 1/4. A nonnegative matrix that
shrinks the l1 norm of every nonnegative vector by a factor c has radius <= c.  []

Theorem (upper bound, both lemmas). The best heavy-ball rate over the best SGD rate, S(B) = (1 - rho_HB*)/(1 - rho_SGD*), satisfies
    S(B) <= 128/3                                   for B <= 2 tr H/h_max,
    S(B) <= min((64/3) B h_max/tr H, (32/3) sqrt kappa)  for B >= 2 tr H/h_max,
so momentum buys at most a constant below B ~ tr H/h_max, at most O(B h_max/tr H) in between, and at most O(sqrt kappa) past
B* ~ sqrt(kappa) tr H/h_max: the crossover found numerically is a theorem from above. Random check on 3,000 points (d 2-30,
spectra over three decades, B 1-1e4): Lemma A's ratio at most 0.78 of the bound over 1,357 stable heavy-ball points, Lemma B's at
least 2.30 times its bound. The constants are loose (measured S/sqrt kappa saturates at 0.75-0.89, the bound says 32/3).
Open: the matching lower bound (that tuned momentum attains c min(max(1, B h_max/tr H), sqrt kappa)); the collapse table above is the
numerical evidence for it, not a proof. Not audited by a second agent.

### Result 2026-10-18 03:4x (agent A): the matching lower bound, by an explicit choice (hb_speedup_lower_check.py, _run1.txt)
SGD ceiling (proved). Jensen gives rho_SGD >= (1 - eta h_min)^2, so 1 - rho_SGD <= 2 eta h_min; S < 1 at beta = 0 forces eta < 2B/tr H,
and the mean recursion forces eta < 2/h_max. Hence 1 - rho_SGD* <= 4 h_min min(B/tr H, 1/h_max).
Heavy-ball choice. delta = min(2/sqrt(kappa), 4 c B h_min/tr H), sqrt(beta) = 1 - delta/2, eta = delta^2/(4 h_min): critical damping at
h_min (so every mode is underdamped with root modulus sqrt(beta)), eta h_max <= 1, and effective step eta/(1 - beta) about
delta/(4 h_min) <= c B/tr H. Measured on 2,000 random points (d 2-30, spectra over three decades, B 1-1e4):
    c = 1/4: every point mean-square stable, (1 - rho_HB)/delta >= 0.2485, and
             speedup >= 0.103 min(max(1, B h_max/tr H), sqrt(kappa))
    c = 1/8: (1 - rho_HB)/delta >= 0.447, speedup >= 0.067 x the same.
With the upper bound above this gives, numerically, S(B) = Theta(min(max(1, B h_max/tr H), sqrt kappa)), constants between about
0.1 and 32/3. Proved: the upper bound and the SGD ceiling. Not proved: that the explicit choice keeps 1 - rho_HB >= c' delta once the
noise couples the modes (the mean-square radius with the rank-one coupling); the route is the secular equation on the real axis plus
a bound on the complex eigenvalues, or a Lyapunov function on the second moments as in Jain-Kakade-Kidambi-Netrapalli-Sidford (2018),
whose accelerated method is a different scheme. Not audited by a second agent.

### 04:0x the heavy-ball rate with noise, reduced to a two-variable inequality (hb_lower_proof_scan.py, hb_lower_scan2.py, runs)
(1) On 1,500 random points the mean-square radius equals max(largest block radius, largest real root of the secular function above it)
to 1e-6. Not proved; the expected route is positivity of the renewal kernel (the impulse responses enter squared), which makes the top
eigenvalue outside the blocks real.
(2) Explicit choice, c = 1/4. Then eta^2 h^2/B <= c delta eta h, and with x = eta h, s = x/delta^2 in [1/4, 1/delta^2], the per-mode term is
(eta/B) h R/delta with R = mu (mu + beta) x delta / p(mu), so the secular sum is at most sup R * eta tr H/(B delta) <= c sup R. Scanned
sup R over mu' >= 1 - delta/4 (worst diagonal noise): 1.90 at delta = 0.5, 1.75 at 0.2, 1.69 at 0.03, 1.684 for delta <= 0.003; R falls
monotonically in mu' (0.80 at mu' = 1, 0.36 at 1 + delta). Block radii stay below 1 - delta/4 (ratio at most 0.9997).
So, granted (1), every secular root lies below 1 - delta/4 and rho_HB <= 1 - delta/4: 1 - rho_HB >= delta/4, which is the measured
0.2485 delta to three figures, the bound is tight. What is left for a proof: (1) and the scalar inequality R(delta, s, mu') <= 2 on
the scanned domain (two variables plus mu'; interval arithmetic or a hand bound on p(mu)). Status: numerical evidence, not a proof.

Note 04:1x on the upper bound's step "S < 1 forces eta <= 2B(1 - beta)/tr H": stability does force S < 1 without the unproved
characterization (1). A secular root mu outside the block spectra is an eigenvalue of the map (the rank-one eigenvector
v_j = (mu I - M_j)^{-1} e_1 h_j). Just above the largest real root of a monic cubic p_j the secular function tends to -infinity, and it
tends to 1 at infinity, so a block with a real root >= 1 would put a map eigenvalue above 1. Hence rho < 1 gives p_j(1) > 0 for every j
and f(1) = 1 - S > 0. Lemma A is therefore complete as written.

### 04:3x step (1) proved in the direction needed: rho <= max(block radii, mu*), mu* the top real secular root
Per mode, (a, b, c) = (E x_t^2, E x_t x_{t-1}, E x_{t-1}^2) evolves by M_j, which is the second-moment map of
x_{t+1} = (k_j + zeta) x_t - beta x_{t-1} with E zeta = 0, E zeta^2 = eta^2 h_j^2/B; it maps the cone of valid states ([[a, b], [b, c]] PSD)
into itself, and the whole map does too. The modes couple only through u_t = sum_k h_k a_k(t):
    a_j(t) = [M_j^t s_j(0)]_1 + (eta^2/B) h_j sum_{s<t} [M_j^{t-s-1} e_1]_1 u_s,
    u_t = u_det(t) + sum_{s<t} K(t-s-1) u_s,   K(tau) = (eta^2/B) sum_j h_j^2 [M_j^tau e_1]_1 >= 0,
the sign because e_1 is a valid state (unit variance now, none before) and [.]_1 is a variance. With generating functions,
U(z) = U_det(z)/(1 - z K^(z)), and z K^(z) at z = 1/mu is (eta^2/B) sum_j h_j^2 mu (mu + beta)/p_j(mu), the secular sum. U_det is analytic for
|z| < 1/(largest block radius). For real 0 < z < z* = 1/mu* the denominator is positive, and for complex |z| = r < z* the nonnegative
coefficients give |z K^(z)| <= r K^(r) < 1. So U is analytic on |z| < min(1/blk, z*), u_t = O((max(blk, mu*) + eps)^t), and a_j, b_j, c_j follow
(convolutions with the block propagators; b by Cauchy-Schwarz). A cone-preserving map whose cone spans the space has its spectral radius
equal to its growth rate on the cone, so rho <= max(blk, mu*). (That rho equals this maximum, as seen on 1,500 points, is not needed.)
What remains for the lower bound 1 - rho_HB >= delta/4 is the scalar inequality only: sup R(delta, s, mu') <= 2 for mu' >= 1 - delta/4,
which with c = 1/4 puts the secular sum below 1/2 there. Scanned (hb_lower_scan2_run1.txt): 1.90 at most. Not yet a proof:
that sup is a grid scan, not a certified bound.

### 04:2x the lower bound is proved: S(B) = Theta(min(max(1, B h_max/tr H), sqrt kappa))  (hb_lower_endpoint_proof.py, _run1.txt)
Take kappa >= 4 and delta = min(2/sqrt kappa, B h_min/tr H) (so delta <= 1), sqrt beta = 1 - delta/2, eta = delta^2/(4 h_min), mu0 = 1 - delta/4.
1. Ranges. x_j = eta h_j lies in [delta^2/4, delta^2 kappa/4], inside [delta^2/4, 1]. The diagonal noise eta^2 h_j^2/B = x_j (eta h_j/B) is at most
   x_j delta/4, because eta h_max/B = delta^2 kappa/(4B) <= delta/4 when delta <= B/kappa, which holds since B h_min/tr H <= B/kappa.
2. Monotonicity. The secular sum at z = 1/mu is z K^(z) with K >= 0 (04:1x section), so it increases in z and decreases in mu above the
   block radii; it is enough to show it is below 1 at mu0. Larger diagonal noise eps lowers p(mu) = p_det(mu) - eps mu (mu + beta), so the
   worst case is eps = delta x/4.
3. The bound at mu0. The secular sum is at most (eta tr H/(B delta)) sup_j R_j <= (1/4) sup R, with R = mu0 (mu0 + beta) x delta / p(mu0), so R < 4 is
   enough. R < 4 is F(delta, x) = p(mu0) - mu0 (mu0 + beta) x delta/4 > 0. F is concave in x (second derivative -2 mu0 (mu0 - beta) < 0, with
   mu0 - beta = delta (3 - delta)/4 > 0), so only x = delta^2/4 and x = 1 need checking:
     F(delta, delta^2/4) = -delta^3 (delta^3 - 9 delta^2 + 26 delta - 22)/128,
     F(delta, 1) = -delta (delta^6 - 11 delta^5 + 40 delta^4 - 20 delta^3 - 212 delta^2 + 496 delta - 320)/256.
   Their smallest positive real roots are 1.4786 and 1.2868 (exact real-root isolation), and both are positive at delta = 1/2 and at 1,
   so F > 0 on (0, 1] at both ends. F > 0 also gives p(mu0) > 0, so every block radius is below mu0 (single-block version of the same renewal
   argument; the deterministic radius is beta < mu0).
4. Hence rho_HB <= 1 - delta/4. Against the SGD ceiling 1 - rho_SGD* <= 4 h_min min(B/tr H, 1/h_max):
     B <= tr H/h_max:  delta = B h_min/tr H, so S >= 1/16;
     B >  tr H/h_max:  S >= delta kappa/16 = min(2 sqrt kappa, B h_max/tr H)/16.
   With the upper bound (03:2x): (1/16) min(max(1, B h_max/tr H), 2 sqrt kappa) <= S(B) <= (64/3) min(max(2, B h_max/tr H), sqrt kappa/2)
   (for kappa >= 4). Numerically the explicit choice gets 1 - rho = 0.2485 delta, so step 3's constant is close to tight. Grid maxima of R
   over x: 2.59 at delta = 1, 1.90 at 1/2, 1.716 at 0.1, 1.685 at 0.001.
STATUS: proved, by hand plus exact polynomial root isolation; the renewal step is the 04:1x section, independently audited by
agent B (58169b3f, audit/AUDIT.md). What is still open: the sharp constants, and whether a time-varying or
tuned-per-B schedule changes the picture (not this row's question).

Second-agent check of the 04:2x proof: agent B, independently, 60e6928b (audit/AUDIT.md, "matching lower bound"):
step 1 and step 3 agree (same endpoint polynomials, first root 1.479; the x = 1 polynomial has no root in [0, 1]; concavity coefficient
-16 (4 - delta)(3 - delta)). Their route differs in three places: monotonicity in mu proved directly from k^2 <= 4 beta, delta capped at 1 so
kappa < 4 is covered too, and rho <= mu0 from the weighted renewal sum without Pringsheim. Their 3,000-point numerics give (1 - rho)/delta >= 0.334.
ROW STATUS: the T417 question (does heavy ball beat SGD in mean square at batch B, and by how much) is answered up to constants:
S(B) = Theta(min(max(1, B h_max/tr H), sqrt kappa)), proved, two agents.
