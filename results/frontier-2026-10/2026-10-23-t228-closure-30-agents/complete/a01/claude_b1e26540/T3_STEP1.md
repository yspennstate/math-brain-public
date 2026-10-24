# T228 target 3, step 1: existence, uniqueness and moments of the stationary law in R^d

claude-b1e26540, 22 Oct 2026 03:4x. Status: draft for review. Setup and notation: T3_SETUP.md. Numbers:
t3_step1_check.py / t3_step1_check_run1.txt.

## Hypotheses
Class (A) as in w688_target1/proofs/T228_A_v1.md: sigma(z) = z + phi(z) with r := sup|phi'| < 1, H := sup|phi| < oo,
D := sup|z phi'(z)| < oo. Put m = 1 - r > 0 and L = 1 + r, so m <= sigma' <= L. Data: a_i ~ N(0, I_d), eps_i ~ N(0, s^2)
with s > 0, y_i = sigma(a_i.x*) + eps_i, fresh and independent at every step; b >= 1, eta > 0, c = eta/b, d >= 1.
    Psi(x) = x + c sum_{i<=b} u_i a_i,   u_i = sigma'(a_i.x) (y_i - sigma(a_i.x)),
    Psi(x) = M x + R(x),   M = I - c sum a_i a_i^T,
    |R(x)| <= B := c sum |a_i| (D + L(2H + |a_i||x*| + |eps_i|))      (independent of x; all moments finite).
xi has the law of Lemma R: xi^2 = (1 - cX)^2 + c^2 X Y, X ~ chi2_b, Y ~ chi2_{d-1} independent, and |M u| =_d xi for
every unit u. h(p) := E xi^p.

(S_d)  gamma := E log xi < 0.

## Lemma 1 (the index alpha)
E|log xi| < oo, h is finite and log-convex on [0, oo), h(0) = 1, h'(0+) = gamma, and h(p) -> oo. Under (S_d) there is a
unique alpha > 0 with h(alpha) = 1, and h(p) < 1 for 0 < p < alpha.

Proof. xi <= 1 + cX + c sqrt(XY), so every positive moment is finite. For the lower tail, P(xi < t) <= P(|1 - cX| < t)
<= C_b t, since chi2_b has a density bounded near 1/c > 0; hence E log^- xi < oo. Log-convexity is Hoelder; the
derivative at 0 is dominated convergence (|xi^p - 1|/p <= |log xi| (1 + xi) for p <= 1). h(p) >= 2^p P(xi > 2) -> oo
because P(xi > 2) > 0. A log-convex function equal to 1 at 0, with negative slope there and tending to infinity,
crosses 1 exactly once more, and lies below 1 between. QED

## Lemma 2 (drift)
Fix p in (0, alpha) and V(x) = 1 + |x|^p. There are gamma_p < 1 and K_p < oo with
    E V(Psi(x)) <= gamma_p V(x) + K_p     for all x.

Proof. |Psi(x)| <= |Mx| + B, and E|Mx|^p = h(p) |x|^p by Lemma R.
p <= 1: (u + v)^p <= u^p + v^p gives E|Psi(x)|^p <= h(p)|x|^p + E B^p; take gamma_p = h(p), K_p = 1 - h(p) + E B^p.
p > 1: Minkowski in L^p gives (E|Psi(x)|^p)^(1/p) <= h(p)^(1/p) |x| + beta, beta = (E B^p)^(1/p). For delta > 0,
(u + v)^p <= (1+delta)^(p-1) u^p + (1 + 1/delta)^(p-1) v^p; choose delta with gamma_p := (1+delta)^(p-1) h(p) < 1.
No independence between M and B is used. QED

## Lemma 3 (one-step minorization on every ball, with the minorizing measure on the ball itself)
For every R > 0 there is eps_R > 0 such that for all |x| <= R and all Borel A,
    P(x, A) >= eps_R Leb(A cap B_R),     B_R = {|w| <= R}.

The rank of the noise is not an issue: one sample already moves Psi(x) along a Gaussian direction a_1, and the radius
along it is spread by eps_1. This replaces the k-step plan of T3_SETUP.md (kb >= d is not needed).

Proof. Write Psi(x) = x + S + c u_1 a_1 with S = c sum_{i>=2} u_i a_i (S = 0 when b = 1); S is independent of
(a_1, eps_1). Let G = {|a_i| <= 1, |eps_i| <= s for 2 <= i <= b}, of probability p_G > 0. Since |sigma(p) - sigma(q)|
<= L|p - q|, |u_i| <= L(L|a_i||x - x*| + |eps_i|), so on G, |S| <= S_R := c(b-1) L(L(R + |x*|) + s).
Polar coordinates for a_1: a_1 = rho_a theta with rho_a = |a_1| and theta uniform on S^{d-1} (normalized surface
measure omega), independent. Given (rho_a, theta) = (q, theta), the scalar t := c q u_1 is affine in eps_1 with slope
c q sigma'(q theta.x) != 0, so t is Gaussian with
    mean mu = c q sigma'(q theta.x)(sigma(q theta.x*) - sigma(q theta.x)),   sd tau = c q sigma'(q theta.x) s.
For q in [1, 2] and |x| <= R: |mu| <= 4 c L^2 (R + |x*|) =: mu_R and tau in [c m s, 2 c L s]. Hence for |t| <= T the
conditional density of t is at least
    g_lo(T) := (2 c L s sqrt(2 pi))^(-1) exp(-(T + mu_R)^2 / (2 c^2 m^2 s^2)) > 0.
For d >= 2 the map (theta, t) -> v = t theta is two-to-one from S^{d-1} x (R \ {0}) onto R^d \ {0}, with
Leb(dv) = |S^{d-1}| |t|^(d-1) dt omega(d theta) on each sheet. Keeping only the sheet t > 0, the density of v given
rho_a = q is at least g(|v| ; theta = v/|v|) / (|S^{d-1}| |v|^(d-1)), where g(. ; theta) is the conditional density of t.
(d = 1 is the scalar case of T228_A_v1: v = t theta with theta = +-1, and the same bound holds with |S^0| = 2, exponent 0.)
Now take |w| <= R. Then v := w - x - S satisfies |v| <= T_R := 2R + S_R on G, so the density of Psi(x) at w is at least
    eps_R := p_G P(1 <= |a_1| <= 2) g_lo(T_R) / (|S^{d-1}| T_R^(d-1)) > 0,
uniformly in |x| <= R and |w| <= R. Measurability of the conditional densities is that of Gaussian kernels composed with
continuous maps; no continuity of phi' is used (only the bounds m <= sigma' <= L). QED

## Theorem 1 (step 1 of target 3)
Under class (A), s > 0 and (S_d), the chain x_{k+1} = Psi_k(x_k) on R^d has a unique invariant probability pi, and for
every p in (0, alpha):
  (i)  E_pi |x|^p < oo;
  (ii) there are C, rho < 1 with sup_{|f| <= 1 + |.|^p} |E_x f(x_n) - pi(f)| <= C (1 + |x|^p) rho^n;
  (iii) pi has a density bounded below by a positive constant on every ball; in particular supp pi = R^d.

Proof. Lemma 2 gives the drift PV <= gamma_p V + K_p. Every sublevel set {V <= R'} is a ball, and by Lemma 3 it carries
a minorization by a multiple of Lebesgue measure on that ball, for every R'. These are Assumptions 1 and 2 of
Hairer-Mattingly, "Yet another look at Harris' ergodic theorem for Markov chains" (Progr. Probab. 63, 2011, 109-117),
whose Theorem 1.2 gives a unique invariant measure and geometric convergence in the V-weighted norm, i.e. (ii); (i)
follows by letting n -> oo in P^n V <= gamma_p^n V + K_p/(1 - gamma_p). The same conclusion is Meyn-Tweedie (2nd ed.)
Theorem 15.0.1 (the ball is small, so petite; the minorizing measure charges the ball, so the chain is strongly
aperiodic). For (iii): pi = pi P >= int_{B_R} pi(dx) P(x, .) >= pi(B_R) eps_R Leb(. cap B_R), and pi(B_R) > 0 for R
large. QED

Citation, read on the page (22 Oct 04:4x) in arXiv:0810.2777v1, p.1-2 (src_hm/HM.pdf, sha256 2ea9915ae59ee286):
Assumption 1 is PV <= gamma V + K with V >= 0, gamma in (0,1); Assumption 2 is inf_(x in C) P(x, .) >= alpha nu(.) for a
probability measure nu and some alpha in (0,1), with C = {V <= R} for some R > 2K/(1 - gamma); Theorem 1.2 gives a unique
invariant measure mu and |P^n phi - mu(phi)| <= C rho^n |phi - mu(phi)| in the norm sup |phi|/(1 + V). Ours: V = 1 + |x|^p,
K = K_p, gamma = gamma_p; {V <= R} is the ball of radius (R - 1)^(1/p), and Lemma 3 on that ball gives Assumption 2 with
nu the normalized Lebesgue measure on the ball and alpha = eps Leb(ball) (shrink eps if needed so alpha < 1). Since
1 + V <= 2V, the bound in their norm gives (ii) as stated. The Meyn-Tweedie reference is an alternative and is not relied on.

## What this feeds
Step 2 (Goldie on |x|) needs E_pi |x|^p < oo for p < alpha: that is (i). Step 3 (c0 > 0) needs unbounded support and a
positive density: that is (iii).

## Numbers (t3_step1_check_run1.txt, 4 million draws each)
(d, b, eta) = (3, 2, 0.9): gamma = -0.044, alpha = 0.358, h < 1 on (0, alpha), E xi^2 = 1.6295 against 1.6300.
(2, 1, 0.8): gamma = -0.065, alpha = 0.400, E xi^2 = 1.9624 against 1.9600.
(5, 4, 1.0): gamma = +0.008, so (S_d) FAILS although eta exceeds the alpha < 2 threshold 2b/(b+d+1) = 0.8; the
alpha < 2 window for (d, b) = (5, 4) ends below eta = 1. Theorem 1 does not apply there, as it should not.
