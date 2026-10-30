SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-24T09:28:09Z.
attacking: partner fleet03/B06 r56 global-null endpoint by product-preserving sparse-kernel deletion.

# Early substantive calculation — sparse kernel deletion

Partner r56 (`math-open-problems@24fd6e4552117b2dd56c62db304883d5360b59f2`) reduces every exact singular localized three-hub face to a density-paid branch or an actual global null vector supported on the three literal hub coordinates. The first unpaid implication is to use that null certificate without replacing the hub triple by a dependent two-dimensional spectral quotient.

Let `A=A^T`, let `K subset ker A` have dimension `d>=1`, and suppose every vector in `K` is supported on one literal coordinate set `H`, `|H|=m<=3`. Choose an orthonormal basis matrix `W` for `K`. By Cauchy--Binet,

`sum_{L subset H, |L|=d} det(W_L)^2 = det(W^T W)=1`.

Hence some `L subset H`, `|L|=d`, satisfies `sigma_min(W_L)^2 >= det(W_L)^2 >= 1/binom(m,d) >= 1/3` (all other singular values of the submatrix `W_L` are <=1). Put `R=L^c`, `T=W_R W_L^{-1}` and `C=A_RR`. The equations `AW=0` force the exact block factorisation, after ordering coordinates as `L,R`,

`A = P^T C P`,  `P=[-T  I_R]`.

Also `P P^T = I + T T^T`, and orthonormality of `W` gives

`||P||^2 = 1/sigma_min(W_L)^2 <= binom(m,d) <=3`.

Therefore every singular value satisfies

`s_k(A) <= ||P||^2 s_k(C)`, hence `s_3(C) >= s_3(A)/3`.

Condition on the original product bank `X_L=x_L`. Then

`X^T A X = (X_R-Tx_L)^T C (X_R-Tx_L)`.

The coordinates of `X_R-Tx_L` are still independent and each density is merely translated, so its density cap remains one. Thus the global-null branch is reduced, with no post-rotation independence, to the same rough-input QFORM problem in fewer original coordinates and with spectral scale degraded by at most the universal factor three.

For the first concrete target payment, take `n=4`. Then `C` is 3x3 and all three eigenvalues have modulus at least `1/3`. The pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A gives, uniformly in the conditioning,

`||p_{Q|X_L=x_L}||_infinity <= 6 sqrt(pi)/(1/3)=18 sqrt(pi)`.

Averaging over `X_L` yields the genuine target inequality `||p_Q||_infinity <=18 sqrt(pi)` for every four-dimensional target matrix possessing such a <=3-coordinate-supported nullspace.

The factor three is sharp at the matrix level: the projection

`A_*=[[2/3,-1/3,-1/3,0],[-1/3,2/3,-1/3,0],[-1/3,-1/3,2/3,0],[0,0,0,1]]`

has spectrum `{1,1,1,0}` and null vector `(1,1,1,0)/sqrt(3)`. Deleting any one of the first three coordinates leaves a 3x3 principal block with spectrum `{1,1,1/3}`.

Status: supporting lemma proved; full QFORM remains open. Next: determine whether the one-time factor-three sparse-kernel reduction can be spliced into the near-singular three-hub compiler without recursive scale loss, or whether a separate aggregate determinant bank is needed in the small-but-nonzero determinant transition.
