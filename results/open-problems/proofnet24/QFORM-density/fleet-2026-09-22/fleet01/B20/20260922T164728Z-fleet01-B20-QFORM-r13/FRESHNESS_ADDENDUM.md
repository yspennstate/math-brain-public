# Freshness addendum — revision 2026-09-22.8 conditional-projection bridge is false as stated

This addendum was written after the main `REPORT.md`, because fresh owner control advanced to revision `2026-09-22.8` during the same actual invocation. The sole target is unchanged and remains OPEN. The branch theorem in `REPORT.md` is unaffected.

Revision 8 proposes a rank-three coarea route whose stated final bridge is a universal bound on the conditional density of three selected spectral coordinates `(Y_1,Y_2,Y_3)` after conditioning on the remaining spectral coordinates. That conditional-density bridge is **false under the exact target assumptions**, even for iid unit-density uniforms. This does not refute QFORM; it refutes only the proposed conditioning step.

## Exact target-valid counterexample to the conditional-density bridge

Let `n=4` and let `X_1,...,X_4` be independent `Uniform[0,1]`, so every original-coordinate density is exactly one on its support. Put

`u=(1,1,1,1)/2`.

Choose any orthonormal basis `r_1,r_2,r_3` of `u^perp`, set `r_4=u`, and let `R=[r_1 r_2 r_3 r_4]` be orthogonal. Define spectral coordinates

`Y=R^T X`.

Then

`Y_4 = u^T X = (X_1+X_2+X_3+X_4)/2`.

The joint density of `Y` is simply the indicator of the rotated unit cube, because the change of variables is orthogonal. Hence for every regular value `w`, the conditional density of `(Y_1,Y_2,Y_3)` given `Y_4=w` is constant on the three-dimensional section of the rotated cube and equals the reciprocal of the marginal density `g(w)` of `Y_4`.

For `0<w<1/2`, write `S_4=X_1+X_2+X_3+X_4`. The Irwin--Hall density is

`f_{S_4}(s)=s^3/6`, `0<s<1`.

Since `Y_4=S_4/2`,

`g(w)=2 f_{S_4}(2w)=2(2w)^3/6=(8/3)w^3`.

Therefore

`boxed( ||p_{(Y_1,Y_2,Y_3)|Y_4=w}||_infinity = 1/g(w) = 3/(8w^3) )`

for `0<w<1/2`, and this diverges as `w downarrow 0`.

To place this exactly inside the spectral setup of QFORM, take

`A=R diag(1,1,-1,0) R^T`.

Then `A` has exactly three eigenvalues with modulus at least one. Conditioning on the remaining spectral coordinate `Y_4` is precisely the conditioning proposed by the revision-8 route, yet no universal conditional three-dimensional density cap exists.

Thus the implication

`original independent cap-one coordinates => uniformly bounded density of selected three spectral coordinates conditioned on the complementary spectral coordinates`

is false.

## Coarea caution

The unconditional three-dimensional projection density can be universally bounded in useful product-projection settings, but bounded joint density alone does not pay the indefinite rank-three quadratic trace without retaining more provenance. The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` (fleet01/B06, canonical `math-open-problems@cfb4137e221cd87aeb4f669389d14fa65e3251e7`) constructs thin two-sheet/hyperboloid-shell densities with bounded X-ray information and arbitrarily large indefinite quadratic pushforward density. That correction is not a QFORM counterexample because its three-dimensional density is not asserted to be an orthogonal marginal of a coordinate-product law; it shows exactly why product provenance cannot be discarded before the curved trace.

Therefore revision 8 should be interpreted as motivation for a **product-provenance rank-three trace theorem**, not as a completed conditional-coarea reduction. Any valid continuation must aggregate or exploit the original product law before or jointly with the indefinite rank-three coarea step.

## Status after freshness correction

The main report's new branch theorem remains valid: every diagonal-dominated localized second Schur row in the fleet02/B20 heavy first-pivot branch is closed, and a survivor must have a cross-dominated second row `||S_{j,-j}||>|S_jj|` with `||S_{j,-j}||>tau/9>=1/36`.

The full QFORM target remains OPEN. Continuity remains separate.
