# One hub: interval hub laws, and what is left for the others

X_h, X_1, ..., X_m are independent with densities at most 1; f_h is the density of X_h, f_i that of X_i, and
X' = (X_1, ..., X_m). Throughout, w, v in R^m are orthonormal with w_i^2 + v_i^2 <= 1/2 for every i, and
L = <w, X'>, V = <v, X'>. Every quadratic term of X' that contains L has the form L <q, X'> for some q in R^m, so
the family

  Q = 2 X_h (L + beta) + lambda V^2 + 2 L <q, X'> + sum_i phi_i(X_i),     phi_i(x) = d_i x^2 + b_i x + c_i,     (0.1)

with lambda != 0 and q, beta, d_i, b_i, c_i arbitrary, contains the hub, the square along V, every term of the twist
inside span(w, v), every cross term L <r, X'> between the hub partner and an outside direction, any diagonal and any
linear term. It does not contain a term V <r, X'> with r orthogonal to w and v, or the off-diagonal part of a
quadratic in the coordinates of X' orthogonal to span(w, v); completing the square in V turns the first kind into
the second.

## 1. Hub laws supported in an interval

**Theorem 1.** If X_h is supported in an interval J of length D, then for every Q of the form (0.1)

  ||p_Q||_inf <= (3/2) (4 sqrt 2 pi^2)^{2/3} (D/|lambda|)^{1/3} <= 22 (D/|lambda|)^{1/3}.

No smallness is assumed of q or of the d_i. For a separable remainder this is real_variable_hub/, Theorem A. The
argument is the same: freeze L before any Fourier step. Freezing L also turns each term containing L into a linear
term, so the cross terms cost nothing.

For l in R write Y_l = lambda V^2 + 2 l <q, X'> + sum_i phi_i(X_i), so that Q = 2 X_h (L + beta) + Y_L. For fixed
l_0, let mu_{l_0, l} be the slice at L = l of the joint law of (L, Y_{l_0}); it is defined for almost every l and has
total mass rho_L(l).

**Lemma 1.1 (the frozen slice).** For every l_0, for almost every l and every interval I,
mu_{l_0, l}(I) <= 2 pi^2 (|I|/|lambda|)^{1/2}.

*Proof.* Write Y_{l_0} = lambda V^2 + <c, X'> + sum_i d_i X_i^2 + const with c = 2 l_0 q + b. For eta != 0 the
complex measure A -> E[e^{i eta Y_{l_0}}; L in A] has Fourier transform Phi(zeta, eta) = E e^{i zeta L + i eta Y_{l_0}}.
The Fresnel identity for e^{i eta lambda V^2}, with Gaussian damping and bounded convergence, and Fubini give

  |Phi(zeta, eta)| <= (4 pi |eta lambda|)^{-1/2} int prod_i |psi_i^{(eta d_i)}(zeta w_i + xi v_i + eta c_i)| d xi,

where psi_i^{(tau)}(theta) = int f_i(x) e^{i theta x + i tau x^2} dx. Lemma 1 of the first record, int |psi|^p <= 4 pi/sqrt p
for p >= 2, involves only |f_i e^{i tau x^2}| = f_i, so it holds for these modulated transforms. With
p_i = 1/(w_i^2 + v_i^2) >= 2 the geometric Brascamp-Lieb inequality (Theorem F of the first record, valid for every
shift) gives int int prod_i |psi_i^{(eta d_i)}(zeta w_i + xi v_i + eta c_i)| d zeta d xi <= (4 pi)^2. Hence
int |Phi(zeta, eta)| d zeta <= (4 pi)^{3/2} |eta lambda|^{-1/2}, the measure has a continuous density in l, and for almost every l
the partial transform of the slice satisfies |mu^_{l_0, l}(eta)| <= 2 (4 pi/|eta lambda|)^{1/2} for every eta != 0 (first for
almost every eta by Fubini, then for all by continuity in eta).

Let I have centre y_0 and length 2a, and K(y) = sinc^2(pi (y - y_0)/(4a)). Then K >= (8/pi^2) 1_I, and K^ is supported in
|eta| <= pi/(2a) with |K^| <= 4a. By Parseval,

  mu(I) <= (pi^2/8)(2 pi)^{-1} int |K^(eta)| |mu^(eta)| d eta
         <= (pi^2/8)(2 pi)^{-1} 4a int_{|eta| <= pi/(2a)} 2 (4 pi/|lambda|)^{1/2} |eta|^{-1/2} d eta = 2 pi^2 (|I|/|lambda|)^{1/2}. ∎

*Proof of Theorem 1.* Fix s and delta > 0, and write t = l + beta. Since f_h <= 1_J,

  P(|Q - s| <= delta) <= E G(L, Y_L),   G(l, y) = |{x in J : |2 x t + y - s| <= delta}| = (2|t|)^{-1} |(s - y + [-delta, delta]) cap 2tJ|.

G is bounded by D and continuous at every (l, y) with t != 0. Cut the line into cells C_k of width h with points
l_k in C_k. As h -> 0, sum_k G(l_k, Y_{l_k}) 1{L in C_k} -> G(L, Y_L) almost surely, because Y_{l_k} - Y_L =
2 (l_k - L) <q, X'>. By dominated convergence,

  E G(L, Y_L) = lim_{h -> 0} sum_k int_{C_k} dl int G(l_k, y) mu_{l_k, l}(dy).

For fixed k and t = t_k != 0 put mu = mu_{l_k, l}. Three bounds hold. First, G(l_k, .) <= delta/|t|, which is used where
|t| >= T and there contributes at most (delta/T) int rho_L <= delta/T. Second, int G(l_k, y) mu(dy) <= (2|t|)^{-1} 2 delta
mu(s - 2tJ + [-delta, delta]) <= (delta/|t|) 2 pi^2 ((2|t| D + 2 delta)/|lambda|)^{1/2} by Lemma 1.1. Third,
int G(l_k, y) mu(dy) = (2|t|)^{-1} int_{2tJ} mu(s - u + [-delta, delta]) du <= D 2 pi^2 (2 delta/|lambda|)^{1/2}. The Riemann sums
converge, so

  P(|Q - s| <= delta) <= delta/T + int_{|t| < T} min{ (delta/|t|) 2 pi^2 ((2|t| D + 2 delta)/|lambda|)^{1/2}, 2 pi^2 D (2 delta/|lambda|)^{1/2} } dt.

Divide by 2 delta. On |t| < delta the integrand is at most (pi^2 D/delta)(2 delta/|lambda|)^{1/2}, so that range contributes
O(delta^{1/2}). On delta <= |t| < T the integrand is at most pi^2 (2(D + 1)/|lambda|)^{1/2} |t|^{-1/2}, because delta <= |t|, and it
tends to pi^2 (2D/|lambda|)^{1/2} |t|^{-1/2}. Hence for every s

  limsup_{delta -> 0} P(|Q - s| <= delta)/(2 delta) <= 1/(2T) + 4 sqrt 2 pi^2 (D T/|lambda|)^{1/2},

and the choice T = (4 sqrt 2 pi^2)^{-2/3} (D/|lambda|)^{-1/3} gives the bound. ∎

If X_h has density at most M, the same proof gives M times the bound for the Lebesgue measure on J. So for a hub
coefficient 2 kappa X_h (L + beta) the bound becomes 22 kappa^{-2/3} (D/|lambda|)^{1/3}. For the degenerate hub
4 X_h L + 2L^2 + 2V^2 + X'^T D X' + <b, X> with X_h supported in a unit interval, this gives about 11, now with any L-cross
terms added.

## 2. Arbitrary hub laws: splitting the hub law

**Lemma 2.1.** For every Q = 2 X_h (L + beta) + Y(X'), every c in R and every r_0 > 0,

  ||p_Q||_inf <= sup_s limsup_{delta -> 0} (2 delta)^{-1} int_{|x - c| <= r_0} P(|Q(x, X') - s| <= delta) dx + sup_{|x - c| > r_0} ||p_{Q(x, .)}||_inf,

where Q(x, .) is Q with X_h = x. For Q of the form (0.1), the first term is at most 22 (2 r_0/|lambda|)^{1/3}.

*Proof.* P(|Q - s| <= delta) = int f_h(x) P(|Q(x, X') - s| <= delta) dx. Use f_h <= 1 on |x - c| <= r_0 and
int f_h <= 1 elsewhere. The first term is the quantity bounded in the proof of Theorem 1 with J = [c - r_0, c + r_0]. ∎

So (0.1) is bounded for every hub law as soon as the frozen-hub forms Q(x, .) are bounded for x away from a centre c.
Write b = b_w w + b_v v + b_perp with b_perp orthogonal to w and v, and take c = -b_w/2. Then
Q(x, .) = 2 x~ L + lambda V^2 + 2 L <q, X'> + (separable), with x~ = x + b_w/2 and no linear term along w left in the
separable part.

*Without cross terms the frozen-hub forms are bounded.* Let q = 0, u = 2 x~ w + b_perp, and suppose the frame (u^, v)
satisfies u^_i^2 + v_i^2 <= 1/2. Fresnel in V and the substitution zeta = t|u| give

  ||p|| <= (2 pi)^{-1} (4 pi |lambda| |u|)^{-1/2} int |zeta|^{-1/2} int prod_i |psi_i(zeta u^_i + xi v_i)| d xi d zeta
        <= (2 pi)^{-1} (4 pi |lambda| |u|)^{-1/2} (16 pi + 16 pi^2),

using the one-dimensional bound in xi for |zeta| <= 1 and the two-dimensional one for |zeta| > 1. Here |u| >= 2 r_0.

*With a cross term they are not, uniformly.*

**Example 2.2.** Let q = eps q^ with q^ a unit vector orthogonal to w and v, fix x~ = r_0, and let X' = c + G, where
c = -(r_0/eps) q^ and G has independent standard Gaussian coordinates (density at most (2 pi)^{-1/2} < 1). Then
<q^, X'> = -r_0/eps + <q^, G>, and the frozen-hub form is

  2 r_0 L + lambda V^2 + 2 eps L <q^, X'> = lambda <v, G>^2 + 2 eps <w, G><q^, G>,

a form with no linear term whose quadratic part has eigenvalues lambda and +-eps. Since <v, G>, <w, G>, <q^, G> are
independent standard Gaussians, its density at 0 is, for lambda > 0,

  (4 pi lambda eps)^{-1/2} pi^{-1} int_0^inf u^{-1/2} e^{-eps u/lambda} K_0(u) du  ~  0.417 (lambda eps)^{-1/2}   (eps -> 0),

using the density K_0(|y|)/pi of a product of two independent standard Gaussians and
int_0^inf u^{-1/2} K_0(u) du = 2^{-3/2} Gamma(1/4)^2. So no bound on the frozen-hub densities can hold uniformly in q,
for any r_0: a translate of the law of X' puts the point where x~ + <q, X'> vanishes wherever it is needed.

In the example the full Q is not in danger. At hub value x, the frozen form has effective slope 2(x - r_0) along L, and
its density is of order (|lambda| |x - r_0|)^{-1/2} away from x = r_0, which the hub law integrates. The point is that
the degenerate hub value x~ = -<q, X'> depends on X', so the hub law cannot be split off before L is frozen. For
cross terms and arbitrary hub laws the route that remains is the frozen-L bathtub of Section 3, except when the cross
term is not small.

*Cross terms of moderate size.* Integrating the hub in Fourier and keeping the partner P = <q^, X'> of the cross term
as a variable of the Parseval step gives a bound for every hub law, with any diagonal on the hub and on the light
coordinates.

**Proposition 2.3.** Let Q = a X_h^2 + 2X_h(L + beta) + lambda V^2 + 2 L <q, X'> + sum_i phi_i(X_i) with
q = q_w w + q_v v + eps q^, where q^ is a unit vector orthogonal to w and v, eps > 0, and a, beta, q_w, q_v and the
phi_i(x) = d_i x^2 + b_i x + c_i are arbitrary. Suppose w_i^2 + v_i^2 + q^_i^2 <= 1/2 for every light coordinate. Then
for every law of X_h with density at most 1,

  |E e^{i eta Q}| <= 31.5 |eta|^{-3/2} (eps |lambda|)^{-1/2}   and   ||p_Q||_inf <= 9.6 (eps |lambda|)^{-1/3}.

*Proof.* Put P = <q^, X'>. Completing the square, lambda V^2 + 2 q_v L V = lambda V'^2 - (q_v^2/lambda) L^2 with
V' = V + (q_v/lambda) L, so Q = a X_h^2 + 2X_h(L + beta) + sigma L^2 + lambda V'^2 + 2 eps L P + sum_i phi_i(X_i) with
sigma = 2 q_w - q_v^2/lambda. Write 2 eps L P = 2 eps (L + beta) P - 2 eps beta P and
W = lambda V'^2 - 2 eps beta P + sum_i phi_i(X_i). Integrating out X_h,

  E e^{i eta Q} = E[H(L, P) e^{i eta W}],   H(l, p) = g(2 eta (l + beta)) e^{i eta sigma l^2 + 2 i eta eps (l + beta) p},
  g(omega) = int f_h(x) e^{i eta a x^2 + i omega x} dx.

Let n(l, p) be the density of the complex measure E[e^{i eta W}; (L, P) in .]. Its Fourier transform
n^(zeta, gamma) = E e^{i zeta L + i gamma P + i eta W} is integrable, by the Fresnel identity in V and the
three-dimensional Brascamp-Lieb bound. In the Fourier transform of H the integral over p forces l + beta =
-gamma/(2 eta eps), and then e^{i zeta l} and e^{i eta sigma l^2} are unimodular constants, so
|H^(zeta, gamma)| = (pi/|eta eps|) |g(-gamma/eps)| for all zeta. Parseval, with Gaussian damping and dominated
convergence, gives

  |E e^{i eta Q}| <= (2 pi)^{-2} (pi/|eta eps|) int |g(-gamma/eps)| G(gamma) d gamma,   G(gamma) = int |n^(zeta, gamma)| d zeta.

The Fresnel identity for lambda V'^2 puts a frequency xi on V' = V + (q_v/lambda) L, that is xi on V and
xi q_v/lambda on L, and the integral over zeta does not see that shift. Hence
G(gamma) <= (4 pi |eta lambda|)^{-1/2} int int |prod_i psi_i^{(eta d_i)}(zeta w_i + xi v_i + (gamma - 2 eta eps beta) q^_i + eta b_i)| d zeta d xi.
Theorem F bounds the double integral by (4 pi)^2 for every gamma. The same inequality in three dimensions, with
p_i = 1/(w_i^2 + v_i^2 + q^_i^2) >= 2, bounds its integral over gamma by (4 pi)^3. Hence ||G||_2 <= (4 pi |eta lambda|)^{-1/2} (4 pi)^{5/2}. Plancherel for the
chirp-modulated hub law gives int |g(gamma/eps)|^2 d gamma = 2 pi eps int f_h^2 <= 2 pi eps. Cauchy-Schwarz in gamma
gives the first bound, and p_Q(s) <= (2 pi)^{-1} int min(1, A |eta|^{-3/2}) d eta = (3/pi) A^{2/3} with
A = 31.5 (eps |lambda|)^{-1/2} gives the second. ∎

So the part of the cross term inside span(w, v) costs nothing here, and (0.1) with any hub diagonal is bounded for
every hub law as soon as the orthogonal part eps of q is bounded below; at eps = 0 it is bounded by degenerate_hub/.
In rank-three terms eps is the tilt of the hub: 2L(X_h + eps P) = 2 (1 + eps^2)^{1/2} L U with U = <u, X>, u = (e_h +
eps q^)/(1 + eps^2)^{1/2}, so the hub coordinate has leverage 1/(1 + eps^2) in the frame (w, u, v). Once that leverage
is at most 1 - delta, eps is at least delta^{1/2} and the constant is at most 9.6 delta^{-1/6} |lambda|^{-1/3},
whatever the hub law. The factor eps^{-1/2} is the only loss. It comes from pairing |g(-gamma/eps)|, which is spread
over |gamma| up to eps times the frequency scale of f_h, with G. If f_h^ is integrable and a = 0, bounding G by its
supremum instead gives |E e^{i eta Q}| <= (4 pi |eta|)^{-1} (4 pi |eta lambda|)^{-1/2} (4 pi)^2 ||f_h^||_1, which does
not depend on eps. What Proposition 2.3 leaves open is therefore the nearly aligned regime, eps -> 0 with a hub law
that is rough at small scales, which is the regime of Example 2.2. The route through Theorem H would also cover it,
given a frame bound with the twist e^{i kappa L P} for kappa up to a constant. On the four-coordinate Walsh frame,
where (w, v, q^) is not spread, that twist lowers the frame integral, like an orthogonal twist and unlike an aligned
one (num/, Section 1). Such a bound cannot come from the lattice structure of the laws alone. If W, V, P in Z^m are
pairwise orthogonal with P = alpha W + beta V modulo q in every coordinate, then at kappa_0 = 2 pi |W| |P|/q the twist
restricted to Z^m equals e^{2 pi i a (alpha a + beta b)/q} with a = <W, k>, b = <V, k>, a Gauss phase in the
integrated variables, which is an aligned twist. For W = (1,1,1,1,1), V = (2,-1,1,0,-2), P = (2,0,-2,-1,1) and q = 5
(alpha = beta = 4), comb laws of four teeth give J(kappa)/J(0) between 2.7 and 3.5 for kappa between kappa_0/2 and
1.06 kappa_0, largest at kappa_0 (num/, Section 6). That frame is not spread and J(kappa_0) stays below the untwisted
constant (4 pi)^2, so it does not contradict the frame bound, but a proof has to use the spread of the frame and not
only the size of kappa. The spread does not rescue it either. On a frame spread in three dimensions (eight
coordinates, every leverage 3/8, an irrational basis) the twist raises the two-dimensional frame integral by a factor
that grows with the number of teeth of comb laws at the integers at every fixed kappa, while the density of Q does not
move; for fine combs of bounded range it stays flat, so the spread of the laws drives the growth (num/, Section 13).
The values computed stay below (4 pi)^2, but the steady growth indicates that no frame bound uniform in the laws
holds, so this route has to use more than the size of the frame integral. A twist orthogonal to the frame does not
show this: for kappa P^2 the same integral stays flat in N, and for kappa bounded below it is at most (4 pi)^{5/2}
|kappa|^{-1/2} by the Fresnel identity in P (num/, Section 13); the growth comes from the partner L inside the twist,
which shears the integration in its frequency.

The frame bound needed there does hold, for every kappa, when the partner of the cross term lives on coordinates away
from part of the frame.

**Proposition 2.4 (localised cross terms).** Let Q = a X_h^2 + 2X_h(L + beta) + lambda V^2 + 2 eps L P + sum_i phi_i(X_i)
with P = <q^, X'>, q^ a unit vector orthogonal to w and v supported on a set T of light coordinates, eps real of any
size, and a, beta and the phi_i arbitrary. Let I be the light coordinates outside T and G_I = sum_{i in I} (w_i, v_i)
(w_i, v_i)^T, and suppose G_I is invertible with (w_i, v_i) G_I^{-1} (w_i, v_i)^T <= 1/2 for i in I. Then for every hub law

  |E e^{i eta Q}| <= 22.3 |eta|^{-3/2} (|lambda| det G_I)^{-1/2},   ||p_Q||_inf <= 7.6 (|lambda| det G_I)^{-1/3}.

*Proof.* Integrating the hub in Fourier and using Parseval in l as in Theorem H, |E e^{i eta Q}| <= (2|eta|)^{-1}
int |n^(zeta)| d zeta with n^(zeta) = E e^{i zeta L + i eta (lambda V^2 + 2 eps L P + sum_i phi_i(X_i))}; the hub
diagonal only multiplies f_h by a unimodular chirp. The Fresnel identity in V bounds int |n^| by
(4 pi |eta lambda|)^{-1/2} J, where J = int int |T(zeta, xi)| d zeta d xi and T(zeta, xi) = E e^{i zeta L + i xi V +
i kappa L P + i eta sum_i phi_i(X_i)}, kappa = 2 eta eps. Let S(zeta, xi; p) be the density at P = p of the complex
measure E[e^{i zeta L + i xi V + i eta sum_i phi_i}; P in .]. Conditioning on P turns the twist into a shift in zeta:
T(zeta, xi) = int S(zeta + kappa p, xi; p) dp. Hence, by the triangle inequality and a translation in zeta,
J <= int int int |S(zeta, xi; p)| dp d zeta d xi, whatever kappa is. The measure factors into the coordinates of I,
which do not carry P, and those of T, whose modulated laws push forward to a complex measure on the P-line of total
variation at most 1. So int |S(zeta, xi; p)| dp <= prod_{i in I} |psi_i^{(eta d_i)}(zeta w_i + xi v_i + eta b_i)|, and the
geometric Brascamp-Lieb inequality in the coordinates G_I^{1/2}(zeta, xi) bounds the remaining integral by
(4 pi)^2 (det G_I)^{-1/2}. This gives the first bound with 22.3 = (4 pi)^{3/2}/2, and the second as in Proposition 2.3. ∎

The same argument bounds the frame integral with the twist e^{i kappa L P} by the average over P of the frame integral
of the conditional law of (L, V) given P, for every kappa and every configuration. That average is finite in general
only when part of the frame lives away from P: for an irrational q^ and lattice laws, conditioning on P fixes every
coordinate up to its tooth, and the average is of order N^2. So localised leakage is covered uniformly in its size,
and spread leakage of moderate size by Proposition 2.3. What remains is spread leakage of small size.

For exact rank three this is case (O1) of low_rank_plus_diagonal/, whose hub direction sqrt(l_h) e_h + eps w is the
tilted hub above. Its Theorem 3.1(c1) conditions on X_h and gives 12 (|det M| eps^2)^{-1/3}. Proposition 2.3 has
eps^{-1/3} in place of eps^{-2/3} and allows any hub and light diagonal. For frames with leverages at most 1/50, (c2)
combines the bound 41.6/|t| from decoupling with a bound C eps^{-1} |t|^{-3/2}, which gives 41 + 27 log_+(1/(6 eps)).
With Proposition 2.3 in the second place the crossover moves to |t| of order 1/eps, and the logarithm remains. It comes
from the band 1 <= |t| <= 1/eps, where the twist strength kappa = 2 |t| eps is at most 2. There a frame bound for
e^{i kappa L P} with kappa <= 2 would give |E e^{itQ}| <= C |t|^{-3/2} through Theorem H, and remove the logarithm; by the
numerics of num/, Section 13, such a bound is not to be expected uniformly in the laws on spread frames.

## 3. The bathtub for arbitrary hub laws, and the fold

The hub bathtub of counterexample_search/, Proposition S does not need the square-root profile. It needs only
some power of |S|.

**Lemma 3.1.** Let Q = 2 X_h (L + beta) + Y_L as above, and let 0 < theta <= 1. Suppose that for every l_0, almost every
l and every Borel set S, mu_{l_0, l}(S) <= K |S|^theta. Then ||p_Q||_inf <= 1/2 + 2^theta K/theta for every hub law.

*Proof.* Now G(l, y) = int f_h(x) 1{|2 x t + y - s| <= delta} dx. As a function of y it lies in [0, delta/|t|], has
integral 2 delta, and is Lipschitz with constant 1/|t|; also G <= 1. The discretisation of the proof of Theorem 1
applies unchanged. The layer-cake formula and Jensen's inequality give
int G(l_k, y) mu(dy) <= (delta/|t|) K (2|t|)^theta. For |t| >= 1 use G <= delta/|t| <= delta. Then

  (2 delta)^{-1} P(|Q - s| <= delta) <= 1/2 + K int_{|t| < 1} (2|t|)^{theta - 1} dt = 1/2 + 2^theta K/theta. ∎

The square-root profile theta = 1/2 is that of a single square; any smaller power suffices.

The hypothesis of Lemma 3.1 concerns the slices of Y_{l_0} = lambda V^2 + X'^T E X' + <c, X'> + const at L = l,
where E is the part of the twist not containing L. After completing the square in V,
Y_{l_0} = lambda' (V - V_0)^2 + G(Z), where Z is the component of X' orthogonal to span(w, v). The derivative of a
quadratic along v is affine, so V - V_0 = <v + a, X'> + a_0 is a linear form with |v + a| >= 1. The fold slab
{|V - V_0| <= r} therefore has mass at most 4r in every slice, by the bound 2 for two-dimensional marginals of
orthogonal projections. Away from the slab, the level sets of Y_{l_0} are graphs over the fold hyperplane. If the
density there is at most K_1/(|lambda'| r), then Lemma 3.1 holds with theta = 1/2 and K = 4 sqrt(K_1) |lambda'|^{-1/2}
(take r = (K_1 |S|/(4 |lambda'|))^{1/2}).

When E = 0 and the d_i vanish, the cross terms have gone into c, and on the slice L = l the form is
lambda (V - V_0)^2 + beta <b^, X'> + const with V_0 constant and b^ the unit vector along the part of c orthogonal to w
and v. Conditioning on <b^, X'> and using |d(lambda V^2)/dV| >= 2 |lambda| r away from the fold, the density there is at
most (|lambda| r)^{-1} M, where

  M = sup_{l, b^} int sup_u rho_{L, V, <b^, X'>}(l, u, s) ds,

the supremum over l and over unit vectors b^ orthogonal to w and v (the direction of c_perp moves with l_0). So (0.1)
without diagonal has density at most 1/2 + 8 sqrt 2 max(M, 2)^{1/2} |lambda|^{-1/2} for every hub law (the 2 covers
c_perp = 0, where the bound 2 for (L, V) gives the same estimate directly). The same argument needs no linear
structure beyond the square:

**Theorem 3.2 (anything on a fixed projection).** Let X_h have any density at most 1. Let w, v be orthonormal, and for
each l let E(l) be a k-dimensional subspace orthogonal to w and v, depending measurably on l. Let

  Q = 2 X_h (L + beta) + lambda V^2 + 2 V g(L, Z) + F(L, Z),   Z = P_{E(L)} X',

with lambda != 0 and g, F arbitrary measurable functions. Then ||p_Q||_inf <= 1/2 + 8 M_k |lambda|^{-1/2}, where
M_k = sup_l int_{R^k} sup_u rho_{L, V, Z}(l, u, z) dz is computed for the frame (w, v, E(l)).

*Proof.* Q is a function of (X_h, L, V, Z), so the slices of (L, Y), Y = Q - 2 X_h (L + beta), are push-forwards of the
slices of the (k+2)-dimensional law of (L, V, Z); no discretisation is needed. On the slice L = l, write
Y = lambda (V - V_0(z))^2 + F_0(z) with V_0 = -g/lambda. Conditioning on Z = z, the fold slab |V - V_0(z)| <= r has mass at
most 2 r M_k, and off the slab the density of Y is at most M_k/(|lambda| r), since each of the two branches has
|dY/dV| >= 2 |lambda| r. With r = (|S|/(2|lambda|))^{1/2} this gives mu_l(S) <= 2 sqrt 2 M_k (|S|/|lambda|)^{1/2}, and
Lemma 3.1 with theta = 1/2 finishes. ∎

No leverage condition enters: the fold slab and M_k use only the bound 2^{(k+2)/2} for (k+2)-dimensional orthogonal
projections of product densities. What Theorem 3.2 needs is a bound on the maximal quantity M_k. For light coordinates
of bounded support it holds:

**Proposition 3.3.** If every X_i (i != h) is supported in an interval of length at most K, then
M_k <= 2^{(k+2)/2} K^k int_{R^k} exp(-2 (|y| - k - 2)_+^2) dy. For k = 1 this is at most 20.5 K. Hence (0.1) without
diagonal, with any cross terms and any linear terms, has density at most 1/2 + 51.2 (K/|lambda|)^{1/2} for every hub law.

*Proof.* Tilt the law of X' by e^{<theta, Z>}. The tilted coordinates stay independent, with densities at most
e^{|theta| |P_E e_i| K} <= e^{|theta| K}, since e^{<theta, P_E e_i> x} varies by at most that factor over the support of X_i.
Scaling each coordinate by its density bound and using the bound 2^{(k+2)/2}/sqrt(det) for a non-orthonormal frame,
the tilted density of (L, V, Z) is at most 2^{(k+2)/2} e^{(k+2) |theta| K}. Undoing the tilt,

  rho_{L,V,Z}(l, u, z) = e^{-<theta, z>} E[e^{<theta, Z>}] rho^theta(l, u, z) <= 2^{(k+2)/2} exp((k+2)|theta| K - <theta, z - EZ> + |theta|^2 K^2/8),

by Hoeffding's lemma (Z - EZ is a sum of independent vectors with |<theta, P_E e_i>| X_i ranging over an interval of
length |<theta, P_E e_i>| K). Taking theta along z - EZ with |theta| = 4 (|z - EZ| - (k+2)K)_+/K^2 gives
sup_u rho_{L,V,Z}(l, u, z) <= 2^{(k+2)/2} exp(-2 (|z - EZ| - (k+2)K)_+^2/K^2), and integrating over z gives the bound.
For k = 1 the integral is 2(k+2) + (pi/2)^{1/2} = 7.25, and 2^{3/2} x 7.25 = 20.5. For (0.1) the form on each slice has
V_0 constant, so the slab has mass at most 4r and the square-root version of the estimate applies:
1/2 + 8 sqrt 2 (20.5 K)^{1/2} |lambda|^{-1/2}. ∎

The same maximal quantities also take a nonzero hub diagonal, through the random-centre argument of
hub_with_diagonal/, Section 3.

**Theorem 3.4 (a hub diagonal as well).** Let X_h have any density at most 1, w, v orthonormal, E a fixed k-dimensional
subspace orthogonal to w and v, and Z = P_E X'. Let

  Q = a X_h^2 + 2 X_h (L + beta) + lambda V^2 + 2 V (g_0(Z) + g_1 L) + f_2 L^2 + f_1(Z) L + f_0(Z),

with a, beta, g_1, f_2 real, lambda != 0, and g_0, f_1, f_0 arbitrary measurable. Put sigma_c = f_2 - g_1^2/lambda and
D_H = 1 - a sigma_c, and suppose D_H != 0. Then

  ||p_Q||_inf <= 1 + 9.05 |lambda|^{-1/2} |D_H|^{-1/4} N_k,
  N_k = int [ 4 sup_{l,u} rho_{L,V,Z}(l, u, z) + int sup_u rho_{L,V,Z}(l, u, z) dl ] dz.

*Proof.* Write Y for the part of Q without X_h, and complete the square: Y = lambda (V - V_0)^2 + C(L, Z) with
C = sigma_c L^2 + phi_1(Z) L + phi_0(Z). For phi >= 0, conditioning on (L, Z) and changing variables in V,

  (wSQ)   E phi(L, Y) <= |lambda|^{-1/2} int int w(l, z) int phi(l, r) |r - C(l, z)|^{-1/2} dr dz dl,   w = sup_u rho_{L,V,Z}.

This is hypothesis SQ of hub_with_diagonal/ with the probability weight of (L, Z) replaced by w. By Lemma 1.1-1.4 there,
p_Q(s) <= 1 + T(s), where T(s) = E K_s(L + beta, Y) collects the roots of the hub quadratic with |a x + t| < 1.
Applying (wSQ) to phi = K_s, then Lemma 1.4(ii) and Lemma 3.2 there (the one-dimensional kernel
J_a(t, sigma) <= 9.05 |t^2 + a sigma|^{-1/4}),

  T(s) <= 9.05 |lambda|^{-1/2} int int w(l, z) |Delta(l, z)|^{-1/4} dz dl,   Delta = (l + beta)^2 + a (s - C(l, z)).

For fixed z, Delta is a quadratic in l with leading coefficient D_H, so |Delta| >= |D_H| |l - m_1| |l - m_2| (with the real
part of the roots if they are complex). Cauchy-Schwarz in l and
int w(l, z) |l - m|^{-1/2} dl <= 4 sup_l w(l, z) + int w(l, z) dl finish the proof. ∎

For light coordinates supported in intervals of length at most K, the tilt of Proposition 3.3, taken along span(w, E),
gives sup_u rho_{L,V,Z}(l, u, z) <= 2^{(k+2)/2} exp(-2 (|(l, z) - E(L, Z)| - (k+2)K)_+^2/K^2). Hence N_k <= C_k K^k + C'_k K^{k+1}, and
for k = 1, N_1 <= 82 K + 118 K^2.

**Corollary 3.5 (window laws, universal constants).** Suppose every light coordinate has a law of the form
U[0, 1] * nu_i, i.e. a density x -> nu_i((x - 1, x]) for some probability measure nu_i. Write X_i = U_i + Y_i with U_i
uniform on [0, 1] and Y_i ~ nu_i, and condition on Y. Given Y the light coordinates are uniform on unit intervals, and
the hypotheses of Theorems 3.2 and 3.4 are statements about the function Q, not about the laws, so they survive the
shift. Hence, for every hub law and uniformly in the nu_i, (0.1) without diagonal has density at most
1/2 + 51.2 |lambda|^{-1/2}, and the family of Theorem 3.4 with k = 1 has density at most
1 + 1810 |lambda|^{-1/2} |1 - a sigma_c|^{-1/4}. The class contains the uniform laws on intervals of integer length,
their mixtures and their convolutions with anything, but no law with structure below unit scale.

*Consequence for exact rank three.* If A has exact rank three and h is a coordinate, then collecting the terms in X_h
gives Q = a X_h^2 + 2 X_h (L + beta) + Y(X') with a = a_hh and Y of rank at most three in X'. The matrix of Y lives on a
three-dimensional space containing the direction of L; choosing v in that space orthogonal to L along the eigenvector
of largest modulus of the remaining 2 x 2 block puts Y in the form of Theorem 3.4, with k = 1, or k = 2 when the linear
term leaves that space. So when every coordinate other than h is supported in an interval of length at most K, exact
rank three is bounded for every law of X_h, with a constant depending on K, on the eigenvalue lambda of that 2 x 2 block
and on D_H; by Corollary 3.5 the constant does not depend on the laws when the light laws are window laws U[0, 1] * nu. This covers the leaking hub (O1), the leak-free hub with a square along the partner (O2) including its corner
p' -> 0, and non-spread light frames or a second heavy row (O3) of low_rank_plus_diagonal/. It does not cover light laws
of unbounded support, and it does not replace the universal constants of that report.

**Corollary 3.6 (light laws of bounded variation).** Suppose every light coordinate has a law g_i * nu_i, with g_i a
density of total variation at most T and nu_i any probability measure. Then for every hub law (0.1) without diagonal
has density at most 1/2 + C (1 + T)^3 |lambda|^{-1/2}, and the family of Theorem 3.4 with k = 1 has density at most
1 + C (1 + T)^3 |lambda|^{-1/2} |1 - a sigma_c|^{-1/4}, with C absolute; with k = 2 the power of 1 + T is 4. Unimodal densities
at most 1 have T <= 2.

*Proof.* Condition on the nu_i-parts as in Corollary 3.5, and write each g_i by the layer-cake formula as the mixture of
the uniform laws on the component intervals J of its superlevel sets {g_i > t}, chosen with weight |J| dt; then
E[1/|J|] = TV(g_i)/2 <= T/2 (extremal_laws/, Corollary 4.4). Given the intervals, the light coordinates are uniform on
intervals of lengths l_i, and (L, V, Z) has a log-concave density rho on R^{k+2} with covariance
Sigma = (1/12) sum_i l_i^2 rho_i rho_i^T, where rho_i collects the i-th entries of w, v and an orthonormal basis of E.
A log-concave density satisfies rho(x) <= C (det Sigma)^{-1/2} exp(-c |Sigma^{-1/2}(x - mu)|); minimising over u replaces
Sigma^{-1} by the inverse covariance of (L, Z), and integrating out the remaining variables gives, with s^2(A|B) the
conditional (Schur-complement) covariance, M_k <= C (s^2(L) s^2(V | L, Z))^{-1/2} and
N_k <= C (det s^2((L, V) | Z)^{-1/2} + s^2(V | L, Z)^{-1/2}). Schur complements increase with Sigma, so both right sides
decrease as Sigma increases, and each l_i may be replaced by min(l_i, 1). Then tr Sigma <= 1/3, so each Schur complement
above, being det Sigma divided by the determinant of a block of Sigma, has determinant at least det Sigma, and both
bounds are at most C (det Sigma)^{-1/2}. By Cauchy-Binet, det Sigma is 12^{-(k+2)} times the sum over (k+2)-sets S of the
products of l_i^2 over S times the squared minors of the frame, whose sum is 1, and convexity of x^{-1/2} gives
E (det Sigma)^{-1/2} <= 12^{(k+2)/2} (1 + T/2)^{k+2}, as E[1/min(l_i, 1)] <= 1 + T/2. Theorems 3.2 and 3.4 hold for each
conditioned configuration, and the density of Q is the average over the configurations. ∎

So (0.1) at a = 0 without light diagonal, the leaking hub and every cross term included, is bounded for every hub law
when the light laws are unimodal, or of bounded variation, or such laws convolved with anything, and by the
consequence above so is exact rank three, with the constant depending only on lambda and D_H. A comb with K teeth has
total variation 2K and the bound grows with K; a comb whose teeth are narrower than its gaps has no factor g * nu with g
unimodal and at most 1, since g would have to fit inside one tooth. Those laws are what stays open. For the leaking hub
on a random frame with m = 8 and an exact best-response hub law, light laws with density e^{-2|x|} give 0.21 to 0.53 on
both sides at eps = 0.1 and 0.01, below the 0.34 to 0.87 of unit intervals (num/hub_unimodal_check.py).

So for light coordinates of bounded support every term that contains L, every term V <r, X'> and every twist of fixed
rank k on the orthogonal coordinates are harmless for every hub law, with constants that grow with K and k. What is
not covered is a full-rank twist (the diagonal included) and light laws spread over unbounded ranges, where the
tilt does not control M. For those the maximal route itself fails. In num/ the two-dimensional version M_2 grows like
N not only for two comb coordinates (the case of low_rank_plus_diagonal/, Section 3.3) but also for three coordinates
whose projection has the rational fibre (1,1,1) and an irrational basis of the orthogonal plane: 2.1, 5.4, 11.0 at
N = 4, 8, 16, against 2.1-2.3 for a rational basis. The fibre lines then run along lattice diagonals through N teeth,
their N^2 images have distinct s-coordinates, and the supremum over u, which may pick a different u for each s, finds
one for almost every s. The fold argument needs less than that supremum: the density of lambda (V - V_0)^2 + beta B
away from the fold, that is an X-ray bound along the parabolas lambda (u - V_0)^2 + beta s = y. A parabola cannot follow
the projected lattice the way the supremum does, and for random frames with m >= 6 even the supremum matches the
uniform control. The open statement is therefore

  (CS)   for orthonormal w, v, b and every l, y, V_0, lambda != 0, beta and r > 0, the density at (l, y) of
         (L, lambda (V - V_0)^2 + beta B) restricted to {|V - V_0| > r} is at most C/(|lambda| r),

with C absolute. With the fold slab (mass at most 4r) and Lemma 3.1 it gives (0.1) without diagonal for every hub law
and all light laws. For coordinate frames (V, B independent) it holds with C = 1 by conditioning on B, and for light
laws of bounded support it follows from Proposition 3.3. In the configuration above where M_2 grows like N, the
density of lambda V^2 + beta B off the fold (without the slice in L) decreases as N grows: for beta = 0.02 its
supremum is 0.62, 0.47, 0.23 at N = 4, 8, 16, and similarly for beta = 0.1 and 0.5, against the value 4 of the bound
at beta = 0 (num/cs_test.py). A resonant choice (rational basis, beta = sqrt6/2, so that the parabola meets the image
lattice in every column) gives 0.42, 0.29, 0.16 (num/cs_resonant.py).

By the coarea formula the density in (CS) is at most (2r)^{-1} times the integral of the product density over the
quadric {L = l, lambda (V - V_0)^2 + beta B = y} (the Jacobian |w ^ (2 lambda (V - V_0) v + beta b)| is at least
2 |lambda| r there). For a flat section of codimension two this integral is at most 2, which is the bound for
two-dimensional marginals; (CS) asks the same of a quadric section. It is a global nonlinear Brascamp-Lieb inequality
for the map x -> (<w, x>, lambda (<v, x> - V_0)^2 + beta <b, x>), whose linearisation at every point is a flat datum of
the kind the flat bound covers. Local versions of nonlinear Brascamp-Lieb inequalities are known; the global statement
for this quadratic map is what is missing. Approximating the quadric by flat pieces gives back the maximal functional
M, and choosing at each point a coordinate along which the section moves fast works for three coordinates but loses a
factor 1/det of the frame block, which is large for spread frames.

*Collisions on a shell.* In L^2 the curved section costs nothing on a single dyadic shell, for every law and every
frame.

**Lemma 3.6.** Let w, v, b be orthonormal, lambda != 0, beta and V_0 real, and 0 < r < K. For fixed l let h(y) be the
density at (l, y) of (L, Y), Y = lambda (V - V_0)^2 + beta B, restricted to {r <= |V - V_0| <= K}. Then

  int h(y)^2 dy <= (8/|lambda|) log(K/r).

In particular a dyadic shell R <= |V - V_0| <= 2R contributes at most 8 log 2/|lambda|, whatever R, beta and the laws.

*Proof.* Let X'' be an independent copy of X' and L', V', B', Y' the same functionals of X''. The integral is the density
at (l, l, 0) of (L, L', Y - Y') for the product of the two restricted measures. Suppose first that V - V_0 and V' - V_0
have the same sign, so that S = V + V' - 2V_0 satisfies 2r <= |S| <= 2K. With D = V - V' and E = B - B',

  Y - Y' = lambda S D + beta E.

For S = sigma fixed this is linear in (D, E) with gradient (lambda sigma, beta). The density of (L, L', S, Y - Y') at
(l, l, sigma, 0) is therefore |(lambda sigma, beta)|^{-1} times the density of (L, L', S, n_1 D + n_2 E) at
(l, l, sigma, 0), where n = (lambda sigma, beta)/|(lambda sigma, beta)|. On R^{2m} the functionals L, L', (S + 2V_0)/sqrt 2
and (n_1 D + n_2 E)/sqrt 2 are given by the orthonormal vectors (w, 0), (0, w), (v, v)/sqrt 2 and (u, -u)/sqrt 2 with
u = n_1 v + n_2 b, so this density is at most 2^{4/2}/2 = 2 by the bound for four-dimensional projections. Integrating
over 2r <= |sigma| <= 2K gives at most (4/|lambda|) log(K/r) for the two same-sign terms. If the signs differ, |D| >= 2r,
and fixing D = delta instead, the functional n'_1 S + n'_2 E with n' proportional to (lambda delta, beta) corresponds to
(n'_1 (v, v) + n'_2 (b, -b))/sqrt 2, again orthonormal to the other three. The mixed terms give (4/|lambda|) log(K/r). ∎

The logarithm counts dyadic shells, and it is the only loss. Lemma 3.1 does not need a power profile: its proof, with
Jensen's inequality applied to a concave nondecreasing profile phi, gives ||p_Q||_inf <= 1/2 + int_0^2 phi(x) dx/x whenever
mu_{l_0, l}(S) <= phi(|S|) for all l_0, almost every l and every Borel S. With Lemma 3.6 this removes most of the
dependence on the support in Proposition 3.3.

**Proposition 3.7.** If every X_i (i != h) is supported in an interval of length at most K, then (0.1) without diagonal,
with any cross terms and any linear terms, satisfies

  ||p_Q||_inf <= 1/2 + C |lambda|^{-1/2} (1 + log(1 + K^2 |lambda|))^{1/2}

for every hub law, with C absolute.

*Proof.* On the slice L = l the form is Y = lambda (V - V_0)^2 + beta B + const, with B a unit projection orthogonal to w
and v (Section 3, first paragraph). The tilt of Proposition 3.3, taken along v alone, gives
rho_{L,V}(l, u) <= 2 exp(-2 (|u - EV| - 2K)_+^2/K^2), so the part of the slice with |V - EV| > 2K + t has mass at most
sqrt(2 pi) K exp(-2 t^2/K^2). Put W = 2K + t and D_0 = |V_0 - EV|. On the rest, |V - V_0| lies between max(r, D_0 - W) and
D_0 + W, a range whose ratio of endpoints is at most 3W/r when r <= W. The fold slab |V - V_0| < r has mass at most 4r.
By Lemma 3.6 and Cauchy-Schwarz, for every Borel S,

  mu(S) <= 4r + (8 log(3W/r)/|lambda|)^{1/2} |S|^{1/2} + sqrt(2 pi) K e^{-2t^2/K^2}.

Take r = min(W, (|S|/|lambda|)^{1/2}) and t so that the last term is at most (|S|/|lambda|)^{1/2}. This gives
mu(S) <= phi(|S|) with phi(x) = (x/|lambda|)^{1/2} (5 + (8 log(3 + 3 W(x) |lambda|^{1/2} x^{-1/2}))^{1/2}) and
W(x) = K (2 + ((1/2) log_+(sqrt(2 pi) K |lambda|^{1/2} x^{-1/2}))^{1/2}). This phi is concave near 0, and it can be capped
at the total mass. Then int_0^2 phi(x) dx/x is at most C |lambda|^{-1/2} (1 + log(1 + K^2 |lambda|))^{1/2}. ∎

Proposition 3.3 had K^{1/2} in the same place. For light laws of unbounded support, the question is what happens when the
law of V on the slice is spread over many shells. The shell-by-shell bound can then be reached only if every shell
concentrates Y on the same small set of values. The statement that excludes this is weaker than (CS). It is a bound on
collisions weighted by the gradient:

  (VD)   for independent copies X', X'', the density of (L, L', (Y - Y')/G) at (l, l, 0) is at most C,
         G = |(lambda (|V - V_0| + |V' - V_0|), beta)|,

with C absolute. Here |V - V_0| + |V' - V_0| is |S| on pairs from the same branch and |D| on pairs from opposite branches,
so for fixed S (respectively D) the normalised difference is a unit linear functional of (D, E) (respectively (S, E)), and
its density is at most 2^{3/2}. The question is whether a direction proportional to (lambda S, beta), turning with the
orthogonal functional S, can raise it. Since the density in the proof of Lemma 3.6 is at most 2 pointwise in sigma, (VD)
and the bathtub principle in sigma give int h^2 <= (C'/|lambda|) log(1 + C''/r) on {|V - V_0| >= r}, with no dependence
on the laws. With Lemma 3.1 this bounds (0.1) without diagonal for every hub law and all light laws. (VD) follows from
the arclength form of (CS), that the integral of rho_{L,V,B}(l, ., .) along each level curve of Y is at most an absolute
constant. The collision norms in num/ (Section 4 of its README) are below 0.12 on every shell tested, against the bound
4 log 2 = 2.77 for the version without the slice, and they decrease as N grows.

*The slice in Fourier.* The linear term beta B of the slice is what (CS) has to control, and it is also what makes a
Fourier bound for the slice square-integrable.

**Lemma 3.8.** Let w, v, b be orthonormal with w_i^2 + v_i^2 + b_i^2 <= 1/2 for every i, lambda != 0, beta > 0 and
V_0 real. The pair (L, Y), Y = lambda (V - V_0)^2 + beta B, has a continuous density rho, with rho <= 16 (|lambda| beta)^{-1/2},
and for every l the slice h(y) = rho(l, y) satisfies

  int h(y)^2 dy <= (101.2 + 16 log_+(|lambda|/beta))/|lambda|.

*Proof.* Put Phi(zeta, xi, theta) = prod_i psi_i(zeta w_i + xi v_i + theta b_i) and G(theta) = int int |Phi(zeta, xi, theta)| d zeta d xi.
Theorem F bounds G(theta) by (4 pi)^2 for every theta, and its three-dimensional form, with p_i = 1/(w_i^2 + v_i^2 + b_i^2) >= 2,
bounds int G by (4 pi)^3. The Fresnel identity in V, with Gaussian damping as in Lemma 1.1, gives

  |E e^{i zeta L + i eta Y}| <= (4 pi |eta lambda|)^{-1/2} int |Phi(zeta, xi, eta beta)| d xi.

Integrating over zeta and eta, with theta = eta beta, the joint transform has integral at most
(4 pi |lambda|)^{-1/2} beta^{-1/2} int |theta|^{-1/2} G(theta) d theta <= (4 pi |lambda|)^{-1/2} beta^{-1/2} 8 sqrt(pi) (4 pi)^2 (split at
|theta| = pi), so rho is continuous and at most 16 (|lambda| beta)^{-1/2}. For the slice, h^(eta) = int e^{i eta y} h(y) dy
satisfies |h^(eta)| <= rho_L(l) <= sqrt 2 and |h^(eta)| <= (2 pi)^{-1} (4 pi |eta lambda|)^{-1/2} G(eta beta). By Plancherel
2 pi int h^2 = int |h^|^2 d eta. The range |eta| <= 1/|lambda| contributes at most 4/|lambda|, and

  int_{|eta| > 1/|lambda|} |h^|^2 d eta <= (16 pi^3 |lambda|)^{-1} int_{|theta| > beta/|lambda|} G(theta)^2 d theta/|theta|
                                   <= (16 pi^3 |lambda|)^{-1} (2 (4 pi)^4 log_+(|lambda|/beta) + (4 pi)^5),

using G <= (4 pi)^2 for |theta| < 1 and G^2 <= (4 pi)^2 G for |theta| >= 1. Dividing by 2 pi gives the bound. ∎

Lemma 3.6 cuts the collision count at the upper end K of the shells; Lemma 3.8 cuts it at the scale beta/|lambda| of the
linear term, whatever the spread of the laws. Stacking shells does not help against it: shells whose values of Y fall on
one short interval give a transform of the size of their total mass up to the inverse length of the interval, and the
Fresnel factor limits that as it limits a single shell.

**Proposition 3.9.** Let (0.1) have no diagonal (d_i = 0). Write q_perp and b_perp for the components of q and b
orthogonal to w and v, eps = |q_perp|, and suppose E = span(q_perp, b_perp) satisfies w_i^2 + v_i^2 + |P_E e_i|^2 <= 1/2 for
every light coordinate. If eps > 0, then for every hub law and all light laws

  ||p_Q||_inf <= 1/2 + 2 sqrt 2 + 14.2 |lambda|^{-1/2} + sqrt 2 log_+(A_0/|lambda|),    A_0 = 101.2 + 16 log_+(|lambda|/(2 eps)),

and also ||p_Q||_inf <= 1/2 + (43 + 11.4 log_+^{1/2}(|lambda|/(2 eps))) |lambda|^{-1/2}. For |lambda| >= 1 the first bound is at
most 17.6 + sqrt 2 log(101.2 + 16 log_+(|lambda|/(2 eps))), a double logarithm in 1/eps.

*Proof.* On the slice L = l the frozen form is Y_{l_0} = lambda (V - V_0)^2 + gamma(l_0) B_{l_0} + const, where
gamma(l_0) = |2 l_0 q_perp + b_perp| and B_{l_0} is the unit projection along 2 l_0 q_perp + b_perp (see the paragraph after
the proof of Lemma 3.1). That direction lies in E, so Lemma 3.8 applies, and with Cauchy-Schwarz
mu_{l_0, l}(S) <= phi_{l_0}(|S|), phi_{l_0}(x) = min(sqrt 2, (A(l_0) x)^{1/2}), A(l_0) = (101.2 + 16 log_+(|lambda|/gamma(l_0)))/|lambda|.
The proof of Lemma 3.1 uses the profile of each cell separately, so it gives, with t = l + beta,

  ||p_Q||_inf <= 1/2 + int_{|t| < 1} min(sqrt 2/(2|t|), (A(t - beta)/(2|t|))^{1/2}) dt.

Here gamma(t - beta) = |2 t q_perp + c_0| with c_0 = b_perp - 2 beta q_perp, so gamma >= 2 eps |t - t_0| for some t_0, and
A(t - beta) <= (A_0 + 16 log_+(1/|t - t_0|))/|lambda|. Since min(a, (x + y)^{1/2}) <= min(a, x^{1/2}) + y^{1/2}, the integral is at
most the sum of two terms. The part with log_+(1/|t - t_0|) is at most 4 |lambda|^{-1/2} int_{|t|<1} (2|t|)^{-1/2}
log_+^{1/2}(1/|t - t_0|) dt <= 8 sqrt(pi) |lambda|^{-1/2}, by rearrangement (t_0 = 0 is the largest case). With
c = A_0/|lambda|, the other is int_{|t|<1} min(sqrt 2/(2|t|), (c/(2|t|))^{1/2}) dt, which equals 2 (2c)^{1/2} <= 2 sqrt 2 if c <= 1
and 2 sqrt 2 + sqrt 2 log c otherwise (the minimum switches at |t| = 1/c). Dropping the minimum instead and using
int_{|t|<1} (2|t|)^{-1/2} dt = 2 sqrt 2 gives the second bound. ∎

With eps = 0 the same proof gives 1/2 + 2 sqrt 2 + sqrt 2 log_+((101.2 + 16 log_+(|lambda|/|b_perp|))/|lambda|), and with
q_perp = b_perp = 0 the fold alone gives 1/2 + 16 |lambda|^{-1/2}; the case eps = 0 is in any event covered by
degenerate_hub/. So without diagonal the dependence on eps is now a double logarithm, against (eps |lambda|)^{-1/3} in
Proposition 2.3, and it holds for light laws of unbounded support: Proposition 3.7 had log(1 + K^2 |lambda|) where
Proposition 3.9 has log log(|lambda|/eps). The double logarithm comes from the slices with 1/c < |t| < 1: there the
relevant sets have measure between 2/c and 2, the Fourier profile (A x)^{1/2} exceeds the total mass, and only the mass
is used. For exact rank three this is case (O1) with m = 0; when b lies in the range, E is the line of the leak and the
hypothesis is the three-dimensional leverage condition. There low_rank_plus_diagonal/ had 41 + 27 log_+(1/(6 eps))
under leverages at most 1/50.

The logarithm in Lemma 3.8 comes from the frequencies 1/|lambda| < |eta| < 1/gamma, where only the Fresnel factor controls
the slice: a fold resolved at the scale gamma of the linear term. In the single hub gamma is of order eps on every slice
near the hub degeneracy, which is why eps appears. On intervals Lemma 1.1 already gives 2 pi^2 (|I|/|lambda|)^{1/2}, free
of gamma; the loss is only for Borel sets, which the hub law can make of many short pieces. Removing the fold slab in
the Fourier bound would remove the logarithm, but a cut |V - V_0| > r becomes a cut |xi| > 2 |eta lambda| r in the
Fresnel frequency, and for comb laws the frame integral over |xi| > M does not decay in M. What (CS) asks is exactly the
missing statement: a bound for the slice off the fold that does not see gamma.

*A small-ball bound with the diagonal.* Pairing the hub window with the slice in Fourier, instead of through a profile of
the slice, needs only the transform bound of Lemma 1.1, which allows every diagonal and every linear term; the hub
enters through its L^2 norm.

**Theorem 3.10.** Let Q have the form (0.1), with any q, any diagonal and any linear terms. For every law of X_h with
density at most 1, all light laws, every s and every delta > 0,

  P(|Q - s| <= delta) <= 2 delta (1/2 + 2 sqrt 2 + sqrt 2 log_+(2 B_delta^2)),
  B_delta = (4 + ((4 + 32 pi log_+(|lambda|/delta))/pi)^{1/2}) / (2 |lambda|^{1/2}).

*Proof.* As in the proof of Theorem 1, now with an arbitrary hub law, P(|Q - s| <= delta) is the limit of
sum_k int_{C_k} dl int G(l_k, y) mu_{l_k, l}(dy) with G(l, y) = int f_h(x) 1{|2 x (l + beta) + y - s| <= delta} dx. For
t = l_k + beta != 0, G(l_k, .) = 1_{[-delta, delta]} * g with g(u) = f_h((s - u)/(2t))/(2|t|), so its transform is
(2 sin(eta delta)/eta) g^(eta), and int |g^|^2 = 2 pi int g^2 <= pi/|t|. By Lemma 1.1, for almost every l the slice
mu = mu_{l_k, l} satisfies |mu^(eta)| <= min(rho_L(l), 2 (4 pi/|eta lambda|)^{1/2}), so
int_{|eta| <= 1/delta} |mu^|^2 <= (4 + 32 pi log_+(|lambda|/delta))/|lambda|. Parseval and Cauchy-Schwarz in each range give

  int G(l_k, y) mu(dy) <= (2 pi)^{-1} [ 2 delta int_{|eta| <= 1/delta} |g^| |mu^| + int_{|eta| > 1/delta} (2/|eta|) |g^| |mu^| ]
                      <= delta (|lambda| |t|)^{-1/2} ( ((4 + 32 pi log_+(|lambda|/delta))/pi)^{1/2} + 4 ),

and also int G(l_k, y) mu(dy) <= (delta/|t|) rho_L(l) <= sqrt 2 delta/|t|. The part |t| >= 1 contributes at most delta, so

  (2 delta)^{-1} P(|Q - s| <= delta) <= 1/2 + int_{|t| < 1} min(sqrt 2/(2|t|), B_delta |t|^{-1/2}) dt,

and the integral is 2 sqrt 2 + sqrt 2 log(2 B_delta^2) when 2 B_delta^2 >= 1 (the minimum switches at |t| = 1/(2 B_delta^2)) and
4 B_delta <= 2 sqrt 2 otherwise. ∎

So the hub, the square along V, every cross term, every diagonal and every linear term together give a small-ball
probability of order delta log log(1/delta), for every hub law and all light laws. What is missing is only the passage
delta -> 0, and above the scale eps of the cross term Proposition 2.3 supplies it.

**Corollary 3.11.** Under the hypotheses of Proposition 2.3 with a = 0 (q = q_w w + q_v v + eps q^, eps > 0,
w_i^2 + v_i^2 + q^_i^2 <= 1/2, any light diagonal and linear terms), for every hub law

  ||p_Q||_inf <= 5.41 (1/2 + 2 sqrt 2 + sqrt 2 log_+(2 B_eps^2)) + 40.1 |lambda|^{-1/2}.

For |lambda| >= 1 this is at most 58.2 + 7.7 log_+(2 B_eps^2), a double logarithm in 1/eps, where Proposition 2.3 has
9.6 (eps |lambda|)^{-1/3}.

*Proof.* The first bound of Proposition 2.3 makes phi_Q integrable, so p_Q is continuous. Let F_eps be the Fejer kernel,
F_eps^(eta) = (1 - eps |eta|)_+. Then |p_Q - p_Q * F_eps| <= (2 pi)^{-1} int |phi_Q| min(1, eps |eta|) d eta, and splitting at
|eta| = 1/eps, with |phi_Q| <= 31.5 |eta|^{-3/2} (eps |lambda|)^{-1/2}, gives at most (2 pi)^{-1} 252 |lambda|^{-1/2} = 40.1 |lambda|^{-1/2}.
Since F_eps(u) <= (2 pi)^{-1} min(1/eps, 4 eps/u^2), splitting |s - Q| into [0, eps] and the dyadic shells (2^{k-1} eps, 2^k eps]
gives p_Q * F_eps(s) <= (34/(2 pi)) sup_{delta >= eps} P(|Q - s| <= delta)/(2 delta), and Theorem 3.10 bounds the supremum,
B_delta being decreasing in delta. ∎

Corollary 3.11 does not need span(q_perp, b_perp) to be spread, as Proposition 3.9 does, and it allows the light diagonal;
Proposition 3.9 holds at every scale by itself, without Proposition 2.3. A hub diagonal is not covered: the law of
a X_h^2 + 2 t X_h has a fold of its own, and its density need not be square-integrable. For localised cross terms
(Proposition 2.4) and for eps = 0 (degenerate_hub/) the density is bounded outright, so in (0.1) with a = 0 the only
loss left is the double logarithm for spread cross terms of small size.

With a hub diagonal the hub still gives an L^2 bound in its partner at each fixed frequency, and that is enough to
halve the exponent of Proposition 2.3.

**Proposition 3.12.** For every Q of the form (0.1) with a hub diagonal, Q = a X_h^2 + 2 X_h (L + beta) + Y_L (any q, any
light diagonal and linear terms, (w, v) orthonormal with w_i^2 + v_i^2 <= 1/2), every hub law and all light laws,

  |phi_Q(eta)| <= 4.72 |lambda|^{-1/4} |eta|^{-3/4}.

Under the hypotheses of Proposition 2.3 (any a), ||p_Q||_inf <= 17.0 eps^{-1/6} |lambda|^{-1/3}.

*Proof.* Put h_eta(l) = E e^{i eta (a X_h^2 + 2 X_h (l + beta))}. As a function of l this is the Fourier transform of
f_h(x) e^{i eta a x^2} at -2 eta (l + beta), so int |h_eta(l)|^2 dl = (2 |eta|)^{-1} 2 pi int f_h^2 <= pi/|eta| for every a. With cells C_k
of length h as in the proof of Theorem 1, phi_Q(eta) = lim_{h -> 0} sum_k int_{C_k} h_eta(l_k) mu^_{l_k, l}(eta) dl by dominated
convergence, and Cauchy-Schwarz over the cells gives

  |phi_Q(eta)| <= (pi/|eta|)^{1/2} (sup_{l_0, l} |mu^_{l_0, l}(eta)| int rho_L)^{1/2} <= (pi/|eta|)^{1/2} (2 (4 pi/|eta lambda|)^{1/2})^{1/2},

by the transform bound in the proof of Lemma 1.1, which allows every diagonal and every linear term; the constant is
(2 pi)^{1/2} (4 pi)^{1/4} = 4.72. With A = 4.72 |lambda|^{-1/4} and B = 31.5 (eps |lambda|)^{-1/2} from Proposition 2.3,
int min(A |eta|^{-3/4}, B |eta|^{-3/2}) d eta <= 8 A eta_0^{1/4} + 4 B eta_0^{-1/2} for every eta_0 > 0, and eta_0 = (B/A)^{4/3} makes this
12 A^{2/3} B^{1/3}. Hence ||p_Q||_inf <= (6/pi) A^{2/3} B^{1/3} <= 17.0 eps^{-1/6} |lambda|^{-1/3}. ∎

So a hub diagonal together with a spread cross term of size eps costs at most eps^{-1/6}, where Proposition 2.3 had
eps^{-1/3}. The exponent 3/4 in the first bound is where one hub stops: Plancherel in a one-dimensional partner gives
|eta|^{-1/2} and the Fresnel factor of the slice a further |eta|^{-1/4} after Cauchy-Schwarz. Two hubs give |eta|^{-5/4}
this way (Theorem 6.1), and three give |eta|^{-3/2} without the slice (Theorem 6.3).

The |eta|^{-1/2} of one hub is the price of a rough hub law, whose Fourier transform is only square-integrable. When the hub
density has bounded variation the transform decays like 1/|zeta|, and the pairing converges without any hypothesis on the
cross terms.

**Proposition 3.13.** Let Q have the form (0.1) with a = 0 (any q, any light diagonal and linear terms, (w, v) orthonormal
with w_i^2 + v_i^2 <= 1/2), and suppose the hub density has total variation V. With A = 2 (4 pi/|lambda|)^{1/2},

  |phi_Q(eta)| <= V |eta|^{-3/2} (A (1 + log_+(2 |eta|^{3/2}/V)) + 1/2),

and ||p_Q||_inf <= 14.9 V^{2/3} whenever |lambda| >= 1, for all light laws.

*Proof.* Now h_eta(l) = psi_h(2 eta (l + beta)) and |psi_h(zeta)| <= min(1, V/|zeta|) (integration by parts against d f_h). As in the
proof of Proposition 3.12, with t = l + beta,

  |phi_Q(eta)| <= int min(1, V/(2 |eta| |t|)) min(rho_L(t - beta), A |eta|^{-1/2}) dt.

On |t| <= T = |eta|^{1/2} use the second minimum's A |eta|^{-1/2}: the integral of min(1, V/(2|eta||t|)) over |t| <= T is at most
(V/|eta|)(1 + log_+(2 |eta| T/V)). On |t| > T use rho_L: the contribution is at most (V/(2 |eta| T)) int rho_L = V/(2 |eta|^{3/2}). This is the
first bound. The substitution eta = (A V)^{2/3} s shows that (2 pi)^{-1} int min(1, .) d eta equals (A V)^{2/3} times a function of A alone,
which is 4.03 at A = 2 (4 pi)^{1/2} (numerical quadrature, recorded in num/README.md). The bound is increasing in A and
|lambda| >= 1 means A <= 2 (4 pi)^{1/2}, so the integral is at most 4.03 (2 (4 pi)^{1/2} V)^{2/3} = 14.9 V^{2/3}. ∎

For larger |lambda| the same integral is smaller (8.8 V^{2/3} at |lambda| = 4, 2.7 V^{2/3} at |lambda| = 100), but it does not tend
to zero: the term 1/2, which comes from the partner law away from the origin, leaves (3/pi) (V/2)^{2/3}.

A window law U[0, 1] * nu has V <= 2, so (0.1) without hub diagonal and with a window hub law is bounded by 24 for every
cross term and every light law; Corollary 3.5 had window light laws with an arbitrary hub. What is open in (0.1)
needs both roughnesses at once: a hub law of large total variation (many teeth; by Proposition 3.18 the variation has to
be exponentially large) and light laws for which the slice has no Borel profile better than Lemma 3.8's.

The hub law enters every slice in the same way. The density at s is E[f_h(x*)/(2|t|)] with t = L + beta and
x* = (s - Y_L)/(2t), so for f_h = 1_S the values of Y_L that the hub can reach on the slice at t form the set s - 2tS, and
as t runs through a dyadic band these sets are dilates of one set. Lemma 3.1 bounds each slice by its worst Borel set
of the right measure and so does not use this. When the slices do not move with t the dilates average out: for a fixed
value y the integral of 1_S((s - y)/(2t))/(2|t|) over 0 < |t| < 1 is at most log(1 + 1/|s - y|), and only the interval
profile of the slice is needed. The slices do not move when the light coordinates that carry part of the hub partner
carry nothing else.

**Proposition 3.14 (a partner-only block).** Let Q have the form (0.1) with a = 0, and let I_1 be a set of light
coordinates such that v_i = 0 and d_i = 0 for i in I_1 and q and b are proportional to w on I_1: q_i = kappa w_i and
b_i = mu w_i for i in I_1. Put omega = |w_{I_1}| > 0. Then for every hub law and all light laws

  ||p_Q||_inf <= 1/2 + (sqrt 2/omega) (3.5 (2 + log(1 + 4 pi^4/|lambda|)) + 0.5 log(1 + 4 |kappa|)),

and ||p_Q||_inf <= 1/2 + (sqrt 2/omega)(2 + log(1 + 2 pi^4/|lambda|)) when kappa = 0. For |lambda| >= 1 these are at most
1/2 + (39.5 + 0.71 log(1 + 4|kappa|))/omega and 1/2 + 10.3/omega.

*Proof.* Write X' = (X_{I_1}, X_R), L_1 = <w_{I_1}, X_{I_1}>, L_R = L - L_1 and t = L + beta. On I_1 the coordinates
enter Q only through L_1: 2 L <q, X'> = 2 kappa L^2 + 2 L P and sum_{i in I_1} b_i X_i = mu L - mu L_R, with
P = <q_R, X_R> - kappa L_R + mu/2. So Q = 2 X_h t + 2 kappa L^2 + 2 L P + W, where P and
W = lambda V^2 + sum_{i in R} phi_i(X_i) - mu L_R + const are functions of X_R. Given X', the conditional density of Q at
s is f_h(x*)/(2|t|) with x* = (s - 2 kappa L^2 - 2 L P - W)/(2t), and with L = t - beta

  x* = alpha/(2t) + c_0 - kappa t,     alpha = s - 2 kappa beta^2 + 2 beta P - W,     c_0 = 2 kappa beta - P,

where alpha and c_0 depend on X_R only. Given X_R, t = L_1 + L_R + beta has a density g <= sqrt 2/omega, because L_1 is
independent of X_R and <w_{I_1}/omega, X_{I_1}> has density at most sqrt 2. On |t| >= 1 use f_h/(2|t|) <= 1/2 and
int g = 1. Hence, for almost every s,

  p_Q(s) <= 1/2 + (sqrt 2/omega) E_{X_R} int_{0 < |t| < 1} f~(alpha/(2t) - kappa t) dt/(2|t|),     f~ = f_h(. + c_0).

For kappa = 0 the substitution x = alpha/(2t) maps 0 < |t| < 1 one-to-one onto |x| > |alpha|/2 with dt/|t| = dx/|x|,
and the bathtub principle (f~ <= 1, int f~ = 1, a weight decreasing in |x|) bounds the integral by the integral of
dx/(2|x|) over |alpha|/2 < |x| < |alpha|/2 + 1/2, which is log(1 + 1/|alpha|). For kappa != 0 put sigma = 2 kappa and
tau = min(1, (|alpha|/(2|sigma|))^{1/2}), and write x(t) = alpha/(2t) - sigma t/2. On 0 < |t| < tau, t x(t) =
(alpha - sigma t^2)/2 has the sign of alpha and modulus between |alpha|/4 and 3|alpha|/4, and
|x'(t)| = |alpha + sigma t^2|/(2t^2) >= |alpha|/(4t^2). So x is monotone on each side of 0, the two sides have disjoint
images in |x| > |alpha|/(4 tau), and dt/|t| <= 3 dx/|x|; the bathtub principle gives at most 3 log(1 + 2 tau/|alpha|)
there, and tau <= |t| < 1 contributes at most log(1/tau). In both cases the integral is at most
3.5 log(1 + 2/|alpha|) + 0.5 log(1 + 2|sigma|).

It remains to average over X_R. As a function of X_R, alpha is a real quadratic polynomial containing -lambda V^2, with v
supported on R and v_i^2 <= 1/2. The Fresnel identity in V and the one-dimensional Brascamp-Lieb bound (Hoelder with
p_i = 1/v_i^2 and Lemma 1 of the first record, for the chirp-modulated transforms as in Lemma 1.1) give
|E e^{i eta alpha}| <= 2 (pi/|eta lambda|)^{1/2}, and the kernel argument in the proof of Lemma 1.1 gives
P(|alpha - a| <= r) <= pi^2 (2r/|lambda|)^{1/2} for every a and r. Hence, with c = 2 pi^2 |lambda|^{-1/2},

  E log(1 + 2/|alpha|) = int_0^inf P(|alpha| < 2/(e^u - 1)) du <= int_0^inf min(1, c (e^u - 1)^{-1/2}) du <= log(1 + c^2) + 2,

since beyond u_0 = log(1 + c^2) the integral is 2c arctan(1/c) < 2. In the same way E log(1 + 1/|alpha|) is at most
2 + log(1 + 2 pi^4/|lambda|). ∎

No hypothesis is made on the light laws, on the size of the cross term, or on the coordinates of R: every cross term
2 L <q_R, X_R>, every diagonal and every linear term there is allowed, and eps plays no part. The one-variable bound
holds with room: over two hundred random (alpha, sigma) with sigma != 0, the bathtub integral of the exact push-forward
density of dt/(2|t|) under x(t) is at most 0.27 of 3.5 log(1 + 2/|alpha|) + 0.5 log(1 + 2|sigma|) (num/p314_check.py).
A block that carries w and v and nothing else leaves, after the same conditioning, a two-dimensional law of bounded
density; that case, with the diagonal allowed, is Proposition 2.4. What the conditioning cannot reach is a hub partner
all of whose coordinates also carry the transverse square or the cross term. There the sigma-algebras that leave t with
a bounded conditional density while x* stays a function of t are those generated by all light coordinates but one, and
the bound they give is of order 1/max_i |w_i| (Proposition 3.16 below), which is not uniform in the frame; otherwise
the dilates of S meet slices that change with t.

With the roles of L and V exchanged no dilation is needed, because a free part of V gives the slices a Borel profile
directly.

**Proposition 3.15 (a square-only block).** Let I_2 be a set of light coordinates, X_R the others, and
Q = 2 X_h (L + beta) + lambda V^2 + 2 V g(X_R) + G(X_R), where L is a function of X_R, V = <v, X'> with |v_{I_2}| > 0,
and g and G are arbitrary measurable functions. Then for every hub law and all light laws

  ||p_Q||_inf <= 1/2 + 8 sqrt 2 |v_{I_2}|^{-1} |lambda|^{-1/2}.

This contains (0.1) with a = 0 whenever w, q, b and the diagonal vanish on I_2, with any twist, cross term, diagonal and
linear term on the other coordinates.

*Proof.* Write V = V_2 + V_R with V_2 = <v_{I_2}, X_{I_2}>, independent of X_R, of density at most sqrt 2/|v_{I_2}|. Since L
is a function of X_R, the slices of Lemma 3.1 are here simply mu_l(S) = E[1{Y in S}; L in dl]/dl with
Y = lambda V^2 + 2 V g + G, and given X_R, Y = lambda (V_2 + c_1)^2 + c_2 with c_1, c_2 functions of X_R. For a Borel set S,
|{u : lambda u^2 in S}| <= 2 (|S|/|lambda|)^{1/2}, so P(Y in S | X_R) <= 2 sqrt 2 |v_{I_2}|^{-1} (|S|/|lambda|)^{1/2}, and
mu_l(S) <= rho_L(l) 2 sqrt 2 |v_{I_2}|^{-1} (|S|/|lambda|)^{1/2} <= 4 |v_{I_2}|^{-1} (|S|/|lambda|)^{1/2}. Lemma 3.1 with theta = 1/2
gives the bound (its discretisation is not needed, since Y does not depend on L once X_R is fixed). ∎

So the single hub is bounded, for every hub law and all light laws, as soon as part of the partner (Proposition 3.14),
part of the transverse direction (Proposition 3.15), or a well-conditioned part of both together (Proposition 2.4) lives on
light coordinates that carry nothing else. In each case conditioning on the other coordinates leaves a low-dimensional
variable with a bounded density and a remainder that depends on it in a known way. The open case is the entangled one,
in which every light coordinate that carries w or v also carries the partner of the cross term.

On a single coordinate the hypothesis of Proposition 3.14 holds automatically: whatever v_i, q_i and b_i are, X_i
enters Q only through w_i X_i. What changes is the curvature left in the remainder.

**Proposition 3.16 (one coordinate of the partner).** Let Q have the form (0.1) with a = 0 and no light diagonal, and
let i be a light coordinate with w_i != 0. Then for every hub law, all light laws and every cross term q,

  ||p_Q||_inf <= 1/2 + |w_i|^{-1} (3.5 (2 + log(1 + 4 pi^4/|lambda|)) + 0.5 log(1 + 2 |lambda v_i^2/w_i^2 + 2 q_i/w_i|)).

With m light coordinates some |w_i| is at least m^{-1/2}, so for |lambda| >= 1 the density is at most
1/2 + m^{1/2} (27.9 + 0.5 log(1 + m |lambda| + 4 m^{1/2} |q_i|)).

*Proof.* Condition on X_R, the light coordinates other than i. Then t = L + beta = w_i X_i + L_R + beta has density at
most 1/|w_i|, and X_i = (t - beta - L_R)/w_i, so V, L, <q, X'> and <b, X'> are affine in t with coefficients that
depend on X_R, and the numerator of x* = (s - lambda V^2 - 2 L <q, X'> - <b, X'>)/(2t) is a quadratic in t. Hence
x* = alpha/(2t) + c_0 - sigma t/2 with alpha and c_0 functions of X_R and sigma = lambda v_i^2/w_i^2 + 2 q_i/w_i, and the
proof of Proposition 3.14 gives the conditional bound 1/2 + |w_i|^{-1} (3.5 log(1 + 2/|alpha|) + 0.5 log(1 + 2|sigma|)).
The value alpha is the numerator at t = 0, a quadratic polynomial in X_R whose quadratic part is -lambda <u_R, X_R>^2 with
u_R = v_R - (v_i/w_i) w_R, and |u_R|^2 = 1 + v_i^2/w_i^2 >= 1 because <v, w> = 0. If every coordinate of u_R/|u_R| has
square at most 1/2, the Fresnel and Hoelder argument at the end of the proof of Proposition 3.14 gives
P(|alpha - a| <= r) <= pi^2 (2r/|lambda|)^{1/2}. Otherwise one coordinate j carries more than half of |u_R|^2; given the
other coordinates of R, alpha is a quadratic in X_j with leading coefficient of modulus at least |lambda|/2, and
P(|alpha - a| <= r) <= 4 (r/|lambda|)^{1/2}. In both cases E log(1 + 2/|alpha|) <= 2 + log(1 + 4 pi^4/|lambda|). ∎

The form of x* and the identity for |u_R| hold to rounding in 400 random configurations, and the exact conditional
density given X_R stays below a tenth of the conditional bound for comb laws and a rough hub law (num/, Section 11).
A light diagonal on the coordinates other than i can be allowed here, and in Proposition 3.17 below, when every
coordinate of u_R/|u_R| has square at most 1/2: it enters alpha as one-coordinate chirps, which the Fresnel and
Hoelder argument of Proposition 3.14 already carries, and it does not change sigma. A diagonal on the coordinate i itself adds d_i/w_i^2 to sigma and a second
square along w_R to alpha, and is not covered.

The factor 1/|w_i| can be confined to a short range of t, where the dilation makes it harmless.

**Proposition 3.17 (a logarithm of the dimension).** In the setting of Proposition 3.16, for every light coordinate i
with w_i != 0,

  ||p_Q||_inf <= 3/2 + 2 |q_i| + 7 pi^3 (|w_i|/(|lambda| (1 + |lambda|)))^{1/2} + sqrt 2 log(1 + |lambda|) + 3 sqrt 2 log(1/|w_i|).

On m light coordinates some |w_i| is at least m^{-1/2}, so the density is at most C (1 + |q|_inf + log(1 + |lambda|)) +
(3/sqrt 2) log m for |lambda| >= 1, for every hub law, all light laws and every cross term.

*Proof.* Put delta = |w_i|^3/(1 + |lambda|) and split according to |t|. The part |t| >= 1 contributes at most 1/2. On
delta <= |t| < 1 use only f_h <= 1: the contribution is at most int rho_L(t - beta) dt/(2|t|) over that range, and
rho_L <= sqrt 2, which gives sqrt 2 log(1/delta). On |t| < delta condition on X_R as in the proof of Proposition 3.16.
The one-variable bound of Proposition 3.14 is invariant under t -> delta t, which replaces (alpha, sigma) by
(alpha/delta, sigma delta), so this part is at most |w_i|^{-1} E(3.5 log(1 + 2 delta/|alpha|) + 0.5 log(1 + 2 |sigma| delta)).
With P(|alpha| < rho) <= pi^2 (2 rho/|lambda|)^{1/2} and int_0^inf (e^u - 1)^{-1/2} du = pi,
E log(1 + 2 delta/|alpha|) = int_0^inf P(|alpha| < 2 delta/(e^u - 1)) du <= 2 pi^3 (delta/|lambda|)^{1/2}, and
|sigma| delta <= (|lambda| v_i^2 + 2 |q_i| |w_i|) |w_i|/(1 + |lambda|) <= (1 + 2 |q_i|) |w_i|. Adding the three parts gives the
bound. ∎

The logarithm is the price of the range delta <= |t| < 1, where only rho_L <= sqrt 2 is used. On a dyadic shell
|t| ~ tau the dilation argument gives about tau^{1/2} times the average conditional density of L, so a shell at
scale tau would need a block I of coordinates with |w_I|^2 of order tau that leaves L a conditional density of order
1/|w_I| given the rest of the block. Even for uniform laws that average is sum_{i in I} |w_i|/|w_I|^2 (the projection
of the cube on the hyperplane orthogonal to w_I), which grows like |I|^{1/2}/|w_I|, so blocks do not improve on the
single coordinate here, and this route stops at log m.

The hub side has the same shape. Lemma 1.1 bounds the slice of a union of n intervals by 2 pi^2 |lambda|^{-1/2} times the
sum of the square roots of their lengths, and where that exceeds the mass of the slice only rho_L <= sqrt 2 is used, as
in Proposition 3.9.
The price is a logarithm of the roughness of the hub law in place of the powers of Theorem 1 and Proposition 3.13.

**Proposition 3.18 (a logarithm of the hub's roughness).** Let Q have the form (0.1) with a = 0. For every cross term q,
every light diagonal and linear term, and all light laws:

(a) if X_h is supported in an interval of length D, then ||p_Q||_inf <= 1/2 + 2 sqrt 2 + sqrt 2 log_+(4 pi^4 D/|lambda|);

(b) if every superlevel set {f_h > u} is a union of at most n intervals, then
    ||p_Q||_inf <= 1/2 + 3 sqrt 2 + sqrt 2 log_+(4 pi^4 n/|lambda|);

(c) if f_h has total variation V, then ||p_Q||_inf <= 1/2 + 3 sqrt 2 + sqrt 2 log(1 + 2 pi^4 V/|lambda|).

*Proof.* Write f_h = int_0^1 1_{A_u} du with A_u = {f_h > u}, so that G = int_0^1 G_u du with
G_u(l, y) = |{x in A_u : |2 x t + y - s| <= delta}|, and run the proof of Theorem 1 for each G_u. Since G <= delta/|t|,
the range |t| >= 1 contributes 1/2 in all. On |t| < 1 two bounds hold for int G_u(l_k, y) mu(dy). The first is
(delta/|t|) rho_L(l) <= sqrt 2 delta/|t|, because mu has mass rho_L(l). The second, when A_u is the union of intervals
I_1, ..., I_n, is (delta/|t|) sum_j 2 pi^2 ((2|t| |I_j| + 2 delta)/|lambda|)^{1/2}, by Lemma 1.1 applied to the intervals of
s - 2t A_u + [-delta, delta]; by Cauchy-Schwarz it is at most (delta/|t|)(K_u |t|^{1/2} + 2 pi^2 n (2 delta/|lambda|)^{1/2}) with
K_u = 2 pi^2 (2 n |A_u|/|lambda|)^{1/2}. The range |t| < delta and the thickening by delta contribute o(1) as delta -> 0, as in
the proof of Theorem 1, and what remains is

  int_{|t| < 1} min(sqrt 2, K_u |t|^{1/2}) dt/(2|t|),

which equals 2 K_u <= 2 sqrt 2 when K_u^2 <= 2 and 2 sqrt 2 + sqrt 2 log(K_u^2/2) otherwise, the minimum switching at
|t| = 2/K_u^2; here K_u^2/2 = 4 pi^4 n |A_u|/|lambda|. For (a), f_h <= 1_J is a single level with n = 1 and |A| = D. For
(b), |A_u| <= 1/u, log_+(x y) <= log_+ x + log_+ y and int_0^1 log(1/u) du = 1. For (c), A_u has at most N(u)/2
intervals, N(u) the number of boundary points of A_u, and int N(u) du <= V (the coarea formula in one variable);
log_+(c n_u/u) <= log(1 + c n_u) + log(1/u) and Jensen's inequality for the concave function log(1 + c .) give the bound. ∎

For |lambda| = 1 the constants are 11.8 in (a) with D = 1, against 22 in Theorem 1, and 13.2 in (c) with V = 2, against
23.7 in Proposition 3.13, and for large D or V the logarithms replace D^{1/3} and V^{2/3}. So a hub law that makes (0.1)
large has superlevel sets made of exponentially many intervals, spread over an exponentially long range, and it has to
meet light laws whose slices have no Borel profile better than Lemma 3.8's.

Lemma 1.1 and rho_L <= sqrt 2 give nothing better than (b). By the substitution y = s - 2tx, the density with a hub
law uniform on A is int_A g(x) dx with g(x) = int rho(t, s - 2tx) dt, rho the joint density of (L + beta, Y_L): the
integral of rho over the line through (0, s) of slope -2x. Let the slice of rho at t, for |lambda|/n < |t| < 2^{-3/2},
consist of n bumps of width 2|t|/n and mass sqrt 2/n centred at s - 2tk, k = 1, ..., n (total mass at most 1). Every
slice has mass sqrt 2 and satisfies the bound of Lemma 1.1, and g = sqrt 2 log(n/(2^{3/2} |lambda|)) on the set of
measure 1 within 1/(2n) of the points k. If instead the slices did not move with t, rho(t, y) = rho_0(y) on |t| < 1
with rho_0 subject to Lemma 1.1, then
g(x) = mu_0([s - 2|x|, s + 2|x|])/(2|x|) <= 2 pi^2 (|lambda| |x|)^{-1/2}, and the density would be at most
1/2 + 4 sqrt 2 pi^2 |lambda|^{-1/2} for every hub law. What is open without diagonal is how the slices move with t: they
must not follow many lines through the point (0, s) at once.

What the conditioning of Propositions 3.16 and 3.17 needs is a variable that enters Q through one row, not a single
coordinate.

**Proposition 3.19 (groups of parallel rows).** In the setting of Proposition 3.16, let G be a set of light coordinates
on which the rows (w_i, v_i, q_i, b_i) are all parallel, and put |w_G| = (sum_{i in G} w_i^2)^{1/2} > 0 and likewise |q_G|.
Then Proposition 3.16 holds with |w_i|^{-1} replaced by sqrt 2 |w_G|^{-1} and the ratios v_i/w_i, q_i/w_i by those of the
group, and

  ||p_Q||_inf <= 1/2 + sqrt 2 (1 + 2 |q_G|) + 7 sqrt 2 pi^3 (|w_G|/(|lambda| (1 + |lambda|)))^{1/2} + sqrt 2 log(1 + |lambda|)
                 + 3 sqrt 2 log(1/|w_G|).

If the light coordinates split into K such groups, the density is at most C (1 + max_G |q_G| + log(1 + |lambda|))
+ (3/sqrt 2) log K for |lambda| >= 1, for every hub law, all light laws and every cross term, however many coordinates there
are.

*Proof.* On G the rows are r_i e for one vector e, so the coordinates of G enter Q only through S = sum_{i in G} r_i X_i, and
S/(sum r_i^2)^{1/2} has density at most sqrt 2 (Ball's bound, the same that gives rho_L <= sqrt 2). Condition on the
coordinates outside G. Then t = L + beta = e_w S + const has density at most sqrt 2/|w_G|, and the rest of the proof of
Proposition 3.16 runs with S in place of X_i. The only other place the coordinate entered is the identity for u_R, and it
survives: with R the coordinates outside G, u_R = v_R - (v_G/w_G) w_R, |v_R|^2 = 1 - v_G^2, |w_R|^2 = 1 - w_G^2 and
<v_R, w_R> = -v_G w_G, because the rows on G are parallel and <v, w> = 0, so |u_R|^2 = 1 + v_G^2/w_G^2 as before. The proof
of Proposition 3.17 then gives the bound with delta = |w_G|^3/(1 + |lambda|), using v_G^2 <= 1 in place of v_i^2 <= 1/2. Of K
groups one has |w_G|^2 >= 1/K. ∎

The same grouping turns Proposition 5.1(b) into a bound of order K for U + c V^2 on frames whose rows (u_i, v_i) take K
directions, since the K group vectors satisfy sum_{G < H} (u_G v_H - u_H v_G)^2 = 1. So the regime left open by
Propositions 3.16 to 3.19 is not merely many light coordinates: the rows (w_i, v_i, q_i, b_i) must point in many different
directions, and a light diagonal must not be what makes them differ.

With a hub diagonal the same conditioning leaves the hub quadratic a x^2 + 2 x t + N(t) = s with N(t) = A + B t + C t^2
quadratic in t. Its roots contribute (f_h(x_+) + f_h(x_-))/(2 D^{1/2}) with D(t) = t^2 + a (s - N(t)), and the part with
D < 1 is at most |w_i|^{-1} int_{0 < D < 1} dt/D^{1/2} given X_R. For kappa = 1 - a C < 0 this integral is at most
pi |kappa|^{-1/2}; for kappa > 0 it is at most |kappa|^{-1/2} (pi + 2 log(1 + 1/|D_m|)), D_m the minimum of D. What is
missing for a hub diagonal is a small-ball bound for D_m, a quadratic polynomial in X_R whose quadratic part has two
squares, along u_R and along the coefficient vector of B; the degenerate case kappa = 0 is the D_H = 0 of Theorem 3.4.
Writing U = <u_R, X_R>, W = <q_R - (q_i/w_i) w_R, X_R> and r = v_i/w_i, that quadratic part is
-a (lambda U^2 + (a/kappa)(lambda r U + W)^2), whose determinant in (U, W) is a^3 lambda/kappa. For a small cross term W
is of size eps, the form is within eps of the rank-one form -a lambda (1 - 2 a q_i/w_i) U^2/kappa, and what is left is
the product U W, a twist of size eps: the obstruction of Section 2 comes back at this step. For kappa < 0 no small-ball
bound is needed: the single hub with a hub diagonal is then bounded by 1 + pi |w_i|^{-1} |kappa|^{-1/2}, and this holds
with any light diagonal, since a diagonal on the coordinates of R does not involve t and one on i only adds d_i/w_i^2
to C. The factor 1/|w_i| there comes from bounding the conditional density of t by its supremum. Averaging over X_R
instead is exact: with t_m = a B/(2 kappa) the centre and h = (D_m/|kappa|)^{1/2} the half-width of the cap {D > 0},
the part with 0 < D < 1 is at most |kappa|^{-1/2} int_{-1}^{1} rho_{Z_y}(0) dy/(1 - y^2)^{1/2} with
Z_y = t - t_m(X_R) - y h(X_R), a function of all the light coordinates. At y = 0 it is the linear functional
<w - (a/kappa)(lambda r u_R + q'), X'> + const, q' = q_R - (q_i/w_i) w_R, whose density is at most sqrt 2 divided by the
norm of that vector, with no dimension in sight; a dimension-free bound for kappa < 0 needs the same for the functionals
Z_y, which differ from it by y times the square root of a quadratic in X_R.

The same averaging can be done in the frame of w instead of a coordinate. Write X' = Y + L w with Y orthogonal to w.
Since v is orthogonal to w, V = <v, Y> does not depend on L, and the hub equation given Y is a x^2 + 2 x t + N(t) = s
with N(t) = A(Y) + B(Y) t + C t^2, B affine in Y and C = 2 <q, w> + sum_j d_j w_j^2 a constant: this kappa = 1 - a C
involves neither lambda nor a coordinate. For kappa < 0 the argument above gives, with t_m and h now functions of Y,

  ||p_Q||_inf <= 1 + |kappa|^{-1/2} int_{-1}^{1} rho_{Z_y}(0) dy/(1 - y^2)^{1/2},     Z_y = <w, X'> + F_y(Y),

F_y = beta - t_m - y h, on {D_m > 0}. Without light diagonal F_y is a function of the projection of X' on the span
of v and of the parts of q and b orthogonal to w, of dimension at most three. The derivative of Z_y along w is exactly 1, so Z_0, which is
linear, has density at most sqrt 2, and when D_m is the square of an affine function of Y each Z_y is linear on each
side of {D_m = 0} with coefficient vectors of norm at least 1, and has density at most 2 sqrt 2. In general
{Z_y = 0} is half of the quadric {(<w, X'> + beta - t_m)^2 = y^2 D_m/|kappa|}, and rho_{Z_y}(0) is the integral of the
product density over it against dY: a statement of the kind (CS) asks for, with the Jacobian in the direction of w
equal to 1. With q parallel to w and no twist the case is already covered by degenerate_hub/; the bound above uses
only f_h <= 1 and is of interest when q has a part orthogonal to w. The shape of F_y has to be used. For two coordinates with comb laws of N teeth and a generic rotated frame,
<w, X> is confined to a few intervals of length of order 1/N given <e, X>, e orthogonal to w, and a function of <e, X>
that follows those intervals makes the density of <w, X> + F(<e, X>) of order N, although every one-dimensional
projection has density at most sqrt 2.
Numerically the hub diagonal changes nothing in the spread regime: with a = 0.5 or -0.5 and eps = 0.01 the largest
density stays between 0.078 and 0.087 for a rough hub and between 0.120 and 0.132 for a uniform one at m = 8, 32, 128
(num/, Section 5).

So the single hub without diagonal is bounded on any fixed number of light coordinates, for every hub law, all light
laws and every cross term, with no leverage condition beyond w_i != 0: by the square root of that number through
Proposition 3.16 and by its logarithm through Proposition 3.17. The Fourier and slicing bounds of Sections 2 and 3
carry a double logarithm of 1/eps uniformly in the dimension instead. Neither estimate implies the other, and the
conjecture asks for both at once: what the results of this record leave open is the spread regime, many light
coordinates, every |w_i| small, and every coordinate that carries w also carrying v or the partner. In that regime the
density itself does not move: for comb laws on random frames with m = 8, 32, 128 light coordinates and eps = 0.01,
0.001 the largest density is 0.078 to 0.091 for a rough hub and 0.123 to 0.132 for a uniform one (num/, Section 5).

The two-hub case with a hub block (hub_pairs/, Proposition 7) has the same shape: there the elliptic maximal function
takes a supremum over the level, while the density only needs the ellipse at the level fixed by X'. With a transverse
square in the remainder the Fourier pairing of Theorem 3.10 avoids that supremum altogether, and with two hubs it
gives a bounded density with no logarithm (Section 6).

## 4. The part of the twist on the orthogonal coordinates

For the off-diagonal part E_Z of the twist on Z, integrating the hub in Fourier (Theorem H) is the natural route. It
works for every hub law, since each hub contributes its full |t|^{-1}, and it needs

  (TL_perp)   sup int int | E exp(i zeta L + i xi V + i t Z^T E_Z Z + i sum_i phi_i^t(X_i)) | d zeta d xi <= C

for t ||E_Z||_F up to a constant (Theorem D takes over above), uniformly in the separable phases phi_i^t. For interval
hub laws, cross terms together with E_Z would follow from the proof of Theorem 1 once Lemma 1.1 holds with E_Z present;
that needs (TL_perp) with shifts for |eta| ||E_Z||_F <= c and a decoupling bound for the frozen slices above it.

*A lattice check.* A twist on Z can agree with an aligned twist on a lattice. For W = (1,1,1,1), V = (1,-1,1,-1) and
P = (1,1,-1,-1), <P,k>^2 - <W,k>^2 = -4 (k_1 + k_2)(k_3 + k_4) for integer k. So with coordinates on Delta Z plus narrow
bumps and kappa = pi/(2 Delta^2), e^{i kappa <P,X>^2} and e^{i kappa <W,X>^2} agree on the support up to phases of order
1/Delta. But then (pi/2) a^2 mod 2 pi depends only on a mod 4, and the aligned twist is itself a combination of two
linear phases, e^{i pi a^2/2} = ((1 + i) + (1 - i) e^{i pi a})/2. A linear phase is a frequency shift, which Brascamp-Lieb
does not see, so the frame integral grows by at most a factor sqrt 2. The inflation of twist_obstruction/, Theorem 1
needs an irrational chirp, and for those the coincidence fails. No counterexample to (TL_perp) of this lattice type
exists.

*Numerics (num/, Section 1).* On four coordinates with comb laws the aligned twist raises the frame integral, up to
2.33 times at N = 6 and more than at N = 4, while the orthogonal twist lowers it (0.65-0.79 at N = 6). This is the
Gauss-sum picture: at kappa = 4 pi/q the chirp restricted to the lattice is a combination of q linear phases of modulus
q^{-1/2}. For an aligned twist these are translates of the untwisted transform along the integrated direction, each
with its full frame integral; for an orthogonal twist they move the product off its revival lattice.

## 5. Where the single hub stands

For the normal form (0.1) plus a twist E_Z on the orthogonal coordinates:
- interval hub laws with E_Z = 0, any q and any diagonal: Theorem 1;
- arbitrary hub laws with q in span(w, v), no diagonal and E_Z = 0: counterexample_search/, Proposition S; with
  q along w (a square sigma L^2) and any diagonal: degenerate_hub/;
- arbitrary hub laws, any q whose part outside span(w, v) has size eps > 0, any hub and light diagonal, spread light
  frame: bounded by 9.6 (eps |lambda|)^{-1/3} (Proposition 2.3) and by 17.0 eps^{-1/6} |lambda|^{-1/3} (Proposition 3.12,
  from the decay |phi_Q(eta)| <= 4.72 |lambda|^{-1/4} |eta|^{-3/4} that holds for every q, every diagonal and every hub law),
  and by C (1 + log(1/eps)) (Corollary 6.7, from |phi_Q(eta)| <= C |eta|^{-1}, Proposition 6.6),
  and without hub diagonal (a = 0) by
  58.2 + 7.7 log_+(2 B_eps^2), a double logarithm in 1/eps (Corollary 3.11, from the small-ball bound
  P(|Q - s| <= delta) <= delta (C + C log log(1/delta)) of Theorem 3.10, which holds for every q, every diagonal and all
  laws); with eps = 0 and any diagonal, degenerate_hub/; so what is open here is that double logarithm (and the power
  log(1/eps) with a hub diagonal) as eps -> 0 when q^ is spread; when q^ lives on a set whose complement carries the (w, v) frame,
  every eps is covered (Proposition 2.4);
- arbitrary hub laws with q outside span(w, v), no diagonal: bounded when the light coordinates have bounded support
  (Proposition 3.7, constant 1/2 + C |lambda|^{-1/2} (1 + log(1 + K^2 |lambda|))^{1/2}) or are window laws
  (Corollary 3.5, universal); for all light laws, when span(q_perp, b_perp) is spread together with the frame, by
  17.6 + sqrt 2 log(101.2 + 16 log_+(|lambda|/(2 eps))) for |lambda| >= 1 (Proposition 3.9, from the Fourier bound of
  Lemma 3.8 for the slice); so without diagonal only a double logarithm of 1/eps is missing as eps -> 0; closing it is the collision
  statement (VD) of Section 3, which is weaker than (CS) and which the maximal functional M does not deliver; each
  dyadic shell is bounded in L^2 for all laws (Lemma 3.6); splitting the hub law off first does not reduce it
  (Example 2.2);
- arbitrary hub laws, light coordinates of bounded support, any function of L and of a fixed k-dimensional
  projection orthogonal to the frame: Theorem 3.2 with Proposition 3.3;
- E_Z != 0: (TL_perp), for every hub law when q = 0, for a bounded density; the small-ball probability is at most
  C delta log(1/delta) for every twist, every hub diagonal and every hub law (Proposition 6.6).
- hub laws of total variation V, any q, any light diagonal, a = 0: at most 14.9 V^{2/3} for |lambda| >= 1 (Proposition 3.13)
  and at most 1/2 + 3 sqrt 2 + sqrt 2 log(1 + 2 pi^4 V/|lambda|) (Proposition 3.18, which also gives a logarithm of the
  number of intervals in the superlevel sets, and of D for a hub supported in an interval of length D);
- every hub law, all light laws, any cross term: bounded as soon as part of the partner (norm omega) or part of the
  transverse direction lives on light coordinates that carry nothing else (Propositions 3.14 and 3.15), or a
  well-conditioned part of both together (Proposition 2.4); without hub or light diagonal, bounded by
  1/2 + |w_i|^{-1}(27.9 + 0.5 log(1 + 2|lambda v_i^2/w_i^2 + 2 q_i/w_i|)) for every light coordinate i (|lambda| >= 1,
  Proposition 3.16), and by C(1 + |q|_inf + log(1 + |lambda|)) + (3/sqrt 2) log m on m light coordinates, uniformly as
  eps -> 0 (Proposition 3.17), and by the same with (3/sqrt 2) log K when the rows (w_i, v_i, q_i, b_i) take K directions
  (Proposition 3.19): what is open is uniformity in the number of those directions.
- a = 0, no light diagonal, linear terms in span(w, v, q^), every eps and every hub law, even a hub that sees P:
  bounded by a maximal functional of (L, P) with a logarithmic correction (Proposition 5.4); that functional is not
  bounded uniformly in the laws, and a uniform bound for a hub that sees P, (SP), would settle the case without hub
  diagonal for every eps at once. For a hub that sees P the density is at most 1/2 + 2 rho* (1 + log_+(c M*/rho*)), with
  rho* the density of L near -beta and M* a three-dimensional maximal quantity; so (SP) holds up to log K when the light
  coordinates that carry both q^ and the frame are supported in intervals of length K, with a bound that decreases in K
  for the comb laws of the numerics, and with a universal constant when those coordinates have window laws, whatever the
  other light laws (Proposition 5.5); also when w lives on a block of window laws on which v vanishes, the partner
  having any part there orthogonal to w (Proposition 5.6).

Only scales above the size of the cross term matter. Proposition 2.3 bounds the integral of |phi_Q| over
|eta| >= 1/(2 eps) by 126 sqrt 2 |lambda|^{-1/2}, for every hub law and any hub diagonal, so multiscale_fourier/, Lemma 6.1
gives

  ||p_Q||_inf <= C_K A_eps + 28.4 |lambda|^{-1/2},     A_eps = sup_s sup_{delta >= eps} P(|Q - s| <= delta)/delta,

with C_K the absolute constant of that lemma. The single hub is therefore bounded exactly when its small-ball
probabilities are linear in delta down to delta = eps. Theorem 3.10 and Proposition 6.6 give delta log log(1/delta) and
delta log(1/delta) there, which is where the double logarithm of Corollary 3.11 and the logarithm of Corollary 6.7 come
from. In the case left open every light coordinate that carries w or v also carries the partner of the cross term.

*Bilinear forms.* For independent random vectors x and y whose coordinates have densities at most K, Banks,
Garza-Vargas, Kulkarni and Srivastava (Overlaps, eigenvalue gaps, and pseudospectrum under real Ginibre and absolutely
continuous perturbations, arXiv:2005.08930, Corollary 2.4) bound the density of x^T Z y + x^T u + v^T y + w by
2 (C_RV K)^2 (2 e pi)^{1/2} min_{j >= 2} j^{-1/2} (sigma_1(Z) ... sigma_j(Z))^{-1/j}. Conditioning on y leaves a linear
form in x with coefficient vector Z y + u, and E|Z y + u|^{-1} is finite as soon as that vector has a bounded density in
two dimensions. The hub term of (0.1) is the bilinear form 2 X_h (L + beta) between the independent variables X_h and
X', of rank one: the coefficient of X_h is the scalar t = L + beta, E|t|^{-1} diverges logarithmically, and the
transverse square has to supply the rest. Two hubs make the bilinear part of rank two, the case of the corollary, which
is why Theorem 6.1 needs no bathtub. A hub spread over several coordinates is still of rank one; Proposition 6.9 uses the
spread on the hub side instead.

*The curved marginal.* (CS) and (VD) ask a curved section to behave like a flat one. Without the slice the question
takes its simplest form. Let u, v be orthonormal with u_i^2 + v_i^2 <= 1/2, U = <u, X'> and V = <v, X'>:

  (P2)   the density of U + c V^2 is at most an absolute constant, for every real c and all light laws.

At c = 0 this is the marginal bound. Two partial bounds hold, and each is uniform in the parameter the other loses.

**Proposition 5.1.** Let c != 0.
(a) ||p_{U + cV^2}||_inf <= 8 |c|^{-1/2} for all light laws.
(b) For every pair of light coordinates i != j, ||p_{U + cV^2}||_inf <= 4 (|v_i| + |v_j|)/|u_i v_j - u_j v_i| for all
light laws.

*Proof.* (a) The Fresnel identity in V, with Gaussian damping as in Lemma 1.1, gives
|E e^{i eta (U + cV^2)}| <= (4 pi |eta c|)^{-1/2} g(eta) with g(eta) = int |Phi(eta, xi)| d xi and
Phi(eta, xi) = prod_i psi_i(eta u_i + xi v_i). Coordinates with v_i = 0 contribute a factor at most 1; for the others,
Hoelder along the line with exponents p_i = 1/v_i^2 >= 2 and Lemma 1 of the first record give int |psi_i(eta u_i + xi v_i)|^{p_i} d xi <= |v_i|^{-1} 4 pi p_i^{-1/2} = 4 pi, so g(eta) <= 4 pi for every
eta, and Theorem F gives int g <= (4 pi)^2. Splitting the frequency integral at |eta| = pi, the density is at most
(2 pi)^{-1} (4 pi |c|)^{-1/2} (4 pi . 4 pi^{1/2} + pi^{-1/2} (4 pi)^2) = 8 |c|^{-1/2}.
(b) Condition on the other coordinates. Then U + cV^2 = A + c B^2 + const with A = u_i X_i + u_j X_j and
B = v_i X_i + v_j X_j + b_0, and (A, B) has density f_i(x_i) f_j(x_j)/|D|, D = u_i v_j - u_j v_i. Along the parabola
a = s' - c b^2 the coordinates x_i(b), x_j(b) are quadratic in the value b of B, with derivatives
x_i' = -(2 c v_j b + u_j)/D and x_j' = (2 c v_i b + u_i)/D. The conditional density at s is
|D|^{-1} int f_i(x_i(b)) f_j(x_j(b)) db. The critical points b_i = -u_j/(2 c v_j) and b_j = -u_i/(2 c v_i) are at distance
|D|/(2 |c v_i v_j|); put Delta = |b_i - b_j|/2. On |b - b_i| < Delta the map x_j is monotone with |x_j'| >= 1/(2 |v_j|), so,
bounding f_i by 1, that part of the integral is at most 2 |v_j|. In the same way the part on |b - b_j| < Delta is at most
2 |v_i|. On the rest x_j is monotone on each side of b_j with |x_j'| >= 1/(2 |v_j|), which gives 4 |v_j|, and
exchanging i and j gives 4 |v_i|. The integral is therefore at most 2 |v_i| + 2 |v_j| + 4 min(|v_i|, |v_j|), for
every value of the other coordinates, and so is its average. ∎

Bound (a) is uniform in the frame and blows up as c -> 0, although at c = 0 the density is at most sqrt 2. Bound (b) is
uniform in c, in the laws and in the other coordinates, and it grows as the frame spreads: with m coordinates of
comparable size the best pair has |D| of order 1/m and |v_i| + |v_j| of order m^{-1/2}. The same conditioning, with a third
coordinate to absorb the slice, bounds the slices of (CS) with constants that depend on the frame. The open part of (P2)
is small |c| together with many coordinates: a parabola that bends only where |V| is of order |c|^{-1/2}, far out in the
laws, for a frame spread over many coordinates. An absolute constant there would be a curved form of the
one-dimensional marginal bound; the Fourier arguments of this record, which are uniform in the frame, all lose there.

In the hub normalization the small values of c are harmless. Given X_h = x, the form 2 X_h (L + beta) + lambda V^2 equals
2x (L + (lambda/2x) V^2) + 2 x beta, so (a) with c = lambda/(2x) bounds its density by 4 sqrt 2 (|lambda| |x|)^{-1/2},
uniformly in the frame and the light laws; a small c is a large hub value, where this bound is small. The bound is
integrable in x, so the bathtub over the hub law gives ||p_Q||_inf <= 16 |lambda|^{-1/2} for every hub law and every hub
diagonal (a hub diagonal only shifts the conditional form); Proposition S covers this form, with twists in span(w, v), by
another route. What the single hub needs beyond it is the same conditional bound with the cross term 2 eps L P present.
There the Fresnel step leaves a frame integral carrying the twist e^{i kappa L P}, and on frames spread in three
dimensions that integral grows with the spread of the laws while the density of Q does not (num/, Section 13). Pairing
the hub law in L^{p'} instead of L^infinity moves the problem to an L^p norm in the partner frequency.

**Proposition 5.3.** Let Q = a X_h^2 + 2 X_h (L + beta) + lambda V^2 + 2 eps L P + sum_i phi_i(X_i) with L = <w, X'>,
V = <v, X'>, P = <q^, X'>, (w, v, q^) orthonormal with w_i^2 + v_i^2 + q^_i^2 <= 1/2, eps > 0, and a, beta and the
one-coordinate quadratics phi_i arbitrary. For 1 <= p < 2 put

  J_p = sup int dt ( int dy |E exp(i (y L + t V + kappa L P) + i sum_i chi_i(X_i))|^p )^{1/p},

the supremum over |kappa| <= 1 and all real quadratics chi_i. Then for every hub law and all light laws

  ||p_Q||_inf <= 1/pi + 2^{-1/p} (1/p - 1/2)^{-1} J_p (4 pi |lambda|)^{-1/2}/pi + 28.4 |lambda|^{-1/2}.

*Proof.* Given X_h = x the form is a x^2 + 2 x beta + 2 x L + lambda V^2 + 2 eps L P + sum_i phi_i(X_i), so
|E e^{i eta Q}| <= int f_h(x) |Phi(eta, 2 eta x)| dx with Phi(eta, y) = E exp(i y L + i eta (lambda V^2 + 2 eps L P +
sum_i phi_i(X_i))); the hub diagonal is a phase. Hoelder with ||f_h||_{p'} <= 1 (since f_h <= 1 and int f_h = 1) and the
substitution y = 2 eta x give |E e^{i eta Q}| <= (2 |eta|)^{-1/p} ||Phi(eta, .)||_{L^p}. The Fresnel identity in V, with
Gaussian damping as in Lemma 1.1, writes Phi(eta, y) as an integral over t, against a kernel of modulus
(4 pi |eta lambda|)^{-1/2}, of E exp(i (y L + t V + kappa L P) + i eta sum_i phi_i(X_i)) with kappa = 2 eta eps, and
Minkowski's inequality in y gives ||Phi(eta, .)||_{L^p} <= (4 pi |eta lambda|)^{-1/2} J_p whenever |eta| <= 1/(2 eps).
Integrate |eta|^{-1/p - 1/2} over 1 <= |eta| <= 1/(2 eps), use |E e^{i eta Q}| <= 1 for |eta| <= 1, and bound the integral
over |eta| >= 1/(2 eps) by 126 sqrt 2 |lambda|^{-1/2} (Proposition 2.3). ∎

For p = 1 the hypothesis is the frame bound with the twist that Theorem H needs (Section 2). Hoelder moves the
integrability from the frame integral to the hub law, which is bounded, and any p < 2 leaves the decay |eta|^{-1/p -
1/2} integrable. The hypothesis would close the single hub with a spread cross term for every hub law and every hub
diagonal, the case left open by Proposition 2.3 and Corollaries 3.11 and 6.7 when q lies outside span(w, v). The
numerics do not support it uniformly. On one irrational rotation of the spread frame of num/, Section 13, the mixed
norm with p = 3/2 stays between 7 and 9 at kappa = 1 for N = 3 to 12 while the p = 1 norm grows from 17 to 32; on a
second rotation, with comb laws at the integers, every mixed norm with p <= 2 grows with N, the one with p = 2
included, although at p = 2 the inner norm is exact by Plancherel, 2 pi int |mu_t(l)|^2 dl with mu_t(l) = E[e^{i (t V
+ kappa l P)}; L in dl]/dl. The mechanism appears to be this: given L = l, comb laws leave a sparse set of lattice
points, the twist is a shift of the frequency of P, and as l varies the line {(t, kappa l)} of the conditional
transform meets its revivals. So the exponent of the hub pairing is not where the route loses. It loses when moduli
are taken at a fixed hub value and a fixed Fresnel frequency t, which discards the cancellation that keeps the density
itself flat (num/, Section 13). The characteristic function of Q itself behaves well: for fine comb laws on the first
rotation |eta|^{3/2} |E e^{i eta Q}| stays between 1.0 and 1.4 and its integral is 3.0 for N = 4, 8, 16 and at eps =
0, 0.03 and 0.003 alike, and for combs at the integers it decays like |eta|^{-1} over several decades with a
coefficient that falls with the spread. A Fourier proof is not ruled out; it has to pair the hub with the light
transform before any modulus is taken. A cross term with a part along w or v adds the aligned chirps L^2 and L V on
top of this; there the square has to go to the hub first, as in degenerate_hub/.

The arithmetic behind the numerics of Section 3 is classical. A strictly convex arc of length l contains at most
O(l^{2/3}) points of the integer lattice (Jarnik), while a lattice line of length l contains about l of them. For comb laws
on a common lattice and a rational frame the projected lattice is two-dimensional, and a parabola, whose slope turns, can
stay near a lattice row only while its slope is close to that of the row; rows are lines, which the marginal bound
controls. This is consistent with the resonant parabolas of num/cs_resonant.py staying below the flat value and
decreasing in N. For an irrational frame the projected lattice is dense and no counting argument of this kind is
available.

Spreading the frame does not rescue the maximal route, and the curvature is what an argument has to use.

**Example 5.2.** Let m = 4, S_1 = X_1 + X_2 and S_2 = X_3 + X_4, and rotate the orthonormal pair (1,1,1,1)/2,
(1,1,-1,-1)/2 through the angle theta with tan theta = sqrt 2:

  U = ((cos theta + sin theta) S_1 + (cos theta - sin theta) S_2)/2,   V = ((cos theta - sin theta) S_1 - (cos theta + sin theta) S_2)/2.

Every coordinate has u_i^2 + v_i^2 = 1/2. The variables S_1, S_2 are independent with densities at most 1, the
determinant is -1/2 and the two coefficients of V have moduli adding up to max(cos theta, sin theta) <= 1, so the
argument of Proposition 5.1(b), run with S_1 and S_2 in place of two coordinates, bounds the density of U + cV^2 by 8 for
every c and all laws. Now let each X_i be uniform on the N teeth [j, j + 1/N], 0 <= j < N, with N >= 6. The density of
S_1 is a tent of height n_k/N >= 1/3 above each integer N/2 <= k <= 3N/2 (n_k counts the pairs of teeth with sum k),
so the density of (S_1, S_2) is at least 1/36 on squares of side 1/N at about N^2 lattice points, and rho_{U,V} >= 1/18
on their images. The ratio of the coefficients of V is (1 + sqrt 2)^2, a quadratic irrational, so the values of V at any
two of these points differ by at least c/N; the lines {V = v} that meet one of the squares therefore fill a set of v of
measure at least c'N, and M_2 = int sup_u rho_{U,V}(u, v) dv >= c'N/18 grows linearly in N, for a frame that satisfies
the leverage condition, while every curved marginal U + cV^2 has density at most 8.
The same happens with many coordinates: on a rational plane in R^8 with eight distinct coordinate directions and an
irrational basis, M_2 grows linearly in N while the density of U + cV^2 stays within 13 percent of the flat marginal
(num/, Section 12).

*The cross term as a hub that sees P.* Take a = 0. Since 2 X_h (L + beta) + 2 eps L P = 2 (L + beta)(X_h + eps P)
- 2 eps beta P, and -2 eps beta P is a linear term in the light coordinates, the single hub with a cross term is the
eps = 0 form

  Q_0 = 2 Y (L + beta) + lambda V^2 + 2 L <q_0, X'> + sum_i phi_i(X_i),     q_0 in span(w, v),

in the hub Y = X_h + eps P, whose conditional law given X' has density f_h(y - eps P) <= 1 and depends on X' only
through P. Call a hub with this property, for some conditional density f(. | p) <= 1, a hub that sees P. Given X', Q_0
is affine in Y with slope 2(L + beta), so p_{Q_0}(s) = int int f(x | p) W(x, p) dx dp, where W is the density of
(x*, P) under the weight 1/(2|L + beta|) and x* = (s - lambda V^2 - 2 L <q_0, X'> - sum_i phi_i(X_i))/(2(L + beta)) is
the hub value that puts Q_0 at s. The supremum over hubs that see P is

  Phi(s) = int ( sup_{|A| = 1} int_A W(x, p) dx ) dp,

and it bounds sup over hub laws of p_Q(s) for every eps. A hub that does not see P uses one set A for all p, and its
supremum is the eps = 0 bathtub, which Proposition S and degenerate_hub/ bound. So the open core without hub diagonal
would follow, for every eps at once, from

  (SP)   Phi(s) <= C for every frame, every unit q^ orthogonal to w and v, all light laws, every q_0, all phi_i and
         every s.

A hub diagonal changes only the partner seen by the new hub. With Y = X_h + eps P,

  a X_h^2 + 2 X_h (L + beta) + 2 eps L P = a Y^2 + 2 Y (L + beta - a eps P) + a eps^2 P^2 - 2 eps beta P,

so given P the form is the eps = 0 form with a hub diagonal and with beta replaced by beta - a eps P. The single hub
with a hub diagonal and a cross term of any size would therefore follow from the eps = 0 statement with a hub diagonal
(proved in degenerate_hub/ for an independent hub when the twist inside span(w, v) is a multiple of L^2) for a hub that
sees P and a shift beta that depends on P, the analogue of (SP) with a hub diagonal.

When w and v vanish on the support of q^, the value of P tells nothing about x* beyond an independent shift, Phi(s) is
at most the supremum over s of the eps = 0 bathtub, and (SP) holds with the eps = 0 constants; this is the case of
Proposition 2.4 in which the frame stays off the support of q^. In general Phi exceeds the eps = 0 bathtub, but by less
than raw estimates suggest: the estimator keeps the largest noisy bins of each P-column, and running it with P shuffled
across the samples, where a hub that sees P can gain nothing, measures that bias. Net of it, on the spread frame where
the twisted frame integrals grow with N, a hub that sees P gains at most about 2 per cent for laws of bounded range
(fine combs at N = 4, 8, 16, two-scale combs at N = 3, 5). For comb laws at the integers the gain grows slowly with N
and does not level off up to N = 20: Phi is 0.59, 0.35, 0.19, 0.16, 0.11, 0.083 at N = 4, 6, 10, 12, 16, 20 against
0.56, 0.31, 0.15, 0.12, 0.076, 0.054 for the eps = 0 bathtub (s = 0, beta = 0), a factor 1.06 rising to 1.54, and the
factor is 1.66 and 1.74 at N = 12, 16 with s = 2, beta = 0.5. Phi itself falls: N Phi decreases from 2.4 to 1.7. So a
hub that sees P can gain an unbounded factor over the eps = 0 value, while in absolute terms it gains nothing. Random
searches over 40 comb laws on that frame and over 113 random frames on four to six coordinates with random comb laws
agree: the largest net Phi found is 0.70 (uniform laws, no gain), factors of 1.8 to 2.7 occur only where the eps = 0
value is at most 0.11. On the two-class frame of Example 5.2, where the maximal functional M_2 grows like N, the gain is 10 per cent at
N = 4, 8 and 1 per cent at N = 16 (num/, Section 13).

The argument of Proposition S carries over, with a maximal functional of the pair (L, P) in place of the bound 2 for the
density of (L, V).

**Proposition 5.4 (a hub that sees P).** Let L = <w, X'>, V = <v, X'>, P = <q^, X'> with w, v, q^ orthonormal, let Y
be a hub that sees P, and let Q = 2 Y (L + beta) + lambda (V - v_c(L, P))^2 + F(L, P) with v_c and F measurable. Put
t = l + beta, c = 2 sqrt 2 |lambda|^{-1/2} and a(l, p) = sup_v rho_{L,V,P}(l, v, p). Then

  ||p_Q||_inf <= 1/2 + int int_{|l + beta| <= 1} min(rho_{L,P}(l, p), c a(l, p) |t|^{1/2}) dl dp/(2|t|).

With r(p) = sup_{|l + beta| <= 1} rho_{L,P}(l, p) and a(p) = sup_{|l + beta| <= 1} a(l, p) the right side is at most
1/2 + int r(p) (2 + 2 log_+(c a(p)/r(p))) dp.

*Proof.* Given X', Y has a density f(. | P) <= 1 and Q is affine in Y with slope 2t, t = L + beta, so
p_Q(s) = int rho_{L,V,P}(l, v, p) f(y | p)/(2|t|) dl dv dp with y = (s - lambda (v - v_c)^2 - F)/(2t). For fixed (l, p)
the bathtub step of Proposition S gives int f(y | p) dv/(2|t|) <= sqrt 2 (|lambda| |t|)^{-1/2}. So the integral over v is
at most min(rho_{L,P}(l, p), c a(l, p) |t|^{1/2})/(2|t|), and at most rho_{L,P}(l, p)/2 for |t| > 1, where the whole
contributes at most 1/2. For the second bound, the integral over |t| <= 1 of min(r, c a |t|^{1/2})/(2|t|) is 2ca when
ca <= r and 2r + 2r log(ca/r) otherwise, in both cases at most r (2 + 2 log_+(ca/r)). ∎

With a = 0 and no light diagonal, the single hub with its linear terms in span(w, v, q^) has this form for every eps,
since 2 X_h (L + beta) + 2 eps L P = 2 (L + beta)(X_h + eps P) - 2 eps beta P and a twist in span(w, v) only moves v_c
and F. Its density is therefore bounded by the right side, uniformly in eps and in the hub law. When P is independent of
(L, V), both bounds are at most a function of lambda alone. The integrand of the first is
rho_{L,P} min(1, c sigma |t|^{1/2})/(2|t|), with sigma = a/rho_{L,P} the largest conditional density of V given
(L, P) = (l, p), so it is large only where L is near -beta and (L, P) nearly determines V.

The second bound is a maximal functional of (L, P), local in l, with a logarithmic correction. It is not bounded under
the leverage condition of (0.1) alone. Take w = (e_1 + e_2)/sqrt 2, q^ = (e_1 - e_2)/sqrt 2, v = (e_3 + e_4)/sqrt 2, and
for X_1, X_2 combs of N teeth of width 1/N at spacings N^{-1/2} and 0.7 sqrt 2 N^{-1/2}. Then rho_{L,P} is 1 on
disjoint squares of side 1/N whose projections on the P-axis cover most of the range of P, and int r(p) dp = 3.9, 7.5,
22.6, 83.7 at N = 64, 256, 1024, 4096, growing like N^{1/2} up to the length 1.41 N^{1/2} of that range
(num/twist3d/rloc_two_coord_output.txt, exact). The first bound stays below 1/2 + sup rho_L (2 +
2 log_+(4 |lambda|^{-1/2})) there, because V is independent of (L, P) and has density at most sqrt 2, and the
configuration is bounded anyway by Proposition 3.15. On the spread frame of num/, Section 13, with lambda = 1 and a(p)
replaced by its bound 2 sqrt 2, the second bound is 9.8, 6.8, 4.6 for combs at the integers at N = 4, 8, 16, 7.9, 7.0,
6.4 for fine combs, and 4.8, 3.0, 2.1 for N teeth of width 1/N at spacing N^{-1/2} (N = 16, 64, 256), estimated from
histograms of (L, P) with bins of side 0.05 (num/twist3d/rloc_output.txt; for the integer combs at N = 8, 16 these bins
do not resolve the cells, and finer bins raise the estimate).

The first bound is not uniformly bounded under the leverage condition w_i^2 + v_i^2 + q^_i^2 <= 1/2 of Proposition 5.3
either. Let L live on two coordinates of its own with uniform laws, and V, P on four others, with v = (1, 1, 1, 1)/2 and
q^ = (1, -1, 1, -1)/2 there and combs of N teeth of width 1/N at spacings 8/N, 8, 8N, 8N^2. The P-values of the cells
are distinct multiples of 4/N and each cell has P-width 2/N, so P determines the cell, V given (L, P) lies in an
interval of length 2/N, sigma >= N/2 on the support, and the first bound grows like log N. That configuration is bounded
by Proposition 3.14, since L lives on coordinates that carry nothing else. Where P determines V the curvature in V is of
no use, because the hub knows V; what keeps the density bounded is that lambda (V - v_c)^2 + F, evaluated near
L = -beta, rarely falls near s. For a hub that sees P this becomes a question of how many cells of a sum of combs placed
along four directions of the (V, P)-plane can lie near a parabola, where incidence bounds for sumsets suggest few.

The two mechanisms combine additively. In the model case where v_c and F depend on P only, split
rho_{L,V,P} = rho_A + rho_B with rho_A, rho_B >= 0. The proof of Proposition 5.4 applies to rho_A. For rho_B take the
bathtub in l at fixed (v, p): there y = z/(2t) with z = s - lambda (v - v_c(p))^2 - F(p), the weight dt/(2|t|) becomes
dy/(2|y|) on |y| >= |z|/2, and a hub density at most 1 of mass 1 collects at most log(1 + 1/|z|) of it. Hence

  ||p_Q||_inf <= 1/2 + A(rho_A) + int int sup_{|l + beta| <= 1} rho_B(l, v, p) log(1 + 1/|z(v, p)|) dv dp,

with A(rho_A) the double integral in the first bound of Proposition 5.4 computed with rho_A in place of rho_{L,V,P}.
The single hub is in the model case when it has no twist inside span(w, v) and no linear term along w: then v_c is
constant and F is affine in P. In the example above all of rho goes to rho_B, and the last term is sup rho_L times
E log(1 + 1/|Z|), Z = lambda (V - v_c)^2 + F(P) - s; for the single hub Proposition 5.1(a), applied to the pair (P, V),
bounds the density of Z, so this term is bounded. (SP) in the model case would follow from a split of every product law
into a part where V given (L, P) is spread and a part on which the supremum over l in the last term is controlled.

In each example where P nearly determines L or V it does so because the laws are spread over a long range in the
coordinates P reads, so that P separates their cells; the same spread makes the density of L near -beta small (the
first example), or makes lambda (V - v_c)^2 rarely fall near s (the second). If P determined L and V exactly, x* would
be a function of P, a hub that sees P could sit on it, and the supremum would be E[1/(2|L + beta|)], which is infinite
as soon as L has a positive density at -beta. So (SP) is an uncertainty statement for linear functionals of independent
coordinates: the better P resolves L or V near the degenerate values, the less mass L or V can put there. For comb laws
with teeth of width 1/N the count behind it is short. A functional of range O(1) that uses two or more coordinates takes
N^2 or more values on the cells, most of them within O(1/N^2) of another, while the value of P varies by order 1/N
inside a cell; so P can resolve such a functional only if it is spread, and the leverage condition, which puts L and V
on at least two coordinates each, leaves no narrow functional for P to resolve. The computations above measure the
trade-off for general comb laws, and none of them comes close to breaking it.

The first bound of Proposition 5.4 depends on the three-dimensional maximal quantity only through a logarithm, and
that logarithm is weighted by the density of L near -beta. Integrated over p first, it reduces to two numbers, and for
bounded laws the trade-off can then be proved: the coordinates of the partner that carry neither w nor v are
conditioned away, and on the others the tilt of Proposition 3.3 bounds the maximal quantity.

**Proposition 5.5 (the partner coordinates).** Let L, V, P be as in Proposition 5.4, let W be a set of light coordinates
on which w and v vanish, and let Q = 2 Y (L + beta) + lambda (V - v_c(L, P))^2 + F(L, P) + G(X_W) with Y a hub that sees
P and v_c, F, G measurable. Let T be the set of light coordinates outside W with q^_i != 0, q^_T the restriction of q^
to T and P' = <q^_T, X'>/|q^_T|. Put

  rho* = sup_{|l + beta| <= 1} rho_L(l),     M* = sup_{|l + beta| <= 1} int sup_v rho_{L,V,P'}(l, v, p) dp

(M* = sup_{|l + beta| <= 1} sup_v rho_{L,V}(l, v) if q^_T = 0), and c = 2 sqrt 2 |lambda|^{-1/2}.
(0) For every hub that sees P and all light laws, ||p_Q||_inf <= 1/2 + 2 rho* (1 + log_+(c M*/rho*)).
(a) Let K >= 1. If every X_i with i in T is supported in an interval of length at most K, then M* <= 20.52 K, and

  ||p_Q||_inf <= 1/2 + 2 rho* (1 + log_+(58.03 K |lambda|^{-1/2}/rho*)) <= 1/2 + 2 sqrt 2 (1 + log_+(41.1 K |lambda|^{-1/2})).

(b) If every X_i with i in T has a window law U[0, 1] * nu_i, then ||p_Q||_inf <= 1/2 + 2 sqrt 2 (1 + log_+(41.1 |lambda|^{-1/2})),
uniformly in the nu_i; for |lambda| >= 1 this is at most 13.9.

*Proof.* (0) Condition on X_W. Then G(X_W) is a constant and P = |q^_T| P' + c with c a constant, so the hub, whose
conditional law depends on X' only through P, is a hub that sees P'. Since w and v vanish on W, q^_T is orthogonal to w
and v, and (w, v, q^_T/|q^_T|) is orthonormal; write v_c and F as functions of (L, P'). The law of (L, V, P') does not
depend on X_W. In the first bound of Proposition 5.4, integrate the minimum over p first:
int min(rho_{L,P'}(l, p), c a(l, p) |t|^{1/2}) dp <= min(rho_L(l), c |t|^{1/2} int a(l, p) dp) <= min(rho*, c M* |t|^{1/2})
for |t| <= 1, t = l + beta. The integral of this minimum against dt/(2|t|) over |t| <= 1 is 2 c M* when c M* <= rho* and
2 rho* (1 + log(c M*/rho*)) otherwise. If q^_T = 0 the hub sees nothing and the same computation runs without p.
(a) Tilting the law of X' by e^{theta P'} moves only the coordinates of T, and the proof of Proposition 3.3 with Z = P'
gives sup_v rho_{L,V,P'}(l, v, p) <= 2^{3/2} exp(-2 (|p - E P'| - 3K)_+^2/K^2) for every l, so
M* <= 2^{3/2} (6 + (pi/2)^{1/2}) K = 20.52 K; if q^_T = 0, M* <= 2 by the bound for two-dimensional marginals. The first
inequality is (0) with c M* <= 58.03 K |lambda|^{-1/2}; the second follows from rho* <= sqrt 2, since x (1 + log_+(y/x))
is nondecreasing in x. (b) Write X_i = U_i + Y_i for i in T, with U_i uniform on [0, 1] and Y_i ~ nu_i, and condition on
the Y_i as well, as in Corollary 3.5. The coordinates of T become uniform on unit intervals, L, V and P move by constants
that go into beta, v_c and F, and the hub still sees P. The second bound of (a) with K = 1 applies to the conditional
law; it does not involve rho*, which the conditioning may change. ∎

With a = 0 the single hub has this form for every eps when the light diagonal vanishes outside W and the linear term
is a vector of span(w, v, q^) plus one supported on W. So without light diagonal on the coordinates that carry the
frame, (SP) holds, uniformly in eps and in the hub, up to the logarithm of the support length of the coordinates that
carry both the frame and the partner, and with a universal constant when those coordinates have window laws; every
other light law is arbitrary, and the frame may be spread over any number of coordinates.

Part (0) says more. Since rho* <= sqrt 2 and rho* log(1/rho*) is bounded, (SP) can fail only along laws for which
rho* log M* is unbounded, so that M* is exponentially large in 1/rho*; for laws supported in intervals of length K on T
this requires K to be exponentially large in 1/rho*. On the spread frame
of num/, Section 13, the combs at the integers 0, ..., N - 1 have rho* = 0.364, 0.169, 0.084, 0.042, 0.021 at
N = 4, 8, 16, 32, 64, so N rho* stays near 1.35 (num/twist3d/rho_star_output.txt), and with K = N and lambda = 1 part
(a) gives 5.9, 3.5, 2.2, 1.5, 1.1: a bound that decreases to 1/2, where the version with rho* <= sqrt 2 grew like
log N. The configurations that part (0) does not reach are those in which L keeps a density of order one near -beta
while (L, P) determines V over a long range of P, as in the second example after Proposition 5.4; there L lived on
coordinates of its own and Proposition 3.14 applies. What (SP) still has to cover is the entangled version of that
configuration, with structure below unit scale on the coordinates that carry both the frame and the partner.

The dilation argument of Proposition 3.14 also survives a hub that sees P, and it needs less than there when L lives on
coordinates of its own: the partner may have a part on those coordinates, orthogonal to w, which P and the hub then see.

**Proposition 5.6 (the hub partner on a block of its own).** Let L, V, P and Y be as in Proposition 5.4, and let
Q = 2 Y (L + beta) + lambda (V - v_0)^2 + F_0 + F_1 P with constants v_0, F_0, F_1, and let w_i^2 + v_i^2 <= 1/2 for every
light coordinate, as in (0.1). Suppose that w is supported on a set I_1 of light coordinates on which v vanishes, let D be the projection of X_{I_1} on the orthogonal complement of w in
R^{I_1}, and put M_D = int sup_{|l + beta| <= 1} rho_{L,D}(l, d) dd. Then for every hub that sees P and all light laws

  ||p_Q||_inf <= 1/2 + M_D (2 + log(1 + 2 pi^4/|lambda|)).

If every coordinate of I_1 has a window law U[0, 1] * nu_i, the bound holds with sum_{i in I_1} |w_i| in place of M_D,
uniformly in the nu_i and in the other light laws; for |I_1| = 2 and |lambda| >= 1 it is at most 10.8.

*Proof.* Let R be the light coordinates outside I_1. Since q^ is orthogonal to w and w lives on I_1, the restriction of
q^ to I_1 is orthogonal to w, so P is a function of (D, X_R); V is a function of X_R. Given (D, X_R), the hub has a fixed
conditional law f(. | P), the value z = s - lambda (V - v_0)^2 - F_0 - F_1 P is fixed, x* = z/(2t), and t = L + beta
has the conditional density g(. | D) of L given D, since L depends only on X_{I_1}. The part |t| >= 1 contributes at
most 1/2. On |t| < 1 the substitution x = z/(2t) and the bathtub principle, as in the proof of Proposition 3.14 with
kappa = 0, bound the conditional density by G(D) log(1 + 1/|z|), G(D) = sup_{|l + beta| <= 1} g(l | D). Given D, z is a
real quadratic polynomial in X_R containing -lambda V^2, with v supported on R and v_i^2 <= 1/2, so the end of that proof
gives E[log(1 + 1/|z|) | D] <= 2 + log(1 + 2 pi^4/|lambda|). Since E G(D) = M_D, the bound follows. For window laws,
condition on the nu-parts of the coordinates of I_1 as in Corollary 3.5: X_{I_1} becomes uniform on a unit cube, L and
D move by constants, and the hub still sees P. Then rho_{L,D} is the indicator of a rotated unit cube, and M_D is at most
the volume of the projection of the unit cube on the hyperplane orthogonal to w, which is sum |w_i| (Cauchy's
formula). For |I_1| = 2 the leverage condition forces w_i^2 = 1/2, so the sum is sqrt 2. ∎

Proposition 3.14 needed q^ to be proportional to w on the block of L; here q^ may take any direction there orthogonal
to w, so P sees the whole block except L itself, and the price is a law on the block with no structure below unit
scale. The proof uses the window laws only to bound M_D: for coordinates of I_1 supported in intervals of length K,
rho_{L,D} <= 1 on the image of a box of side K, so M_D <= K^{|I_1| - 1} sum |w_i|, which is sqrt 2 K for two coordinates.
Nor does it use that v vanishes on I_1 beyond making V a function of X_R: since w lives on I_1, the part of v there is
orthogonal to w, so V is always a function of (D, X_R), and the proof goes through with |lambda| |v_R|^2 in place of
|lambda| whenever v_R, the restriction of v to R, satisfies v_i^2 <= |v_R|^2/2. On the smallest configuration that only
this proposition covers, w = (e_1 + e_2)/sqrt 2 on two uniform coordinates, v = (e_3 + e_4)/sqrt 2 on two combs at the
integers and q^ = (e_1 - e_2 + e_3 - e_4)/2, the worst hub that sees P is 1.88, 1.20, 0.78, 0.45 at N = 4, 8, 16, 32
(s = 0, net of the shuffled control; num/, Section 13), against the bound 10.8. With window laws on the coordinates that
carry both the frame and the partner (Proposition 5.5), or on a block that carries all of w (Proposition 5.6), a hub
that sees P gains nothing unbounded. The configurations left have structure below unit scale on coordinates that carry
both the frame and the partner, and no block of bounded laws carries all of w.

*Summary of the obstruction.* The single hub with a small spread cross term is bounded up to log log(1/eps) without hub
diagonal and up to log(1/eps) with one; it is bounded outright for hub laws of bounded variation, for localised cross
terms, when part of the frame or of the partner lives on coordinates that carry nothing else, on any fixed number of
light coordinates when there is no diagonal (with a constant of order the logarithm of that number), and, without light
diagonal on the frame, when the coordinates that carry both the frame and the partner have window laws or when w lives
on a block of window laws; up to a square
root of a logarithm it is bounded for light laws of bounded support. Every route that bounds the transform by moduli taken before
the hub integration loses in the same way. At frequency eta the partner L carries the twist kappa L P with
kappa = 2 eta eps, which shifts the partner frequency by kappa P; for comb laws spread over a range of order N the
resulting frame integrals, in L^1 or in the mixed L^p norms of Proposition 5.3, grow with N (Section 2 and num/,
Section 13). Twists that do not contain L stay bounded, and so do all of these integrals for laws of bounded range.
The density of Q and its transform do not grow: in every configuration computed int |E e^{i eta Q}| d eta is bounded
uniformly in eps and N. A proof therefore has to estimate the pairing int f_h(x) E exp(i eta (2x (L + beta) +
lambda V^2 + 2 eps L P)) dx while keeping the oscillation in the hub variable, or replace it by a real-variable
estimate of the kind (CS), (VD) or (SP) describe.

## 6. Two or more hubs

With two hubs the Fourier pairing of the proof of Theorem 3.10 needs no bathtub. Plancherel in the two-dimensional
hub partner gives a factor |eta|^{-1} that does not depend on the hub block, and with the Fresnel factor of the slice
the frequency integral converges.

**Theorem 6.1.** Let X_H = (X_{h_1}, X_{h_2}) and X' have independent coordinates with densities at most 1. Let M be a
2 x m matrix with singular values s_1 >= s_2 > 0 whose row space has the orthonormal basis e_1, e_2, let v be a unit
vector orthogonal to e_1 and e_2 with e_{1i}^2 + e_{2i}^2 + v_i^2 <= 1/2 for every i, and put L = M X' and V = <v, X'>. For
every real symmetric 2 x 2 matrix B, beta in R^2, lambda != 0, q_1, q_2 in R^m and one-coordinate quadratics phi_i, the form

  Q = X_H^T B X_H + 2 <X_H, L + beta> + lambda V^2 + 2 L_1 <q_1, X'> + 2 L_2 <q_2, X'> + sum_i phi_i(X_i)

satisfies ||p_Q||_inf <= 11.5 (s_1 s_2)^{-2/5} |lambda|^{-1/5}, for all laws.

The terms 2 L_j <q_j, X'> contain every term with a factor L_j: squares and products of L_1 and L_2, L_j V, and the cross
terms with outside directions. B is any hub block, definite, indefinite or singular.

*Proof.* By weak limits it suffices to take compactly supported laws. Put
Y_{t_0} = lambda V^2 + 2 sum_j t_{0,j} <q_j, X'> + sum_i phi_i(X_i). As in the proof of Theorem 1, now with square cells in
R^2, P(|Q - s| <= delta) = lim_{h -> 0} sum_k int_{C_k} d^2t int G(t_k, y) mu_{t_k, t}(dy), where mu_{t_0, t} is the slice at
L = t of (L, Y_{t_0}) and G(t, y) = P(|q_t(X_H) + y - s| <= delta), q_t(x) = x^T B x + 2 <x, t + beta>. As a function of y,
G(t, .) = 1_{[-delta, delta]} * g_t with g_t the density of s - q_t(X_H), and g_t^(eta) = e^{i eta s} F_eta(2 eta (t + beta)),
where F_eta is the two-dimensional Fourier transform of x -> f_H(x) e^{-i eta x^T B x}. Plancherel in R^2 gives

  int |g_t^(eta)|^2 d^2t = (2|eta|)^{-2} (2 pi)^2 int f_H^2 <= pi^2/eta^2     for every eta != 0, whatever B is.

For the slice, Fresnel in V and the three-dimensional Brascamp-Lieb bound for (e_1, e_2, v), after the change of variables
that takes the frequency of L to that of (<e_1, X'>, <e_2, X'>), give |mu^_{t_0, t}(eta)| <= C_3 (|eta| |lambda|)^{-1/2} with
C_3 = (2 pi)^{-2} (4 pi)^{5/2}/(s_1 s_2) = 8 sqrt(pi)/(s_1 s_2); also |mu^_{t_0, t}(eta)| <= rho_L(t), and int rho_L = 1. By
Cauchy-Schwarz over the cells and t,

  sum_k int_{C_k} |g_{t_k}^(eta)| |mu^_{t_k, t}(eta)| d^2t <= (sum_k |C_k| |g_{t_k}^(eta)|^2)^{1/2} (C_3 (|eta| |lambda|)^{-1/2})^{1/2},

and only the finitely many cells meeting the support of L count, so the Riemann sum tends to the integral of |g_t^(eta)|^2
over that set, which is at most pi^2/eta^2. With K_2 = pi C_3^{1/2} |lambda|^{-1/4}, the pairing at frequency eta is thus at most
min(1, K_2 |eta|^{-5/4}) in the limit (the 1 from |g^| <= 1 and |mu^| <= rho_L), and Parseval with dominated convergence gives

  P(|Q - s| <= delta) <= (2 pi)^{-1} int min(2 delta, 2/|eta|) min(1, K_2 |eta|^{-5/4}) d eta.

Dividing by 2 delta and letting delta -> 0, ||p_Q||_inf <= (2 pi)^{-1} int min(1, K_2 |eta|^{-5/4}) d eta = (5/pi) K_2^{4/5}, and
(5/pi) (pi (8 sqrt pi)^{1/2})^{4/5} = 11.49. ∎

For one hub the same Cauchy-Schwarz gives pi^{1/2} |eta|^{-1/2} in place of pi/|eta|, hence |eta|^{-3/4} at frequency eta,
which is not integrable; that is why a single hub needs the slice-by-slice argument of Theorem 3.10 and loses a double
logarithm. For k >= 2 hubs with a (k + 1)-dimensional spread frame the power is |eta|^{-k/2 - 1/4}, and the argument goes
through unchanged.

So a pair of hubs with any hub block is bounded as soon as the remainder carries a square transverse to the hub
partners, for every hub law and all light laws. This is the configuration of hub_pairs/, Conjecture 6, for both signs
of det B, and case M-2H of architecture/PROOF_TREE.md for remainders of this form; the elliptic maximal inequality of
hub_pairs/, Proposition 7, is not needed. The rank-two counterexample of hub_pairs/, Theorem 1, has no transverse square:
there the slice of the remainder is a point mass and its transform does not decay. A twist on the coordinates orthogonal
to (e_1, e_2, v) enters the slice bound through the frame integral, so for such remainders the two-hub case meets the
same (TL_perp) as the single hub.

Without any square the same pairing still gives a small-ball bound, for every remainder.

**Proposition 6.2.** Let X_H, M, s_1, s_2, L be as in Theorem 6.1, B any real symmetric 2 x 2 matrix, beta in R^2, and
R(X') any real quadratic polynomial in the light coordinates. Then Q = X_H^T B X_H + 2 <X_H, L + beta> + R(X') satisfies, for
every s and every delta > 0, with C_0 = pi (2/(s_1 s_2))^{1/2},

  P(|Q - s| <= delta) <= 2^{3/2} (s_1 s_2)^{-1/2} delta (2 + log_+(1/(C_0 delta))).

*Proof.* Here R does not enter the hub part, so P(|Q - s| <= delta) = int d^2t int G(t, y) mu_t(dy) with mu_t the slice at
L = t of the joint law of (L, R), and no freezing is needed. As in the proof of Theorem 6.1, int |g_t^(eta)|^2 d^2t <= pi^2/eta^2,
while now only |mu^_t(eta)| <= rho_L(t) <= 2/(s_1 s_2) is available, so int |mu^_t(eta)|^2 d^2t <= 2/(s_1 s_2) and the pairing at
frequency eta is at most min(1, C_0/|eta|). The frequency integral (2 pi)^{-1} int min(2 delta, 2/|eta|) min(1, C_0/|eta|) d eta is
at most (2 C_0/pi) delta (2 + log_+(1/(C_0 delta))). ∎

The logarithm is attained: the rank-two example of hub_pairs/, Theorem 1, has P(|Q| <= eps) >= c eps log(1/eps). So two
hubs with independent partners give a logarithm whatever the hub block and the remainder are, and a square transverse
to the partners removes it (Theorem 6.1). A hub pair whose remaining large eigenvalue lies along
the partners is not covered by Theorem 6.1 (a square along L is a constant on each slice; it only adds the phase
e^{i eta t^T C t} to g_t^, which Plancherel in t does not see), but it reduces to one hub. If the square is mu L_1^2 in
coordinates where <X_H, L> = X_{h_1} L_1 + X_{h_2} L_2 with L_1, L_2 orthogonal, conditioning on X_{h_1} = x leaves the hub
X_{h_2} with partner L_2 + b_12 x, hub diagonal b_22 and the square mu L_1^2 transverse to its partner, the term 2 x L_1
being linear. When the remainder has no term L_1 <r, X'> with r outside span(L_1, L_2) (such a term is of the kind
V <r, X'> that (0.1) excludes), this is a form of the family (0.1) with a hub diagonal, whose bounds (Proposition 2.3,
degenerate_hub/) are uniform in x.

*Three hubs.* With three hubs the Plancherel step alone is integrable, and the remainder is not needed at all.

**Theorem 6.3.** Let X_H in R^k (k >= 3) and X' be independent, where X_H has a density f_H with int f_H^2 <= 1 (for instance
independent coordinates with densities at most 1), and let L = M X' in R^k have a density bounded by D. For every real
symmetric k x k matrix B, every beta in R^k and every measurable function R of X', the form

  Q = X_H^T B X_H + 2 <X_H, L + beta> + R(X')

satisfies |phi_Q(eta)| <= min(1, D^{1/2} (pi/|eta|)^{k/2}) and ||p_Q||_inf <= (k/(k - 2)) D^{1/k}. If X' has independent
coordinates with densities at most 1 and M has singular values s_1 >= ... >= s_k > 0, then D <= 2^{k/2}/(s_1 ... s_k); for
three hubs ||p_Q||_inf <= 3 sqrt 2 (s_1 s_2 s_3)^{-1/3}.

*Proof.* Given X', E[e^{i eta Q} | X'] = e^{i eta R(X')} h_eta(L), where h_eta(l) = int f_H(x) e^{i eta (x^T B x + 2 <x, l + beta>)} dx.
As a function of l, h_eta(l) is the Fourier transform of x -> f_H(x) e^{i eta x^T B x} at -2 eta (l + beta), so Plancherel in R^k
gives int |h_eta(l)|^2 d^k l = (2|eta|)^{-k} (2 pi)^k int f_H^2 <= (pi/|eta|)^k for every B. Hence, by Cauchy-Schwarz,

  |phi_Q(eta)| <= E |h_eta(L)| = int rho_L |h_eta| <= (int rho_L^2)^{1/2} (pi/|eta|)^{k/2} <= D^{1/2} (pi/|eta|)^{k/2}.

For k >= 3 this is integrable, so p_Q is continuous, and with K = D^{1/2} pi^{k/2} the switch point of the minimum is
K^{2/k} = pi D^{1/k}, which gives (2 pi)^{-1} int min(1, K |eta|^{-k/2}) d eta = (k/(pi (k - 2))) K^{2/k} = (k/(k - 2)) D^{1/k}. With
M = U Sigma V^T, V^T X' is an orthonormal k-dimensional projection, whose density is at most 2^{k/2}, and L = U Sigma V^T X'. ∎

For k = 2 the same inequality gives |phi_Q(eta)| <= D^{1/2} pi/|eta|, which is Proposition 6.2 in one line, and for k = 1
it gives |eta|^{-1/2}; one or two hubs need the remainder, three do not. Applied to X^T A X + b^T X + c with H any three
coordinates, M = A_{H, H^c} and R the rest, Theorem 6.3 gives ||p_Q||_inf <= 3 sqrt 2 (s_1 s_2 s_3)^{-1/3}, where s_j are the
singular values of the 3 x (n - 3) off-diagonal block A_{H, H^c}, with no hypothesis on the eigenvalues, the diagonal or
the rest of A. So the conjecture can fail only for matrices in which every such block has a small product s_1 s_2 s_3:
three heavy rows whose partners, restricted to the complement of the three, are well conditioned are always
bounded. This settles the well-conditioned part of the many-hub case M-MH of architecture/PROOF_TREE.md, and it
settles peeling as soon as the remainder of one hub carries two sub-hubs of size bounded below with partners
independent of the first. What is left is at most two effective hub directions.

*Two hubs.* For two hubs the pairing in the proof of Theorem 6.1 is |eta|^{-1} times the L^2 norm of the slice transforms,
and any polynomial profile of the slices on intervals makes the frequency integral converge.

**Theorem 6.4.** Let X_H in R^2 and X' be independent, f_H <= 1, and L = M X' in R^2 with a density. Let (Y_l)_{l in R^2} be
measurable functions of X' with Y_{l'} -> Y_l pointwise as l' -> l (for instance Y_l = R_0(X') + 2 l_1 <q_1, X'> + 2 l_2 <q_2, X'>),
and let mu_{l_0, l} be the slice at L = l of the joint law of (L, Y_{l_0}). Suppose that for some 0 < b <= 1 and K

  mu_{l_0, l}(I) <= K |I|^b     for every l_0, almost every l and every interval I.

Then for every real symmetric 2 x 2 matrix B and beta in R^2, Q = X_H^T B X_H + 2 <X_H, L + beta> + Y_L(X') satisfies
||p_Q||_inf <= 1/pi + (10 K)^{1/2}/(1 - 2^{-b/2}).

*Proof.* By weak limits the laws may be taken compactly supported. Cut R^2 into square cells C_k of side h with points l_k
in C_k and put h_eta(l) = E e^{i eta (X_H^T B X_H + 2 <X_H, l + beta>)}. Since h_eta is continuous and Y_{l_k} -> Y_L on {L in C_k},
dominated convergence gives phi_Q(eta) = lim_{h -> 0} S_h(eta), S_h(eta) = sum_k int_{C_k} h_eta(l_k) mu^_{l_k, l}(eta) d^2 l. By
Cauchy-Schwarz |S_h(eta)| <= P_h(eta) = (sum_k |C_k| |h_eta(l_k)|^2)^{1/2} nu^_h(eta)^{1/2}, where
nu_h = sum_k int_{C_k} mu_{l_k, l} * mu~_{l_k, l} d^2 l (mu~ the reflection of mu) is a finite positive measure with
nu^_h = sum_k int_{C_k} |mu^_{l_k, l}|^2 d^2 l >= 0 and, by the hypothesis, nu_h([-r, r]) <= int rho_L(l) K (2r)^b d^2 l = K (2r)^b.

For a finite positive measure nu with nonnegative transform and nu([-r, r]) <= K' r^b for all r > 0, the Fejer kernel gives
int_{-Lambda}^{Lambda} nu^ <= 2 int nu^(eta) (1 - |eta|/(2 Lambda))_+ d eta = 4 Lambda int sinc^2(Lambda x) d nu(x), and splitting
|x| into [0, 1/Lambda] and the dyadic shells (2^j/Lambda, 2^{j+1}/Lambda] with sinc^2(u) <= min(1, u^{-2}) bounds the last integral by
K' Lambda^{-b} (1 + 2^b/(1 - 2^{b-2})) <= 5 K' Lambda^{-b}. So int_{|eta| <= Lambda} nu^_h <= 20 K' Lambda^{1-b} with K' = 2^b K.

Let Omega_A = {A <= |eta| <= 2A}. By Fatou's lemma and Cauchy-Schwarz in eta,

  int_{Omega_A} |phi_Q| <= liminf_{h -> 0} (sum_k |C_k| int_{Omega_A} |h_eta(l_k)|^2 d eta)^{1/2} (int_{Omega_A} nu^_h)^{1/2}.

Only the finitely many cells meeting the support of L count, and l -> int_{Omega_A} |h_eta(l)|^2 d eta is continuous, so the
first factor tends to at most (int_{Omega_A} int |h_eta(l)|^2 d^2 l d eta)^{1/2} <= (int_{Omega_A} pi^2 eta^{-2} d eta)^{1/2} = pi A^{-1/2}
(Plancherel in l, as in the proof of Theorem 6.1, for every B). The second is at most (20 K' (2A)^{1-b})^{1/2}. Hence
int_{Omega_A} |phi_Q| <= pi (40 K)^{1/2} A^{-b/2}, and summing over A = 2^j, j >= 0, and adding int_{|eta| < 1} |phi_Q| <= 2,
||phi_Q||_1 <= 2 + pi (40 K)^{1/2}/(1 - 2^{-b/2}). So p_Q is continuous and ||p_Q||_inf <= ||phi_Q||_1/(2 pi). ∎

Theorem 6.4 needs of the remainder only a power of |I| on intervals, where the single hub needs a profile on every Borel
set (Lemma 3.1) and still loses a double logarithm. The transform bound in the proof of Theorem 6.1, with the kernel of
Lemma 1.1, gives mu(I) <= 4 pi^2 (s_1 s_2)^{-1} (|I|/|lambda|)^{1/2}, so Theorem 6.4 contains Theorem 6.1 with b = 1/2, up to the
constant. For a remainder lambda V^2 plus a twist T on the coordinates orthogonal to (e_1, e_2, v), Fresnel in V bounds the
slice transform at frequency eta by (2 pi)^{-2} (4 pi |eta lambda|)^{-1/2} J_T(eta), where J_T(eta) is the three-dimensional frame
integral with the twist eta T. A growth bound J_T(eta) <= C (1 + |eta|)^{1/2 - b} for some b > 0 therefore bounds the hub pair
with such a twist. This is weaker than (TL_perp), which asks for J_T bounded, and for |eta| ||T|| >= 1 the twist itself
supplies decay (Fresnel in its large eigen-directions, or Theorem D when it is spread), so what the hub pair needs is a
growth bound for weak twists only.

*Decoupling the slices.* The pairing needs the slices only through nu^(eta) = int |mu^_t(eta)|^2 d^2t, an average over t, and
that average can be decoupled like a characteristic function. Splitting the light coordinates into two halves cancels the
remainder inside one half and turns what is inside the other into a phase, so a twist of any size costs nothing; what
remains is the block of the remainder that crosses the split.

**Theorem 6.5.** Let X_H in R^2 and X' be independent, f_H <= 1, X' with independent coordinates of densities at most 1,
L = M X' in R^2, and let R(X') = X'^T A_R X' + b^T X' + c be any real quadratic polynomial. Split the light coordinates as
I and J, let M_J be the columns of M in J, with singular values s_1' >= s_2' > 0, let Pi be the orthogonal projection of R^J
onto the row space of M_J, and let C = (A_R)_{I,J} (Id - Pi), with rows c_i (i in I). If F = ||C||_F > 0 and |c_i|^2 <= F^2/2
for every i, then for every real symmetric 2 x 2 matrix B and beta in R^2, Q = X_H^T B X_H + 2 <X_H, L + beta> + R(X') satisfies

  |phi_Q(eta)| <= pi^{3/2} 2^{5/4} (s_1' s_2' F)^{-1/2} |eta|^{-3/2},     ||p_Q||_inf <= 5.35 (s_1' s_2' F)^{-1/3}.

*Proof.* As in the proof of Theorem 6.3, phi_Q(eta) = E[h_eta(L) e^{i eta R}] = int h_eta(l) mu^_l(eta) d^2 l, where mu^_l(eta) is the
density at l of the complex measure A -> E[e^{i eta R}; L in A], and int |h_eta|^2 <= pi^2/eta^2 for every B. By Cauchy-Schwarz
|phi_Q(eta)| <= (pi/|eta|) nu^(eta)^{1/2} with nu^(eta) = int |mu^_l(eta)|^2 d^2 l.

Let k_h be the normalized indicator of the disc of radius h and m_h(l) = E[e^{i eta R} k_h(l - L)], so that int |m_h|^2 -> nu^(eta).
Write X' = (X_I, X_J). For fixed l, m_h(l) = E_{X_I} g(X_I, l) with g(x, l) = E_{X_J}[e^{i eta R(x, X_J)} k_h(l - L(x, X_J))], and
|m_h(l)|^2 <= E_{X_I} |g(X_I, l)|^2. With an independent copy X_J' of X_J and D_J = X_J - X_J', integrating in l gives

  int |m_h|^2 <= E[e^{i eta (R(X_I, X_J) - R(X_I, X_J'))} kappa_h(M_J D_J)],   kappa_h = k_h * k_h,

since L(X_I, X_J) - L(X_I, X_J') = M_J D_J. In the difference of the two values of R every term without X_J cancels, the terms
in X_J alone give a function of (X_J, X_J'), and the cross terms give 2 <X_I, (A_R)_{I,J} D_J>. Averaging over X_I first,
E e^{2 i eta <X_I, (A_R)_{I,J} D_J>} = prod_{i in I} psi_i(2 eta <a_i, D_J>), with a_i the rows of (A_R)_{I,J} and psi_i the Fourier
transform of f_i. Hence int |m_h|^2 <= E[kappa_h(M_J D_J) prod_{i in I} |psi_i(2 eta <a_i, D_J>)|].

Put theta_i = |c_i|^2/F^2 <= 1/2 and p_i = 1/theta_i >= 2 (a factor with c_i = 0 is bounded by 1). Hoelder for the finite measure
kappa_h(M_J D_J) dP bounds the last expectation by prod_i (E[kappa_h(M_J D_J) |psi_i(2 eta <a_i, D_J>)|^{p_i}])^{theta_i}. Here
<a_i, D_J> = <c_i, D_J> + lambda_i . M_J D_J for some lambda_i in R^2, the coordinates of D_J are independent with densities
f_j * f_j~ <= 1 (f~(x) = f(-x)), and (M_J D_J, <c_i, D_J>) has a density bounded by 2^{3/2}/(s_1' s_2' |c_i|) (the
three-dimensional marginal bound; c_i is orthogonal to the rows of M_J, so the Gram determinant is (s_1' s_2' |c_i|)^2).
Substituting u + lambda_i . x for the last coordinate at each value x of M_J D_J,

  E[kappa_h(M_J D_J) |psi_i(2 eta <a_i, D_J>)|^{p_i}] <= (2^{3/2}/(s_1' s_2' |c_i|)) (2|eta|)^{-1} int |psi_i|^{p_i}
                                                   <= (2^{3/2}/(s_1' s_2' |c_i|)) (2|eta|)^{-1} 4 pi theta_i^{1/2},

by int |psi|^p <= 4 pi/sqrt p (Lemma 1 of the first record). Since |c_i| theta_i^{-1/2} = F for every i, the product is
2^{5/2} pi/(s_1' s_2' F |eta|), uniformly in h. So |phi_Q(eta)| <= (pi/|eta|) (2^{5/2} pi/(s_1' s_2' F |eta|))^{1/2}, which is the first
bound, and with |phi_Q| <= 1, ||p_Q||_inf <= (2 pi)^{-1} int min(1, K |eta|^{-3/2}) d eta = (3/pi) K^{2/3} = 3 2^{5/6} (s_1' s_2' F)^{-1/3}. ∎

No hypothesis is made on R beyond the split: squares along the partners, every twist on either half, any diagonal and any
linear terms are free. The weights theta_i make the bound depend only on the Frobenius norm of the crossing block, because
int |psi|^p decreases like p^{-1/2}. A transverse square lambda V^2 whose direction v meets both halves gives
C ~ lambda v_I (v_J^perp)^T, with F about |lambda| |v_I| |v_J^perp| and row shares v_i^2/|v_I|^2, and a twist may add to C in any
way that does not cancel it. For a split in which each coordinate goes to I with probability 1/2, every off-diagonal
pair is separated with probability 1/2, so E ||(A_R)_{I,J}||_F^2 = ||offdiag(A_R)||_F^2/4; with A_R = lambda v v^T + T + D,
T of zero diagonal and D diagonal, ||offdiag(A_R)||_F >= |lambda| (1 - sum_i v_i^4)^{1/2} - ||T||_F. So a crossing block can be
small for every split only if the off-diagonal part of the remainder nearly vanishes, which a large eigenvalue with a
spread eigenvector excludes; turning this into a statement with constants (the projection off the partners, the row
shares, and a twist comparable to lambda) is bookkeeping that is not done here. With that proviso, a hub pair inside a
matrix whose third large eigenvalue is not along the partners is bounded whatever twist the remainder carries, and when
that eigenvalue is along the partners the pair reduces to one hub (above). The twisted hub pair of the open list of
README.md is therefore settled for such remainders, and neither (TL_perp) nor its growth version is needed. The block that crosses the split plays the part of the partner of a third hub, which is why Theorem 6.5 has the
decay of Theorem 6.3. The rank-two example has C = 0: its remainder 2 L_1 L_2 lies along the partners.

The same argument with one hub gives |eta|^{-1} for every remainder.

**Proposition 6.6.** Let X_h and X' be independent, f_h <= 1, X' with independent coordinates of densities at most 1,
L = <w, X'>, and R any real quadratic polynomial in X'. For a split I, J with w_J != 0 let C = (A_R)_{I,J} (Id - Pi_{w_J})
with rows c_i, F = ||C||_F > 0 and |c_i|^2 <= F^2/2. Then for every a and beta, Q = a X_h^2 + 2 X_h (L + beta) + R(X') satisfies
|phi_Q(eta)| <= 2 pi (|w_J| F)^{-1/2} |eta|^{-1} and

  P(|Q - s| <= delta) <= pi^2 (|w_J| F)^{-1/2} delta (1 + log_+((|w_J| F)^{1/2}/(4 delta)))     for every s and delta > 0.

*Proof.* In the proof of Theorem 6.5, Plancherel in the one-dimensional partner gives int |h_eta|^2 <= pi/|eta| for every a, and
the marginal of (<w_J, D_J>, <c_i, D_J>) is bounded by 2/(|w_J| |c_i|); so nu^(eta) <= 4 pi/(|w_J| F |eta|) and
|phi_Q(eta)| <= (pi/|eta|)^{1/2} nu^(eta)^{1/2}. For the small ball take the kernel K of the proof of Lemma 1.1, with
K >= (8/pi^2) 1_{[-delta, delta]}, K^ supported in |eta| <= pi/(2 delta) and |K^| <= 4 delta:
P(|Q - s| <= delta) <= (pi^2/8) (2 pi)^{-1} 4 delta int_{|eta| <= pi/(2 delta)} min(1, K_1 |eta|^{-1}) d eta with K_1 = 2 pi (|w_J| F)^{-1/2}, and
the integral is at most 2 K_1 (1 + log_+(pi/(2 K_1 delta))). ∎

For one hub this is the first bound that allows a twist: the small-ball probability is of order delta log(1/delta) for every
remainder with a crossing block, where Theorem 3.10 gives delta log log(1/delta) without twists. With a hub diagonal and
a spread cross term it also improves Proposition 3.12.

**Corollary 6.7.** Under the hypotheses of Proposition 2.3 (any hub diagonal a), for every split as in Proposition 6.6,

  ||p_Q||_inf <= 2 (|w_J| F)^{-1/2} (3 + log_+(4 (|w_J| F)^{3/2}/(eps |lambda|))).

*Proof.* |phi_Q(eta)| <= min(1, K_1 |eta|^{-1}, B |eta|^{-3/2}) with K_1 = 2 pi (|w_J| F)^{-1/2} and B = 31.5 (eps |lambda|)^{-1/2}
(Proposition 2.3). Splitting the frequency integral at K_1 and at eta_0 = (B/K_1)^2 gives at most 2 K_1 (3 + log_+(B^2/K_1^3)),
and B^2/K_1^3 = 992 (|w_J| F)^{3/2}/(8 pi^3 eps |lambda|) <= 4 (|w_J| F)^{3/2}/(eps |lambda|). Divide by 2 pi. ∎

So the hub diagonal together with a small spread cross term costs log(1/eps); without the hub diagonal Corollary 3.11 has
log log(1/eps). Numerically (num/threehub_check65.py, num/check65_gauss.py, num/check66_gauss.py) the bounds hold with room:
for Gaussian coordinates, where nu^ is explicit, the ratio of nu^(eta) to the bound of the proofs is at most 0.0062 for two
hubs and 0.027 for one hub over several hundred random matrices, partners and frequencies.

When the crossing block has exact rank two the same decoupling gives |eta|^{-2} for the averaged slices, and one hub is then
bounded.

**Proposition 6.8.** In the setting of Proposition 6.6 suppose that the crossing block, projected off w_J, has rank two:
there are orthonormal e_1, e_2 in R^J orthogonal to w_J and gamma_i in R^2 with (A_R)_{i,J} = lambda_i w_J + gamma_{i1} e_1 + gamma_{i2} e_2
for every i in I. Let G = sum_i gamma_i gamma_i^T have eigenvalues sigma_1^2 >= sigma_2^2 > 0 and suppose gamma_i^T G^{-1} gamma_i <= 1/2 for
every i. Then for every a and beta, Q = a X_h^2 + 2 X_h (L + beta) + R(X') satisfies

  |phi_Q(eta)| <= 2^{7/4} pi^{3/2} (|w_J| sigma_1 sigma_2)^{-1/2} |eta|^{-3/2},     ||p_Q||_inf <= 6.73 (|w_J| sigma_1 sigma_2)^{-1/3}.

*Proof.* As in the proof of Theorem 6.5, nu^(eta) <= E[kappa_h(<w_J, D_J>) prod_{i in I} |psi_i(2 eta <a_i, D_J>)|], and on the value x
of <w_J, D_J> one has <a_i, D_J> = lambda_i x + <gamma_i, U> with U = (<e_1, D_J>, <e_2, D_J>). The density of (<w_J, D_J>, U) is at
most 2^{3/2}/|w_J|, so

  nu^(eta) <= (2^{3/2}/|w_J|) int kappa_h(x) [ int_{R^2} prod_i |psi_i(2 eta <gamma_i, U> + 2 eta lambda_i x)| d^2U ] dx.

The inner integral is a two-dimensional Brascamp-Lieb integral with shifts: after U = G^{-1/2} U' / (2|eta|) the data are
geometric with leverages gamma_i^T G^{-1} gamma_i <= 1/2, and Theorem F of the first record bounds it by
(4 pi)^2 (2|eta|)^{-2} (sigma_1 sigma_2)^{-1} for every value of the shifts. Hence nu^(eta) <= 2^{3/2} 4 pi^2/(|w_J| sigma_1 sigma_2 eta^2), and
|phi_Q(eta)| <= (pi/|eta|)^{1/2} nu^(eta)^{1/2} gives the first bound. The second is (3/pi) K^{2/3} with K the constant of the first. ∎

A twist inside I or inside J does not change the crossing block, so it is free here as in Theorem 6.5; only a twist
between the halves adds rank. Two transverse squares lambda_1 V_1^2 + lambda_2 V_2^2 give a rank-two crossing block with
sigma_1 sigma_2 of order |lambda_1 lambda_2| |v_{1,I}| |v_{2,I}|, so a single hub inside a matrix with four large eigenvalues
(the hub's pair and two transverse ones) is bounded. With three, the second direction of the crossing block is only
as large as the cross term: in (0.1) without twist the projected block is lambda v_I (v_J^perp)^T + w_I (q_J^perp)^T, of rank
two with sigma_2 of order eps, and Propositions 6.6 and 6.8 together give |phi_Q(eta)| <= min(C |eta|^{-1}, C' eps^{-1/2} |eta|^{-3/2}),
which is the logarithm of Corollary 6.7 again. The case the conjecture needs, one hub and one transverse square, is
exactly where the decoupled slices stop at |eta|^{-1}.

A hub that is spread over several coordinates behaves like a hub law of bounded variation, because its characteristic
function is integrable; then the pairing with the slices converges for every cross term, as in Proposition 3.13.

**Proposition 6.9 (a spread hub).** Let H be a set of hub coordinates, c in R^H with c_h^2 <= |c|^2/2 for every h, and
U = <c, X_H>. Let

  Q = 2 U (L + beta) + sum_{h in H} phi_h(X_h) + lambda V^2 + 2 L <q, X'> + sum_i phi_i(X_i),

with L, V, q and the phi_i as in (0.1) and phi_h(x) = d_h x^2 + b_h x + c'_h arbitrary. Then for all laws

  |phi_Q(eta)| <= 8 pi^{3/2} |c|^{-1} |lambda|^{-1/2} |eta|^{-3/2},     ||p_Q||_inf <= 12 (|c|^2 |lambda|)^{-1/3}.

*Proof.* Given X', the expectation over X_H of e^{i eta Q} is e^{i eta Y_L} H_eta(L + beta), where Y_L collects the terms
without X_H and H_eta(t) = prod_{h in H} psi_h^{(eta d_h)}(2 eta t c_h + eta b_h), with the modulated transforms of Lemma 1.1.
Hoelder with p_h = |c|^2/c_h^2 >= 2 and Lemma 1 of the first record give

  int |H_eta(t)| dt <= prod_h (|2 eta c_h|^{-1} 4 pi p_h^{-1/2})^{1/p_h} = 2 pi/(|eta| |c|),

since |c_h|^{-1} p_h^{-1/2} = 1/|c| and sum_h 1/p_h = 1. The factor H_eta(L + beta) is a function of L alone, so the
discretisation in the proof of Theorem 1 gives phi_Q(eta) as a limit of sums of integrals of H_eta(l + beta) against the
slice transforms mu^_{l_k, l}(eta), which Lemma 1.1 bounds by 2 (4 pi/|eta lambda|)^{1/2} for every cross term. Hence
|phi_Q(eta)| <= 2 (4 pi/|eta lambda|)^{1/2} 2 pi/(|eta| |c|), which is the first bound, and ||p_Q||_inf <= (3/pi) K^{2/3} with
K = 8 pi^{3/2} |c|^{-1} |lambda|^{-1/2} is the second. ∎

For |H| = 1 the hypothesis fails, and that is the single hub. In the matrix setting Proposition 6.9 is the case of
several heavy rows whose partners are exactly parallel, m_h = c_h w, with no coupling among the heavy coordinates beyond
the diagonal and no single row carrying more than half of the weight c: the configuration of many heavy rows with one
common partner direction (M-MH of architecture/PROOF_TREE.md) in its exact form. Off-diagonal terms among the heavy
coordinates, or partners that are only nearly parallel, bring back a dependence of the hub factor on X' beyond L, and are
not covered.
