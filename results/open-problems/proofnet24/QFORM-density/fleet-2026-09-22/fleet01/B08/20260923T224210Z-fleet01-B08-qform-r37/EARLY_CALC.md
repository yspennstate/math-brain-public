# B08 r37 early calculation — angle-free three-volume at the zero-tail endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T224210Z-fleet01-B08-qform-r37`  
Status at this checkpoint: supporting calculation; full target OPEN.

The first missing implication attacked is the near-alignment endpoint left by B08 r36.  The r36 smallest-singular-value crossing estimate deteriorates when the physical star is nearly aligned with the top-two child eigenspace.  Here the mechanism is changed: retain the **product of the three crossing singular values** rather than the smallest one.  At the exact rank-two child endpoint the aligned part of the star cancels identically from this product.

## Setup

Let `A` be real symmetric and let `R in R^{n x 3}` have orthonormal columns with

`A R = R Lambda`, `min_j |lambda_j| >= L > 0`.

Delete an ORIGINAL coordinate `i` and write

`A = [[a,b^T],[b,C]]`.

Let `p=||R_{i,*}||^2 <= 1/48`.  Assume for this endpoint calculation

`s_3(C)=0`.

B08 r36 proves, with `U` the top-two absolute-eigenvalue frame of `C`, `P=UU^T`, `r=(I-P)b`, `tau=||r||`, that

`tau >= L sqrt((1-p)/p)`

and

`s_2(C) >= sqrt(1-p) L`.

Thus `C=U D U^T` for a nonsingular symmetric `2 x 2` diagonal `D` satisfying

`|det D| >= (1-p)L^2`.

Put `w=r/tau`; then `W=[w,U]` has orthonormal columns.  Assume the assigned diffuse gate

`max_j ||W_{j,*}||^2 <= 1/48`.

The completed designated-partner result fleet02/B08 r28, Lemma 3.1, gives an ORIGINAL-coordinate child split `S disjoint_union T` with

`G_S=W_S^T W_S >= I_3/4`, `G_T=W_T^T W_T >= I_3/4`.

Write `b=tau w+U beta`.  Put the deleted hub coordinate on the `T` side.  The **actual** crossing is

`M = [ C[S,T] , b_S ]`.

Because the child tail is exactly zero, no coefficient perturbation is discarded:

`M = W_S H`,

where the `T`-columns of `H` are `[0; D U_T^T]` and the hub column is `z=(tau,beta)^T`.

## Exact three-volume identity

Let `G_{T,U}=U_T^T U_T`.  Then

`H H^T = diag(0, D G_{T,U} D) + z z^T`.

The first diagonal block has a one-dimensional nullspace exactly in the `w` coordinate.  Taking the Schur complement in the bottom `2 x 2` block gives the exact identity

`det(H H^T) = tau^2 det(D G_{T,U} D)
             = tau^2 (det D)^2 det(G_{T,U}).`

Since `W_S` has full column rank,

`prod_{j=1}^3 s_j(M)^2
 = pdet(MM^T)
 = det(G_S) det(HH^T).`

Therefore

`prod_{j=1}^3 s_j(M)
 = tau |det D| sqrt(det G_S det G_{T,U}).`

The partner half-cut gives `det G_S >= 4^{-3}` and, since `G_{T,U}` is the `U` principal block of `G_T`, `det G_{T,U}>=4^{-2}`.  Hence

`prod_{j=1}^3 s_j(M) >= tau |det D|/32`

and consequently

`prod_{j=1}^3 s_j(M)
 >= [(1-p)^{3/2}/(32 sqrt p)] L^3
 >= [47 sqrt(47)/1536] L^3.`

Crucially, **beta does not appear**.  Thus the crossing three-volume is uniformly macroscopic even as the star angle from `range(U)` tends to zero and `||beta||/tau` tends to infinity.

## Density consequence at this endpoint

The checked interactive exact-rank crossing theorem in

`math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`, Section 1,

applies to the actual rank-three original-coordinate crossing `M`.  For independent cap-one scalar coordinates on both sides and crossing rank three it gives

`||p_Q||_infinity <= 6 (s_1(M)s_2(M)s_3(M))^{-1/3}`,

with a continuous `C_0` density.  Therefore

`||p_Q||_infinity
 <= 6 [1536/(47 sqrt(47))]^{1/3} L^{-1}
 = 10.0979386229... L^{-1}.`

This is angle-free and keeps arbitrary internal quadratic terms on the two physical banks.  It closes the exact `s_3(C)=0` diffuse deletion endpoint but does **not** yet give a leakage-uniform estimate for `0<s_3(C)<<L`: a small child tail is a genuine additional crossing term and cannot be treated as a small random quadratic perturbation.

Latest designated-partner update fleet02/B08 r28 (2026-09-23T21:49:09Z) also gives the independent full-matrix gate: if any original-coordinate `2 x 2` principal block has least singular value at least `L/64`, then `||p_Q||_infinity<619/L` (essential boundedness; continuity not claimed there).  The new three-volume endpoint above remains valid even when every such pair gate fails.
