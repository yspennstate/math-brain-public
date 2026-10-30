SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B05, 2026-09-23T17:28:48Z.
attacking: QFORM-ARBITRARY-PIVOT-SAME-COORDINATE-MIXED-SHEAR-v1 by changing mechanism from scalar/conditional coarea to an exact projected-crossing determinant identity and a diffuse-frame partition. Owner continuation QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z acknowledged.

# fleet01/B05 auto14 — exact Pluecker currency and projected-crossing factor in the heavy-hub mixed-shear state

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Assignment:** quadratic coarea bound.  
**Status:** `NEW SUPPORTING STRUCTURAL THEOREM / NEW DIFFUSE SUBBRANCH DENSITY BOUND / PRECISE REMAINING FACTOR IDENTIFIED / FULL QFORM OPEN`.  
**Regularity:** the diffuse subbranch theorem below has a bounded continuous density by the projected-crossing Fourier theorem; the unrestricted full-target continuity claim remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Input state from the preceding B05 run

Use the exact-rank-three heavy-row state after the support-disjoint longitudinal mass has been absorbed. Thus there is an independent scalar `S` with density cap one, a mixed original-coordinate product bank `X=(X_j)`, rows

`r_j=(u_j,t_j) in R x R^2`,

and a symmetric invertible active matrix `B` such that

`Q = (sqrt(c) S e1 + sum_j r_j X_j)^T B (sqrt(c) S e1 + sum_j r_j X_j)`

up to an arbitrary deterministic affine/constant term arising from previously conditioned coordinates. Here

`c>1/2`,
`sum_j r_j r_j^T = G = diag(rho,1,1)`,
`rho=1-c in (0,1/2)`,

and in the normalization coming from the preceding absorption theorem one has `|det B|>1/2`. The scalar `S` is independent of the mixed bank; no independence is asserted after any spectral rotation.

Write `T` for the matrix with rows `t_j`. Hence

`T^T T = I_2`.                                                    (1.1)

The punctured regime `rho>0` is the one considered here. The exact `rho=0` coloop endpoint was already paid in the preceding run.

## 2. New exact physical-minor identity — all longitudinal overlap cancels

For any two mixed physical coordinates `j,k`, retain the three independent scalar variables `(S,X_j,X_k)` and condition every other original coordinate. The homogeneous `3 x 3` matrix of the retained variables is

`A_{0jk}=P_{jk} B P_{jk}^T`,

where

`P_{jk}=[sqrt(c)e1^T; r_j^T; r_k^T]`.

Therefore

`det A_{0jk}=det(B) det(P_{jk})^2`.

But

`det(P_{jk}) = sqrt(c) det(t_j,t_k)`,

because expansion in the first row deletes the longitudinal entries `u_j,u_k`. Consequently

`boxed(det A_{0jk}=c det(B) det(t_j,t_k)^2).`                    (2.1)

This is independent of every longitudinal coefficient `u_j`.

Cauchy--Binet and (1.1) give

`sum_{j<k} det(t_j,t_k)^2 = det(T^T T)=1`.                       (2.2)

Hence the entire physical three-scalar determinant currency satisfies the exact conservation law

`boxed(sum_{j<k} |det A_{0jk}| = c |det B|).`                    (2.3)

In particular the near-coloop limit `rho->0` does not destroy total three-variable curvature; it only diffuses this curvature among many physical pairs. Applying the previously proved three-independent-scalar coarea theorem pair by pair would pay the reciprocal factor `det(t_j,t_k)^(-2/3)`, so (2.3) pinpoints the aggregation-before-reciprocal issue exactly.

## 3. Exact projected-crossing identity for an arbitrary physical split

Let `I,J` be a partition of the mixed original coordinates. Put

`G_J = sum_{j in J} r_j r_j^T`,
`H_I = sum_{i in I} t_i t_i^T`.

Assume for the moment `G_J>0` and `H_I>0`. Regard the independent scalar `S` as a one-dimensional hub. Its cross vector into the `J` bank is

`m_J = sqrt(c) e1^T B R_J^T`,

so

`S_J^2 := ||m_J||^2 = c h`,
`h:=e1^T B G_J B e1 >0`.                                       (3.1)

The residual quadratic matrix is `A_R=RBR^T`. In the notation of the proved projected-crossing theorem, remove from the `I x J` crossing matrix the row direction of `m_J`:

`C = (A_R)_{I,J}(I-Pi_{m_J})`.

Define

`K = B G_J B - (B G_J B e1)(B G_J B e1)^T/h`.                  (3.2)

A direct multiplication gives

`C C^T = R_I K R_I^T`.                                         (3.3)

Moreover `K e1=0`; since `K` is symmetric, relative to `R e1 + e1^perp` it has the form

`K = 0 direct_sum K_T`,

with a positive definite `2 x 2` block `K_T`. Thus

`C C^T = T_I K_T T_I^T`.                                       (3.4)

The Schur determinant identity applied to `B G_J B` gives

`h det(K_T) = det(B G_J B)=det(B)^2 det(G_J)`.                  (3.5)

Since `C` has rank two, its two-volume is

`Z_2=e_2(CC^T)=det(K_T) det(H_I)`.                              (3.6)

Multiplying (3.1), (3.5), and (3.6) yields the exact identity

`boxed(S_J^2 Z_2 = c det(B)^2 det(G_J) det(H_I).)`              (3.7)

Again, no diagonal-pivot size, Schur condition number, or individual physical coefficient appears.

There is also an exact formula for the two-volume row marginals of `C`. Because `K_T` is invertible, `col(C)=col(T_I)`. Therefore for each `i in I`,

`boxed(alpha_i = t_i^T H_I^{-1} t_i.)`                          (3.8)

Thus the row-marginal gate of the projected-crossing theorem is purely a transverse-frame gate; it is independent of `B` and independent of all longitudinal coefficients.

## 4. Apply the new projected-crossing theorem

The interactive theorem `NEW_PROJECTED_CROSSING.md` proves, for one independent cap-one hub and `ell=2`,

`||p_Q||_infinity < 9.4 (S_J^2 Z_2)^(-1/6)`                    (4.1)

whenever every two-volume row marginal `alpha_i<=1/2`. Arbitrary internal hub functions are allowed, so the hub square `c B_11 S^2` is inside the theorem's scope. Arbitrary quadratic terms internal to `I` and `J`, all diagonals, and affine terms are also allowed.

Substituting the exact identity (3.7) gives the concrete heavy-hub inequality

`boxed(||p_Q||_infinity < 9.4 [c det(B)^2 det(G_J) det(H_I)]^(-1/6).)`   (4.2)

This is a direct application to the actual B05 mixed-shear form, not a generic citation.

## 5. A proved diffuse mixed-shear subbranch

Normalize the mixed rows by

`a_j=(u_j/sqrt(rho),t_j) in R^3`.

Then

`sum_j a_j a_j^T=I_3`.

Define the normalized mixed-leaf leverage

`ell_j=||a_j||^2=u_j^2/rho+||t_j||^2`.                          (5.1)

Assume

`max_j ell_j <= 1/64`.                                         (5.2)

Use the two-part Marcus--Spielman--Srivastava frame partition theorem in exactly the source-pinned form already used in the QFORM ridge-window proof: a Parseval frame with row norms squared at most `epsilon` admits a partition `I,J` for which both partial frame operators have norm at most

`beta=(1/sqrt(2)+sqrt(epsilon))^2`.

For `epsilon=1/64`, set

`beta = 33/64 + sqrt(2)/8`,
`a = 1-beta = (31-8sqrt(2))/64 >0.30759`.                       (5.3)

Because the two frame sums add to the identity,

`a I_3 <= sum_{j in J} a_j a_j^T <= beta I_3`,
`a I_3 <= sum_{i in I} a_i a_i^T <= beta I_3`.                 (5.4)

Let `D=diag(sqrt(rho),1,1)`. Then

`G_J = D (sum_{j in J} a_j a_j^T) D`,

hence

`det(G_J) >= a^3 rho`.                                         (5.5)

The lower-right `2 x 2` principal block of the `I` frame operator is `H_I`, so

`H_I >= a I_2`,
`det(H_I)>=a^2`.                                                (5.6)

Finally, by (3.8) and (5.2),

`alpha_i <= ||t_i||^2/a <= (1/64)/a = 1/(31-8sqrt(2)) <0.051 <1/2`.  (5.7)

Therefore the projected-crossing theorem applies. In the absorption normalization, `c>1/2` and `|det B|>1/2`, so from (4.2), (5.5), and (5.6),

`||p_Q||_infinity
 < 9.4 [a^5 rho/8]^(-1/6)
 < 35.51 rho^(-1/6).`                                          (5.8)

This proves:

**QFORM-DIFFUSE-MIXED-SHEAR-PROJECTED-CROSSING-v1.** In the punctured heavy-hub mixed-shear state, if every normalized mixed leaf has leverage at most `1/64`, then the output has a bounded continuous density and

`boxed(||p_Q||_infinity <35.51 rho^(-1/6).)`                    (5.9)

The earlier direct leave-one-out estimate in this state was `12 rho^(-1/3)` under the weaker `ell_j<=1/2` gate. Thus (5.9) improves the singular exponent in the genuinely diffuse near-coloop regime from `1/3` to `1/6`; it does not remove the last `rho` loss.

## 6. Designated partner fleet02/B05 applied to an actual critical collar

The newest completed fleet02/B05 moving-slope theorem, canonical mathematics at

`yspennstate/math-open-problems@36d0dc0c4ac0910e8d84ae64d443136df86242d5`,

uses the near-null coordinates

`L=eta sqrt(rho) T+bV`,

and proves, for `|eta|<=1/2`,

`||p_(L,W)||_infinity <= 4/sqrt(3)`.                            (6.1)

Therefore for every centers `l_0,w_0` and every `r,s>0`,

`boxed(P(|L-l_0|<=r, |W-w_0|<=s) <= 16 r s/sqrt(3).)`           (6.2)

In particular a fixed doubly-critical collar of widths `sqrt(epsilon),sqrt(epsilon)` costs at most

`16 epsilon/sqrt(3)`.                                          (6.3)

This is the partner theorem spent at an actual small-ball inequality. What remains is not a fixed rectangular critical collar: after the indefinite two-sheet completion, the critical transverse center moves with the same-source coordinate `V`. Replacing this moving center by a supremum of conditional fibers is exactly one of the corrected invalid interfaces. Thus (6.2) pays the fixed collar and isolates the moving-center factor rather than merely restating a projection-density bound.

## 7. Precise first unpaid implication

The new identities show that the punctured heavy-hub obstruction is not absence of determinant currency:

- total physical three-scalar currency is exactly `c|det B|` by (2.3);
- for every admissible split, the projected-crossing currency is exactly (3.7);
- the newest crossing theorem spends this currency without touching arbitrary internal phases;
- in the diffuse branch MSS makes all gates quantitative, leaving only `rho^(-1/6)`.

The remaining factor is therefore

`QFORM-NEARCOLOOP-RHO-SIXTH-ROOT-RECOVERY-v1`:

> recover one factor `rho^(1/6)` in the near-coloop limit, or replace the projected-crossing receiver by a phase-sensitive one that uses the nonzero hub diagonal / moving two-sheet geometry before the longitudinal three-volume is paid. The estimate must preserve the original product-linear source and remain valid for fragmented rough laws; it may not use small-operator-error as small random error, arbitrary-joint coarea, conditional-density suprema, or pointwise quadratic-phase decay.

The exact coloop `rho=0` remains uniformly bounded from the preceding theorem, so the divergence in (5.9) is an interface loss, not evidence that the target density diverges.

## 8. Source and scope record

Fresh brain controls were read from current `main`; owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` keeps all workers on QFORM and explicitly preserves the correction that a frozen interval square-root slice estimate is not an arbitrary Borel-set profile. The full QFORM statement and full continuity statement remain OPEN.

Sources actually used:

1. preceding fleet01/B05 absorption theorem: `yspennstate/math-open-problems@118a74200ff58a869f7e4f81d93d5da45ecd7d8d`;
2. projected-crossing theorem: `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md` on current master (source file sha `c1bf1f2816e579069352848e04a32d4a22994096` when read);
3. MSS two-part frame theorem in the source-pinned QFORM ridge-window proof, where the exact `(1/sqrt(2)+sqrt(epsilon))^2` bound is recorded;
4. designated partner fleet02/B05 moving-slope report, canonical mathematics `36d0dc0c4ac0910e8d84ae64d443136df86242d5`.

No Gaussianity, log-concavity, moment, compact-support, connected-support, post-rotation independence, or diagonal-basis assumption is used in the new deductions. No full solution or counterexample is claimed.
