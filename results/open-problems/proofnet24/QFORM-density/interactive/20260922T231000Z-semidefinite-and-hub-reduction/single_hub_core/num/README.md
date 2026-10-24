# Numerics for single_hub_core/

## 1. Twisted frame integrals (tlperp_comb.py, run_sel.py)

J(kappa) = int int |E exp(i zeta L + i xi V + i kappa U^2)| d zeta d xi for four coordinates, w = (1,1,1,1)/2,
v = (1,-1,1,-1)/2, and each X_i a comb of N teeth of width 1/N at the integers 0..N-1. The twist direction is aligned
(u = w) or orthogonal to the frame (u = p = (1,1,-1,-1)/2). Inside a tooth the phase is linearised (error at most
kappa/N^2 times a constant). On the comb U lies in Z/2, so kappa = 4 pi/q makes exp(i kappa U^2) a combination of q
linear phases of modulus q^{-1/2}. For the aligned twist these are translates of the untwisted transform along the
integrated direction, each carrying its full frame integral; for the orthogonal twist they shift the product off
its revival lattice. The prediction is that J grows with N for the aligned twist and not for the orthogonal one.

J(kappa)/J(0), with J(0) = 64.3 (N = 4) and 63.9 (N = 6):

| q | 8 | 12 | 16 | 24 | 36 |
|---|---|---|---|---|---|
| aligned, N = 4 | 1.890 | 1.738 | 1.589 | 1.396 | 1.250 |
| aligned, N = 6 | 2.332 | 2.333 | 2.203 | 1.921 | 1.647 |
| orthogonal, N = 4 | 0.835 | 0.760 | 0.764 | 0.804 | 0.884 |
| orthogonal, N = 6 | 0.791 | 0.741 | 0.706 | 0.647 | 0.691 |

At the non-lattice values kappa = 0.1, 0.3, 1.0 (N = 4) the ratios are 1.05, 1.21, 1.72 aligned and 1.00, 0.91, 0.76
orthogonal. The small q (kappa >= pi) are outside the linearisation. Full outputs: tlperp_N4_output.txt,
tlperp_N6_output.txt.

The mixed twist exp(i kappa L P), P = <p, X> with p = (1,1,-1,-1)/2 orthogonal to the frame but on the same
coordinates (lp_twist.py, the twist relevant to Proposition 2.3 of the report), with the same linearisation:

| q | 8 | 12 | 16 | 24 |
|---|---|---|---|---|
| L P, N = 4 | 0.768 | 0.430 | 0.363 | 0.422 |
| L P, N = 6 | 0.819 | 0.848 | 0.524 | 0.270 |

It lowers the frame integral, like the orthogonal twist and unlike the aligned one (lp_twist_N4_output.txt, which
also repeats the L^2 and P^2 rows of the table above, and lp_twist_N6_output.txt, whose P^2 row reproduces
0.791, 0.741, 0.706, 0.647).

## 2. The maximal functional (m2_comb.py, m2_fibre.py)

M_2 = int sup_u rho_{V,B}(u, s) ds for two orthonormal projections V = <v, X>, B = <b, X> of m comb coordinates
(N teeth of width 1/N at the integers), computed by rasterising each coordinate's line measure with bilinear weights
and multiplying 2D FFTs; the control is uniform on [0, N] (same spread, no fine structure).

| frame | N = 4 | N = 8 | N = 16 | uniform control, N = 16 |
|---|---|---|---|---|
| m = 2, rotation by 45 degrees | 2.37 | 2.37 | 2.70 | 0.10 |
| m = 2, irrational rotation | 3.98 | 7.98 | 14.44 | 0.10 |
| m = 3, fibre (1,1,1), rational basis | 2.06 | 2.26 | 2.30 | 0.09 |
| m = 3, fibre (1,1,1), irrational basis | 2.11 | 5.43 | 10.99 | 0.08 |
| m = 4, Walsh | 1.60 | 1.62 | 1.63 | 0.08 |
| m = 4, random | 0.79 | 0.45 | 0.25 | 0.08 |
| m = 6, random | 0.37 | 0.16 | 0.08 | 0.07 |
| m = 8, random | 0.34 | 0.16 | 0.08 | 0.08 |

M_2 grows like N in two situations: a projection with no fibre (m = 2), and a one-dimensional rational fibre with an
irrational basis of its orthogonal plane. There the fibre lines run along lattice diagonals through N teeth, their N^2
images have distinct s-coordinates, and the supremum over u finds one for almost every s. For random frames with
m >= 6 the comb matches the uniform control. Full outputs: m2_comb_output.txt, m2_fibre_output.txt.

## 3. Curved slicing (cs_test.py, cs_resonant.py)

The density of Y = V^2 + beta B off the fold {|V| > 1/2}, pushed forward from the same grids, for the projection where
M_2 grows like N (fibre (1,1,1), irrational basis) and, as an adversarial case, for the rational basis with
beta = sqrt6/2, where the parabola u^2 + beta s = y meets a point of the image lattice in every column. The supremum
over y of that density:

| configuration | N = 4 | N = 8 | N = 16 |
|---|---|---|---|
| irrational basis, beta = 0.02 | 0.62 | 0.47 | 0.23 |
| irrational basis, beta = 0.1 | 0.71 | 0.39 | 0.24 |
| irrational basis, beta = 0.5 | 0.40 | 0.18 | 0.12 |
| rational basis, beta = sqrt6/2 (resonant) | 0.42 | 0.29 | 0.16 |
| rational basis, beta = sqrt6 | 0.28 | 0.16 | 0.10 |

The bound (CS) asks for C/r = 2C here. The density decreases with N in every case, while M_2 grows like N in the first
three rows: the lattice points a resonant parabola does meet carry mass of order 1/N^2 each, and there are only of
order N^{1/2} of them in the support.

## 4. Collisions on dyadic shells (shell_l2.py)

The collision norm int h^2 dy of the density of Y = V^2 + beta B restricted to R <= |V - V_0| < 2R, on the same grids
as Section 3 (fibre (1,1,1), irrational basis), with V_0 the mean of V. Lemma 3.6 of the report, in its version without
the slice in L, bounds each shell by 4 log 2 = 2.77.

| N | beta | R = 1/4 | R = 1/2 | R = 1 | R = 2 | all of \|V - V_0\| >= 1/4 |
|---|---|---|---|---|---|---|
| 4 | 0.02 | 0.118 | 0.113 | 0.052 | 0.003 | 0.318 |
| 4 | 0.5 | 0.040 | 0.045 | 0.034 | 0.002 | 0.202 |
| 8 | 0.02 | 0.026 | 0.032 | 0.028 | 0.013 | 0.140 |
| 8 | 0.5 | 0.008 | 0.009 | 0.015 | 0.015 | 0.078 |
| 16 | 0.02 | 0.005 | 0.008 | 0.008 | 0.007 | 0.058 |
| 16 | 0.5 | 0.002 | 0.002 | 0.003 | 0.008 | 0.029 |

beta = 0.1 lies between the two (shell_l2_output.txt). The norms fall with N while M_2 grows like N on this frame.

## 5. Small cross terms (small_eps.py)

The density of Q = 2 X_h L + V^2 + 2 eps L P as eps -> 0, the regime Propositions 2.3 and 2.4 leave open when P is
spread. The estimator is exact in the hub: given X', Q is affine in X_h, so P(|Q - y| <= delta | X') is a difference of
values of the hub distribution function. The resolution is fixed at delta = 0.002 for every eps, the maximum is over a
grid of y, and each entry uses 3 million samples of X'. Hub laws: uniform on [0, 1], or a random union of intervals of
length eps covering half of [0, 2] (rough at the scale of the cross term, the case in which Proposition 2.3 loses
eps^{-1/2}). Light laws: combs of 8 teeth of width 1/8 at the integers, centred, or uniform on [-1/2, 1/2]. Frames: the
Walsh frame of Section 1 (w, v, p on four coordinates) and a random orthonormal frame on six coordinates, drawn afresh
for every entry.

| frame, light law, hub law | eps = 0.3 | 0.1 | 0.03 | 0.01 | 0.003 |
|---|---|---|---|---|---|
| Walsh, comb, rough hub | 0.190 | 0.166 | 0.229 | 0.300 | 0.268 |
| Walsh, comb, uniform hub | 0.316 | 0.433 | 0.434 | 0.433 | 0.436 |
| Walsh, uniform, rough hub | 2.505 | 0.623 | 1.061 | 1.614 | 1.277 |
| Walsh, uniform, uniform hub | 2.135 | 2.141 | 2.144 | 2.140 | 2.142 |
| random m = 6, comb, rough hub | 0.056 | 0.089 | 0.076 | 0.078 | 0.074 |
| random m = 6, comb, uniform hub | 0.103 | 0.119 | 0.121 | 0.120 | 0.119 |
| random m = 6, uniform, rough hub | 0.611 | 0.949 | 1.112 | 1.099 | 1.289 |
| random m = 6, uniform, uniform hub | 1.885 | 1.863 | 2.025 | 1.891 | 2.097 |

Nothing grows beyond the uniform-hub values as eps decreases. The rough law is redrawn for each eps (and the random
frame for each entry), which accounts for the variation along the rough-hub rows. Outputs: small_eps_walsh_output.txt,
small_eps_random6_output.txt.

Control (small_eps_ctrl.py): one fixed random frame on six coordinates, the rough hub with cells of length c, and the
cross term at eps = c and at eps = 0 on the same hub law.

| light law | c = 0.1 | 0.03 | 0.01 | 0.003 |
|---|---|---|---|---|
| uniform, eps = c | 0.798 | 1.162 | 1.340 | 1.275 |
| uniform, eps = 0 | 0.794 | 1.161 | 1.331 | 1.277 |
| comb, eps = c | 0.071 | 0.075 | 0.075 | 0.085 |
| comb, eps = 0 | 0.083 | 0.086 | 0.075 | 0.084 |

The cross term changes the peak by less than the sampling noise; the rise along the uniform row is the hub law's,
which gets rougher as c decreases. Output: small_eps_ctrl_output.txt.

The same estimator in the spread regime (small_eps_dim.py, small_eps_dim_output.txt): one random frame per m with
w_i^2 + v_i^2 <= 1/2, comb light laws, 10^6 samples per entry.

| m, largest abs(w_i) | rough hub, eps = 0.01 | rough hub, 0.001 | uniform hub, 0.01 | uniform hub, 0.001 |
|---|---|---|---|---|
| 8, 0.61 | 0.078 | 0.080 | 0.123 | 0.123 |
| 32, 0.43 | 0.091 | 0.085 | 0.131 | 0.131 |
| 128, 0.21 | 0.078 | 0.085 | 0.132 | 0.132 |

Nothing grows with m or with 1/eps, where Proposition 3.17 of the report allows a logarithm of m and the Fourier
bounds a double logarithm of 1/eps.

With a hub diagonal a (small_eps_dim_diag.py, small_eps_dim_diag_output.txt; given X' the hub measure of the set where
a x^2 + 2 x L lands in the window is read off the hub distribution function at the four root endpoints), eps = 0.01,
the same frames: rough hub 0.078, 0.083, 0.084 at m = 8, 32, 128 for a = 0.5 and 0.081, 0.086, 0.087 for a = -0.5;
uniform hub 0.120, 0.128, 0.129 and 0.123, 0.131, 0.132. The case with hub diagonal, where the bounds of the report
carry log(1/eps), is as flat as the one without.

## 6. A sheared rational frame (shear_twist.py)

For integer vectors W, V, P, pairwise orthogonal, with P = alpha W + beta V modulo q coordinatewise, the value
<P, k> mod q is a linear function of (<W, k>, <V, k>) on Z^m. At kappa_0 = 2 pi |W| |P|/q the mixed twist
exp(i kappa L P) restricted to the lattice is then exp(2 pi i a (alpha a + beta b)/q), a = <W, k>, b = <V, k>: a Gauss
phase in the integrated variables, i.e. an aligned twist. The frame W = (1,1,1,1,1), V = (2,-1,1,0,-2),
P = (2,0,-2,-1,1) has P = 4W + 4V mod 5 (found by find_shear.py), so kappa_0 = 2 pi sqrt50/5 = 8.886 and the lattice
phase is exp(-2 pi i (a^2 + a b)/5). Comb laws of N = 4 teeth of width 1/4 at the integers, phase linearised inside a
tooth, integral over |zeta|, |xi| <= 64 with step 1/4; J(0) = 18.92.

| kappa | kappa_0/2 | kappa_0/sqrt2 | kappa_0 | 1.0613 kappa_0 |
|---|---|---|---|---|
| J(kappa)/J(0) | 2.803 | 2.744 | 3.481 | 3.250 |

So on this frame the mixed twist raises the frame integral, unlike on the Walsh frame of Section 1, with the largest
value at the lattice-aligned kappa_0. The frame is not spread (w_1^2 + v_1^2 + p_1^2 = 1), and J(kappa_0) = 65.9 is below
the constant (4 pi)^2 = 157.9 of the untwisted bound for spread frames, so this is not a counterexample to the frame
bound that Theorem H would need; it shows that such a bound has to use the spread of the frame. Output:
shear_twist_N4_output.txt.

## 7. Two hubs (twohub.py)

Q = 2 X_1 X_2 + 2 X_1 L_1 + 2 X_2 L_2 + 2 L_1 L_2 + lambda V^2 = 2 (X_1 + L_2)(X_2 + L_1) + lambda V^2: at lambda = 0 this is the
rank-two example of hub_pairs/, Theorem 1 (hub block [[0,1],[1,0]], Schur-matched remainder), whose small-ball probability
is of order eps log(1/eps). Hubs uniform on [0, 1], six light coordinates uniform on [-1/2, 1/2], (l_1, l_2, v) a random
orthonormal frame; exact in X_2, 4 million samples, maximum over a grid of levels near 0 of P(|Q - s| <= delta)/(2 delta).

| lambda | delta = 0.01 | 0.003 | 0.001 | 0.0003 |
|---|---|---|---|---|
| 0 | 1.564 | 1.866 | 2.140 | 2.444 |
| 1 | 0.948 | 0.960 | 0.963 | 0.955 |

Without the transverse square the values grow like log(1/delta); with it they are flat, as Theorem 6.1 of the report
requires (its bound is 11.5 here). Output: twohub_output.txt.

## 8. Light laws with nested scales (cantor_eps.py)

The probe of Section 5 with light laws X = sum_{j < J} 3^j B_j + 2^{-J} U (B_j fair bits, U uniform on [0, 1]): 2^J intervals of
length 2^{-J}, density 1, structure at J scales. The estimator is that of Section 5 (delta = 0.002, 2 million samples, one
fixed frame per row).

| frame, hub law, eps | J = 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Walsh, rough, 0.01 | 1.013 | 0.538 | 0.238 | 0.113 | 0.046 | 0.012 |
| Walsh, rough, 0 | 1.021 | 0.546 | 0.252 | 0.109 | 0.043 | 0.017 |
| Walsh, uniform, 0.01 | 1.575 | 0.841 | 0.397 | 0.177 | 0.060 | 0.016 |
| random m = 6, rough, 0.01 | 0.460 | 0.118 | 0.025 | 0.005 | 0.001 | 0.000 |
| random m = 6, uniform, 0.01 | 0.769 | 0.174 | 0.037 | 0.007 | 0.001 | 0.000 |

Structure at more scales forces a larger spread under the density bound 1, and the peak falls. Output:
cantor_eps_output.txt.

## 9. Three hubs (Theorem 6.3)

threehub_check.py samples Q = X_H^T B X_H + 2 <X_H, L> + R(X') with three hubs, M = I_3 (so the bound of Theorem 6.3 is
3 sqrt 2 = 4.24) and adversarial choices: the rank-two swap block with R = 2 L_1 L_2, the Schur-matched remainder
L^T B^{-1} L for an indefinite B (the form is then rank three), comb light laws, a remainder with 30 sin(X_1 X_2), and a
small hub block with no remainder. The histogram peaks (4 million samples, bin widths 0.02, 0.01, 0.005) are at most
0.52, flat in the bin width (threehub_check_output.txt).

## 10. Constant of Proposition 3.13

With g(eta) = V |eta|^{-3/2} (A (1 + log_+(2 |eta|^{3/2}/V)) + 1/2) and A = 2 (4 pi/|lambda|)^{1/2}, trapezoid quadrature of
(2 pi)^{-1} int min(1, g) over |eta| in [1e-3, 1e9] (600001 log-spaced points) gives 4.03 (A V)^{2/3} at |lambda| = 1 and
3.80 (A V)^{2/3} at |lambda| = 4, the same for V = 2, 10 and 100 (the ratio depends on A only, by scaling). The ratio is not
monotone in A (3.38 at |lambda| = 100, 4.83 at 10^4, 16.9 at 10^6), but the bound itself, ratio times (A V)^{2/3}, is increasing
in A: 14.88, 8.83, 2.69, 0.83, 0.62 V^{2/3} at |lambda| = 1, 4, 100, 10^4, 10^6, with limit (3/pi) (V/2)^{2/3} = 0.60 V^{2/3}
(f313.py in the scratch record).

## 11. The one-variable bound of Proposition 3.14

p314_check.py computes the exact push-forward density of dt/(2|t|) on 0 < |t| < 1 under x(t) = alpha/(2t) - sigma t/2
(both roots of sigma t^2 + 2xt - alpha = 0), on a grid of step 2e-5, and integrates it over its top set of measure 1.
Over 200 random (alpha, sigma) with |alpha| in [1e-4, 10] and |sigma| in [1e-3, 1e3] the result is at most 0.27 of
3.5 log(1 + 2/|alpha|) + 0.5 log(1 + 2|sigma|). For sigma = 0 the value is log(1 + 1/|alpha|) exactly; the grid gives it
to within 1 percent (the midpoint rule at the edge |x| = |alpha|/2).

Proposition 3.16 (p316_check.py, p316_check_output.txt): 400 random configurations, m = 3 to 8 light coordinates, a
random orthonormal pair (w, v), cross terms q of three sizes, linear terms b, lambda of either sign, i the coordinate of
largest |w_i| and X_R uniform in [-2, 2]. The hub value computed with X_i = (t - beta - L_R)/w_i agrees with
alpha/(2t) + c_0 - sigma t/2, sigma = lambda v_i^2/w_i^2 + 2 q_i/w_i, to 2.5 x 10^-14, and |u_R|^2 = 1 + v_i^2/w_i^2 to
10^-15. With X_i uniform on one to five teeth and a hub law uniform on a random half of the cells of [-1, 1] (cells of
length 0.05 or 0.2), the exact conditional density of Q at s given X_R (quadrature over X_i) is at most 0.10 of the
conditional bound 1/2 + |w_i|^{-1}(3.5 log(1 + 2/|alpha|) + 0.5 log(1 + 2|sigma|)).

The hub diagonal in the frame of w (wframe_check.py, wframe_check_output.txt): five light coordinates, a random
orthonormal frame, random q, b and light diagonal d. With X' = Y + L w and Y expanded in a basis of the orthogonal
complement of w, sympy gives N(t) of degree 2 in t = L + beta with leading coefficient equal to 2 <q, w> + sum_j d_j w_j^2
to twelve digits, the coefficient of t in V equal to <v, w> (rounding, 2 x 10^-17), and t_m = a B/(2 kappa) linear in X'
with a coefficient vector orthogonal to w, so that Z_0 = t - t_m has a coefficient vector of norm at least 1 (1.63 here).

## 12. Curved marginals against the maximal functional on lattice frames (p2_lattice.py)

Comb laws X_i = K_i + W_i/N (K_i uniform on 0..N-1, W_i uniform on [0,1]), so every coordinate has density 1 on N teeth.
The lattice part (<a,K>, <b,K>) is computed exactly by integer convolution; the cell part is replaced by its Gaussian limit
(covariance I/(12 N^2)), which changes densities by a bounded factor and not their growth in N. The density of U + cV^2 is
the sum over lattice points of the line integral of a Gaussian bump along the tangent of the parabola; M_2 is estimated
row by row. Three frames: the two-class frame of Example 5.2 (m = 4, leverage 1/2, tan theta = sqrt 2); a rational plane in
R^8 with eight distinct coordinate directions, a = (2,-2,-2,-3,-1,-2,3,3), b = (2,-3,3,2,-3,2,2,-1) (orthogonal, maximal
leverage 0.30), rotated by tan theta = sqrt 2; and the same plane with its rational basis. Values for N = 4, 8, 12, 16
(p2_lattice_output.txt):

- two-class frame: the curved density over c in {0, 0.001, ..., 0.1} is at most 1.19, 0.60, 0.56, 0.32, below the bound 8 of
  Example 5.2, while M_2 = 3.2, 6.3, 8.5, 11.3 grows linearly;
- eight directions, irrational basis: the curved density is 0.34, 0.17, 0.11, 0.09, never more than 13 percent above the
  flat marginal at c = 0 (both decay like 1.4/N, the scale of the spread laws), while M_2 = 0.36, 0.46, 0.68, 0.91 grows
  linearly: every line V = v meets an isolated lattice bump of height of order one;
- eight directions, rational basis: the flat marginal is resonant (0.28 for every N, the lattice rows of U) and every c > 0
  lowers it (to 0.07-0.16 at N = 16), while M_2 stays at 0.28 because most lines V = v meet no row.

So on every lattice frame tested the parabola collects at most the flat share, and the maximal functional grows linearly in
N as soon as the projected lattice is two-dimensional and the basis is irrational, whatever the number of coordinates.

## 13. The cross-term twist on a frame spread in three dimensions (twist3d/)

Section 1 measured the twist exp(i kappa L P) on a four-coordinate frame, where (w, v, p) has leverages 3/4, and
Section 6 on a five-coordinate sheared frame. Here the frame is spread in three dimensions: the 8 x 3 matrix of all sign
vectors divided by sqrt 8, so every coordinate has w_i^2 + v_i^2 + p_i^2 = 3/8, rotated inside its span by
R = R_(1,2,0)(arctan sqrt 2) R_(0,1,3)(arctan sqrt 3) so that no lattice direction survives in (L, V, P). Comb laws
X_i = K_i + W_i/N as in Section 12. The lattice part of (L, V, P) is exact (an integer convolution of the eight sign
vectors, checked against 2 x 10^6 samples: mc_check_output.txt); the cell part is its Gaussian limit N(0, I_3/(12 N^2)),
isotropic because the frame is orthonormal, with mean zero because the sign rows sum to zero. Given L = l the twist is
linear in the cell's P-part, so in this model the complex density of (L, V) under the twist is exact:

  A(l, v) = exp(-sigma^2 kappa^2 l^2/2) sum_z p_z exp(i kappa l P_z) g_sigma(l - L_z) g_sigma(v - V_z),   sigma^2 = 1/(12 N^2).

T(y, t) = E exp(i (y L + t V + kappa L P)) is its Fourier transform. Two computations: A deposited on a grid of step
sigma/3, padded twice, and a two-dimensional FFT (j2d.py, j2dp.py); and, for each y, the cell's (L, P)-part integrated in
closed form and the V-part deposited before a one-dimensional FFT in t (j1check.py, j1mixed.py). They agree to three or
four digits (N = 4: J_2 = 9.032, 15.431, 25.129 against 9.033, 15.432, 25.131 at kappa = 0, 1, 2).

The frame integral that Theorem H needs, J_2(kappa) = int int |T| dy dt (the mixed norm below with p = 1):

| N | 3 | 4 | 5 | 6 | 8 | 10 |
|---|---|---|---|---|---|---|
| kappa = 0 | 13.35 | 9.03 | 7.05 | 5.67 | 3.96 | 3.09 |
| kappa = 0.5 | 14.65 | 11.22 | 10.47 | 10.74 | 12.55 | 14.96 |
| kappa = 1 | 16.98 | 15.43 | 16.59 | 18.62 | 23.45 | 28.23 |
| kappa = 2 | 22.88 | 25.13 | 28.95 | 32.63 | 38.35 | 42.79 |

At N = 12, J_2(1) = 32.50.

The untwisted integral falls like 32/N, the scale of the spread laws, and at every fixed kappa the twist raises it by a
factor that grows with N (from 1.3 at N = 3 to 5.9 at N = 8 for kappa = 1). The values stay below (4 pi)^2 = 157.9, but
nothing in the table suggests a bound uniform in N.

The mixed norms int dt ( int dy |T(y, t)|^p )^{1/p} that Proposition 5.3 of the report needs, kappa = 1 (full tables for
kappa = 0, 0.5, 1, 2 in j2dp_output.txt; N = 10, 12 from j1mixed.py, j1mixed_N10_N12_output.txt):

| N | 3 | 4 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|
| p = 1 | 16.98 | 15.43 | 18.62 | 23.45 | 28.23 | 32.50 |
| p = 1.25 | 11.21 | 9.85 | 10.40 | 11.43 | 12.40 | 13.25 |
| p = 1.5 | 8.76 | 7.55 | 7.30 | 7.33 | 7.40 | 7.51 |
| p = 1.75 | 7.45 | 6.34 | 5.78 | 5.45 | 5.23 | 5.11 |
| p = 2 | 6.65 | 5.61 | 4.91 | 4.42 | 4.08 | 3.87 |

At kappa = 2 the p = 3/2 norm is 9.92, 9.44, 9.18, 9.06, 9.13 for N = 3, 4, 6, 8, 10. On this rotation the norms with p >= 3/2
are flat or falling in N and the one with p = 1.25 grows slowly. With the off-plane phase e^{3iP} added
(j2dp.py N irr 0,1 3.0) the kappa = 1 values at N = 4, 6, 8 are 14.80, 18.43, 23.31 for p = 1 and 7.15, 7.21, 7.29 for
p = 3/2. A second irrational rotation, R_(3,-1,2)(arctan sqrt 5) R_(1,1,1)(arctan sqrt 7) (j2dp.py N irr2; N = 10
from j1mixed.py), behaves differently at kappa = 1:

| N | 4 | 6 | 8 | 10 |
|---|---|---|---|---|
| p = 1 | 15.45 | 18.33 | 23.06 | 27.77 |
| p = 1.5 | 7.14 | 8.35 | 9.80 | 10.72 |
| p = 2 | 5.17 | 5.95 | 6.74 | 7.03 |

(at kappa = 0: 8.79, 5.39, 4.00 for p = 1 and 4.34, 3.66, 3.24 for p = 2). So whether an L^p norm with p > 1 stays bounded
depends on the frame, and on the second rotation even the p = 2 norm grows, although its inner integral is exact by
Plancherel (2 pi int |mu_t(l)|^2 dl). Only unmodulated comb laws are computed; the supremum over modulations in the
definition of J_p is not tested. The growth comes from the spread of the laws, not from their roughness. For fine combs, teeth of width 1/N at
spacing 2/N filling [0, 2] (the same density, the same tooth width, bounded range), on the second rotation
(j2dp.py N irr2 0,1,4 0 fine, j2dp_fine_output.txt) J_2 is 20.6, 17.5, 17.3 at kappa = 1 and 24.8, 18.8, 17.5 at
kappa = 4 for N = 4, 8, 12, against 19.9, 17.4, 17.3 untwisted, and every mixed norm is flat or falling in N.

The orthogonal twist exp(i kappa P^2) of TL_perp behaves differently on the same frames and laws (j2perp.py,
j2perp_output.txt): at kappa = 1, J = 14.74, 13.75, 13.48 (first rotation) and 14.78, 13.61, 13.33 (second) for
N = 4, 6, 8, and it is smaller at kappa = 0.05, 0.2, 0.5. It rises above the untwisted value, which falls like 1/N,
but its size stays flat in N. For kappa bounded below it is bounded outright: the Fresnel identity in P and the
three-dimensional Brascamp-Lieb bound give J(kappa) <= (4 pi)^{5/2} |kappa|^{-1/2}. The growth of Section 13 is
therefore special to twists that involve the hub partner L, which shear the integration in its frequency y.

The hub-conditioned form, where the twist is proportional to the partner frequency (kappa = theta y, theta = eps/|x|
for a hub value x), J_mult(theta) = int_{|y| <= 2/theta} int |T(y, t; theta y)| dt dy (jmult.py): its largest value over
theta in {0.02, 0.05, 0.1, 0.3, 1} is 12.4, 14.6, 17.0 at N = 4, 6, 8, always at theta = 0.05, against J_2(0) = 9.0, 5.7,
4.0. It grows as well.

The density itself does not follow these integrals. For Q = 2 X_h (L + beta) + V^2 + 2 eps L P on the same frame, exact
comb laws (uniform teeth, no Gaussian cell), X_h uniform on [-1/2, 1/2], beta = 0 and 4 x 10^7 samples per line
(hub_mc.py, bin 0.02), the largest density is 1.53, 0.51, 0.18 at N = 2, 4, 8, the same for eps = 0, 0.01, 0.001 within
the sampling noise (hub_mc_output.txt). A window estimator that is exact in the hub (audit_density.py) gives 1.527,
0.516 and 0.1825 at the same three points. The worst hub law for given light laws is the bathtub one, density 1 on the unit set where
W(x) = p_{Q_x}(s) is largest (Q_x the form given X_h = x); W is the density of the weighted push-forward of X' under
x* = (s - V^2 - 2 eps L P)/(2(L + beta)) with weight 1/(2|L + beta|) (bathtub.py, bathtub_output.txt). On the second
rotation, where every frame integral above grows, the worst-hub density is 0.5623 and 0.5626 at N = 4 (s = 0) for
eps = 0 and 0.003, and 0.3350 and 0.3352 at N = 6, from the same samples for both values of eps. The scatter between
seeds is larger: 0.559 +- 0.005 at N = 4 and 0.315 +- 0.011 at N = 6 over five seeds, the seed of these runs being the
high one at N = 6. At s = 0.3 the two values of eps agree to four digits; for fine combs the worst-hub density is 1.3731,
1.3730, 1.3732 at eps = 0, 0.003, 0.03 (N = 4, s = 0) and 1.324 at N = 8. Neither the rough hub nor the spread of the
light laws lets the cross term move the density. Where the cross term is effectively large, laws spread over a range N of
order 1/eps so that eps P is of order one on the hub scale, it lowers the worst-hub density: 0.0340, 0.0318, 0.0241 at
eps N = 0, 0.9, 3 (N = 30) and 0.0136, 0.0128, 0.0103 (N = 60), as Proposition 2.3 leads one to expect. Two-scale combs,
X = K + J/N + W/N^2 (N^2 teeth of width 1/N^2), give the same picture: 0.7506, 0.7506, 0.7501, 0.7467 at
eps = 0, 0.003, 0.03, 0.1 for N = 3 and 0.3557, 0.3556, 0.3551, 0.3508 for N = 5 (bathtub_output.txt).

A hub that sees P (adapted_hub.py, adapted_hub_output.txt). With beta = 0 the hub value is x* = (s - V^2)/(2L) - eps P
under a weight that does not depend on eps, so conditioning on P bounds the worst-hub density at every eps by
Phi = int dp sup_{|A| = 1} int_A W(x, p) dx, W the weighted density of (x*_0, P) (Section 5 of the report, (SP)). The
script estimates Phi from a weighted histogram in (x*_0, P), keeping in each P-column its top unit set of x-bins, on
columns of several widths dP, and prints the eps = 0 bathtub from the same samples. Both estimates are biased upward by
the selection of noisy bins, the more so the narrower the columns. With shuffle=True the script also runs the estimator
with P permuted across the samples; a hub that sees a shuffled P can gain nothing, so the excess of that control over
the bathtub is the bias alone, and net Phi is Phi minus it. The half-sample rows give the same size of bias. On the
second rotation, bin 0.01, P resolved to dP = 0.05 (integer combs), 0.005 (fine combs), 0.01 (two-scale combs):

  law                    N    s, beta    bathtub   Phi raw   shuffled P   net Phi   ratio
  combs at the integers  4    0, 0       0.557     0.630     0.595        0.592     1.06
                         6    0, 0       0.305     0.380     0.336        0.349     1.14
                         10   0, 0       0.148     0.205     0.165        0.188     1.27
                         12   0, 0       0.121     0.173     0.134        0.159     1.32
                         16   0, 0       0.076     0.117     0.083        0.110     1.44   (8 x 10^7 samples)
                         20   0, 0       0.054     0.089     0.060        0.083     1.54   (8 x 10^7 samples)
                         6    0.3, 0.5   0.245     0.297     0.249        0.293     1.19
                         12   2, 0.5     0.072     0.120     0.073        0.119     1.66
                         16   2, 0.5     0.051     0.090     0.052        0.089     1.74   (8 x 10^7 samples)
  fine combs             4    0, 0       1.381     1.522     1.525        1.378     1.00
                         8    0, 0       1.331     1.472     1.468        1.336     1.00
                         16   0, 0       1.319     1.450     1.447        1.322     1.00
  two-scale combs        3    0, 0       0.755     0.828     0.819        0.764     1.01
                         5    0, 0       0.354     0.405     0.397        0.362     1.02
  combs at the integers  2    0, 0       1.666     1.715     1.717        1.663     1.00
                         3    0, 0       0.886     0.946     0.929        0.903     1.02
                         3    0.5, 0.3   0.482     0.536     0.483        0.535     1.11
  the same, first rotation (irr)
                         2    0, 0       1.585     1.636     1.639        1.582     1.00
                         3    0, 0       0.845     0.895     0.883        0.856     1.01

For laws of bounded range the whole raw excess is the estimator's; for comb laws at the integers the gain is real and
grows slowly with N while both values fall. Where the eps = 0 bathtub is largest, two or three teeth, the hub that sees
P gains at most 2 per cent at s = 0, so the largest net Phi in these tables, 1.66, is the eps = 0 value itself. The fine-comb bathtub scatters by several per cent between sample sets
(1.315 and 1.379 for the two halves at N = 16 in the first runs): these laws are centred at 0, and the weight 1/(2|L|)
has a heavy tail. For the integer combs the ratio does not level off up to N = 20, while N times net Phi falls (2.37,
2.09, 1.88, 1.91, 1.75, 1.66 at N = 4, 6, 10, 12, 16, 20): the gain is not a bounded multiple of the eps = 0 value, but
Phi itself decreases. The comb structure does not rescale to a smooth profile at the resolution in P that is used, and
for s != 0 the fold of x*_0, at s/(2(L + beta)), moves with the conditional law of L given P, which a hub that sees P can
follow.

The same on the two-class frame of Example 5.2 (adapted_hub_twoclass.py, adapted_hub_twoclass_output.txt; w, v the
rotation by atan(sqrt 2) of (e_1 + e_2)/sqrt 2 and (e_3 + e_4)/sqrt 2, q^ in the span of e_1 - e_2 and e_3 - e_4 at
angle atan(sqrt 3), integer combs, beta = -E L, s = 0, bins 0.05, 8 x 10^7 samples), where the maximal functional M_2
grows like N: bathtub 0.438, 0.171, 0.064 at N = 4, 8, 16, net Phi 0.480, 0.189, 0.064, ratio 1.10, 1.11, 1.01. At
N = 16 the raw Phi at dP = 0.05 is 0.095 and the shuffled control 0.094: all of that excess is noise.

A random search over the extreme laws (adapted_hub_search.py, adapted_hub_search_output.txt). Each of the eight light
coordinates is uniform on T teeth of width 1/T at random positions in [0, R] (T = 1 to 4, R = T, 2T, 4T or 8T), and s
and beta are random in [-2, 2] and [-3, 3]; second rotation, x-bins 0.02, dP = 0.05, 4 x 10^6 samples per draw with the
shuffled control, and the three largest draws re-estimated with 4 x 10^7. Over 40 draws the largest net Phi is 0.70,
for uniform laws on [0, 1] (T = 1, R = 1), where the hub that sees P gains nothing (ratio 1.000); the next are 0.65 and
0.62, with ratios 1.01 and 1.00. The ratio is large only where Phi is small: 1.86 at bathtub 0.038 (T = 2, R = 8), 1.43 at
0.025 (T = 3, R = 24), 1.36 at 0.055 (T = 2, R = 16). A hub that sees P gains in proportion where the laws are spread
with gaps, which is also where the density is small.

The same over frames (adapted_hub_search_frames.py, adapted_hub_search_frames_output.txt and
adapted_hub_search_frames_centre_output.txt): m = 4, 5 or 6 light coordinates, (w, v) a tight frame for m = 4 (where
the leverage condition forces w_i^2 + v_i^2 = 1/2) and a Gaussian Q-factor redrawn until w_i^2 + v_i^2 <= 1/2 for
m = 5, 6, q^ random in the orthogonal complement; each coordinate uniform on [0, 1] or on T = 2..8 teeth of width 1/T at
random positions in [0, R], R = T, 4T, 16T; beta within 1 of -E L; in the second run the square is centred,
(V - v_c)^2 with v_c within 1 of E V. Sixty draws each (five of the first run have all their hub values beyond
|x| = 6 and read 0). The largest net Phi is 0.52 and 0.45. A hub that sees P gains in proportion often: the ratio is at
least 1.8 in 45 of the 113 draws and reaches 2.7 (bathtub 0.068, net 0.19, re-estimated with 3.2 x 10^7 samples), but
every draw with a ratio of at least 1.8 has bathtub at most 0.11 and net Phi at most 0.20.

The density of L near -beta for the integer combs (rho_star.py, rho_star_output.txt; second rotation, window
|l - E L| <= 1, 8 x 10^6 samples, bins 0.02 and 0.05, two halves): rho* = 0.364, 0.169, 0.084, 0.042, 0.021 at
N = 4, 8, 16, 32, 64, so N rho* stays at 1.35 to 1.45 and the bound of Proposition 5.5(a) with K = N falls from 5.9 to 1.1.

The block of L (block_of_L.py, block_of_L_output.txt): w = (e_1 + e_2)/sqrt 2 on two coordinates uniform on [0, 1],
v = (e_3 + e_4)/sqrt 2 on two combs at the integers, q^ = (e_1 - e_2 + e_3 - e_4)/2, lambda = 1, beta = -E L, V centred,
1.6 x 10^7 samples, x-bins 0.02, dP = 0.05. Only Proposition 5.6 covers this configuration (bound 10.8). Net Phi is
1.88, 1.20, 0.78, 0.45 at N = 4, 8, 16, 32 for s = 0, ratio to the bathtub 1.02 to 1.03, and 0.34, 0.21, 0.12, 0.057
for s = 1, ratio 1.22 to 1.29.

The maximal functionals of Proposition 5.4 (rloc.py, rloc_output.txt): from a histogram of (L, P) with square bins of
side h, the local functional int dp sup_{|l - l0| <= 1} rho_{L,P}(l, p) at l0 = 0 (the centre of L, so the window around
-beta = 0), the global one int dp sup_l rho_{L,P}(l, p), and the right side of Proposition 5.4 with lambda = 1 and a(p)
replaced by 2 sqrt 2. On the second rotation, h = 0.05:

  combs at the integers   N = 4, 8, 16       local 0.998, 0.520, 0.276   global 1.011, 0.542, 0.290   bound 9.75, 6.75, 4.56
  fine combs              N = 4, 8, 16       local 0.908, 0.769, 0.675   global 0.908, 0.769, 0.675   bound 7.86, 7.02, 6.40
  N teeth of width 1/N    N = 16, 64, 256    local 0.381, 0.174, 0.093   global 0.381, 0.174, 0.093   bound 4.80, 2.98, 2.07
  at spacing N^{-1/2}

On this frame the local and the global functional nearly agree and neither grows. With h = 0.1 the integer combs give
0.443 and 0.160 instead of 0.520 and 0.276 at N = 8, 16, so for them bins of side 0.05 do not yet resolve the cells and
the true values are larger; the other rows change by at most ten per cent.

The characteristic function of the single hub itself, phi_Q(eta) = E exp(i eta (2 X_h L + V^2 + 2 eps L P)), on the first
rotation (phiq.py): given the lattice point and the hub value the Gaussian cell integrates in closed form, and the hub,
a comb of Nh teeth of width 1/Nh, is integrated by Gauss-Legendre inside each tooth; 400 values of eta on a log grid from
0.05 to 12/sigma (phiq_output.txt). For combs at the integers (spread laws) eta |phi_Q(eta)| stays near a constant
across four decades of eta (between 0.05 and 0.12 for N = 4 with an 8-tooth hub), so the transform decays like |eta|^{-1} there, with
a coefficient that falls with the spread (0.04 at N = 8). With the cross term on, int |phi_Q| over the grid is 0.256 and 0.270 at eps = 0.03,
0.003 (0.263 on the second rotation at eps = 0.003), against 0.257 at eps = 0, for N = 8 and an 8-tooth hub. For fine combs of the same density, teeth of width 1/N at
spacing 2/N filling [0, 2] for the light coordinates and the hub, |eta|^{3/2} |phi_Q(eta)| stays between 1.0 and 1.4
from eta = 1 on, and int |phi_Q| over the grid is 3.01, 3.00, 3.02 at N = 4, 8, 16 and 2.99, 3.00 (N = 8) with the cross term at eps = 0.03,
0.003. In these examples the transform of Q is integrable, uniformly in eps and N, while the frame integrals above are
not bounded: the bounds lose by taking moduli of the twisted light transform before the pairing with the hub. A direct
Monte Carlo of the same fine-comb model gives largest densities 0.878 (N = 4) and 0.855 (N = 8), just below the value
(1/pi) int |phi_Q| = 0.96 that the transform bounds them by (audit_density_output.txt).
