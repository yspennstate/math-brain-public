# T357 Overconfidence of overparameterized classifiers

Lead: unassigned. Dossier written 2026-10-16 by claude-99aebc7f from the row and the arXiv records below (abstracts read 16 Oct
08:3x, the 16 Oct 07:07 audit (status PARTLY, calibration diagnostic)).

## STATUS (20 Oct 17:34, claude-99aebc7f)
Linear model (logistic regression on the Gaussian single-index teacher, proportional regime), leading order in 1/alpha:
- Ridge: the risk optimum and FM = 0 coincide (FM = 0 is the rescaling first-order condition), and OC = 0 needs more ridge,
  lam_OC/lam_risk > 1 at every beta > 0: 1.007 at beta 1, 1.029 at beta 2, rising to 1.093 as beta -> inf (and to 1 as beta -> 0). Proved given the CGMT fixed point, which
  reduces to the classical constants by an implicit-function argument (05:5x and 11:4x sections).
- Gradient descent from 0: the late path is a rescaling of the MLE (the Hessian's slow direction tilts into w_perp by exactly
  1/beta), so again t_risk = t_FM and OC = 0 comes first, by ln(lam_OC/lam_FM)/i_par (0.473 at beta 2). Measured 0.408 +- 0.025 at
  alpha 40; path slope 2.0-2.2 against the radial 2.06 (12:09 and 12:2x sections).
- So in the linear case the joint calibration-risk objective gains little: a risk-tuned stop is FM-calibrated and leaves an
  O(1/alpha) OC over-confidence; an OC-calibrated stop costs O(1/alpha^2) risk.
  The alpha 160 spread is kappa_hat's sampling noise read through a log (13:1x note in the 12:09 section): the crossings' kappa
  distance is steady across seeds (cv 0.06) while the time gap is not; the limit is d -> inf first.
Random features (the row's target), at n = inf under Gaussian equivalence (13:4x and 17:0x sections, 20 Oct):
- The RF logistic model is misspecified: the teacher seen through the features is z* = b s + tau Z, link E sigma(b s + tau Z). The
  risk optimum is still FM = 0 but OC > 0 there, of order 1 in alpha: at most 0.0035 (beta 5, N/d 1), fading as N/d grows. So on
  ridge lam_OC/lam_risk grows without bound in alpha, unlike the linear model's 1.007-1.093.
- The over-confident sign is PROVED (17:34): a one-crossing lemma plus the star order of logistic + tau Z against the logistic, which
  follows from the logistic being a normal scale mixture and a TP2 kernel. Real tanh features match the GE size (OC_inf about 0.003).
- This effect is two orders too small to explain the 19 Oct finite-n table (alpha 3), which is a finite-alpha effect.
OPEN: the finite-alpha RF constant (fixed point written 17:25, sweep running); GD's finite-alpha
corrections at d -> inf, and rigour for the GD path beyond the linearisation at the MLE.

## STATEMENT
Repaired statement (the audit: use the source's score-conditional definition of over-confidence, state the regime where the
MLE exists, choose the network class, initialization, signal scaling and a population calibration metric other than binned
ECE; early stopping must also meet a risk target): for one Gaussian single-index teacher P(y = 1 | x) = sigma(beta <w*, x>)
and random-feature logistic regression (N features, ridge lambda or gradient-flow time t, n/d and N/d proportional), derive
the population score-calibration curve E[y | p_hat = p] - p and the excess risk along training, and decide whether a stopping
time improves a joint calibration-risk objective.

## FRONTIER
- Bai, Mei, Wang, Xiong arXiv:2102.07856: unregularized logistic regression in the proportional regime is over-confident.
- Clarte, Loureiro, Krzakala, Zdeborova arXiv:2202.03295: uncertainty in high-dimensional linear classification; ERM vs
  Bayes calibration; regularization tuned for calibration.
- Audit diagnostic: in the scalar population flow with 0 < b(0) < beta the model stays under-confident until it reaches
  beta; a constant predictor is calibrated, so a calibrated stopping time alone is vacuous.
- Open: random-feature and feature-learning networks.

## ARCHITECTURE
Random features with Gaussian equivalence reduce the RF logistic ERM to a generalized linear model in a Gaussian design with
an extra noise term; the CGMT fixed point of 2102.07856 / 2202.03295 then gives the joint law of (true score, fitted score),
from which the calibration curve follows.

## FAILURE POINT
Gaussian equivalence for RF logistic regression holds for ERM at fixed lambda; along gradient-flow time it needs a dynamical
equivalence (DMFT), which is not rigorous in this setting.

## SHAPE
Days: ridge-path version (lambda as the proxy for training time), by Gaussian equivalence plus CGMT.

## OBSTRUCTION
Time dependence. Moves: use the ridge path as the time proxy (known equivalence of gradient flow and ridge for squared loss
does not hold for logistic loss; state it as a separate result).

## TARGETS
1. RF logistic ERM, fixed lambda: the calibration curve as a function of (n/d, N/d, lambda, beta); the lambda that
   minimizes calibration error subject to excess risk at most a stated level.

## 19 Oct (claude-99aebc7f): Target 1, linear-feature case - the calibrating lambda and the risk-optimal lambda nearly coincide
Setup (calib_path.py, calib_cross.py): teacher P(y=1|x) = sigma(beta <w*, x>), x ~ N(0, I_d), n = alpha d, logistic ridge with
penalty lam/2 |w|^2, L-BFGS warm-started down a 49-point log grid 1e-4..30. No binning: for any linear predictor zhat = w.x the pair
(z*, zhat) is jointly Gaussian with q = |w|, c = w.w*, so the population calibration curve is exact,
  E[y | zhat = s] = E sigma(beta z*),  z* | s ~ N((c/q^2) s, 1 - c^2/q^2),
and CE = E|E[y|p] - p|, the signed over-confidence OC = E[(p - E[y|p]) sign(p - 1/2)] and the excess risk over Bayes are
Gauss-Hermite integrals (80 nodes) in (q, c). lam_cal = the sign change of OC (log-linear root), lam_risk = argmin of the
excess risk (parabola in log lam). d = 400, 4 seeds, medians (calib_cross_run1.txt):
  alpha  beta   lam_cal   lam_risk  ratio   excess at lam_cal / min   CE at lam_risk   OC at lam 1e-4
  3      2      0.111     0.110     1.009   0.11105 / 0.11098         0.0068           +0.285
  1      2      0.430     0.420     1.024   0.18061 / 0.18053         0.0030           +0.338
  0.5    2      0.875     0.872     1.004   0.20148 / 0.20143         0.0019           +0.332
  10     2      0.0286    0.0279    1.025   0.04225 / 0.04219         0.0025           +0.066
  3      1      0.387     0.383     1.010   0.06434 / 0.06425         0.0065           +0.264
  3      5      0.0280    0.0248    1.131   0.16025 / 0.15942         0.0116           +0.191
  1      5      0.154     0.136     1.129   0.32025 / 0.31964         0.0083           +0.247
Read. (1) Below lam_cal the fit is over-confident, above it under-confident; the near-interpolating fit (lam 1e-4) is
over-confident at every setting (the 2102.07856 effect). (2) lam_cal sits within 1-3 percent of lam_risk at beta <= 2 and
13 percent above it at beta = 5 (every seed's ratio > 1 there: 1.07-1.28), so calibrating costs at most 0.0008 of excess risk on
this grid. (3) The coincidence is not exact and not forced: at lam_risk the first-moment calibration E[(p - E[y|p]) zhat], which
vanishes when the SCALE of a fixed direction is risk-optimal, is +0.006 / +0.012 at beta 2 / 5, because ridge moves direction
and scale together. This agrees in kind with Clarte, Loureiro, Krzakala, Zdeborova arXiv:2210.12760 (optimally regularized
estimators are not calibrated in general; trade-off between accuracy and calibration), read 19 Oct, abstract only.
CONSEQUENCE for the row's question: in the linear case a stopping/regularization rule chosen for risk is already within CE 0.012
of calibrated, and a rule chosen for calibration loses under 0.001 risk; the joint objective gains little over either.
OPEN, the next moves: (a) prove lam_cal > lam_risk for beta large (sign seen at beta 5, both alpha) [20 Oct: proved for the OC measure at every beta > 0, at leading order in 1/alpha, given the CGMT fixed point; see the 05:5x section]; (b) DONE: at d = 800 (alpha 3,
beta 5, 2 seeds, calib_cross_d800.txt) lam_cal / lam_risk = 1.152 (seeds 1.18, 1.12), so the beta-5 gap is not finite-size; (c) the random-feature case, the row's real target.

19 Oct 06:0x (claude-99aebc7f): Target 1, random-feature case, first numerics (rf_cross.py). zhat = a . tanh(F x), F rows
N(0, I/d), d = 200, n = 600, beta 2, logistic ridge in a, 33-point lambda grid. q^2 = E zhat^2 and c = E zhat z* are estimated on
fresh points (200k, capped at 3e7/N for memory) and put into the Gaussian-equivalence (GE) formula of calib_path.py. The same points
give a binned check (40 quantile bins). GE and binned CE agree to about 0.001 everywhere, and their lam_cal agree to 1-2 percent
(rf_cross_run1.txt), so the (q, c) formula is usable for random features at this size.
  N/d    0.5          1            2            3 (N = n)    4            8
  lam_cal / lam_risk per seed (GE):
         1.13 1.11 1.57  1.23 1.68 1.33  1.15 1.28 1.25  1.14 1.18 1.18  1.09 1.01 1.19  1.05 1.06 1.11
The calibrating lambda sits above the risk-optimal one in all 18 fits, with ratio 1.0-1.7, against 1.00-1.03 for the linear
predictor at the same beta. The gap is widest at N/d 1-2 and narrows past interpolation (1.05-1.11 at N/d = 8). Both lambdas grow
with width (lam_risk 0.05-0.09 at N/d <= 1, 0.27-0.29 at N/d = 8). The cost of calibrating is small because the risk is flat near
its minimum. From the median curves at N/d = 1 and 3 (rf_cross_tables.txt, printed grid about 2x per step, so rough): excess risk
0.1553 at lam_cal against 0.1541 at the grid minimum, and 0.1222 against 0.1217; CE at the risk minimum 0.005.
NEXT: refine the grid near the two lambdas, add seeds, and check the 1.7 outliers. Then the question the row asks: does early
stopping of gradient flow track the ridge path for calibration (it does not have to for logistic loss)?

19 Oct 06:2x (claude-99aebc7f): the row's own question, early-stopped gradient descent against the ridge path (linear predictor,
gd_cross.py). GD on the unregularized logistic loss from w = 0, step 0.1 (gd_cross_eta01.txt; the step-1 run gd_cross_run1.txt is
too coarse in time at alpha 1). d = 400, 4 seeds, medians. Times are steps x step size.
  alpha beta  time_cal/time_risk  q_cal GD / ridge  GD excess at t_cal / GD min / ridge min  CE at t_risk  max|c_GD - c_ridge| at same q
  3     2     5.41/5.90 = 0.92    1.165 / 1.174     0.11200 / 0.11182 / 0.11098            0.0072        0.030
  1     2     1.67/1.70 = 0.98    0.676 / 0.684     0.18150 / 0.18146 / 0.18053            0.0022        0.084
  3     5     17.0/22.2 = 0.76    2.419 / 2.489     0.16677 / 0.16474 / 0.15942            0.0186        0.031
  10    2     14.2/15.1 = 0.94    1.651 / 1.659     0.04322 / 0.04301 / 0.04219            0.0039        0.006
Read. (1) GD crosses from under- to over-confident shortly BEFORE its risk optimum, at every setting. That is the same side as
ridge, where lam_cal > lam_risk also means a smaller norm. So on both paths the calibrated fit is a slightly shrunk version of the
risk-optimal one. (2) The calibrated NORM is nearly the same on the two paths (within 1-3 percent), although at a given norm GD's
alignment c differs from ridge's by up to 0.08 (alpha = 1). Calibration seems to be set mainly by the norm. (3) Early stopping is
worse than optimal ridge for risk by 0.0008-0.0053, the largest gap at beta 5, and it is less calibrated at its own optimum
(CE 0.002-0.019). (4) Stopping at calibration costs 0.00004-0.002 of excess risk.
CONSEQUENCE: in the linear Gaussian case the joint calibration-risk stopping question has a small, measurable answer: stop at
t_cal, lose at most about 0.002 of risk. The gap grows with signal strength beta. No proof yet. A candidate route: show that OC and
the scale-derivative of the risk change sign at nearby norms, with a gap of order the alignment deficit 1 - c/q.

19 Oct 06:4x (claude-99aebc7f): why the calibrated fit sits just before the risk optimum. An exact identity, checked on both paths
(path_lemma.py, path_lemma_run1.txt, path_lemma_run2.txt).
IDENTITY. For a linear predictor zhat = w.x with q = |w| and c = w.w*, zhat ~ N(0, q^2) whatever its direction, and Stein gives
E[y zhat] = c kappa_beta with kappa_beta = E[sigma(beta g) g]. So the population logistic risk is
  R(q, c) = A(q) - kappa_beta c,     A(q) = E softplus(q g),   g ~ N(0, 1)
(checked against the Gauss-Hermite risk to 1e-11). Note A'(beta) = kappa_beta. Two consequences.
(a) The first-moment calibration FM := E[(sigma(zhat) - y) zhat] equals q A'(q) - kappa_beta c = q dR/dq at fixed c/q, so FM = 0
exactly when the scale is risk-optimal for the direction. In terms of rho = c/q, FM = 0 iff A'(q) = rho A'(beta), i.e.
  q_cal(rho) = (A')^{-1}( rho A'(beta) ),
one function for every training path (A' is increasing). At beta = 2, q_cal(0.74) = 1.13 and q_cal(0.76) = 1.18. This is why ridge
and GD calibrate at nearly the same norm (1.174 and 1.165, gd_cross_eta01.txt): they reach the calibration point at nearly the same
alignment. The earlier reading "calibration is set by the norm alone" should be read as "by the norm given the alignment".
(b) PATH LEMMA. Along any path with q increasing (ridge as lambda decreases, GD as time increases), at a stationary point of R,
A'(q) = kappa_beta dc/dq, hence
  FM at the risk optimum = kappa_beta q^2 d rho / d q   (exact).
So the risk-optimal fit is over-confident in the first-moment sense, and the calibrating lambda lies above the risk-optimal one
(the calibrating GD time below the risk-optimal time), EXACTLY when the alignment is still improving along the path at the risk
optimum. The size of the miscalibration is the alignment slope times kappa q^2. The identity uses only joint Gaussianity of
(z*, zhat), so it also holds for random features in the Gaussian-equivalence approximation used in rf_cross.py. There the 18 of 18
fits with lam_cal > lam_risk say the alignment was still rising at every RF risk optimum. Direct look at the median tables
(rf_cross_tables.txt, grid about 2x per step): at N/d = 1, rho = c/q peaks at lambda 0.0154 (0.653), well below lam_risk
0.054-0.057 (rho 0.621 at the grid risk minimum), consistent with the large ratios 1.23-1.68 there. At N/d = 3 the peak and the
risk minimum fall on the same grid point, too coarse to read.
CHECK (d = 400, 3 seeds per setting; optimum located by a quadratic fit in log(time), d rho/dq by a quadratic fit of rho on q,
7 points). FM at the optimum against kappa q^2 drho/dq, GD: +0.0054/+0.0056, +0.0085/+0.0087, +0.0097/+0.0099 (alpha 3, beta 2);
+0.0219/+0.0220, +0.0327/+0.0328, +0.0277/+0.0279 (alpha 3, beta 5); GD cases with |FM| > 0.001 within 0.0003 (alpha 0.5: 0.0006). Ridge:
+0.0069/+0.0076, +0.0177/+0.0183, +0.0120/+0.0128 (alpha 3, beta 5); ridge cases within 0.0008, from the coarser 90-point lambda grid.
Signs agree in every case with |FM| > 0.001. The cases where they disagree all have |FM| < 0.001 (alpha 0.5 and beta 1, where the
alignment is flat at the optimum) and are within the fit error. Across 7 settings: the alignment is still rising at the optimum
in all 21 GD cases and in 18 of 21 ridge cases. The three ridge exceptions are slightly falling (kappa q^2 drho/dq =
-0.0017 at alpha 10 beta 2, -0.0009 at alpha 3 beta 1, -0.0003 at alpha 0.5). So lam_cal < lam_risk does happen, and only where the gap is
negligible. Two empirical facts the lemma turns into one question: GD's FM at its optimum (median over seeds) is larger than
ridge's at every setting except alpha 0.5, where both are within 0.001 of zero. GD stops while the alignment is still rising: its
rho peaks at 1-20 times t_risk, median about 3. The gap grows with beta.
WHAT REMAINS FOR A THEOREM: sign(d rho/dq) at the risk optimum. For ridge this is a statement about the CGMT fixed point of
logistic ridge (2202.03295): show that the alignment-maximizing lambda lies below the risk-optimal lambda when beta is large.
For GD from 0 it needs the DMFT or a two-timescale description (signal direction learned fast, noise directions slower).
NOVELTY: the decomposition R = A(q) - kappa c is elementary and very likely known in some form. The path lemma, which reduces
the calibration-versus-risk question on any path to the sign of the alignment slope, was not seen in the abstracts read
(2102.07856, 2202.03295, 2210.12760). That is not a literature check.

19 Oct 06:4x (claude-99aebc7f): a large-alpha look at sign(drho/dq) for ridge. A heuristic, partly checked, and not a proof.
Delta method for alpha -> infinity: the ridge solution is r(lam) w* plus perpendicular noise, where r solves the population
equation kappa_beta - A'(r) = lam r. The noise has squared norm g(r)/(alpha (h(r) + lam)^2), with h(r) = E sigma'(r g) the
perpendicular Hessian and g(r) = E[(y - sigma(r z*))^2] the gradient variance. Hence
  1 - rho^2 ~ g(r) / (alpha r^2 (h(r) + lam)^2),   L(lam) := log of the right side times alpha.
(Check: alpha 10, beta 2 gives rho 0.926 at lam 0, against the measured 0.92-0.93 at the risk optimum.) The derivative in lam
CANCELS to first order at lam = 0. Three facts give this: g'(beta) = 0 (well-specified model, g(beta) = h(beta)), r'(0) = -beta/A''(beta),
and A'' = h + q h' (Stein: A'(q) = q h(q)). Together dL/dlam(0) = (2 + 2 beta h'/h)/A'' - 2/h = 0. Numerically,
dL/dlam is 0.0016, 0.014, 0.82 at lam = 1.5e-4 and 0.089, 0.58, 6.75 at lam = 0.01, for beta = 1, 2, 5. So dL/dlam ~ C_beta lam with
C_beta about 9, 58, 675, growing fast with beta.
READ. To leading order the alignment is flat at lam = 0, and the population term makes it fall for small lam > 0. So it is
still rising (as lam decreases) at any small lam_risk, which gives lam_cal > lam_risk, with a gap that grows with beta through
C_beta. But FM at the optimum is then a second-order quantity, O(lam_risk / alpha). The finite-alpha inflation of the logistic
estimator (Sur-Candes) enters at that same order and is NOT computed here, so the sign is not settled by this argument. Quantitative
check: the population term alone predicts FM_opt ~ C_beta A''(beta) lam_risk / (2 alpha) = 0.022 at alpha 3, beta 5 (measured
0.007-0.018, right order), but 0.064 at alpha 3, beta 2 (measured 0.001-0.003, twenty times too big). So at beta 2 something
else, most likely the inflation term or lam_risk = 0.11 being outside the small-lam range, cancels most of it. What the
cancellation does explain is why the calibration gap is small at all: the leading term vanishes. The next step is the
second-order term with the CGMT fixed point of 2202.03295, which carries the inflation exactly.

19 Oct 17:0x-18:3x (claude-99aebc7f): the exact proportional-limit fixed point settles the ridge sign, and it changes with alpha.
cgmt_ridge.py solves the leave-one-out (CGMT) system for logistic ridge at n/d = alpha. With Q = mu Z1 + s Z2, P = prox_{c rho_y}(Q),
rho_y(t) = softplus(t) - y t, the three equations are
  lam mu = -E[Z1 rho'_y(P)],   1/alpha = 1 - E[1/(1 + c rho''(P))] + lam c,   s^2 = alpha c^2 E[rho'_y(P)^2],
then q = sqrt(mu^2 + s^2), rho = mu/q, and the population risk and FM as in calib_path.py (Gauss-Hermite, 80 nodes by default).
Checks: on ridge regression the same system gives |w|^2 = s^2/(alpha - 1) at lam 0 and the population ridge at alpha -> inf. A
direct fit at d = 2000 (cgmt_check_direct_run1.txt) gives q 1.199 against 1.1918 and rho 0.7647 against 0.7651.
--refine finds lam_risk (risk minimum), lam_rhomax (alignment maximum) and lam_cal (FM = 0) to 1e-10 in log lam.
RESULTS (cgmt_ridge_run2.txt, run3.txt). sign(FM at lam_risk) = sign(drho/dq at lam_risk) in all 16 settings, as the path
lemma says. lam_cal/lam_risk:
  beta 5:  alpha 3 1.038,  10 1.001,  15 0.9984,  20 0.9978,  25 0.9978,  30 0.9978 (0.9980 with 140 nodes),  40 0.9980,  60 0.9980
  beta 2:  alpha 1.5 1.008,  3 1.006,  10 1.0004,  30 0.9996,  100 0.9998
  beta 1:  alpha 3 1.0007
So for ridge, lam_cal > lam_risk at small alpha and lam_cal < lam_risk at large alpha. The sign change lies between alpha 10 and 15
at beta 5 and between 10 and 30 at beta 2. Beyond it the gap is tiny: at most 0.22 pct in lam, with |FM| below 1e-4.
The finite-d ridge exceptions in the CHECK above (alpha 10 beta 2, alpha 3 beta 1) are NOT this effect. In the limit both are
slightly positive (1.0004, 1.0007), so those were seed noise on a 90-point grid. The 06:4x large-alpha heuristic predicted a
positive sign at large alpha. The exact system says the opposite, so the term that heuristic left out (the finite-alpha
inflation) wins at large alpha, as its own READ feared. The quadrature check at alpha 30, beta 5 moves FM from -6.1e-5 to -5.7e-5
and keeps the sign.
WHAT THIS MEANS FOR TARGET 1. The conjecture "the calibrating lambda exceeds the risk-optimal one" is false for ridge in general.
It holds at small alpha (where the gap is a few percent at beta 5) and fails, by a negligible margin, past alpha_c(beta). GD is a
different path: its FM at the optimum is larger and was positive in 21 of 21 finite-d cases. The GD statement needs its own limit
(DMFT) and is still open. Next: bracket alpha_c(beta) more tightly (cgmt_ridge_run4.txt: alpha 11-14 at beta 5, 12-20 at beta 2,
10 and 30 at beta 1) and see whether alpha_c grows or shrinks with beta.

19 Oct 18:5x (claude-99aebc7f): alpha_c(beta) bracketed (cgmt_ridge_run4.txt, GHN 80, every point --refine).
  beta 5: lam_cal/lam_risk = 1.00015 (alpha 11), 0.99948 (12), 0.99899 (13), 0.99863 (14)      -> alpha_c(5) in (11, 12)
  beta 2: 1.00009 (12), 0.99983 (15), 0.99966 (20)                                             -> alpha_c(2) in (12, 15)
  beta 1: 1.00029 (10), 1.00001 (30)                                                           -> alpha_c(1) > 30, just above
In all nine points sign(lam_cal/lam_risk - 1) = sign(drho/dq at lam_risk), the path-lemma prediction, with drho/dq of order 1e-6 to 1e-5
near the crossing. alpha_c grows as the signal strength beta falls. The size of the effect stays below 0.15 pct in this range.

19 Oct 20:5x (claude-99aebc7f): beta 1 closed off (cgmt_ridge_run5.txt, GHN 80, --refine).
  beta 1: 1.00001 (alpha 30, run4), 0.99999 (40), 0.99998 (60), 0.99998 (100)   -> alpha_c(1) in (30, 40)
sign(lam_cal/lam_risk - 1) = sign(drho/dq) again at all three new points. So alpha_c(5) in (11, 12), alpha_c(2) in (12, 15),
alpha_c(1) in (30, 40): the crossing moves out as beta falls. Past it the gap is at the 1e-5 level in lambda at beta 1.

20 Oct 00:4x (claude-99aebc7f): large alpha (cgmt_ridge_run6.txt at GHN 80, cgmt_ridge_run7.txt at GHN 160 and 240, all --refine).
  beta 2, GHN 80:  lam_cal/lam_risk = 0.99990 (alpha 200), 0.99995 (400), 0.99998 (1000); lam_rhomax/lam_risk 1.028, 1.029, 1.030
  beta 5, GHN 80:  0.99737 (100), 0.99596 (200), 0.99467 (400); lam_rhomax/lam_risk 1.24, 1.49, 1.42
  beta 5, GHN 160: 0.99913 (100), 0.99970 (400)
  beta 5, GHN 240: 0.99914 (100), 0.99976 (400)
At beta 5 the GHN-80 values drift away from 1 and the alignment maximum jumps about, and both are quadrature error: with 160 and
240 nodes the ratio agrees to four digits at alpha 100 and to 6e-5 at alpha 400, and it moves toward 1. So past alpha_c the gap
closes like c_beta/alpha, with alpha (1 - lam_cal/lam_risk) about 0.02 at beta 2 (0.020, 0.020, 0.020) and about 0.09-0.10 at
beta 5 (0.086 at alpha 100, 0.096 at 400). The sign stays negative, as drho/dq at lam_risk says (-9.1e-7 at alpha 100, -6.3e-8 at
400). lam_rhomax/lam_risk is NOT resolved at beta 5: it moves from 1.121 to 1.094 between 160 and 240 nodes at alpha 400, because
rho is flat near its maximum (rho = 0.99933 there). Only the calibration ratio is quoted.
CAVEAT FOR THE EARLIER TABLES. The beta 5 runs at alpha <= 60 used 80 nodes and were checked at 140 nodes only at alpha 30
(0.9978 -> 0.9980). The bracket alpha_c(5) in (11, 12) sits where 80 nodes were adequate (|FM| ~ 1e-5 and the sign agrees with
drho/dq at every point), but the values at alpha 40-60 may carry the same small downward bias seen at alpha 100.
Ridge picture as of now: lam_cal > lam_risk for alpha < alpha_c(beta), lam_cal < lam_risk beyond it, and the gap tends to 0 like
1/alpha. Target 1 for ridge is therefore false as stated but true to O(1/alpha); the GD statement is still open.
20 Oct 01:1x (claude-99aebc7f): the 80-node values at alpha 40-60 re-checked with 160 nodes (cgmt_ridge_run8.txt), beta 5:
lam_cal/lam_risk 0.99825 (alpha 40, was 0.9980 at 80 nodes) and 0.99868 (alpha 60, was 0.9980). The sign is unchanged and the
bias was about 2.5e-4 and 7e-4. With the 160/240-node values, alpha (1 - lam_cal/lam_risk) at beta 5 is 0.070, 0.079, 0.086,
0.096 at alpha 40, 60, 100, 400: a slow climb toward a constant near 0.1, so the 1/alpha law holds up to that drift.

## 20 Oct 02:3x (claude-99aebc7f): GD past the ridge crossover (gd_cross.py, gd_cross_largealpha.txt)
Ridge changes side at alpha_c(beta) (alpha_c(5) in (11, 12), alpha_c(2) in (12, 15)): beyond it the calibrating lambda is below
the risk-optimal one. GD from w = 0, step 0.1, d 400, 4 seeds, was run at three points past those crossings:
    alpha  beta  time_cal/time_risk   GD excess at t_cal / GD min / ridge min   q_cal GD / ridge   max|c_GD - c_ridge| at same q
    30     2     0.970                0.01587 / 0.01583 / 0.01572               1.865 / 1.867      0.0028
    20     5     0.919                0.02423 / 0.02418 / 0.02417               4.405 / 4.407      0.0055
    40     5     0.954                0.01292 / 0.01291 / 0.01291               4.664 / 4.664      0.0031
GD still calibrates before its risk optimum at all three: it does not cross where ridge does. With the four earlier cells
(alpha 1-10) the GD ratio is below 1 in six of seven step-0.1 cells, and 1 - ratio falls roughly like 1/alpha at beta 5
(0.236, 0.081, 0.046 at alpha 3, 20, 40) and more slowly at beta 2 (0.059, 0.030 at alpha 10, 30). The two paths reach the
calibration point at the same norm to 0.1 percent and their coefficient curves agree to 0.006 at equal norm, so the side GD
sits on is set by where its own risk minimum falls along the path, consistent with the path lemma (GD's alignment is still rising
at its optimum). The cost of stopping at calibration instead of the risk optimum is under 0.3 percent of the excess risk in every
cell. Caveat: four seeds at d 400, and the risk is flat near its minimum (0.04 percent between t_cal and t_risk at alpha 40), so
the location of t_risk carries finite-d noise that these runs do not measure. The GD statement (calibration before the optimum,
gap O(1/alpha)) is now the empirical picture; its limit still needs the DMFT description.

## 20 Oct 04:5x (claude-99aebc7f): which calibration measure (audit 1, claude-5693aca3, audit_5693aca3/, push 6890fe6e)
The audit confirms the CGMT system (re-derived by Sherman-Morrison) and reproduces the FM roots with an independent trapezoid
solver (1.0384, 0.99953, 0.99798, 0.99962 at alpha/beta 3/5, 12/5, 30/5, 30/2). Its finding stands: two different measures carry
the name lam_cal in this dossier.
  OC = E[(p - E[y|p]) sign(zhat)]  (signed over-confidence): the 19 Oct finite-d table, the d 800 check, and gd_cross.py.
  FM = E[(p - E[y|p]) zhat]        (first moment): calib_path, the path lemma, and every CGMT table from 19 Oct 17:0x on.
At lam_risk, OC is positive at all four audited points, including three past the FM crossing, and lam_OC/lam_risk is 1.104,
1.072, 1.070, 1.028 there. So every statement above about alpha_c(beta), the sign change, and the 1/alpha closing holds for FM
only. "Target 1 for ridge is false as stated" must read "false for the FM measure": under OC, ridge gives no counterexample at any
point tested. The GD section of 02:3x measured OC, so its contrast "GD does not cross where ridge does" compares OC on GD with FM
on ridge. Under OC the two paths agree in sign at every tested point (both calibrate on the large-lambda / early side). The path
lemma (sign FM = sign drho/dq) says nothing about OC. The statement of Target 1 has to name its measure; OC is the one in the
row's source (score-conditional over-confidence).
Running (their cgmt_indep.py, oc_sweep_99aebc7f/): lam_OC/lam_risk at alpha 60, 100, 400, beta 5, to see whether the OC gap
(1.070 at alpha 30) closes with alpha at all, and an H 0.035 grid check at alpha 3.

## 20 Oct 05:2x (claude-99aebc7f): the OC gap does not close with alpha (oc_sweep_99aebc7f/, solver audit_5693aca3/cgmt_indep.py)
beta 5, H 0.05, the same solver as the audit:

    alpha    lam_FM/lam_risk   lam_OC/lam_risk   FM at lam_risk   OC at lam_risk
    12       0.999525          1.072392          -2.7e-05         +1.9e-03     (audit run)
    30       0.997982          1.069849          -5.6e-05         +9.1e-04     (audit run)
    60       0.998685          1.069668          -2.0e-05         +4.9e-04
    100      0.999139          1.069658          -8.1e-06         +3.1e-04
    400      0.999763          1.069670          -5.8e-07         +8.0e-05

FM closes like 1/alpha, as before. OC does not close. lam_OC/lam_risk settles at 1.0697 by alpha 30 and holds to five digits out to
alpha 400, while both lambdas scale like 1/alpha. The reason is elementary. For p = sigma(s zhat), the derivative of the population
log-loss in s at s = 1 is E[(p - y) zhat] = E[(p - E[y|p]) zhat] = FM. So FM = 0 is exactly the first-order condition that no
rescaling of the output lowers the risk. At lam_risk, the only obstruction is that the ridge path moves the direction as well as the
scale, and that coupling vanishes as rho -> 1, which is why lam_FM -> lam_risk. OC has no variational meaning, so its root stays a
fixed fraction away. Consequences for Target 1 (ridge, beta 5): under FM, "calibrated at the risk optimum" holds to O(1/alpha)
and fails in sign past alpha_c. Under OC it fails by a constant 7 percent in lambda at every alpha, always on the large-lambda side,
with OC at lam_risk positive (over-confident) and shrinking only in absolute size, like 1/alpha. At beta 2, alpha 30, the constant is
1.028. The grid check at alpha 3, beta 5 (H 0.035 against 0.05, run_a3b5_H035.txt) reproduces every printed digit.

The constant depends on beta and not on alpha (05:4x, same solver, H 0.05):

    beta   alpha   lam_FM/lam_risk   lam_OC/lam_risk   OC at lam_risk
    1      100     0.999979          1.006889          +6.0e-05
    2      30      0.999616          1.027796          +4.9e-04
    2      100     0.999811          1.028618          +1.7e-04
    2      400     0.999947          1.028917          +4.4e-05
    3      100     0.999587          1.047687          +2.4e-04
    5      100     0.999139          1.069658          +3.1e-04

At beta 2 the ratio moves by 3e-4 between alpha 100 and 400, against 0.029 of gap; at beta 5 it is flat to 1e-5. The gap grows with
the signal strength and its increments shrink (0.007, 0.029, 0.048, 0.070 at beta 1, 2, 3, 5). Beta 10 is running at both grids
(run_a100b10_r2.txt, run_a100b10_H035.txt; the first beta 10 run exited with no output). The large-alpha limit of the constant is a
first-order-in-1/alpha computation: as alpha -> inf the estimate is beta z plus a Gaussian error of variance O(1/alpha), both FM and
OC vanish at the noiseless point, and the ratio is fixed by how the two measures weigh the O(1/alpha) error. Not done.

## 20 Oct 05:5x (claude-99aebc7f): the OC constant in closed form (oc_limit_99aebc7f/oc_limit.py, oc_limit_run1.txt)

Leading order in 1/alpha. Write the ridge estimate as kappa w* + w_perp with |w_perp|^2 = C/alpha, C = 1/i_perp, i_perp = E sig'(beta z),
and kappa - beta = b/alpha - A lam, where b = -E[z sig''(beta z)]/(2 i_par i_perp) is the Cox-Snell bias of the logistic MLE (its trace
term; i_par = E[sig'(beta z) z^2]) and A = dkappa/dlam at lam = 0. With q = |w_hat| and rho = kappa/q,

    delta = q - beta rho = (kappa - beta) + |w_perp|^2/beta,    eps = 1 - rho^2 = |w_perp|^2/beta^2,

and the calibration residual at zhat = q u is m(u) = delta u sig'(beta u) - (beta^2 eps/2) sig''(beta u) + O(1/alpha^2): the first term is
the over-scaling, the second is the averaging of sig over the direction error, which makes the true E[y|zhat] less extreme. FM = 0 and
OC = 0 each fix delta/eps:

    r_FM = (beta^2/2) E[u sig''(beta u)] / E[u^2 sig'(beta u)],    r_OC = (beta^2/2) E[sign(u) sig''(beta u)] / E[|u| sig'(beta u)],

and the root in lam is A alpha lam_r = b - C (r - beta)/beta^2. A cancels in the ratio, and lam_risk = lam_FM at this order (FM = 0 is
the rescaling first-order condition, 05:2x), so

    lam_OC/lam_risk -> (b - C (r_OC - beta)/beta^2) / (b - C (r_FM - beta)/beta^2).

    beta     limit       solver (alpha)            difference
    1        1.007179    1.006889 (100)            -2.9e-4
    2        1.029019    1.028618 (100), 1.028917 (400)   -4.0e-4, -1.0e-4
    3        1.048028    1.047687 (100)            -3.4e-4
    5        1.069681    1.069658 (100)            -2.3e-5
    10       1.085910    1.086819 (100), 1.086125 (400)   +9.1e-4, +2.2e-4
    20       1.091312    1.094054 (100), 1.091918 (400)   +2.7e-3, +6.1e-4

At beta 2 the difference falls by four from alpha 100 to 400, as an O(1/alpha) correction should. At beta 5 the solver reads 1.069668, 1.069658 and 1.069670 at alpha 60, 100 and 400, so there the 1/alpha coefficient is near zero and what is left (1e-5) is grid error. The coefficient changes sign between beta 5 and 10 (about -0.03 at beta 1-3, +0.09 at beta 10). The closed-form value at beta 10 was re-integrated with the sign discontinuity split out (1.085910 again). At alpha 100 the solver gives 1.086819 at both H 0.05 and H 0.035, so the difference is not grid error, and at alpha 400 it gives 1.086125: the difference falls from 9.1e-4 to 2.2e-4, a factor 4.2, so it is the O(1/alpha) correction. At beta 20 the difference is +2.7e-3 at alpha 100 and +6.1e-4 at alpha 400, a factor 4.5, so it is the same O(1/alpha) correction with a coefficient near 0.25, about three times the one at beta 10. The gap is there because the two
measures weigh the over-scaling (u sig' against |u| sig') and the blur (u sig'' against sign(u) sig'') differently, and OC puts relatively
more weight on the blur, so it calls for more shrinkage. It grows with beta and tends to 1/2 + pi^2/(24 ln 2) = 1.093285 (11:1x, oc_limit_99aebc7f/oc_limit_large_beta.py). As beta -> inf
the integrals concentrate on |u| ~ 1/beta, and with phi0 = phi(0) one gets C ~ beta/phi0, b ~ 3 beta^2/(2 pi^2 phi0), r_FM ~ -3 beta^3/(2 pi^2)
and r_OC ~ -beta^3/(8 ln 2). These use int x sig'' = -1, int x^2 sig' = pi^2/3, int_0^inf sig'' = -1/4 and int_0^inf x sig' = ln 2. Hence
A alpha lam_FM ~ 3 beta^2/(pi^2 phi0) and A alpha lam_OC ~ (beta^2/phi0)(3/(2 pi^2) + 1/(8 ln 2)). Numerically the ratio is
1.092963, 1.093204, 1.093264 and 1.093280 at beta 50, 100, 200 and 400. The gap to the limit falls like 0.32/beta^2, and the
split integrals reproduce oc_limit.py at beta 5, 10 and 20 to six digits. So at every signal strength, at leading order in
1/alpha, OC calls for at most 9.3 percent more ridge than the risk optimum does. It also calls for more ridge at every beta > 0, not only on the six tabulated values (11:1x, oc_limit_99aebc7f/oc_sign_all_beta.py). Since b > 0, C > 0 and r_FM, r_OC < 0 (sig'' is odd and negative for u > 0), both lambdas are positive and the ratio exceeds 1 exactly when r_OC < r_FM, that is when D(beta) = E[u sig''(beta u)]/E[u^2 sig'(beta u)] - E[sign(u) sig''(beta u)]/E[|u| sig'(beta u)] > 0. From the Gaussian moments, D = beta^3/24 - beta^5/20 + 611 beta^7/8064 + O(beta^9) at small beta. From the integrals above, D/beta -> 1/(4 ln 2) - 3/pi^2 = 0.056710 at large beta. Quadrature at 30 digits on 21 points from beta 0.05 to 1000 gives D > 0 throughout: D/beta^3 is 0.0415 at beta 0.05 (series value 1/24 = 0.0417), D/beta is 0.0206 at beta 1 and 0.0567 at beta 1000. It is also a theorem (11:2x, oc_sign_mixture_check.py). By Gaussian integration by parts, E[u sig''(beta u)] = (E[u^2 s] - E[s])/beta and E[sign(u) sig''(beta u)] = (E[|u| s] - 2 phi0 s0)/beta, with s = sig'(beta u) and s0 = 1/4. Hence D = (1/beta)(2 phi0 s0/E[|u| s] - E[s]/E[u^2 s]), and D > 0 iff 2 phi0 s0 E[u^2 s] > E[s] E[|u| s]. The logistic density is a normal scale mixture, sig'(x) = int N(x; 0, sigma^2) dF(sigma) with sigma = 2K and K Kolmogorov-distributed (Stefanski 1991). Against a Gaussian kernel exp(-a u^2/2), a = beta^2/sigma^2 and c = 1 + a, the three expectations are c^-1/2, c^-3/2 and 2 phi0 c^-1. With X = c^-1/2 in (0, 1) under the probability P proportional to dF(sigma)/sigma, the condition becomes E[X^3] > E[X] E[X^2]. That is Chebyshev's sum inequality for the two increasing functions X and X^2, and it is strict because X is not constant when beta > 0. The script checks the mixture against sig' to 15 digits and the three expectations against direct quadrature to 12 digits at beta 0.5, 2 and 10. So at leading order in 1/alpha, lam_OC > lam_risk at every beta > 0. The step from the proportional fixed point to the classical constants is proved as well (11:4x, below). The ratio tends to 1 as beta -> 0 because D is O(beta^3) while the lambdas are O(1). The Cox-Snell bias
and the 1/i_perp variance are classical fixed-d results. The proportional fixed point reduces to them at leading order in 1/alpha
(11:4x, oc_limit_99aebc7f/fp_classical_check.py). Put eps = 1/alpha, lam = ell eps and rescale the unknowns of cgmt_ridge.py's
equations (i)-(iii) as mu = beta + eps m, sig_^2 = eps s, c = eps g. The prox gives P = Q - c rho'(Q) + O(c^2), and averaging over
Z2 keeps only even powers of sig_, so after dividing each equation by eps the system is smooth in eps down to eps = 0. At eps = 0 it is
triangular: (ii) gives g i_perp = 1, (iii) gives s = g^2 E[(sig(beta Z) - y)^2] = g^2 i_perp, and (i) gives
i_par m + (s/2) E[Z sig''(beta Z)] + ell beta = 0. The diagonal entries are i_perp, 1 and i_par, all positive. The implicit function
theorem then gives a unique smooth branch with
    alpha c -> 1/i_perp,   alpha |w_perp|^2 = alpha sig_^2 -> 1/i_perp = C,   alpha (kappa - beta) -> b - A ell,  A = beta/i_par,
which are the constants used above. The fixed point is unique at lam > 0, so this branch is the one the solver tracks. The exact fixed
point at alpha 100, 400, 1600 and 6400 (beta 1, 2, 5; ell 0, 1) matches the three limits, and every gap falls by 4.0 per factor 4 in
alpha. At beta 1, ell 0 the gap in alpha(kappa - beta) runs 1.56e-2, 3.85e-3, 9.6e-4, 2.4e-4. The beta 5, ell 1 solves at alpha 100
and 400 did not converge (residual 7e-3) and are left out; from 1600 to 6400 that gap falls by 3.5. What this takes as given is the
fixed-point equations themselves, the CGMT characterisation of ridge logistic regression cited at the top.

## 20 Oct 12:09 (claude-99aebc7f): GD, where OC = 0 falls against FM = 0 (oc_limit_99aebc7f/gd_gap.py)
Late in gradient descent from 0 the flow contracts along w* at rate i_par = E z^2 sig'(beta z) and across it at i_perp = E sig'(beta z),
and i_perp > i_par (Chebyshev: sig' falls as z^2 grows). So kappa(t) = kappa_hat - K0 exp(-i_par t), while alpha |w_perp|^2 is C up
to a relative O(exp(-i_perp t)). OC = 0 and FM = 0 are zero crossings of O(1/alpha) functionals of (kappa, |w_perp|^2), and at fixed
|w_perp|^2 = C/alpha they sit on the kappa axis where ridge's do. Hence, at leading order,
    t_FM - t_OC -> ln(lam_OC/lam_FM)/i_par > 0:  0.473 at beta 2, 8.15 at beta 5,
so GD also reaches OC = 0 before FM = 0. This does not give the risk optimum. Ridge's risk gain comes partly from shrinking w_perp,
which enters the risk at the same order as the kappa shift, and GD has already converged w_perp, so t_risk is not tied to t_FM.
The first version of this check predicted t_risk - t_OC by the same formula and was wrong for that reason (gd_gap_b*.txt: 1.0 at
alpha 40 and 1.57 at alpha 160, beta 2, against 0.47). It also used a log-spaced time grid; gd_cross.py's grid is coarser than these
gaps (about 2 time units at t 27, 12 at t 170), so its time ratios cannot resolve them.
Measured with every step on the grid (d 400, step 0.1, OC and FM by Gauss-Legendre on the half line):
    alpha 40, beta 2, 8 seeds:  t_FM - t_OC = 0.408 +- 0.025 (seeds 0.34-0.51); limit 0.473.  t_risk - t_FM = +0.36 +- 0.24.
At alpha 40 the measured gap is 86 percent of the limit. The alpha 160 run is below.
    alpha 160, beta 2, 4 seeds: t_FM - t_OC = 0.375, 0.684, 0.378, 1.982; mean 0.85 +- 0.38, median 0.53; limit 0.473.
                                t_risk - t_FM = +0.72 +- 0.28 (gd_gap2_b2_a160.txt).
Three seeds sit at 0.38-0.68. Seed 3 crosses late (t_OC 73.5 against 47-55) and gives 1.98. The mean is within one se of the limit, but
the spread is larger than at alpha 40, which the leading-order picture does not by itself predict. A likely reason is finite d. The
OC-to-FM distance in kappa is O(1/alpha), and the seed-to-seed spread of kappa_hat is O(1/sqrt(alpha d)), so their ratio grows like
sqrt(alpha/d): about 0.3 at alpha 40 and 0.6 at alpha 160 with d 400. On that reading the per-seed gap is a log of a ratio of two
nearby small numbers, and one seed can be far off. The check is alpha 160 at d 1600 (n 256,000, a 3.3 GB design), which waits for
memory. Until then: alpha 40 agrees with the limit to 14 percent, and alpha 160 is consistent with it but not a sharper test.
13:1x, the mechanism checked directly (gap_mechanism.py). On the late path exp(-i_par t_X) = (kappa_hat - kappa_X)/K0, so if the two
crossings sit at fixed kappa positions and only kappa_hat moves, D = exp(-i_par t_OC) - exp(-i_par t_FM) = (kappa_FM - kappa_OC)/K0 is
the same on every seed while L = exp(-i_par t_FM) is not, and the time gap ln(1 + D/L)/i_par takes L's noise. Coefficients of variation
across seeds:
    alpha 160, d 400 (alpha/d 0.4), 4 seeds:     D 0.055,  L 0.56,  corr(gap, t_FM) +0.994
    alpha 40,  d 100 (alpha/d 0.4), 12 seeds:    D 0.146,  L 0.22,  corr +0.954  (gaps 0.29-0.51 and one seed at 1.14; mean 0.473, median 0.408)
    alpha 40,  d 400 (alpha/d 0.1), 8 seeds:     D 0.063,  L 0.13,  corr +0.950  (gaps 0.34-0.51)
D is steady while L moves by up to a factor 5 across seeds, and the late seeds carry the large gaps. So the kappa-distance between
OC = 0 and FM = 0 is the deterministic quantity, as the leading-order analysis says; the time gap reads it through a log whose
denominator carries kappa_hat's sampling noise, of relative size sqrt(alpha/d). The limit ln(lam_OC/lam_FM)/i_par is the d -> inf
limit at fixed alpha, taken before alpha -> inf. At alpha/d 0.4 the gap has a heavy upper tail at both alpha 40 and alpha 160, so the
alpha 160 spread is that tail and not a failure of the limit. D is noisier at d 100 than at d 400 because kappa_FM - kappa_OC itself
depends on |w_perp|^2, whose relative noise is O(1/sqrt d). The large t_risk - t_FM spread has the same source and one more:
the risk is flat at its minimum, so its argmin in t moves a lot for a small change in the curve (d 100 seeds: -0.34 to +1.35).

## 20 Oct 12:2x (claude-99aebc7f): GD's late path is radial, so its risk optimum is FM = 0 (derived; slope test running)
Gaussian integration by parts gives E[z sig''(beta z)] = (1/beta) E[(z^2 - 1) sig'(beta z)] = (i_par - i_perp)/beta. With it the two
closed forms for the leading-order FM root, the hand expansion -(T3/(2 i_par i_perp) + 1/(beta i_par)) and the 05:5x form
(T3/(2 i_par) - 1/beta)/i_perp, are the same expression, -(i_par + i_perp)/(2 beta i_par i_perp) for alpha (kappa_FM - beta)
(fm_root_check.py: direct quadrature of E[(sig(kz + g) - sig(beta z))(kz + g)] = 0 converges to it, -5.78132 at beta 2; at beta 5 the
05:5x form read -13.439 against -13.417 only because 120 Hermite nodes break the identity there).
The 12:09 section assumed GD has converged w_perp when it crosses OC and FM, so that the path runs along the kappa axis at fixed
|w_perp|^2. That is wrong at the order that matters for the risk. Late in GD, w - w_hat lies along the slowest eigenvector of the
Hessian at the MLE. Its w_perp part is (i_par - H_perp)^{-1} h with h = E_n[sig''(beta z) z x_perp x_perp^T] w_perp_hat + (noise
uncorrelated with w_perp_hat at leading order), so it tilts by tau = T3/(i_par - i_perp) = 1/beta:
    w_perp(kappa) = w_perp_hat (1 + (kappa - kappa_hat)/beta),  |w_perp|^2 = (C/alpha)(1 + 2 (kappa - kappa_hat)/beta).
That is a rescaling of the MLE to first order. The |w_perp|^2 change is O(1/alpha^2), too small to move OC = 0 or FM = 0 (both
O(1/alpha) functionals), so the 12:09 calibration result stands. It is not too small for the risk: the risk gradient along the kappa axis
at fixed |w_perp|^2 vanishes at kappa_hat to leading order (i_par (kappa - beta) + T3 C/(2 alpha) = 0 is the MLE's own fixed-point equation
(i)), so the O(1/alpha^2) term (i_perp/2) d|w_perp|^2 decides where the minimum falls. Along a radial path the risk derivative is the
rescaling derivative, which is FM. Hence on GD, at leading order,
    t_risk - t_FM -> 0,   t_risk - t_OC -> ln(lam_OC/lam_FM)/i_par (0.473 at beta 2),
the same picture as ridge (lam_risk = lam_FM). Measured so far: t_risk - t_FM = +0.36 +- 0.24 (alpha 40) and +0.72 +- 0.28 (alpha 160),
d 400. Finite-alpha corrections are of order c/(alpha i_par), about 2 at alpha 40 for c ~ 5, so neither contradicts the limit. The
alpha 160 value, larger rather than smaller, is not yet explained. Test running: gd_slope.py measures d ln|w_perp|^2/d ln kappa on the
GD path; radial predicts 2 kappa/beta (about 1.9 at alpha 40, beta 2), converged-w_perp predicts 0.
Slope test (12:3x, gd_slope_b2_a40.txt, d 200, alpha 40, beta 2): d ln|w_perp|^2/d ln kappa on the GD path is
    seed 0: 1.89 (t 30), 1.95 (40), 2.01 (60), 2.03 (80);  seed 1: 2.11, 2.16, 2.20, 2.21;  radial 2 kappa/beta = 1.87-2.07.
At t 60-80 the perp transient is down by exp(-i_perp t) < 1e-4, so the w_perp change still riding with kappa is the tilt, and its
size is the radial one to within 7 percent (finite alpha: alpha |w_perp|^2 is 8.0 and 6.7 there against C = 6.6). The converged-w_perp
picture (slope 0) is ruled out. So on GD as on ridge, the risk optimum and FM = 0 coincide at leading order and OC = 0 comes first.

## 20 Oct 13:4x (claude-99aebc7f): random features at n = inf - misspecification leaves an O(1) OC gap (rf_limit_99aebc7f/)
Under Gaussian equivalence u = tanh(F x) ~ mu1 F x + mus xi (mu1 0.6057, mus^2 0.0274), and the best linear predictor of
z* = beta w*.x from u leaves an independent Gaussian residual: z* = b s + tau Z with s the standardized projection,
b = beta rho_max, tau^2 = beta^2 (1 - rho_max^2), rho_max^2 = mu1^2 avg lam/(mu1^2 lam + mus^2) over the spectrum of F'F. So y | u
follows the link g(s) = E sigma(b s + tau Z), which is not a logistic: the RF logistic model is misspecified at every finite N/d.
At n = inf the score equation still gives FM = 0 at the risk optimum (lam -> 0), but OC is not 0 there. Two routes, which share no
code: the radial family zhat = k s fitted against g (rf_limit.py, d 1500 spectrum), and the population ridge path
a = kappa (A'(q)/q Sig + lam)^{-1} m solved self-consistently through R(q, c) = A(q) - kappa c (rf_ridge_inf.py, d 800).
  OC at the n = inf risk optimum (radial / ridge), beta 5:  N/d 0.5 +0.00236/+0.00243, 1 +0.00350/+0.00350, 2 +0.00228/+0.00225,
  4 +0.00115/+0.00116; beta 2 (radial): N/d 1 +0.00126, peak near N/d 1, 0.00001 by N/d 64.
  Ridge at n = inf, beta 5: lam_OC = 4.4e-4, 2.2e-4, 1.4e-4, 1.4e-4 at N/d 0.5, 1, 2, 4; the risk paid for OC = 0 is 3.4e-5, 1.1e-4,
  5.0e-5, 1.4e-5 (radial temperature scaling: k_OC/k_FM 0.976 at N/d 1, cost 7.5e-5; ridge also loses a little alignment).
The sign is over-confident in every case (beta 2 and 5, N/d 0.25 to 64). Consequence for the row: on ridge, lam_risk -> 0 like 1/n
while lam_OC tends to a positive constant, so for random features lam_OC/lam_risk grows without bound in alpha (the linear model
tends to 1.007-1.093). The absolute effect is small: OC at most 0.0035 and the risk cost of removing it about 1e-4 at beta 5.
This does NOT explain the 19 Oct finite-n table (alpha 3, lam_cal/lam_risk 1.1-1.7 at N/d 1-2): there lam_risk is 0.05-0.09, two
orders above lam_OC at n = inf, so at alpha 3 the gap is a finite-alpha effect, as in the linear case but larger. The misspecification
term takes over only when lam_risk falls below about 2e-4, alpha of order 10^3. Open: the finite-alpha RF constant (CGMT with the GE
covariance), and a check with real tanh features rather than the GE model (rf_limit_check.py, running).

### 20 Oct 17:0x (claude-99aebc7f): the sign of the n = inf OC gap, and real tanh features
Sign lemma. In the radial family zhat = k s against the link g(s) = E sigma(b s + tau Z), put D(s) = sigma(k s) - g(s), odd about
1/2 in s. The risk optimum in k is FM = E[D(s) s] = 2 int_0^inf D s phi = 0, and OC (mean confidence minus accuracy) is
2 int_0^inf D phi. Write L = logit g. Then D(s) > 0 exactly when k > L(s)/s. If L(s)/s is strictly increasing on (0, inf), from
b Lam'(0) to b, then D has one sign everywhere unless k lies in that range, and FM = 0 rules the one-sign case out. So D changes sign
once, + then -, at some s0, and OC = 2 int_0^inf D (1 - s/s0) phi > 0, because D (1 - s/s0) >= 0 with equality only at s0. By scaling,
L(s) = Lam(b s) with Lam(x) = logit E sigma(x + tau Z), so the condition depends on tau alone. Lam(x) is F_logistic^{-1}(F_W(x)) for
W = logistic + tau Z, so the condition says W precedes the logistic in van Zwet's star order. Not proved. Checked numerically
(logit_convex.py, logit_convex_run1.txt): Lam(x)/x is increasing on (0, 40] for every tau in [0.02, 12], the smallest step
difference being +2.5e-9 to +6.3e-6 per 0.02 in x. Lam'(0) = 4 f_W(0) runs from 0.9999 down to 0.13, and Lam(x) - x + tau^2/2 is
under 1e-6 at x = 40 for tau <= 4. Lam itself is convex (the stronger convex transform order) up to finite-difference noise: its most
negative second difference is -5e-10, where Lam' = 1 to four places. So the over-confident sign at the n = inf risk optimum is a
theorem given one inequality about a single function of tau, and that inequality holds on the whole checked range.
The inequality in a cleaner form (var_ratio.py, var_ratio_run2.txt). With Y = sigma(x + tau Z) and m = E Y, f_W = E[Y (1 - Y)]
= m (1 - m) - Var Y, so Lam'(x) = f_W/(m (1 - m)) = 1 - r(x) with r(x) = Var Y/(m (1 - m)), a normalized variance in [0, 1). Lam is
convex on x > 0 exactly when r is decreasing there, and convexity with Lam(0) = 0 gives the star condition. The identity matches a
central-difference Lam' to 5e-11. On (0, 40] r decreases at every grid step for every tau in {0.02, 0.1, 0.5, 1, 2, 3, 4, 6, 8, 12}:
r(0) runs from 1.0e-4 (tau 0.02) to 0.869 (tau 12), and r(40) from 1.7e-21 to 0.707. For small tau, r ~ tau^2 sigma'(x), which
decreases on x > 0, so the small-tau case is immediate to leading order. What remains to prove: Var sigma(x + tau Z)/(m (1 - m)) is
decreasing in x > 0 for every tau. The Gaussian variation-diminishing route does not apply directly, since sigma(c x) is not a
Gaussian smoothing of anything (the logistic's characteristic function decays only like e^{-pi |t|}).
Proof of the star condition (17:34 20 Oct; star_mixture_check.py, star_mixture_check_run1.txt). The sign lemma needs only
Lam(x)/x increasing, not convexity, and that follows from the logistic being a normal scale mixture: L = V Z with V = 2K and K
Kolmogorov-distributed, independent of Z (Andrews and Mallows 1974; Stefanski 1991). Then W = L + tau Z' = U Z with U = sqrt(V^2 +
tau^2). Lam(x) > c x exactly when F_W(x) > F_L(c x), so it is enough that for every c > 0 the difference F_W(x) - F_L(c x) changes
sign at most once on x > 0, and from - to +. Put x = e^t. Then F_W(x) - F_L(c x) = E Phi(e^(t - log U)) - E Phi(e^(t - log(V/c))),
and integrating by parts in u it equals int k(t - u) N(u) du, with k(v) = e^v phi(e^v) and
    N(u) = P(log U <= u) - P(log(V/c) <= u) = P(V^2 <= e^(2u) - tau^2) - P(V^2 <= c^2 e^(2u)).
The sign of N(u) is the sign of (1 - c^2) e^(2u) - tau^2 wherever it is nonzero, because both terms are the same distribution function
of V^2. For c >= 1, N <= 0, so Lam(x) < c x for all x. For c < 1, N changes sign once, - then +. The kernel k is log-concave
(log k = v - e^(2v)/2 + const), hence TP2, and a TP2 kernel neither adds sign changes nor reverses their order when there is at most
one (Karlin, Total Positivity, ch. 5). So F_W(x) - F_L(c x) changes sign at most once, - then +. Lam(x)/x is then nondecreasing, and
it is strictly increasing because it is analytic and not constant (it runs from Lam'(0) < 1 to 1). That closes the sign lemma: at the
n = inf risk optimum (FM = 0) of the RF logistic model the predictor is over-confident, OC > 0, for every beta, N/d and tau > 0. The
argument uses only that the link (shared by teacher and student, as in T357) is the cdf of a normal scale mixture, so it holds as
stated for the probit and Student-t links too (for the probit, W is itself Gaussian, Lam is linear, and OC = 0 exactly). Checks: the mixture gives sigma to 1.4e-5 on
[-10, 10] (the grid's error), and for tau 0.1 to 8 and c in 0.05..1.2 the difference F_W(x) - F_L(c x) has at most one sign change on
(0, 40], always - then +. The stronger claim (Lam convex, equivalently r decreasing) is still unproved and is no longer needed.

Real features (rf_limit_check.py, rf_limit_check_b5_psi1.txt). beta 5, N/d 1, actual tanh features, three draws of F, at alpha 25,
50, 100 and 200. Each OC is a mean over test points at the fitted risk optimum, with its standard error.
    seed 0: OC +0.0278, +0.0145, +0.0102, +0.0038 (se 0.0003)   FM +0.050, +0.022, +0.013, -0.0003   rho_max 0.909
    seed 1: OC +0.0247, +0.0163, +0.0124, +0.0051 (se 0.0004)   FM +0.038, +0.022, +0.015, +0.0028   rho_max 0.832
    seed 2: OC +0.0374, +0.0248, +0.0073, +0.0083 (se 0.0004)   FM +0.068, +0.041, +0.007, +0.0077   rho_max 0.867
With an a + c/alpha fit the alpha -> inf intercepts are +0.0019, +0.0050 and +0.0025, mean +0.0031; the GE predictions for the same F
are +0.0034, +0.0034 and +0.0035. The fit is loose (four alphas, and seed 2 dips at alpha 100), each intercept good to about +-0.002.
The test that does not lean on the fit is seed 0 at alpha 200: FM -0.0003 (calibrated in the FM sense) and OC +0.0038, 11 se above 0.
So real tanh features keep a positive OC once FM is 0, of the size Gaussian equivalence predicts. Open: the finite-alpha RF constant
(CGMT on the GE covariance), a proof of the star-order inequality, GD rigour.

## 20 Oct 17:25 (claude-99aebc7f): random features at finite alpha - a fixed point that reproduces the 19 Oct table (rf_limit_99aebc7f/rf_cgmt.py)
cgmt_ridge.py's leave-one-out fixed point carried to the anisotropic Gaussian design of Gaussian equivalence (Sig = mu1^2 F F' +
mus^2 I, teacher direction t = Sig^-1 m/rho in u-space). The prox step becomes c = (1/n) tr Sig G with G = (lam + Vh Sig)^-1, the
mean equation mu = -A1 t'Sig G Sig t, and the spread mu^2 + sg^2 = A1^2 t'Sig G Sig G Sig t + (E rho'^2/n) tr (Sig G)^2, with
Vh = E[rho''/(1 + c rho'')] and A1 = E[Z1 rho'] - mu Vh. With Sig = I these are cgmt_ridge.py's three equations exactly (checked by
hand). Same model, scaling and F draws as rf_cross.py (d 200, alpha 3, N/d 1, beta 2, F seeds 100-102):
                     fixed point (per F)        simulation 19 Oct (per seed; same F, its own data)
    lam_cal (OC)     0.0727  0.0871  0.0758     0.0664  0.0956  0.0717
    lam_risk         0.0559  0.0656  0.0544     0.0539  0.0571  0.0538
    cal/risk         1.301   1.328   1.393      1.233   1.676   1.334
The lam_cal values agree within the simulation's data noise. The simulation's lam_risk is the argmin of a flat noisy test risk.
The new fact is where FM = 0 falls: lam_FM = 0.0714, 0.0857 and 0.0745, within 2 pct of lam_cal. So at alpha 3 the ridge risk
optimum is NOT the FM = 0 point, unlike the linear model, where they coincide at leading order. The ridge path is not a rescaling:
more ridge shrinks the small-eigenvalue directions of Sig and so changes zhat's direction as well as its size, and the risk
optimum trades scale calibration for direction. The 19 Oct gap is therefore mostly lam_FM/lam_risk (1.28-1.31, a direction
effect) and only a little lam_cal/lam_FM (1.02, the OC-versus-FM effect the n = inf section measures). The N/d grid and the alpha sweep are in the 18:26 section below.

## 20 Oct 18:26 (claude-99aebc7f): the finite-alpha fixed point over N/d and alpha - where the calibration gap comes from
N/d grid (rf_cgmt.py, d 200, alpha 3, beta 2, F seeds 100-102; simulation = rf_cross_run1.txt, same F, its own data):
    N/d   cal/risk (fixed pt)  cal/risk (sim)       cal/FM               FM/risk
    0.5   1.114 1.176 1.326    1.128 1.110 1.568    1.011 1.010 1.012    1.102 1.165 1.310
    1     1.301 1.328 1.393    1.233 1.676 1.334    1.019 1.017 1.018    1.277 1.306 1.369
    2     1.201 1.278 1.397    1.147 1.282 1.248    1.021 1.020 1.020    1.177 1.253 1.370
    3     1.161 1.170 1.241    1.137 1.180 1.184    1.021 1.021 1.020    1.138 1.146 1.216
    4     1.104 1.132 1.145    1.092 1.009 1.193    1.020 1.020 1.020    1.082 1.110 1.122
    8     1.032 1.079 1.098    1.046 1.063 1.106    1.019 1.019 1.020    1.012 1.059 1.076
The fixed point follows the simulation at every N/d within its seed noise (the simulation's lam_risk is the argmin of a flat
noisy risk), including the fall of the ratio toward 1 as N/d grows. At every N/d cal/FM is 1.02-1.03: at alpha 3 nearly all of
the gap is FM/risk, the direction effect of the 17:25 section. At N/d 4 and 8 the solver loses the root below lam ~ 0.004
(interpolation regime, N > n); all three crossings lie above that.
alpha sweep (d 1000, N/d 1, F seed 100; the alpha >= 100 rows from the 18:1x solver fix). lam_OC_inf is the n = inf ridge
path on the same F (rf_ridge_inf.py beta 1 1000 100: 1.677e-4 for beta 2, 2.206e-4 for beta 5); the last column is
alpha (lam_cal - lam_FM - lam_OC_inf) x 1000:
    b  alpha   lam_cal  lam_FM  lam_risk   cal/FM FM/risk  a.lamFM a.lamrisk  resid
    2      3   0.08318  0.08185  0.06042   1.016  1.355   0.2455  0.1813   3.478
    2     10   0.01521  0.0146  0.00966   1.042  1.512   0.1460  0.0966   4.433
    2     30   0.003988  0.003685  0.002677   1.082  1.377   0.1106  0.0803   4.059
    2    100   0.001199  0.0009916  0.000773   1.209  1.283   0.0992  0.0773   3.973
    2    300   0.0005035  0.0003204  0.0002564   1.572  1.250   0.0961  0.0769   4.632
    2   1000   0.0002701  9.51e-05  7.68e-05   2.840  1.238   0.0951  0.0768   7.259
    5      3   0.03111  0.02952  0.01993   1.054  1.481   0.0886  0.0598   4.108
    5     10   0.005325  0.004753  0.003504   1.120  1.357   0.0475  0.0350   3.510
    5     30   0.001594  0.001269  0.001035   1.257  1.225   0.0381  0.0311   3.146
    5    100   0.0006085  0.0003526  0.0002998   1.726  1.176   0.0353  0.0300   3.525
    5    300   0.0003528  0.0001151  9.904e-05   3.065  1.162   0.0345  0.0297   5.121
    5   1000   0.0002658  3.428e-05  2.962e-05   7.755  1.157   0.0343  0.0296   10.928
Reading: lam_FM and lam_risk both fall like 1/alpha (alpha lam_FM -> about 0.095, alpha lam_risk -> about 0.077 for beta 2), so
FM/risk tends to a constant near 1.25: the direction effect is a variance effect and survives at every alpha. lam_cal does NOT
fall like 1/alpha: lam_cal - lam_FM tends to lam_OC_inf, the ridge that the n = inf over-confidence (the scale-mixture theorem
of 343864c5) needs, plus a remainder (the last column). The remainder is a/alpha + b with a constant b: from alpha 100 and 1000,
a = 3.6e-3, b = 3.7e-6 for beta 2 (predicts 1.57e-5 at alpha 300, measured 1.54e-5) and a = 2.7e-3, b = 8.2e-6 for beta 5
(predicts 1.72e-5, measured 1.71e-5). b is not mathematics: rf_cgmt.py takes OC with 120-node Gauss-Hermite across the kink of
sign(p - 1/2) and reads it 2-4 percent high (oc_quadrature_check.py: 0.001280 against 0.001253 split-Legendre at beta 2,
0.003611 against 0.003484 at beta 5), and that bias divided by dOC/dlam near lam_OC_inf (about 7.6 and 16) is 3.6e-6 and
8e-6, which is b. With the quadrature corrected, then,
    lam_cal = lam_FM + lam_OC_inf + a/alpha + o(1/alpha),   lam_FM, lam_risk = Theta(1/alpha),
and cal/risk grows linearly in alpha once alpha lam_OC_inf is comparable with 0.1 (alpha about 600 at beta 2, 450 at beta 5). The 19 Oct
alpha 3 gap and the large-alpha gap are two different things: at small alpha it is the direction term FM/risk, at large alpha
it is the population over-confidence, which no amount of data removes.
Why (18:31): two scales. At lam of order 1 the finite-alpha fixed point is the n = inf ridge solution plus an O(1/(alpha lam))
variance correction; at lam of order 1/alpha the correction is O(1). On the data the correction acts, for the calibration
functionals, as a shift of the ridge: OC_alpha(lam) ~ OC_inf(lam - k_cal/alpha) and FM_alpha(lam) ~ FM_inf(lam - k_FM/alpha), with
FM_inf(0) = 0 (the population first-order condition) and OC_inf(lam_OC_inf) = 0. Then lam_FM = k_FM/alpha and
lam_cal = lam_OC_inf + k_cal/alpha. Measured (quadrature offset b removed): beta 2, alpha (lam_cal - lam_OC_inf) = 0.103, 0.0996,
0.0987 at alpha 100, 300, 1000 and alpha lam_FM = 0.0992, 0.0961, 0.0951, so k_cal = 0.099, k_FM = 0.095; beta 5, 0.0380,
0.0372, 0.0370 against 0.0353, 0.0345, 0.0343, so k_cal = 0.037, k_FM = 0.034. The shift is nearly the same for both
functionals (k_cal/k_FM 1.04 and 1.08), which is why a = k_cal - k_FM is small. The risk optimum is not a pure shift
(alpha lam_risk -> 0.077 and 0.030, below k_FM): the variance adds risk of its own. A proof would show the fixed point's
(q, cov) at lam > 0 fixed equal the n = inf ones up to a correction whose first-order effect on OC and FM is a ridge
shift: matched asymptotics between the two scales, with the outer expansion valid once alpha lam >> 1.

## 20 Oct 19:17 (claude-99aebc7f): why lam_FM is Theta(1/alpha) - an exact identity
For the ridge-penalised logistic fit without intercept, FM = E[(sig(zhat) - y) zhat] satisfies, on the TRAINING sample and at
every n, FM_train(lam) = -lam |w_hat|^2 exactly: the stationarity condition (1/n) sum (sig(w.u_i) - y_i) u_i + lam w = 0 dotted
with w_hat. The population version is the same computation on the population objective A(q) - kappa a.m + lam |a|^2/2:
stationarity A'(q) Sig a/q - kappa m + lam a = 0 dotted with a gives q A'(q) - kappa c = -lam |a|^2, and q A'(q) - kappa c is FM
(E sig(q u) q u = q A'(q); E y zhat = kappa c by Stein). So FM_inf(lam) = -lam |a_lam|^2, zero only at lam = 0.
Check on the n = inf path (fm_identity_check.py, d 1000, N/d 1, F seed 100):
beta 2
  lam     1e-05  FM -1.056296e-04  -lam|a|^2 -1.056296e-04  rel diff +1.7e-10  OC +0.00119
  lam    0.0001  FM -1.039562e-03  -lam|a|^2 -1.039562e-03  rel diff +1.7e-11  OC +0.00051
  lam 0.0001677  FM -1.722924e-03  -lam|a|^2 -1.722924e-03  rel diff +1.0e-11  OC -0.00000
  lam     0.001  FM -9.010548e-03  -lam|a|^2 -9.010548e-03  rel diff +1.9e-12  OC -0.00557
  lam      0.01  FM -4.151103e-02  -lam|a|^2 -4.151103e-02  rel diff +3.1e-13  OC -0.03670
  lam       0.1  FM -6.250595e-02  -lam|a|^2 -6.250595e-02  rel diff +9.3e-14  OC -0.10152
beta 5
  lam     1e-05  FM -2.937616e-04  -lam|a|^2 -2.954514e-04  rel diff +5.8e-03  OC +0.00334
  lam    0.0001  FM -2.866033e-03  -lam|a|^2 -2.867705e-03  rel diff +5.8e-04  OC +0.00187
  lam 0.0001677  FM -4.704602e-03  -lam|a|^2 -4.706262e-03  rel diff +3.5e-04  OC +0.00081
  lam     0.001  FM -2.244215e-02  -lam|a|^2 -2.244369e-02  rel diff +6.8e-05  OC -0.01007
  lam      0.01  FM -7.924673e-02  -lam|a|^2 -7.924778e-02  rel diff +1.3e-05  OC -0.05807
  lam       0.1  FM -9.972515e-02  -lam|a|^2 -9.972560e-02  rel diff +4.5e-06  OC -0.13864
At beta 2 the identity holds to 1e-10 relative. At beta 5 FM sits a constant 1.6-1.7e-6 above -lam|a|^2 at every lam: the
quadrature error of the steeper link (120 Hermite nodes, the same kind as the 2-4 percent OC bias of the 18:3x section), not
the identity; it would move lam_FM by 1.6e-6/|a|^2, about 6e-8.
Consequences. (i) At finite n the FM-calibrating ridge is fixed by the generalisation gap of the FM statistic:
    lam_FM |w_hat(lam_FM)|^2 = FM_pop(lam_FM) - FM_train(lam_FM) + ... i.e.  lam_FM = gap_FM / |w_hat|^2,
so lam_FM = Theta(1/alpha) is equivalent to the FM train-test gap being Theta(1/alpha), which is what the alpha sweep shows
(alpha lam_FM -> 0.095 / 0.034). (ii) lam_risk = Theta(1/alpha) for the same reason: the population risk is minimised at
lam = 0 (the population minimiser over the feature class), so the risk-optimal ridge is set by the 1/alpha variance term alone.
(iii) lam_cal does not go to 0, because OC_inf(0+) = +0.00127 (beta 2) is not zero: the misspecified population fit (tanh
features, sigmoid link) is over-confident, and lam_cal -> lam_OC_inf > 0 by continuity of the fixed point in 1/alpha, with
an O(1/alpha) correction where OC_inf has nonzero slope at lam_OC_inf (implicit function theorem). So the three ridges
separate for structural reasons: two are zeros of quantities that vanish at lam = 0 in the population (FM by the identity,
the risk gradient by optimality), the third is not.
Open: the gap coefficient itself (gap_FM alpha -> k_FM |a_0|^2) in closed form from the fixed point, and a proof that the
fixed point is C^1 in 1/alpha at 0.

## 20 Oct 19:41 (claude-99aebc7f): the FM gap coefficient in closed form - lam_FM |w|^2 -> N/n
From the identity of the previous section: at the fixed point a training prediction is P = Q - c rho'(P) and a fresh one has
the law of Q, so with g(z, y) = (sig(z) - y) z the train-test gap of FM is c E[g'(Q) rho'(Q)] + O(c^2), and
c = (1/n) tr Sig G -> N/(n Vh) as lam -> 0 (Vh = E sig'(zhat), Sig full rank). Setting FM_pop = 0 at lam_FM:
    k_FM = lim alpha lam_FM = psi E[(sig'(zhat) zhat + sig(zhat) - y)(sig(zhat) - y)] / (Vh |a_0|^2),
all at the n = inf population fit (fm_gap_coefficient.py, d 1000, N/d 1, F seed 100):
    beta 2.0 psi 1.0 lam0 1e-08: q0 1.48432  Vh 0.17760  E[g'rho'] 0.178036  |a0|^2 10.58193  k_FM predicted 0.09473
    beta 2.0 psi 1.0 lam0 1e-06: q0 1.48425  Vh 0.17761  E[g'rho'] 0.178034  |a0|^2 10.58005  k_FM predicted 0.09474
    beta 5.0 psi 1.0 lam0 1e-08: q0 2.48442  Vh 0.13164  E[g'rho'] 0.133377  |a0|^2 29.64548  k_FM predicted 0.03418
    beta 5.0 psi 1.0 lam0 1e-06: q0 2.48413  Vh 0.13165  E[g'rho'] 0.133374  |a0|^2 29.63550  k_FM predicted 0.03418
against the alpha sweep (rf_cgmt_*_v2.txt): alpha lam_FM = 0.0961 / 0.0951 at alpha 300 / 1000 for beta 2 (predicted 0.0947)
and 0.0345 / 0.0343 for beta 5 (predicted 0.0342) - within 0.4 percent at alpha 1000 and closing at the 1/alpha rate.
The numerator is nearly Vh (0.17804 against 0.17760; 0.13338 against 0.13164): for a well-specified link (P(y | zhat) =
sig(zhat)) it is exactly Vh, since then E(sig - y)^2 = E sig(1 - sig) and E sig' zhat (sig - y) = 0. So to the accuracy of the
misspecification
    lam_FM |w_hat|^2 -> N/n   (alpha lam_FM -> psi / |a_0|^2: 0.0945 and 0.0337 here),
a Takeuchi-type count: the FM-calibrating ridge spends exactly the number of fitted parameters per sample on |w|^2.
With the 18:3x and 19:17 sections the large-alpha picture is closed in formulas up to the C^1 claim:
lam_FM ~ N/(n |a_0|^2), lam_risk ~ k_risk/alpha (from the same expansion of the risk; not yet written out), lam_cal -> lam_OC_inf.
Open: write k_risk the same way; prove C^1 of the fixed point in 1/alpha.

## 20 Oct 20:20 (claude-99aebc7f): k_risk - a first closed form is short by a third; the CGMT sweep is confirmed by simulation
Exact at every n (risk_gap_coefficient.py docstring): R(w_hat_lam) is stationary where
    lam_risk = [grad R - grad Rhat](w_hat) . Hh^-1 w_hat / (w_hat' Hh^-1 w_hat),
the FM identity of the 19:17 section with w_hat replaced by Hh^-1 w_hat. A leave-one-out expansion of the numerator gives, to
first order, (1/n) tr(H^-2 J) + (tiny misspecification term) over a_0' H^-1 a_0, H the full population Hessian
(Vh Sig + gam Sig a a' Sig). That predicts (d 1000, F seed 100):
    beta 2.0 psi 1.0 lam0 1e-08: q0 1.48432 Vh 0.17760 gam -0.03776 E rho'^2 0.17783 E rho''rho'zeta +0.01064 mean(1/s) 8.7205 a'H^-1 a 951.6752 (spike-free 699.4922)  k_risk predicted 0.05178  (variance term alone 0.05166)
    beta 2.0 psi 1.0 lam0 1e-06: q0 1.48425 Vh 0.17761 gam -0.03776 E rho'^2 0.17783 E rho''rho'zeta +0.01049 mean(1/s) 8.7205 a'H^-1 a 951.3833 (spike-free 699.2932)  k_risk predicted 0.05180  (variance term alone 0.05167)
    beta 5.0 psi 1.0 lam0 1e-08: q0 2.48442 Vh 0.13164 gam -0.01470 E rho'^2 0.13262 E rho''rho'zeta +0.08862 mean(1/s) 8.7205 a'H^-1 a 5042.8700 (spike-free 2643.8347)  k_risk predicted 0.01350  (variance term alone 0.01323)
    beta 5.0 psi 1.0 lam0 1e-06: q0 2.48413 Vh 0.13165 gam -0.01470 E rho'^2 0.13262 E rho''rho'zeta +0.08796 mean(1/s) 8.7205 a'H^-1 a 5039.7198 (spike-free 2642.4378)  k_risk predicted 0.01351  (variance term alone 0.01324)
against the sweep's alpha lam_risk 0.0768 (beta 2) and 0.0296 (beta 5). To decide which is wrong, sim_risk_derivative.py
simulates the Gaussian-equivalent design directly (N = d = 200, alpha 100, n 20000, same F; ridge-logistic fits by Newton at
five lam, common data) and averages the exact per-fit dR/dlam = -grad R(w_hat).(Hh + lam)^{-1} w_hat, grad R in closed form:
  reps 10: mean dR/dlam -5.5578e-01(8.0e-02) -3.3313e-01(7.1e-02) -1.4223e-01(6.3e-02) +2.2378e-02(5.6e-02) +1.6505e-01(5.1e-02)  -> linear zero lam_risk 7.8779e-04  alpha*lam_risk 0.0788
  reps 20: mean dR/dlam -5.7454e-01(4.8e-02) -3.4677e-01(4.3e-02) -1.5180e-01(3.8e-02) +1.6076e-02(3.5e-02) +1.6137e-01(3.1e-02)  -> linear zero lam_risk 7.9527e-04  alpha*lam_risk 0.0795
  reps 30: mean dR/dlam -5.7141e-01(3.9e-02) -3.4481e-01(3.5e-02) -1.5066e-01(3.1e-02) +1.6668e-02(2.8e-02) +1.6161e-01(2.6e-02)  -> linear zero lam_risk 7.9449e-04  alpha*lam_risk 0.0794
  reps 40: mean dR/dlam -5.4126e-01(3.5e-02) -3.1770e-01(3.2e-02) -1.2610e-01(2.8e-02) +3.9056e-02(2.6e-02) +1.8214e-01(2.3e-02)  -> linear zero lam_risk 7.6941e-04  alpha*lam_risk 0.0769
CGMT on the same F: F seed 100: rho 0.9021  lam_cal(OC) 0.0011055  lam_FM 0.00092157  lam_risk 0.00076352  cal/risk 1.448
and the closed form at d 200 gives 0.0514. So alpha lam_risk = 0.077 +- 0.003 by simulation, matching CGMT (0.0764), and the
closed form is short by about a third. The simulated slope of dR/dlam (about 900) matches a_0' H^{-1} a_0 with the spike (984 at
d 200; 693 without), so the denominator is right and the variance side is not: the intercept is -0.72 against the predicted
-(1/n) tr(H^{-2} J) = -0.505. One term identified so far: the sampling covariance C = H^{-1} J H^{-1}/n is taken at a_lam, and
dH/dlam = -E[sig''(zhat) zeta x x'] has full-rank part -gam K Sig (K = a' Sig H^{-1} a, 23.3 at beta 2), which adds
|gam K| / mean(1/s) = 10 percent (0.0518 -> 0.057). The remaining ~25 percent is not accounted for: the fixed-N expansion has
terms with a' Sig^{-k} a that are as large as N here (var zeta = a' H^{-1} Sig H^{-1} a is about 5,400 at N 1000), so the
classical second-order formula is not the right leading order at these sizes, while CGMT is.
Status: lam_FM closed form (19:41) stands; for lam_risk the CGMT fixed point is the verified description, the closed form is open.
Open: expand the rf_cgmt.py fixed point itself in 1/alpha (its variance equation (iii) and the q-dependence of Vh, A1) instead of
the fixed-N M-estimator expansion.

## 20 Oct 21:47 (claude-99aebc7f): k_risk inside the CGMT fixed point - the noise term carries it, the frozen part is closed
cgmt_decompose.py switches off each finite-n ingredient of the rf_cgmt.py fixed point (alpha 1000, psi 1, d 1000, F seed 100):
    NOISE 1 PROXC 1: lam_risk 7.6826e-05  alpha*lam_risk 0.07683  min excess 6.8098e-02
    NOISE 1 PROXC 0: lam_risk 7.6851e-05  alpha*lam_risk 0.07685  min excess 6.8098e-02
    NOISE 0 PROXC 1: lam_risk 6.4249e-06  alpha*lam_risk 0.00642  min excess 6.7599e-02  (minimum at the grid edge)
    NOISE 1 PROXC 1: lam_risk 2.9656e-05  alpha*lam_risk 0.02966  min excess 1.6675e-01
    NOISE 1 PROXC 0: lam_risk 2.9567e-05  alpha*lam_risk 0.02957  min excess 1.6675e-01
    NOISE 0 PROXC 1: lam_risk 6.4286e-06  alpha*lam_risk 0.00643  min excess 1.6625e-01  (minimum at the grid edge)
The prox step does not matter at this alpha; without the noise term (E rho'^2/n) T3 there is no interior minimum. So the fixed
point reduces to (ii) mu = -A1 T1, (iii) mu^2 + sg^2 = A1^2 T2 + (R2/n) T3, with A1 = E[Z1 rho'(Q)] - mu Vh, Vh = E rho''(Q),
R2 = E rho'^2, G = 1/(lam + Vh S), T3 = sum S^2 G^2 (cgmt_feedback.py docstring). FULL solves it; FROZEN adds the noise to sg^2
with Vh, A1, R2 held at their n = inf values (no feedback):
  beta 2: full    : alpha*lam_risk 0.07683  min excess 6.809783e-02 | frozen  : alpha*lam_risk 0.06412  min excess 6.809711e-02
  beta 5: full    : alpha*lam_risk 0.02957  min excess 1.667489e-01 | frozen  : alpha*lam_risk 0.02143  min excess 1.667480e-01
The frozen part in closed form. With dE/d(sg^2) = Vh/2 (Stein), the frozen excess is E0(lam) + (1/n) g(lam) T3(lam, Vh(lam)),
g = R2 Vh/2; this matches the computed frozen excess to 3e-7 of 5e-4 at three lam (run3 files). Its minimiser solves
    E0'(lam) + (1/n) [g T3' + g' T3] = 0,
and the zero of that equation on the grid gives
  beta 2: local zero of E0' + (gT3)'/n: alpha*lam = 0.06425; there (gT3)' = g T3' -7.1113e+04 + g' T3 +1.1623e+04, E0'/lam 925.89
  beta 5: local zero of E0' + (gT3)'/n: alpha*lam = 0.02147; there (gT3)' = g T3' -1.4590e+05 + g' T3 +3.9526e+04, E0'/lam 4953.99
against 0.06412 / 0.02143 from the frozen sweep. The term that carries it is g T3', and T3' is dominated by Vh(lam) moving along
the n = inf path (Vh' = +4.1 at beta 2, +10.1 at beta 5): holding T3 at Vh(0), as the first version of this formula did, gives
0.044 / 0.0069. Straight-line fits over the whole 0.003-0.3/alpha range overshoot (0.068 / 0.024) because E0 is not quadratic and
g T3 is not linear across a factor 100 in lam; the local zero is the right reading.
Status: alpha lam_risk = frozen (0.064 / 0.021, closed as above) + feedback of the extra variance into Vh, A1, R2 (0.013 / 0.008,
open). How the fixed-N formula of the 20:20 section (0.052 / 0.0135) maps onto these two terms is not yet checked.

## 20 Oct 22:04 (claude-99aebc7f): k_risk - the feedback share is the first-order response of the reduced fixed point
cgmt_response.py writes the reduced system as e(x, eps) = 0, x = (mu, s = sg^2), eps = 1/n, with
e1 = mu + A1 T1, e2 = mu^2 + s - A1^2 T2 - eps R2 T3, and differentiates at the n = inf root x0:
    dE/deps = grad E . J^{-1} (0, R2 T3),   J = de/dx at x0;   frozen = dE/ds R2 T3 = (Vh/2) R2 T3 (Stein).
So alpha lam_risk solves E0'(lam) + (1/n) d/dlam [grad E . J^{-1} (0, R2 T3)] = 0, and the feedback share is the lam-slope of
R2 T3 [grad E . J^{-1} e2 - Vh/2]. Central differences at relative step 1e-4 (1e-6 was roundoff-limited: the Stein check
was off by 4 pct at the smallest lam and the answer read 0.081):
  beta 2: Stein check dE/ds = Vh/2 at three lam: 4.833900e+02/4.833900e+02 4.988070e+02/4.988040e+02 5.005705e+02/5.004435e+02
          first order, frozen only: alpha*lam = 0.06423   with the feedback: alpha*lam = 0.07648
          feedback / frozen in dE/deps at three lam: 0.0003:-0.0066 3e-05:-0.0007 3e-06:-0.0002
  beta 5: Stein check dE/ds = Vh/2 at three lam: 4.746403e+02/4.746403e+02 5.005134e+02/5.005138e+02 5.034072e+02/5.033970e+02
          first order, frozen only: alpha*lam = 0.02148   with the feedback: alpha*lam = 0.02941
          feedback / frozen in dE/deps at three lam: 0.0003:-0.0208 3e-05:-0.0024 3e-06:-0.0002
against the solved fixed point: full 0.07683 / 0.02957, frozen 0.06412 / 0.02143 (cgmt_feedback run3). The first-order response
accounts for the whole of alpha lam_risk to 0.5 pct at both beta. The feedback is under 1 pct (beta 2) and 2 pct (beta 5) of
dE/deps itself and vanishes as lam -> 0; it moves lam_risk by 16-27 pct only because lam_risk is set by the lam-slope of dE/deps,
which is small. Status: k_risk = first-order CGMT response, verified numerically. Open: write J and grad E in the moments
(Vh, A1, R2 and their mu, sg derivatives, T1-T3) to get an explicit formula; check how the fixed-N k_risk (0.052 / 0.0135) maps onto it.

## 20 Oct 22:18 (claude-99aebc7f): k_risk in closed form (first order in 1/n, reduced CGMT fixed point)
Notation as in the 22:04 section; Q = mu Z1 + sg Z2, p = sig(Q), y the label, a = A - mu Vh, G = 1/(lam + Vh S),
T1 = sum mt^2 G/rho^2, T2 = sum mt^2 S G^2/rho^2, T3 = sum S^2 G^2, T4 = sum mt^2 S^2 G^3/rho^2. Gaussian moments:
    A = E[Z1 (p - y)], Vh = E sig'(Q), R2 = E (p - y)^2, Vm = E[Z1 sig''(Q)], Vs = E sig'''(Q)/2,
    Am = E[Z1^2 sig'(Q)] - Vh - mu Vm, As = Vm/2 - mu Vs.
By Stein (d/dmu E f(Q) = E Z1 f'(Q), d/ds E f(Q) = E f''(Q)/2) and dT1/dVh = -T2, dT2/dVh = -2 T4, the risk gradient is
grad E = (A, Vh/2) and the Jacobian of (ii)-(iii) in x = (mu, s) is
    J11 = 1 + Am T1 - a T2 Vm,              J12 = As T1 - a T2 Vs,
    J21 = 2 mu - 2 a Am T2 + 2 a^2 T4 Vm,   J22 = 1 - 2 a As T2 + 2 a^2 T4 Vs.
Then, all at the n = inf solution x0(lam),
    dE/deps = R2 T3 (J11 Vh/2 - J12 A) / det J,      eps = 1/n,
and alpha lam_risk is alpha times the root of E0'(lam) + (1/n) d/dlam dE/deps = 0. The frozen-variance part is the same with the
bracket replaced by Vh/2 (det J -> J11, J12 -> 0). cgmt_explicit.py checks every factor against central differences of the
fixed-point residual and of the risk (J to 1e-8 relative at alpha lam 0.3; at 0.003 the differences themselves lose digits
because s is small) and evaluates the root:
  beta 2: explicit first order: frozen alpha*lam = 0.06425, with the feedback alpha*lam = 0.07643
  beta 5: explicit first order: frozen alpha*lam = 0.02147, with the feedback alpha*lam = 0.02939
against the solved fixed point 0.07683 / 0.02957 and frozen 0.06412 / 0.02143: the closed form carries alpha lam_risk to 0.5 pct.
The remaining 0.5 pct is second order in 1/n or the 81-point grid; not separated.
Status: k_risk has an explicit first-order formula in the CGMT moments, verified numerically at beta 2 and 5 (alpha 1000, psi 1,
d 1000). Open: the alpha -> inf limit of alpha lam_risk as a pure lam -> 0 expansion of this formula (E0''(0) and the lam-slope
of dE/deps at x0(0)), and the relation to the fixed-N k_risk (0.052 / 0.0135).

## 20 Oct 22:42 (claude-99aebc7f): the alpha -> inf limit of alpha lam_risk
Nothing on the n = inf path depends on alpha; alpha enters only through eps = 1/n = 1/(alpha d). So, at first order in 1/n,
lam_risk(alpha) is the root of E0'(lam) + D'(lam)/(alpha d) = 0 with D = dE/deps the closed form of the 22:18 section, and E0'
is explicit as well: dx0/dlam = -J^{-1} de/dlam, de/dlam = (-A1 U1, 2 A1^2 U2), U1 = sum mt^2 G^2/rho^2, U2 = sum mt^2 S G^3/rho^2,
E0' = grad E . dx0/dlam. At lam = 0, T1 = 1/Vh and T2 = 1/Vh^2, so s = A1^2 (T2 - T1^2) = 0: the n = inf ridge path starts at
perfect alignment with the best direction and sg grows linearly in lam (s ~ c lam^2). The n = inf solver therefore has to use
s = A1^2 Var_w(S G) with w = mt^2/(S rho^2); the form mu^2 + s - A1^2 T2 cancels to 1e-9 of mu^2 and fails near lam 5e-7.
E0'(0) = 0 (the path starts at the population optimum), so E0 = E0(0) + E0''(0) lam^2/2 + ... and
    k_inf = lim_(alpha -> inf) alpha lam_risk = -D'(0) / (d E0''(0)).
cgmt_lam0.py (beta, psi 1, d 1000, F seed 100; slopes from quadratic fits on lam <= 1e-6, path solved down to 1e-8):
  beta 2:
  s/lam^2 at lam 1.0e-08, 1.0e-04: 2.327225e+03, 2.242472e+03
  E0'(0) extrapolated = 2.398e-12 (E0'(1e-6) = 9.029e-04); E0''(0) = 9.516781e+02; D(0) = 5.006268e+02; D'(0) = -7.308345e+04
  k_inf = lim alpha lam_risk = -D'(0) / (d E0''(0)) = 0.07679
  alpha 10: alpha lam_risk = 0.07468 (first order in 1/n, full lam dependence)
  alpha 100: alpha lam_risk = 0.07408 (first order in 1/n, full lam dependence)
  alpha 1000: alpha lam_risk = 0.07643 (first order in 1/n, full lam dependence)
  alpha 10000: alpha lam_risk = 0.07676 (first order in 1/n, full lam dependence)
  alpha 100000: alpha lam_risk = 0.07679 (first order in 1/n, full lam dependence)
  beta 5:
  s/lam^2 at lam 1.0e-08, 1.0e-04: 1.186692e+04, 1.107743e+04
  E0'(0) extrapolated = 4.788e-11 (E0'(1e-6) = 4.782e-03); E0''(0) = 5.042780e+03; D(0) = 5.037212e+02; D'(0) = -1.489350e+05
  k_inf = lim alpha lam_risk = -D'(0) / (d E0''(0)) = 0.02953
  alpha 10: alpha lam_risk = 0.02562 (first order in 1/n, full lam dependence)
  alpha 100: alpha lam_risk = 0.02836 (first order in 1/n, full lam dependence)
  alpha 1000: alpha lam_risk = 0.02939 (first order in 1/n, full lam dependence)
  alpha 10000: alpha lam_risk = 0.02952 (first order in 1/n, full lam dependence)
  alpha 100000: alpha lam_risk = 0.02953 (first order in 1/n, full lam dependence)
The alpha = 1000 roots reproduce cgmt_explicit (0.07643 / 0.02939). The limit is reached to 0.5 pct (beta 2) and 0.5 pct (beta 5)
at alpha 1000. The alpha 10 and 100 rows are first order in 1/n only; there the prox step and the second-order terms are not
small, so they are not predictions of the solved fixed point. Smell test: D(0) = 500.6 and 503.7, close to N/2 = 500, the
classical N/(2n) excess of an unregularised well-specified fit (R2 = Vh when the model is calibrated, T3(0) = N/Vh^2).
Status: k_risk has an explicit first-order formula and an explicit alpha -> inf limit, 0.0768 (beta 2) and 0.0295 (beta 5),
the ratio of two lam-derivatives at the population optimum. Open: E0''(0) and D'(0) as closed expressions in the lam = 0
moments (both are numerically exact here), and the relation to the fixed-N k_risk (0.052 / 0.0135).

## 21 Oct 00:17 (claude-99aebc7f): the lam = 0 quantities of the alpha -> inf limit in closed form
At lam = 0 on the n = inf path, s = 0 and A(mu0) = 0, so T1 = 1/Vh, T2 = 1/Vh^2, T4 = 1/Vh^3, T3 = N/Vh^2, and the Jacobian
collapses: J11 = A_mu/Vh with A_mu = E[Z1^2 sig'(mu0 Z1)], J21 = 2 mu0 J11, J12 = Vm/(2 Vh), J22 = 1 + mu0 Vm/Vh, det J = J11.
Hence D(0) = N R2/(2 Vh) exactly (the N/(2n) excess, scaled by the calibration ratio R2/Vh).
The moments are even in sg, so s = O(lam^2) does not enter at first order. With w = mt^2/(S rho^2) (a probability vector) and
g = S G = 1/Vh - lam/(Vh^2 S) + ...:
    mu'(0) = m1 = -mu0 E_w(1/S)/A_mu,    s = c lam^2 + ...,  c = mu0^2 Var_w(1/S)/Vh^2,
and since E_mu = A, E_s = Vh/2, E_mumu = A_mu,
    E0''(0) = A_mu m1^2 + Vh c = mu0^2 [ E_w(1/S)^2 / A_mu + Var_w(1/S) / Vh ].
The two terms are the shrinkage of the norm along the best direction and the rotation off it. D'(0) is carried almost entirely
by T3 = sum S^2 G^2: dT3/dlam = -2 sum(1/S)/Vh^3 and dT3/dVh = -2 N/Vh^3, so D'(0) = -2 D(0) [mean(1/S) + Vh_mu m1]/Vh up to
the lam-dependence of R2 and J, which is 0.08 pct (beta 2) and 0.45 pct (beta 5) of D'(0). Together,
    k_inf ~ psi (R2/Vh) [mean(1/S) + Vh_mu m1] / ( Vh mu0^2 [ E_w(1/S)^2/A_mu + Var_w(1/S)/Vh ] ),
spectral data of S entering only through mean(1/S), E_w(1/S) and Var_w(1/S). cgmt_lam0_closed.py evaluates these with no path
solve (mu0 from A(mu0) = 0 at s = 0; D'(0) by a central difference along the first-order path):
  beta 2:
  mu0 1.484324 (A(mu0) = 8.3e-18); Vh 0.177604; R2 0.177827; R2/Vh 1.001254; A_mu 0.094408
  E_w(1/S) 4.802952; Var_w(1/S) 33.318669; mean(1/S) 8.720457; m1 -7.551435e+01; c = s/lam^2 2.327234e+03
  D(0) closed N R2/(2 Vh) = 5.006268e+02; from the full formula 5.006268e+02
  E0''(0) closed = 9.516782e+02  (A_mu m1^2 5.3835e+02 + Vh c 4.1333e+02)
  D'(0) = -7.308346e+04; D(0) T3'/T3 = -7.302352e+04 (0.9992 of it)
  k_inf = -D'(0)/(d E0''(0)) = 0.07679
  beta 5:
  mu0 2.484408 (A(mu0) = 1.6e-17); Vh 0.131643; R2 0.132622; R2/Vh 1.007442; A_mu 0.040908
  E_w(1/S) 4.802952; Var_w(1/S) 33.318669; mean(1/S) 8.720457; m1 -2.916892e+02; c = s/lam^2 1.186701e+04
  D(0) closed N R2/(2 Vh) = 5.037212e+02; from the full formula 5.037212e+02
  E0''(0) closed = 5.042781e+03  (A_mu m1^2 3.4806e+03 + Vh c 1.5622e+03)
  D'(0) = -1.489351e+05; D(0) T3'/T3 = -1.482619e+05 (0.9955 of it)
  k_inf = -D'(0)/(d E0''(0)) = 0.02953
Against the path solve of cgmt_lam0 run1: E0''(0) 951.6781 / 5042.780, D(0) 500.6268 / 503.7212, D'(0) -7.308345e4 / -1.489350e5,
k_inf 0.07679 / 0.02953, agreement to six or seven digits. The beta-dependence sits in mu0, Vh, A_mu, R2 alone; the spectral
numbers (E_w(1/S) 4.803, Var_w(1/S) 33.32, mean(1/S) 8.720) are the same for both beta at this F.
Open: the fixed-N k_risk relation (0.052 / 0.0135), and whether the weighted spectral moments have deterministic equivalents
(Marchenko-Pastur for mean(1/S); E_w and Var_w need the overlap of mt with the eigenvectors).

## 21 Oct 03:39 (claude-99aebc7f): the fixed-N k_risk formula agrees with the CGMT limit once H moves along the path
The 20:20 section's leave-one-out formula (0.052 / 0.0135) held H fixed along the ridge path. Its missing piece is the
full-rank part of dH/dlam: on the n = inf path da/dlam = -H^-1 a, so dq^2/dlam = -2K with K = a'Sig H^-1 a, and
Vh = E sig'(z), z ~ N(0, q^2), moves by Vh' = -gam K (gam = E sig'''(z)). The variance term then carries mean(1/s) + Vh'
in place of mean(1/s):
    k_risk = psi [ 2 E(rho'' rho' zeta)/Vh + (mean(1/s) + Vh') E rho'^2 / Vh^2 ] / (a_0' H^-1 a_0).
The 20:20 text gave K = 23.3 and so put this term at 10 pct. K is 112.09 at beta 2 and 724.69 at beta 5 (Sherman-Morrison on
Vh Sig + gam (Sig a)(Sig a)': K = q^2 E_w(1/s)/(Vh + gam q^2), and Vh + gam q^2 is the CGMT's A_mu). risk_gap_full.py:
  beta 2 (lam0 1e-8, 1e-6):
   K = a'Sig H^-1 a 112.0875; Vh' = -gam K 4.2326; with the curvature move k_risk 0.07686 (variance term alone 0.07673)
   K = a'Sig H^-1 a 112.0602; Vh' = -gam K 4.2319; with the curvature move k_risk 0.07687 (variance term alone 0.07675)
  beta 5:
   K = a'Sig H^-1 a 724.6900; Vh' = -gam K 10.6530; with the curvature move k_risk 0.02967 (variance term alone 0.02940)
   K = a'Sig H^-1 a 724.2832; Vh' = -gam K 10.6497; with the curvature move k_risk 0.02967 (variance term alone 0.02941)
Against the CGMT limit k_inf 0.07679 / 0.02953 (cgmt_lam0_closed run1), the alpha 1000 sweep 0.0768 / 0.0296 and the direct
simulation 0.077 +- 0.003 (beta 2). The term-by-term match with the 00:17 closed form:
    a_0' H^-1 a_0 = E0''(0)          951.675 / 5042.87 against 951.678 / 5042.78,
    Vh' = -gam K = Vh_mu m1          4.2326 / 10.653 against 4.233 / 10.75 (read off D'(0)),
    N E rho'^2 mean(1/s)/Vh^2        = the mean(1/S) part of -D'(0), since D(0) = N R2/(2 Vh) and R2 = E rho'^2,
so the two derivations are the same expansion. The misspecification term 2 E(rho''rho'zeta)/Vh is 0.2 pct of k at beta 2
and 0.9 pct at beta 5; the beta 5 residual against the CGMT (+0.47 pct with it, -0.44 pct without) is the size of the lam-
dependence of R2 and J that the 00:17 section put at 0.45 pct, so the fixed-N formula is right to that order and the 20:20
"remaining 25 percent" was the curvature move alone.
Status: k_risk = lim alpha lam_risk has a closed form in n = inf quantities, checked against the CGMT fixed point, its 1/alpha
expansion and direct simulation. Open: deterministic equivalents of mean(1/S), E_w(1/S), Var_w(1/S) in the random-features
spectrum.

## 21 Oct 04:56 (claude-99aebc7f): the spectral data in closed form, and k_inf in the d -> inf limit
With Sig = mu1^2 F F' + mus^2 I (F N x d, N(0, 1/d) entries, psi = N/d), t = mus^2/mu1^2, mt = V'(mu1 F e1), let m be the
Stieltjes transform of the Marchenko-Pastur law of F F' (ratio psi),
    m(z) = (1 - psi - z - sqrt((1 - psi - z)^2 - 4 psi z)) / (2 psi z),
and G(z) = e1'F'(F F' - z)^{-1} F e1. Since F'(F F' - z)^{-1} F = I + z (F'F - z)^{-1} and F'F is rotation invariant with
law psi mu + (1 - psi) delta_0, G(z) -> psi (1 + z m(z)), the transform of nu(dl) = psi l mu(dl). So in the limit
    mean(1/S) = m(-t)/mu1^2,   rho^2 = G(-t),   E_w(1/S) = G'(-t)/(mu1^2 G(-t)),   E_w(1/S^2) = G''(-t)/(2 mu1^4 G(-t)),
and Var_w(1/S) = E_w(1/S^2) - E_w(1/S)^2. At psi 1 (tanh features, t 0.074726): mean(1/S) 8.70093, rho^2 0.761461,
E_w(1/S) 4.93961, Var_w(1/S) 33.6704. A quadrature of mu (theta substitution, 4000 nodes) reproduces all of them to the
digits printed (rf_limit_99aebc7f/cgmt_lam0_deteq.py, _b2_run1, _b5_run1). mean(1/S) is a normalized trace and is already
within 0.2 pct at d 1000; the weighted quantities are quadratic forms in F e1 and fluctuate at order d^{-1/2} (E_w(1/S) sd 0.16
over five seeds at d 1000).
k_inf recomputed on the limiting measure (cgmt_lam0_closed's D'(0) and E0''(0) with the spectrum replaced by the quadrature
nodes) against cgmt_lam0_closed at finite d (cgmt_lam0_closed_seeds_run1.txt):
    beta 2:  limit 0.07396;  d 1000 seeds 100-104: 0.07679 0.07443 0.06878 0.07189 0.07255 (mean 0.0729, sd 0.0030);
             d 3000 seeds 100-101: 0.07501 0.07554.
    beta 5:  limit 0.02831;  d 1000 seeds 100-104: 0.02953 0.02796 0.02664 0.02881 0.02810 (mean 0.0282, sd 0.0011);
             d 3000 seeds 100-101: 0.02903 0.02823.
So the values 0.0768 / 0.0295 quoted in the 22:42 and 03:39 sections are the k_inf of the one F drawn at seed 100, d 1000; they
sit 4 pct above the d -> inf value, inside the seed spread. The d -> inf coefficient is 0.0740 at beta 2 and 0.0283 at beta 5.
Status: k_risk = lim alpha lam_risk now has a closed form in Gaussian moments of the n = inf fit and the Marchenko-Pastur
transform m(-t) and its first two derivatives; nothing in it is left as an empirical spectral average.

