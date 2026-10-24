SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-22T19:26:41Z.
attacking: replace single-minor inversion by a projection-Plancherel payment for an entire rectangular coordinate-minor bank.

# account01/B07 handoff — rectangular coordinate-minor bank payment

Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`. Execution remains `WITHOUT_VERIFIED_BRAIN`.

Fresh pre-publication control was `yspennstate/math-research-brain@1fbdb5a35599eecac8fca5ea351df896aad3b319`, OWNER CONTROL revision `2026-09-22.14`. A later final refresh reached `5911d85bd4183e123e8a6464a1a6ea536378ff36`, revision `2026-09-22.15`; there is no stop and QFORM remains the sole target. Revision `.15` promotes joint integrated characteristic-function estimates, which is exactly the mechanism of the theorem below. The consolidated `CURRENT_RESEARCH.md` still keeps the arbitrary-joint rank-three coarea claim refuted, and this run does not use it.

Canonical immutable mathematics: `yspennstate/math-open-problems@dad41d7b7fbcd294cc180cfba6ed989d0b841a59`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/a01-b07-20260922T192641Z-qform-coordinate-minors/REPORT.md`. Final-control addendum: `yspennstate/math-open-problems@699efe68f22348f9bc79f1c3ff01b8ea8dc61dd2`, same run directory, `CONTROL15_ADDENDUM.md`.

Assigned partner actually consumed and applied: account02/B07 `QFORM-DISJOINT-CROSS-PLANCHEREL-v1`, canonical `yspennstate/math-open-problems@dbf85b8f59fcbb22d4599b7cba9edd97d9ffa83f`. I combined its conditional `L^2` Plancherel mechanism with account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.

New theorem `QFORM-PROJECTION-CROSS-PLANCHEREL-v1`: for disjoint physical coordinate banks `I,J`, if `C=A[I,J]` has exact rank `r>=3` and `Delta_r(C)=pdet(CC^T)`, then the FULL quadratic form, with arbitrary self blocks, outside couplings, affine terms, signs and extra spectrum, has a continuous density satisfying

`||p_Q||_infinity <= e [r/(r-2)] Delta_r(C)^(-1/(2r)).`

If one side has exactly `r` coordinates, the factor `e` improves to `sqrt(e)`; if both sides have exactly `r`, it improves to `1` and recovers the partner theorem exactly.

Coordinate-minor consequence: for a fixed physical row triple `I` and any disjoint column bank `J`,

`Delta_I(J)=det(A[I,J]A[I,J]^T)=sum_{K subset J, |K|=3} det A[I,K]^2`,

and if `Delta_I(J)>0`,

`||p_Q||_infinity <= 3 sqrt(e) Delta_I(J)^(-1/6).`

Thus the whole column-minor bank is aggregated before reciprocal payment; no column triple is selected. More generally, for any physical cut whose cross block has rank exactly three,

`||p_Q||_infinity <= 3 e E_3(A[S,S^c])^(-1/6)`

with no coordinate-leverage hypothesis.

Actual determinant-weight application: my earlier exact-rank-three Pluecker identity, derived from the designated account02/B07 disjoint-basis invariant, gives a cut with

`E_3 >= |det Lambda|^2 delta/64`.

The old `q=1` determinant route additionally needed a leverage-good cut. The new theorem removes that gate and yields directly

`||p_Q||_infinity <= 6e |det Lambda|^(-1/3) delta^(-1/6)`.

At `delta>=1/8`, `|det Lambda|>=1`, this is `<23.066`; continuity is proved on this branch. The six-coordinate paired-frame stress case that defeated every `q=1` leverage cut is paid directly; its balanced `3x3` cross block gives the sharper bound `<=6`.

First unpaid implication: `QFORM-ROW-PACKET-PROJECTION-PAYMENT-v1`. The column dispersion is now completely paid once a physical row triple is fixed. What remains is to turn the existing finite-heavy/third-compound determinant-weighted FAMILY of row triples into either one triple with constant full rectangular Gram determinant, or a genuine mixture-level projection/Plancherel inequality that sums row-triple weights before inversion. For high-rank cross blocks one cannot simply replace the full pseudodeterminant by `E_3`; the residual two-sided cross phase must be routed rather than dropped.

Full QFORM remains OPEN. Full continuity remains OPEN; continuity is established for the scoped projection-cross branches above.
