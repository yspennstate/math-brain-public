# MOC4 shared handoff — account03/B07 — 20260922T061700Z

Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

## New theorem

`MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`.

At a genuine global support maximizer, take any complementary-pair Spin(4) mixed-Hessian gate from account03/B07 `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`, with pair quantities `T,C`. If `T=|C|`, then one of the two genuine coordinate `SU(2)` factors has identically zero spherical Hessian. By account04/B08 `MOC4-PAIR-FLAT-BOUNDARY-v1`, support on that true-unitary pair sphere is Bloch-affine; zero curvature at its global maximum therefore forces the entire pair sphere to be support-flat. A genuine `SU(2)` rotation on this flat orbit produces a unitary with a zero entry and **exactly the same support value**.

Hence any support-violating maximizer on a saturated mixed-conformal gate has an equal-gap zero-entry support-violating maximizer. No arbitrary bistochastic relaxation is used.

Because the full support Hessian at a global maximum is negative semidefinite, the two zero-curvature Spin(4) directions actually lie in the kernel of the full Hessian. The transported zero-entry representative therefore carries a genuine two-dimensional transverse Hessian nullity.

## Named assigned partner consumed

Consumed account04/B08 `MOC4-CUBATURE-ROOF-RIGIDITY-v1`, shared commit `fe74bcda174dc2d6f5df7ffa9a36d8c78de3f6cb`, scientific commit `2852795649a9b6d03d97231b3848732e9a9e8e9c`. It proves generic unique-coset cubature-roof saturation is MOC4-safe; a support violator saturating the lead cubature ceiling must be on the all-seven tied-coset degeneracy branch.

Also directly used assigned-partner account04/B08 `MOC4-PAIR-FLAT-BOUNDARY-v1`, shared commit `e8ea294115f41ca1f77047e21af4b712528780a9`, scientific commit `25792dbad3f38449a2115c7302dcc721e3237100`.

## Smallest conditional full deduction

It is enough to prove both:

- `ZF`: every true `4 x 4` unitary with at least one zero entry satisfies the support bound `h_eta(U)<=M_eta` for all spectra and support directions;
- `SI`: every genuine global support maximizer with no zero entry and with `T>|C|` at every left/right complementary-pair Spin(4) gate satisfies the support bound using same-unitary `P/R/D`, subgroup-roof, Cartan and full-Hessian constraints.

Then every hypothetical support violation is either saturated and reduces by the new theorem to `ZF`, or lies in `SI`. Simple nonsingular spectra suffice for the interior proof; singular and repeated spectra follow by continuity, with additional exact boundary reductions already available from account02/B08.

## First remaining implication

The former lead gap `MOC4-FLAT-PAIR-MIXED-RIGIDITY-v1` no longer requires a separate weighted-Gram classification for target reduction: mixed-Hessian saturation already collapses to the zero-entry face.

The first boundary target is now account02/B09 `MOC4-ZERO-FACE-PR-RESERVE-v2`: combine its exact residual-`U(2)` Haar lift/quaternion Hessian reserve with the new two-dimensional transverse Hessian kernel and the retained true-unitary `P/R/D`/pair-roof structure to exclude a positive zero-face support gap. The strictly curved Spin(4) interior remains the second branch.

Adversarial calibration: account01/B09 shared commit `6536718d687d1747dc6306582a1e55eb91cc05af` proves first-order stationarity plus all twelve strict pair tops is insufficient, but its witness is a mixed-Hessian saddle, reinforcing the necessity of the surviving full-Hessian gate.

Scientific report in this repository: `proofnet24/collective-MOC4/account03/B07/20260922T060726Z-account03-B07-MOC4-r11/REPORT.md`, creation commit `edf77dbc0a4657c2fc81630802c3227f193e3faf`.
