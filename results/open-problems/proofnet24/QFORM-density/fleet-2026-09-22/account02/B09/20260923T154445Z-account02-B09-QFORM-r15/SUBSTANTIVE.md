SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T15:44:45Z.
attacking: localized high-hub pair near-stratum interpolation: spend pair cross-volume before reciprocal core determinants, retaining arbitrary same-side curvature.

# Early substantive checkpoint — two-hub mixed-frame interpolation

Full QFORM remains OPEN. This checkpoint records the first new implication before the final report.

## 1. Uniform-core two-hub corollary of the completed mixed-hub theorem

Let `a,b` be two literal ORIGINAL coordinates and let `I` be a disjoint leaf bank. Condition any further disjoint coordinates. Assume

`A_II = D + sum_{k=1}^r lambda_k v_k v_k^T`,

where `D` is diagonal, `r>=0`, the nonzero `lambda_k` are real, and the `v_k` are orthonormal. Put

`rho_i=((v_1)_i,...,(v_r)_i,A_{ia},A_{ib}) in R^{r+2}`,
`G=sum_{i in I} rho_i rho_i^T`,

and suppose `G>0` and every normalized leverage satisfies

`rho_i^T G^{-1} rho_i <=1/2`.

The completed mixed-hub Theorem H in `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, allows **arbitrary** `A[{a,b},{a,b}]`, arbitrary outside same-side blocks/couplings after conditioning, and arbitrary affine terms. With two hubs it gives, for `t!=0`,

`|phi_Q(t)| <= K_r |t|^{-(r+4)/2}`,

where

`K_r = (1/4)(4*pi)^((r+4)/2) [det(G) prod_k |lambda_k|]^(-1/2)`.

Writing `alpha=(r+4)/2`, direct integration of `min(1,K_r |t|^{-alpha})` yields

`||p_Q||_infinity <= C_r [det(G) prod_k |lambda_k|]^(-1/(r+4))`,

`C_r = 4 (r+4)/(r+2) * 2^(-4/(r+4))`.

The characteristic function is in `L^1`, hence this branch has a continuous density and the same coefficient gives

`P{Q in L} <= C_r [det(G) prod_k |lambda_k|]^(-1/(r+4)) |L|`.

No probability squaring occurs: this is the undecoupled mixed-hub Fresnel/BL mechanism, so there is no square-root loss.

For `r=1`,

`C_1=(5/3)2^(6/5)=3.8289945166...`.

## 2. Rank-one leaf curvature and the partner's anchored third volume

Now take disjoint leaf banks `S,T` and suppose on `S union T`

`A_leaf = D + eps q q^T`, `eps in {+1,-1}`,

with `D` diagonal. Let the literal hub pair be `a,b`, and write on `T`

`u=(A_{ja})_{j in T}`, `v=(A_{jb})_{j in T}`,
`G_T=Gram(q_T,u,v)`.

For the partner account03/B09 r35 anchored physical volume

`V_ab(S)=sum_{k in S} sum_{J subset T, |J|=3} det A[{a,b,k},J]^2`,

the diagonal part has no `S x T` entries, so for every `k in S`, `J subset T`,

`det A[{a,b,k},J] = eps q_k det([u_J;v_J;q_J])`.

Cauchy-Binet therefore gives the exact identity

`boxed: V_ab(S)=||q_S||_2^2 det(G_T).`

Column rescaling from `q_T` to the normalized eigenvector in Theorem H shows that the invariant product `|lambda| det(G)` is exactly `det(G_T)`; normalized leverages are unchanged by this invertible column rescaling. Hence, if the mixed-frame leverage on `T` is <=1/2,

`boxed: ||p_Q||_infinity <= (5/3)2^(6/5) det(G_T)^(-1/5)`

and equivalently, when `V_ab(S)>0`,

`boxed: ||p_Q||_infinity <= (5/3)2^(6/5) (||q_S||_2^2/V_ab(S))^(1/5).`

This bound is **completely independent of the physical 2x2 hub core**. Thus it crosses the zero/rank-one/definite/indefinite core strata continuously at the level of the estimate, provided one transverse dense rank-one same-side leaf mode survives on the disjoint bank.

## 3. Target-valid near-stratum family

Let `|T|=m>=6`; choose flat orthonormal Walsh vectors `c1,c2,w` on `T`, and a flat unit vector `s` on a disjoint bank `S`. Put

`q=(s+w)/sqrt(2)`

and for arbitrary real `delta` define

`Q_delta = X_a^2 + delta X_b^2
          +2 X_a <c1,X_T> +2 X_b <c2,X_T>
          +<q,X_{S union T}>^2`.

In the orthonormal coefficient basis `(e_a,c1,e_b,c2,q)` its matrix is the direct sum

`[[1,1],[1,0]] direct_sum [[delta,1],[1,0]] direct_sum [1]`.

Hence its spectrum is

`{(1+sqrt(5))/2,(1-sqrt(5))/2,
  (delta+sqrt(delta^2+4))/2,(delta-sqrt(delta^2+4))/2,1}`.

The first 2x2 block has one eigenvalue of modulus >1; the second has determinant `-1`, so at least one eigenvalue has modulus >=1; the final eigenvalue is `1`. Thus **for every real delta** the exact owner target has at least three eigenvalues of modulus >=1.

On `T`, `G_T=diag(1/2,1,1)`, `det G_T=1/2`, and each normalized mixed-frame leverage is `3/m<=1/2`. Therefore

`boxed: ||p_{Q_delta}||_infinity <= (5/3)2^(7/5)=4.3983597026...`

for every real `delta` and every admissible independent cap-one input law, with a continuous density and the same linear interval constant. Also `V_ab(S)=1/4` and the pair cross wedge is `1`.

As `delta ->0`, the physical pair core `diag(1,delta)` approaches rank one. The partner r35 exact-core bounds split by rank/sign and the invertible bounds deteriorate near this stratum; the mixed-hub estimate above stays uniform because it spends the transverse dense leaf curvature before any reciprocal pair determinant.

## First unpaid implication after this checkpoint

`QFORM-LOCALIZED-HUBPAIR-GENERAL-LEAFCURVATURE-ROUTING-v1`: in the account03/B09 r35 localized-pair branch, either extract a disjoint leaf bank on which the same-side operator has a diagonal-plus-low-rank transverse mixed-frame packet with leverage <=1/2 (paid above), or use the anchored volume `V_ab(S)>=27G_*/400` to control genuinely general leaf curvature without taking a reciprocal near-zero pair determinant. Full QFORM remains open.
