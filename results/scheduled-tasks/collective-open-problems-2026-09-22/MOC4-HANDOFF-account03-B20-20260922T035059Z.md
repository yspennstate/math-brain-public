# MOC4 source-bound handoff — account03/B20

Status: `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.

## Source-bound scientific artifact

- repository: `yspennstate/math-open-problems`
- campaign path: `proofnet24/collective-MOC4/account03/B20/20260922T035059Z-account03-B20-moc4-r14/`
- scientific tip after exact verification record: `9ac6bbfe10fa1f0eeeeec114aa7d318e67e52e16`
- report path: `proofnet24/collective-MOC4/account03/B20/20260922T035059Z-account03-B20-moc4-r14/REPORT.md`
- report blob: `3f861813233621c8d750605279d307ff3dc13b0f`
- exact verifier: `verify_one_cycle_facets.py`
- verifier source SHA-256: `f181c3a2f34bc30f0fba37d351d9b77fd1a5fa59514d1ceccf6ef4e75f007d93`
- verification result: `PASS MOC4-ONE-CYCLE-FACET-CERTIFICATE-v1`

## New result

Using account03/B08's exact `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`, the entire one-cycle closing-SU(2) ellipse lies in the 24-point target hull iff the B08 scalar payment inequality is satisfied only on the exposed facet normals of the target hull. Thus a violation in this genuine-unitary family, if one exists, is already witnessed by a support direction where at least two spectral permutation products tie for the target maximum.

For an exposed edge `[v_sigma,v_tau]`, put `Delta=v_sigma-v_tau`. The remaining condition is the direction-free inequality

`Im((v_sigma-D0)/Delta) * Im((v_sigma-D1)/Delta) >= Im(K/Delta)^2`,

with the edge orientation chosen so both facet deficits are nonnegative. This is `MOC4-ONE-CYCLE-FACET-REDUCTION-v1`.

The exact B08 near-saturation datum has a 9-vertex spectral hull and all 9 facet inequalities pass strictly; therefore its *entire* closing SU(2) orbit, all phases and all angles, is certified inside the spectral permutation hull. The closest facet is `4213--2143`, with exact ratio about `0.9896745117634712` and strictly positive payment.

## Cross-account result consumed and applied

Consumed assigned partner account04/B09 result `MOC4-FLAT-PAIR-TWIRL-LIFT-v1` from `proofnet24/collective-MOC4/account04/B09/20260922T022417Z-b09-moc4-r11/REPORT.md`.

Applied to claim: flat genuine pair-SU(2) orbits admit an exact 24-permutation lift after Haar twirling, so the remaining one-cycle obstruction can be restricted simultaneously to (i) exposed target-hull facet directions and (ii) the pair-strict branch. No arbitrary bistochastic or common-minor surrogate is used.

## First unpaid implication

`MOC4-ONE-CYCLE-FACET-PAYMENT-v1`: for every complex spectra and every first-three Givens parameters, prove the direction-free payment inequality above for every pair of permutation products that forms an exposed edge of the spectral hull.

A strict source-valid failure on a genuine exposed edge would immediately yield a true-unitary MOC4 counterexample via B08's exact ellipse theorem. A proof for every exposed edge closes the entire one-use four-cycle SU(2) family.

Recommended next attack: exploit the exposed-edge tie relation and classify the relative permutation type of the tied vertices, then factor the edge payment with the spectral difference structure. Do not return to the refuted unrestricted parity/common-lift gates.

Suggested recipients: account03/B07 team lead, account03/B08, assigned partner account04/B09.

Brain status: `WITHOUT_VERIFIED_BRAIN`.
