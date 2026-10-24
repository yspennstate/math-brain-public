# NOTES - counterexample search (wave 2, piece 12)

Started 2026-09-23 (wall clock ~02:15 local). Target: break the conjecture where open, or give strong
numerical evidence of boundedness, families (a)-(e) of the assignment.

## 0. Plan (written before any computation)

Estimators (all exact conditional formulas averaged by Monte Carlo, no bins):
- E1 (hub-conditional). Condition on all non-hub coordinates X'. For one hub h with diagonal a,
  Q = a X_h^2 + 2 T X_h + R(X'), T = <A_{h,-h}, X'> + b_h/2, R = X'^T M X' + b'^T X' + c.
  p(s) = E_{X'} sum_{roots x of a x^2 + 2Tx + R = s} f_h(x) / |2 a x + 2 T|.
  For a = 0: E f_h((s-R)/(2T)) / (2|T|). Cost O(n^2) per sample (M X'), then the whole s-grid is
  nearly free. Variance is log-divergent at T = 0 (E[1/|T|; |s-R|<|T|]); SE from the sample is then
  only indicative, so every headline number is re-checked by E2 or by increasing N.
- E2 (fibre identity, all coordinates). p(s) = sum_i E_{X_-i} sum_roots f_i(t)|d_iQ|/|grad Q|^2.
  O(n^2 + n S) per sample. Finite variance when the critical set has codimension >= 3.
- E3 (histogram with shrinking bins) only as a coarse sanity check.

Law optimisation: p(s) is multilinear in (f_1..f_n); best response of coordinate i is the indicator
of the top measure-one superlevel set of g_i(x) = p(s | X_i = x). For leaves g_i is obtained from E1
by substituting X_i -> x on a grid (R, T are quadratic/affine in x): O(M G) per leaf. For a hub use the
proposal trick with E2 (sample X_h from a wide uniform, bin by X_h).

Families and what is swept:
(a) star + rank one + eps W, n in {50..500}, eps sqrt(n) in [0.01, 3], W: Wigner, aligned (wv^T+vw^T,
    ww^T, vv^T), low rank + noise, sign patterns, complement-supported, "anti-Fresnel" designs; lambda = +-1;
    beta and linear terms; hub law and leaf laws optimised.
(b) hub diagonal a in [0.001, 0.3] + dense remainder.
(c) 2-3 hubs with a nonzero small hub block B + remainder.
(d) multi-scale spectra, lattice-tuned combs at large n, hub/spread overlaps.
(e) convex side of rank three (definite; two-sheet side s<0) with mixed leverage.

## 1. Heuristic before numerics (CONJECTURAL, used only to aim the search)

For (a) with a uniform hub law on [-1/2,1/2]:
  p(s) = int dt/(2|t|) P(|R - s| <= |t|, T in dt).
So p(s) is controlled by the 2D small-ball of (T, R) near (0, s): if P(|T|<=tau, |R-s|<=u) <= K tau u^delta
then p is bounded. Growth needs R | T ~ 0 to concentrate at scales -> 0 on an event of probability
comparable to rho_T(0). With R = lambda V^2 + eps Q_W, V = <v,X'>, v perp w, the conditional spread of V
given T is >= c (each leaf has variance >= 1/12), and ||eps W|| << lambda cannot cancel lambda V^2. So I
expect (a) to be bounded with sup close to the eps = 0 value; the adversary's best chance is eps -> 0
itself (Prop 5.4 regime) with optimised laws. Gaussian-limit value of the pure star + rank one at s = 0,
lambda = 1: p(0) = int phi_sigma(l)/(2|l|) erf(sqrt(|l|)/(sigma sqrt 2)) dl, sigma^2 = 1/12 - to compute.

## 2. Estimator validation (NUMERICAL, t1_validate.py, t2_gauss_star.py; 02:25)

- E2 on X1^2+X2^2+X3^2 (uniform): 1.4037/1.9861/3.1438 at s = .05/.1/.25 vs exact 2 pi sqrt(s) = 1.405/1.987/3.1416.
- Star + rank one, 30 leaves, uniform laws, Q = 2 X_h L + V^2 (eigenvalues -1, 1, 1):
  s      -0.2    -0.05   0       0.05    0.15    0.3
  E1     0.501   1.591   3.547   2.838   1.736   0.784   (N = 1e6; SE .035 at s = 0, log-divergent variance)
  E2     0.499   1.594   3.559   2.838   1.733   0.785   (N = 1e5; SE .019 at s = 0)
  hist   0.499   1.576   3.369   2.812   1.751   0.781   (bin .005; cusp at 0 so the bin underestimates)
  E1 and E2 agree within error everywhere; E2 has the better variance at the cusp.
- Gaussian leaf limit (L, V iid N(0, 1/12), X_h uniform on [-1/2,1/2], Q = 2 X_h (L+beta) + lam V^2), by quadrature
  p(s) = int phi(v) E_1((s - lam v^2)^2/(2 sig^2)) / (2 sig sqrt(2 pi)) dv:
  max_s p = p(0) = 3.6207 (lam = +-1), 2.7873 (lam = 2); beta = .05/.1/.2 lowers it to 3.586/3.483/3.110.
  So the pure star + rank one has sup ~3.62 in the spread limit, below 3 sqrt 2 = 4.243.
- Figure of merit used from now on (scale invariance of the problem): F = |mu_3(A)| sup_s p_Q(s), mu_3 the third
  largest eigenvalue in modulus. The conjecture is sup F < infinity. Every number reported below is F.
- Bathtub bound for the kernel of the pure star + rank one: if the (L,V) density is <= 2 (Ball), then
  p(0) = int rho_LV 1{v^2 <= |l|}/(2|l|) <= 8 sqrt(l0), l0 = (3/16)^(2/3), i.e. <= 4.58 (PROVED, elementary bathtub;
  the extremal rho would be 2 on {|l| <= l0, v^2 <= |l|}, not a product-measure projection).

## 3. Compute situation (02:50)
Machine saturated (CPU load 100 %, 66 python processes from the parallel pieces). Measured throughput of numpy
is ~35M element-ops/s for me. So: exact low-dimensional quadrature for the spread (Gaussian) limits, and
Monte Carlo only for targeted finite-n and non-Gaussian (comb-law) checks. First attempt (famA_gauss.py,
Nelder-Mead on E2 with 2e4 samples) timed out without output - abandoned in favour of quadrature.

## 4. Family (a), first results (03:00)

4.1 Gaussian (spread-leaf) hub model, exact quadrature (gq.py, gq2.py). Q = 2 X_h (Y1 + beta) + mu Y1^2 + 2 kap Y1 Y2
 + lam Y2^2 + b1 Y1 + b2 Y2, Y ~ N(0, diag(s1^2, s2^2)), s_i >= 1/sqrt(12), X_h uniform. Exact formula
   p(s) = int phi(y1)/(2|y1+beta|) P_{Y2}(|s - R(y1,Y2)| <= |y1+beta|) dy1  (inner probability in closed form, erf),
 y1 = -beta +- u^2 substitution, Gauss-Legendre. Checked: p(0) = 3.620667 for every node count (60..400), equal to
 the scipy value 3.6207 of t2_gauss_star.py. This model is the n -> infinity limit of family (a) with W in
 span{ww^T, vv^T, wv^T + vw^T} (and of Prop 5.4's setting), with arbitrary leaf-variance inflation.
 Nelder-Mead over (mu, kap, lam, beta, b1, b2, s1, s2), F = mu_3 max_s p (opt_k2.py, 6 starts): the pure point
 mu = kap = 0, lam = +-1, beta = b = 0, s = 1/sqrt12 is a local max with F = 3.6207; the five random starts climb
 to 3.27-3.39 and are all heading to the same point (mu, kap -> 0, lam -> +-1, variances -> minimum, linear terms ->
 0). NUMERICAL: sup F = 3.6207 in this model.

4.2 Finite n1 = 50 leaves, uniform laws, exact window estimator (delta = .004, 6e4 samples, common random numbers),
 lam = 1, nine W types (Wigner, wv^T+vw^T, ww^T, vv^T, low rank on (w, v, u1, u2), low rank + Wigner, Wigner on
 span(w,v)^perp, sign pattern sgn(w)sgn(v)^T, Sylvester-Hadamard), eps sqrt(n) in {0, .01, .03, .1, .3, 1, 3}:
 F(eps = 0) = 3.390 (window value; the cusp at s = 0 makes the window underestimate the exact 3.55);
 for EVERY W type F decreases monotonically in eps: at eps sqrt n = 3, F = 1.61 (Wigner), 2.44 (wv), 2.72 (ww),
 3.02 (vv), 2.68 (lr), 2.35 (lrn), 1.53 (comp), 2.56 (sgn), 1.17 (Hadamard). Largest value over all 55 configs:
 the eps = 0 one. Nothing increases with eps. (out_famA_n50.txt)
 The aligned types (wv, ww, sgn) lose mainly through mu_3 < 1 (the twist lowers the third eigenvalue), the
 spread types (Wigner, comp, Hadamard) through smoothing of R given T, as the heuristic of Section 1 predicts.

## 5. Rank-3 remainder in the Gaussian hub model: the optimiser leaves the hub (03:09)

opt_k3.py (exact in X_h, Y1, Y2; 12-node Gauss-Hermite in Y3; Nelder-Mead over the 10 parameters of D and the linear
terms), start 2 climbed from 2.86 to F = 4.0789 at s = 0 with
  D = [[.011, -.001, 1.025], [-.001, 1.429, .013], [1.025, .013, 0]],  beta, b ~ 0,  eigenvalues (-1.426, 0, 1.426, 1.440).
Reading: R contains 2 (1.025) Y1 Y3, so Q = 2 L (X_h + 1.025 U) + 1.43 V^2 = 2 Z L + lam V^2 with the "hub variable"
Z = X_h + 1.025 U half a single coordinate and half a spread direction. In matrix terms the hub vector e_h has been
replaced by the unit vector (e_h + 1.025 u)/1.432, whose leverage on the coordinate h is only .49. The optimiser is
walking from the star + rank one (3.62) towards the fully Gaussian form 2 Z L + V^2 = Y1^2 - Y2^2 + V^2 with Z, L, V
iid N(0,1/12), i.e. the (1,1,-1) Gaussian form, whose density at 0 is exactly 3 sqrt 2 = 4.2426.
Mechanism (NUMERICAL + elementary): p(0) = int f_Z(y) g(y) dy with g(y) = E[delta(y + lam V^2/(2L))/(2|L|)] ~ c |y|^(-1/2)
at 0; with a pure |y|^(-1/2) kernel the three candidate hub laws give int f |y|^(-1/2) = 2.83 (uniform, a single
coordinate), 3.17 (triangle, (X1+X2)/sqrt2), 3.20 (Gaussian, variance 1/12). A genuine hub (single coordinate, density
<= 1) is therefore strictly worse than its spread version; hub configurations are dominated by the Gaussian (1,1,-1)
form. Not a counterexample; consistent with sup = 3 sqrt 2 being approached only in the Gaussian limit.
opt_k3 final (6 starts, 03:15): BEST 4.0789 (start 2 above); start 4 went the same way (k13 = .75, F = 3.68); the
other starts stayed below 3.46. Every start that climbed above 3.62 did so by spreading the hub direction.

## 6. Family (d), Gaussian spectra (famD_spectra.py, famD_spectra2.py; 03:20)
PROVED (elementary): for Gaussian Y, Q = sum_k theta_k (Z_k + m_k)^2 + c with independent Z_k, so for ANY sub-sum
Q_S, p_Q = p_{Q_S} * p_{Q - Q_S} and sup p_Q <= sup p_{Q_S}. Hence in the spread (Gaussian) limit adding eigenvalues
at any scales never raises the peak: sup F <= sup over three-term forms with |theta| >= mu_3 sigma^2.
Numerics (exact bin masses + FFT convolution; the method overestimates the cusp of (1,1,-1) by c sqrt(h):
4.345/4.295/4.269 at h = 4e-4/1e-4/2.5e-5, extrapolating to the exact 3 sqrt 2 = 4.2426; smooth cases are exact:
(1,1,1) 2.9037 = 12 x 0.24197, (1,1,-1,-1) 3.001 vs exact 3, (1,1,-2) 3.49 vs exact 12/(2 sqrt 3) = 3.464):
  (1,1,-1) + (.5,-.5,.25,-.25,.125,-.125): 2.516     (1,1,-1) + (2,-2,4,-4): 0.79     (1,-1,2,-2,4,-4,8,-8): 0.40
  (1,1,-1) + 40 x (+-.1): 2.56    (1,1,1) + (-.5,-.25,-.125): 2.68    (1,2,-1): 3.25    (1,1,-2): 3.46.
Nothing above the (1,1,-1) value; multi-scale spectra lower the peak sharply.

## 7. Family (b): hub with small diagonal + dense remainder (famB_mc.py, n1 = 100, 4e4 samples; 03:25)
Q = a X_h^2 + 2 X_h L + lam V^2 + eps X'^T W X', a in {+-.001, +-.01, +-.03, +-.1, +-.3}, lam = +-1, W in {Wigner, low
rank on (w,v,u1,u2), Wigner on span(w,v)^perp, sign pattern}, eps sqrt n in {0, .3, 1}; 240 configurations, exact
window estimator (delta .004), F = mu_3 max_s. Max F by |a| (over everything else):
  |a| = .001: 3.407   .01: 3.396   .03: 3.368   .1: 3.241-3.251   .3: 2.955      (eps = 0 values 3.404/3.396/3.368/3.24/2.95)
Mean F over configurations: 3.259 (eps = 0), 3.123 (eps sqrt n = .3), 2.770 (eps sqrt n = 1). The diagonal lowers F
mostly through mu_3 (.86 at |a| = .3); the window density itself stays at ~3.40 for every a. Q -> -Q symmetry
(a, lam) -> (-a, -lam) reproduced to 4 digits. No growth in a or eps; max at a -> 0, eps = 0 (the star + rank one).

## 8. The pointwise Rudelson-Vershynin correction and the bumpy-law experiment (03:27)
Correction received: Rudelson-Vershynin Lemma 3.1 bounds the decreasing rearrangement of |psi|, not |psi| pointwise
(uniform on M tiny intervals at spacing 2 pi/s0 gives |psi(s0)| ~ 1). The twist piece (04, N2/N13) proves that bumpy
laws make J = int |E exp(i u L + i kap L^2)| du >= c N for an aligned twist, killing Fresnel/BL bounds.
Real-variable remark (PROVED by citation): the aligned twist kap L^2 + kap' L V is a function F(L,V) of the form of
GEOM Prop 5.4 (complete the square in V: lam (V + kap' L/(2 lam))^2 + (kap - kap'^2/(4 lam)) L^2), so for the pure
hub + rank one + aligned twist the DENSITY is <= 1/2 + 16 |lam|^(-1/2) for ALL product laws (a = 0), bumpy or not.
The Fourier L^1 blow-up of N2 is therefore an artefact of the method on that family. What is not covered is aligned
twist + dense bulk W; famBump.py tests both, with (1) the N13 construction itself (n1 = 4, base-N boxes, D = 8N/kap),
(2) random boxes on [-R/2, R/2] at n1 = 50, (3) lattice-tuned boxes at spacing Delta (psi(2 pi/Delta) ~ 1), with and
without a Wigner bulk.
RESULTS (out_bump1/2/3.txt, 03:30) - bumpy and lattice-tuned laws LOWER the density in every case, twist or not:
 (1) N13 construction itself (n1 = 4, w = (1,1,1,1)/2, v = (1,-1,1,-1)/2, Q = 2 X_h L + lam V^2 + kap L^2, leaves = N
     unit-height boxes of width 1/N at base-N positions, D = 8N/kap - the laws for which J >= 2 pi N):
       kap = 1:  F = .294/.308 (N = 2, lam = +-1), .105/.096 (N = 3), .038/.040 (N = 4);  uniform leaves 2.01/2.15
       kap = .3: F = .409/.406, .149/.133, .047/.047;                                  uniform leaves 2.86/2.99
     F ~ N^-3: the component with all leaves in their first box has probability N^-4 and conditional density ~ N;
     every other component has |L| ~ D and is spread by the hub over width ~ D. J grows like N while p falls like N^-3.
 (2) n1 = 50, spread w, v, boxes at random positions in [-R/2, R/2]: kap = .1: F = 3.32 (R = 1, uniform), 2.11 (1.5),
     1.56 (2), .55 (4), .04 (16); kap = 1: 2.09, 1.37, .89, .23, .011 (N = 4 boxes); N = 2/8 at R = 2: 1.96/1.30 (kap .1).
 (3) n1 = 50, lattice-tuned laws (M boxes of width 1/M at spacing Delta, psi(2 pi/Delta) ~ 1), aligned twist kap in
     {0, .3, 1}, with and without a Wigner bulk eps sqrt n = .3: M = 4: F(kap = 0) = 3.48 (Delta = 1/4, uniform), 2.70
     (.3125), 2.07 (.375), 1.36 (.5), .54 (1), .20 (2); M = 8: 3.48, 2.63, 2.07, 1.38, .19, .07. The twist lowers F only
     through mu_3 (.861 at kap = .3, .618 at kap = 1): the window densities at Delta = 1/M are 3.48/3.51/3.50 for
     kap = 0/.3/1. The Wigner bulk lowers them further (3.13).
 Conclusion (NUMERICAL, consistent with Prop 5.4 for the pure aligned case): the bumpy laws that defeat the Fourier L^1
 bound do not raise the density; they spread L and V and the density falls like the inverse spread.

## 9. Family (c): two hubs with a nonzero hub block (famC_mc.py, n1 = 100, 2e4 samples, window in X1 exact,
12-node Gauss-Legendre in X2; 03:35)
Q = a1 X1^2 + 2 kap X1 X2 + a2 X2^2 + 2 X1 T1 + 2 X2 T2 + lam V^2 + eps X'^T W X', rows w1, w2 = cos th w1 + sin th u.
 th = 90 (orthogonal rows): F = 2.27 (no remainder: 4 eigenvalues +-1, +-1), 1.92 with lam V^2; hub blocks
   (kap, a1, a2) in {(0,0,.03..0.3), (.1,-.1,0), (.1,.1,0), (.1,0,0), (.1,-.1,.1), (.3,0,0), (.3,.3,.3)}: 2.17-2.28 and
   1.84-1.90 respectively (mu_3 applied); Wigner bulk eps sqrt n = .3/1: 1.88/1.77.
 th = 30: window density ~3.0 without remainder but mu_3 = .37-.55 (the second pair of eigenvalues +-sqrt(1 - cos th)
   is small), F = 1.09-1.59; with lam V^2: F = 2.23-2.30.
 th = 10 with lam V^2: F = 2.76 / 2.74 (kap = 0 / .1) - tending to the one-hub value as the rows become parallel.
 Max over family (c): 2.76 (th = 10, lam = 1). Nothing grows with the hub block or with the overlap.

## 10. Growth in n of the extremal hub configuration (exact_star.py, 1e6 samples each, E1 exact + window .002; 03:37)
Q = 2 X_h L + V^2, uniform laws, n1 leaves:  n1 = 30: 3.580 +- .050 (window 3.504);  100: 3.545 +- .017 (3.548);
300: 3.569 +- .021 (3.560);  1000: 3.577 +- .014 (3.579).  Gaussian limit 3.6207. Approached from below, no growth.

## 11. Family (e) engine validated (famE_semi.py; 03:39)
Semi-Gaussian model Y = X0 rho + G, G ~ N(0, sig^2 (I - rho rho^T)); given X0 the form is a noncentral generalised
chi-square in 3 Gaussian dimensions, density by an exact surface integral (sphere / one- or two-sheet hyperboloid,
invariant measure r^2 sinh(eta) or r^2 cosh(eta)), Gauss-Legendre x uniform-angle rule. Checks against closed forms
(chi2_2 - chi2_1 has density e^{-x/2}/(2 sqrt 2) for x >= 0 and e^{|x|/2} Gamma(1/2,|x|)/(2 sqrt(2 pi)) for x < 0):
 (1,1,-1): p(+.001) = 4.2173 (exact 4.2172), p(-.001) = 3.7427 (exact 3.742), p(-.05) = 1.5653 (exact 1.565);
 (1,1,1): max 2.9025 on the grid (exact 2.9037 at s = 1/12). Note the Gaussian two-sheet side falls like
 -c sqrt|s| from 3 sqrt 2 at s = 0-.

## 12. Two sharpened bounds by the bathtub principle (PROVED; 03:45)

Proposition S (star + rank one, zero hub diagonal, any laws). w, v in R^{n-1} orthonormal, L = <w,X'>, V = <v,X'>,
X_h independent of X' with density f_h <= 1, and Q = 2 (L + beta) X_h + lam (V - v_c(L))^2 + F_c(L) with beta real,
lam != 0, v_c, F_c arbitrary measurable. Then for mu = |lam|,
   ||p_Q||_inf <= C(mu) := 2 sqrt2 + sqrt2 log(1/3 + 4 sqrt2/mu)  for 1 <= mu <= 6 sqrt2,   C(1) = 5.360..
(and <= 2 sqrt2 for mu >= 6 sqrt2). This improves the zero-diagonal constant 1/2 + 16 |lam|^{-1/2} (= 16.5) of GEOM
Prop 5.4 and covers every aligned twist kap L^2 + kap' L V (complete the square in V) for every product law, including
the bumpy laws of the twist piece (N2/N13).
Proof. Given X', Q is affine in X_h with slope 2t, t = L + beta, so for a.e. s, p_Q(s) = E K(L,V) with
 K(l,v) = f_h(y)/(2|t|), y = (s - lam (v - v_c(l))^2 - F_c(l))/(2t).
(i) K <= 1/(2|t|).  (ii) For fixed l put u = v - v_c(l), s' = s - F_c(l). On each branch u > 0, u < 0 the map u -> y
is monotone with |du/dy| = |t|/sqrt(mu |s' - 2ty|), so
 int K(l,v) dv = mu^{-1/2} int f_h(y) 1{(s' - 2ty)/lam > 0} |s' - 2ty|^{-1/2} dy
              = mu^{-1/2} (2|t|)^{-1/2} int f_h(y) 1{y on one side of y0} |y - y0|^{-1/2} dy,  y0 = s'/(2t),
 and by the bathtub principle (0 <= f_h <= 1, int f_h = 1, weight decreasing in |y - y0|) the last integral is
 <= int_0^1 z^{-1/2} dz = 2. So int K(l,v) dv <= sqrt2 (mu |t|)^{-1/2}.
(iii) The density rho of (L,V) is <= 2 and the density m of T = L + beta is <= sqrt2 (Ball; Livshyts-Paouris-
 Pivovarov: k-dimensional projections of product measures with densities <= 1 have density <= 2^{k/2}). Hence for
 each l, int rho(l,v) K(l,v) dv <= min(2 sqrt2 (mu|t|)^{-1/2}, m(t)/(2|t|)) = min(m(t), M(t))/(2|t|) with
 M(t) = min(sqrt2, 4 sqrt2 mu^{-1/2} |t|^{1/2}) (using m <= sqrt2).
(iv) p_Q(s) <= int g(t)/(2|t|) dt with 0 <= g <= M, int g <= 1. The weight 1/(2|t|) decreases in |t|, so by the
 bathtub principle the maximum is at g = M on |t| <= tau, int_{|t|<=tau} M = 1. With t* = mu/16 (where M switches):
 mass on |t| <= t* is sqrt2 mu/12 (< 1 iff mu < 6 sqrt2) and contributes int M/(2|t|) = 2 sqrt2; the rest, height
 sqrt2 on t* <= |t| <= tau with 2 sqrt2 (tau - t*) = 1 - sqrt2 mu/12, contributes sqrt2 log(tau/t*), and
 tau/t* = 1/3 + 4 sqrt2/mu. For mu >= 6 sqrt2 the mass is exhausted inside |t| <= t* and the value is <= 2 sqrt2. []
Check (second way): mu = 1: tau = 1/48 + 1/(2 sqrt2) = .37438, 16 tau = 5.990, value 2[sqrt2 + (sqrt2/2) log 5.990]
 = 5.360 (direct evaluation of the water-filling integral). Numerically the true sup is ~3.62 (Gaussian limit).

Proposition S2 (two hubs, zero hub block, any remainder). H = {h1,h2}, A_HH = 0, the 2 x (n-2) matrix A_{H,H^c} with
singular values s1, s2 > 0. Then ||p_Q||_inf <= 2 sqrt2 (s1 s2)^{-1/2} for every A_{H^cH^c}, every linear term and
all laws (GEOM Prop 5.5 had 1/2 + 8 s^{-2}). For orthonormal hub rows: <= 2.83 (window numerics: 2.27).
Proof. Given X_{H^c}, Q = c1 X_h1 + c2 X_h2 + const with (c1,c2) = 2(T1,T2), and the density of c1 X_h1 + c2 X_h2 is
<= min(1/|c1|, 1/|c2|) (convolution: sup of a convolution <= sup of either factor). (T1,T2) is an affine image of a
2D orthogonal projection of X_{H^c}, so its density is <= D = 2/(s1 s2). So p_Q <= E g(T) with g(z) = 1/(2|z|_inf);
bathtub: density D on the square |z|_inf <= r with 4 r^2 D = 1 gives E g <= (D/2) int_0^r 8 rho d rho / rho = 4 D r
= 2 sqrt D = 2 sqrt2 (s1 s2)^{-1/2}. []

## 13. Family (e) results (famE_opt.py two/pd, famE_cone.py; 03:47-03:50)
Semi-Gaussian optimisation (Nelder-Mead over heavy row rho, eigenvalues, linear terms b, c0; 5 starts each):
 two-sheet side (s <= critical - .002): BEST 3.559 at s = -.0031 (rho = (-.441,.062,.105), leverage .21, b ~ .1);
   Gaussian start 3.549 at s = -.002; the other starts 3.38-3.39. The sup of the two-sheet side sits at the cone.
 definite side: BEST = Gaussian (1,1,1) 2.9033 (s = .0815 ~ 1/12); mixed-leverage starts 2.69-2.87.
Cone study, p at s = -1e-4, -.003, -.01, -.03, -.1, -.2 | +1e-4, +.01, +.05 for (1,1,-1):
 Gaussian              4.079 3.406 2.812 2.012 .938 .401 | 4.240 3.996 3.143
 one heavy lev .9 on the + axis   3.537 3.004 2.516 1.830 .870 .375 | 3.659 3.546 3.109
 one heavy lev .9 on the - axis   3.916 3.412 2.973 2.363 1.324 .468 | 4.039 3.805 2.993
 pair-sum heavy (X0+X1) lev .9, - axis 4.012 3.367 2.804 2.059 1.051 .476 | 4.166 3.926 3.088
 heavy on + and - axes (.6 each) 3.828 3.273 2.775 2.074 1.026 .423 | 3.959 3.775 3.092
A heavy coordinate on the negative direction fattens the two-sheet side AWAY from the cone (s = -.1: .94 -> 1.32)
but lowers the peak at the cone; nothing exceeds the Gaussian cone value 4.24. (1,1,1): heavy coordinates lower
the peak (2.90 -> 2.62 at leverage .9) and move mass outward. With <= 2 heavy coordinates the definite-form sup is
the Gaussian 2.90; the known 3.11 (n = 4, every coordinate heavy) is a small-n effect.
Reason at the cone (heuristic, consistent with the numbers): by the ruled-surface identity p(0) = (pi/sqrt2) x the
average over a circle of planes of the 2D marginal densities at 0; a heavy uniform coordinate replaces part of a
Gaussian marginal by a flat uniform of the same variance, which lowers the peak; only pair sums (triangle, peak
sqrt 2 > 1.38) can raise individual marginals, and not all planes of the circle at once.

## 14. Family (d) non-Gaussian multi-scale and hub-of-hubs (famD_multiscale.py; 03:52)
Hub row w and square direction v with geometric entries r^j (largest entry .17-.37, so every hub-leaf 2x2 minor is
<= .14), random signs, uniform laws, Q = 2 X_h L + V^2: window maxima 3.48-3.57 (E1 3.47-3.60, one E1 spike 3.70 +- .15
that the window value 3.55 does not confirm), n1 = 60, 120, 200 - all below the Gaussian 3.62, no dependence on scales.
Hub of hubs (root hub coupled with weights K^{-1/2} to K sub-hubs, each coupled with weight rho to its own spread
leaf direction, plus V^2): F = 2.54/2.34/1.97 (rho = .3, K = 2/3/6), 1.62/1.31/.94 (rho = 1). Decreasing in K and rho.
Two orthogonal hubs, exact Gaussian value at s = 0: E[1/(2|T|_inf)] = 2.436, against the bathtub bound 2 sqrt2 = 2.828
of Proposition S2 (the bound is within 16 %).

## 15. Second-estimator checks (verify.py, famB_e2.py; 03:55)
- Star + rank one n1 = 100: E2 3.514/3.538/3.524 (+-.05/.044/.040) at s = 0/.002/.004 vs E1 3.477 +- .020 (s = 0),
  3.545 +- .017 (s = .002). Agree.
- Star + Wigner (eps sqrt n = .3), n1 = 50, s = 0/.01/.02/.03: E1 2.847/3.016/3.116/3.066 (+-.02-.04, 8e4 samples),
  E2 2.911/3.105/3.179/3.126 (+-.02-.025, 2e4 samples). E1 sits ~.06-.09 (2-2.7 sigma) below E2: E1 has a heavy right
  tail (weights 1/(2|T|)), so its finite-sample mean is biased low and its SE is optimistic. Headline values below
  are therefore quoted from E2; E1 and the window estimator are used for scans and comparisons only.
- Hub diagonal a = .1 + rank one, n1 = 100: E2 (seed 9) p(0) = 3.705 +- .063; the dedicated E2 scan (seed 11, common
  random numbers across a) gives p(0) = 3.606/3.603/3.596/3.576/3.504 (+- .051) for a = 0/.01/.03/.1/.3, smooth and
  monotone, F = mu_3 max = 3.606/3.585/3.543/3.401/3.018. The 3.705 was a 2-sigma fluctuation; no bump from the diagonal.
- Semi-Gaussian (e) best two-sheet configuration: quadrature 3.552/2.831/2.013 at s = -.0031/-.01/-.03; realised as an
  actual product measure (one heavy row rho, n - 1 spread rows, uniform laws), E2: n = 40: 3.472/2.779/1.976,
  n = 160: 3.592/2.839/2.044 (+-.06/.04/.03). Agrees with the quadrature (n = 40 slightly below: non-Gaussian bulk).

## 16. Law optimisation by alternating best responses (best_response.py, best_response_gs.py; 04:00)
Jacobi version (all leaves at once from one sample) diverges (3.29 -> 3.14 -> 1.77 -> 0): each leaf's partial density
is nearly monotone in its own shift, so simultaneous top-set jumps compound. Documented and replaced by Gauss-Seidel
(one coordinate per fresh sample). Gauss-Seidel, star + rank one, n1 = 8, window estimator (delta .003, noise ~.05):
 uniform start 3.148 -> 3.001 -> 3.098; random multi-interval starts 1.104 -> 2.823 -> 3.191 and .723 -> 2.800 -> 3.104.
Leaves converge to single unit intervals, the hub to an interval of length ~.86 plus histogram-noise fragments.
Best responses reach the uniform-law value and do not exceed it.

## 17. Final summary (04:02)
Largest verified densities F = mu_3 sup_s p (second estimator E2 unless stated):
 (a) star + rank one + eps W: 3.606 +- .051 at eps = 0 (n1 = 100, s = 0); Gaussian limit 3.6207 (exact quadrature);
     every one of nine W types lowers F monotonically in eps sqrt n in [.01, 3]; n1 = 30..1000 flat (3.55-3.58, E1).
     Broad hub + dense remainder (Gaussian model, rank 3): 4.079 - the optimiser gets there only by spreading the hub
     direction, i.e. by turning the configuration into the Gaussian (1,1,-1) form (3 sqrt 2 = 4.2426).
 (b) hub diagonal a: 3.606/3.585/3.543/3.401/3.018 for a = 0/.01/.03/.1/.3 (E2, common random numbers). Decreasing.
 (c) two hubs + hub block: max 2.76 (window, rows at 10 degrees); orthogonal rows 2.27 (window), Gaussian exact 2.436.
 (d) Gaussian spectra at many scales: never above the three-term value (sub-sum lemma); multi-scale hub rows 3.48-3.57;
     hub of hubs <= 2.54; lattice-tuned and bumpy laws (including the twist piece's N13 laws) LOWER the density
     (N13: .29/.11/.04 for N = 2/3/4 while its Fourier L^1 norm grows like 2 pi N).
 (e) convex side, semi-Gaussian with 1-2 heavy coordinates: two-sheet side max 3.559 at s = -.003 (confirmed by E2 on
     real product measures n = 40/160: 3.47/3.59); definite side 2.903 (Gaussian); nothing above the cone value 4.24.
Growth: none, in n, eps, a, hub block, overlap, scales, comb spacing, bump number. Everything rises at most to the
Gaussian limit of its family from below.
Proved: Proposition S (star + rank one + any F(L,V), any laws) <= 2 sqrt2 + sqrt2 log(1/3 + 4 sqrt2/|lam|) (5.36 at
|lam| = 1); Proposition S2 (two hubs, zero hub block, anything else) <= 2 sqrt2 (s1 s2)^{-1/2}; sub-sum lemma for
Gaussian forms; exact window estimator.
Most useful next check: hub + aligned twist + NON-aligned dense bulk with bumpy laws tuned against BOTH the aligned part
and the bulk (the twist piece's open "small non-aligned coupling" regime), measured with E2 - the only configuration
where neither Proposition S nor Theorem D applies and the laws that break the Fourier bound have not been tried
together with a bulk that the laws also try to resonate with.
