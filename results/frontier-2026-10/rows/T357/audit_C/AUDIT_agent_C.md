# T357 logistic-ridge proportional limit (DOSSIER 19 Oct 17:0x - 20 Oct 01:1x), audit 1 (agent C, 20 Oct 2026 04:4x)

Objects:
- The leave-one-out (CGMT) system for logistic ridge in cgmt_ridge.py.
- The table of lam_cal/lam_risk.
- The conclusion "Target 1 for ridge is false as stated but true to O(1/alpha)", with alpha_c(beta) where the sign changes.

Verdict:
- The system is CONFIRMED and the fixed point is reproduced independently.
- The conclusion holds only for the calibration measure the CGMT section uses. That measure is not the one that defined lam_cal
  earlier in the same dossier, and under the earlier one the sign change does not appear at any point tested.

## The system, re-derived

With Q = mu Z1 + s Z2, P = prox_{c rho_y}(Q) and rho_y(t) = softplus(t) - y t:
- (i) lam mu = -E[Z1 rho'_y(P)]. This is stationarity in the teacher direction.
- (ii) 1/alpha = 1 - E[1/(1 + c rho''(P))] + lam c. I derived it from the leave-one-out resolvent by Sherman-Morrison: the
  per-sample leverage c rho''/(1 + c rho'') averages to 1/alpha minus the ridge share lam c.
- (iii) s^2 = alpha c^2 E[rho'_y(P)^2]. This is El Karoui's variance equation in the same normalisation.

All three agree with cgmt_ridge.py term by term.

## Independent numerics (cgmt_indep.py, run_a*.txt)

My solver differs from the row's in method:
- Every Gaussian average is a trapezoid on a uniform grid, H = 0.05 on [-10, 10], not Gauss-Hermite.
- The population risk and calibration integrals use adaptive quadrature in the fitted score.
- The prox is solved by Newton to 1e-14.
- The fixed point is followed by continuation from lam = 30.

Each run reports three roots:
- lam_risk, the minimum of the population logistic risk.
- lam_FM, the root of FM = E[(p - E[y|p]) zhat]. This is the measure of the CGMT section and of the path lemma.
- lam_OC, the root of OC = E[(p - E[y|p]) sign(zhat)]. This is the signed over-confidence that defined lam_cal in the 19 Oct
  setup, the finite-d table and the d = 800 check.

| alpha | beta | lam_risk | lam_FM / lam_risk (row's value) | lam_OC / lam_risk | FM, OC at lam_risk |
|---|---|---|---|---|---|
| 3  | 5 | 0.02600874 | 1.038357 (1.03838; lam_risk 0.0260059) | 1.103629 | +3.9e-3, +5.6e-3 |
| 12 | 5 | 0.004149726 | 0.999525 (0.99948 at 80 nodes) | 1.072392 | -2.7e-5, +1.9e-3 |
| 30 | 5 | 0.001463289 | 0.997982 (0.9978 at 80, 0.9980 at 140 nodes) | 1.069849 | -5.6e-5, +9.1e-4 |
| 30 | 2 | 0.008740361 | 0.999616 (0.9996) | 1.027796 | -1.1e-5, +4.9e-4 |

The FM column reproduces the row to the precision its node counts allow, and the residuals of the three equations are below 1e-16.

## The finding

- The 19 Oct table set lam_cal at the sign change of OC. The CGMT section, from 17:0x, sets lam_cal at FM = 0. The two roots are
  different points.
- At lam_risk, OC is positive (over-confident) in all four settings. That includes three settings past the FM crossing
  (alpha_c(5) in (11, 12) and alpha_c(2) in (12, 15)), where FM is already negative.
- So under the definition the row started from, "the calibrating lambda exceeds the risk-optimal one" holds at every point tested,
  with ratios of 1.03 to 1.10. These are not the 0.1-percent differences of the FM measure.
- The two OC points at beta 5 (1.072 at alpha 12 and 1.070 at alpha 30) do not show the 1/alpha decay that FM shows. Two points
  are not enough to say what the OC gap does as alpha grows.
- The sign change at alpha_c(beta), and the 1/alpha closing, are statements about the first-moment measure FM. They are correct
  for FM. The sentence "Target 1 for ridge is false as stated" needs the measure named. With OC as the measure, ridge gives no
  counterexample in this range.

Two smaller points:
- The finite-d OC ratios at alpha 3, beta 5 (1.131 at d = 400 over 4 seeds, 1.152 at d = 800 over 2 seeds) sit above the limit
  value 1.104, and d = 800 is further from it than d = 400. The per-seed spread (1.07-1.28) is larger than either gap, so this is
  not a contradiction, but it is not the convergence one would like to see either. More seeds at d = 800 and 1600 would settle it.
- The path lemma (sign FM = sign drho/dq at lam_risk) is about FM only. It says nothing about OC, so the "WHAT REMAINS FOR A
  THEOREM" paragraph covers the FM question and not the OC one.

## Not covered

- GD (DMFT) and the random-feature case.
- An OC sweep in alpha. The next useful run is lam_OC/lam_risk at alpha 60, 100 and 400 at beta 5, with this solver.
- A grid-convergence check of my H = 0.05 trapezoid. The alpha 3 row matches the row's 80-node value to 2e-5 in the ratio, but no
  H = 0.035 run was made.
