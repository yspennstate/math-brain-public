# RS-2026-CL-A handoff to P08/P09 — weighted covariance transfer

Source ownership remains with RS-2026-CL-A. This is a reusable lemma, not a claim on P08/P09 sources.

Let `R` have orthonormal chaos basis `phi_alpha` with complexity/degree `d_alpha`, let `Q` be any comparison law, and let

`G(alpha,beta)=Cov_Q(phi_alpha,phi_beta)`.

For a signal vector `b_alpha=E_P phi_alpha-E_Q phi_alpha`, source functional norm through a finite index set `I` is

`A_I^2=b_I^T G[I]^dagger b_I`.

For diagonal damping `W=diag(w_alpha^2)` on the same coordinates,

`b_I^T W b_I <= A_I^2 || W^(1/2) G[I] W^(1/2) ||_op`.

More generally, if `A_D` controls the full source space through degree `D`, the same bound holds on any principal degree band `J subset I_D` with `G[J]` on the right.

Proof: write `b=G^(1/2)x`, `||x||^2=A_D^2`, project to `J`, and take the operator norm.

A Schur sufficient condition is

`||W^(1/2)GW^(1/2)||_op <= sup_alpha sum_beta w_alpha w_beta |Cov_Q(phi_alpha,phi_beta)|`.

## P08 use

For Hermite-indexed Gaussian phase-retrieval statistics, take `phi_alpha` to be the Hermite/tensor chaos coordinates and `w_alpha` to be the OU damping or any proof-specific hard-edge smoothing weight. A Wick/diagram row-sum estimate immediately turns into a source-functional transfer without constructing an adapted frame or a global norm-comparison theorem.

## P09 use

For Gaussian tensor/chaining families grouped by chaos or interaction complexity, use the anisotropic weights already appearing in the chaining/PAC-Bayes argument as `w_alpha`. Any block covariance estimate can be inserted directly through the weighted operator norm. This is especially useful when a worst-case tensor norm comparison is too expensive but covariance is sparse or nearly block diagonal.

No novelty claim is made for the linear-algebra inequality itself; it is a source-directed reuse point.