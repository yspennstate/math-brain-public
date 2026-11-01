# Finite-time explosion of the covariance SDE of the shaped transformer

Draft of the statement page (title, abstract, main results). Proofs are in M2_EXACT.md, sections 2 and 6 to 14.

## Abstract

Noci, Li, Li, He, Hofmann, Maddison and Roy showed that, after shaping the softmax so that attention is a small
perturbation of the identity, the covariance of m token representations in a transformer converges, as depth and width
grow proportionally, to the solution of a matrix stochastic differential equation, up to a stopping time. The drift of
that equation is cubic, so its solution may leave every compact set in finite time. We determine exactly when it does.
For m = 2 tokens the solution explodes with positive probability if and only if gamma^2 < 1/2, where gamma is the
residual weight. For m >= 3 it explodes with positive probability from every positive-definite initial condition and for
every gamma^2 in (0, 1]. In all cases explosion is never certain, and the solution stays positive definite up to its explosion time.
The same classification holds when shaped ReLU MLP blocks are added. For m >= 3 the explosion comes from a corner of the
cone where one token carries the variance, and the proof rests on a Lyapunov function adapted to that corner.

## Setting

V_t is the m x m covariance, t the depth-to-width ratio, and

    dV = b(V) dt + L dGamma L^T,   V = L L^T,   dGamma = sqrt(c) dH + k (dN K + K dN^T),   K = L^T P L,

with P = I - 11^T/m, c = gamma^2 (2 - gamma^2), k = gamma^2/(m tau0), H a GOE Brownian motion, N an m x m matrix of
independent Brownian motions, and

    b(V) = (gamma^2/tau0^2) [ V |PVP|_F^2/m^2 + (1/2m)(v (V D)^T + (V D) v^T) ],   v = diag V,
    D = diag(PVP) - (tr(PVP)/m) 1.

With MLP blocks (Corollary 4.3 of Noci et al.) the drift gains b_res = gamma^2 (nu(rho_ij) sqrt(V_ii V_jj))_ij, where
nu(r) = (Delta/2pi)(sqrt(1 - r^2) - r arccos r) and nu(1) = 0. The martingale part gains sqrt(2 gamma^2) L dH' L^T,
with H' an independent GOE Brownian motion. Let zeta denote the explosion time.

## Results

Theorem 1 (positivity). For every m >= 2 and every positive-definite V_0, V_t is positive definite for all t < zeta,
with or without MLP blocks.

Theorem 2 (two tokens). Let m = 2. Then P(zeta < infinity) > 0 if and only if gamma^2 < 1/2. The quantity
w = tr(PV) is an autonomous one-dimensional diffusion, and P(zeta < infinity) is given by its scale function. With MLP
blocks, w lies between two one-dimensional diffusions that have the same Feller exponent, so the threshold 1/2 is
unchanged.

Theorem 3 (three or more tokens). Let m >= 3. For every gamma^2 in (0, 1] and every positive-definite V_0,
P(zeta < infinity) > 0. The same holds with MLP blocks, for every Delta >= 0.

Theorem 4 (explosion is never certain). For every m >= 2, every gamma^2 in (0, 1] and every positive-definite V_0,
P(zeta < infinity) < 1, with or without MLP blocks. There are delta > 0 and q in (0, 1) with
P(zeta < infinity) <= (tr V_0 / delta)^q whenever tr V_0 < delta.

Corollary. The shaped-attention SDE explodes with probability strictly between 0 and 1 when m >= 3, or when m = 2 and
gamma^2 < 1/2. Otherwise it is defined for all t, almost surely.

## Plan of the paper

1. Introduction and the limit of Noci et al.
2. The noise in congruence form; positivity (Theorem 1).
3. Two tokens: the reduction to one dimension and the Feller test (Theorem 2).
4. The one-token corner: coordinates, the corner and Schur-complement exponents, the Lyapunov function
   psi = Phi_S + 1/a (Theorem 3).
5. Explosion is never certain: the supermartingale (tr V)^q near the origin and the support theorem (Theorem 4).
6. MLP blocks: the arc-cosine kernel bound, the forcing off the corner, the two-token comparison.
7. Numerical illustration: Monte Carlo explosion fractions against the bounds of Section 6.

## Related work

Li, Nica and Roy (2022) give the one-dimensional explosion criterion for shaped MLPs with smooth activations through the
same Feller test. Li and Nica (2024) prove convergence of the covariance in the proportional limit up to localising
stopping times.

## Draft of Section 3: two tokens

Let m = 2 and e = (1, -1)/sqrt 2. Then P = e e^T, so W = PVP = w e e^T with

    w = tr(PV) = (V_11 + V_22 - 2 V_12)/2,

the variance of the difference of the two token representations. Since diag W = (w/2, w/2), the vector D of Section 1
vanishes, and the drift reduces to b(V) = (gamma^2/tau0^2) w^2 V/4. As w is linear in V it carries no Ito correction, and

    tr(P b(V)) = (gamma^2/(4 tau0^2)) w^3 = kappa w^3.

The martingale part of w is tr(P L dGamma L^T). The GOE part contributes quadratic variation 2c |L^T P L|_F^2 = 2c w^2,
since L^T P L has the single nonzero eigenvalue w. The matrix part contributes 4 k^2 w^4, because K = L^T P L is of rank one
K = w f f^T with f a unit vector, and each of the two terms tr(P L dN K L^T) and tr(P L K dN^T L^T) equals
w^2 (f^T dN f). Both depend on w alone, so by Levy's characterisation

    dw = kappa w^3 dt + (2c w^2 + 4 k^2 w^4)^(1/2) d beta                                   (3.1)

for a one-dimensional Brownian motion beta. Equation (3.1) is autonomous.

Lemma 3.1. For (3.1), the scale density normalised at y = 0 is s'(y) = (1 + 2k^2 y^2/c)^(-1/(4 gamma^2)).

Proof. 2 kappa y^3/(2c y^2 + 4 k^2 y^4) = (kappa/(4k^2)) d/dy log(2c + 4k^2 y^2), and kappa/(4k^2) = 1/(4 gamma^2). QED

Proof of Theorem 2 without MLP blocks. Near 0, log w has drift -c + O(w^2) and bounded quadratic variation, so 0 is not
reached and w tends to 0 on the event that it does not explode. At infinity s'(y) behaves like y^(-1/(2 gamma^2)), which is
integrable exactly when gamma^2 < 1/2. If gamma^2 >= 1/2 then s(infinity) = infinity and w does not explode. If gamma^2 < 1/2,
Feller's test function v(infinity) is finite, because s'(y) int_0^y 2/(s' sigma^2) is O(y^-3) for gamma^2 < 1/6, O(y^-3 log y)
at gamma^2 = 1/6 and O(y^(-1/(2 gamma^2))) for 1/6 < gamma^2 < 1/2. So w explodes in finite time with probability

    P(zeta < infinity) = int_0^{w_0} s'(y) dy / int_0^infinity s'(y) dy,                  (3.2)

which lies strictly between 0 and 1. It remains to see that V explodes exactly when w does. The sum S = 1^T V 1 satisfies a
linear equation dS = (gamma^2 w^2/(4 tau0^2)) S dt + dM with d<M> <= C (1 + w)^2 S^2 dt, so S stays finite on every interval
where w is bounded, and |V| <= C (w + S). QED

For example, at gamma^2 = 0.2, tau0 = 1 and w_0 = 1, (3.2) gives 0.1923.

The ratio (3.2) has a closed form. Put p = 1/(4 gamma^2) and x = gamma w_0/(tau0 (2(2 - gamma^2))^(1/2)). Since
int_0^x (1 + u^2)^(-p) du = x 2F1(1/2, p; 3/2; -x^2) and int_0^infinity (1 + u^2)^(-p) du = (pi^(1/2)/2) Gamma(p - 1/2)/Gamma(p)
for p > 1/2,

    P(zeta < infinity) = (2 Gamma(p)/(pi^(1/2) Gamma(p - 1/2))) x 2F1(1/2, p; 3/2; -x^2),   0 < gamma^2 < 1/2.   (3.3)

Two limits follow. As gamma^2 -> 0, the substitution u = v p^(-1/2) and p^(1/2) x -> w_0/(4 tau0) give
P(zeta < infinity) -> erf(w_0/(4 tau0)), which is positive: weak residual weighting does not make explosion rare. As
gamma^2 -> 1/2, Gamma(p - 1/2) ~ 1/(p - 1/2) and p - 1/2 ~ 1/2 - gamma^2, so
P(zeta < infinity) ~ 2 asinh(w_0/(6^(1/2) tau0)) (1/2 - gamma^2), and the probability vanishes linearly at the threshold.
At tau0 = w_0 = 1 the values at gamma^2 = 0.1, 0.2, 0.3, 0.4, 0.45 are 0.2381, 0.1923, 0.1379, 0.0741, 0.0384, between the
limits 0.2763 and 0.

With MLP blocks, (3.1) acquires the drift -theta_t with 0 <= theta_t <= gamma^2 (Delta/4) w_t, and its noise coefficient
becomes ((2c + 4 gamma^2) w^2 + 4 k^2 w^4)^(1/2), still a function of w alone (Section 6). Comparison with the equations
whose drifts are kappa y^3 and kappa y^3 - gamma^2 (Delta/4) y brackets P(zeta < infinity) between the two values of (3.2)
for those equations; at gamma^2 = 0.2, Delta = 4, tau0 = 1 and w_0 = 1 they are 0.0801 and 0.1339.

## Draft of Section 5: explosion is never certain

Let x = tr V. By Section 2, d tr V = tr b(V) dt + dM_t, where M is the trace of the martingale part. Because H and N are
independent, the quadratic variation of M is at least that of its GOE part, and Var tr(L dH L^T) = 2 |L^T L|_F^2 dt =
2 |V|_F^2 dt. Hence

    d<M>_t >= 2c |V_t|_F^2 dt >= (2c/m) x_t^2 dt,                                           (5.1)

since |V|_F^2 >= (tr V)^2/m on the positive-definite cone. The drift b is a homogeneous cubic polynomial in V, so there is
C = C(m, gamma, tau0) with |tr b(V)| <= C x^3 for V positive definite.

Lemma 5.1. Let 0 < q < 1 and delta^2 = (1 - q) c/(2mC). Then f(V) = (tr V)^q satisfies Lf <= 0 on {0 < tr V < delta}.

Proof. By (5.1), Lf <= q x^(q-1) C x^3 + (q(q - 1)/2) x^(q-2) (2c/m) x^2 = q x^q (C x^2 - (1 - q) c/m), and the bracket is
at most -(1 - q) c/(2m) < 0 when x < delta. QED

Proof of Theorem 4. Suppose first that tr V_0 < delta, and let tau be the first time tr V_t = delta. By Theorem 1, V stays
positive definite before explosion, so x_t > 0 and f(V_{t ^ tau}) is a nonnegative supermartingale. Optional stopping gives
delta^q P(tau < infinity) <= (tr V_0)^q. On {tau = infinity} the trace, and with it |V|, stays below delta, so the solution
does not explode. Hence P(zeta < infinity) <= (tr V_0/delta)^q < 1.

For a general positive-definite V_0, fix x_1 < delta. The GOE part of the noise acts by the congruence L dH L^T with L
invertible, so the diffusion matrix is nondegenerate at every positive-definite V, and the coefficients are smooth there.
On a compact neighbourhood, inside the cone, of the segment phi(s) = (1 - s) V_0 + s (x_1/(2m)) I, s in [0, 1], the
equation is uniformly elliptic, and the support theorem of Stroock and Varadhan shows that the solution follows phi within
any prescribed distance with positive probability. On that event tr V falls below x_1 before explosion. The strong Markov
property at that time and the first case finish the proof. QED

With MLP blocks, the trace of b_res vanishes because nu(1) = 0, and the extra noise sqrt(2 gamma^2) L dH' L^T only increases
the quadratic variation in (5.1). The same argument applies with the same delta.

## Draft of Section 4: three or more tokens

Let m >= 3. Write a = V_11 for the variance of the first token, w = V_{perp 1}/a in R^(m-1) for the tilt of the other tokens
towards it, and

    X = V_{perp perp} - a w w^T,     Phi_S = tr X / a,

so that X is the Schur complement of V_11 and V is positive definite exactly when a > 0 and X is positive definite. The set
{X = 0} is the rank-one stratum. It is invariant, as is every stratum of fixed rank: the noise acts by congruence, and the drift b(V) satisfies
P_K b(V) P_K = 0 for P_K the projection onto the kernel of V. On it V = lambda u u^T with |u| = 1, the noise L dGamma L^T is a multiple of u u^T, and

    du = (gamma^2 lambda^2 beta(u)/(2 m tau0^2)) Pi_perp(u o u) dt,
    d lambda = f(u) lambda^3 dt + lambda (2c + B(u)^2 lambda^2)^(1/2) dB,                                    (4.1)

where u o u is the entrywise square, Pi_perp the projection orthogonal to u,

    beta(u) = sum_i u_i ((Pu)_i^2 - |Pu|^2/m),   f(u) = (gamma^2/tau0^2)(|Pu|^4/m^2 + beta(u) sum_i u_i^3/m),
    B(u) = 2 gamma^2 |Pu|^2/(m tau0).

The direction u moves without noise, along the gradient of sum u_i^3 on the sphere. At u fixed, lambda is a diffusion of the
type (3.1) and explodes if and only if 2f/B^2 > 1. At u = e_1, where one token carries all the variance,

    beta(e_1) = (m - 1)(m - 2)/m^2,     2f(e_1)/B(e_1)^2 = (m^2 - m - 1)/(2 gamma^2 (m - 1)).                (4.2)

For m = 2 this is 1/(2 gamma^2), the threshold of Theorem 2. For m >= 3 it is at least 5/(4 gamma^2) > 1 for every
gamma^2 <= 1. So the corner is exploding along the stratum. The point of this section is that it also attracts the
transverse coordinates (w, Phi_S), and that this suffices.

We measure time near the corner by the clock du = |W|^2 dt, W = PVP. At the corner |W|^2 = a^2 ((m - 1)/m)^2 (1 + O(|w| + Phi_S)).

Lemma 4.1. As |w|, Phi_S and 1/a tend to 0, uniformly in the shape X/tr X, the following hold in the clock u.
(i) The drift of log a tends to alpha_m = (f(e_1) - B(e_1)^2/2) m^2/(m - 1)^2, which is positive by (4.2), and the rate of its
quadratic variation stays bounded.
(ii) The drift of log Phi_S tends to

    mu_S = (gamma^2/(m^2 tau0^2)) (gamma^2 - m(m - 2)/(m - 1)),

which is negative for every m >= 3 and gamma^2 <= 1, since m(m - 2)/(m - 1) >= 3/2. The rate of its quadratic variation stays
bounded.
(iii) The drift of |w|^2 is at most -2 kappa |w|^2 (1 - C|w|) + C Phi_S, where kappa = gamma^2 (m - 2)/(2 m (m - 1) tau0^2),
and the rate of its quadratic variation is O(Phi_S).

Proof. Suppose first w = 0, so that V = diag(a, X) and L = diag(sqrt a, L_x). The attention noise is spanned by the matrices
k (l_i g_j^T + g_j l_i^T) with l_i = L e_i and g_j = V P l_j. To leading order in X/a the term i = j = 1 contributes
2k a^2 (m - 1)/m to the (1, 1) entry and every other term is O(a^(3/2) |X|^(1/2)); this gives (i), with alpha_m read off from
(4.1) at u = e_1. In the lower block the noise is O(a^(1/2) |X|^(3/2)), so the Schur complement has no first-order noise of
its own, while

    tr b(V)_{perp perp} = (gamma^2/tau0^2) a^2 ((m - 1)^2/m^4) tr X + O(a |X|^2).

The drift of log tr X is therefore (a^2/tau0^2)((m - 1)^2/m^4)(gamma^2 - gamma^4) + O(a |X|). Subtracting the drift of log a and
dividing by |W|^2 gives mu_S. Only tr X enters at leading order and the error terms are quadratic forms in X divided by tr X,
so the limit is uniform in the shape, with error O(Phi_S). For general w, the row operation T with rows (1, 0) and (-w, I)
maps V to diag(a, X), keeps the Schur complement and replaces P by T^(-T) P T^(-1); the same computation gives mu_S + O(|w|)
+ O(Phi_S). For (iii), on X = 0 the tilt w follows the noiseless flow (4.1), whose linearisation at e_1 is -kappa w in the
clock u, because u o u = e_1 + O(|w|^2) and Pi_perp e_1 = -w + O(|w|^2). Off the stratum the drift changes by O(Phi_S) and the
quadratic variation of w is k^2 a tr X ((m - 1)/m)^2/a^2 per unit t, which is O(Phi_S) per unit u. The linear part of the
noise, sqrt(c) L dH L^T, adds O(c/a^2) per unit u to each of these rates. Its contribution to the drift of log Phi_S has the
helpful sign. QED

For m = 3..7 the limits in (i) and (ii) agree with an exact symbolic computation at w = 0 for general lower-triangular X, and
at m = 3 for general w. At m = 4 and 5 the gap to mu_S at |w| = 10^-1, 10^-2, 10^-3 shrinks linearly in |w| over random
shapes. Monte Carlo over 400 paths at m = 3, gamma^2 = 1 gives -0.048 +- 0.009 against mu_S = -0.056.

Proof of Theorem 3 without MLP blocks. (1) Near the corner. Choose q, p in (0, 1) and delta > 0 small and lambda_1 large so
that, on D = {a > lambda_1, |w| < delta, Phi_S < delta}, Lemma 4.1 gives in the clock u

    drift(a^-q) <= -(q alpha_m/2) a^-q,   drift(Phi_S^p) <= (p mu_S/2) Phi_S^p,   drift(|w|^2) <= -kappa |w|^2 + C Phi_S^p.

The first two follow from (i) and (ii) because the quadratic-variation terms are of order q^2 and p^2. The third follows from
(iii) and Phi_S <= delta^(1-p) Phi_S^p. Put Y = a^-q + |w|^2 + M Phi_S^p with M p |mu_S| >= 4C. Then drift(Y) <= 0 on D, so
Y stopped at the exit time tau from D is a nonnegative supermartingale. On the boundary of D one of the three terms is at
least y_0 = min(lambda_1^-q, delta^2, M delta^p), so P(tau < infinity) <= Y(V_0)/y_0.

On {tau = infinity} the drift of log a is at least alpha_m/2 and its quadratic variation rate is bounded, so log a >= alpha_m u/4
for all large u, almost surely. If the solution lived for all real time, then u(t) >= c' lambda_1^2 t would tend to infinity,
because |W|^2 >= c' a^2 on D. But t = int du/|W|^2 <= int du/(c' a(u)^2) is finite, a contradiction. So the solution explodes,
with a tending to infinity, at a finite real time, and

    P(zeta < infinity) >= 1 - Y(V_0)/y_0                                                                    (4.3)

for V_0 in D. The right side tends to 1 as a_0 -> infinity and |w_0|, Phi_S(V_0) -> 0.

(2) From an arbitrary start. As in Section 5, the diffusion matrix is nondegenerate on the positive-definite cone and the
coefficients are smooth there. Take V* = lambda e_1 e_1^T + eta I with lambda large and eta small, so that V* lies in D and
Y < y_0/2 on a ball B around V*. By the support theorem of Stroock and Varadhan, applied on a compact neighbourhood inside the
cone of a continuous path from V_0 to V*, the solution is in B at a fixed time T with positive probability. The strong Markov
property at T and (4.3) give P(zeta < infinity) >= P(V_T in B)/2 > 0. QED

Two features of the proof are worth recording. The corner exponent along the stratum, (4.2), and the transverse exponent mu_S
have different thresholds: at m = 3 the first is positive for every gamma^2 <= 1 and the second negative, so no choice of
gamma^2 <= 1 removes the explosion. And the natural coordinate (tr V - V_11)/V_11 is the wrong one: it contains |w|^2, which
lies inside the stratum, and its initial growth rate at m = 3, gamma^2 = 1 is positive although the Schur coordinate decays.

## Draft of Section 6: MLP blocks

Corollary 4.3 of Noci et al. adds to the drift

    b_res(V) = gamma^2 ( nu(rho_ij) sqrt(V_ii V_jj) )_ij,   rho_ij = V_ij/sqrt(V_ii V_jj),
    nu(r) = (Delta/(2 pi)) (sqrt(1 - r^2) - r arccos r),   Delta = (c_+ - c_-)^2,

where c_+ and c_- are the slopes of the shaped ReLU, and adds to the noise a term whose covariance is 2 gamma^2 times that of the
linear part. That term has the congruence form sqrt(2 gamma^2) L dH' L^T with H' an independent GOE Brownian motion, so its
only effect is to replace c by c' = c + 2 gamma^2 in the linear noise. Two facts about nu are used throughout: nu(1) = 0, so
b_res has zero diagonal and zero trace; and nu is decreasing on [-1, 1] with nu(-1) = Delta/2.

Positivity. By Section 2, log det V has drift tr(V^-1 b(V)) - (1/2) tr(dGamma^2)/dt, all polynomial in |V|. The MLP adds
tr(V^-1 b_res(V)). The identity sqrt(1 - r^2) - r arccos r = pi (k_1(r) - r), where k_1(r) = 2 E[relu(g) relu(g')] for a
standard Gaussian pair with correlation r is the arc-cosine kernel of degree one, gives, with V = D^(1/2) R D^(1/2) and D = diag V,

    tr(V^-1 b_res(V)) = gamma^2 (Delta/2) tr(R^-1 (k_1(R) - R)) = gamma^2 (Delta/2) (tr(R^-1 k_1(R)) - m) >= -gamma^2 (Delta/2) m,

because the entrywise image k_1(R) is a Gram matrix, hence positive semidefinite, and tr(R^-1 A) >= 0 for A positive
semidefinite. So log det V remains bounded below on every interval on which |V| is bounded, and Theorem 1 holds with MLP blocks.

Theorem 4 with MLP blocks was noted at the end of Section 5: tr b_res = 0, and the extra noise only increases the quadratic
variation in (5.1).

Three or more tokens. Near the corner a e_1 e_1^T the MLP leaves the drift of log a unchanged, since (b_res)_11 = 0, and its
noise adds O(1/a^2) per unit u to every rate, as the linear noise does in Lemma 4.1. Its effect on w is a drift of order
(|w| + Phi_S^(1/2)) per unit t, so the drift of |w|^2 gains at most C(|w|^2 + Phi_S)/a^2 per unit u. The new feature is in tr X:

    d tr X = (attention terms) - 2 sum_{i >= 2} w_i (b_res)_{i1} dt,     |(b_res)_{i1}| <= gamma^2 (Delta/2) (a V_ii)^(1/2),

so that Phi_S receives, per unit u, a forcing F <= C (|w|^2 + |w| Phi_S^(1/2))/a^2 <= C' (|w|^2 + Phi_S)/a^2. The forcing does
not vanish on the stratum: at X = 0 with w_i < 0, token i is anti-aligned with token 1, rho_i1 = -1, and the forcing equals
2 gamma^2 nu(-1) a w_i^2 > 0 per unit t. The MLP pushes two opposed tokens apart, and the rank-one stratum is no longer
invariant. In particular the term M Phi_S^p of Section 4 fails: its generator gains M p Phi_S^(p-1) F, which is unbounded as
Phi_S tends to 0 with w fixed.

The remedy is to measure the transverse coordinate against the scale. Put

    psi = Phi_S + 1/a = (tr X + 1)/a,       Y = a^-q + |w|^2 + M psi^p.

Lemma 6.1. For p small and (1/a, |w|, Phi_S) small, in the clock u,

    drift(psi^p) <= -(p/2) min(|mu_S|, alpha_m) psi^p + p C' |w|^2 a^(-1-p),

where the last term is what remains of the forcing.

Proof. First the forcing. Since psi >= 1/a, psi^(p-1) <= a^(1-p), and so

    p psi^(p-1) F <= p C' (|w|^2 a^(1-p) + psi^(p-1) Phi_S)/a^2 <= p C' (|w|^2 a^(-1-p) + psi^p a^-2).

Next the attention part. Write psi = e^(X_1) + e^(X_2) with X_1 = log Phi_S and X_2 = -log a, and t = Phi_S/psi in [0, 1]. Ito's
formula gives

    drift(psi^p)/(p psi^p) = t drift(X_1) + (1 - t) drift(X_2) + (1/2) t (1 - t) qv(X_1 - X_2) + (p/2) qv(log psi).

Here X_1 - X_2 = log tr X. After the row operation of Lemma 4.1, the attention noise of the lower block is O(a^(1/2) |X|^(3/2)) per
unit square root of t, for every |w| < delta, so qv(log tr X) = O(Phi_S + 1/a^2) per unit u and the third term vanishes at the
corner. By Lemma 4.1, drift(X_1) -> mu_S and drift(X_2) -> -alpha_m, so the right side is at most
t (mu_S + o(1)) - (1 - t)(alpha_m + o(1)) + O(p), which is below -(3/4) min(|mu_S|, alpha_m) uniformly in t for p small. The forcing term p C' psi^p a^-2 is absorbed into this rate once a
is large. QED

The weight 1/a is the only power of a that works. With a^-r in its place, qv(X_1 - X_2) contains (1 - r)^2 qv(log a), which does
not vanish, and the middle of the mixing interval t in [0, 1] acquires a positive term (1/8)(1 - r)^2 sigma_a^2. The choice
r = 1 cancels the noise of log a common to the two summands of psi.

Proof of Theorem 3 with MLP blocks. Take D = {a > lambda_1, |w| < delta, Phi_S < delta} with lambda_1 >= 1/delta, so that
psi < 2 delta on D. The drift of |w|^2 is at most -kappa |w|^2 + C psi <= -kappa |w|^2 + C (2 delta)^(1-p) psi^p. Choose M with
M (p/2) min(|mu_S|, alpha_m) >= 2 C (2 delta)^(1-p), and then lambda_1 so large that M p C' a^(-1-p) <= kappa/2 for a > lambda_1.
With Lemma 6.1, drift(Y) <= 0 on D. On the boundary of D one of a = lambda_1, |w| = delta and
Phi_S = delta holds, and since psi >= Phi_S, Y >= min(lambda_1^-q, delta^2, M delta^p) there. The rest of part (1) of the proof
in Section 4 is unchanged. For part (2): b_res is analytic on the positive-definite cone, because |rho_ij| < 1 off the diagonal
and nu is analytic on (-1, 1), and the linear noise keeps the diffusion matrix nondegenerate. The support argument applies as
before. QED

Two tokens. For m = 2, w = tr(PV) is linear in V. The attention drift of w is kappa w^3 as in Section 3, and the MLP adds
tr(P b_res) = -(b_res)_12 = -gamma^2 nu(rho) (V_11 V_22)^(1/2) =: -theta_t <= 0. The linear noise and the MLP noise are
congruences, and Var tr(P L dH L^T) = 2 |L^T P L|_F^2 dt = 2 w^2 dt, so

    dw = (kappa w^3 - theta_t) dt + sigma(w) d beta,     sigma(y)^2 = (2c + 4 gamma^2) y^2 + 4 k^2 y^4.                 (6.1)

The noise coefficient is a function of w alone; the drift is not. But nu(r) <= (Delta/4)(1 - r) on [-1, 1], with equality at
r = -1, and (V_11 V_22)^(1/2) - V_12 <= (V_11 + V_22)/2 - V_12 = w, so

    0 <= theta_t <= gamma^2 (Delta/4) w_t.

Let w_up and w_lo solve (6.1) driven by the same beta, with theta replaced by 0 and by gamma^2 (Delta/4) y. The coefficients are
locally Lipschitz on (0, infinity), and the comparison theorem of Ikeda and Watanabe, localised to compact subintervals, gives
w_lo <= w <= w_up up to explosion.

Proof of Theorem 2 with MLP blocks. Both comparison diffusions have scale density of order y^(-1/(2 gamma^2)) at infinity, because the linear drift term is
negligible against sigma^2 of order y^4. Near 0 the scale density of w_up is bounded and that of w_lo is of order
y^(gamma^2 Delta/(4(c + 2 gamma^2))); both are integrable, and 0 is not reached, since log y has drift at most -c' < 0 near 0 and
bounded quadratic variation. If gamma^2 >= 1/2, w_up does not explode, so neither does w. If gamma^2 < 1/2, w_lo explodes in
finite time with positive probability by the Feller test, as in Section 3, and w >= w_lo. Finally V is bounded while w is: the
sum S = 1^T V 1 has drift at most (gamma^2 w^2/(4 tau0^2)) S + C w and noise of order (1 + w) S, and |V| <= C (w + S). The upper
bound P(zeta < infinity) < 1 is Theorem 4. QED

The two comparison equations also bracket the probability: P(zeta < infinity) lies between the values of (3.2) computed for
w_lo and w_up.

## Draft of Section 2: the noise in congruence form; positivity

Theorem 4.2 of Noci et al. states the limit as dV = b(V) dt + Sigma(V)^(1/2) dB with Sigma written entry by entry. For our
purposes a different description of the same martingale part is more useful. Write the token representations of one layer as
X = L Q with Q Q^T = n I and V = L L^T. Expanding one layer of the shaped attention to order n^(-1/2), with
Softmax(Z)_ij = (1 + (Z P)_ij)/m + O(|Z|^2), gives

    dV = b(V) dt + L dGamma L^T,     dGamma = sqrt(c) dH + k (dN K + K dN^T),     K = L^T P L,              (2.1)

with c = gamma^2 (2 - gamma^2) and k = gamma^2/(m tau0). Here H is a GOE Brownian motion (diagonal entries of variance 2,
off-diagonal entries of variance 1), coming from the value weights, and N is an m x m matrix of independent Brownian motions,
coming from the query and key weights, independent of H. The covariance of L dGamma L^T is the matrix Sigma(V) of Theorem 4.2,
as an entrywise expansion shows; against one layer of the finite network the discrepancy closes as the width grows (to
0.1 per cent of max |Sigma| at width 160,000). The law of V does not depend on the choice of L, since the covariance of
L dGamma L^T is invariant under L -> L O for O orthogonal.

Two consequences of (2.1) are used repeatedly. First, the noise preserves every stratum of fixed rank, because it acts by
congruence, and so does the drift. Second, the GOE part alone makes the diffusion matrix nondegenerate on the open cone: the map
H -> L H L^T is onto the symmetric matrices when L is invertible.

Proof of Theorem 1. By Ito's formula,

    d log det V = tr(V^-1 b(V)) dt + tr(dGamma) - (1/2) tr(dGamma^2),

and the inverse cancels in the drift term:

    tr(V^-1 b(V)) = (gamma^2/tau0^2) (|W|_F^2/m + D^T v/m),

because tr(V^-1 v (VD)^T) = D^T v. Since |K| <= |V|, the coefficients of d log det V are polynomials in |V|. On the interval
before |V| first reaches r, log det V is therefore a semimartingale with bounded coefficients and cannot reach -infinity. So V
stays positive definite until |V| leaves every bounded set, that is, until zeta. The MLP case is in Section 6. QED

## Draft of Section 1: introduction

Deep transformers at initialization tend to degenerate as depth grows: the representations of different tokens align, and the
network forgets which token is which. One remedy is to shape the attention. Noci et al. scale the logits by a temperature that
grows with the width and centre the softmax, so that each attention layer is the identity plus a perturbation of order
n^(-1/2). With a residual branch of weight gamma, the m x m covariance V of the token representations then has a limit when
the depth d and the width n grow together with d/n -> t: it converges to the solution of the matrix SDE (2.1), with drift b and
the martingale part described in Section 2 (Theorem 4.2 of Noci et al.; Corollary 4.3 adds shaped ReLU MLP blocks).

The convergence is proved up to the exit time of a bounded set, and this restriction is not cosmetic. The drift b is a cubic
polynomial in V, and Noci et al. observe in their Section 4.4 that the limit may become unstable at large depth. Whether
the SDE has a global solution is the question of whether the proportional limit describes the network at every depth-to-width
ratio, or only up to a random one. We answer it for every m >= 2 and every gamma^2 in (0, 1], with and without MLP blocks.

For two tokens the answer is a threshold. The variance w of the difference of the two representations is an autonomous
one-dimensional diffusion, and the Feller test applies: explosion happens with positive probability if and only if
gamma^2 < 1/2, with an explicit probability. For three or more tokens there is no threshold. Explosion always happens with
positive probability, and the reason is a configuration in which a single token carries the variance. Along the set of rank-one
covariances that configuration is exploding for every gamma^2 <= 1 and every m >= 3, and across it the Schur complement of the
large token decays. The proof turns these two exponents into a Lyapunov function near the corner and reaches the corner from
any start by the support theorem. In every case the explosion probability is below one: near the origin the linear part of the
noise dominates the cubic drift.

The MLP blocks change the picture in one place. Their drift does not preserve the rank-one set, because two anti-aligned
tokens are pushed apart, and the transverse coordinate acquires a forcing that the Lyapunov function of the attention-only case
cannot absorb. Measuring the transverse coordinate against the scale, through (tr X + 1)/V_11 instead of tr X/V_11, absorbs it.
For two tokens the MLP breaks the exact reduction, and the threshold survives by comparison with two one-dimensional diffusions.

The criterion is simple enough to read as advice. At the scaling of Noci et al., a long sequence always carries some
probability that the representation of one token runs away at finite depth-to-width ratio, and the probability is not removed
by any residual weight gamma^2 <= 1. The finite-width simulations in their Figure 5 show the same instability.

## Draft of Section 7: numerical illustration

The covariance (2.1) was compared with one layer of the finite network entry by entry: at m = 3, gamma^2 = 1 and scale 12, the
largest gap between the empirical covariance and Sigma(V) is 2.1 per cent of max |Sigma| at width 40,000 and 0.10 per cent at
width 160,000.

The rank-one law (4.1) at u = e_1 was tested on the finite network started with a single nonzero token, which keeps the chain
on the stratum exactly. With width 8000, a_0 = 4 and 3000 runs, the probability of reaching 20 before 0.05 is, for the chain and
for (4.1):

    m = 3, gamma^2 = 1:    0.466 +- 0.009   against 0.470
    m = 3, gamma^2 = 0.5:  0.539 +- 0.009   against 0.545
    m = 4, gamma^2 = 1:    0.554 +- 0.009   against 0.554
    m = 2, gamma^2 = 0.5:  0.367 +- 0.009   against 0.349

The Schur exponent mu_S of Lemma 4.1 against Monte Carlo of the SDE near the corner (400 paths, clock u <= 16):

    m = 3, gamma^2 = 1:    -0.048 +- 0.009   against -0.056
    m = 3, gamma^2 = 0.5:  -0.052 +- 0.004   against -0.056
    m = 4, gamma^2 = 1:    -0.107 +- 0.006   against -0.104

For two tokens, (3.2) at gamma^2 = 0.2, tau0 = 1 and w_0 = 1 gives P(zeta < infinity) = 0.1923. With MLP blocks at Delta = 4 the
comparison of Section 6 brackets the probability in [0.0801, 0.1339]. A Monte Carlo run of the full two-token equation with
MLP blocks (400 paths, Euler step 0.01, run to time 340) gives 44 explosions, 349 paths decided against explosion and 7
undecided, so the fraction lies in [0.110, 0.128], inside the bracket.
