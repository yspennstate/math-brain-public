# The degenerate hub, for every hub law

## Statement

X_h, X_1, ..., X_m are independent real random variables with densities at most 1; f_h is the density of X_h,
f_i that of X_i, and X' = (X_1, ..., X_m). Let l, u in R^m be linearly independent, L = <l, X'>, U = <u, X'>,
G = Gram(l, u), and rho_i = (l_i, u_i). Assume

  (F2) rho_i^T G^{-1} rho_i <= 1/2 for every i,    (F1) u_i^2 <= |u|^2/2 for every i.

Consider

  Q = a X_h^2 + 2 X_h (L + beta) + b_h X_h + sigma L^2 + lambda U^2 + sum_i phi_i(X_i),

where sigma, lambda are nonzero, a, beta, b_h are real, and each phi_i(x) = d_i x^2 + b_i x + c_i is an arbitrary
real quadratic polynomial. The coefficients d_i need not be small.

**Theorem 1.** If a sigma != 1, then

  ||p_Q||_inf <= 2.23 (1.53 B_0)^{6/7},   B_0 = 16.8 |lambda|^{-1/2} |sigma|^{-1/6} |1 - a sigma|^{-1/6} (det G)^{-5/12} |u|^{-1/6},

uniformly in beta, b_h, the phi_i, m and all the laws.

**Theorem 2.** If a = 0, then ||p_Q||_inf <= C(lambda, G, |u|) uniformly in sigma != 0 as well; for sigma = 0
Theorem H of the first record applies directly.

A general quadratic in (L, V) with a square along V reduces to this form: completing the square in V and then in
L (multiscale_fourier/, Lemma 2.1) gives lambda'(V + kappa L + gamma')^2 + sigma L^2 + (linear), and the frame
(l, v + kappa l) has determinant one when l, v are orthonormal.

**Corollary 3 (the degenerate hub).** For w, v orthonormal with w_i^2 + v_i^2 <= 1/2, every diagonal matrix D and
every b, the form 4 X_h L + 2L^2 + 2V^2 + X'^T D X' + <b, X> has density at most 18 for every hub law. Here
L = 2<w, X'> is taken as the hub partner, so sigma = 1/2, lambda = 2, det G = 4, |u| = 1 and B_0 = 7.48.

This is the case M-DEG of architecture/PROOF_TREE.md, which was open for general hub laws (real_variable_hub/
settles interval hub laws, with the bound 8.99). The numerical peak on this family is 1.45 - 1.67.

## Proof of Theorem 1

Write phi(t) = E e^{itQ}. Fix t != 0 and X_h = x. Completing the square,

  t(a x^2 + 2x(L + beta) + b_h x + sigma L^2) = t sigma (L + x/sigma)^2 + t(a - 1/sigma) x^2 + t(2 beta + b_h) x.

Linearise the two squares with the Fresnel identity of multiscale_fourier/, Section 1 (with Gaussian damping, then
dominated convergence):

  e^{it sigma Y^2} = (4 pi i t sigma)^{-1/2} int e^{-i zeta^2/(4 t sigma) + i zeta Y} d zeta,

once with Y = L + x/sigma and once, with lambda in place of sigma, with Y = U. After Fubini the exponent is
linear in (L, U), so the expectation factorises between X_h and the coordinates of X':

  phi(t) = (4 pi i t sigma)^{-1/2} (4 pi i t lambda)^{-1/2} int int e^{-i zeta^2/(4 t sigma) - i xi^2/(4 t lambda)}
           g_h(t(a - 1/sigma), t(2 beta + b_h) + zeta/sigma) prod_i psi_i^{(t)}(zeta l_i + xi u_i + t b_i) d zeta d xi,

with g_h(c, omega) = int f_h(x) e^{icx^2 + i omega x} dx and psi_i^{(t)}(theta) = int f_i(x) e^{i theta x + i t d_i x^2} dx.
The separable part of Q has gone into the coordinate transforms; nothing else of it remains. Hence

  |phi(t)| <= (4 pi |t|)^{-1} |sigma lambda|^{-1/2} int |g_h(t(a - 1/sigma), t(2 beta + b_h) + zeta/sigma)| K_t(zeta) d zeta,
  K_t(zeta) = int prod_i |psi_i^{(t)}(zeta l_i + xi u_i + t b_i)| d xi.

*Bounds for K_t.* Lemma 1 of the first record, int |psi|^p <= 4 pi/sqrt(p) for p >= 2, holds for every modulated
transform psi_i^{(t)}, because only |f_i e^{i t d_i x^2}| = f_i enters. Hoelder with exponents p_i = |u|^2/u_i^2
(at least 2 by (F1)) gives

  ||K_t||_inf <= prod_i (|u_i|^{-1} 4 pi p_i^{-1/2})^{1/p_i} = 4 pi/|u|.

The Brascamp-Lieb bound of multiscale_fourier/, Section 1 (Theorem F of the first record), which holds for all
shifts and needs (F2), gives ||K_t||_1 <= (4 pi)^2 (det G)^{-1/2}. So

  ||K_t||_{6/5} <= ||K_t||_1^{5/6} ||K_t||_inf^{1/6} <= (4 pi)^{11/6} (det G)^{-5/12} |u|^{-1/6}.

*Strichartz step.* Lemma S (multiscale_fourier/, Lemma 3.1): for every density f <= 1,
int int |g(c, omega)|^6 dc d omega <= 4 pi^3/sqrt(3) = C_6^6, C_6 = 2.0377. The proof pushes f x f x f forward
under x -> (sum x_i, sum x_i^2); the fibres are circles and the pushed density is at most pi/sqrt(3). On a dyadic
block T <= t <= 2T apply Hoelder with exponents 6 and 6/5 in (t, zeta). The map
(t, zeta) -> (t(a - 1/sigma), t(2 beta + b_h) + zeta/sigma) is injective with Jacobian |1 - a sigma|/sigma^2, so

  int_T^{2T} |phi| <= (4 pi)^{-1} |sigma lambda|^{-1/2} T^{-1} (sigma^2/|1 - a sigma|)^{1/6} C_6 T^{5/6} (4 pi)^{11/6} (det G)^{-5/12} |u|^{-1/6}
                   = B_0 T^{-1/6}.

The same holds for negative t. Summing the blocks T = 2^k T_0, k >= 0, gives
int_{|t| >= T_0} |phi| <= 2 B_0 T_0^{-1/6}/(1 - 2^{-1/6}) <= 18.33 B_0 T_0^{-1/6}, and trivially
int_{|t| < T_0} |phi| <= 2 T_0. By Fourier inversion

  ||p_Q||_inf <= (2 pi)^{-1} (2 T_0 + 18.33 B_0 T_0^{-1/6}).

The choice T_0 = (1.5275 B_0)^{6/7} gives (14/(2 pi)) T_0 <= 2.23 (1.53 B_0)^{6/7}. ∎

## Proof of Theorem 2

For |sigma| bounded below Theorem 1 suffices. Otherwise follow multiscale_fourier/, Theorem 6.2: its Proposition
4.1 is the high-frequency bound above, and its Proposition 5.1 bounds P(|Q - s| <= delta) <= (6.5 C_H + 2) delta for
delta >= |sigma| by comparing Q on three events with Q_1 = Q - sigma L^2 and Q_2 = Q - sigma (L + beta)^2. Both
comparison forms have one hub, a rank-one block lambda U^2 and a diagonal block, so they are in the class of
Theorem H, which allows an arbitrary diagonal on the non-hub coordinates and arbitrary linear terms; under (F2)
their density is at most a constant C_H depending only on lambda and G (7.56 |lambda'|^{-1/3} in the normalisation
of multiscale_fourier/). The event on which Q is
compared with neither uses only that Q is affine in X_h when a = 0 and X' is fixed, which the separable part does
not affect. Lemma 6.1 there joins the two scales at |sigma|. ∎

## Consequences

- The degenerate hub of the architecture (M-DEG) is closed with zero hub diagonal, for every hub law, every
  diagonal twist and every linear term; with a nonzero hub diagonal it is closed when |sigma| >= sigma_0 and
  |1 - a sigma| >= c. A two-eigenvalue statement such as M-D2 (degenerate_hub_numerics/) is not needed.
- Exact rank three, configuration (O2) of low_rank_plus_diagonal/ (a leak-free hub, a square along the hub partner,
  a linear term outside the range): in its normal form Q = m X_h^2 + 2 kappa X_h S_1 + p S_1^2 + 2q S_1 S_2 + s S_2^2
  + <b, X>, take L = kappa S_1, U = S_2 + (q/s) S_1, lambda = s, sigma = p'/kappa^2 with p' = p - q^2/s, and a = m.
  Then det G = kappa^2, and (F1)-(F2) hold when the light leverages are at most 1/4. So (O2) is closed for m = 0,
  and for m != 0 whenever |p'|/kappa^2 is bounded below and D_H = |1 - m p'/kappa^2| = |det M|/(|s| kappa^2) is
  bounded below. What is left of (O2) is the corner p' -> 0 with m != 0, where Theorem H (p' = 0) and Theorem 1 do
  not meet.
- The separable part of any twist is free in these Fourier arguments. What remains of the canonical family
  star + rank one + eps W is the part of W outside span(w, v) with its diagonal removed, together with the cross
  terms L <r, X'> between the hub partner and outside directions. Completing the square in L turns such a cross term
  into a second, X'-dependent frequency for the hub, and the factorisation above is lost.
