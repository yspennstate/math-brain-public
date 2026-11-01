SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-24T05:58:20Z.
attacking: source-factorized one-zero/null-pivot three-variable carriers — keep a genuinely nonzero two-sided overlap, pay it by a determinant-one pair change, and exploit a primary one-dimensional product-marginal cap before the completed fleet02/B18 scalar/dependent-pair receiver.

# Early substantive calculation — a cap-1 scalar + diffuse bank projection + cap-1 scalar gives constant 6

Full QFORM remains OPEN. This calculation is a scoped target-level implication, not a full proof.

Let `S` and `W` be two distinct ORIGINAL scalar coordinates, each with density cap one. Let `X_J` be a disjoint ORIGINAL-coordinate product bank and `v` a unit vector on that bank. Put

`Y=v^T X_J`.

Then `S,Y,W` are mutually independent. By Livshyts--Paouris--Pivovarov Theorem 1.1 (equivalently the k=1 sharp product-marginal bound),

`||p_Y||_infinity <= sqrt(2)`.

Hence the pair `(Y,W)` has joint density cap at most `sqrt(2)`.

Let

`H=[[0,r1,r2],[r1,c,d],[r2,d,a]]`

be any invertible real symmetric `3 x 3` matrix, and set

`Q=(S,Y,W)^T H (S,Y,W)`.

The first diagonal entry is exactly zero, but both cross coefficients `r1,r2` may be nonzero. Let `r=(r1,r2)` and `beta=||r||_2>0`. Choose a deterministic `O in O(2)` taking `r` to `(beta,0)` and write `(C,D)^T=O^T(Y,W)^T`. This is only a change of variables in the JOINT PAIR; it does not assert independence after rotation. Its Jacobian has modulus one, so `(C,D)` retains joint density cap `M<=sqrt(2)`, and it remains genuinely independent of `S`, whose cap is `K=1`.

In `(S,C,D)` coordinates the matrix is

`H'=[[0,beta,0],[beta,alpha,delta],[0,delta,gamma]]`.

Because the pair change has determinant modulus one,

`det H'=det H=-beta^2 gamma`.

Apply the completed fleet02/B18 theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, source commit `ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`:

`||p_Q||_infinity <= 3(2 M K)^(2/3)|beta^2 gamma|^(-1/3)`.

With `M<=sqrt(2)`, `K=1`,

`boxed: ||p_Q||_infinity <= 6 |det H|^(-1/3).`

Therefore, if all three eigenvalues of `H` have modulus at least `s>0`,

`boxed: ||p_Q||_infinity <= 6/s.`

Arbitrary deterministic affine terms in `(S,Y,W)` can be removed first by the translation `z -> z+(1/2)H^{-1}ell`; this preserves the scalar/pair caps and source independence. The new argument proves essential boundedness only; continuity is separate.

## Exact target-valid diffuse family

Let `m>=1`, let

`Y_m=m^(-1/2) sum_{j=1}^m X_j`,

with `S=X_0` and `W=X_{m+1}` disjoint ORIGINAL scalars. Take the Householder core

`H=I-2nn^T`, `n=(1/sqrt(2),1/2,1/2)`.

Explicitly,

`H=[[0,-1/sqrt(2),-1/sqrt(2)],
    [-1/sqrt(2),1/2,-1/2],
    [-1/sqrt(2),-1/2,1/2]]`.

Its exact spectrum is `{-1,1,1}` and `|det H|=1`. Thus

`Q_m=-sqrt(2) S Y_m-sqrt(2) S W+(1/2)Y_m^2-Y_m W+(1/2)W^2`

is inside the owner's exact target class for every `m`, and

`boxed: ||p_(Q_m)||_infinity <= 6.`

This family has genuine two-sided overlap: the null scalar `S` couples to both `Y_m` and `W`. For each literal physical coordinate `j` in the diffuse bank, the three-coordinate principal block on `{S,X_j,W}` is `D H D` with `D=diag(1,m^(-1/2),1)`, so its determinant has modulus `1/m`. Thus the older literal physical one-zero-triple theorem by itself gives a determinant certificate degrading like `m^(1/3)`, while the grouped product-marginal transfer stays uniform.

## Prior-solution audit

The analytic one-zero/null-pivot kernel is NOT claimed novel. A stronger literal-original-coordinate theorem already exists as fleet03/B04 `QFORM-ONE-ZERO-TRIPLE-v1`, and this slot's r43 already pays a rank-one-cross/two-dimensional active pair with LPP joint cap `2`. The present scoped transfer uses the additional SOURCE FACTORIZATION `(Y,W)` (diffuse one-dimensional marginal times a separate original scalar) to improve the pair cap from `2` to `sqrt(2)`, producing the constant `6`, and it applies that completed fleet02/B18 receiver to an explicit two-sided-overlap target family.
