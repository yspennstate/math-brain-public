# RS-2026-CL-A reusable handoff to P08/P09 — spectral-dimension tail

Ownership: the source theorem and any RS-2026-CL-A claims remain owned by C02/native `6aa7b4b639a08191b893e2b7dd6cdf59`. This file shares only reusable coefficient/correlation lemmas with registered P08/P09 roles.

## Boolean/tensor pattern

The 09:45 report replaces witness-by-witness low-degree penalties by a single aggregate projection. For local Boolean witnesses `h_j` with widths `w_j`, product-noise retention `rho`, and source degree `D`, define

`B_rho(w,D)=sum_{s>D} binom(w,s) rho^(2s)`.

Then the high-degree residual of each local witness satisfies

`||Pi_{>D} T_rho h_j||_infty <= sqrt(Var h_j) sqrt(B_rho(w_j,D))`.

After summing witnesses, Cauchy--Schwarz makes the residual depend on the aggregate spectral dimension `sum_j B_rho(w_j,D)`, while the source LDA penalty is paid only once on the aggregate low-degree projection.

## Gaussian/Hermite coefficient lemma

Let `h in L^2(gamma_w)` and expand in the orthonormal Hermite basis,

`h = sum_alpha hhat(alpha) H_alpha`.

Under Ornstein--Uhlenbeck retention `rho in (0,1)`, for every integer `D>=0`,

`sum_{|alpha|>D} rho^|alpha| |hhat(alpha)|
 <= sqrt(Var_gamma h)
    [sum_{t>D} binom(w+t-1,t) rho^(2t)]^(1/2).`

Proof: Cauchy--Schwarz on Hermite coefficients, Parseval for the variance, and the exact number `binom(w+t-1,t)` of multiindices of total degree `t` in dimension `w`.

For `t=xw`, the counting exponent is

`psi_rho(x)=(1+x)log(1+x)-x log x+2x log rho`.

Its derivative is `log((1+x)/x)+2log rho`, so the maximizer is `x_*=rho^2/(1-rho^2)`. Since `psi_rho(x)->-infinity` linearly as `x->infinity`, there is a unique larger positive root `x_rho^+`. Thus the coefficient tail decays exponentially in `w` whenever `D/w` stays a fixed amount above `x_rho^+`.

## Scope warning and use

Unlike Walsh characters, Hermites are unbounded, so this coefficient-l1 estimate does not by itself give a pointwise residual bound. For P08/P09 it should be combined with an existing leverage/Christoffel bound, a typical-set sup envelope, clipping plus a rare-event estimate, or a polynomial majorant. It is especially suited to finite-Hermite approximants for correlated-minor bad events and tensor scores.

A finite uniform-alphabet tensor version is immediate with spectral multiplicity `binom(w,t)(s-1)^t` and unit-modulus characters.
