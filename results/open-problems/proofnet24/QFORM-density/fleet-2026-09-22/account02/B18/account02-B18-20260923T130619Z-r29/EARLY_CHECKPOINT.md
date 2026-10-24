# account02/B18 r29 early checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: substantive partial result; full QFORM remains OPEN.

## First unpaid implication at entry

The previous B18 debt was `QFORM-CIRCULAR-THREEDIM-PROVENANCE-TWOSHEET-v1`: uniformly control the negative/two-sheet side of the exact target-valid circular family

`Q_m = 2/sqrt(1+m^2) (Y_1+mX_0)Y_2 + Y_3^2`,

whose physical nonzero spectrum is exactly `{-1,1,1}`, without replacing the genuine original-coordinate product provenance by a generic 3D density cap.

## Designated-partner theorem closes that debt

The completed designated partner account03/B18 r28 is

`yspennstate/math-open-problems@43b16ba3992035298289170540682e8aa62a9ad4`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T120257Z-account03-B18-QFORM-r28/REPORT.md`.

For a Schur-isotropic packet

`Q=(Y+r n X_0)^T D(Y+r n X_0)`, `V^T V=I_3`, `n^T D n=0`,

it proves, whenever every residual row has transverse leverage

`q_j=||P_(n^perp)v_j||^2<=1/2`,

that

`||p_Q||_infinity <= 3*2^(4/3) [r^2 |det D|]^(-1/3)`,

with a continuous `C_0` density. This is an original-product mixed-Fresnel theorem; it does not infer independence after a spectral rotation.

For the circular B18 family,

`v_j=m^(-1/2)(1,sqrt(2)cos(2pi j/m),sqrt(2)sin(2pi j/m))`, `n=e_1`, `r=m`,

so exactly

`q_j=2/m`.

Hence for every `m>=4` the partner gate holds, while

`|det D|=1/(1+m^2)`.

Therefore the PREVIOUSLY UNPAID WHOLE-LINE inequality is now

`||p_(Q_m)||_infinity <= 3*2^(4/3)(1+m^(-2))^(1/3)`.

The right side decreases in `m`; at `m=4` it is

`3*2^(4/3)(17/16)^(1/3)=7.713844771974705...`,

and it tends to `3*2^(4/3)=7.559526299369239...`.

Thus the circular negative/two-sheet obstruction is CLOSED, continuously, for all `m>=4`.

For comparison, the pinned e5f ruled one-sheet theorem still gives the sharper one-sided statement `p_(Q_m)(t)<=pi*sqrt(2)` for a.e. `t>=0`; the new partner transfer is what now pays the negative side as well.

## New complementary structural calculation

In the remaining moderate/high-shear branch `r>=1/2`, failure of the partner gate means some original residual coordinate `i` has `q_i>1/2`. The same exact null-hub shear used in account03/B10 gives leaf vectors `alpha,beta` with orthonormal columns, `q_j=alpha_j^2+beta_j^2`, and for hub-leaf couplings `g_j` a canonical local block

`[[0,g_i,g_j],[g_i,d beta_i^2,d beta_i beta_j],[g_j,d beta_i beta_j,d beta_j^2]]`

up to a determinant-one hub shear. Therefore

`|det A[{0,i,j}]| = h |det M| (alpha_i beta_j-alpha_j beta_i)^2`.

Summing over `j!=i` and using Parseval in the two transverse columns gives

`sum_(j!=i) |det A[{0,i,j}]| = h |det M| q_i`.

Under the account03/B18 Schur whitening, `h|det M|=r^2|det D|`, while

`(1+r^2)|det D|=|pdet A|`.

Thus, if the three nonzero physical eigenvalues have modulus at least `s`,

`sum_(j!=i) |det A[{0,i,j}]| >= [r^2/(1+r^2)] s^3 q_i`.

For `r>=1/2` and `q_i>1/2`, this is strictly greater than `s^3/10`; in the owner normalization `s=1`, it is `>1/10`.

This is an aggregate original-coordinate curvature certificate, not a claim that one physical 3x3 minor is uniformly large. The next unpaid implication is to turn this fixed-two-anchor triple-minor star mass into a product-preserving density bound without selecting one tiny leaf minor or replacing the source law by a generic joint density.
