# B13 early checkpoint — rectangular null-bank aggregate

Programme `QFORM-DENSITY-3EIG-20260922`; run `20260923T102244Z-fleet02-B13-extreme-7c91d2ab`.

First unpaid implication attacked: replace single-minor payment in the exact/null-bank endpoint by an aggregate rectangular cross-volume bound, so a high-dimensional null leaf bank cannot hide its rank-two resource among many tiny minors.

Let `r>=2`, `m>=r`, let `U in R^r`, `V in R^m` be disjoint original-coordinate banks with independent scalar densities bounded by one, let `Z` be the remaining independent coordinates, and let `B` be an `r x m` full-row-rank matrix. For

`Q = F(U,Z) + 2 U^T B V + c(Z)^T V`,

I obtain

`||p_Q||_inf <= K_r det(B B^T)^(-1/(2r))`,

`K_r = [r/(sqrt(2)(r-1))] omega_r^(1/r)`.

The proof combines the designated partner fleet03/B13 exact-null-bank mechanism with the dimension-free Rogozin/Ball linear-form bound `||p_{a dot V}||_inf <= sqrt(2)/||a||_2`, then averages the reciprocal distance under the `r`-dimensional affine map `(BB^T)^(1/2)(U-u0)`. No rotation of the random vector is used.

For `r=2`,

`||p_Q||_inf <= sqrt(2 pi) det(BB^T)^(-1/4)`

and Cauchy-Binet gives

`det(BB^T)=sum_{|T0|=2} det(B[:,T0])^2`.

Thus the exact-null-bank endpoint is paid by aggregate squared two-minor mass before taking the reciprocal fourth root; one large selected minor is unnecessary. The remaining branch is genuinely nonzero same-bank curvature, not fragmentation of the cross resource.

Sources already read for the full proof: partner fleet03/B13 `math-open-problems@57d2f3bcf9a2dec39c1761aafff0f3f7f1732c59`; no-attainment purification `@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`; required Claude package `@e5f71d79eff325201dd0274053d20268ce65b837` including RESULTS, FOURIER_ROUTE_REPORT and COUNTEREXAMPLE_SEARCH.
