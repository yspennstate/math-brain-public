# RS-2026-CL-A ownership-preserving handoff to P08/P09 — coefficient-direction frame lemma

Source ownership remains **RS-2026-CL-A / C02**, native ID `6aa7b4b639a08191b893e2b7dd6cdf59`. This file shares only reusable correlation/chaos lemmas with P08 Gaussian Phase Retrieval and P09 Gaussian Tensor Bounds; it does not claim their targets or alter their ownership.

## Exact basis-independent frame identity

Let `R` be any reference probability law and let centered local scores `h_1,...,h_m in L2(R)` have nonzero variances. For a signed score

`F=sum_j a_j h_j`,

put

`b_j=a_j sqrt(Var_R h_j)`,

`Gamma_{j ell}=Corr_R(h_j,h_ell)`.

Then exactly

`Var_R(F)=b^T Gamma b`,

so the coefficient-direction frame ratio is

`kappa_F=(b^T Gamma b)/(b^T b)`.

This is often substantially weaker than requiring a uniform inverse-Gram estimate: for one target statistic only its actual Rayleigh quotient must stay nondegenerate. A sufficient uniform condition is `lambda_min(Gamma)>=kappa_0>0`; a simple check is

`sup_j sum_{ell != j}|Corr_R(h_j,h_ell)| <= delta<1`,

which gives `lambda_min(Gamma)>=1-delta` by Gershgorin.

## Transfer once a model-specific chaos residual is available

Suppose a stationary noise/semigroup operator `T` is diagonal with respect to an orthogonal degree decomposition, source low-degree advantage through degree `D` is at most `A`, and each local score has a deterministic residual guard

`||Pi_{>D} T h_j||_infinity <= sqrt(Var_R h_j) t_j`.

Then for `F=sum_j a_j h_j`,

`|E_{PT}F-E_R F|
 <= A sqrt(Var_R F) + sum_j |b_j| t_j`.

Define

`s_F=(sum_j |b_j|t_j)^2/(sum_j b_j^2)`.

Then

`|E_{PT}F-E_R F|/sqrt(Var_R F)
 <= A + sqrt(s_F/kappa_F)`.

Thus the obstruction to transfer is explicitly separated into (i) correlation/frame collapse and (ii) persistent source-high-degree local chaos.

## Gaussian/Hermite caveat and use

For Gaussian `R`, Hermite basis functions are unbounded, so a global `L_infinity` residual guard generally cannot be obtained from coefficient counting alone. Do **not** import the Boolean unit-modulus step. Instead combine the frame identity with a P08/P09-specific residual mechanism such as:

- a high-probability typical-set Hermite envelope plus control of the exceptional set;
- leverage/Christoffel trimming;
- clipping of the score before polynomial approximation;
- a model-specific operator-norm or tensor-contraction bound on `Pi_{>D}T h_j`.

The frame identity itself is exact for Gaussian-process/tensor local scores and may replace a stronger global inverse-covariance assumption when only one coefficient direction is relevant.

Primary proof remains in RS-2026-CL-A report `runs/2026-09-20/2026-09-20T10-39-27Z__report.md`.