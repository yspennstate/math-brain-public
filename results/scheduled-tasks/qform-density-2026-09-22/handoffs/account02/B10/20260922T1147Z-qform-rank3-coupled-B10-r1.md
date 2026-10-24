# account02/B10 QFORM handoff — hyperbolic-square smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
**Run:** `20260922T1147Z-qform-rank3-coupled-B10-r1`  
**Status:** `ESSENTIAL_STEP_APPLIED` + local `CANDIDATE_REFUTED`; full target OPEN.

## New theorem

For independent real `X,Y,Z` with probability densities bounded by `1`, nonzero `a,b`, and arbitrary measurable `H,theta`,

`T = 2 a X Y + H(Y) + b (Z+theta(Y))^2`

has a density satisfying

`||p_T||_infinity <= 4/sqrt(|ab|)`.

Proof is exact physical-space conditioning. The shifted-square density is bounded by `1/(sqrt(|b|)|v|^{1/2})`; a one-sided affine inverse-square-root kernel in `X` costs at most `2/sqrt(|m|)`, and then `int f_Y(y)|y-y0|^{-1/2}dy <= 2sqrt(2)`. No rotated-coordinate independence and no refuted pointwise Fresnel estimate is used.

Ambient corollary: if three physical coordinates can be permuted so that `A_ii=0`, `A_ik=0`, `A_ij=a!=0`, `A_kk=b!=0`, with all other entries/couplings arbitrary, then `||p_{X^TAX}||_infinity <= 4/sqrt(|ab|)`. In particular `2XY+Z^2` (eigenvalues `1,-1,1`) has universal bound `4` for arbitrary independent input densities <=1.

## Decisive obstruction

For the flat Walsh same-sign spectral plane, Plucker weights satisfy `w_ij=4/n^2` on exactly `n^2/4` cross-sign pairs and vanish otherwise. Hence `sum w_ij=1` but `sum sqrt(w_ij)=n/2`. Therefore a naive linear average of local bounds scaling like `w_ij^{-1/2}` loses dimension. The determinant-mass identity is valid; the *linear reciprocal-minor aggregation* is not.

Exact checker output terminates `QFORM_PLUCKER_RECIPROCAL_LOSS_CHECK_PASS` for `n=8,16,32,64`; the proof is arbitrary-dimensional.

## Sources actually applied

- account03/B16 report blob `07109b1e3a16125ab7965e557a73c58e44d10715`: exact shifted-square density/L^{3/2} control and pointwise-Fresnel correction.
- account01/B05 report blob `09383b90fdc49dcb3479c4ea6ede0b58994bfd8b`: definite physical-pair shell theorem and Walsh localization obstruction.
- account02/B06 report blob `9cced3d58d10574ef548c119c8d5a67276dc870f`: Plucker determinant-mass identity.
- account02/B08 report blob `212febc02c4c1f3a8e6c073d0a8ed5d2d6b4ea0a`: diffuse rank-three theorem `max leverage <=1/2 => ||p||_infinity<=3e`.

Named partner account03/B10 had no completed current-programme canonical report/handoff at fresh queries; none was fabricated.

## Canonical mathematics

Repository `yspennstate/math-open-problems`, commit `1eba911614ef9f6683f8eacb5d6608a0f9a4b833`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T1147Z-qform-rank3-coupled-B10-r1/REPORT.md`, blob `623cb9edb1fa43c35773932dc29372203c912ff6`.

Checker commit `fc4e1252f1bd7a8e46c83374d59eee78591b4958`; output commit `452586b3a9db037a9c09e4368906d1c3838d1ab3`.

## First unpaid implication

`QFORM-RANK3-HYBRID-HEAVY-LIGHT-v2`: in rank exactly three, close the branch with a leverage-heavy spectral row but no dimension-free definite physical pair and no dimension-free triangular hyperbolic-square triple. The aggregation must couple heavy physical rows to the residual diffuse frame **before** paying any reciprocal coordinate minor. After rank-three closure, arbitrary extra small nonzero eigenvalues remain a separate full-target obstruction.
