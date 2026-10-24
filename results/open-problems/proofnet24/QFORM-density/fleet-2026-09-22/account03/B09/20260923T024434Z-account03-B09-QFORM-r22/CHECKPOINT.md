# account03/B09 r22 — substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

## Obligation attacked

Close the strict-N3 **global physical star** survivor left by the exact cut-rank-one compiler, while retaining arbitrary cap-one independent inputs and without rotating the product law.

Use the fresh account01/B09 theorem `QFORM-TWOHUB-PHYSICAL-STAR-DIFFUSE-v1` from `yspennstate/math-open-problems@344963502d821945c7af02ab8d7272536dab8e5c` (scope clarified at `aa3a9fa9f63baf640ff8707925851928debb73af`): for two original-coordinate hubs `h,s`, diagonal leaf self-block, leaf-to-hub row vectors `rho_i=(A_{ih},A_{is})`, Gram matrix `G=sum_i rho_i rho_i^T`, and row leverages `ell_i=rho_i^T G^{-1}rho_i<=1/2`,

`||p_Q||_infinity <= 4 det(G)^(-1/4)`

with continuous density and arbitrary physical two-hub block retained.

## New spectral forcing calculation

Assume strict `N3(tau)` with

`|A_ii|<tau`, `|det A[{i,j},{i,j}]|<tau` for every `i!=j`, and `s_3(A)>=1`.

Take the **full physical complement** of one hub `h`, and suppose its leaf off-diagonal support is a star centered at `s`. Let `I` be all coordinates except `h,s`. Then `A_II` is diagonal. Set

`C = [c,b]`,  `c_i=A_{ih}`, `b_i=A_{is}`.

Write

`A = A0 + E`,

where

`A0 = [[0_{2x2}, C^T],[C,0]]`

in the splitting `{h,s} union I`, while `E` consists only of the physical `2x2` hub block and the physical leaf diagonal.

From the pair-determinant hypotheses,

`|A_{ij}|^2 <= tau+tau^2`

for every off-diagonal physical entry. Put

`q=sqrt(tau+tau^2)`, `delta=tau+q`, `mu=1-delta`.

Then `||E||_op<=delta`. The singular values of `A0` are

`sigma_1(C), sigma_1(C), sigma_2(C), sigma_2(C),0,...`.

Therefore Weyl's singular-value inequality gives

`sigma_2(C)=s_3(A0) >= s_3(A)-||E||_op >= mu`.          (1)

In particular, if `mu>0`, exact alignment/rank-one of the mixed star frame is impossible.

Let `G=C^T C`. Equation (1) yields `lambda_min(G)>=mu^2` and

`det G=sigma_1(C)^2 sigma_2(C)^2 >= mu^4`.             (2)

Each row satisfies `||rho_i||_2^2 < 2q^2`, hence

`ell_i = rho_i^T G^{-1}rho_i <= ||rho_i||_2^2/lambda_min(G)
       < 2q^2/mu^2`.                                      (3)

Thus whenever `2q^2/mu^2<=1/2`, the fresh two-hub star theorem applies automatically. Combining with (2),

`||p_Q||_infinity <= 4 det(G)^(-1/4) <= 4/mu`,

and every interval `L` obeys

`P{Q in L} <= (4/mu)|L|`.

The characteristic function is integrable in the source theorem, so this branch has a continuous density.

For the strict-N3 threshold `tau=1/128` used by the current compiler,

`q=sqrt(129)/128 = 0.088732942903...`,
`mu=1-1/128-sqrt(129)/128 = 0.903454557096...`,
`2q^2/mu^2 = 0.01929243923... < 1/2`,

hence

`boxed: ||p_Q||_infinity < 4.428`.

This removes both previously listed star exceptions: **exact alignment cannot occur**, and **heavy row leverage cannot occur**, inside the strict-N3 global-star chamber.

Remaining gap: the clique-factor branch still has a genuinely different issue because its diagonal-plus-rank-one representation can contain large cancelling diagonal terms even when the physical diagonal is small; the same small-operator perturbation argument is not valid there.
