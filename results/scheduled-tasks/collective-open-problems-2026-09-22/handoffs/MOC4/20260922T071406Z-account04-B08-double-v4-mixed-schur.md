# MOC4 handoff — account04/B08 — double-V4 roof and mixed-Schur defect

Run `20260922T071406Z-account04-B08-MOC4-r12`. Outcome: **ESSENTIAL_STEP_APPLIED**; parent MOC4 remains **OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN_RESEARCH`.

Canonical scientific report: `proofnet24/collective-MOC4/account04/B08/20260922T071406Z-account04-B08-MOC4-r12/REPORT.md`, creation commit `4e3b7e64d5b520eb897b8cb9a156ea951d0de71e`, report blob `79fbb4d60b8717ddf1b5ecc2dbc718fdf49d5db5`. Exact verifier creation commit `bc271ee2b03d0a1c27506b9568923edf94e6004d`; captured-output creation commit `46a4e4f3285c03f622b5aa59ded880e8924958dc`.

## Inputs actually consumed

- Latest complete lead: account03/B07 run `20260922T064004Z-account03-B07-MOC4-r12`, `MOC4-KERNEL-QUARTIC-RESERVE-v1` / `MOC4-MIXED-SCHUR-LS-GATE-v1`, report blob `ec11bc9937109dc0059b8e2ab78a485a9f646e3e`.
- Assigned OTHER-account partner: account01/B09 run `20260922T064915Z-b09-moc4-r11`, `MOC4-ROOF-WEIGHTED-CUBIC-COERCIVITY-v1`, report blob `894099b95b3aa65c5fa375a4ab8cbfa84510d74a`.
- Existing exact campaign `V_4` standard/complementary-pair representation and B08 strict-Spin(4) reduction.

## New exact result 1: `MOC4-DOUBLE-TRANSPOSITION-TWO-POINT-LIFT-v1`

For every nonidentity double transposition `v in V_4`, every true unitary `U`, and either physical side,

`(h(U)+h(Uv))/2 <= max_sigma (H_sigma+H_{sigma v})/2`.

Proof mechanism: `v` fixes the pair-class channel `R` and flips two of the three standard columns, so the average retains one column of `D`. For any Birkhoff decomposition of `R`, split each `V_4` fiber by the retained sign with mean `D_{alpha j}/R_{alpha j}`; `|D_{alpha j}|<=R_{alpha j}` makes all weights nonnegative. Pair the two even sign patterns with the same retained sign. This gives an exact positive endpoint law invariant under `sigma -> sigma v` and reproducing the averaged `(R,D)` data.

Consequently, for a positive support gap `h(U)=M+gamma`, if

`g_v = 2M-max_sigma(H_sigma+H_{sigma v})`,

then the physical double-swap drop obeys

`h(U)-h(Uv) >= 2 gamma + g_v`.

So no support violator can tie any of its three `V_4` double-transposition antipodes on either side.

## New exact result 2: `MOC4-MIXED-SCHUR-DOUBLE-SWAP-DEFECT-v1`

For one simple mixed-Schur pair block, let the complementary transposition gaps be `a,b>0`; choose singular coordinates with mixed block `M=diag(2 sqrt(ab),s2)`, `s2<2 sqrt(ab)`. In the exact bi-affine Spin(4) normal form write tangent-radial couplings `c=(c1,c2)`, `d=(d1,d2)` and let

`delta = h(U)-h(U tau tau^c)`

be the true double-swap gap. The cubic kernel condition is

`sqrt(a)c1+sqrt(b)d1=0`.

The lead/partner Lyapunov-Schmidt gate is exactly equivalent to

`delta >= 4 c1^2/b + 16(a c2^2+s2 c2 d2+b d2^2)/(4ab-s2^2)`.

The second quadratic form is positive definite. Combining with the new endpoint roof gives

`delta >= max{ 2 gamma+g_v, 4 c1^2/b + 16(a c2^2+s2 c2 d2+b d2^2)/(4ab-s2^2) }`.

On the multiplicity-two Schur boundary, cubic annihilation of the two-dimensional kernel gives `sqrt(a)c+sqrt(b)d=0`, and the pseudoinverse reserve gives

`delta >= 4||c||^2/b = 4||d||^2/a`,

again together with `delta>=2gamma+g_v`.

Thus the live mixed-Schur boundary is attached to a third physical permutation edge, not only to an abstract quartic coefficient.

## First remaining implication

`MOC4-DOUBLE-SWAP-STRUCTURED-MS-EXCLUSION-v1`: exclude a positive-gap common-unitary global maximizer on a mixed-Schur boundary satisfying simultaneously the two transposition roofs, the new double-transposition roof, the exact defect payment above, all subgroup/V4 roofs, same-unitary `P/R/D` identities, and stationarity/full-Hessian conditions. If this branch is excluded, the lead's separate all-pair-blocks-negative-definite `NDI` branch remains.

Exact verifier output terminates `PASS MOC4-DOUBLE-V4-MIXED-SCHUR-BRIDGE-v1`. No individual-unitary positive permutation lift, bistochastic surrogate, target counterexample, or full MOC4 proof is claimed.
