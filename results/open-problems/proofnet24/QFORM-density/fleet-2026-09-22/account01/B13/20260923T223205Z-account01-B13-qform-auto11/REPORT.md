SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T22:32:05Z.
attacking: grouped-hub / three-leaf transverse curvature, eliminating reciprocal selection of one physical hub pair and applying account02/B13 r35's D5 gate to the remaining low-transverse-rank chamber.

# account01/B13 — grouped hub volume times three-leaf transverse curvature

Programme: `QFORM-DENSITY-3EIG-20260922`. Control: OWNER CONTROL revision `2026-09-22.15`. Execution: `WITHOUT_VERIFIED_BRAIN`. Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**. Continuity of the unrestricted target: **OPEN**.

No rotation of the random variables is declared independent. No pointwise law-uniform quadratic oscillatory decay, unrestricted joint coarea bound, projection-density-only shortcut, bounded support diameter, single-interval extremality, or bounded fragment count is used.

## 1. Inputs actually used

1. `account01/B01`, source-pinned at `yspennstate/math-open-problems@39db1d98a37e71ccc28619a59bc53b79d1be8408`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T083643Z-account01-B01-qform-auto11/REPORT.md`, Theorem `QFORM-RANK2-CROSS-3D-RECEIVER-MIXEDTIME-v1`. If an original-coordinate hub bank `I` and receiver bank `J` have exact rank-two cross block with singular product `Delta=s1*s2`, the entire receiver quadratic part is supported in the three-space spanned by the two cross right-singular directions and one transverse vector `w`, and the transverse quadratic coefficient is `a!=0`, then

`||p_Q||_infinity <= c0 Delta^(-2/5)|a|^(-1/5)`,

where

`c0=15/2^(1/5)=13.058258449441862...`.

Arbitrary hub self-curvature and outside couplings are retained; the proof uses an integrated mixed-time estimate, not a pointwise Fresnel envelope.

2. Designated partner `account02/B13` r35, canonical mathematics `yspennstate/math-open-problems@bcf2076c00cd23415733cae004e13cc67cdd3daa`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T210358Z-account02-B13-robust-schur-twist-r35/REPORT.md`. In particular its proved `QFORM-D5-TRANSVERSE-THREE-MODE-v1` says: for disjoint original banks `I,J,T`, with `M=A[I,J]`, `C=A[I,T]`, `s2(M)>0`, and `t1>=t2>=t3` the singular values of `(I-P2)C` after projecting away the top two left singular vectors of `M`, every slab ratio `rho` obeys

`s1(M)s2(M)t1t2t3 <= (5 sqrt(2e)/rho)^5`.                         (1.1)

Thus three substantial transverse shared-input modes are already paid.

3. The previously completed finite-family purification theorem (account02/B13 r24) remains valid: any finite battery of bounded kernels under arbitrary cap-one product laws can be approximated simultaneously by bounded finite-union unit-measure product indicators. I do not re-prove or rename it here.

## 2. New grouped-hub three-leaf invariant

Let `I` be any original-coordinate bank and let `L={r,s,t}` be three disjoint original coordinates. Put

`B=A[I,L]`                                                        (2.1)

and assume `rank B=2`. Set

`C=B^T B`                                                         (2.2)

and define the scalar

`Theta_{I,L}(A) := | tr( A[L,L] adj(C) ) |`.                       (2.3)

Because `C` is positive semidefinite of rank two, if `nu` is a unit vector spanning `ker B=ker C` and `s1>=s2>0` are the singular values of `B`, then

`adj(C)=s1^2 s2^2 nu nu^T`.                                      (2.4)

Consequently

`Theta_{I,L}(A)=s1^2 s2^2 |nu^T A[L,L] nu|`.                     (2.5)

This is basis-free and aggregates **all** hub rows before any pair is selected.

### Theorem 2.1 — `QFORM-GROUPED-HUB-3LEAF-TRANSVERSE-v1`

For arbitrary independent real inputs with densities at most one, if `rank A[I,L]=2` and `Theta_{I,L}(A)>0`, then the full ambient quadratic form has an essentially bounded density satisfying

`boxed: ||p_{X^T A X}||_infinity <= c0 Theta_{I,L}(A)^(-1/5),`   (2.6)

with

`c0=15/2^(1/5)<13.059`.                                           (2.7)

All coefficients on `I`, all coefficients outside `I union L`, and all couplings to conditioned outside coordinates are arbitrary.

#### Proof

Condition every original coordinate outside `I union L`. The remaining hub self-term is an arbitrary quadratic-plus-affine function of `X_I`, which is permitted by the B01 mixed-time theorem. Since `L` consists of exactly three physical coordinates, after an orthogonal coefficient change inside its deterministic three-dimensional coefficient space, the entire `L`-self quadratic part is automatically supported on the span of the two right-singular directions of `B` plus the unit kernel vector `nu`. This orthogonal change is used only to identify coefficient directions; no independence of the transformed leaf coordinates is asserted. Their joint density remains bounded by one because the original three-dimensional product density is bounded by one and the coefficient change has Jacobian one.

In the notation of the B01 theorem,

`Delta=s1(B)s2(B)`, `a=nu^T A[L,L]nu`.                             (2.8)

Therefore

`||p_Q||_infinity <=c0 Delta^(-2/5)|a|^(-1/5)`

`=c0 [s1^2 s2^2 |a|]^(-1/5)`

`=c0 Theta_{I,L}(A)^(-1/5)`                                       (2.9)

by (2.5). The bound is uniform in the conditioned outside coordinates, so averaging preserves it. QED.

For a slab `J0`, (2.6) is the geometric product-set inequality

`|{x in prod E_i : x^T A x in J0}|
 <=c0 Theta_{I,L}(A)^(-1/5)|J0|`                                  (2.10)

for arbitrary measurable unit-measure product indicators. Hence any actual slab ratio `rho` forces

`boxed: Theta_{I,L}(A) <= (c0/rho)^5
 = (759375/2) rho^(-5).}`                                         (2.11)

No individual physical hub pair appears in (2.11).

## 3. Exact diagonal-plus-rank-two specialization: aggregate pair volume replaces one pair

Suppose now

`A=D+U Lambda U^T`,                                                (3.1)

where `D=diag(d_1,...,d_n)`, `U^T U=I_2`, and `Lambda` is invertible symmetric. Write the physical rows of `U` as `u_i^T`, and

`q_ij=det(u_i,u_j)^2`.                                             (3.2)

For a coordinate bank `K`, put

`G_K=U_K^T U_K`.                                                   (3.3)

Take `I cap L=empty`, `L={r,s,t}`, and assume both `G_I` and `G_L` are positive definite. Then `B=A[I,L]=U_I Lambda U_L^T` has rank two. Its two-dimensional squared singular-volume is

`e_2(B^T B)=det(G_I)(det Lambda)^2 det(G_L).`                      (3.4)

Indeed the product of the two nonzero eigenvalues of `B^T B` equals the determinant of the induced two-dimensional map, giving (3.4).

A kernel vector of `U_L^T` has squared coordinates proportional to the complementary Pluecker squares. Since

`det(G_L)=q_rs+q_rt+q_st`,                                        (3.5)

for unit `nu in ker U_L^T`,

`nu_r^2=q_st/det(G_L)`,
`nu_s^2=q_rt/det(G_L)`,
`nu_t^2=q_rs/det(G_L)`.                                           (3.6)

The rank-two carrier vanishes on `nu`, so

`nu^T A[L,L]nu=nu^T D_L nu
=(d_r q_st+d_s q_rt+d_t q_rs)/det(G_L).`                          (3.7)

Combining (2.5), (3.4), and (3.7) gives the exact cancellation-free denominator identity

`boxed:
 Theta_{I,L}(A)
 =det(G_I)(det Lambda)^2
  |d_r q_st+d_s q_rt+d_t q_rs|.}`                                (3.8)

Finally, by Cauchy--Binet,

`det(G_I)=sum_{i<j, i,j in I} q_ij`.                              (3.9)

Thus the new receiver replaces account03/B13's previously selected hub-pair factor `q_ij` by the **entire aggregate hub pair-volume**. No reciprocal selected minor is paid.

Every slab ratio `rho` therefore satisfies

`boxed:
 det(G_I)(det Lambda)^2
 |d_r q_st+d_s q_rt+d_t q_rs|
 <=(759375/2) rho^(-5).}`                                         (3.10)

## 4. Quantitative localization-or-cancellation alternative

Choose the maximal aggregate hub bank `I=L^c`. Then

`G_I=I_2-G_L`.                                                     (4.1)

For any `eta in (0,1)`, (3.10) gives the following exact dichotomy for every rank-two physical triple `L`.

**Cancellation branch.** If

`det(I_2-G_L)>eta`,                                                (4.2)

then

`boxed:
 |d_r q_st+d_s q_rt+d_t q_rs|
 <= (759375/2) [eta (det Lambda)^2]^{-1} rho^(-5).}`              (4.3)

**Localization branch.** If

`det(I_2-G_L)<=eta`,                                               (4.4)

let `lambda_1>=lambda_2` be the eigenvalues of `G_L`. Since

`det(I-G_L)=(1-lambda_1)(1-lambda_2)
 >=(1-lambda_1)^2`,                                                (4.5)

there is a unit latent direction `v in R^2` with

`boxed: ||U_{L^c}v||_2 <= eta^(1/4).}`                            (4.6)

Thus a high-ratio exact rank-two survivor cannot hide behind many individually tiny hub minors. For every physical triple it must either nearly localize one latent carrier direction onto those three coordinates, or force the signed transverse diagonal curvature in (4.3) to be `O(rho^-5)` after the aggregate pair-volume is paid.

This is a genuinely grouped statement; it survives arbitrarily diffuse Pluecker mass.

## 5. Designated-partner result applied to an actual inequality

Apply account02/B13 r35's completed D5 theorem (1.1). If a rank-two physical cross carrier satisfies

`s1(M)s2(M)>=mu>0`,                                                (5.1)

then, because `t1,t2>=t3`, every slab ratio `rho` obeys

`mu t3^3 <= (5 sqrt(2e)/rho)^5`,                                  (5.2)

hence

`boxed:
 t3 <= (5 sqrt(2e))^(5/3) mu^(-1/3) rho^(-5/3)
 <59.941 mu^(-1/3) rho^(-5/3).}`                                  (5.3)

This is an equation-level use of the designated partner, not a status citation.

The combination of (5.3) with Theorem 2.1 narrows the previously named one-/two-transverse-mode rough endpoint as follows. Three substantial transverse shared-input modes are impossible at high `rho` by (5.3). In the residual low-transverse-rank chamber, **every actual three-coordinate receiver packet whose total grouped hub crossing has rank two** must obey the invariant suppression

`Theta_{I,L}(A)<= (759375/2)rho^-5`.                               (5.4)

In the exact `D+U Lambda U^T` endpoint, (5.4) becomes the explicit localization-or-cancellation alternative (4.3)/(4.6). The remaining obstruction is therefore not "all physical hub pairs are tiny"; aggregate pair volume has been eliminated from the denominator. What remains is systematic near-null kernel curvature / signed cancellation, rank-at-most-one crossing on the relevant three-leaf packets, or finite-center localization.

## 6. Extremal product-law scope

The new receiver is already proved for arbitrary cap-one product laws. At the geometric level, (2.10) holds for every unit-measure product set, including arbitrarily fragmented and widely separated sets. The source-checked finite-family purification theorem may therefore be used without loss of scope when one wants a finite battery of these slab/invariant tests on a strict witness. Nothing here assumes an attained optimizer, a centered uniform law, a common diameter, or a fixed number of fragments.

## 7. Remaining unpaid implication

`QFORM-GROUPED-TRIPLE-NULLKERNEL-OR-FINITECENTER-GLUE-v1`:

Starting from the D5-reduced one-/two-transverse-mode chamber, prove that systematic suppression of every grouped invariant `Theta_{I,L}` either forces a product-preserving finite-center/null-ray normal form already covered by existing bank receivers, or contradicts the third-large-eigenvalue hypothesis. The exact-rank-two formula (3.8) shows the algebraic core: systematic cancellation of `d_r q_st+d_s q_rt+d_t q_rs` must be routed globally rather than by selecting one pair.

The full conjecture remains OPEN. No continuity conclusion is claimed beyond source theorems in their own sufficient branches.
