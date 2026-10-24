# Addendum: invariant rank-one / rank-two bank transducer

Status: proved supporting exact-rank-three theorem; full QFORM remains OPEN.

The main report used a spectral line and its orthogonal plane. Orthogonality is not needed after the arbitrary overlap bank has been conditioned. The correct invariant resource is the smallest eigenvalue of the Gram matrix of the surviving disjoint rank-one and rank-two original-coordinate banks.

## Theorem — `QFORM-RANK1-RANK2-CONDITIONING-44-v1`

Let

`A=RBR^T`, `R^TR=I_3`, `min_j |lambda_j(B)|>=1`

be an exact-rank-three target. Partition ORIGINAL coordinate indices as

`I disjoint_union J disjoint_union K=[n]`

such that

`rank(R_I)=1`, `rank(R_J)=2`.

Let

`G_D=R_(I union J)^T R_(I union J)`

and assume

`g=lambda_min(G_D)>0`.

Then for arbitrary independent input densities bounded by one,

`boxed: ||p_(X^TAX)||_infinity <44/g.`

No orthogonality between the spectral line `range(R_I^T)` and spectral plane `range(R_J^T)` is assumed. The overlap rows in `K` are arbitrary and may have all three spectral components.

### Proof
Choose a unit vector `e` spanning `range(R_I^T)`. Write rows on `I` as `a_i e^T` and put

`alpha=sum_I a_i^2>0`,
`S=alpha^(-1/2) sum_I a_i X_i`.

Then S is a normalized one-dimensional product projection.

Choose a 3x2 matrix `V` with orthonormal columns spanning `range(R_J^T)`. Write the spectral rows on J as

`r_j=V y_j`, `y_j in R^2`,

and set

`G_2=sum_J y_j y_j^T`,
`Y=G_2^(-1/2) sum_J y_j X_j`.

Because `rank(R_J)=2`, `G_2` is positive definite. The coefficient matrix of Y has orthonormal columns. Because I and J are disjoint ORIGINAL-coordinate banks, the scalar S is genuinely independent of the whole pair Y. Their source-valid density caps are the same ones used in account02/B16 r23.

Define the 3x3 synthesis matrix

`T=[sqrt(alpha)e, V G_2^(1/2)]`.

For `xi=(S,Y)` one has

`R_I^T X_I+R_J^T X_J=T xi`.

Moreover

`T T^T
 =alpha e e^T+V G_2 V^T
 =R_(I union J)^T R_(I union J)
 =G_D`.

Thus

`s_min(T)^2=lambda_min(G_D)=g`,

so T is invertible.

Condition on the arbitrary overlap coordinates `X_K=x_K` and put `z_K=R_K^T x_K`. Then

`Q | X_K=x_K=(T xi+z_K)^T B(T xi+z_K)`
`=(xi+eta)^T C(xi+eta)`,

where

`eta=T^(-1)z_K`, `C=T^T B T`.

As in the main report, the deterministic scalar and planar translations in eta can be realized by deterministic translations of the physical coordinates in I and J along their normalized coefficient columns. Hence the translated variables remain independent cap-one original-coordinate product sources in exactly the rank-one/rank-two bank class of the designated partner theorem.

The coefficient satisfies

`s_min(C)
 >=s_min(T)^2 s_min(B)
 >=g`.

Therefore `C/g` is symmetric with all three eigenvalue moduli at least one. Apply account02/B16 r23 `QFORM-DISJOINT-SPECTRAL-LINE-PLANE-44-v1` in the ABSTRACT normalized bank coordinates `(S,Y)`: its physical frame has the I rows on the first abstract axis and the J rows in the abstract transverse plane, regardless of the angle between their original spectral subspaces before the synthesis map T. It gives a density bound `<44` for the conditional output divided by g. Scaling back gives

`||p_(Q | X_K=x_K)||_infinity <44/g`

uniformly in `x_K`. Average the conditional densities. QED.

## Invariant overlap-volume companion
With `D=I union J`, put `G_K=R_K^TR_K=I_3-G_D`. If `G_D,G_K` are positive definite, then for the physical cross block

`M=A[K,D]=R_K B R_D^T`

one has exactly

`e_3(M^TM)=det(G_K)det(G_D)det(B)^2`.

Because M has rank three, its row third-volume marginal on k in K equals

`r_k^T G_K^(-1)r_k`.

Hence, if

`max_(k in K) r_k^T G_K^(-1)r_k<=1/2`,

the q=1 theorem from the newest volume-stability package gives a continuous density satisfying

`boxed: ||p_Q||_infinity
 <=3e [det(G_D)det(I_3-G_D)det(B)^2]^(-1/6)
 <=3e [det(G_D)det(I_3-G_D)]^(-1/6).`

This invariant form strictly contains the orthogonal line/plane formula in the main report.

## Consequence and remaining debt
For any `delta>0`, every exact-rank-three configuration admitting disjoint original-coordinate banks with ranks one and two and

`lambda_min(R_(I union J)^TR_(I union J))>=delta`

has

`||p_Q||_infinity<44/delta`,

with no restriction at all on the conditioned overlap bank K. Thus the designated partner's source-separated theorem survives arbitrary overlap after conditioning whenever a quantitatively transverse rank-one/rank-two product skeleton remains.

The remaining structural problem is to force such a skeleton with universal `delta`, or else route the failure to a diffuse cross-volume, heavy-pivot, finite-core, or other already-paid exit. The known singleton-plus-two-diffuse-banks and bad-minor corrections show that one cannot simply assert a universally well-conditioned finite physical triple.

Source actually applied: account02/B16 r23 at `yspennstate/math-open-problems@7044d3cf479cc067d97a317cf67b41121cc48aab`. Newest volume theorem applied in the companion statement: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`.
