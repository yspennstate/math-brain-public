# fleet02/B09 MOC4 report — transposition-tie closure of the flat Spin(4) branch

Run: `20260922T064517Z-fleet02-B09-MOC4-r17`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Exact target and support notation

For complex normal `4 x 4` pairs, after diagonalization write

`h_eta(U)=Re(conj(eta) det(D_a+U D_b U*))`

and

`M_eta=max_{sigma in S_4} Re(conj(eta) prod_i(a_i+b_{sigma(i)}))`.

A counterexample in one support direction would give a genuine unitary global maximizer `U_*` with
`h_eta(U_*)=M_eta+gamma`, `gamma>0`.

This run uses no arbitrary bistochastic surrogate. Every transformation below is a genuine row/column coordinate unitary acting on the same `U`.

## Fresh lead and peer inputs actually consumed

Latest complete campaign-lead snapshot:
- fleet03/B07 run `20260922T060726Z-fleet03-B07-MOC4-r11`,
  theorem `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`.
  At a genuine global support maximizer, for any complementary-pair Spin(4) gate,
  saturation `T=|C|` forces one genuine coordinate `SU(2)` pair factor to be support-flat.
  The lead then moved along that flat orbit to an equal-support unitary with a zero entry.

Named OTHER-account results applied:
- fleet04/B08 `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`, shared commit
  `f6de93d3fe3b7a1af69b55e3b45f446f5b2e8770`.
  For each row transposition `tau`,
  `(h(U)+h(tau U))/2 <= R_tau^row`,
  and symmetrically for columns, where
  `R_tau=max_sigma (H_sigma+H_paired_sigma)/2 <= M`.
- fleet04/B08 `MOC4-PAIR-FLAT-BOUNDARY-v1`, shared commit
  `e8ea294115f41ca1f77047e21af4b712528780a9`.
  The exact true-unitary pair sphere is Bloch-affine
  `alpha+c_x n_x+c_y n_y+c_z n_z`; at a global maximizer a zero pair Hessian is
  equivalent to flatness of the whole pair orbit.

Compatible local dependency:
- fleet02/B09 `MOC4-ZERO-FIBER-HAAR-LIFT-v1`, shared commit
  `aaa26fb7d2e80915369a0348ffba7479cb1d0a26`, retained only for the still-open
  strict zero-entry branch.

## New theorem: `MOC4-TRANSPOSE-TIE-SAFE-v1`

Fix arbitrary complex spectra (with multiplicity), an arbitrary support direction `eta`,
and a genuine `U in U(4)`.

If for some coordinate row transposition `tau`

`h_eta(U)=h_eta(tau U)`,

then

`h_eta(U) <= M_eta`.

The same holds for a column transposition if
`h_eta(U)=h_eta(U tau)`.

### Proof

By fleet04/B08 `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`,

`(h_eta(U)+h_eta(tau U))/2 <= R_tau^row`

for the matching row transposition, with

`R_tau^row=max_sigma (H_sigma+H_paired_sigma)/2`.

Every endpoint support `H_sigma` is at most `M_eta`, hence `R_tau^row<=M_eta`.
Under the assumed tie, the left side is exactly `h_eta(U)`. Therefore
`h_eta(U)<=M_eta`. The column case is identical. QED.

No global-maximizer hypothesis, endpoint uniqueness, invertibility, simple spectrum,
or limiting argument is needed for this tie-safety statement.

## Flat pair closure

If an entire genuine row or column `SU(2)` pair orbit is support-flat, it contains the
coordinate swap point. Hence the current point and its transposition partner tie.
`MOC4-TRANSPOSE-TIE-SAFE-v1` therefore gives

`flat coordinate pair orbit  ==>  h_eta(U)<=M_eta`.

Thus a support-violating global maximizer can have **no flat coordinate pair orbit**.

More quantitatively, let

`g_tau=2M_eta-max_sigma(H_sigma+H_paired_sigma)>=0`

and let `h_eta(U_*)=M_eta+gamma`, `gamma>0`.
The same pair-roof inequality gives

`h_eta(U_*)-h_eta(tau U_*) >= 2 gamma + g_tau`

(and the column analogue). In the Bloch normalization of
`MOC4-PAIR-FLAT-BOUNDARY-v1`, where this swap drop equals `2c_z`, every pair sphere at
a violator has

`c_z >= gamma + g_tau/2 > 0`.

So even when the maximizing endpoint face itself has a transposition edge (`g_tau=0`),
a positive target gap forces strict pair curvature.

## New campaign consequence: `MOC4-SPIN4-SATURATION-EXCLUSION-v1`

Let `U_*` be a genuine global maximizer in a support direction. For any one of the
lead's left/right complementary-pair Spin(4) gates, let `T,C` be the lead quantities.

If `h_eta(U_*)>M_eta`, then necessarily

`T>|C|`.

### Proof

The lead theorem `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1` proves that `T=|C|` makes
one of the two genuine coordinate `SU(2)` factors support-flat through `U_*`.
By the flat-pair closure just proved, that already implies `h_eta(U_*)<=M_eta`,
contradicting positive gap. QED.

This is stronger than merely moving a saturated maximizer to the zero-entry face:
**the saturated mixed-conformal branch is target-safe and cannot contain a support
violator at all.**

## Sharpened conditional end-to-end reduction

Assume MOC4 fails. Choose a support direction and a global maximizer with positive gap.

1. By `MOC4-TRANSPOSE-TIE-SAFE-v1`, all twelve row/column transposition gaps are
   strictly positive, quantitatively at least `2 gamma+g_tau`.
2. By `MOC4-SPIN4-SATURATION-EXCLUSION-v1`, every lead mixed-conformal Spin(4) gate is
   strict: `T>|C|`. There is no saturation branch to send to the zero face.
3. By fleet04/B08 cubature-roof rigidity (as consumed by the lead), saturation of a
   positive subgroup roof with a unique maximizing endpoint coset is target-safe; any
   surviving cubature-boundary violator must therefore be in the fully tied degeneracy
   locus.
4. If the maximizing unitary independently has a zero entry, apply the exact zero-face
   Haar/quaternion theorem and P-weighted reserve. Otherwise it lies in the no-zero
   strict interior branch.

Thus the lead's former `T=|C| -> zero face` branch is completely removed from the
counterexample geometry rather than merely relocated.

## First essential missing implication after this run

`MOC4-ZERO-FACE-STRICT-PAIR-RESERVE-v3`.

For arbitrary complex spectra and support direction, there is no genuine global
maximizer `U_*` with a zero entry and positive gap `gamma` satisfying simultaneously:

- every row/column transposition gap is at least `2 gamma+g_tau`;
- every coordinate pair sphere is strictly curved;
- after relabelling the zero to `u_00=0`, the residual true-unitary `U(2)` fiber has
  quaternion form `h(q)=q^T Hq` with
  `lambda_max(H)=M+gamma`;
- the exact Haar lift has
  `tr(H)/4=M-Delta_mu`, with
  `Delta_mu >= (1/2) sum_{i,j>0} C_i R_j max{g^L_{tau_i},g^R_{tau_j}}`.

Proving this source-valid strict zero-face exclusion, together with the lead's strictly
curved no-zero interior exclusion, would close the current conditional support proof.
A failure must be an actual zero-entry true unitary with actual complex spectra and one
common support direction.

## Boundary and provenance checks

The new tie-safety theorem is inherited directly from an all-true-unitary pair roof and
uses only endpoint inequalities, so singular determinant points and repeated spectra are
included. No endpoint-uniqueness assumption is present. The lead saturation theorem and
pair-flat theorem use genuine `SU(2)` actions/adjugates rather than inverses, so the
saturation-exclusion corollary also has no hidden nonsingularity assumption.

No scientific numerical computation was used in this run. No benchmark material,
answers, credentials, scheduler identifiers, machine paths, unrelated private data,
email, Drive data, paid/API/Codex execution, remote workflow, or public posting was used.
