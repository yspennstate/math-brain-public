SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T06:40:43Z.
attacking: the partner k=1 physical rank-split survivor by a two-physical-hub determinant-balanced mixed-hub estimate that keeps the entire physical hub core and a dense same-side leaf packet.

# Substantive checkpoint — two-hub determinant-balanced mixed smoothing

Full QFORM remains OPEN.

Let the original independent coordinates be split as `H={h1,h2} union I union J`. After conditioning only on `J`, assume the exact leaf block is

`A_II = D + sum_(k=1)^r lambda_k v_k v_k^T`,

with `D` diagonal and each `lambda_k!=0`. Put `c_a=A[I,h_a]`,

`W=[v_1,...,v_r,c_1,c_2]`, `G=W^T W`, `d=r+2`,

and assume `G>0`. Whiten only the coefficient frame, `U=W G^(-1/2)`, so `U^T U=I_d`; no random coordinate is rotated. Let `w_S=det(U_S)^2` over physical `d`-subsets and let

`rho=P(S cap T=empty)`

for iid `S,T` from the Pluecker law.

Combining the pre-leverage part of newest-Claude Theorem H at
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
with the completed determinant-entropy BL theorem
`math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a`
gives, when `rho>0`,

`|phi_Q(t)| <= pi^((r+4)/2) exp((r+2)/2)
 [rho det(G) prod_k |lambda_k|]^(-1/2) |t|^(-(r+4)/2)`.

Therefore

`||p_Q||_infinity <= C_r [rho det(G) prod_k |lambda_k|]^(-1/(r+4))`,

`C_r=((r+4)/(r+2)) exp((r+2)/(r+4))`.

The blocks `A_HH,A_HJ,A_IJ,A_JJ` and all affine terms are arbitrary. The bound is continuous-density and directly linear in interval length; there is no probability squaring.

In particular:

- `r=0`: `||p_Q||_infinity <= 2 sqrt(e) [rho det(c_1,c_2 Gram)]^(-1/4)`; this pays an arbitrary near-zero/nonzero physical `2 x 2` hub core whenever the disjoint leaf cross two-frame has determinant-balanced mass.
- `r=1`: with one exact dense same-side leaf square, `||p_Q||_infinity <= (5/3)e^(3/5)[rho det(G)|lambda|]^(-1/5)`.

Splice to the completed account02/B09 k=1 torsion extraction used by the newest account03/B09 r25 partner: if its selected pair `(i,h)` and disjoint outside bank `T` satisfy

`Delta_i(T) >= [eta^2(1-eta)/3] Theta^2`,

and `A_TT` is diagonal, then the `r=0` two-hub theorem gives uniformly over the ENTIRE actual physical pair core

`||p_Q||_infinity <= 2 sqrt(e) 3^(1/4) eta^(-1/2)(1-eta)^(-1/4)
 rho_2^(-1/4)|Theta|^(-1/2)`.

At `eta=1/16` the prefactor is `<17.642`. Thus the exact core-rank split of account03/B09 r25 is unnecessary on this determinant-balanced diagonal-outside branch: rank 0, rank 1, near-null rank 2, definite and indefinite cores are all paid at once.

Remaining gap: if the outside same-side operator is genuinely non-diagonal, spend a low-rank exact curvature packet (`r>=1`) as above or route small Pluecker disjointness to a finite physical core. Arbitrary dense residual curvature cannot be silently absorbed because the source-valid cancellation obstruction from the preceding B09 run remains active.
