SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-23T10:16:41Z.
attacking: the newest completed fleet02/B20 exact-rank-three three-packet survivor; close its Cases A/B by converting the bounded physical core plus the high-leverage row into a quantitatively nondegenerate physical 2-plane, then pay by a scalar pivot or an indefinite physical pair.

# fleet01/B20 auto11 — physical-plane closure of fleet02/B20 Cases A/B

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** revision `2026-09-22.15`, QFORM sole research target; no later B20 stop observed at start.  
**Run status:** `ESSENTIAL_STEP_APPLIED / FLEET02-B20 CASES A+B PAID / FULL QFORM OPEN`.  
**Continuity:** OPEN globally; the new payment below proves essential boundedness only.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not claimed as authenticated learned-memory receiver use.  
**Model self-report:** `GPT-5.6 Sol`; configured reasoning effort and provider reasoning counters are unexposed (`UNKNOWN/null`).

## 1. Exact sources consumed

The newest completed designated fleet02/B20 result used here is

`yspennstate/math-open-problems@6a4e9c575bcea2bbc12efd5a439bfb94f290d399`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260923T090422Z-fleet02-B20-QFORM-auto11/REPORT.md`.

Its exact-rank-three chamber is

`A = R M R^T`, `R^T R=I_3`, `s_min(M)>=1`,                       (1.1)

where the rows `r_i in R^3` are the physical-coordinate spectral rows. The partner proves that after already-paid branches, there is an ORIGINAL-coordinate core `K`, `|K|<=18`, whose Gram

`T=sum_(i in K) r_i r_i^T`                                       (1.2)

has eigenvalues/eigenbasis

`lambda_1>63/64`, `lambda_3<1/64`, `(v_1,v_2,v_3)`,             (1.3)

and there is a physical row `h` with

`||r_h||^2>1/2`.                                                  (1.4)

Its remaining three-packet compiler has three explicit cases. This report pays **Case A and Case B**. Case C (`h in K`) is left separate.

The scalar-pivot receiver used below is `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`, from

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For a full exact-rank-three target with nonzero eigenvalue magnitudes at least one, it gives

`||p_Q||_infinity <=128/sqrt(|A_ii|)`                            (1.5)

for every nonzero physical scalar pivot `A_ii`.

The indefinite-pair receiver is `QFORM-RANK3-INDEFINITE-PAIR-PIVOT-v1`, from

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

If a physical principal pair `B` is invertible indefinite, with

`D=|det B|`, `kappa=sigma_min(B)`,                               (1.6)

then in the present exact-rank-three scale `s=1`,

`||p_Q||_infinity <=8 sqrt(5) (D kappa)^(-1/4)`.                 (1.7)

Both receivers allow the original cap-one product laws and retain arbitrary affine shifts in their stated scopes. No rotated random coordinates are declared independent.

## 2. A bounded-core row with a fixed longitudinal component

Because

`sum_(i in K) <r_i,v_1>^2=lambda_1>63/64`                       (2.1)

and `|K|<=18`, there is a physical coordinate `p in K` such that

`|<r_p,v_1>|^2 > (63/64)/18 = 7/128`.                            (2.2)

Write

`p_j=<r_p,v_j>`, `h_j=<r_h,v_j>`.                                (2.3)

Every physical row satisfies `||r_i||<=1`, because `R R^T` is an orthogonal projection.

The key point is that the partner's Cases A/B provide more geometry than the generic three-packet statement. That extra geometry is what makes the local two-coordinate extraction below valid; this is not the refuted inference “packet mass alone gives a good local pivot.”

## 3. Case A gives a quantitative physical 2-plane

In partner Case A,

`h notin K`, `lambda_2>=1/64`,                                   (3.1)

and the already-paid robust-update branch has been removed. The surviving inequalities are

`h_1^2<1/64`, `h_3^2<1/64`, `h_2^2>15/32`.                       (3.2)

Let

`w=r_p cross r_h`.                                                (3.3)

Its `v_3` component satisfies

`|<w,v_3>|=|p_1 h_2-p_2 h_1|`
` >= |p_1||h_2|-|p_2||h_1|`
` > sqrt((7/128)(15/32))-1/8`
` = (sqrt(105)-8)/64`.                                           (3.4)

Thus

`||r_p cross r_h||^2 > d_0`,                                     (3.5)

where

`d_0 := ((sqrt(105)-8)/64)^2
      =0.0012326141954703185...`.                                 (3.6)

## 4. Case B is even more transverse

In partner Case B,

`h notin K`, `lambda_2<1/64`.                                    (4.1)

Because the complement of `K` carries less than `1/64` total `v_1` mass,

`h_1^2<1/64`.                                                      (4.2)

Together with `||r_h||^2>1/2`,

`h_2^2+h_3^2>31/64`.                                              (4.3)

Choose `j in {2,3}` with

`h_j^2>31/128`.                                                    (4.4)

For the same `p` from (2.2), since each term is bounded by the corresponding eigenvalue of `T`,

`p_2^2<=lambda_2<1/64`, `p_3^2<=lambda_3<1/64`.                  (4.5)

Let `k` be the other transverse index. Then the `v_k` component of `r_p cross r_h` obeys

`|<r_p cross r_h,v_k>|`
` >= |p_1||h_j|-|p_j||h_1|`
` > sqrt((7/128)(31/128))-1/64`
` = (sqrt(217)-2)/128`.                                           (4.6)

Its square is

`0.00989235354915619... > d_0`.                                  (4.7)

Hence the common conclusion (3.5) holds in **both Cases A and B**.

## 5. Physical-plane compression lemma

Set the `3 x 2` physical-row matrix

`C=[r_p  r_h]`.                                                    (5.1)

Then

`det(C^T C)=||r_p cross r_h||^2>d_0`,                             (5.2)

while

`tr(C^T C)=||r_p||^2+||r_h||^2<=2`.                              (5.3)

Therefore

`sigma_min(C)^2 >= det(C^T C)/tr(C^T C) > d_0/2`.                (5.4)

Let `U` be a `3 x 2` orthonormal basis of `range(C)` and write

`C=U G`,                                                          (5.5)

where `G` is invertible. Put

`H=U^T M U`.                                                      (5.6)

Since all three eigenvalues of `M` have absolute value at least one, the middle eigenvalue of `M` lies either in `[1,infinity)` or in `(-infinity,-1]`. By Cauchy interlacing for the two-dimensional compression `H`,

`||H||_op>=1`.                                                     (5.7)

The physical principal pair on coordinates `{p,h}` is

`B=A[{p,h},{p,h}]=C^T M C=G^T H G`.                              (5.8)

Choose a unit eigenvector `y` of `H` with eigenvalue of modulus `||H||_op`, and let

`x=G^{-1}y/||G^{-1}y||`.                                         (5.9)

Then

`||B||_op >= |x^T B x|`
` = ||H||_op / ||G^{-1}y||^2`
` >= sigma_min(G)^2`
` = sigma_min(C)^2`
` > d_0/2`.                                                       (5.10)

This is the crucial new implication: the bounded partner core plus the Case-A/B high row forces a quantitatively nondegenerate **physical** two-coordinate compression.

## 6. Scalar-or-indefinite-pair payment

Write

`B=[[a,b],[b,d]]`,                                                (6.1)

and define

`rho := d_0/4 = ((sqrt(105)-8)^2)/16384
      =0.0003081535488675796...`.                                 (6.2)

Because for a symmetric `2 x 2` matrix

`||B||_op<=||B||_F<=2 max(|a|,|b|,|d|)`,                         (6.3)

(5.10) implies

`max(|a|,|b|,|d|)>rho`.                                          (6.4)

### 6.1 A scalar diagonal is not tiny

If

`|a|>=rho/2` or `|d|>=rho/2`,                                   (6.5)

apply (1.5) at that physical coordinate:

`||p_Q||_infinity
 <=128/sqrt(rho/2)
 =128 sqrt(2/rho)
 =10311.963820900834...
 <10312`.                                                        (6.6)

### 6.2 Both scalar diagonals are tiny

Otherwise

`|a|<rho/2`, `|d|<rho/2`.                                       (6.7)

Then (6.4) forces

`|b|>rho`,                                                       (6.8)

so `B` is indefinite. Indeed

`D=|det B|=|ad-b^2|=b^2-ad`
` > rho^2-rho^2/4`
` =3rho^2/4`.                                                     (6.9)

Moreover

`sigma_max(B)<=|b|+rho/2`.                                      (6.10)

For a nonsingular `2 x 2` matrix, the product of its singular values is `D`, so

`kappa=sigma_min(B)=D/sigma_max(B)`
` >(b^2-rho^2/4)/(b+rho/2)`
` =b-rho/2`
` >rho/2`.                                                       (6.11)

Apply the physical indefinite-pair theorem (1.7):

`||p_Q||_infinity`
` <8 sqrt(5) [(3rho^2/4)(rho/2)]^(-1/4)`
` =8 sqrt(5) (3rho^3/8)^(-1/4)`
` =9828.602970807939...`
` <9829`.                                                        (6.12)

Combining (6.6) and (6.12),

`boxed(||p_Q||_infinity <10312)`                                 (6.13)

throughout partner Cases A and B.

## 7. New theorem and exact scope

### `QFORM-18CORE-HIGHROW-CASEAB-PHYSICAL-PAIR-PAYMENT-v1`

Under the exact-rank-three setup (1.1) and the completed fleet02/B20 auto11 survivor hypotheses (1.2)--(1.4), **every state in its Case A or Case B has an essentially bounded density satisfying (6.13)**.

No moment, iid, support, log-concavity, Gaussian, or rotated-independence hypothesis was added. Every selected object `p,h` is an original physical coordinate. The only spectral rotations occur inside deterministic three-dimensional linear algebra.

This theorem is stronger than the previous generic high-row transverse-cut compiler on these two partner cases: it turns the aggregate geometry into an actual paid scalar/pair receiver. It does **not** assert that generic three-packet masses alone yield a good physical pair; the partner's stress/counterexample warnings remain valid.

## 8. What remains

Inside the fleet02/B20 exact-rank-three three-case compiler, the first unclosed case is now **Case C**, where the high-leverage row `h` lies inside the nearly rank-one core `K`. In that case the partner rotates the transverse deterministic plane so that `{h}` supplies the first packet, while the other two directions are distributed across two potentially diffuse original-coordinate banks. The local-pair argument above cannot simply be repeated because no single row in either diffuse bank need have a fixed transverse coefficient.

A natural next target is therefore

`QFORM-CASEC-HUB-TWODIFFUSE-BANK-PAYMENT-v1`:                     (8.1)

retain the genuine physical hub `h`, aggregate each diffuse transverse bank before reciprocal inversion, and feed either a fixed-volume bank or a near-hyperbolic two-bank structure into an already source-valid grouped/pair/ridge receiver. The previous B20 transverse-cut compiler remains relevant to precisely this residual geometry.

Separate arbitrary-extra-spectrum/N3/O0 debts also remain. Thus the full target is **OPEN**. This report does not claim a continuous density representative.

## 9. Corrections explicitly preserved

The proof does not use any of the invalidated interfaces: law-uniform pointwise quadratic oscillatory decay; post-rotation independence; unrestricted three-dimensional joint-density coarea; worst-fiber conditional density caps or positive conditional-density moments; a generic one-good-minor extraction; deletion of a small nonzero spectral tail; or the false implication from packet mass alone to a robust local pivot.

## 10. Arithmetic self-check

A local arithmetic self-check (not an independent mathematical review) gives

`d_0=0.0012326141954703185`,
`rho=0.0003081535488675796`,
`128 sqrt(2/rho)=10311.963820900834`,
`8 sqrt(5)(3rho^3/8)^(-1/4)=9828.602970807939`,
`((sqrt(217)-2)/128)^2=0.00989235354915619>d_0`.

The analytic proof is Sections 2--7; these decimal evaluations only check the displayed constants.
