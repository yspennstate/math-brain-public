# MOC4 handoff — account04/B09 `MOC4-ROOT-SATURATION-EXCLUSION-v1`

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account04/B09/20260922T060924Z-b09-moc4-r12/REPORT.md`, report commit `cf16df018edc33d522789a14bf924a0257e83110`. Exact root-identification verifier commit `4cc6095bf9e9260c154d4a5f8acdb308ded0bcf6`; captured exact output commit `a02f441640888ef6376bd69ae27e2fb51309ad3c`.

## Named other-account result applied

Applied account01/B07 `MOC4-BIORIENTATION-PAIR-GATE-v1`, scientific report commit `a643a4e465e4f0243a961c10cad73aeb60089be2`, together with its later exact Spin(6) stationarity balances in coordination commit `06b94d9eccff5122288e51bd1992eeb42a84f975`.

For each block-row or block-column pair the pair gate has exact endpoint losses `T-epsilon C`, `epsilon=+-1`. The new result identifies those two endpoints with the two complementary elementary `SU(2)` roots of `SU(4)`. In the grouped wedge basis `(12,34)|(13,24)|(14,23)`, exact calculation gives complementary original roots acting on the same block-plane pair with opposite `det Z`.

## New theorem

At a genuine support-violating **global** maximizer every pair gate is strict:

`T^L_ag > |C^L_ag|` for all three block-row pairs and `T^R_bd > |C^R_bd|` for all three block-column pairs.

Proof: if `T=|C|`, choose `epsilon` with `T-epsilon C=0`. The account01/B07 endpoint formula gives an equal-support elementary root endpoint. That root differs from the ordinary coordinate pair swap only by a diagonal phase gauge. Account04/B08 `MOC4-PAIR-FLAT-BOUNDARY-v1` then upgrades the tie at a global maximizer to complete flatness of the genuine embedded `SU(2)` pair orbit. Account04/B09 `MOC4-FLAT-PAIR-TWIRL-LIFT-v1` Haar-averages that orbit to an exact probability mixture of the 24 permutation squared-minor vectors, forcing the support to be at most the maximum permutation-product support. This contradicts violation. The column argument is symmetric.

No simple-spectrum, invertibility, nonzero-minor or genericity assumption enters this saturation exclusion.

## Consequence for the lead tree

The latest lead tree (`e8eaccf8e3393ae7a5b75f12310d54ef92c15775`) treated `MOC4-FLAT-PAIR-MIXED-RIGIDITY-v1` as the first unpaid branch after the new mixed Hessian theorem (`f81667d2ddb67bfa45c96cae39320b078c3e4c4c`). That branch is unnecessary for target closure: a violating global maximizer cannot satisfy `T=|C|` at all. The lead's equality-induced Gram-collinearity remains mathematically valid but is not needed to classify a counterexample maximizer.

The first remaining universal implication is therefore the **strict interior** problem `MOC4-STRICT-SPIN6-SIX-WITNESS-v2`: prove the six-fiber support inequality for a genuine `Lambda^2 U` global maximizer satisfying complete left/right stationarity, all strict bi-orientation gates, all mixed-Hessian inequalities, all 24 subgroup roofs, and the exact same-unitary `P/R/D` identities. No claim is made that this strict branch is solved.
