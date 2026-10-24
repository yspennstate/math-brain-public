# account01/B08 MOC4 handoff — exact refutation of the universal 24-state Bogoliubov lift

Run: `20260922T024227Z-account01-B08-MOC4-r12`  
Outcome: **CANDIDATE_REFUTED**; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Named OTHER-account result consumed

Assigned partner **account02/B09**, run `20260922T014320Z-account02-B09-MOC4-r12`, `MOC4-PARITY-EXCESS` / surviving `MOC4-MAXIMIZER-SIX-WITNESS-v1`. Its exact six-fiber compression and pair-maximizer conclusion are applied here: once an unconditional common-unitary positive lift is eliminated, any surviving proof must use the structured weights and maximizer-local row/column pair conditions rather than another coefficient-free lift.

Also consumed the newest complete representation-theoretic result **account04/B07 `MOC4-ODD-WEYL-ORIENTATION-v1`**, which proves `sum sqrt(q_selected)<=2` for every odd signed matching of an actual `SO(6)` exterior-square point.

## New exact counterexample

Test the strongest remaining unconditional representation:

`MOC4-BOGOLIUBOV-EVEN-LIFT-v1`: for every actual unitary, its Bogoliubov mass array `(q+,q-)` lies in the convex hull of the 24 even coloured matching / `S4` endpoint arrays.

This would imply MOC4 support immediately because the exact support objective is linear in `(q+,q-)`. It is false.

For `R=q++q-` and `D=q+-q-`, every 24-state even endpoint satisfies the exact facet

`Phi = R11-R12+3D13+3D21+R22-R23-R31-3D32+R33 <= 3`.

Exact endpoint enumeration gives only values `3,-3,-9`. The even polytope has affine dimension 13; exactly 13 vertices are tight and have affine rank 12, so this is a genuine facet.

For the exact real orthogonal matrix

```
[  636/1105,  -423/1105,   -12/65,   -772/1105 ]
[ 3576/5525,    332/5525, -144/325,  3411/5525 ]
[   164/425,     348/425,      9/25,    -96/425 ]
[      27/85,       -36/85,       4/5,       24/85 ]
```

one has exactly `U^T U=I`, `det U=1`, all 16 entries nonzero, and all 36 two-by-two minors nonzero. In the complementary-pair basis `(12,34 | 13,-24 | 14,23)`, form `O=Lambda^2 U` and the account04/B07 Bogoliubov masses. Exact rational arithmetic gives

`Phi(actual q)=2403485709/763140625`,

hence

`Phi(actual q)-3 = 114063834/763140625 > 0`.

Therefore this actual strict true-unitary `(q+,q-)` is outside the convex hull of the 24 even endpoint arrays. No universal probability law on those 24 states can reproduce these masses.

This is **not** an MOC4 counterexample; it refutes only the universal positive lift. Since the datum is an actual `SO(6)` point, account04/B07's odd-Weyl overlap theorem still applies. Thus that overlap constraint is necessary but does not characterize the 24-state hull.

## Next shared implication

`MOC4-STATIONARY-FACET-PAYMENT-v1`: at a global maximizer for a structured spectral support pair `(K,X)`, use full block orthogonality plus the account02/B09 twelve row/column pair-optimality conditions / account01/B07 Spin(6) stationarity balances to prove the structured objective cannot profit from outward even-lift facet directions, even though arbitrary actual unitaries can violate those facets.

Do not return to an unconditional common positive lift, parity roof, or orientation-forgetting 48-state relaxation.

## Exact scientific delivery

Private scientific repository: `yspennstate/math-open-problems`  
Path: `proofnet24/collective-MOC4/account01/B08/20260922T024227Z-account01-B08-MOC4-r12/`  
Report commit: `e624fbd2f4f8e05b2fa780fbc3a5829b3a87e3ba`  
Verifier: `verify_even_lift_facet.py`  
Captured exact output: `VERIFICATION.txt`.
