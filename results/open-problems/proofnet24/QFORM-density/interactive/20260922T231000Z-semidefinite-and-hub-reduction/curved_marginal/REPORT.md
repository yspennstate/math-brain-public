# The curved marginal when the square is bounded

X_1, ..., X_m are independent with densities at most 1, X' = (X_1, ..., X_m), and u, v are orthonormal in R^m with
u_i^2 + v_i^2 <= 1/2. U = <u, X'>, V = <v, X'>. The curved marginal is

  (P2)   the density of U + c V^2 is at most an absolute constant, for every real c and all laws,

the simplest form of the curved-slicing statement (CS) of single_hub_core/ (OPEN_CORE.md). Proposition 5.1 there gives
8 |c|^{-1/2} for every frame and 4 (|v_i| + |v_j|)/|u_i v_j - u_j v_i| for every pair of coordinates. The first blows up
as c -> 0, the second as the frame spreads, and single_hub_core/ locates the open part in a parabola that bends only
where |V| is of order |c|^{-1/2}, far out in the laws. When V is bounded that part costs only the square root of its
range, uniformly in c and in the frame, and exponential tilting turns this into a bound for all laws of bounded support.

## 1. A bounded square

Write psi_i for the characteristic function of X_i and Psi(tau, xi) = E e^{i (tau U + xi V)} = prod_i psi_i(tau u_i + xi v_i).
Two facts about Psi are used, both from the first record.

(i) Along every line of the form xi = xi_0 + b tau, int |Psi(tau, xi_0 + b tau)| d tau <= 4 pi. The line is the
characteristic function of <u + b v, X'> with shifts xi_0 v_i in the coordinates; |u + b v| >= 1 and
(u_i + b v_i)^2 <= (u_i^2 + v_i^2)(1 + b^2) <= |u + b v|^2/2, so Hoelder with exponents p_i = |u + b v|^2/(u_i + b v_i)^2 >= 2
and int |psi|^p <= 4 pi/sqrt p give 4 pi/|u + b v|.

(ii) int int |Psi| <= (4 pi)^2 (Theorem F), with any shifts in the coordinates.

**Proposition 1.** Suppose that |V - v_0| <= R almost surely for some v_0 and some R >= 1. Then for every real c and
every s,

  p_{U + cV^2}(s) <= C_1 + C_2 R^{1/2},

with absolute constants C_1, C_2.

*Proof.* Take c != 0 (at c = 0 the marginal bound applies). Fix a smooth chi with 0 <= chi <= 1, chi = 1 on [-1, 1] and
chi = 0 outside [-2, 2], and put a = tau c and g_tau(w) = e^{i a w^2} chi(w/R). Since chi((V - v_0)/R) = 1 almost surely,

  E e^{i tau (U + cV^2)} = e^{-i a v_0^2} E[ e^{i tau (U + 2 c v_0 V)} g_tau(V - v_0) ]
                        = e^{-i a v_0^2} (2 pi)^{-1} int g^_tau(xi) e^{-i xi v_0} Psi(tau, xi + 2 c v_0 tau) d xi,

so |E e^{i tau (U + cV^2)}| <= (2 pi)^{-1} I(tau) with I(tau) = int |g^_tau(xi)| |Psi(tau, xi + 2 c v_0 tau)| d xi. Three bounds
on the transform of g_tau are used, with constants depending only on chi:

(g1) for |a| R^2 <= 1, g^_tau(xi) = R h^(R xi) with h(y) = e^{i a R^2 y^2} chi(y), and two integrations by parts give
|g^_tau(xi)| <= min(4R, A/(R xi^2)), so int sup_{|a| R^2 <= 1} |g^_tau(xi)| d xi <= 8 A^{1/2};

(g2) for every a, |g^_tau(xi)| <= B |a|^{-1/2} (van der Corput, the phase having second derivative 2a);

(g3) for |xi| >= 8 |a| R the phase a w^2 - xi w has derivative at least |xi|/2 on the support, and two integrations by
parts give int_{|xi| >= 8|a|R} |g^_tau(xi)| d xi <= D/(|a| R^2).

Let T_0 = 1/(|c| R^2). On |tau| <= T_0, (g1) and (i) along the lines xi -> xi + 2 c v_0 tau give

  int_{|tau| <= T_0} I(tau) d tau <= int sup_{|tau| <= T_0} |g^_tau(xi)| ( int |Psi(tau, xi + 2 c v_0 tau)| d tau ) d xi <= 32 pi A^{1/2}.

For k >= 0 let J_k be the set 2^k T_0 <= |tau| < 2^{k+1} T_0, where 2^k <= |a| R^2 < 2^{k+1}, and gamma_k = int_{J_k} G with
G(tau) = int |Psi(tau, xi)| d xi, so that sum_k gamma_k <= (4 pi)^2 by (ii). On J_k two bounds hold. By (g2),
int_{J_k} I <= B R 2^{-k/2} gamma_k. By (g2) on |xi| < 8 |a| R, (g3) outside, and (i),
int_{J_k} I <= 4 pi (32 B 2^{k/2} + D 2^{-k}). Take k_* with 2^{k_*} <= R < 2^{k_* + 1}; the second bound for k <= k_* and the
first for k > k_* give

  sum_k int_{J_k} I <= 128 pi B (2 + sqrt 2) R^{1/2} + 8 pi D + (4 pi)^2 B R^{1/2}.

So the characteristic function is integrable, and its integral, divided by 2 pi, bounds the density. ∎

For c >= 1/R the bound 8 |c|^{-1/2} of single_hub_core/ is at most 8 R^{1/2}, so the content of Proposition 1 is the range
of small c, where the parabola is nearly flat over the range of V and only a frequency band sees its curvature: on
|tau| <= 1/(|c| R^2) the chirp e^{i tau c V^2} makes less than one turn over the range and is a smooth multiplier, which
the one-dimensional bound (i) absorbs; above, the Fresnel factor |tau c|^{-1/2} is at most R 2^{-k/2} on the k-th dyadic
band. The loss R^{1/2} comes from the band where the chirp makes about R turns over the range of V: there the Fresnel
bound and the bandwidth bound meet, and neither (i) nor (ii) says how Psi is distributed inside that band. The loss
is that of the method: |Psi| <= 1, (i) and (ii) all allow |Psi| = 1 on the rectangle 1/(|c| R) <= tau <= 1/(|c| R) + 4 pi,
|xi - 2 c v_0 tau| <= 2, whose line integrals are at most 4 pi and whose area is 16 pi, and there a = tau c is about 1/R, the
stationary point xi/(2a) of the chirp lies in the range of V, and |g^_tau(xi)| is about (pi R)^{1/2}. A bound built from
these three facts alone is therefore of order R^{1/2} at least; a better one has to use the phases of Psi.

The proof uses a weight on the laws in the same way as Proposition 3 of two_sheet_side/. If phi(Y) is a weight with
0 <= phi <= 1, Y = <y, X'> for any y, and |V - v_0| <= R wherever phi(Y) > 0, then the density of U + cV^2 under the
measure phi(Y) dPr is at most kappa (C_1 + C_2 R^{1/2}), kappa = (2 pi)^{-1} int |phi^|: expanding phi(Y) in Fourier adds
shifts eta y_i to the arguments of the psi_i, which (i) and (ii) do not see.

## 2. Laws of bounded support

**Proposition 2.** Suppose that every X_i with v_i != 0 is supported in an interval of length at most K, K >= 1. Then
for every real c, every s and every m,

  p_{U + cV^2}(s) <= C (1 + K^{1/2}),

with C an absolute constant.

*Proof.* The iterated tilt of Proposition 4 of two_sheet_side/, with V in place of the leak P. For u >= 1 put
delta = (log 2)/(4 u^{1/2}), theta = 4 u^{1/2}/K and r = K u^{1/2}, let B = {i : |v_i| > delta}, S the other coordinates with
v_i != 0, and V_S = sum_{i in S} v_i X_i. Since |B| <= delta^{-2}, the part of V on B lies within K/(2 delta) of a fixed
point, so on the weight phi((V_S - E V_S)/r) (phi a smooth cutoff, 1 on [-1, 1], 0 outside [-2, 2]) V lies within
R = K/(2 delta) + 2r <= 5 K u^{1/2} of a fixed point, and the weighted form of Proposition 1 applies. If the densities are at
most c_0 >= 1 instead of 1, the substitution X_i = Y_i/c_0 gives U + cV^2 = c_0^{-1}(U_Y + (c/c_0) V_Y^2), in which V_Y has
range c_0 R, so the weighted density is at most

  b(c_0, u) = c_0 kappa (C_1 + C_2 (5 c_0 K u^{1/2})^{1/2}).

On the rest, 1 - phi((V_S - E V_S)/r) <= e^{theta (V_S - E V_S) - 4u} + e^{-theta (V_S - E V_S) - 4u}; by Hoeffding's lemma each
term contributes at most e^{-2u} times the density of U + cV^2 under the law in which each X_i, i in S, is tilted by
e^{±theta v_i x}, and as theta delta K = log 2 the tilted densities are at most twice the ones they tilt, with the same
supports. With D(c_0) the supremum of p_{U + cV^2}(s) over laws of the kind in the statement with densities at most c_0,

  D(c_0) <= b(c_0, u) + 2 e^{-2u} D(2 c_0)   for every u >= 1,

and D(c_0) is finite by the unweighted Proposition 1 with the whole range of V. Iterating at c_0 = 2^j with u_j = j + 1,
the coefficient of b(2^j, u_j) is 2^j e^{-2j - j(j-1)}, which beats the growth 2^{3j/2} of b in j, and the last term tends
to 0. The term j = 0 is b(1, 1) <= C (1 + K^{1/2}). ∎

Comb laws whose teeth fill an interval of bounded length, however many and however narrow, are therefore bounded
uniformly: for (P2) the fine structure of the laws costs nothing, and what remains open is laws spread over long ranges
with gaps, such as the comb laws at the integers in single_hub_core/num/, where the maximal functional M_2 grows like N
and Proposition 2 gives a bound of order N^{1/2}. The same division holds for the leaking hub: for light laws of bounded
support it is at most C + sqrt 2 log log K (two_sheet_side/, Proposition 4).

Laws of bounded variation, unimodal laws among them, need neither bounded supports nor the leverage condition.

**Proposition 3.** Let u, v be orthonormal in R^m and let every X_i have a density of total variation at most T. Then for
every real c and every s, p_{U + cV^2}(s) <= C (1 + T)^2 with C an absolute constant. Unimodal densities at most 1 have
T <= 2.

*Proof.* As in Corollary 4.4 of extremal_laws/, write each density by the layer-cake formula as the mixture of the uniform
laws on the component intervals of its superlevel sets, weighted by length; given the intervals, X_i is uniform on an
interval of length l_i, and E[1/l_i] = TV/2 <= T/2. For such laws (U, V) has a log-concave density with covariance M/12,
M = sum_i l_i^2 r_i r_i^T, r_i = (u_i, v_i). A log-concave density p on the plane with mean mu and covariance Sigma satisfies
p(x) <= C (det Sigma)^{-1/2} exp(-c |Sigma^{-1/2}(x - mu)|), the exponential decay of isotropic log-concave densities moved
back by Sigma^{1/2}; as |Sigma^{-1/2}(x - mu)| >= |t - mu_2| lambda_max(Sigma)^{-1/2} at x = (a, t),
sup_a p(a, t) <= C (det Sigma)^{-1/2} exp(-c |t - mu_2| lambda_max(Sigma)^{-1/2}), whose integral in t is at most
C' lambda_min(Sigma)^{-1/2}. The density of U + c(V - b)^2 at s is at most int sup_a p(a, t) dt, hence at most
C lambda_min(M)^{-1/2} given the intervals. Replacing l_i by min(l_i, 1) lowers M, after which
lambda_min(M) >= det M/tr M >= det M/2, and by Cauchy-Binet det M = sum_{i<j} l_i^2 l_j^2 det(r_i, r_j)^2 with
sum_{i<j} det(r_i, r_j)^2 = det sum_i r_i r_i^T = 1. Convexity of x^{-1/2} gives
lambda_min(M)^{-1/2} <= 2^{1/2} sum_{i<j} det(r_i, r_j)^2 (l_i l_j)^{-1}, and averaging over the independent choices of
intervals, with E[1/min(l_i, 1)] <= 1 + T/2, gives the bound. ∎

A comb with N teeth has total variation 2N, and in every representation of it as a mixture of uniform laws on intervals
those intervals lie in teeth, so E|I|^{-1} >= N: the open part of (P2) is exactly where the laws cannot be written with long
intervals. On ten random orthonormal pairs in R^2 to R^12, with leverages up to 0.99, laws with density e^{-2|x|} give Monte
Carlo curved marginals 0.60 to 0.74 over c in {0.01, 0.1, 1, 10}, against 1.22 to 1.35 for unit intervals
(num/unimodal_p2_check.py).

## 3. Numerics

num/p2_adversary.py searches for comb laws that make the curved marginal large. Each X_i is uniform on N = 4 teeth of
width 1/4, and a (1+1) evolution strategy moves the gaps between the teeth to maximise the largest density of
U + c (V - b)^2 over c in {0.003, 0.01, 0.03, 0.1, 0.3}, seven vertex positions b and all s, on one random frame with
u_i^2 + v_i^2 <= 1/2 for each of m = 6, 10, 16 and 24 (40 minutes for m = 6 and 10, 45 for m = 16 and 24). The density of
(U, V) is computed by FFT of the product of the coordinate transforms; num/p2_validate2.py checks it against 8 x 10^6
samples, and the two agree to the sampling error (0.002 to 0.007) at three grid resolutions. num/p2_verify2.py rebuilds
each law found on a finer grid, re-estimates the density at the maximiser by Monte Carlo, and computes for the same laws
the largest density of a linear form cos t U + sin t V over 360 directions t, integrating the grid density along the
level lines (num/p2_lines.py).

  m    steps   largest density of U + c (V - b)^2      at c    largest density of a linear form    pair bound
               (grid / Monte Carlo, window 0.01)
  6    2054    1.292 / 1.296                           0.1     1.312                               5.99
  10   1416    1.219 / 1.221                           0.1     1.276                               6.44
  16    604    1.239 / 1.239                           0.01    1.243                               8.04
  24    425    0.861 / 0.863                           0.1     1.040                               11.08

In every case the parabola carries less than the best line for the same laws, although the search maximised the
parabola and never the line (num/p2_verify2_small.out, num/p2_verify2_big.out). Two further searches (num/p2_ratio.py,
40 minutes each for m = 6 and 10) maximised the ratio of the parabola to a line statistic that used nine slopes and
undercounted slanted lines, and reached 1.44 and 1.23 against it; against lines in every direction, computed as above,
the laws they found give 0.322 against 0.357 and 0.411 against 0.490, ratios 0.90 and 0.84 (num/p2_verify2_ratio.out).
A local search on six frames with four teeth per coordinate is weak evidence, and it does not reach laws spread over
long ranges, where Proposition 2 stops.

The same comparison on the two-class frame of Example 5.2 of single_hub_core/, with comb laws at the integers (N teeth of
width 1/N at 0, 1, ..., N - 1), where single_hub_core/num/ (section 12) found the parabola collecting two to three times
the density of U: the largest density of U + c (V - b)^2 over c in {±0.001, ±0.003, ±0.01, ±0.03, ±0.1, ±0.3} and 25
vertex positions is 1.145, 0.725 and 0.513 for N = 4, 8 and 12, and the largest density of a linear form over 360
directions is 1.352, 1.213 and 1.076 (num/p2_twoclass_lines.py). The lines that win run along the rows of the lattice
that carries the teeth. So every computation so far is consistent with a statement stronger than (P2):

  (P2') for every frame, all laws, every c and every s, the density of U + cV^2 at s is at most the largest density of a
        linear form cos t U + sin t V,

which with the flat bound would give (P2) with the constant sqrt 2. (P2') fails for densities on the plane that are not
marginals of product laws, such as a density spread evenly over a thin neighbourhood of an arc of the parabola, so a
proof has to use the product structure.
