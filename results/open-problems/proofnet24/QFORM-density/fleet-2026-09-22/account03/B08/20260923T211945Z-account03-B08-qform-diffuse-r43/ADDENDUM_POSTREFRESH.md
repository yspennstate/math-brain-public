# Post-refresh addendum — rank-free first-compound source collapses the r45 edge/tail debt

A source-matching stronger theorem landed on `master` after the initial B08 report was written:

`yspennstate/math-open-problems@5d4cd3fcb9976deebd0cb409ebcca9cfb29cb9ba`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T212739Z-account01-B04-QFORM-auto11-r20/REPORT.md`

Its `QFORM-INDEFINITE-PAIR-FIRSTCOMPOUND-RANKFREE-v1` proves, for an invertible indefinite original physical pair `B` with

`D=|det B|`, `kappa=sigma_min(B)`,

and an exact pair-Schur residual containing two disjoint original-coordinate banks whose full cross block is `N`,

`||p_Q||_infinity
 <= C_* (D kappa)^(-1/4) ||N||_F^(-1/4),
 C_*<15.829,`                                                     (A.1)

with arbitrary same-bank quadratic-affine terms and **no rank assumption on `N`**.  Equivalently its source notation is `Z_1=||N||_F^2` and the factor is `Z_1^(-1/8)`.  This source strictly dominates this run's rank-one-crossing theorem on the overlapping scope.  I therefore stop duplicate work on the rank-one-only analytic receiver and apply the stronger theorem to the actual B08 r45 common-plane/tail state.

## A.1 Exact Pythagorean first-compound identity in the r45 state

Use r45 notation.  The two full-row-rank physical hub-to-bank arms are

`M_1 in R^(2 x m_1)`, `M_2 in R^(2 x m_2)`.

Let `P_r` be the orthogonal projection onto `row(M_r)` in the corresponding light bank.  The pre-completion light-light crossing is decomposed exactly as

`C = M_1^T R_c M_2 + T`,
`P_1 T P_2=0`.                                                    (A.2)

For an invertible physical hub pair `B`, exact pair-Schur completion gives

`N=C_B=M_1^T J M_2+T`,
`J=R_c-B^(-1)`.                                                   (A.3)

The common-plane term belongs to the `P_1-P_2` matrix corner, while `T` has zero component in that corner.  Hence they are Frobenius-orthogonal:

`<M_1^T J M_2,T>_F
 =<M_1^T J M_2,P_1 T P_2>_F=0`.                                  (A.4)

Therefore

`boxed:
 ||N||_F^2
 =||M_1^T J M_2||_F^2+||T||_F^2.}`                              (A.5)

There is no cancellation, regardless of the rank or sign pattern of `J` or `T`.

Put

`beta_r=sigma_2(M_r)>0`, `r=1,2`.                               (A.6)

The linear map `J -> M_1^T J M_2` has least singular value at least `beta_1 beta_2` in Frobenius norm (vectorize, or use the two SVDs).  Thus

`||M_1^T J M_2||_F
 >= beta_1 beta_2 ||J||_F`,                                        (A.7)

and (A.5) yields

`boxed:
 ||N||_F^2
 >= beta_1^2 beta_2^2 ||J||_F^2+||T||_F^2.}`                    (A.8)

## A.2 Rank-free r45 payment

Insert (A.8) into the new account01/B04 theorem (A.1).  Every r45 branch with `N!=0` satisfies

`boxed:
 ||p_Q||_infinity
 <15.829 (D kappa)^(-1/4)
 [beta_1^2 beta_2^2 ||R_c-B^(-1)||_F^2+||T||_F^2]^(-1/8).}`      (A.9)

This is an essential-supremum density bound; continuity is not claimed by the source theorem.

At target scale, if

`kappa>=tau L`

and

`sqrt(beta_1^2 beta_2^2 ||R_c-B^(-1)||_F^2+||T||_F^2)
 >= xi L`,                                                       (A.10)

then `D>=kappa^2` and

`boxed:
 ||p_Q||_infinity
 <15.829 tau^(-3/4) xi^(-1/4) L^(-1).}`                         (A.11)

The crucial structural consequence is exact.  Because both arms have full row rank, (A.5) implies

`N=0  <=>  J=0 and T=0
      <=>  R_c=B^(-1) and T=0`.                                 (A.12)

Thus for an invertible indefinite physical hub pair, the entire r45 **nonzero common-plane mismatch OR nonzero transverse tail** debt is now paid without any rank assumption.  The only zero-first-compound survivor is the exact Schur-match / zero-tail state (A.12), where the target's genuine third curvature must lie in the retained same-bank Schur remainder.

## A.3 Relation to the initial rank-one result of this run

The initial theorem in `REPORT.md` independently derived the special case `rank(N)=1`, with constant `15.083` and singular-value currency.  It remains mathematically valid, but the new source (A.1) is broader and is the preferred fleet handoff.  Per owner instruction, the source-matching theorem ends duplicate work on the rank-one-only scope.

The designated account04/B08 theorem remains an actual complementary inequality:

`||p_(L X_0^2+2LRU_1V_1+2LR^(-1)U_2V_2)||_infinity<7.251/L`,

uniformly for `R>=3`.  It pays an extreme fixed-`E_2` anisotropic endpoint where least-singular-value currencies can degenerate.

## A.4 New remaining B08 debt

After the post-refresh source is consumed, the sharpened debt is:

`QFORM-R45-EXACT-SCHUR-MATCH-ZEROTAIL-THIRD-CURVATURE-RECEIVER-v1`.

Namely, in the common-plane state with invertible indefinite physical pair, one only still needs the exact configuration

`R_c=B^(-1)`, `T=0`,                                              (A.13)

while retaining arbitrary same-bank Schur curvature.  A full target proof must show that the third large eigenvalue forces a product-preserving payable third-curvature mechanism there.  Singular/near-singular physical hub pairs remain a separate debt.  Full QFORM and global continuity remain OPEN.
