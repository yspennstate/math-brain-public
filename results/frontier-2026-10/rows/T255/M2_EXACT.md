# T255: the noise of the attention SDE, PD preservation, and m = 2 settled (agent Q, 16 Oct 14:5x, written 17 Oct 19:0x)

Status: derivation checked against the dossier's measured ray variances; m = 2 law checked against the exact chain
(m2_check.py, results below when they land). Not yet independently audited.

## 1. The SDE written out
Theorem 4.2 of 2306.17759 gives dV = b(V) dt + Sigma(V)^(1/2) dB. Expanding one layer of Eq. 1 + Eq. 9 to order 1/sqrt n
(X = L Q, Q Q^T = n I, V = L L^T; Softmax(Z)_ij = (1 + (Z P)_ij)/m + O(|Z|^2), P = I - 11^T/m) gives the martingale part
in congruence form:

    dV = b(V) dt + L dGamma L^T,   dGamma = sqrt(c) dH + k (dN K + K dN^T),   K = L^T P L,
    c = gamma^2 (2 - gamma^2),  k = gamma^2/(m tau0),

H a GOE Brownian motion (diagonal variance 2, off-diagonal 1), N an m x m matrix of independent Brownian motions, H and N
independent (H from W^V, N from W^Q W^K). Check: on V = a I + e 11^T this gives Var rate of a = tr(PV)/(m-1) equal to
2 c a^2/(m-1) + 4 gamma^4 a^4/(tau0^2 m^2 (m-1)), the dossier's formula, which ray_check.py matched against the chain.
The drift, from the paper's formula (sdrift.py, MC-checked), simplifies to

    b(V) = (gamma^2/tau0^2) [ V |W|_F^2/m^2 + (1/2m)(v (V D)^T + (V D) v^T) ],
    W = P V P,  v = diag V,  D = diag W - (tr W/m) 1   (so 1^T D = 0).

## 2. Positive definiteness is never lost before explosion (every m)
d log det V = tr(V^{-1} b) dt + tr(dGamma) - (1/2) tr(dGamma^2), and tr(V^{-1} b) = (gamma^2/tau0^2)[|W|^2/m + D^T v/m]
(the term tr(V^{-1} v (VD)^T) = D^T v has no inverse left). All coefficients are polynomial in |V|. So on [0, T_r]
(T_r = exit of {|V| < r}) log det V is a semimartingale with bounded coefficients and cannot reach -infinity:
the solution stays positive definite up to its explosion time. The only way the global question fails is |V| -> infinity.

## 3. The centred block W = PVP
P L = W^{1/2} U with U orthogonal (polar form), and U dN U^T, U dH U^T are again an iid matrix BM and a GOE BM (Levy).
So the noise of W depends on W alone:
    dW_noise = sqrt(c) W^{1/2} dH' W^{1/2} + k (W^{1/2} dN' W^{1/2} W + W W^{1/2} dN'^T W^{1/2}).
Its drift is, with r = P V 1 (the cross term between the centred tokens and their mean),
    P b P = (gamma^2/tau0^2) [ W |W|^2/m^2 + (1/2m)(D (WD)^T + WD D^T) + (1/m^2)(r (WD)^T + WD r^T) ]
(Pv = D + (2/m) r). The r-terms are the only coupling of W to the rest of V. Checked numerically (t2.py): for m = 3, 4,
P b P changes with r at fixed W; for m = 2 it does not.

## 4. m = 2 is a one-dimensional diffusion, and it explodes with positive probability iff gamma^2 < 1/2
For m = 2, W = w e e^T with e = (1,-1)/sqrt2, w = tr(PV) = (V11 + V22 - 2 V12)/2, and diag W = (w/2, w/2), so D = 0 and
the r-coupling vanishes. Then exactly

    dw = kappa w^3 dt + sqrt(2 c w^2 + 4 k^2 w^4) dbeta,   kappa = gamma^2/(4 tau0^2),  4 k^2 = gamma^4/tau0^2,

an autonomous diffusion on (0, inf) driven by one Brownian motion beta. Its scale density is exact:
    s'(y) = (2c + 4k^2 y^2)^(-1/(4 gamma^2)),   s'(y) ~ y^(-1/(2 gamma^2)) at infinity, s' bounded near 0.
- 0 is not reached (near 0 it is a geometric Brownian motion with drift -c in log w); s(0+) is finite, so w -> 0 on the event of no explosion.
- If gamma^2 < 1/2: s(inf) < inf, and Feller's v(inf) < inf (s' times int 2/(s' sigma^2) is O(y^-3) for gamma^2 < 1/6,
  O(y^-3 log y) at gamma^2 = 1/6, where the inner integral diverges like log y, and O(y^(-1/(2gamma^2))) above 1/6),
  so w explodes in finite time with probability
      P_explode(w0) = int_0^{w0} s' / int_0^inf s'   in (0, 1), for every tau0 > 0 and every PD V_0.
- If gamma^2 >= 1/2: s(inf) = inf, no explosion of w; w -> 0 a.s. (rank collapse in the limit, never in finite time).
V cannot explode while w stays bounded: the drift of S = 1^T V 1 is (gamma^2 w^2/(4 tau0^2)) S (D = 0) and its noise is
O((1 + w) S), so S is a linear SDE with bounded coefficients on {w <= r}; r = P V 1 is bounded by sqrt(w S) (PSD). So for
m = 2 the explosion time of V equals that of w, and the shaped-attention SDE of Theorem 4.2 has a global positive-definite
solution iff gamma^2 >= 1/2. This is the dossier's TARGET 2, settled as the ray predicted, by an exact reduction rather
than the ray heuristic. (Corollary 4.3, with MLP blocks, is not covered: the MLP terms depend on the token correlation.)

## 5. m >= 3: what fails so far
The one-dimensional functionals do not have a drift that beats their own variance on the whole cone (t1.py, attention
part only, 3000 random V per cell, min of drift(log F)/|V|^2): F = tr W and F = det V both go negative for every
m in {3, 4, 6} and gamma^2 in {0.3, 0.6, 0.9, 1}. At V = sI: log det has drift (gamma^2 (m-1) s^2/(tau0^2 m))(1 - gamma^2 (m+1)/m),
positive iff gamma^2 < m/(m+1); log tr W has drift (gamma^2 a^2/(tau0^2 m^2))((m-1) - 2 gamma^2/(m-1)) on the ray, positive
iff (m-1)^2 > 2 gamma^2. On the ray the mean-token variance S grows faster than tr W in the clock du = |W|^2 dt (S/tr W
drifts up at rate 2 gamma^4/(tau0^2 m^2 (m-1)^2)), so the projectivized process drifts toward the rank-collapse corner 11^T,
where the r-coupling is the term to control. Explosion for m >= 3 needs either a corrector psi(angle) making
log tr W + psi a submartingale-with-rate, or the sign of the Lyapunov exponent of the projectivized process.

## 6. Checks (17 Oct)
- m2_gen.py: drift and quadratic variation of w through the matrix generator (gen.py, attention + linear noise), 1,600 random
  PD 2x2 matrices over gamma^2 in {0.2, 0.5, 0.9, 1}: largest relative error 2.2e-12 against kappa w^3 and 2cw^2 + gamma^4 w^4/tau0^2.
  So w is autonomous to machine precision, whatever the rest of V is.
- Feller at infinity: inner integrand 2/(s' sigma^2) ~ z^(1/(2 gamma^2) - 4); for gamma^2 < 1/6 the product with s' is O(y^-3), for
  1/6 <= gamma^2 < 1/2 the inner integral converges and s' is integrable; so v(inf) < inf on the whole range gamma^2 < 1/2.
  At 0: d log w has drift -> -c and bounded noise near 0, so 0 is natural (never hit), s(0+) finite.
- m2_check.py, exact finite-network chain (n = 2000, 3000 runs, w0 = 0.8, P(w hits 20 before 0.02)) against the 1D law
  int_eps^w0 s' / int_eps^K s': gamma^2 0.5: 0.1110 +- 0.0057 vs 0.1122; gamma^2 0.9: 0.0790 +- 0.0049 vs 0.0885 (1.9 se, the
  chain is at finite n and the depth-to-n correction has not been taken); gamma^2 0.2: 0.1570 +- 0.0066 vs 0.1603 (P_explode from w0 = 0.8 by the formula: 0.1518).

## 7. m = 3, the large-scale limit measured (lyap.py, 17 Oct)
Attention noise only (the linear noise is lower order at large |V|), exact drift, Euler at h = 0.002 in a clock scaled to
|W||V|, renormalised each step, 200 runs from random PD V at scale 1e3, gamma^2 = 0.5, 20,000 steps (u_W = int |W|^2 dt ~ 28):
median growth of log tr W per unit u_W +0.035 (ray value (gamma^2/m^2)(1 - 2 gamma^2/(m-1)^2) = 0.042), still rising;
76 pct of runs have tr W up; median log(S/tr W) stays near -0.4 from step 14,000 to 20,000, so the ratio does NOT run off to
the rank-collapse corner as the ray computation suggested; rho = |r|^2/(m S tr W) sits near 0.4-0.5 (r substantially aligned);
accumulated real time converges (median 8.6e-6 from scale 1e3). Evidence for positive-probability explosion at m = 3, gamma^2 = 0.5,
with a stationary angular part; not a proof, and the window (log increment ~1) is short against the spread.

## 8. m >= 3: two fates, and an exact result on rank-one data (17 Oct 20:0x)
Measured first (lyap3.py, m = 3, h = 0.002, 120 runs, u_W ~ 35; lyapR.py on the merged set). The median growth of log tr W
is the wrong statistic: paths split into two groups. About 40 pct at gamma^2 = 1 (60 pct at 0.5) grow; in them W becomes rank
one (2nd/1st eigenvalue 0.02-0.05), r lines up with WD (cos 0.99-1.00), T3 is 0.64-0.76 of |W|^2, and real time settles. The
rest drift toward rank collapse (S/tr W rising, cos(r, WD) 0.1-0.5) and decay. The growing share was flat at 0.38-0.42 from
u_W = 8 to 49 on the 60,000-step gamma^2 = 1 run, so a negative median does not mean no explosion. (Section 7's reading that
gamma^2 = 1 might not explode came from the median and is withdrawn.) On the invariant set {x2 = x3} (kept exactly by the
noise, checked to 0.0) the growing paths end with one token carrying the energy: |x2|^2/|x1|^2 0.007-0.08.

Every rank-r stratum is invariant (the noise is L(.)L^T, and P_ker v (VD)^T P_ker = 0). On rank one, V = lam u u^T, the noise
L dGamma L^T is a multiple of u u^T, so u moves only by the drift:
    du  = (gamma^2 lam^2 beta(u) / (2 m tau0^2)) Pi_perp(u o u) dt          (no noise; Pi_perp(u o u) = grad_sphere of sum u_i^3 / 3)
    dlam = lam^3 f(u) dt + lam sqrt(2c + B(u)^2 lam^2) dB,
    beta(u) = sum_i u_i ((Pu)_i^2 - |Pu|^2/m),  f(u) = (gamma^2/tau0^2)(|Pu|^4/m^2 + beta(u) sum u_i^3 / m),  B(u) = 2 gamma^2 |Pu|^2/(m tau0).
(r1_check.py: against bdrift, 800 random rank-one V, m in {2,3,4,6}, largest relative error 5.5e-10.) At u fixed the scale
density is (2c + B^2 y^2)^(-f/B^2), so lam explodes iff 2f/B^2 > 1. At u = e_1 (one token carries everything):
    beta(e_1) = (m-1)(m-2)/m^2,   2f/B^2 = (m^2 - m - 1) / (2 gamma^2 (m - 1)).
m = 2 gives 1/(2 gamma^2), the section 4 threshold. For m >= 3 the ratio is at least 5/(4 gamma^2) > 1 on all of gamma^2 <= 1.

Proposition (rank-one data, m >= 3, every gamma^2 in (0, 1], tau0 > 0). There are delta > 0 and q > 0 such that from
V_0 = lam_0 u_0 u_0^T with sum (u_0)_i^3 >= 1 - delta the solution explodes in finite time with probability at least
1 - (lam_1/lam_0)^q (lam_1 depends on m, gamma, tau0, delta); in particular with probability -> 1 as lam_0 -> infinity.
Proof. beta > 0 on N_delta = {sum u^3 >= 1 - delta} for small delta, and d(sum u^3)/dt = (3 gamma^2 lam^2 beta/(2 m tau0^2))
|Pi_perp(u o u)|^2 >= 0, so N_delta is forward invariant; shrink delta so that 2f/B^2 >= 1 + 2q there. With h(lam) = lam^(-q),
Lh = q lam^(-q)[ -lam^2 (f - (q+1)B^2/2) + (q+1)c ] <= 0 for lam >= lam_1, since f - (q+1)B^2/2 >= q B^2/2 and B is bounded below
on N_delta. Optional stopping: P(lam reaches lam_1) <= (lam_1/lam_0)^q. Off that event, in the clock dv = lam^2 dt, log lam
has drift (f - B^2/2) - c/lam^2 >= a > 0 and bounded diffusion coefficient, so log lam >= a v/2 for large v a.s.; since
lam >= lam_1 > 0, v reaches infinity unless lam explodes, and t = int dv/lam^2 <= int e^{-a v} dv < infinity: explosion in
finite time. Well-posedness at singular V: the noise covariance is polynomial in V (V (x) V and V (x) VPVPV terms), so its
square root is locally Lipschitz (Stroock-Varadhan, the C^2 square-root lemma), the matrix SDE has a pathwise-unique
solution up to explosion, and the (lam, u) solution above is it. QED (not yet audited).

Check of the rank-one law on the exact finite network (r1_chain.py). Start the chain with only token 1 nonzero. Tokens 2..m
then stay exactly zero, so the chain lives on the rank-one stratum at u = e_1. Its one scalar has an exact one-step law. Setup:
n = 8000, a_0 = 4, the hitting race is K = 20 against eps = 0.05, 3000 runs. P(hit K first), chain against the rank-one SDE:
    m 3 g2 1.0: 0.466 +- 0.009 vs 0.470;  m 3 g2 0.5: 0.539 +- 0.009 vs 0.545;  m 4 g2 1.0: 0.554 +- 0.009 vs 0.554;
    m 2 g2 0.5 (the threshold): 0.367 +- 0.009 vs 0.349.

Transverse exponent at lam e_1 e_1^T. Take the large-scale limit (attention noise only) and the u-clock du = |W|^2 dt. A
transverse block of size s (tokens 2..m small against token 1) changes Phi = (tr V - V_11)/V_11 at the rate
    d log Phi / du -> mu_perp(m, gamma) = (2 gamma^2/m^2) (gamma^2 - m(m-2)/(2(m-1)))      as s -> 0.
This is exact in sympy for m = 3..8 (trans_sym.py: transverse block s^2 I, limit s -> 0). It is the same for 60 random
transverse blocks per (m, gamma^2) in floating point (trans_gen3.py: the spread is under 1e-3, so the rate does not depend on
the block's shape). It is confirmed by Monte Carlo at m = 3 (trans_sim.py): +0.043 +- 0.012 and +0.048 +- 0.019 at gamma^2 = 1
against +0.056, and -0.021 +- 0.007 at gamma^2 = 0.5 against -0.028. Moves along the stratum, i.e. tokens 2..m parallel to token 1,
are pulled back to e_1 by the u-flow (-0.167 at m 3, gamma^2 1).
[REPLACED BY SECTION 9: Phi mixes in the in-stratum tilt; the Schur-complement exponent is negative for every m >= 3 and gamma^2 <= 1.] So e_1 is transversally attracting iff gamma^2 < m(m-2)/(2(m-1)): at m = 3 for gamma^2 < 3/4, and at every m >= 4 for all
gamma^2 <= 1 (the threshold is 4/3 at m = 4). Along the stratum it explodes for every m >= 3 (the proposition above). The two
thresholds are different: 5/4 along the stratum against 3/4 across it at m = 3.

So the corner lam e_1 e_1^T with lam large is an exploding, locally attracting configuration in two cases: m >= 4 at any
gamma^2 <= 1, and m = 3 at gamma^2 < 3/4. The local statement still needs its proof. Conjecture: PD data in a small cone around
it, at large scale, explode with probability close to 1. The proof route is a Lyapunov function lam^(-q) (1 + Phi^p + angle
terms) built from the two exponents. Target 1 from V_0 = sI then also needs a support theorem: the control system reaches that
cone with positive probability. m = 3 with gamma^2 in (3/4, 1] is not covered: e_1 repels there. Yet section 8's numerics still
show 40 pct growing paths at gamma^2 = 1, with W anisotropy 0.02-0.05 and not 0, which suggests a nearby off-stratum
attracting shape. lyapT.py (PD starts eta 1e-2 / 1e-4 around e_1, gamma^2 = 1, with the c-noise): the m = 4 runs move toward
rank one (lam_2/lam_1 median 1.5e-2 -> 1.1e-3). The m = 3 runs drift down as well over u <= 27, because the c-noise
dominates at moderate scale.

## 9. The transverse exponent is the Schur complement's; explosion with positive probability for every m >= 3 (17 Oct 20:1x)
Phi = (tr V - V_11)/V_11 in section 8 is the wrong transverse coordinate. It contains a |w|^2 part, where w = V_perp1/V_11 is the
tilt of tokens 2..m toward token 1, which lives inside the rank-one stratum. At w = 0 the tilt is fed at rate O(Phi), so the
initial rate of log Phi is not its long-run rate. (Monte Carlo at m = 3, gamma^2 = 1: the rate of log Phi falls from +0.043 over
u <= 6 to +0.006 +- 0.007 over u <= 16.) The transverse coordinate is the Schur complement:
    a = V_11,  w = V_perp1 / a,  X = V_perpperp - a w w^T  (PD, (m-1) x (m-1)),  Phi_S = tr X / a.
The rank-one stratum is {X = 0}. Section 8's conclusions about m = 3 above 3/4 are replaced by the following.

Lemma A (exponents at the corner a e_1 e_1^T, large scale, u-clock du = |W|^2 dt). As (w, Phi_S, 1/a) -> 0, uniformly in the
shape X/tr X:
  (i)   drift of log a -> alpha_m = (f(e_1) - B(e_1)^2/2) m^2/(m-1)^2 > 0 for m >= 3 (2f/B^2 = (m^2-m-1)/(2 gamma^2 (m-1)) > 1),
        and its quadratic variation rate stays bounded;
  (ii)  drift of log Phi_S -> mu_S = (gamma^2/(m^2 tau0^2))(gamma^2 - m(m-2)/(m-1)), with bounded quadratic variation rate. mu_S < 0 for
        every m >= 3 and gamma^2 <= 1, since m(m-2)/(m-1) >= 3/2. Exact in sympy for m = 3..7 (schur_sym.py; at m = 3, 4 with a
        general lower-triangular transverse block, and the limit does not depend on its entries). At m = 3 the limit is regular in
        w at w = 0 and equals mu_S there (trans_sym3.py, general w). Monte Carlo (trans_simS.py, u <= 16, 400 runs) against mu_S:
        m 3 gamma^2 1: -0.048 +- 0.009 vs -0.056;  m 3 gamma^2 0.5: -0.052 +- 0.004 vs -0.056;  m 4 gamma^2 1: -0.107 +- 0.006 vs -0.104;
  (iii) drift of |w|^2 <= -2 kappa |w|^2 (1 - C|w|) + C Phi_S, with kappa = gamma^2 (m-2)/(2m(m-1) tau0^2), the linearisation of the
        noiseless u-flow at e_1 (u o u = e_1 + O(|w|^2) and Pi_perp e_1 = -w + O(|w|^2)). On X = 0 the tilt has no noise; off it
        its quadratic variation is O(Phi_S).
The linear (c) noise adds O(c/a^2) per unit u to every rate. Its contribution to the drift of log Phi_S per unit t is
-c (sum t_i^4)/(sum t_i^2)^2 at the corner (schur_lin.py, m = 3, 4): bounded, and of the helpful sign.

General m (agent H's derivation, AUDIT_H.md addendum). At w = 0 write V = diag(a, X), L = diag(sqrt a, L_x).
The noise directions are E = k(l_i g_j^T + g_j l_i^T), with l_i = L e_i and g_j = V P l_j. To leading order in X/a:
E_11 = 2k a^2 (m-1)/m from i = j = 1, and the other terms are O(a^{3/2} X^{1/2}), which gives (i). The pp-block noise is
O(sqrt(a) X^{3/2}), so the Schur complement has no first-order noise of its own. tr b_pp = (gamma^2/tau0^2) a^2 ((m-1)^2/m^4) tr X
+ O(a X^2). Hence the drift of log tr X' is (a^2/tau0^2)((m-1)^2/m^4)(gamma^2 - gamma^4) + O(a X). Subtracting the drift of log a
and dividing by |W|^2 = a^2 ((m-1)/m)^2 gives mu_S for every m >= 3. Only tr X enters at leading order, and the error terms
are quadratic forms in X over tr X, so the limit is uniform in the shape with error O(Phi_S). For general w, the row
operation T = [[1, 0], [-w, I]] maps V to diag(a, X), keeps the Schur complement, and replaces P by T^{-T} P T^{-1}. The same
computation then gives mu_S + O(|w|) + O(Phi_S). For (iii), qv(w) = k^2 a tr X ((m-1)/m)^2 / a^2 per unit t, which is
O(Phi_S) per unit u. The audits' numbers (m = 3..10) agree with these formulas.

Theorem (audited three times, 17 Oct: agent A, agent B, agent H; section 10). Take m >= 3, gamma^2 in (0, 1], tau0 > 0. From every positive-definite V_0, the solution of
the Theorem 4.2 SDE explodes in finite time with positive probability. From V_0 with a_0 -> infinity and |w_0|, Phi_S(V_0) -> 0,
the probability tends to 1.
Proof. (1) Local. Choose q, p in (0, 1) small and delta small, lambda_1 large, so that on
D = {a > lambda_1, |w| < delta, Phi_S < delta}:
    drift(a^-q) <= -(q alpha_m/2) a^-q;   drift(Phi_S^p) <= (p mu_S/2) Phi_S^p;   drift(|w|^2) <= -kappa |w|^2 + C Phi_S^p.
The first two follow from Lemma A by the usual small-power argument (the quadratic-variation term is O(q^2), O(p^2)).
Set Y = a^-q + |w|^2 + M Phi_S^p with M p |mu_S| >= 4C. Then drift(Y) <= 0 on D, so Y stopped at the exit time tau from D
is a nonnegative supermartingale in the u-clock. On the exit boundary, Y >= y_0 = min(lambda_1^-q, delta^2, M delta^p).
Hence P(tau < infinity) <= Y(V_0)/y_0, which tends to 0 at the corner. On {tau = infinity}: the drift of log a is >= alpha_m/2
and its quadratic variation rate is bounded, so log a >= alpha_m u/4 for all large u, a.s. If the solution lived for all real
time, then u(t) >= c' lambda_1^2 t would tend to infinity (|W|^2 >= c' a^2 on D). But t = int du / |W|^2
<= int du / (c' a(u)^2) < infinity, a contradiction. So the solution explodes, with a -> infinity, at a finite real time.
(2) Support. Write the noise as sqrt(c) L dH L^T plus the attention part, with c = gamma^2(2 - gamma^2) > 0. H -> L H L^T is
onto the symmetric matrices for invertible L, so the diffusion matrix is nondegenerate on the PD cone. The drift is polynomial
and the diffusion's square root is analytic on the PD cone. By the Stroock-Varadhan support theorem (localised to compact
subsets of the PD cone, before explosion), for every T > 0 and every continuous PD path phi from V_0 to a point V* in D with
Y(V*) < y_0/4, there is a positive probability that V stays within eps of phi up to time T. Take V* = lambda e_1 e_1^T + eta I
with lambda large and eta small, and eps small enough that Y < y_0/2 on the eps-ball around V*. By the strong Markov property,
P(explosion | V_0) >= P(V_T in that ball) * (1/2) > 0. QED.

With section 4 (m = 2: explosion iff gamma^2 < 1/2), this answers the repaired statement completely for positivity: there is
explosion with positive probability from every PD V_0 iff m >= 3, or m = 2 with gamma^2 < 1/2. The numerics of sections 7-8
show that the probability is below 1, with decaying paths heading to rank collapse 11^T. That part is not proved, and it is not
needed for the statement.

Weakest points, as given to the auditors (all three are now answered: (a) by the general-m derivation above, (b) and (c)
in section 10). (a) Uniformity in Lemma A. It is computed in exact arithmetic only at w = 0 for general shapes, and at
m = 3 for general w. (b) The
noise representation: gen.py's E_j against Theorem 4.2's Sigma. It is checked through the m = 2 exact chain, the drift Monte
Carlo of 16 Oct and r1_chain.py at m = 3, 4, but the full Sigma has not been compared entry by entry. (c) The support theorem
for locally Lipschitz coefficients on an open domain.

Check of (b), 17 Oct 20:3x (cov_check.py). Every entry of n Cov(V' - V) over ONE layer of the finite network (the exact chain
of chain_blowup.py) is compared with sum_j E_j (x) E_j from gen.py, all upper-triangle pairs, random V:
    m 3 g2 0.6, scale 1, n 20000, 400k layers: max gap 0.04 pct of max|Sigma|, max |z| 1.75 (the linear part dominates);
    m 4 g2 0.8, scale 10, n 40000, 300k: attention part 93 pct of Sigma, gap 0.29 pct, max |z| 3.8;
    m 3 g2 1.0, scale 12, n 40000: gap 2.1 pct; n 160000: gap 0.10 pct (attention part 99.6 pct of Sigma).
The gap closes as n grows (the softmax nonlinearity at |Y|/tau ~ 0.15), so the coded covariance is the network's limit. This
also checks the attention part independently of the paper's printed Sigma.

Check of (a) at m = 4, 5 (schur_wreg.py, analytic gradient and Hessian of log(tr Schur/V_11), transverse size 1e-6, 20
random tilts and shapes per cell). The largest gap to mu_S at |w| = 1e-1, 1e-2, 1e-3:
    m 4: 5.7e-3, 4.3e-4, 3.9e-5 (g2 0.5) and 1.3e-2, 6.8e-4, 8.2e-5 (g2 1);
    m 5: 4.1e-3, 1.8e-4, 3.2e-5 (g2 0.5) and 8.0e-3, 6.9e-4, 6.1e-5 (g2 1).
So the error is O(|w|), uniformly over the shapes tried.

## 10. Audits and the remaining checks (17 Oct 20:3x)
First independent audit: agent A, 20:2x, sections 2, 4 and 9, from the text with its own mpmath code
((local dir)). PASS given section 1. One correction, of notation only: the large-scale
rates in Lemma A scale as 1/tau0^2, so the displayed formulas should read
    mu_S = (gamma^2/(m^2 tau0^2))(gamma^2 - m(m-2)/(m-1)),   kappa = gamma^2 (m-2)/(2 m (m-1) tau0^2).
The reason: the drift and the attention noise's variance carry 1/tau0^2, while the clock |W|^2 and the linear noise
do not. alpha_m, written through f and B, already has the factor. No sign changes, so the theorem holds for every
tau0 > 0. (Folded into section 9 at 20:4x.)
Second audit: agent B, 20:3x (rows/T255/reviews_agent_B/). PASS for sections 4 and 9, checked against the
paper's LaTeX source: section 1's Sigma equals the paper's to 6e-61 and its b to 4e-61; Lemma A is exact at the corner for
m = 3..6, uniform down to shape condition 1e-18. Wording point at gamma^2 = 1/6 in section 4, folded in.
Third audit: agent H, 20:36 (AUDIT_H.md, reviews_H/). KEEP sections 2, 4 and 9. Its own 100-digit
generator covers m = 3..10. Its addendum derives Lemma A by hand for every m; that derivation is now in section 9 in place
of the earlier "argued from rational dependence". It found the same tau0 clock point.
Recorded through frontier.py at 20:38 (move T255-POSITIVITY-001, route settled).

Weak point (b), closed against the paper's own formula (paper_sigma.py). The drift b and the diffusion matrix
Sigma = gamma^2(2 - gamma^2) Sigma_lin + gamma^4 tau0^-2 A are built from Theorem 4.2 as printed (p. 9-10 of
2306.17759, with S1, S2 as printed above it and Sigma_lin from Theorem 3.2). They are compared, every entry over
alpha <= beta, delta <= omega, with b(V) and sum_j E_j (x) E_j from section 1. For m = 2..5, gamma^2 0.3 and 1,
tau0 0.7, 1 and 2, five random PD V each, the largest relative gaps are 1.1e-14 (drift) and 3.6e-15 (Sigma).
Control: scaling the paper's A by 1.01 shows up as a 7.6e-4 gap, and a wrong tau0 as 5.2e-2. So section 1 is the
paper's SDE exactly, and section 9's cov_check.py separately ties it to the finite network.

The local step of the proof, checked directly (lyapY.py). The generator of Y = a^-q + |w|^2 + M Phi_S^p uses the full
SDE (drift, attention noise, linear noise) and exact first and second derivatives, in 50-digit arithmetic. Each point
is built in coordinates (L = [[sqrt a, 0], [sqrt a w, chol X]]), so nothing cancels. The constants are q = p = 0.1,
delta = 0.05, lambda_1 = 100, M = 10. Sampling: 300 random points of D per cell, a log-uniform on [10^2, 10^10], |w| up to
delta, Phi_S log-uniform on [delta 10^-12, delta], random transverse shapes. The largest LY/(|W|^2 Y) is
    m 3: -1.5e-3 (g2 1), -4.3e-3 (g2 0.5), -1.4e-3 (g2 0.1);  m 4: -8.4e-3 (g2 1), -4.2e-3 (g2 0.3);
    m 5: -9.6e-3 (g2 1), -6.1e-3 (g2 0.5).
It is negative everywhere sampled, so the supermartingale holds with explicit constants, not only "for q, p small".

Weak point (c), the support step, as the first audit read it. Take a compact PD neighbourhood K of the eps-tube around
the path. Replace the coefficients outside K by smooth, bounded, uniformly elliptic ones. The two processes agree until
the exit from K, and the support theorem for the modified one gives the tracking event positive probability. The noise
is the explicit sum E_j(V) dB_j, with E_j polynomial in the Cholesky factor, which is analytic on the PD cone. So the
coefficients are smooth on K, and the law is the one fixed by the generator (weak uniqueness up to explosion).

NEXT (17 Oct 20:4x): target 3, Corollary 4.3 (the shaped transformer with ReLU MLP blocks). At large scale the MLP terms
are degree 1 (drift) and degree 2 (Sigma_res = 2 gamma^2 Sigma_lin), so they add O(1/a^2) per unit u, like the c-noise.
Still needed: section 2 for the extra drift near the boundary of the PD cone, and the support step with Sigma + Sigma_res.
Earlier NEXT (19:5x) kept below.
NEXT (17 Oct 19:5x): longer lyap runs m3 g2 1.0, m4 g2 1.0, m3 g2 0.5 (60k steps, logs in (local dir)); then a corrector for T3 when r is anti-aligned; the m >= 3 corner analysis (does r/sqrt(S tr W) decay as S/tr W grows?).

## 11. Explosion is never certain: P(explode) < 1 from every PD V_0, every m >= 2, every gamma in (0, 1] (agent Q, 17 Oct 21:42; not yet audited)
Let x = tr V and f = x^q with 0 < q < 1. From section 1, d tr V = tr b(V) dt + dM, and since H and N are independent,
d<tr V> = c * Var-rate of tr(L dH L^T) + (k-part >= 0) = 2 c |V|_F^2 + (>= 0), using Var tr(H M) = 2|M|_F^2 for GOE H and
|L^T L|_F = |V|_F. With |V|_F^2 >= x^2/m and |tr b(V)| <= C x^3 on the PD cone (b is a cubic polynomial, homogeneous of degree 3):
    L f = q x^(q-1) tr b + (q(q-1)/2) x^(q-2) d<tr V>/dt <= q x^q [ C x^2 - (1 - q) c/m ] < 0   on {0 < x < delta},
delta^2 = (1 - q) c/(2 m C). V stays PD up to explosion (section 2), so x > 0 and f(V_{t ^ tau}) (tau = first time x = delta)
is a nonnegative supermartingale: from tr V_0 = x0 < delta, P(tau < inf) <= (x0/delta)^q < 1, and on {tau = inf} |V| stays
bounded, so no explosion. From an arbitrary PD V_0: the noise covariance is >= c Sigma_lin, which is positive definite on
symmetric matrices at every PD V (congruence by invertible L), so the SDE is uniformly elliptic with smooth coefficients on
any compact subset of the PD cone; by the Stroock-Varadhan support theorem the path phi(t) = (1 - t) V_0 + t (x1/2m) I, x1 < delta a chosen level,
t in [0, 1], is tracked within any eps (inside the cone) with positive probability, so {tr V < x1} is reached before
explosion with positive probability, and the strong Markov property finishes it. Quantitative, when tr V_0 < delta: P(explode | V_0) <= (tr V_0/delta)^q.
Together with sections 9 and 4: for m >= 3 (every gamma) and for m = 2 with gamma^2 < 1/2, 0 < P(explode) < 1 from
every PD V_0; for m = 2, gamma^2 >= 1/2, P(explode) = 0. This closes the open item "whether explosion is certain".
Self-check (17 Oct 22:05, not an audit): the linear part of the quadratic variation of tr V equals 2 c |V|_F^2 to 12 digits on
2,400 random PD V (m = 2, 3, 4, 6; gamma^2 = 0.1, 0.5, 1; scales 1e-6..1e6, gen.noise_basis); the attention part is a sum of
squares, hence >= 0; |tr b|/(tr V)^3 stays below 0.05 on the same sample.

## 12. Corollary 4.3 (shaped attention + shaped ReLU MLP): what carries over (agent Q, 17 Oct 21:42)
Cor 4.3 (2306.17759 v2 p10, text in ../../papers/2306.17759v2.txt): dV = [b + b_res] dt + [Sigma + Sigma_res]^(1/2) dB with
(Thm 3.2) b_res = gamma^2 [nu(rho_ab) sqrt(V_aa V_bb)], nu(rho) = ((c+ - c-)^2/(2 pi)) (sqrt(1 - rho^2) - rho arccos rho),
Sigma_res = 2 gamma^2 Sigma_lin.
(a) Noise: Sigma_res has the same congruence form as the c-part (L dH'' L^T, H'' an independent GOE BM), so the linear noise
    coefficient becomes c' = gamma^2 (2 - gamma^2) + 2 gamma^2; nothing else in the noise changes.
(b) nu(1) = 0, so tr b_res = 0. Hence section 11 holds verbatim for Cor 4.3 (extra noise only lowers L f): P(explode) < 1
    from every PD V_0.
(c) PD preservation: sqrt(1 - rho^2) - rho arccos rho = pi (k1(rho) - rho), k1 the degree-1 arc-cosine kernel,
    k1(rho) = 2 E[relu(g_a) relu(g_b)] (mlp_checks.py (a), MC to 3 decimals). With V = D^(1/2) R D^(1/2), D = diag V,
    tr(V^-1 b_res) = gamma^2 ((c+ - c-)^2/2) tr(R^-1 (k1(R) - R)) >= -gamma^2 ((c+ - c-)^2/2) m, because k1(R) (entrywise)
    is a Gram matrix, hence PSD, and tr(R^-1 X) >= 0 for X PSD. (mlp_checks.py (b): min over 20000 near-degenerate R is
    -0.46 / -1.03 / -1.59 / -2.76 / -3.53 for m = 2, 3, 4, 6, 8, above the bound -pi m in the units there.) The Ito part is as
    in section 2. So V stays PD up to explosion for Cor 4.3 too.
(d) [Superseded by section 13, which carries this step out.] Explosion with positive probability: in the large-scale clock (V = R U, t = R^-2 u) b_res is O(R^-2) and Sigma_res
    O(R^-1), the same order as the linear noise already handled in section 9, so the three corner exponents are unchanged.
    NEW DIFFICULTY: b_res does not preserve the rank-one stratum (nu(-1) = (c+ - c-)^2/2 > 0), so Phi_S gets an ADDITIVE
    forcing of order |w|^2/a^2 in the u-clock, while the section 9 supermartingale uses M Phi_S^p with p < 1, whose generator
    term p Phi_S^(p-1) |w|^2 a^-2 is unbounded as Phi_S -> 0. The forcing is integrable along an exploding path (|w| decays,
    a grows), so the expected fix is Phi_S -> Psi = Phi_S + eta a^(-r) with small r (a^(-r) has negative drift where a explodes),
    or restricting the corner region to |w|^2 <= a^(-1) Phi_S. NEXT: carry this out against section 9's exact generator bounds.

## 13. Corollary 4.3, m >= 3: explosion with positive probability from every PD V_0 (agent Q, 17 Oct 22:00; not yet audited)
Theorem. Take m >= 3, gamma^2 in (0, 1], tau0 > 0 and any shaped-ReLU slopes c+, c-. From every PD V_0 the Corollary 4.3 SDE
explodes in finite time with positive probability, and with probability < 1 (section 12 (b)). With section 12 (c) the solution
stays PD up to explosion.
What the MLP terms do near the corner a e_1 e_1^T (coordinates a, w, X, Phi_S of section 9; Delta = (c+ - c-)^2):
  - b_res_11 = 0 and every diagonal entry of b_res is 0 (nu(1) = 0), so the drift of log a is unchanged; Sigma_res is of the
    congruence form of the c-noise, so it adds O(1/a^2) per unit u to every rate, as the c-noise does in section 9.
  - w: b_res_p1 / a = O(|w| + sqrt(Phi_S)) per unit t, so the drift of |w|^2 gains at most C (|w|^2 + Phi_S)/a^2 per unit u.
  - tr X: the only new term is d tr X = -2 sum_i w_i (b_res)_{i1} dt, and |(b_res)_{i1}| <= gamma^2 (Delta/2) sqrt(a V_ii),
    V_ii = a w_i^2 + X_ii. So the forcing of Phi_S per unit u is F <= C (|w|^2 + |w| sqrt(Phi_S))/a^2 <= C' (|w|^2 + Phi_S)/a^2.
    It is ADDITIVE: at X = 0 with some w_i < 0 (token i anti-aligned with token 1, rho_i1 = -1) it equals 2 gamma^2 nu(-1) a w_i^2 > 0
    per unit t. This is why section 9's M Phi_S^p fails: its generator gains M p Phi_S^(p-1) F, unbounded as Phi_S -> 0.
The fix: psi = Phi_S + 1/a = (tr X + 1)/a, and Y = a^-q + |w|^2 + M psi^p.
  (1) Forcing: psi >= 1/a gives psi^(p-1) <= a^(1-p), so M p psi^(p-1) F <= M p C' (|w|^2 a^(1-p) + psi^(p-1) Phi_S)/a^2
      <= M p C' (|w|^2 a^(-1-p) + psi^p/a^2),
      absorbed by -kappa |w|^2 and by the psi^p rate below once a > lambda_1.
  (2) Mixing. Write psi = e^X1 + e^X2, X1 = log Phi_S, X2 = -log a, t = Phi_S/psi. For psi^p,
        drift/(p psi^p) = t drift(X1) + (1 - t) drift(X2) + (1/2) t (1 - t) qv(X1 - X2) + (p/2) qv(log psi).
      X1 - X2 = log tr X. Its noise is O(sqrt(a) X^(3/2)) per unit sqrt(t) for every |w| < delta (after the row operation T of
      section 9, T L = diag(sqrt a, L_x), and [d Gamma]_pp = O(sqrt(a X)) because K_pp = O(X), K_1p = O(sqrt(a X))), so
      qv(log tr X) = O(Phi_S + 1/a^2) per unit u and the cross term vanishes at the corner. Hence
        drift(psi^p)/(p psi^p) <= t (mu_S + o(1)) - (1 - t)(alpha_m + o(1)) + O(p) < 0,
      uniformly in t in [0, 1], for p small and (a^-1, |w|, Phi_S) small. Here drift(X1) is the drift of log Phi_S without the MLP
      forcing; the forcing is the term of (1), and F/psi <= C (|w|^2/a + 1/a^2), so it is o(1) either way. (A weight a^-r with r != 1 in place of 1/a leaves
      qv(X1 - X2) = (1 - r)^2 qv(log a) + ..., which does not vanish and puts a bump (1/8)(1 - r)^2 sigma_a^2 in the middle of
      [0, 1]; r = 1 is the choice that cancels the common noise of log a.)
  (3) The rest of section 9's proof is unchanged: drift(|w|^2) <= -kappa |w|^2 + C psi with C psi <= C (2 delta)^(1-p) psi^p absorbed
      by M (take lambda_1 >= 1/delta, so psi < delta + 1/lambda_1 <= 2 delta on D); Y stopped at the exit from D is a supermartingale; Y -> 0 at the corner; on the exit boundary Y >= min(lambda_1^-q,
      delta^2, M delta^p) (faces a = lambda_1, |w| = delta, Phi_S = delta); on {never exit} log a grows linearly in u and real time is finite.
  (4) Support: b_res is analytic on the PD cone (|rho_ab| < 1 off the diagonal, nu is analytic on (-1, 1)), and the noise
      covariance is >= c Sigma_lin, nondegenerate; section 9 (2) applies verbatim.
Check (lyapY_mlp.py, 50 digits, exact generator with b_res and Sigma_res, Phi_S sampled down to delta 1e-40, a in [1e2, 1e10],
q = p = 0.1, delta = 0.05, lambda_1 = 100, M = 10, 300 points per cell; results in lyapY_mlp_results.txt). Max of LY/(|W|^2 Y):
    new Y:  m 3 g2 1 Delta 1 -2.7e-3; m 3 g2 0.5 Delta 1 -4.5e-3; m 3 g2 1 Delta 4 -1.9e-3; m 4 g2 1 Delta 1 -8.6e-3;
            m 4 g2 0.3 Delta 4 -4.2e-3; m 5 g2 1 Delta 1 -9.7e-3.
    old Y (section 9's) with the MLP: m 3 g2 1 Delta 1 +1.1e29 and m 4 g2 1 Delta 4 +3.1e29, both at Phi_S ~ 1e-40 (the forcing);
    old Y with Delta = 0 (section 9's own case): -1.9e-3. So the check sees the failure and the fix.
Not covered: m = 2 with the MLP. There the attention-only explosion is not a corner phenomenon (mu_S > 0 at m = 2) but the exact
1-D reduction of section 4, which b_res breaks. Expected: the same threshold gamma^2 < 1/2, since b_res and Sigma_res are lower
order at large scale; it needs its own proof (a Feller test with a perturbed 2-D system).
NEXT (17 Oct 22:00): audits of sections 11-13; m = 2 with the MLP; the novelty check through the papers citing 2306.17759.

## 14. Corollary 4.3, m = 2: the same threshold gamma^2 < 1/2 (agent Q, 17 Oct 22:08; not yet audited)
Theorem. For m = 2, every gamma^2 in (0, 1], tau0 > 0, slopes c+, c- (Delta = (c+ - c-)^2) and every PD V_0, the Corollary 4.3
SDE explodes with probability in (0, 1) if gamma^2 < 1/2 and never explodes if gamma^2 >= 1/2.
Proof. w = tr(PV) = (V11 + V22 - 2 V12)/2 is linear in V, so it has no Ito term.
  - Drift: the attention part is kappa w^3 exactly (section 4, D = 0). The MLP part is tr(P b_res) = -(b_res)_12
    = -gamma^2 nu(rho) sqrt(V11 V22) <= 0.
  - Noise: the attention part has qv 4 k^2 w^4 (section 4). The c-noise and Sigma_res are congruences L H L^T, and
    Var tr(P L H L^T) = 2 |L^T P L|_F^2 = 2 w^2, so the qv is (2c + 4 gamma^2) w^2. All three are independent and the total
    sigma(w)^2 = (2c + 4 gamma^2) w^2 + 4 k^2 w^4 is a function of w alone, so dw = [kappa w^3 - theta_t] dt + sigma(w) d beta
    with beta a Brownian motion.
  - Bound on theta: nu(rho) <= (Delta/4)(1 - rho) on [-1, 1] (max of nu/(Delta (1 - rho)) is 1/4, attained at rho = -1).
    Also sqrt(V11 V22)(1 - rho) = sqrt(V11 V22) - V12 <= (V11 + V22)/2 - V12 = w (AM-GM). Hence 0 <= theta_t <= gamma^2 (Delta/4) w_t.
  - Comparison (Ikeda-Watanabe, same sigma, locally Lipschitz on (0, inf), localised up to exit from compacts): w_lo <= w <= w_up
    pathwise, where w_up has drift kappa y^3 and w_lo has drift kappa y^3 - gamma^2 (Delta/4) y, both with diffusion sigma(y).
  - Feller tests. Both scale densities are ~ y^(-1/(2 gamma^2)) at infinity (2 kappa/(4 k^2) = 1/(2 gamma^2); the linear term is
    integrable there against sigma^2 ~ y^4). Near 0, s'_up is bounded and s'_lo ~ y^(gamma^2 Delta/(4(c + 2 gamma^2))), both
    integrable, and 0 is not reached (log y has drift <= -c' < 0 near 0 and bounded qv).
    For gamma^2 < 1/2, w_lo explodes with probability int_0^{w0} s'_lo / int_0^inf s'_lo > 0, and Feller's v(inf) < inf as in
    section 4. So w, and with it V, explodes with positive probability. For gamma^2 >= 1/2, w_up never explodes, so neither
    does w.
  - V is bounded while w is. S = 1^T V 1 has drift (gamma^2 w^2/(4 tau0^2)) S + 2 (b_res)_12 <= (gamma^2 w^2/(4 tau0^2)) S + C w and noise
    O((1 + w) S). That is a linear SDE with bounded coefficients on {w <= r}, and |V| <= C (w + S).
  - P(explode) < 1 is section 12 (b). QED
Checks: max_rho nu/(Delta (1 - rho)) = 0.250000 at rho = -1 (2e6-point grid); w - (sqrt(V11 V22) - V12) >= 0 on 2e5 random PD
V (smallest relative gap 3e-11, at V11 = V22).
With sections 11-13 this answers the whole row, MLP included, pending audits: for every m >= 2 and gamma^2 in (0, 1], with or
without the shaped ReLU MLP blocks, the covariance SDE explodes with probability in (0, 1) if m >= 3, or if m = 2 and
gamma^2 < 1/2. Otherwise it has a global PD solution almost surely.
NEXT (17 Oct 22:08): independent audits of sections 11-14; the novelty check through the papers citing 2306.17759; then
frontier.py moves.

Novelty, second pass (17 Oct 22:1x, two web searches, one extended): no paper found that proves explosion, non-explosion or global
existence for the shaped-attention covariance SDE, with or without MLP blocks. The hits are the paper itself (local convergence up to
T_r = inf{t : |V_t| >= r}, stability by parameter sweeps), its predecessor 2206.02768 (1-D criterion, shaped MLP, no attention) and
unrelated explosion results. Still owed: a citing-papers list (Semantic Scholar / Google Scholar) read by title and abstract.

Self-check of section 14 (17 Oct 22:2x, lyapY_mlp.py's own drift and noise basis, 50 digits, not an audit): at m = 2 the qv of
w equals (2c + 4 gamma^2) w^2 + gamma^4 w^4 / tau0^2 to 1e-48 on 1,600 random PD V (gamma^2 = 0.2, 0.5, 0.7, 1; scales 1e-6..1e6),
and theta = kappa w^3 - tr(P B) satisfies 0 <= theta <= gamma^2 (Delta/4) w on 3,000 more (max ratio 0.998, Delta = 1 and 4).

Novelty, third pass (17 Oct 22:2x): Semantic Scholar lists 59 papers citing 2306.17759. All titles read; the five that could touch
the question were read by abstract (2310.12079 Li-Nica ODE/SDE limits of shaped and unshaped nets; 2403.02579 signal-propagation
geometry; 2505.24333 two failure modes; 2601.21942 rank across depth; 2607.14018 clustering in deep stochastic transformers). None
studies explosion or global existence of the shaped-attention covariance SDE. Not covered: citers missing from Semantic Scholar
(Google Scholar usually lists more) and the full text of 2310.12079.

Referees, sections 11-14 (17 Oct 22:2x-22:3x, blind, read-only): agent H, agent B (independent generator, sympy Hessian,
110 digits, reproduces section 13's table: new Y -1.5e-3..-9.9e-3, old Y +4e24..+1.2e27), agent C (checked against the
paper's Thm 3.2/4.2/Cor 4.3 text). All three: PASS on 11, 12, 13, 14, no FAIL. Their fixes are applied above (x1 in section 11;
12 (d) marked superseded; 13 (2) names which drift; 13 (3) exit constants and lambda_1 >= 1/delta; 14 tau0^2). All three run on the
same Claude login as the author: independent replays, not distinct-account reviews. Reports: reviews_agent_B/REVIEW_T255_S11_14.md,
reviews_H/T255_s11_14_audit_20261017.md, and the mesh message of agent C (copied to reviews_C/REVIEW.md).
A fourth blind referee, agent A (same login), 19:31Z: PASS on 11-14, no broken line, the same x0 and exit-bound fixes. It notes that
the paper's appendix (about line 1361 of the source) prints nu with (c+ + c-)^2 and + rho arccos rho. The form used here is eq. 6 of
Thm 3.2, (c+ - c-)^2/(2 pi) (sqrt(1 - rho^2) - rho arccos rho), which equals (c+ - c-)^2/2 (k1(rho) - rho) with k1 the arc-cosine kernel
and vanishes with the slopes equal, as a ReLU-difference term must; the appendix form is read as a typo.
A fifth, agent J (same login), 19:45Z: PASS on 11-14, no broken line; independent generator from eq. 6 and Cor 4.3 at
200 digits, report in reviews_agent_J/. Admission still needs one review from a distinct account.

NEXT (17 Oct 23:5x): paper Sections 3, 4, 5 drafted (PAPER_DRAFT.md, pushed f8ef8b6). Next: Section 6 (MLP: sections 12-14 here),
Section 7 (numerics); read mc_m2_g02_D4.out when pid 35280 ends (at step 30000: 33 exploded, 18 live, 349 decided-no of 400,
so the fraction lies in [0.083, 0.128], inside the bracket [0.080, 0.134]) and write the section 14 Monte Carlo note.

Check for the paper's Section 2 (18 Oct 00:0x, orth_inv.py): the covariance of L dGamma L^T is the same for L and L O, O orthogonal,
so the law of V does not depend on the square root chosen. Exact sum over the noise directions, m = 2..5, 20 random (V, O) each:
largest relative gap 3.3e-15.

Second derivation of the section 14 bracket (18 Oct 00:0x, feller_closed.py): the scale density in closed form,
s'(y) = y^(2 eps/A) ((A + B y^2)/A)^(-(2 kappa + 2 eps B/A)/(2B)), A = 2c (+ 4 gamma^2 with the MLP), B = 4 k^2, eps the linear drift,
integrated by scipy quad, a different route from the mpmath quadrature of the drift. gamma^2 0.2, tau0 1, w0 1, Delta 4:
no MLP 0.192333, MLP upper 0.133936, MLP lower 0.080080 - the same three numbers.


Section 14 Monte Carlo (sim_mlp.py, m=2, gamma^2 0.2, Delta 4, 400 paths, step 0.01): at step 34,000 (t=340) 44 exploded, 349 decided-no, 7 live; fraction in [0.110, 0.1275], inside the Feller bracket [0.0801, 0.1339]. The run stopped at the 18 Oct 00:09 power-off; the remaining 7 paths cannot move the interval outside the bracket. Written into PAPER_DRAFT.md section 7.

NEXT (18 Oct 01:0x): the paper draft is complete with no placeholder. Remaining: a distinct-account review (Codex paused, or a person); until then the row stays a proof-PASS on same-login replays only.

NEXT (18 Oct 01:1x): REVIEW_BRIEF.md written for the distinct-account referee (six claims in dependency order, with the check script for each). Waiting on a referee from another account; nothing else is open on the row.

Novelty pass 5 (18 Oct 01:1x): web search 'shaped transformer covariance SDE explosion global existence 2026' returns only Noci et al. 2023 (arXiv 2306.17759, NeurIPS 2023) and its mirrors; no follow-up on explosion or global existence. NEXT unchanged: waiting on a distinct-account referee (REVIEW_BRIEF.md).

Voice audit (18 Oct 02:1x): PAPER_DRAFT.md grepped for the banned self-narration phrases (none) and every we/our read; one process sentence in Section 2 restated as mathematics. NEXT unchanged: waiting on a distinct-account referee (REVIEW_BRIEF.md).

Section 15 (18 Oct 03:3x): m=2 without MLP in closed form. P = 2 Gamma(p) x 2F1(1/2,p;3/2;-x^2)/(sqrt(pi) Gamma(p-1/2)), p = 1/(4 gamma^2), x = gamma w0/(tau0 sqrt(2(2-gamma^2))). Agrees with quadrature of (3.2) to 6e-15 at 11 values of gamma^2 in [0.02, 0.48] (m2_closed_form.py). Limits: erf(w0/(4 tau0)) as gamma^2->0 (0.27629 at gamma^2=1e-4 vs erf(1/4)=0.27633); ~ 2 asinh(w0/(sqrt6 tau0)) (1/2-gamma^2) at the threshold (ratio 0.79531 at 1/2-1e-4 vs 0.79537). Added to PAPER_DRAFT.md as (3.3). Monotonicity in gamma^2 is seen numerically, not proved, and the paper does not claim it.
NEXT: waiting on a distinct-account referee (REVIEW_BRIEF.md); (3.3) is a new claim for the referee, checked by m2_closed_form.py.
