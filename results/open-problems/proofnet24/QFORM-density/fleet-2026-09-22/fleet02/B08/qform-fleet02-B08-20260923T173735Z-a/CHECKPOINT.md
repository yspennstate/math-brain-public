SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-23T17:37:35Z.
attacking: the k=1 aligned/low-rank-cross survivor by grouping the whole two-dimensional cross bank before any physical pivot.

# Early checkpoint — exact-rank-two grouped-bank router

Full QFORM remains OPEN.

Let the original independent coordinates be split into physical banks `I disjoint_union J`, with arbitrary induced affine terms after conditioning any outside coordinates. Assume the ACTUAL cross block has exact rank two,

`B=A[I,J]=U Sigma V^T`, `U^T U=V^T V=I_2`, `s_1>=s_2>0`.

Put `W=U^T X_I`. The two-dimensional orthonormal projection theorem gives the joint-density cap `M_H<=2` for `W`, while every quadratic and affine term internal to `I` may be left inside an arbitrary hub function `F(X_I)`.

Let `m=|J|>=4`, `k=ceil(m/2)`, and choose a `k`-coordinate subset `J_1` as follows. For `M=Sigma V^T`, Cauchy--Binet and uniform averaging over all `k`-subsets give

`E det(M_{J_1}M_{J_1}^T) = [k(k-1)/(m(m-1))] det(MM^T) >= (1/6)s_1^2s_2^2`.

Thus some ACTUAL physical `J_1` has full row rank and singular-product

`S:=sqrt(det(M_{J_1}M_{J_1}^T)) >= s_1s_2/sqrt(6)`.

This is exactly the half-subset extraction used in the newest fleet03/B08 r42 router, now applied before selecting any physical hub row.

Set `J_0=J\J_1`, let `Pi` be the orthogonal projection in `R^{J_1}` onto `row(M_{J_1})`, and define the projected internal crossing

`C=A[J_0,J_1](I-Pi)`, `F_perp=||C||_F`.

The completed grouped projected-crossing theorem (`NEW_PROJECTED_CROSSING.md`, k=2, ell=1) applies to the full ambient form because the entire left bank is the hub group and its only light-bank coupling is mediated by `W`. If every order-one row marginal obeys `||C_{j,*}||^2/F_perp^2<=1/2`, then

`||p_Q||_infinity <= 3*2^(5/6) M_H^(1/3) (S F_perp)^(-1/3)`
`                  <= 3*2^(7/6) (S F_perp)^(-1/3)`.

Consequently, in the actual k=1 gate where `s_2(B)>= beta L`, `beta=(3/16)sqrt(3/5)=0.145236875482778...`, and hence `s_1s_2>=beta^2 L^2`, fixing `rho=1/8` gives the explicit router

`F_perp>=L/8` and all row marginals `<=1/2`
`  ==> ||p_Q||_infinity <= 3*2^(7/6)*6^(1/6)*beta^(-2/3)*8^(1/3) L^(-1)`
`  = 65.7143458185.../L`,

with a continuous `C_0` density.

If this paid branch fails for the extracted `J_1`, then either

`F_perp<L/8`,

which is an explicit child-bank alignment/small-transverse-crossing obstruction, or some ACTUAL physical `j in J_0` satisfies

`||C_{j,*}||>F_perp/sqrt(2)>=L/(8sqrt(2))`,

which is a literal localized transverse row. No scalar pivot, moment, support bound, post-rotation independence, or coefficient-small random-error deletion appears.

## Exact alignment obstruction inside the target

Let `u,v in R^m` be orthonormal normalized Hadamard columns and set

`A_align = [[u u^T, u u^T+v v^T], [u u^T+v v^T, u u^T]]`.

Its nonzero spectrum is exactly `{2,1,-1}`: the `u`-symmetric mode has eigenvalue 2, the `v` symmetric/antisymmetric modes have eigenvalues +1,-1, and all remaining modes vanish. Hence it is a genuine target matrix, with selected large-eigenspace physical leverage `3/(2m)->0`. Each child has one large direction and the actual cross block has exact singular values `1,1`.

For EVERY `J_1` for which `M_{J_1}` has row rank two, `u_{J_1}` lies in `row(M_{J_1})`. Since the child crossing is `u_{J_0}u_{J_1}^T`,

`A_align[J_0,J_1](I-Pi)=0`.

Thus `F_perp=0` identically: a large child eigenvalue plus an exact diffuse rank-two cross bank does NOT force a third projected crossing direction. This is a mechanism obstruction, not a QFORM counterexample. Applying the fixed-source e5f71d79 Fresnel--Brascamp--Lieb theorem to this SAME exact rank-three target, whose eigenvalue product has magnitude 2 and whose three-frame leverage is `3/(2m)<=1/2`, gives

`||p_Q||_infinity <= 12*2^(-1/3) = 9.5244063118...`

for every cap-one product source, with a continuous density.

So the unpaid exact-rank-two endpoint is now sharply split: transverse projected child curvature is paid dimension-freely (<65.72/L at the gate scale), while the truly aligned child/cross geometry survives and must be aggregated by a different receiver. Arbitrary nonzero cross tail remains separate; it was not discarded.
