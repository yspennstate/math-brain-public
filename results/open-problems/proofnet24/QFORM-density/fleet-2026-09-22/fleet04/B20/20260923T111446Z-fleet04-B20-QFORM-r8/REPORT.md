# fleet04 B20 — heavy-anchor deletion closure

Run: 20260923T111446Z-fleet04-B20-QFORM-r8

Status: ESSENTIAL_STEP_APPLIED; SUPPORTING BRANCH CLOSED; FULL QFORM OPEN.

## Source pins and correction gates

This note uses:

- Claude source baseline math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 and the later correction-safe fleet graph.
- fleet01/B20 at c45a270dbf4a4d81742bc934ff54eba97d81f4f3, especially QFORM-HEAVYROW-ANCHORED-MIXED-DISCRIMINANT-v1.
- fleet01/B18 at b42066397eb5ba83a885c6e700e0417a49a1d8ac, especially QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1.
- fleet01/B06 at 9838f01d705e379c6ff9b855bf1bb787d94b1c5c.
- the fleet04 correction-safe graph through c44df8e6d98a4e3832dc542eb42cfb4a25ddc257.

All conditioning remains on original physical coordinates. No independence after rotation is used. Aggregate minor energy is not replaced by a single selected large minor. No arbitrary-joint coarea or law-uniform scalar Fresnel decay is invoked.

## New theorem: QFORM-MODERATE-HEAVY-ANCHOR-DELETION-v1

Let A=R M R^T have exact rank three, with R^T R=I_3 and s_min(M)>=1. Let r_i denote the physical rows of R. Choose an anchor h and put

    z=r_h,    c=|z|^2.

Assume

    1/2 < c <= 3/4

and, for every i different from h,

    lambda_i := |r_i|^2 + (r_i dot z)^2/(1-c) <= 1/2.

For independent original coordinates with probability densities bounded by one, Q=X^T A X has a density satisfying

    ||p_Q||_infinity <= 3 e (1-c)^(-1/3)
                      <= 3 e 4^(1/3)
                      = 12.945010302125787...

The same assertion remains true after adding arbitrary affine terms to the conditional residual form.

### Proof

Delete the physical anchor row and form the 3 by (n-1) matrix B whose columns are the remaining rows r_i. Parseval gives

    G := B B^T = I_3 - z z^T.

Since c<1, G is positive definite and

    det G = 1-c.

Normalize the residual frame by

    W=G^(-1/2) B,    D=G^(1/2) M G^(1/2).

Then W W^T=I_3 and

    B^T M B = W^T D W,
    |det D| = (1-c)|det M| >= 1-c.

The leverage of residual coordinate i in this normalized Parseval frame is

    |G^(-1/2) r_i|^2 = r_i^T G^(-1) r_i.

Sherman-Morrison gives G^(-1)=I_3+z z^T/(1-c), hence this leverage equals lambda_i above.

Condition on the original physical coordinate X_h=x. The remaining coordinates are still independent cap-one variables. The conditional form is

    X_res^T B^T M B X_res
      + 2 x z^T M B X_res
      + x^2 z^T M z.

Thus its quadratic part is W^T D W and the other terms are affine or constant in the residual variables. The capped-basis Fresnel theorem from fleet01/B18 applies uniformly in x: the complete determinant-squared basis law of W has score one and coordinate marginals lambda_i<=1/2. Translation of each one-dimensional Fourier argument shows that the same estimate holds with the affine term. Therefore

    ||p_(Q | X_h=x)||_infinity
       <= 3 e |det D|^(-1/3)
       <= 3 e (1-c)^(-1/3).

Mixing in the physical variable X_h preserves this cap. The final numerical inequality uses 1-c>=1/4. This proves the theorem.

## Exact residual obstruction exposed

Fleet01/B20 proves that every exact-rank-three heavy-row survivor has some c>1/2 and anchored aggregate physical minor mass c. The deletion normalization shows that the moderate-heavy portion is now closed unless one of two explicit events occurs:

1. extreme anchor: c>3/4; or
2. second normalized heavy coordinate: for some i different from h,

       |r_i|^2 + (r_i dot r_h)^2/(1-|r_h|^2) > 1/2.

The formula is exact. In particular, failure is not merely “mixed rows”: it is a quantitatively heavy coordinate after deleting and whitening the anchor. The endpoint c=1 has rank-two residual Gram and belongs to the coloop ruled/convex split; it cannot be obtained by taking a limit in this theorem.

## Compact noncircular proof graph

1. Claude D-prime, D5 and sharp Hausdorff-Young estimates are usable only with their marginal gates and endpoint factors retained.
2. The fleet01/B18 capped-basis theorem closes rank-three Parseval cores carrying a determinant-basis law with all marginals at most one half and positive score.
3. The diffuse exact-rank-three Schur core is covered by the previously published full-basis cap.
4. fleet01/B20 supplies an anchored aggregate determinant identity in every heavy-row survivor, but not a density estimate and not a single large minor.
5. The new deletion theorem above closes the moderate heavy anchor whenever the whitened residual frame is diffuse, with universal cap below 12.946.
6. fleet01/B06 and the fleet04 three-bank mixed-Fresnel result cover the non-near-null one-sided heavy-hub alternatives in their stated scopes.
7. Ruled/Plucker and orientation-free rank-two estimates pay only their one-sheet or rank-two scopes.
8. Leakage-free double-star, convex-chain, and square-hyperbola theorems pay their explicit endpoint models but do not absorb arbitrary same-bank quadratic leakage.

No step transfers independence through an orthogonal change of variables, and no scoped endpoint result is promoted to the full theorem.

## Remaining first unproved implications

The full conjecture remains open. The live gaps are:

- the extreme-anchor or second-normalized-heavy-coordinate compound, especially with same-bank quadratic leakage;
- the punctured convex/two-sheet near-null collar;
- arbitrary additional spectrum interacting with the selected three-dimensional spectral core.

The next useful receiver must integrate the anchor and the newly exposed second heavy coordinate before taking a worst conditional-density supremum. It must also retain the fleet01/B20 aggregate anchored determinant mass rather than select one minor.

There is no full end-to-end candidate here, so two end-to-end review requests would be premature. Continuity is not claimed beyond branches whose cited theorems prove it.
