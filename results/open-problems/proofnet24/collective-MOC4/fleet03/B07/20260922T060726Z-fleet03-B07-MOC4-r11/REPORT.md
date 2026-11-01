# fleet03/B07 MOC4 report — Spin(4) saturation collapses to the zero face

Run: `20260922T060726Z-fleet03-B07-MOC4-r11`  
Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**.  
Execution status: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Target

For every complex normal `4 x 4` pair `A,B` with spectra `a_i,b_i`, prove

`det(A+B) in conv{ prod_i (a_i+b_{sigma(i)}) : sigma in S_4 }`,

including singular and repeated spectra.

For a unit-modulus support direction `eta`, write

`h_eta(U)=Re(conj(eta) det(D_a+U D_b U*))`

and

`M_eta=max_{sigma in S_4} Re(conj(eta) prod_i(a_i+b_{sigma(i)}))`.

A target counterexample is equivalent to some support direction with a genuine unitary global maximizer `U_*` satisfying `h_eta(U_*)>M_eta`.

## Fresh compatible state consumed

The active owner control remains `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; fleet03/B07 remains MOC4 team lead. No later stop was present at the final pre-write control read.

Latest complete lead theorem entering this run was fleet03/B07 `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1` (shared blob `8ff513a0355006854065775e0a614f4857846097`). For a chosen complementary-pair block split in the real `Lambda^2 SU(4) ~= SO(6)` model, the genuine tangent

`L_Z|_{alpha+gamma}=[[0,Z],[-Z^T,0]]`, `Z in M_2(R)`,

has Hessian block, after conformal/anticonformal decomposition,

`[ -2(T-C) I_2   M ; M^T   -2(T+C) I_2 ] <= 0`,

hence `T>=|C|` and `||M||_op^2<=4(T^2-C^2)` at a global support maximizer.

### Named assigned other-account result consumed

Consumed assigned partner **fleet04/B08** result `MOC4-CUBATURE-ROOF-RIGIDITY-v1`, shared commit `fe74bcda174dc2d6f5df7ffa9a36d8c78de3f6cb`, scientific commit `2852795649a9b6d03d97231b3848732e9a9e8e9c`. It proves that saturation of any one of the lead's seven positive subgroup roofs with a unique maximizing endpoint coset forces a proper coordinate block and is therefore MOC4-safe; any support violator saturating the cubature ceiling must lie in the all-seven tied-coset degeneracy branch.

Also applied the earlier assigned-partner theorem **fleet04/B08** `MOC4-PAIR-FLAT-BOUNDARY-v1`, shared commit `e8ea294115f41ca1f77047e21af4b712528780a9`, scientific report commit `25792dbad3f38449a2115c7302dcc721e3237100`. It proves that on a true row/column `SU(2)` pair orbit the support is Bloch-affine, and that a flat pair orbit through a global maximizer can be moved at equal support to a genuine unitary with a zero entry.

For adversarial calibration, fleet01/B09's newest `MOC4-STATIONARY-STRICT-PAIR-PROJECTED-LIFT-v1` no-go (shared commit `6536718d687d1747dc6306582a1e55eb91cc05af`) shows that full first-order stationarity plus all twelve strict pair tops is not enough: its exact genuine unitary is a mixed-Hessian saddle. Thus the mixed-Hessian layer cannot be discarded.

## New exact theorem

### `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`

Let `U_*` be a genuine global maximizer of `h_eta`. Choose any one of the three complementary-pair decompositions in the real exterior-square model and let `T,C` be the corresponding mixed-Hessian pair quantities from `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`.

If

`T=|C|`,

then there is a genuine unitary `U_0` with at least one zero entry such that

`h_eta(U_0)=h_eta(U_*)`.

In particular, if `U_*` is support-violating then `U_0` is an equal-gap zero-entry support-violating global maximizer. Therefore a target counterexample cannot be trapped solely on a saturated mixed-conformal Hessian gate away from the zero-entry boundary.

### Proof

Fix the selected complementary-pair split. Let the untouched complementary-pair plane correspond to a coordinate partition `I union I^c={1,2,3,4}`, `|I|=|I^c|=2`.

1. **Spin(4) identification is genuine-unitary, not bistochastic.**  
   The stabilizer of the untouched exterior-square plane is a `Spin(4)` subgroup of `Spin(6) ~= SU(4)`. Its two simple factors are exactly the coordinate subgroups `SU(2)_I` and `SU(2)_{I^c}` acting on the two two-dimensional coordinate subspaces of `C^4`. On the four cross wedges, their infinitesimal exterior-square actions are respectively the conformal and anticonformal two-dimensional subspaces of the matrices `Z in M_2(R)`. Directly on the wedge basis, an `X in su(2)` acting on `span{e_i:i in I}` fixes `e_I` and `e_{I^c}` and acts on the four cross wedges as two copies of `X`; the complementary `su(2)` factor gives the opposite Spin(4) chirality.

2. **The lead Hessian gives one zero-curvature genuine `SU(2)` factor.**  
   The restriction of the full Hessian to the two Spin(4) factors is

   `-2(T-C) I_2` and `-2(T+C) I_2`.

   At a global maximum `T>=|C|`. If `T=C`, the first genuine `SU(2)` factor has zero Hessian on both Bloch-sphere tangent directions; if `T=-C`, the second factor does.

3. **Zero curvature on the Bloch-affine pair sphere forces exact flatness.**  
   By fleet04/B08 `MOC4-PAIR-FLAT-BOUNDARY-v1`, on either genuine coordinate `SU(2)` pair orbit the support has the exact form

   `h_eta(GU_*)=alpha+c_x n_x+c_y n_y+c_z n_z`, `n in S^2`.

   Because `U_*` is a global maximizer, the current pole maximizes this affine sphere, so after choosing north-pole coordinates `c_x=c_y=0` and `c_z>=0`. The spherical Hessian on its two tangent directions is a negative scalar multiple of `c_z I_2`. Step 2 makes that Hessian identically zero, hence `c_z=0`; therefore `c=0` and the entire genuine pair orbit is support-flat.

4. **Move the flat orbit to a zero entry without changing support.**  
   A nontrivial row (or column) pair has some nonzero two-coordinate column (or row) vector. `SU(2)` acts transitively on the unit sphere in `C^2`, so an element of the same pair subgroup sends that vector to one coordinate axis. The resulting genuine unitary has a zero entry. Because the entire pair orbit is flat, its support is exactly `h_eta(U_*)`.

This proves the theorem. No inverse, spectral gap, simplicity assumption, stochastic relaxation, or genericity assumption is used.

## Full-Hessian nullity corollary

At a global maximizer the real support Hessian is negative semidefinite. In the saturated case above, every vector in the two-dimensional flat Spin(4) factor has zero quadratic form. For a symmetric negative-semidefinite operator, `v^T H v=0` implies `Hv=0`. Hence the full Hessian has a two-dimensional genuine-unitary kernel, not merely a vanishing principal block. This nullity is transported along the flat `SU(2)` orbit to the zero-entry representative.

Thus a zero-entry violator reached from mixed-Hessian saturation is more special than an arbitrary zero-entry point: it carries a two-dimensional transverse exact flat orbit.

## Smallest conditional full deduction now

The support-separation proof is reduced to two target-level obligations.

`ZF`: **Zero-face support.** For every true unitary with at least one zero entry and every spectra/support direction, prove `h_eta(U)<=M_eta`.

`SI`: **Strict Spin(4) interior.** For every genuine global support maximizer with no zero entry and with `T>|C|` for every left/right complementary-pair Spin(4) gate, prove `h_eta(U)<=M_eta` using the retained same-unitary `P/R/D`, subgroup-roof, Cartan and full-Hessian constraints.

If `ZF` and `SI` hold for simple nonsingular spectra, full MOC4 follows: any support violation has a global maximizer; a saturated Spin(4) gate is sent by the theorem above to `ZF`, while otherwise it lies in `SI`. Repeated/singular spectra follow by continuity of the determinant support function and the 24 endpoint support values; independently, fleet02/B08 has already solved the repeated-spectrum/common-block faces except explicit collinear supported-face degeneracies.

The newest fleet04/B08 cubature-rigidity theorem further narrows `SI`: generic saturation of a subgroup cubature roof is already safe, so an interior violator is either strictly below the active cubature ceiling or lies on the fully tied seven-roof degeneracy locus.

## Direct attack on the first unpaid implication

The previous first gap `MOC4-FLAT-PAIR-MIXED-RIGIDITY-v1` asked for a classification of the weighted Gram-cancellation locus at `T=|C|`. The theorem above bypasses that classification: every such saturation already reduces to the zero-entry boundary by a genuine coordinate `SU(2)` orbit. The Gram-collinearity conclusion remains valid but is no longer the first target-level obstruction.

The first boundary implication is now the source-valid `MOC4-ZERO-FACE-PR-RESERVE-v2` isolated by fleet02/B09: on `u_00=0`, its exact residual `U(2)` fiber has Haar-average endpoint lift and quaternion form `h(q)=q^T H q`, with

`-Tr Hess_{S^3} h >= 8 gamma + 4 sum_{i,j>0} C_i R_j max{g^L_{tau_i},g^R_{tau_j}}`

for any positive violation gap `gamma`. Combining that lower curvature payment with the present two-dimensional transverse full-Hessian kernel is the next clean zero-face mechanism; no arbitrary bistochastic substitute is permitted.

## Verdict

`ESSENTIAL_STEP_APPLIED`. The saturation branch of the mixed-conformal Hessian gap is collapsed exactly to the zero-entry face, using only true-unitary group actions. Full MOC4 is still **OPEN** because the general zero-entry support inequality and the strictly curved interior branch remain unpaid.
