# fleet02/B03 early substantive checkpoint — sharpened parabolic-hub half-Frostman constant

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T041654Z-fleet02-B03-QFORM-auto11`  
Assignment: Decoupled time integral.  
Status at checkpoint: supporting calculation proved; full target open.

The latest partner result fleet03/B03 r25 proves for

`R=aX^2+LX+S`,

with `X` independent of `(L,S)`, `||p_X||_infinity<=1`, and `||p_L||_infinity<=M`, a half-Frostman bound with constant `4(1+sqrt(3))`. The same proof admits a smaller universal constant.

Write `A=|a|` and `r=AM`. In the nonzero-`a` proof, for any `K>1`, its near/far split gives

`P(|R-z|<=eps) <= 4 sqrt(M eps) [ sqrt(r(K+1)) + 1/sqrt(r(K-1)) ].`    (1)

If `r<=1/9`, choose `K-1=1/r`. Then

`P(|R-z|<=eps) <= 4[ sqrt(1+2r)+1 ] sqrt(M eps)`

`<= 4[1+sqrt(11)/3] sqrt(M eps) < 6 sqrt(2) sqrt(M eps).`          (2)

If `r>=1/9`, use instead the unconditional scalar quadratic sublevel estimate from the same partner proof,

`P(|R-z|<=eps) <= 2 sqrt(2 eps/A)`

`=2 sqrt(2) r^(-1/2) sqrt(M eps) <= 6 sqrt(2) sqrt(M eps).`        (3)

The `a=0` case is `<=4 sqrt(M eps)`. Therefore uniformly in every real `a`, arbitrary dependence between `L` and `S`, and arbitrary translations,

`boxed: sup_z P(|R-z|<=eps) <= 6 sqrt(2) sqrt(M eps).`             (4)

For the product-source specialization `L=2m^T Y+beta`, the completed one-dimensional projection theorem gives `M<=1/(sqrt(2)||m||_2)`, hence

`boxed: sup_z P(|R-z|<=eps) <= 6*2^(1/4) ||m||_2^(-1/2) eps^(1/2).` (5)

Next step in this run: apply the completed physical-indefinite-pair logarithmic transducer from the pinned Claude package, which consumes exactly a half-power remainder small-ball bound, rather than degrading (5) to a quarter-power bound. This should produce a scale-homogeneous full density certificate proportional to `( |det B| sigma_min(B) ||m||_2 )^(-1/4)` and an improved dependence-safe weighted independent-copy time estimate.

Sources actually used at this checkpoint:
- fleet03/B03 r25: `yspennstate/math-open-problems@f445f3dd7e2b845f96ac58cc4bd96f12ec7a839c:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T031216Z-fleet03-B03-QFORM-r25/REPORT.md`.
- pinned Claude package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` (physical indefinite-pair logarithmic smoothing statement).

No conjugate sum/difference variables are declared independent; no post-rotation independence, moment, support, or pointwise law-uniform stationary-phase premise is used.
