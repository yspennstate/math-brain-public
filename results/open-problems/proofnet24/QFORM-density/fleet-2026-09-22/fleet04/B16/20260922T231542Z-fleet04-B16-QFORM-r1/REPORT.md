# QFORM-RULED-PLUECKER-ENDPOINT-v1

Classification: `ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN`  
Continuity: not asserted by the new one-sided argument; continuity is available in the partner cross-cut branch.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Target and source pins

The target is the law of `Q=X^TAX` for arbitrary independent real coordinates with densities at most one, when `A` has at least three eigenvalues of modulus at least one.  No moment, support, log-concavity, or post-rotation independence hypothesis is imposed.

The new geometric input is Claude's ruled-level-set theorem in `yspennstate/math-open-problems`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb`, read on `master` after the required baseline `e5f71d79eff325201dd0274053d20268ce65b837`.  The product-preserving cross-cut input is fleet01/B16's `QFORM-PLUCKER-DISJOINT-CUT-v1`, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260922T223900Z-qform-b16-r11/REPORT.md` (report blob `8b36df2db3e1af9f2534b995de54059d485fb30d`).

## Theorem

Assume first that the *entire* matrix has exact rank three,

`A=R Lambda R^T`, `R^T R=I_3`,

and that the eigenvalues of `Lambda` are `lambda_1,lambda_2,-mu`, where `lambda_1,lambda_2,mu>=1`.  Let

`w_S=det(R_S)^2`, `|S|=3`,

and, for independent triples `S,T` with law `w`, put `d=P(S cap T=emptyset)`.

Then:

1. On the one-sheet (majority-sign) side,

   `ess sup_{s>=0} p_Q(s) <= pi sqrt(2)`.

2. If `d>0`, the partner cross-cut theorem gives the full two-sided estimate

   `||p_Q||_infinity <= 12 |det Lambda|^(-1/3)d^(-1/6) <= 12d^(-1/6)`.

3. If `d=0`, the only endpoint not already paid by the finite-line alternatives in the partner report is a leverage-one coloop plus a rank-two spectral plane.  In that endpoint the one-sheet side is still bounded by `pi sqrt(2)`.  Hence the exact remaining analytic debt is only the two-sheet/convex side of the null or near-null coloop model.

The sign-reversed statement holds for signature `(1,2)`: the ruled bound is on `s<=0`.

## Proof of the ruled bound with product provenance

Let `Y=R^T X` and let `rho` be its three-dimensional density.  This notation does not assert that the coordinates of `Y` are independent.  The ruled proof uses only line integrals of `rho`, and each such line integral is a two-dimensional marginal of the *original product measure*.

After scaling the spectral variables, a positive level of

`q(y)=lambda_1 y_1^2+lambda_2 y_2^2-mu y_3^2`

is a one-sheet hyperboloid.  One ruling gives a parametrization by `(theta,t)`.  The exact coarea identity from the Claude source is

`d sigma/|grad q|=(1/2)d theta dt`.

For each fixed `theta`, integration in `t` is a line integral of `rho`.  The orthogonal complement of that line is a two-dimensional linear image of the original independent coordinates.  The sharp product projection theorem used in the source bounds the corresponding two-dimensional marginal density by `2` after the appropriate Jacobian normalization.  Keeping the spectral scaling yields

`p_Q(s) <= (lambda_1 lambda_2 mu)^(-1/2)
 integral_0^(2pi) [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2)d theta`.

The source's elementary estimate of this integral is `pi sqrt(2)` when all three moduli are at least one.  This proves item 1 without a fiber supremum, without an arbitrary-joint coarea bound, and without independence of the spectral coordinates.

## Actual application of fleet01/B16

For a random original-coordinate bipartition `I union J`, fleet01/B16 proves

`E Delta_3(A_[I,J])^2=|det Lambda|^2 d/64`.

Thus some cut obeys

`Delta_3(A_[I,J])>=|det Lambda|sqrt(d)/8`.

Its completed product-preserving cross-bank theorem applies to the *same original-coordinate cut* and gives

`||p_Q||_infinity
 <=6 Delta_3(A_[I,J])^(-1/3)
 <=12 |det Lambda|^(-1/3)d^(-1/6)`.

This is an equation-level use of the designated partner result, not a projection-density substitution.

When `d=0`, the partner's matroid reduction has three cases.  Rank-zero and rank-one obstructions are compressed into finitely many spectral line banks and are already bounded there.  Rank two forces a coloop row of leverage one and all remaining rows into its orthogonal spectral plane.  The ruled estimate above does not require `d>0`, so it pays the entire one-sheet side even in this endpoint.  It does not pay the opposite two-sheet side.

## Why this does not finish the conjecture

The argument is exact-rank-three.  Additional spectrum cannot be discarded: it changes the same physical cross block and the same level sets.  Even in exact rank three, the null/near-null coloop's convex side remains unpaid.  An arbitrary bounded joint density on the three-dimensional projection is insufficient, and the live corrections rule out worst conditional-density suprema and one-star half-Riesz shortcuts.

The next precise implication is therefore:

`QFORM-NULL-COLOOP-CONVEX-SIDE-v1`: bound the two-sheet side of

`aX_0^2+2X_0 L(Y)+q_2(Y)`

uniformly as `a -> 0`, where `X_0` is an original cap-one coordinate, `Y` is the two-dimensional projection of the remaining original product source, and the full three-dimensional spectral matrix has determinant modulus at least one.

No counterexample is supplied, and the full theorem remains open.
