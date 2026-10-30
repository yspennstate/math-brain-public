# T262 The infinite depth-and-width limit of unshaped ReLU networks

Lead: unassigned. Dossier written 2026-10-16 by agent A from the auditor's triage (worker L: UNSURE; 2106.04013
is a ResNets paper, its standard-residual analysis is conditional on its Conjecture 5; specify the model and whether the
raw degenerate Gram limit or a rescaled fluctuation law is wanted) and computations in this folder. Overlaps T244 (single
input, the scale) and T255 (shaped networks).

## STATEMENT
Repaired statement. Fully connected ReLU network, He initialization (weight variance 2/n), no bias, width n, depth
L = t n, two fixed inputs at angle theta_0 in (0, pi). The scale of each output is the single-input log-normal (T244). The
raw correlation of the two outputs tends to 1 (degenerate limit), so the question is the rescaled one: show that
phi_L = n * theta_L (theta_L the angle between the two layer-L outputs) converges in law to a nondegenerate random variable
Phi_t, identify its law (a diffusion in the depth variable s = l/n, jointly with the log-norm), and prove convergence; then
the same for p >= 3 inputs (the rescaled shape of the Gram matrix) and for smooth activations at criticality.

## FRONTIER
- Li, Nica, Roy arXiv:2106.04013: log-Gaussian norms for ResNets at L/n = t; the residual case conditional on their
  Conjecture 5; Theorem 1 an exact Gaussian-times-radial representation.
- Li, Nica, Roy arXiv:2206.02768: the neural covariance SDE for SHAPED activations; unshaped ReLU correlations degenerate,
  which is why they shape.
- Hanin, Nica arXiv:1812.05994: single-input log-normal for fully connected ReLU.
- No result found on the rescaled angle of unshaped networks at L ~ n (arXiv search 16 Oct for "infinite depth and width",
  "covariance SDE", "unshaped").

## ARCHITECTURE
Exact reduction (two_input.py): given the layer-l outputs only their two norms and their angle matter; the next layer is
n iid pairs (a1 g, a2 (cos theta g + sin theta g')), g, g' iid N(0, 2/n), through ReLU. The infinite-width angle map for
ReLU gives theta_l ~ 3 pi / l, so at l = s n the angle is of order 1/n and phi = n theta is the natural variable. Per layer
the number of units whose sign differs between the two inputs is about phi/pi (checked: flips/layer = n theta/pi within a
few percent), O(1), and each flip moves phi by O(phi/n); over a unit of s there are of order n flips, so their effect
averages, and the randomness of the limit comes from the multiplicative width-noise of the tangent direction, which
accumulates to O(1) over n layers. The limit should be a diffusion for (log phi, log |h|) in s.

## FAILURE POINT
Identifying the diffusion. The naive candidate d phi = -phi^2/(3 pi) ds + sigma phi dB with constant sigma does NOT fit
(sde_check.py): its drag holds log phi near log(3 pi/s), giving sd log phi 0.54 at s = 1 (sigma^2 = 0.8) against the
measured 0.9, and a mean too high (8.3 against 6.0-6.7). The measured law spreads like sqrt(0.8 s) with no saturation and
sits well below 3 pi/s: the drift and noise must be computed from the exact two-input chain (the conditional law of the
next angle given phi, to order 1/n), including the correlation with the norm (measured corr(log phi, log|h1|) about -0.6).

## SHAPE
Days: compute the one-layer conditional mean and variance of the angle increment at theta = phi/n to order 1/n (an
explicit Gaussian integral over the ReLU pair), write the limiting SDE, check it against two_input_run1.txt; then a proof by
the standard Markov-chain-to-diffusion theorem (the T255 chain has the same structure).

## OBSTRUCTION
A Markov chain on (norms, angle) whose angle is driven to 0 at rate 1/l while width noise is O(1/sqrt n) per layer; the
limit lives on the scale theta ~ 1/n where the drift is singular. Moves: the SDE for phi with the measured law matched; a
proof of convergence in law; the p-input version.

## SETTLED
- Computed 16 Oct (two_input.py, two_input_run1.txt; 400 reps, theta_0 = 1): phi = n theta at L = t n, quantiles
  10/25/50/75/90 and mean log / sd log:
    t 0.25: n 200 13.9 18.4 27.1 35.0 44.1 (3.24 / 0.44);  n 400 15.9 20.2 27.7 35.6 44.3 (3.29 / 0.43)
    t 0.5 : n 200  5.9  8.3 11.9 17.7 27.2 (2.49 / 0.60);  n 400  5.3  7.8 12.0 18.8 25.1 (2.48 / 0.63)
    t 1   : n 200  1.4  2.4  4.6  8.6 15.1 (1.48 / 0.97);  n 400  1.3  2.4  4.4  7.5 11.4 (1.44 / 0.89)
    t 2   : n 200 0.16 0.45 1.03 2.87 5.70 (0.04 / 1.37); n 400 0.17 0.42 1.23 2.90 5.87 (0.05 / 1.45)
  n = 800 (same run, finished 05:1x):
    t 0.25: 17.5 22.9 29.7 39.0 50.5 (3.39 / 0.43);  t 0.5: 5.8 8.2 13.1 19.5 28.0 (2.54 / 0.62)
    t 1   : 1.19 2.34 4.64 8.49 13.17 (1.47 / 0.94);  t 2  : 0.17 0.40 1.00 3.15 5.89 (0.02 / 1.36)
  against the deterministic 3 pi/t = 37.7, 18.8, 9.4, 4.7. The law of n theta has converged in n from t = 0.5 on (the
  n = 800 quantiles sit within the 400-rep noise of n = 200 and 400); at t = 0.25 the centre still drifts up slowly
  (mean log 3.24, 3.29, 3.39), as expected while the initial angle theta_0 = 1 is being forgotten.
  n = 1600 (finished 05:3x): mean log / sd log 3.41 / 0.42, 2.56 / 0.58, 1.49 / 0.92, 0.15 / 1.41 at t = 0.25, 0.5, 1, 2;
  medians 30.6, 13.5, 4.83, 1.30. Converged in n at t >= 0.5 (the t = 2 mean log moves 0.02 -> 0.15, about two standard
  errors of 0.07); at t = 0.25 the drift slows (3.29, 3.39, 3.41).
  Nondegenerate, with sd of log growing like sqrt(0.8 t).
- NOT moves: the raw correlation limit (it is 1); single-input statements (T244); shaped networks (2206.02768).

## TARGETS
1. The limiting SDE for (log phi, log |h|) and a proof that n theta_(tn) converges in law to its solution.
2. Three or more inputs: the rescaled shape of the Gram matrix (angles of order 1/n), whether it is a diffusion on shapes.
3. Smooth activations at criticality (tanh): the angle scale and the limit.

## 18 Oct 06:5x (agent A): the failure point is resolved by T244's diffusion (t244_law_check.py, _run1.txt)
The SDE that fits is the one written and checked in rows/T244 (one-layer generator on the exact kernel, u_generator_n*.txt):
    d log phi = (-1 - phi/(3 pi)) ds + sqrt 2 dB,   phi = n theta,
equivalently u = 1/phi solves the LINEAR equation du = (2u + 1/(3 pi)) ds - sqrt 2 u dB, u(0) = 0, so
    phi_(tn) -> 3 pi / (t A_t),  A_t = (1/t) int_0^t exp(s + sqrt 2 W_s) ds.
The naive candidate above missed two things: the noise is sigma^2 = 2 (the chi-square ratio of the active coordinates, log-variance
2/n per layer), not 0.8, and there is a drift -1 in log phi (log-mean -1/n per layer from the same ratio). Against the n = 800 run
(theta_0 = 1, 400 reps), quantiles 10/25/50/75/90 and mean / sd of log phi:
    t 0.25  limit 18.3 24.2 32.4 42.7 54.1 (3.46 / 0.42)   n = 800  17.5 22.9 29.7 39.0 50.5 (3.39 / 0.43)
    t 0.5   limit  6.0  9.0 13.8 20.6 28.8 (2.59 / 0.61)   n = 800   5.8  8.2 13.1 19.5 28.0 (2.54 / 0.62)
    t 1     limit  1.41 2.62 5.00 8.99 14.5 (1.55 / 0.91)  n = 800  1.19 2.34 4.64 8.49 13.2 (1.47 / 0.94)
    t 2     limit  0.18 0.46 1.23 3.03 6.23 (0.11 / 1.39)  n = 800  0.17 0.40 1.00 3.15 5.89 (0.02 / 1.36)
The spread matches at every t (sd within 0.03); the means sit 0.05-0.09 below the limit, and at t = 0.25 the gap closes with n (mean
log 3.24, 3.29, 3.39 at n = 200, 400, 800 against 3.46). So the law of the rescaled angle is identified. A proof outline (exact Markov
chain in theta, chi-square ratio plus Poisson flips at theta ~ 1/n, entrance from u = 0, Ethier-Kurtz on the linear SDE) is in
rows/T244/DOSSIER.md, 18 Oct. Still open in this row: the joint law with log|h| (the correlation -0.6 measured above), p >= 3 inputs,
smooth activations at criticality (the tanh one-input version is in rows/T250, 2 L q_L -> 1/A_t).

## 19 Oct 22:0x (agent A): the joint law with the norm (joint_check.py, one_layer_cov.py and their _run1.txt)
One layer at theta ~ 1/n, on the active set A (|A| = K ~ n/2), x the radial and y the tangent Gaussians: log|h'|^2 - log|h|^2 =
log(2K/n) + X with X = log(sum_A x^2 / K); log theta' - log theta = (1/2)(Y - X) + O(1/n), Y the same for the tangent part
projected off x. X and Y are independent with variance 2/K = 4/n each, log K has variance 1/n. So per layer
    n Var dlog theta = 2,   n Var dlog|h|^2 = 5,   n Cov = -Var(X)/2 * n = -2,   correlation -2/sqrt 10 = -0.632.
Checked directly at one layer (n 400 and 1600, phi 2 and 10): 1.98-2.12, 4.84-5.04, -1.93 to -2.09. The joint limit is
    d log phi   = (-1 - phi/(3 pi)) ds + sqrt 2 dB1,   phi entering from infinity,
    d log|h|^2  = -5/2 ds + sqrt 5 dB2,                  d<B1, B2> = -(2/sqrt 10) ds,
the norm being the Hanin-Nica log-normal (variance 5 t, mean -5t/2) and the angle the 18 Oct diffusion. The terminal correlation of
log phi_t with log|h_t| is smaller than 0.632 in size because phi's drift is nonlinear: Monte Carlo of the limit gives -0.551,
-0.557, -0.563, -0.574 at t = 0.25, 0.5, 1, 2. Measured in two_input_run1.txt (theta_0 = 1, 400 reps, SE about 0.035 each),
pooled over n = 100-1600: -0.53, -0.53, -0.57, -0.59. Agreement within two pooled standard errors at every t, the two small-t
values still carrying the theta_0 = 1 start. Target 1 of this row (the joint SDE) is identified; the proof outline in
rows/T244 carries over with the 2 x 2 covariance in place of the scalar one. Left: p >= 3 inputs, tanh at criticality.

## 20 Oct 02:1x (agent A): three inputs, the exact net against the mesoscopic model (three_input.py, three_input_run1.txt)
Three unit inputs at pairwise angle 30/n (equilateral), critical He ReLU net of width n, depth t n, 300 nets per cell. The
mesoscopic model runs the triangle of pairwise angles (in units of 1/n) through two moves per layer: the Wishart action
Q -> P^T S P with S = Y^T Pi_x Y / |x|^2 on the K active units (the same chi-square structure that gave the two-input covariance
in the 19 Oct section), then the infinite-width contraction phi -> phi(1 - phi/(3 pi n)) on each side. Statistics: the flatness
r = (a + b - c)/c of the sorted sides (0 = collinear) and log c, the longest side.

    median r, net / model           t 0.5          t 1            t 2
      n 200                          0.313/0.322    0.188/0.212    0.090/0.098
      n 400                          0.288/0.304    0.210/0.210    0.097/0.099
    median log c, net / model
      n 200                          2.32/2.26      1.69/1.52      0.03/0.36
      n 400                          2.32/2.31      1.53/1.55      0.53/0.40

The 10th, 25th, 75th and 90th percentiles of r and the 10th and 90th of log c agree the same way (full table in the run file).
With 300 nets per arm the standard error of a median difference is about 0.02 for r and 0.10-0.15 for log c; every r difference
is within about one of them, and the largest log c gap (n 200, t 2: 0.33, about two standard errors) shrinks to 0.13 at n 400.
So the three-point process is the two-point one applied to every side plus a shared Wishart rotation; no new three-body term
appears at order 1/n. The triangle also flattens with depth (median r 0.3 at t 0.5, 0.1 at t 2): the correlated tangent noise
pulls the three outputs toward a line while the kernel contraction shrinks it, so the angle process for p >= 3 inputs is not
the product of independent pairwise diffusions. The p-input limit to write down and prove is the matrix SDE for the Gram of the
tangent positions under this per-layer law. Left: the matrix SDE's covariance written out and checked at one layer the way
one_layer_cov.py checked the scalar one; tanh at criticality.

## 20 Oct 02:3x (agent A): the one-layer law of the tangent Gram (one_layer_gram.py, one_layer_gram_run1.txt)
For three inputs at angles of order 1/n, write G for the 2 x 2 Gram of the tangent positions of inputs 2 and 3 relative to input 1
(in units of 1/n, from the exact pairwise angles), G' for the same after one critical He ReLU layer, and M = G^(-1/2) G' G^(-1/2).
In the mesoscopic model M has the law of S = W/|x|^2 conjugated by a fixed rotation, with W ~ Wishart_2(K-1, I) independent of
|x|^2 ~ chi-square_K and K ~ n/2. To first order S11 = 1 + w11 - u, S22 = 1 + w22 - u, S12 = w12 with Var w_ii = Var u = 2/K and
Var w12 = 1/K, all independent, which gives
    n Var log(M11/M22) = 8,   n Var M12/sqrt(M11 M22) = 2,   n Var log det M = 24,   cross covariances 0,
and n E log det M = -6 from E log det W = 2 log K - 5/K and E log |x|^2 = log K - 1/K, plus the kernel contraction.
Exact net, 20,000 layers per cell, two triangles (sides about 2 and 6):
    n      triangle             Var log ratio    Var M12n        Var log det      cross covariances
    400    (2,0), (1,1.7)       8.10 +/- 0.08    2.02 +/- 0.02   24.70 +/- 0.25   -0.07..+0.06
    1600   (2,0), (1,1.7)       7.93 +/- 0.08    2.00 +/- 0.02   23.80 +/- 0.24   -0.03..+0.05
    400    (6,0), (-2,3)        8.08 +/- 0.08    2.02 +/- 0.02   24.68 +/- 0.25   +0.01..+0.07
    1600   (6,0), (-2,3)        7.93 +/- 0.08    2.00 +/- 0.02   23.79 +/- 0.24   -0.00..+0.08
The model simulated directly (same statistics, K binomial) gives 7.9-8.1, 1.99-2.03 and 24.1-24.6. The covariance of the Gram
step is confirmed at both widths and both shapes, so the p-input limit is the matrix SDE
    dG = 2 G ds + G^(1/2) dN G^(1/2) - (contraction drift) ds,   dN symmetric, n-scaled covariances Var dN11 = Var dN22 = 8,
    Cov(dN11, dN22) = 4, Var dN12 = 2,
with the contraction acting on each side length as in the two-input diffusion. The drift of log det is not resolved here: with
20,000 layers its standard error is 0.7-1.4 in units of 1/n, and net and model differ by 1.0-2.8 of those units, inside two
standard errors. Pinning it needs about 10^6 layers per cell. Left: that drift check; the proof (the T244 outline with this 3 x 3
covariance); tanh.

## 20 Oct 04:1x (agent A): Target 3, critical tanh - no degeneration, the angle is a Fisher-z diffusion (tanh_one_layer.py, tanh_two_input.py)
Critical tanh (W ~ N(0, 1/n), no bias). Unlike ReLU, the two-input correlation does NOT go to 1. For small q,
    E tanh u tanh v = q c (1 - 2q + 5q^2 + (2/3) q^2 c^2) + O(q^4),   so   c' = c - (2/3) q^2 c (1 - c^2) + O(q^3),
and with q_l ~ 1/(2l) the total movement is summable: c_l -> c_inf(theta0) < 1. At theta0 = 1 (q0 = 1), from the exact Gaussian map:
c_l = 0.5120, 0.5013, 0.4900, 0.4848, 0.4795, 0.47893 at l = 1, 2, 5, 10, 100, 1000; c_inf = 0.478868 (theta_inf = 1.0714). Past the first
few layers the network is linear to leading order, so the 2 x 2 Gram is a Wishart chain. The Fisher z = atanh(c) of each layer's sample
correlation of n iid pairs moves by tanh(z)/(2n) in mean and 1/n in variance. Prediction at L = t n:
    dz = (1/2) tanh z ds + dB,   z_0 = atanh(c_inf(theta0)),
i.e. the angle is O(1) and random; for large z, log theta ~ -z, a drift of -t/2 with variance t. That is the Lyapunov gap 1/(2n) of real
Ginibre products, half the ReLU rate (ReLU's active set is n/2).
One-layer checks (tanh_one_layer_run1.txt, n = 100, 2e6 reps, linear twin on the same Gaussians):
- The expansion's relative error is 2e-3 at q = 0.05 and 1.3e-4 at q = 0.02, a ratio of 14 for q^3's 15.6, so the error is O(q^4) absolute.
- n Var dz = 1.017-1.022, against n/(n-2) = 1.020.
- tanh minus the linear twin, n E dz: -0.0018 / -0.0044 at q = 0.01, c = 0.3 / 0.8 (predicted -(2/3) q^2 c n = -0.0020 / -0.0053);
  -0.00002 / -0.00006 at q = 0.001 (predicted -0.00002 / -0.00005); standard errors 1e-5 to 1.4e-4.
- Linear twin n E dz: 0.146, 0.396, 0.175, 0.412 against tanh(z)/2 = 0.15, 0.40, 0.15, 0.40, with se 0.007.
The nonlinearity enters only at O(q^2), which is O(1/l^2) and summable.
Net against the limit (tanh_two_input_run1.txt, exact rotation-invariant reduction, theta0 = 1, 2,000 reps): limit z mean/sd at
t = 0.25, 0.5, 1, 2: 0.582/0.522, 0.635/0.766, 0.735/1.162, 0.916/1.814. At n = 200, t = 0.25 the net reads 0.570/0.520 (se 0.012),
with quantiles within 0.04 of the limit. A smoke test at n = 50 (200 reps) matched the sd at every t; there the means sat 0.06-0.12
high. The full runs (2,000 reps each):
    n     t 0.25         t 0.5          t 1            t 2          (net mean/sd; limit above)
    200   0.570/0.520    0.621/0.770    0.725/1.159    0.896/1.806
    400   0.550/0.538    0.610/0.769    0.719/1.153    0.952/1.822
The sd matches the limit within 0.02 in all eight cells. The means differ by 1.0, 0.8, 0.4, 0.5 se at n = 200 and 2.7, 1.5, 0.6, 0.9 se
at n = 400 (se 0.012-0.041). Seven of the eight differences are negative, but the offset does not shrink from n = 200 to 400 and the
four t values share paths, so this reads as noise, not a 1/n correction. Target 3 holds at the level of these runs: under critical tanh
the angle stays O(1) and follows the Fisher-z diffusion.

## 20 Oct 05:0x (agent A): Target 2, the drift of log det after one layer (one_layer_drift.py, one_layer_drift_run1.txt)
n E log det M after one critical He ReLU layer, three inputs at tangent positions 0, p2, p3 (units 1/n), 10^6 layers per cell.
The model has two parts. The Wishart part is exact given K: psi((K-1)/2) + psi((K-2)/2) - 2 psi(K/2), with K ~ Bin(n, 1/2), about -6/n.
The side contraction is D -> D (1 - D/(3 pi n)) at the input distances. The model is computed without sampling.
    shape (p2; p3)      n     net             model     (Wishart, contraction)   (net - model)/se
    (2,0; 1,1.7)        200   -6.9296 0.0699  -6.9856   (-6.1443, -0.8414)       +0.80
                        400   -6.9586 0.0985  -6.9122   (-6.0710, -0.8411)       -0.47
                        800   -6.9775 0.1389  -6.8763   (-6.0353, -0.8410)       -0.73
    (6,0; -2,3)         200   -6.1581 0.0698  -6.2721   (-6.1443, -0.1279)       +1.63
                        400   -6.2147 0.0984  -6.1891   (-6.0710, -0.1181)       -0.26
Chi-square 4.13 on 5 cells (p about 0.53). The shape (6,-2,3) cell at n 800 was cut by the 5,000 s timeout and is not run.
Both shapes share the same Wishart term, so the difference between them isolates the contraction term. That difference is measured
at 0.771 +/- 0.099 (n 200) and 0.744 +/- 0.139 (n 400), against a model value of 0.713 and 0.723. That is 7.8 and 5.3 se away from
zero and 0.6 and 0.15 se from the model. The two shapes ran on the same random stream, so these se overstate the noise in the
difference. So both parts of the one-layer drift are confirmed. The Wishart -6/n term is fixed by the Gram law (02:3x). The
contraction is the geometric term D^2/(3 pi n), which only the angle map contributes. Together with the covariance (02:3x) this
gives the one-layer generator of log det M to O(1/n). What remains for Target 2 is the proof, via the T244 outline: compose layers,
control the error, and pass to the diffusion limit.
