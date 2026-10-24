SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-23T15:04:43Z.
attacking: the heavy-transverse null-hub survivor; reroot an exact-null heavy anchor with the compatible account03/B18 compiler, and pay every nonzero anchor by the rank-two half-Riesz Schur identity.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full owner target remains OPEN. This checkpoint records the first mathematical implication before the longer construction/audit.

## 1. Nonzero heavy anchor is a rank-two half-Riesz branch

Let `A=R M R^T` have exact rank three with `R^T R=I_3`, `M` invertible symmetric, and `D=|det M|`. Let the original physical row of coordinate `i` be `u_i`, put `c_i=||u_i||^2`, and let `a=A_ii=u_i^T M u_i`.

For `a!=0`, complete the square in the ORIGINAL coordinate `X_i`. The completed e5f square-peel theorem gives

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(S_i)`,

where `S_i` is the Schur residual on the remaining original coordinates.

There is an exact pseudodeterminant identity

`|pdet_2 S_i| = c_i D/|a|`.

Proof: for each `p<q`, `p,q!=i`, Schur determinant factorization gives

`det A[{i,p,q}] = a det S_i[{p,q}]`.

On the other hand

`det A[{i,p,q}] = det(M) det(u_i,u_p,u_q)^2`.

Choose the spectral basis so `u_i=sqrt(c_i)e_1`. Parseval gives that the two transverse columns of the remaining rows are orthonormal, hence Cauchy--Binet gives

`sum_(p<q) det(u_i,u_p,u_q)^2=c_i`.

Since `S_i` has rank at most two, the sum of its principal `2x2` minors is its rank-two pseudodeterminant. Therefore `a pdet_2(S_i)=c_i det M`, proving the identity.

Apply the completed orientation-free theorem `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` at `math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, which is valid for arbitrary affine terms and gives

`H_(1/2)(S_i)<=128 |pdet_2 S_i|^(-1/4)`.

Thus

`boxed: ||p_Q||_infinity <=128 [c_i D |a|]^(-1/4).`

In the live heavy-transverse branch from account02/B18 r29, `c_i>=q_i>1/2` and `D>=1`, so every anchor with `|A_ii|>=eta>0` is paid by

`||p_Q||_infinity <128 (2/eta)^(1/4)`.

The only issue in this route is the punctured near-null collar `0<|A_ii|<<1`; no coefficient deletion or support/moment assumption is used.

## 2. Exact-null rerooting pays a large compatible subbranch

Suppose instead `a=A_ii=0`. Put `n_i=u_i/sqrt(c_i)`. If

`max_(j!=i) ||P_(n_i^perp)u_j||^2 <=1/2`,

then the designated-partner theorem account03/B18 r28, `QFORM-SCHUR-NULLHUB-TRANSVERSE-COMPILER-v1`, can be applied after an exact algebraic rerooting at physical coordinate `i`.

For `c_i<1`, the residual covariance is `G=I-u_i u_i^T`; let `H=G^(1/2)`. Write residual rows as `v_j=H^(-1)u_j`, so `sum v_jv_j^T=I`. With

`D_i=H M H`, `u'=H^(-1)u_i=sqrt(c_i/(1-c_i)) n_i`,

one has the exact same physical matrix in Schur-isotropic form. Moreover `H^(-1)` is the identity on `n_i^perp`, so the transverse gate is unchanged, while

`r_i^2 |det D_i| = [c_i/(1-c_i)] [(1-c_i)D]=c_iD`.

Therefore the partner gives

`boxed: ||p_Q||_infinity <=3*2^(4/3)(c_iD)^(-1/3),`

with a continuous `C_0` density. The endpoint `c_i=1` is the completed isometric null-hub theorem itself and gives the same formula.

For the live heavy-transverse anchor `q_i>1/2`, one has `c_i>1/2`; hence in target normalization `D>=1`, the exact-null reroot-diffuse branch satisfies

`||p_Q||_infinity <3*2^(5/3)=9.5244063118092...`.

The newest account03/B18 r30 theorem is NOT applicable at this exact-null point because it assumes its scalar pivot `a!=0`. The compatible designated-partner input is r28.

## 3. Current first unpaid implication

The previous generic anchor-star debt is now reduced to two explicit collars:

1. `0<|A_ii|<<1`, where the nonzero-pivot estimate above loses a negative quarter power and exact-null rerooting cannot be invoked by continuity on arbitrary unbounded inputs;
2. `A_ii=0` but the rerooted transverse gate itself fails, producing a second original-coordinate heavy direction.

A source-valid stress family for this dichotomy is being worked out next; it will also test whether aggregate anchor-star determinant mass can force a single good physical minor (it should not be assumed).
