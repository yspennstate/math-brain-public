# Rank three: the two-sheet side of a leaking hub

X_0, X_1, ..., X_m are independent with densities at most 1 and X' = (X_1, ..., X_m).

## 1. Where rank three stands

Let Q = X^T A X + b^T X + c with A of rank exactly three and nonzero eigenvalues lambda_1, lambda_2 >= 1 and
-mu <= -1 (signature (2, 1); the other signature is the reflection s -> -s). The level sets {Q = s} are one-sheet
hyperboloids for s above the critical value and two-sheet hyperboloids below it.

- One-sheet side: density at most pi sqrt 2 for every product law, every dimension and every linear term in the
  range of A (Theorem C of the first record, COUNTEREXAMPLE_SEARCH.md and RESULTS.md there; the same theorem is
  Theorem 3.12 of the manuscript in interactive/20260923T164118Z-full-proof-paper/). The level set is doubly ruled, the
  coarea measure is (1/2) d theta dt in the ruling parameters, and each ruling integral is a two-dimensional marginal of
  the product law, at most 2 (Ball; Livshyts-Paouris-Pivovarov).
- Both sides: bounded when every row of the eigenvector matrix has squared norm at most 1/2 (Fourier and the geometric
  Brascamp-Lieb inequality), and when some row has squared norm above 1/2 and its diagonal entry has modulus at least c
  (a pivot: at most 176 c^{-1/2}, low_rank_plus_diagonal/).
- What is left is a heavy row with a small diagonal. In its simplest form (zero diagonal, no cross term inside
  span(w, v), no linear term outside the range) it is the leaking hub
    Q = 2 X_0 L + lambda V^2 + 2 eps L P = 2 L (X_0 + eps P) + lambda V^2,   L = <w, X'>, V = <v, X'>, P = <p, X'>,
  w, v, p orthonormal, eps > 0. Its matrix has rank three with eigenvalues lambda and +-(1 + eps^2)^{1/2}, whatever eps
  is. For eps = 0 it is bounded on both sides for every hub law (degenerate_hub/).

So for homogeneous forms the conjecture is open already at rank exactly three, and there only on the two-sheet side
of a heavy row with a small diagonal, whose simplest form is this leaking hub with s lambda < 0 (case (O1) of
low_rank_plus_diagonal/); a linear term outside the range reopens the one-sheet side as well ((O1) and (O2) there).
On the two-sheet side the bounds of single_hub_core/ apply to the leaking hub:
C + (3/sqrt 2) log K when the rows (w_i, v_i, p_i) take K directions (Propositions 3.17 and 3.19), and
C + 7.7 log_+(2 B_eps^2), a double logarithm in 1/eps, uniformly in the dimension (Corollary 3.11).

In the conditioning of Propositions 3.14 and 3.16 the two-sheet side has one simplification. Given the light
coordinates other than i, the hub value is x* = alpha/(2t) + c_0 - sigma t/2 with t = L and alpha = s - lambda V_0^2,
where V_0 is the value of V at t = 0. For s lambda < 0 this gives |alpha| >= |s|, so the dilation integral is at most
3.5 log(1 + 2/|s|) + 0.5 log(1 + 2|sigma|) pointwise, with no small-ball estimate for alpha. The factor 1/|w_i| from
the conditional density of t is untouched, and it is the whole difficulty.

## 2. Line integrals do not control the two-sheet side

Theorem C uses two facts about the three-dimensional marginal of the product law: a bounded density, and bounded
integrals over every line. The remark in COUNTEREXAMPLE_SEARCH.md of the first record, that shells are not excluded by
bounds on line integrals, can be made exact: those two facts, with the same constants as for a product law, give no
bound at all on the two-sheet side.

**Proposition 1 (rings on a two-sheet hyperboloid).** For every K there is a probability density rho on R^3 with
rho <= 2 sqrt 2 and int_l rho <= C_0 for every line l, C_0 an absolute constant, such that
Z = (Z_1, Z_2, Z_3) ~ rho makes q(Z) = Z_1^2 + Z_2^2 - Z_3^2 have density at least 2.1 K on an interval around -1.

*Construction.* Write y = (z_1, z_2), r = |y| and h(r) = (1 + r^2)^{1/2}, so that {q = -1, z_3 > 0} is the graph
z_3 = h(r). Put R_k = 4^k, a = 1/4, w_k = c R_k^{-3} with c = 1/20, and

  B_k = {(y, z_3) : R_k <= r <= R_k + a, |z_3 - h(r)| <= w_k},   k = 1, ..., K.

Let rho = 2 sqrt 2 on the union of the B_k and spread the remaining mass uniformly over a ball of radius 1 centred at
(10^6, 0, 0), where q > 10^{11}; its density is below 1/4, so it adds at most 1/2 to any line integral and nothing to
the density of q near -1. The B_k are disjoint and their total mass is
2 sqrt 2 sum_k 2 w_k pi ((R_k + a)^2 - R_k^2) <= 0.031.

*The density of q.* By coarea over the upper sheet, p_q(s) = int rho(y, h_s(r)) dy/(2 h_s(r)) with h_s = (r^2 - s)^{1/2}
for s < 0. For |s + 1| <= c R_K^{-2} the graph of h_s runs inside every B_k over the annulus R_k <= r <= R_k + a, so

  p_q(s) >= 2 sqrt 2 pi sum_k (h(R_k + a) - h(R_k)) >= 2 sqrt 2 pi K (0.243) >= 2.1 K.

*Line integrals.* Let l(t) = (y_0 + t u, z_0 + t tau) with |u|^2 + tau^2 = 1 and g(t) = z_0 + t tau - H(y_0 + t u), where
H(y) = h(|y|). H is convex with |grad H| < 1 and Hessian at least H^{-3} I, so g is concave with
g'' <= -|u|^2 H(y(t))^{-3}, and l(t) lies in B_k only if |g(t)| <= w_k and R_k <= |y(t)| <= R_k + a.

(i) If |u| <= 1/2, then |g'| >= |tau| - |u| > 0.36, g is monotone and the line meets the union of the B_k in a set of
length at most 2 w_1/0.36 < 6 w_1.

(ii) If |u| > 1/2, then g'' <= -(4 H^3)^{-1}, and H <= 2^{1/2} r for r >= 1. The set {R_k <= |y(t)| <= R_k + a} is at
most two intervals (|y(t)|^2 is a convex quadratic), and on each the set {|g| <= w_k} has length at most
4 (w_k/kappa_k)^{1/2} with kappa_k = (4 (2^{1/2} (R_k + a))^3)^{-1}; this is at most 8 (11.3 c (1.07)^3)^{1/2} < 7 for
every k. So each band contributes a bounded length, and it remains to see that only boundedly many bands contribute
more than a summable amount. Let t* be the point where the concave g is largest; if g has no maximum, g' has one sign
and t* is the end of the line towards which g increases. Then |g'(t)| grows with |t - t*|. The set where l meets B_k
consists of at most four intervals (two radial intervals, each split at t*); on each, let t_k be its point nearest to
t*, so that |g'| >= |g'(t_k)| on the whole interval and its length is at most 2 w_k/|g'(t_k)|. If |y(t*)| >= 2 R_k + 2,
the segment between t_k and t* has a piece of length at least R_k on which R_k + a <= |y| <= 2 R_k + 2 <= 3 R_k (the
speed of |y(t)| is at most 1), so |g'(t_k)| >= R_k (4 (3 * 2^{1/2} R_k)^3)^{-1} >= (400 R_k^2)^{-1}, and each interval has
length at most 800 c/R_k. If |y(t*)| <= R_k/2, the piece of the segment on which |y| runs from R_k/2 to R_k gives the
same bound. At most two bands have R_k/2 < |y(t*)| < 2 R_k + 2, because consecutive radii differ by the factor 4, and
each of these meets l in length less than 7. Summing, and adding the ball,
int_l rho <= 2 sqrt 2 (6 w_1 + 2 * 7 + 4 * 800 c sum_k R_k^{-1}) + 1/2 < 200, an absolute constant. ∎

On the one-sheet side the same density is harmless: the one-sheet level sets {q = s}, s > 0, stay at distance at least
of order 1/r from the upper sheet, far outside the bands, and Theorem C's argument bounds p_q(s) by pi times the
largest line integral whatever rho is.

Numerically (num/ring_check.py, K = 4): the four bands contribute 2.159, 2.217, 2.221 and 2.221 to p_q(-1), total 8.82,
with total mass 0.031, and over 1,600 lines tangent to the sheet inside a band (random tangent directions, normal tilts
of order 10^{-3}) and 600 radial lines tangent to the hyperbola at radii from 1 to 512, the longest piece inside the
union of the bands is 0.367. So with rho <= 2 sqrt 2 the line integrals stay below 1.04, under the bound 2 that every
two-dimensional marginal of a product law satisfies, while the density of q at -1 is linear in K.

For a product law the three-dimensional marginal is a convolution of measures carried by lines, and whether such a
convolution can concentrate near a family of circles is invisible to every line integral. A proof for the two-sheet
side has to use that convolution structure: it is the same curved-section information that (CS), (VD) and (P2) of
single_hub_core/ ask for, now for a convex surface instead of a parabola.

## 3. With L fixed the cross term costs nothing

Section 2 concerns the three-dimensional marginal alone. For the hub form itself there is a bound in which the cross
term plays no role, whatever its size and direction, and in which everything lost is carried by the transform of the
hub law. For a density f_0 put f^_0(omega) = int f_0(x) e^{i omega x} dx and

  H(f_0) = int |f^_0(omega)| |omega|^{-1/2} d omega.

**Proposition 2.** Let X_0, X_1, ..., X_m be independent with densities at most 1, f_0 the density of X_0 and
X' = (X_1, ..., X_m). Let w, v be orthonormal in R^m with w_i^2 + v_i^2 <= 1/2, let z in R^m be arbitrary,
L = <w, X'>, V = <v, X'>, Z = <z, X'>, and

  Q = 2 (L + beta)(X_0 + Z) + lambda V^2 + sum_i (d_i X_i^2 + b_i X_i) + c,   lambda != 0.

Then for every s

  p_Q(s) <= 1/2 + 2 sqrt 2 (1 + log_+(2 H(f_0)/(pi |lambda|)^{1/2})).

This is (0.1) of single_hub_core/ with a = 0, cross term q = z, any light diagonal and any linear terms; the leaking
hub is z = eps p.

*Proof.* The constant c only moves s, so take c = 0. Condition on L = l and put t = l + beta. Given X', Q is affine in X_0 with slope 2t, so the conditional
density of Q given L = l is at most 1/(2|t|). Since rho_L <= sqrt 2, the range |t| >= 1 contributes at most 1/2 to
p_Q(s), and for |t| < 1 the contribution rho_L(l) p_{Q|L=l}(s) is at most sqrt 2/(2|t|). For a second bound fix t_0,
let R = 2 t_0 Z + lambda V^2 + sum_i (d_i X_i^2 + b_i X_i) and psi_i(theta) = E exp(i theta X_i + i tau (d_i X_i^2 + b_i X_i)).
As X_0 is independent of X', E[e^{i tau Q} | L = l] = f^_0(2 tau t) E[e^{i tau R} | L = l] at t_0 = t. Fourier inversion
in l and the Fresnel identity e^{i a Y^2} = c_a int e^{-i xi^2/(4a) + i xi Y} d xi with |c_a| = (4 pi |a|)^{-1/2}
(multiscale_fourier/, Section 1), applied with a = tau lambda, give

  rho_L(l) E[e^{i tau R} | L = l]
    = (2 pi)^{-1} c_{tau lambda} int int e^{-i zeta l - i xi^2/(4 tau lambda)} prod_i psi_i(zeta w_i + xi v_i + 2 tau t_0 z_i) d zeta d xi.

The two-dimensional Brascamp-Lieb bound used in degenerate_hub/, which holds for all shifts, together with
int |psi_i|^p <= 4 pi/sqrt p for p >= 2, bounds the double integral of the moduli by (4 pi)^2 whatever the shifts
2 tau t_0 z_i are. Hence |rho_L(l) E[e^{i tau Q} | L = l]| <= 4 sqrt pi |tau lambda|^{-1/2} |f^_0(2 tau t)|, and inverting in
tau and substituting omega = 2 tau t,

  rho_L(l) p_{Q|L=l}(s) <= (2/sqrt pi) |lambda|^{-1/2} (2|t|)^{-1/2} H(f_0).

With K = 2 H(f_0)/(pi |lambda|)^{1/2}, the integral over |t| < 1 of min(sqrt 2/(2|t|), K (2|t|)^{-1/2}) is
2 sqrt 2 (1 + log_+ K), the minimum switching at |t| = K^{-2}. ∎

The cross term enters only through the shifts 2 tau t z_i, which the Brascamp-Lieb bound does not see; once L is fixed,
its size and direction are irrelevant and the whole loss is in H(f_0).

*The size of H.* Here |f^_0| <= 1 and int |f^_0|^2 = 2 pi int f_0^2 <= 2 pi. With b_j the part of int |f^_0|^2 on
2^j < |omega| <= 2^{j+1}, Cauchy-Schwarz on each dyadic band gives

  H(f_0) <= 4 + (2 log 2)^{1/2} sum_{j >= 0} b_j^{1/2}.

So H(f_0) <= 4 + 4 TV(f_0) for a hub law of bounded variation, and 4 + 8n for a union of n intervals, which recovers
Proposition 3.18(b), (c) of single_hub_core/ with a larger logarithmic constant. H(f_0) <= 4 + (2 pi/sigma)^{1/2} ||f_0||_{H^sigma},
with ||f||_{H^sigma}^2 = (2 pi)^{-1} int |omega|^{2 sigma} |f^|^2, for every positive fractional smoothness sigma, and
H(f_0) <= 4 + (4 pi log 2 (1 + J))^{1/2} when f^_0 vanishes outside |omega| <= 2^J, as for g * F with F a Fejer kernel of
width 2^{-J}. In the last case the density is at most C + sqrt 2 log J, a double logarithm of the finest scale of the
hub law; Proposition 3.18 goes through the total variation, which for such a law can be of order 2^J, and so gives a
single logarithm of it. A law whose mass is split evenly among random unions of intervals at the scales
2^{-1}, ..., 2^{-J} has b_j of order 1/J on about J bands (a second-moment computation for the random sums), so
H(f_0) of order J^{1/2}; the bound does not settle the case.

*The size of the cross term in the same computation.* Let z = eps p with (w, v, p) orthonormal and
w_i^2 + v_i^2 + p_i^2 <= 1/2, and drop the light diagonal and linear terms, so that Q = 2 (L + beta)(X_0 + eps P) + lambda V^2.
The double integral is then (4 pi)^2 B(omega) at omega = 2 tau t, where

  B(omega) = (4 pi)^{-2} int int prod_i |f^_i(zeta w_i + xi v_i + eps omega p_i)| d zeta d xi <= 1,   int B(omega) d omega <= 4 pi/eps,

the last by the three-dimensional Brascamp-Lieb bound. Keeping B in the proof replaces H(f_0) by
H_eps = int |f^_0| |omega|^{-1/2} B d omega, which is at most H(f_0) and, splitting at |omega| = 1 and |omega| = 1/eps, at most
4 + 2 (pi log(1/eps))^{1/2} + 2 sqrt 2 pi for eps < 1. So

  p_Q(s) <= 1/2 + 2 sqrt 2 (1 + log_+((2/(pi |lambda|)^{1/2}) min(H(f_0), 12.9 + 2 (pi log(1/eps))^{1/2}))).

The second entry of the minimum is the double logarithm in 1/eps of Proposition 3.9 and Corollary 3.11 of
single_hub_core/; the first is uniform in eps. For the leaking hub to reach density M, both log(1/eps) and the number
of dyadic scales that carry the hub law have to exceed a constant times exp(M/sqrt 2).

What is lost is the modulus of f^_0 on 1 <= |omega| <= 1/eps, where B need not be small. At those frequencies a leak with P of
order one moves x* by less than a wavelength of the hub law, and the same computation at eps = 0 loses the same logarithm,
although that case is bounded for every hub law (degenerate_hub/), by an argument that keeps the hub law in physical
space and bounds the density of 2xL + lambda V^2 for each hub value x. For eps > 0 that argument meets the twist
2 eps L P inside the density of 2L(x + eps P) + lambda V^2, and Fourier bounds with moduli of the twisted form lose a
power of eps (Proposition 2.3 of single_hub_core/) and are not bounded for laws with many narrow bumps
(twist_obstruction/). What is missing is an estimate that keeps the hub law in physical space below frequency 1/eps and
uses its transform only above it. For a leak of bounded range there is one.

**Proposition 3 (a leak of bounded range).** Let Q = 2 (L + beta)(X_0 + eps P) + lambda V^2 with (w, v, p) orthonormal,
w_i^2 + v_i^2 + p_i^2 <= 1/2 and eps > 0, and suppose that |P - a| <= R almost surely for some a and some R >= 1. Then
for every s and every hub law

  p_Q(s) <= 1/2 + (640 sqrt 2/pi) |lambda|^{-1/2} + 2 sqrt 2 (1 + log_+(2 sqrt 2 |lambda|^{-1/2} (1 + (2 log R + 4 pi)^{1/2}))),

which grows like sqrt 2 log log R, uniformly in eps and in the hub law.

*Proof.* Translating the hub law by eps a, take a = 0. Let F_sigma(v) = (2 sigma/pi) sin^2(v/(2 sigma))/v^2 be the Fejer
kernel, whose transform is (1 - sigma |omega|)_+, and put sigma = eps R, S = f_0 * F_sigma and G = f_0 - S. Then 0 <= S <= 1,
|G| <= 1 and G^(omega) = f^_0(omega) min(1, sigma |omega|).

The part of G. The proof of Proposition 2 with B kept in it applies to a signed hub function bounded by 1, since the
first bound there uses only |G| <= 1; it gives |E[G(x*)/(2|L + beta|)]| <= 1/2 + 2 sqrt 2 (1 + log_+ K) with
K = (2/sqrt pi) |lambda|^{-1/2} int |G^| |omega|^{-1/2} B d omega. Write B(omega) = b(eps omega), where b <= 1 and int b <= 4 pi.
Below |omega| = 1/sigma, int |f^_0| sigma |omega|^{1/2} d omega <= sigma (2 pi)^{1/2} (int_{|omega| <= 1/sigma} |omega| d omega)^{1/2} = (2 pi)^{1/2};
above it, Cauchy-Schwarz and u = eps omega give at most (2 pi)^{1/2} (int_{|u| > 1/R} b(u)^2 du/|u|)^{1/2} <= (2 pi)^{1/2} (2 log R + 4 pi)^{1/2}.
So K <= 2 sqrt 2 |lambda|^{-1/2} (1 + (2 log R + 4 pi)^{1/2}).

The part of S. For |h| <= sigma, F_sigma(v - h) <= (32/pi) F~_sigma(v) with F~_sigma(v) = (1/4) min(1/sigma, sigma/v^2), a
probability density (numerically the best constant is 4.56 in place of 32/pi). As |eps P| <= sigma,

  S(x*) = S(x*_0 - eps P) <= (32/pi) (f_0 * F~_sigma)(x*_0),   x*_0 = (s - lambda V^2)/(2(L + beta)),

and f_0 * F~_sigma is a hub density at most 1. So E[S(x*)/(2|L + beta|)] is at most 32/pi times the density at s of the
degenerate hub 2 (L + beta) Y + lambda V^2, Y ~ f_0 * F~_sigma independent. Given Y = x that density is at most
4 sqrt 2 |lambda x|^{-1/2}, by the bound 8 |c|^{-1/2} for U + c V^2 (OPEN_CORE.md), so it is at most
4 sqrt 2 |lambda|^{-1/2} (1 + int_{|x| <= 1} |x|^{-1/2} dx) = 20 sqrt 2 |lambda|^{-1/2} for every hub law. ∎

In the smoothed part the leak is a shift by at most sigma, which a kernel of width sigma absorbs, so there the hub law
stays in physical space and meets only the degenerate hub; the Fourier side sees only frequencies above 1/sigma, where
the cost is a logarithm of sigma/eps = R. For light laws supported in intervals of lengths K_i one may take
R = max(1, (1/2) sum_i |p_i| K_i), so the leaking hub is then at most C + sqrt 2 log log(e + |p|_1 max_i K_i), uniformly in eps
and in the hub law, with |p|_1 <= m^{1/2}; Proposition 3.7 of single_hub_core/ gives (log K)^{1/2} for such laws,
uniformly in the dimension, so the gain here is the mechanism and the uniformity in eps and the hub law.

For bounded light laws the range of P costs only log log K: its tails can be tilted away, and the tilting can be
repeated.

**Proposition 4 (bounded light laws).** In the setting of Proposition 3 with |lambda| >= 1, suppose that every X_i,
i >= 1, is supported in an interval of length at most K, K >= 3. Then, uniformly in eps, in the hub law and in m,

  p_Q(s) <= C + sqrt 2 log log K,

with C an absolute constant. Proposition 3.7 of single_hub_core/ gives (log K)^{1/2} for such laws.

*Proof.* Two properties of Proposition 3 are used.

(a) It carries a weight. Let 0 <= phi <= 1 be smooth and Y = sum_{i in S} p_i X_i for a set S of light coordinates. The
density of Q at s under the measure phi(Y) dPr obeys the bound of Proposition 3 with R the range of the leak on the
support of phi(Y), and with log kappa, kappa = (2 pi)^{-1} int |phi^|, added to the logarithm. The smoothed part uses
only that the weight is at most 1. In the Fourier part, phi(Y) = (2 pi)^{-1} int phi^(eta) e^{i eta Y} d eta shifts the
arguments of the light transforms by eta p_i, i in S, which neither Brascamp-Lieb bound sees, so B is replaced by an
average of shifted copies with the same two properties, B <= 1 and int B <= 4 pi/eps.

(b) If the light densities are at most c >= 1 instead of 1, then X_i = Y_i/c gives Q = Q'/c, where Q' has the same form
with lambda/c, eps/c and c beta in place of lambda, eps and beta and the same leak eps P. So p_Q(s) is at most c times the
bound of Proposition 3 with lambda/c in place of lambda and cR in place of R. For |lambda| >= 1 and a fixed cutoff phi
the weighted bound of (a) is then at most

  a(c, R) = C_1 c^{3/2} + 2 sqrt 2 c log(1 + (2 log(c R) + 4 pi)^{1/2}),   R >= 1.

For u >= 1 put delta = (log 2)/(4 u^{1/2}), theta = 4 u^{1/2}/K and r = K u^{1/2}, and let phi be a smooth cutoff, 1 on
[-1, 1] and 0 outside [-2, 2]. Take a law of the kind in the statement with light densities at most c, let
B = {i : |p_i| > delta}, S the other light coordinates and P_S = sum_{i in S} p_i X_i. Since |B| <= delta^{-2}, the part of P
on B lies within K |p_B|_1/2 <= K/(2 delta) of the centre of its range, so on the support of phi((P_S - E P_S)/r) the leak
lies within eps (K/(2 delta) + 2r) <= 5 eps K u^{1/2} of a fixed point, and there the density is at most a(c, 5 K u^{1/2}).
On the rest |P_S - E P_S| > r, and

  1 - phi((P_S - E P_S)/r) <= e^{theta (P_S - E P_S) - 4u} + e^{-theta (P_S - E P_S) - 4u}.

Since the integrand of the density is nonnegative, each term contributes at most e^{-4u} E e^{±theta (P_S - E P_S)} times
the density of Q at s under the law in which each X_i, i in S, is tilted by e^{±theta p_i x}. Hoeffding's lemma bounds
the expectation by e^{theta^2 K^2/8} = e^{2u}. As theta delta K = log 2, each tilted density is at most twice the one it
tilts, and the tilted law is again of the kind in the statement, with the same supports and light densities at most 2c.

Let D(c) be the supremum of p_Q(s) over the laws of the kind in the statement with light densities at most c, the frame,
eps, beta, lambda and s held fixed. Then

  D(c) <= a(c, 5 K u^{1/2}) + 2 e^{-2u} D(2c)   for every u >= 1,

and D(c) <= a(c, K m^{1/2}/2) is finite, by (b) applied to the whole range |P - a| <= K m^{1/2}/2. Take u_j = j + u_0 with
u_0 = 1 + log(1 + log(1 + log K)) and use the inequality at c = 2^j, j = 0, ..., J - 1:

  D(1) <= sum_{j < J} 2^j e^{-2 j u_0 - j(j-1)} a(2^j, 5 K u_j^{1/2}) + 2^J e^{-2 J u_0 - J(J-1)} D(2^J).

The last term tends to 0 as J -> infinity, since D(2^J) grows only like 2^{3J/2} log(J + log(K m)). The term j = 0 is at
most C + sqrt 2 log log K. For j >= 1, a(2^j, 5 K u_j^{1/2}) <= C 2^{3j/2} (1 + j)(1 + log(1 + log K)) and
2^j e^{-2 j u_0 - j(j-1)} <= e^{-2 u_0} 2^j e^{-2(j-1) - j(j-1)}, so these terms sum to at most
C e^{-2 u_0} (1 + log(1 + log K)) <= C. ∎

A density M on bounded light laws therefore needs K >= exp(exp((M - C)/sqrt 2)), in every dimension. Each tilt doubles
the density cap and costs a factor 2 e^{-2u}, and the recursion closes because the cap enters Proposition 3 only
polynomially. The tilting uses the bounded supports twice, for Hoeffding's lemma and for the cap on the tilted
densities; for unbounded laws a large |P| is a tail event that neither step controls.

Averaging over either free parameter of the leaking hub gives a bound for all laws at once.

**Proposition 5 (averages over the shift and over the leak).** Let Q_{beta, eps} = 2 (L + beta)(X_0 + eps P) + lambda V^2
with w, v orthonormal, w_i^2 + v_i^2 <= 1/2, P any linear form and lambda != 0, and write p_{beta, eps}(s) for its density.
For every hub law, all light laws and every s:

(a) for every probability density phi on R and every eps >= 0,

  int p_{beta, eps}(s) phi(beta) d beta <= 1/2 + ||phi||_inf (2 + log(1 + 2 pi^4/|lambda|));

in particular int_I p_{beta, eps}(s) d beta <= |I|/2 + 2 + log(1 + 2 pi^4/|lambda|) for every interval I, and for |lambda| >= 1
the set of beta in I where p_{beta, eps}(s) > M has measure at most (|I|/2 + 7.28)/M;

(b) for every beta and every eps_0 > 0,

  eps_0^{-1} int_{eps_0}^{2 eps_0} p_{beta, eps}(s) d eps <= 4 E[Mf_0(x*_0)/(2|L + beta|)] <= 128 sqrt 2 |lambda|^{-1/2},

with Mf_0 the Hardy-Littlewood maximal function of the hub law and x*_0 = (s - lambda V^2)/(2(L + beta)).

*Proof.* (a) Let B have density phi and be independent of X_0 and X'. The left side is the density at s of
2 t (X_0 + eps P) + lambda V^2 with t = L + B. Given X', t has density phi(t - L) <= ||phi||_inf, and the hub value is
x* = alpha/(2t) + c_0 with alpha = s - lambda V^2 and c_0 = -eps P, both functions of X'. This is the situation of
Proposition 3.14 of single_hub_core/ with kappa = 0, the variable B in the place of the partner-only block and
||phi||_inf in the place of sqrt 2/omega, and its proof gives the bound.
(b) Fix the light coordinates, with P != 0. As eps runs over [eps_0, 2 eps_0] the hub value x*_0 - eps P runs over an
interval of length eps_0 |P| inside the interval of length 4 eps_0 |P| centred at x*_0, so the average of f_0 over it is at
most 4 Mf_0(x*_0). Averaging p_{beta, eps}(s) = E[f_0(x*_0 - eps P)/(2|L + beta|)] over eps therefore gives the first
inequality, and the second is the bound for E[Mf_0(x*_0)/(2|L + beta|)] in the paragraph after this proof (the density of
2x(L + beta) + lambda V^2 at s is at most 4 sqrt 2 |lambda x|^{-1/2}, and the decreasing rearrangement of Mf_0 is at most
min(1, 2/t)). ∎

So both parameters can be averaged away: a leaking hub of density M exists, if at all, only for beta in a set of
measure at most about 7.3/M in every unit interval, and only for eps in a set of relative measure at most about 181/M in
every window [eps_0, 2 eps_0], for every hub law and all light laws. The cross term has to move with the partner for
(a): a cross term 2 L <q, X'> that does not contain beta leaves, after averaging, the product -2 B <q, X'> of the new
variable with the light coordinates, which Proposition 3.14 does not allow.

With a smoothing scale that depends on the leak, sigma = eps max(1, |P - a|), taken on the dyadic levels of |P - a| by
a partition of unity in P, the smoothed parts of all levels together are at most (32/pi) E[Mf_0(x*_0)/(2|L + beta|)], Mf_0
the Hardy-Littlewood maximal function, since f_0 * F~_sigma <= Mf_0 for every sigma. That is bounded for every hub law:
the density of 2x(L + beta) + lambda V^2 at s is at most 4 sqrt 2 |lambda x|^{-1/2} for all x, the decreasing
rearrangement of Mf_0 is at most min(1, 2/t), and the rearrangement inequality gives 32 sqrt 2 |lambda|^{-1/2}. What this
leaves is the transform of the hub law on 1/(eps |P - a|) <= |omega| <= 1/eps where |P - a| > 1: hub frequencies at which
the leak moves x* by more than a wavelength while the light transform in the direction of p has not yet decayed. The
band is empty where |P - a| is of order one and small for light laws whose transform decays at the inverse of their
spread; it matters on the tails of P and for light laws that are both spread and rough, the comb laws of OPEN_CORE.md.

## 4. Numerics: the two sides of the leaking hub

num/sides.py and num/sides2.py estimate the largest density over hub laws of Q = 2L(X_0 + eps P) + lambda V^2 at
s = +sigma (one-sheet side) and s = -sigma (two-sheet side), for lambda = 1 and a random orthonormal frame (w, v, p) in
R^32. That largest density is the top unit mass of the law of x* = (s - lambda V^2)/(2L) - eps P weighted by 1/(2|L|),
read off a weighted histogram with bins of width 1/64 from 2 x 10^6 samples. The light laws are combs: each X_i is
uniform on 16 teeth of width 1/16 at 16 distinct integers in [0, 32). At each eps, sides2.py also runs a copy in which
P is shuffled across samples, which makes the leak independent of (L, V). Two frames (seeds 1 and 2, which also draw
the teeth):

  eps                               0.03     0.01     0.003    0.001    0
  frame 1, sigma 0.05, one-sheet    0.0243   0.0261   0.0261   0.0261   0.0261
  frame 1, sigma 0.05, two-sheet    0.0215   0.0228   0.0228   0.0228   0.0228
  frame 1, sigma 0.3,  one-sheet    0.0241   0.0255   0.0256   0.0256   0.0256
  frame 1, sigma 0.3,  two-sheet    0.0179   0.0188   0.0188   0.0188   0.0189
  frame 2, sigma 0.05, one-sheet    0.0224   0.0243   0.0244   0.0244   0.0244
  frame 2, sigma 0.05, two-sheet    0.0190   0.0203   0.0204   0.0204   0.0204
  frame 2, sigma 0.3,  one-sheet    0.0210   0.0227   0.0228   0.0228   0.0229
  frame 2, sigma 0.3,  two-sheet    0.0160   0.0170   0.0171   0.0171   0.0171

The values settle by eps = 0.01 and below it agree with eps = 0 to within one unit in the last digit. At eps = 0.03
the leak lowers them by 5 to 8 per cent, and the two-sheet value is below the one-sheet value in every row. The
shuffled leak differs from the true one by at most 0.0003 (num/sides2_seed1.out, num/sides2_seed2.out), so on these
frames a leak correlated with (L, V) does nothing that an independent one does not. For uniform light laws
(num/sides_seed0.out, eps = 0.3, 0.1, 0.03) the two-sheet side is again the smaller one: 1.57, 1.65, 1.68 against
2.82, 2.84, 2.84 at sigma = 0.05, and 0.22 against 0.26 at sigma = 1. Random frames are not adversarial, and none of
these numbers bears on the configurations that Sections 2 and 3 single out.

num/bl_check.py checks the shifted two-dimensional Brascamp-Lieb bound behind Propositions 2 and 3 on random frames
with m = 6, 10, 16 light coordinates (leverages at most 1/2), uniform and comb laws and shifts of size 0, 5 and 100: the
integral is at most 70.3 against (4 pi)^2 = 157.9 (num/bl_check.out).

num/prop4_recursion.py evaluates the recursion in the proof of Proposition 4 with the constants of Proposition 3 at
|lambda| = 1. The bound is 300.2 at K = 3 and 308.9 at K = e^{6908}, the same for every m from 10 to 10^{300}; most of it
is the constant 640 sqrt 2/pi of the smoothed part (num/prop4_recursion.out).

## 5. The cone between the two sides

At s = 0 the level set of q = lambda_1 z_1^2 + lambda_2 z_2^2 - mu z_3^2 is a cone, ruled by lines through the origin. With
d_theta = (lambda_1^{-1/2} cos theta, lambda_2^{-1/2} sin theta, mu^{-1/2}), the map (r, theta) -> r d_theta covers it, and the coarea
measure is |d_theta x d_theta'| (2 |Lambda d_theta|)^{-1} dr d theta, which does not depend on r (it is (1/2) dr d theta when all three
eigenvalues have modulus 1). So p_q(0) is at most a constant depending on the eigenvalues times the largest line
integral, exactly as on the one-sheet side. At rho = (lambda_1 z_1^2 + lambda_2 z_2^2)^{1/2} the two-sheet level set at s < 0 lies
at distance |s| (sqrt mu ((rho^2 + |s|)^{1/2} + rho))^{-1}, about |s|/(2 sqrt mu rho), from the cone, and the one-sheet level set at
-s at the same distance on the other side. Line integrals cannot tell the three apart at scales above |s|/rho, so a
three-dimensional density that is bounded on the cone and on the one-sheet side and large on the two-sheet side has to
separate the two-sheet level set from the cone below that scale, at many values of rho. The rings of Proposition 1 do
so: at rho = R_k their thickness c R_k^{-3} is between 10^{-2} and 10^{-7} of the gap for R_k = 4, ..., 4^5. For a
product law this asks for structure at scale |s|/R in the part of the three-dimensional projection at distance R from
the origin, organised along the level set rather than along the rulings of the cone.

Every bound in this report and in single_hub_core/ that holds for all product laws pays at least a double logarithm in
one parameter: 1/eps (Corollary 3.11 there, Proposition 2), the finest scale of the hub law (Proposition 2), the range
of the leak (Propositions 3 and 4). A density M needs all of them extreme at once, log(1/eps) and the number of dyadic
scales of the hub law each above a constant times exp(M/sqrt 2). The statement that would remove the logarithms is (CS)
of single_hub_core/, a global nonlinear Brascamp-Lieb inequality for sections of a product density by quadrics
(OPEN_CORE.md, Related results); (P2) is its smallest case.
