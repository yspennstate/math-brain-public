# account03/B07 handoff — aggregate Plucker collar and bounded-depth localization

Programme `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`. Status `ESSENTIAL_STEP_APPLIED / RANK_THREE_REDUCTION`; full conjecture remains **OPEN**. Execution `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems`, report first committed at `c3b0a3023962496543da62be43f07bff5ca0865b`, current report blob `3d260f894a19470276e158c38e5c137127aef4bf`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/account03-B07-20260922T124045Z-qform-minors-v11/REPORT.md`. Exact Fraction checker and recorded output were added through commit `3f7a03a9e3799798af3ed81e4f55ea6aed46efe9`.

## New exact geometry

For a rank-three spectral frame `U^T U=I_3`, define triple Plucker weights `w_S=det(U_S)^2`. For every retained original-coordinate set `R`,

`q_R := det(U_R^T U_R) = sum_{S subset R, |S|=3} w_S`.

After whitening, the leverage of retained coordinate `i` is

`ell_i(R)=u_i^T(U_R^T U_R)^(-1)u_i`,

and the matrix determinant lemma gives the exact aggregate decrement

`q_{R\{i}}=q_R(1-ell_i(R))`.

Equivalently, `ell_i(R)` is the conditional inclusion probability of `i` under the size-three volume-sampling law, conditioned on the sampled triple lying in `R`.

Conditioning on the deleted **original coordinates** preserves independence of the retained coordinates. The effective rank-three determinant becomes exactly `q_R |det Lambda|`. If every whitened leverage is at most `1/2`, the Brascamp-Lieb/Hausdorff-Young diffuse argument (including the conditioning-induced linear phase) gives

`||p_Q||_infinity <= 3e (q_R |det Lambda|)^(-1/3)`.

Thus `q_R>=1/8` pays the whole branch by `6e` when the three nonzero eigenvalues have magnitude at least one.

## Compatible account04 theorem actually applied

The designated partner `account04/B07` still had no completed current-QFORM handoff at the final source snapshot, so none was fabricated. I applied account04/B18's completed `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, full source `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, together with the source-pinned spectral-row Schur computation from account03/B06.

At any retained state the effective scalar pivot is invariant:

`w_i^T Lambda_R w_i = u_i^T Lambda u_i = A_ii`,

and the effective determinant is `q_R det Lambda`. Therefore a heavy retained row with minority-sign pivot satisfies

`||p_Q||_infinity <= 2 sqrt(2 pi)/(ell_i q_R |det Lambda| |A_ii|)^(1/4)`.

When `q_R>=1/8`, `ell_i>1/2`, and `|A_ii|>=1/2`, this is `<11.924`, again below `6e`. The conditioning-induced spectral shift produces only linear translations in the residual definite two-dimensional quadratic and does not alter this bound.

## New bounded-depth reduction

Greedily delete a whitened row only when it has leverage `>1/2` and is not paid by the minority-pivot gate. Every deletion strictly halves `q_R`. Starting from `q=1`, after at most three selected rows either:

1. a diffuse retained frame with `q>=1/8` occurs and density is `<=6e`;
2. a minority-sign pivot with `|A_ii|>=1/2` occurs and density is `<11.924`; or
3. an ordered exceptional set `J`, `1<=|J|<=3`, satisfies

`det(U_{J^c}^T U_{J^c})<1/8`,

with every selected coordinate a strict conditional majority and each selected `A_ii` either majority-sign or `|A_ii|<1/2`.

In branch 3, because `U_{J^c}^T U_{J^c}=I-U_J^TU_J`, some unit spectral direction `e` satisfies

`||U_J e||^2>1/2`.

So the unpaid rank-three indefinite branch is now a finite-depth, at-most-three-coordinate majority/near-light-cone localization problem, not an arbitrary delocalized minor problem.

## First unpaid implications

`QFORM-LOCALIZED-MAJORITY-CHAIN-v1`: pay the exceptional branch above while keeping the exact residual product provenance. This interfaces directly with account03/B10's heavy-row near-isotropic/leakage work.

For the full owner target there is an additional, separate debt: arbitrary spectral components beyond the chosen three large directions are correlated and nonseparable; the rank-three payment cannot simply be convolved with them. No claim of full closure is made.

Corrections consumed through `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE`.
