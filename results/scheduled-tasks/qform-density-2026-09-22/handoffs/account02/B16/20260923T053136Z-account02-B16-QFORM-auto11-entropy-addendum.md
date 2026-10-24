# Supplemental handoff — near-coloop capped-basis entropy barrier

Programme: `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.15`.  
Worker: account02/B16, Projection-product interaction.  
Run: `20260923T053136Z-account02-B16-QFORM-auto11`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Status: new supporting theorem + exact proof-engine obstruction; full QFORM remains open.

Canonical new mathematics:

`yspennstate/math-open-problems@2f75117bdad55f4c825bccb1aa0dca301056fed7:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T053136Z-account02-B16-QFORM-auto11/ADDENDUM-CAPPED-BASIS-ENTROPY.md`.

Read this together with the run's immutable `REPORT.md` and `CORRECTION.md`.

## New theorem

For an exact-rank-three Parseval frame, let the natural Pluecker law be

`v_S=det(R_S)^2`,

and let one physical coordinate have leverage `c`, with `a=1-c`. For every probability law `w` on nonsingular physical triples whose every coordinate inclusion marginal is at most `1/2`, define

`Z_w=exp(H(w)+sum_S w_S log v_S)`.

Then

`Z_w=exp(-D_KL(w||v)) <= 2 sqrt(c(1-c))`.

Proof: under `v`, the binary event that the hub is absent has probability `a`; under any capped law `w` it has probability `q>=1/2`. Data processing gives `D_KL(w||v)>=d_Ber(q||a)`, whose minimum over `q>=1/2` is at `q=1/2`, namely `-log(2 sqrt(ac))`.

Therefore the completed account03/B16 r26 capped-basis Fresnel certificate

`3e(D Z_w)^(-1/3)`

cannot remain uniform in the true near-coloop limit at fixed determinant resource: its best possible score is at most order `sqrt(a)`, so this proof engine necessarily loses at least the `a^(-1/6)` scale. This is not a lower bound on the true density.

## Sharp target-valid family

Let `m>128` be divisible by four and use all four balanced sign pairs `(sigma_j,tau_j)`. Put `eta_j=sigma_j tau_j` and

`r_0=sqrt(c)e_1`,
`r_j=(sqrt(a)eta_j,sigma_j,tau_j)/sqrt(m)`.

These rows form a Parseval frame. With coefficient matrix

`B=[[0,1,0],[1,0,0],[0,0,1]]`,

`A=RBR^T` has nonzero spectrum `{1,-1,1}`. The rows occupy only five spectral line directions. The completed account02/B16 theorem `QFORM-FINITE-LINE-BANK-COMPRESSION-v1`, source `yspennstate/math-open-problems@b9e19e2c19ecd6f6ede282cd3c73ad014c449e9f`, therefore gives

`||p_Q||_infinity <= 2 C_3 binom(5,3)^(1/3)=449.0569661600281...<450`

for every independent cap-one original-coordinate input law, uniformly as `a->0`.

For this same family the entropy barrier is exact. Take

`w_*=(1/2)v(.|hub in)+(1/2)v(.|hub out)`.

The hub marginal is `1/2`; every leaf marginal is `(1/2)(2/m)+(1/2)(3/m)=5/(2m)<1/2`; and

`D_KL(w_*||v)=-log(2 sqrt(ac))`, hence `Z_{w_*}=2 sqrt(ac)`.

So the `a^(-1/6)` degradation of the capped-basis certificate is structurally forced even on a family whose true density is uniformly bounded.

## Required pinned source application

The required Claude package at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

applies its ruled one-sheet theorem to this exact-rank-three indefinite family and gives the real curved inequality

`ess sup_{majority-sign levels} p_Q <= pi sqrt(2)`.

Its use of a two-dimensional product projection does not assert projected independence.

## Partner integration and next step

Designated partner source actually used:

`yspennstate/math-open-problems@d6730c301e46e6337bc3b32e30eb3d04f07dc90b:proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T045948Z-account03-B16-QFORM-r26/REPORT.md`.

Partner r26 closes broad exact-rank-three chambers but leaves the true near-coloop collar `c>63/64`. The entropy theorem proves that a uniform solution cannot come merely from optimizing the r26 capped-basis law while retaining the `alpha_k<=1/2` constraint.

First unpaid implication: `QFORM-NEAR-COLOOP-SOURCE-PROVENANCE-TRANSITION-v1`. Retain the original hub factor and the common-source longitudinal/transverse modulation before completion or full absolute value. For indefinite exact rank three the pinned Claude theorem already pays the majority-sign side, so the remaining curved debt is the minority/two-sheet side. Arbitrary higher-rank spectrum remains a separate global debt.
