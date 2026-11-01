SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T12:14:44Z.
attacking: elevate a physical star center into a three-coordinate hub and extract a literal two-hub diffuse cross packet with a direct O(interval length) bound.

# fleet01/B09 — three-hub elevation closes the strict-N3 diagonal-complement / leaf-star branch

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This run closes a substantial global strict-N3 branch: after elevating one original star-center coordinate, if the remaining physical complement has diagonal quadratic block, then the full form has a continuous density bounded by an explicit universal constant `<5.536`. The proof uses only original-coordinate conditioning and a deterministic three-column selection lemma. It does not rotate the random input, does not discard a small quadratic perturbation, and does not pass through a square-root small-ball estimate.

## 1. Fresh source inputs and corrections


The live correction ledger and the newest fleet03/B09 correction were consumed. In particular, this proof does **not** use: law-uniform pointwise quadratic-phase decay; post-rotation independence; an arbitrary-joint coarea bound; a worst conditional projection-density supremum; a universally good single physical minor; the false `max singleton third-volume => low-rank closeness` implication; or a small-matrix-norm-as-small-random-error step.

Two completed analytic sources are used at equations:

1. **Designated partner fleet02/B09** `QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`, canonical source

   `yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`,

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T064043Z-fleet02-B09-QFORM-r13/REPORT.md`.

   For two literal physical hubs and a diagonal leaf block, if `G` is the Gram matrix of the two physical hub-to-leaf columns and `rho` is the determinant-weighted probability that two iid two-row bases are disjoint, then

   `||p_Q||_infinity <= 2 sqrt(e) [rho det G]^(-1/4)`,          (1.1)

   with a continuous density and the same coefficient multiplying every interval length. The physical two-hub core, conditioned outside blocks, and affine terms are arbitrary.

2. **Newest owner-required volume theorem**, canonical source

   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

   For an original-coordinate cross block `M`, `Z=e_3(M^T M)>0`, and `1<=q<3/2`, if its row third-volume marginals obey `alpha_i<=q/2`, then

   `||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`,        (1.2)

   continuously, with arbitrary same-side phases and outside couplings retained.

The newest fleet03/B09 aggregate-stability theorem

`yspennstate/math-open-problems@e8b97d9dcd8dd85cacc8fc73c2be4e86fde4b27a`

was also read. Its correction that a small **maximum** singleton augmentation volume does not imply closeness is respected; no such maximum argument appears below.

## 2. Strict N3 entry estimate

Fix

`tau=1/128`,
`eta=sqrt(tau+tau^2)=0.08873294290312927`.                    (2.1)

Assume the strict no-pivot hypotheses

`s_3(A)>=1`,
`|A_ii|<tau`,
`|det A[{i,j},{i,j}]|<tau` for every `i!=j`.                  (2.2)

Then every physical off-diagonal coefficient satisfies

`|A_ij|^2
 = |A_ii A_jj - det A[{i,j},{i,j}]|
 <= |A_ii A_jj|+|det A[{i,j},{i,j}]|
 < tau^2+tau`,                                                 (2.3)

so

`|A_ij|<eta`.                                                  (2.4)

This is a deterministic statement about the actual matrix, not about rotated eigen-coordinates.

## 3. New theorem

### Theorem `QFORM-N3-THREEHUB-DIAGONAL-COMPLEMENT-v1`

Under (2.2), suppose there is a set `K` of exactly three **original physical coordinates** such that, with `R=K^c`, the principal block `A_RR` is diagonal. No restriction is imposed on the physical `3 x 3` block `A_KK` or on the cross block `A_RK` beyond the strict-N3 inequalities already in (2.2).

Then `Q=X^T A X` has a continuous density and

`boxed: ||p_Q||_infinity < 5.536.`                             (3.1)

Consequently, for every interval `I`,

`boxed: P{Q in I} < 5.536 |I|.`                               (3.2)

This immediately covers a two-hub packet whose arbitrary within-leaf off-diagonal curvature is a physical star: elevate the star center into `K`; the surviving complement is diagonal.

### Proof

Write the actual physical block decomposition

`A = [[B, M^T],
      [M, D]]`,                                                (3.3)

where `B=A_KK` is `3 x 3`, `D=A_RR` is diagonal, and `M=A_RK` has three physical columns.

By (2.1)-(2.4), the row-sum bound gives

`||B||_op <= tau+2eta`,
`||D||_op <= tau`.                                             (3.4)

Set

`b=tau+2eta=0.18527838580625855`,
`c=1-b=0.8147216141937414`.                                   (3.5)

Let

`A_cross=[[0,M^T],[M,0]]`,
`E=diag(B,D)`.                                                 (3.6)

Then `||E||_op<=b`. If the singular values of `M` are `sigma_1>=sigma_2>=sigma_3>=0`, the singular values of `A_cross` are each `sigma_j` repeated twice. Therefore

`s_3(A_cross)=sigma_2(M)`.                                    (3.7)

Singular-value Lipschitz continuity gives

`1 <= s_3(A) <= s_3(A_cross)+||E||_op`,                        (3.8)

hence

`boxed: sigma_2(M)>=c.`                                       (3.9)

In particular, the augmented physical cross has rank at least two. This already rules out the rank-one star obstruction without conditioning or inversion.

Now put

`H=M^T M`,
`lambda_1>=lambda_2>=lambda_3>=0`                              (3.10)

for the eigenvalues of `H`. Thus `lambda_2=sigma_2(M)^2>=c^2`.

For each two-element physical hub pair `S subset K`, let `N_S=M[:,S]` and `G_S=N_S^T N_S=H[S,S]`. The sum of the three physical `2 x 2` principal Gram determinants is the second elementary symmetric polynomial:

`sum_(|S|=2) det G_S
 = e_2(H)
 = lambda_1 lambda_2+lambda_1 lambda_3+lambda_2 lambda_3
 >= lambda_1 lambda_2`.                                       (3.11)

Choose one literal physical pair `S` with

`det G_S >= lambda_1 lambda_2/3`.                              (3.12)

Since `lambda_max(G_S)<=lambda_1`,

`lambda_min(G_S)
 = det G_S/lambda_max(G_S)
 >= lambda_2/3
 >= c^2/3`.                                                    (3.13)

Also

`det G_S >= lambda_2^2/3 >= c^4/3`.                           (3.14)

Let `n_i` be the two-entry row of `N_S` corresponding to physical leaf `i in R`, and let

`ell_i=n_i^T G_S^(-1)n_i`                                     (3.15)

be its whitened row leverage. Both entries of `n_i` are actual off-diagonal coefficients, hence by (2.4)

`||n_i||^2 <2eta^2`.                                          (3.16)

Using (3.13),

`ell_i <= 2eta^2/(c^2/3)
       = 6eta^2/c^2
       =: q_0
       = 0.07117091432392135 <1/2`.                            (3.17)

Let `w_T` be the two-frame Pluecker basis law for the whitened matrix `N_S G_S^(-1/2)`, and let `rho` be the probability that two iid bases are disjoint. The inclusion probability of row `i` is exactly `ell_i`, and `sum_i ell_i=2`. Therefore, by the union bound through the expected intersection size,

`1-rho
 = P(T cap T' != empty)
 <= E|T cap T'|
 = sum_i ell_i^2
 <= q_0 sum_i ell_i
 =2q_0`.                                                       (3.18)

Thus

`boxed: rho >= rho_0:=1-2q_0
 =0.8576581713521573.`                                        (3.19)

Now condition only on the **third original physical coordinate** in `K\S`. This preserves independence of the two selected literal hubs and every leaf coordinate. The leaf quadratic block remains the exact diagonal matrix `D`; the conditioned hub creates only affine terms and is among the arbitrary outside blocks allowed by the designated fleet02/B09 theorem. Apply (1.1) to the selected literal physical pair:

`||p_Q||_infinity
 <=2sqrt(e)[rho det G_S]^(-1/4)`                               (3.20)

and hence, using (3.14) and (3.19),

`||p_Q||_infinity
 <= [2sqrt(e) 3^(1/4)/(c rho_0^(1/4))]
 =5.535027140807026... <5.536`.                               (3.21)

The partner theorem supplies a continuous density and the identical coefficient times interval length. This proves (3.1)-(3.2). QED.

### Why this avoids the earlier losses

The only conditioning is on an original coordinate. The deterministic Gram whitening in (3.15) is not a rotation of the random variables. There is no pointwise scalar stationary-phase estimate, no probability squaring into an `O(sqrt(|I|))` bound, and no replacement of a small matrix coefficient by a small random variable. The final interval exponent is exactly one.

## 4. Star elevation interpretation

Start instead with two literal old hubs `h_1,h_2` and a leaf bank `L={s} union R`. Allow **arbitrary weighted and signed star curvature** from the physical leaf `s` into every coordinate of `R`, while assuming only that `A_RR` is diagonal. The old leaf block may therefore contain the dense star

`A_L,L = [[A_ss, d^T],[d,D]]`,                                (4.1)

with arbitrary `d` subject only to the N3 physical-entry bounds.

Elevate the same original coordinate `s` into the hub set

`K={h_1,h_2,s}`.                                               (4.2)

The augmented physical cross becomes

`M=[C_R,d]`,                                                   (4.3)

while the surviving leaf block is exactly `D`, diagonal. Theorem 3 now pays the entire packet uniformly. Thus **arbitrary within-bank star curvature is not a surviving strict-N3 obstruction**.

This is stronger than the early-checkpoint route: no weighted-EKR star/triangle case split is needed. The finite three-column selection in (3.11)-(3.13), combined with the physical coefficient cap, automatically produces a diffuse literal two-hub frame.

## 5. Newest-Claude theorem applied to an actual target inequality

The owner-required volume theorem (1.2) is applied here to a literal star-elevation family, not merely cited.

For `m>=129`, take three physical hubs `K={h_1,h_2,s}` and three disjoint physical leaf groups `I_1,I_2,I_3`, each of size `m`. Let `u_a=m^(-1/2) 1_(I_a)` and put

`M_m=[u_1,u_2,u_3]`,
`A_m=[[0,M_m^T],[M_m,0]]`.                                    (5.1)

Viewed before elevation, `s` is a leaf-star center coupled to the whole third group, while `h_1,h_2` are the old hubs. All diagonals vanish, every nonzero physical off-diagonal entry is `1/sqrt(m)`, and every physical pair determinant has magnitude either `0` or `1/m<1/128`. Hence `A_m` lies in strict N3 at `tau=1/128`.

The three singular values of `M_m` are exactly one, so the nonzero spectrum of `A_m` is

`{1,1,1,-1,-1,-1}`.                                           (5.2)

For the third-volume law, a basis chooses one row from each disjoint group. Therefore

`Z=e_3(M_m^T M_m)=1`,
`alpha_i=1/m <=1/2`.                                          (5.3)

Take `q=1` in the newest volume theorem (1.2). It gives the actual universal inequality

`boxed: ||p_(X^T A_m X)||_infinity <=3e<8.155`,                (5.4)

with a continuous density and

`boxed: P{X^T A_m X in I} <=3e |I|`                           (5.5)

for every admissible cap-one product law and every interval `I`. Theorem 3 gives the sharper `<5.536` bound on the same family, but (5.4) is the required direct application of the newest volume result to an exact target-valid matrix.

## 6. Relation to the newest aggregate-stability result

Fleet03/B09 r31 proves that for a rank-two two-hub cross `C` and arbitrary leaf self-block `D`, the correct defect from the exact no-augmentation model is the **aggregate** third-volume quantity

`[sum_k Gamma_k^2]^(1/2)/sqrt(det(C^T C))`,                    (6.1)

not `max_k Gamma_k`. Its Walsh family shows the latter can tend to zero while the former remains order one.

The theorem here is compatible with that correction. It does not infer global structure from one small singleton augmentation. Instead it closes the exact structural case where a physical star center can be elevated so that the remaining complement is diagonal. The general arbitrary `D` branch remains unpaid.

## 7. First unpaid B09 implication after this run

`QFORM-N3-THREEHUB-GENERAL-COMPLEMENT-ROUTING-v1`:

Starting from the near-coloop/high-leverage physical leaf produced in the previous B09 run, elevate that literal leaf into the hub set. If the remaining complement is diagonal, the present theorem closes the branch. For genuinely arbitrary remaining complement curvature, combine the existing low-leverage vertex-cover puncture theorem and fleet03/B09's aggregate singleton-volume identity to force one of:

1. a low-leverage physical conditioning set after which the complement becomes diagonal and Theorem 3 applies;
2. a quantitative rank-at-least-three volume packet paid by the newest volume theorem;
3. a determinant-balanced low-rank same-side packet paid by grouped mixed-hub smoothing; or
4. a bounded physical collar / ridge / definite-pair / grouped-square exit.

The missing implication is the **exhaustive structural routing for arbitrary `D`**. No claim here removes that debt. Full QFORM essential boundedness and full-target continuity remain OPEN.

## 8. Review status

This is a new supporting theorem, not a full candidate proof. No independent end-to-end review of this new theorem is claimed in this run. The completed analytic ingredients are source-pinned above; the new deterministic column-selection and strict-N3 splice should receive an independent check before proof assembly promotes it beyond supporting status.
