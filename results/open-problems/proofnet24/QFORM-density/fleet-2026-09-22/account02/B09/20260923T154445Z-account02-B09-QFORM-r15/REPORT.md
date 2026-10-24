SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T15:44:45Z.
attacking: localized high-hub pair near-stratum interpolation: spend pair cross-volume before reciprocal core determinants, retaining arbitrary same-side curvature.

# account02/B09 r15 — mixed-hub interpolation across a localized physical-pair rank transition

## Status and first unpaid implication

**NEW SUPPORTING THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN.**

The first unpaid B09 implication is now

`QFORM-LOCALIZED-HUBPAIR-GENERAL-LEAFCURVATURE-ROUTING-v1`:

> In the account03/B09 localized physical-hub-pair branch, either extract on a disjoint original-coordinate leaf bank a diagonal-plus-low-rank same-side packet whose mixed frame with the two physical star rows is quantitatively diffuse, or use the already-retained pair-anchored physical third volume to control genuinely general leaf curvature without first paying a reciprocal determinant of the near-singular physical pair core.

This run pays the first alternative, including an explicit target-valid family whose physical pair core crosses rank one. The result is uniform in that physical pair core and therefore removes the near-stratum blow-up for this whole low-rank-plus-diagonal leaf class.

The unrestricted conjecture remains OPEN. No moment, support, centering, log-concavity, Gaussian, diagonal-basis, or post-rotation independence assumption is used. Continuity is proved only in the branch stated below.

Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Completed sources used at equations

1. `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, Theorem H. With a hub bank `H`, leaf bank `I`, and

   `A_II = D + sum_{k=1}^r lambda_k v_k v_k^T`,

   where `D` is diagonal, the mixed rows

   `rho_i=((v_k)_i,k<=r; A_{ih},h in H)`

   with Gram `G` and normalized leverages at most `1/2` give an undecoupled mixed-hub Fresnel/Brascamp--Lieb estimate. Crucially `A_HH`, `A_HJ`, `A_IJ`, `A_JJ` are arbitrary. I use this theorem with two literal physical hubs and integrate its exact Fourier envelope.

2. Designated partner account03/B09 r35, `QFORM-LOCALIZED-HUBPAIR-EXACT-CORE-ROUTING-v1`, canonical `math-open-problems@82f6ea83f0e981f756fd18080ffdd11a447b60a8`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T144532Z-account03-B09-QFORM-r35/REPORT.md`. In its localized rank-two hub/star branch, a literal physical pair `a,b` retains a pair cross wedge `Delta_T` and a pair-anchored physical third volume

   `V_ab(S)=sum_{k in S} sum_{J subset T, |J|=3} det A[{a,b,k},J]^2`,

   with `V_ab(S)>=27G_*/400`. r35 pays every **exact** algebraic type of the physical `2x2` core but leaves a quantitative near-rank-stratum interpolation debt because the invertible-core bounds deteriorate as the determinant tends to zero.

3. The companion pinned reports `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md` at the same `e5f71d79...` source were read. They preserve the leverage requirements of the absolute-value BL route and report no valid counterexample to the full conjecture.

Corrections retained throughout: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; arbitrary-joint rank-three coarea is false; worst conditional projection-density moments are unavailable; a small nonzero quadratic coefficient cannot be deleted under unrestricted supports; and a single uniformly good physical cross minor is not forced by the three-large-eigenvalue hypothesis.

## 2. Two physical hubs: an explicit linear-small-ball corollary of Theorem H

### Theorem `QFORM-TWOHUB-MIXEDFRAME-UNIFORMCORE-v1`

Let `a,b` be two literal ORIGINAL coordinates, let `I` be a disjoint original-coordinate bank, and condition any further disjoint coordinates. Suppose

`A_II = D + sum_{k=1}^r lambda_k v_k v_k^T`,                    (2.1)

where `D` is diagonal, the `v_k` are orthonormal, and every `lambda_k !=0`. For `i in I` put

`rho_i=((v_1)_i,...,(v_r)_i,A_{ia},A_{ib}) in R^(r+2)`,        (2.2)
`G=sum_{i in I} rho_i rho_i^T`.                                (2.3)

Assume `G>0` and

`rho_i^T G^(-1) rho_i <=1/2` for every `i in I`.               (2.4)

Then for **arbitrary** symmetric physical hub core

`E=A[{a,b},{a,b}]`,                                            (2.5)

arbitrary same-side/cross blocks involving the conditioned coordinates, and arbitrary affine terms, the law of the full quadratic polynomial has a continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_r [det(G) prod_{k=1}^r |lambda_k|]^(-1/(r+4)),`          (2.6)

where

`C_r = 4 (r+4)/(r+2) 2^(-4/(r+4)).`                            (2.7)

Consequently every interval `L` obeys the direct linear small-ball estimate

`boxed:
 P{Q in L}
 <= C_r [det(G) prod_k |lambda_k|]^(-1/(r+4)) |L|.`            (2.8)

No probability squaring or Weyl decoupling is used.

### Proof

Theorem H at the pinned `e5f71d79...` source, with hub set `H={a,b}`, gives for `t!=0`

`|phi_Q(t)|
 <=(2|t|)^(-2)
   prod_k (4*pi*|t lambda_k|)^(-1/2)
   (4*pi)^(r+2) det(G)^(-1/2).`                                (2.9)

Set

`alpha=2+r/2=(r+4)/2`,                                        (2.10)

and

`K_r=(1/4)(4*pi)^alpha
     [det(G) prod_k |lambda_k|]^(-1/2).`                       (2.11)

Thus

`|phi_Q(t)| <= min(1,K_r |t|^(-alpha)).`                       (2.12)

Because `alpha>1`, the envelope is integrable. With

`T=K_r^(1/alpha)`,                                             (2.13)

an exact integration gives

`integral_R min(1,K_r |t|^(-alpha)) dt
 =2[T+K_r integral_T^infinity t^(-alpha)dt]
 =2 alpha/(alpha-1) K_r^(1/alpha).`                            (2.14)

Fourier inversion therefore gives

`||p_Q||_infinity
 <= alpha/[pi(alpha-1)] K_r^(1/alpha)
 =4 (r+4)/(r+2) 2^(-4/(r+4))
   [det(G) prod_k |lambda_k|]^(-1/(r+4)),`                     (2.15)

which is (2.6). `phi_Q in L^1` gives a continuous density. Integrating that density over `L` gives (2.8).

The important structural point is that the physical pair core (2.5) stays wholly inside the hub phase permitted by Theorem H. It is never inverted, completed, or treated as a perturbation. Hence (2.6) is uniform as `E` crosses the zero, rank-one, definite and indefinite strata. QED.

For `r=0`, (2.6) gives `4 det(G)^(-1/4)` for a diffuse two-star with diagonal leaf curvature. For the first genuinely dense same-side case `r=1`,

`C_1=(5/3)2^(6/5)=3.828994516656783...`.                       (2.16)

## 3. Exact conversion of the partner's anchored physical volume

The rank-one same-side case admits a useful source-coordinate identity linking r35's volume currency directly to (2.6).

Let `S,T` be disjoint leaf banks and suppose on `S union T`

`A_leaf = D + epsilon q q^T`, `epsilon in {+1,-1}`,            (3.1)

with `D` diagonal. Keep the physical hub pair `a,b`. On `T` define

`u=(A_{ja})_{j in T}`, `v=(A_{jb})_{j in T}`,                  (3.2)

and

`G_T=Gram(q_T,u,v)`.                                           (3.3)

For `k in S` and `J subset T`, `|J|=3`, the diagonal part contributes no `k x J` entries. Therefore

`det A[{a,b,k},J]
 =epsilon q_k det([u_J;v_J;q_J]).`                             (3.4)

Squaring, summing first over `J`, and using Cauchy--Binet gives

`sum_{|J|=3} det A[{a,b,k},J]^2
 =q_k^2 det(G_T).`                                             (3.5)

Summing over `k in S` yields the exact identity

`boxed:
 V_ab(S)=||q_S||_2^2 det(G_T).`                                (3.6)

This is a literal physical-minor identity; no spectral rotation of the product law occurs.

To apply (2.6), write `q=||q|| v_1` and `lambda_1=epsilon ||q||^2`. Scaling the first mixed-frame column from `v_1` to `q` multiplies its Gram determinant by `||q||^2`, while normalized leverages are invariant under an invertible column rescaling. Therefore

`|lambda_1| det G(v_1,u,v)=det G(q,u,v)=det(G_T).`              (3.7)

If the mixed-frame leverages on `T` are at most `1/2`, conditioning `X_S` and every other outside coordinate and applying (2.6) with `r=1` gives

`boxed:
 ||p_Q||_infinity
 <=(5/3)2^(6/5) det(G_T)^(-1/5).`                              (3.8)

Using (3.6), whenever `V_ab(S)>0`,

`boxed:
 ||p_Q||_infinity
 <=(5/3)2^(6/5)
   (||q_S||_2^2/V_ab(S))^(1/5).`                              (3.9)

The same coefficient multiplies interval length, and this branch has a continuous density.

Equation (3.9) is the desired near-stratum interpolation for this leaf geometry: **the bound contains no determinant, eigenvalue, or inverse of the physical hub core `E`.** The dense same-side rank-one operator `epsilon q q^T` is not conditioned away; its transverse direction is spent jointly with the two source-coordinate stars.

In the partner r35 localized branch, where `V_ab(S)>=27G_*/400`, (3.9) also implies the coarser compiler bound

`||p_Q||_infinity
 <=(5/3)2^(6/5)
   (400 ||q_S||_2^2/(27G_*))^(1/5)`                            (3.10)

whenever the same rank-one-plus-diagonal and mixed-leverage hypotheses hold.

## 4. Actual target-valid near-stratum family

This section applies both the pinned mixed-hub theorem and the completed partner result to a concrete owner-target family.

Let `S,T` be disjoint original-coordinate banks, `|T|=m>=6`. Choose flat orthonormal Walsh vectors `c_1,c_2,w` on `T`, and a flat unit vector `s` on `S`. Put

`q=(s+w)/sqrt(2)`.                                             (4.1)

For arbitrary real `delta`, define

`Q_delta
 =X_a^2+delta X_b^2
  +2 X_a <c_1,X_T>
  +2 X_b <c_2,X_T>
  +<q,X_{S union T}>^2.`                                      (4.2)

All inputs remain arbitrary independent cap-one laws.

### 4.1 Exact target spectrum

The five vectors `e_a,c_1,e_b,c_2,q` are orthonormal. On their span, the coefficient matrix is

`[[1,1],[1,0]] direct_sum [[delta,1],[1,0]] direct_sum [1].`   (4.3)

Thus the nonzero spectrum is

`{(1+sqrt(5))/2,(1-sqrt(5))/2,
  (delta+sqrt(delta^2+4))/2,
  (delta-sqrt(delta^2+4))/2,1}.`                               (4.4)

The first block contributes one eigenvalue of modulus greater than one. The second block has determinant `-1`, so at least one of its two eigenvalues has modulus at least one. The last eigenvalue equals one. Hence (4.2) satisfies the **full three-large-eigenvalue hypothesis for every real `delta`**, including `delta=0`.

### 4.2 Mixed-frame payment

On `T`, the mixed frame is `(q_T,c_1,c_2)`. Since `q_T=w/sqrt(2)`,

`G_T=diag(1/2,1,1)`, `det G_T=1/2`.                            (4.5)

Flatness gives normalized leverage

`1/m+1/m+1/m=3/m<=1/2`.                                       (4.6)

Therefore (3.8) gives, uniformly in `delta`,

`boxed:
 ||p_{Q_delta}||_infinity
 <=(5/3)2^(7/5)
 =4.398359702576314...`                                        (4.7)

and

`boxed:
 P{Q_delta in L} <=4.399 |L|.`                                 (4.8)

The density is continuous.

The physical pair cross wedge is `Delta_T=1`, while (3.6) gives

`V_ab(S)=(1/2)(1/2)=1/4`.                                     (4.9)

### 4.3 Actual use of account03/B09 r35 and the improvement at the rank transition

For this family the physical hub core is

`E_delta=diag(1,delta)`.                                       (4.10)

Apply the completed partner r35 exact-core routing with the actual `Delta_T=1` and `V_ab(S)=1/4`:

- `delta=0`: the rank-one branch gives

  `||p_Q||_infinity
   <=4*2^(3/4)e^(1/4)(sqrt(2))^(1/2)
   =10.2722033335...`.                                         (4.11)

- `0<delta<=1`: the definite branch gives

  `||p_Q||_infinity <=pi delta^(-1/2)`.                        (4.12)

- `-1<=delta<0`: the indefinite branch gives

  `||p_Q||_infinity
   <=11.463 *4^(1/20) |delta|^(-1/2)
   <12.286 |delta|^(-1/2)`.                                   (4.13)

Thus the partner theorem identifies the precise near-stratum proof blow-up on the two invertible sides, even though its exact rank-one endpoint is finite. The mixed-hub payment (4.7) replaces all three lines by one uniform bound `4.399` across the transition. This is an actual quantitative interpolation, not a declaration that the small coefficient can be ignored.

The reason it works is structural: the third source-compatible resource is the dense same-side direction `q`, which is transverse to both physical star rows and is retained in the phase until the mixed-frame Brascamp--Lieb integration.

## 5. What is and is not solved

The new theorem pays every localized physical pair core **provided** the active opposite-bank same-side operator has a diagonal-plus-low-rank decomposition with a quantitatively nondegenerate mixed frame. In particular, the physical core may be arbitrarily small, singular, indefinite, or large; none of those regimes costs a reciprocal core determinant.

It does **not** show that a general symmetric leaf operator contains such a packet after a product-preserving disjoint partition. One cannot rotate the leaf bank and declare the new coordinates independent. Nor may one throw the residual leaf operator into a small perturbation: input supports are unrestricted.

Accordingly the remaining B09 debt is genuinely about routing **general leaf curvature**. A useful next formulation is:

`QFORM-LOCALIZED-HUBPAIR-GENERAL-LEAFCURVATURE-ROUTING-v1`:

Given the partner's fixed physical pair and `V_ab(S)>=27G_*/400`, prove that either

1. a disjoint subbank supports a diagonal-plus-low-rank mixed-frame packet satisfying a universal leverage/determinant gate, so `QFORM-TWOHUB-MIXEDFRAME-UNIFORMCORE-v1` applies; or
2. the residual general leaf operator itself, together with the anchored third volume, gives a direct `O(|L|)` estimate before any reciprocal pair determinant is paid; or
3. route to an already-paid physical-pair/ridge/definite/multi-cross exit.

This is narrower than r35's near-stratum debt: the rank transition is no longer an analytic obstruction in the mixed-frame subclass. Full QFORM remains OPEN, and the pinned counterexample search supplies no valid counterexample to it.
