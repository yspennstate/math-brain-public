SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-24T08:36:35Z.
attacking: Schur-boundary localization for arbitrary translations and outside cross-couplings; determine exactly when the conditioning-generated sheet boundary is atomless and exploit the completed fleet04/B14 receiver.

# fleet03/B14 — Schur-boundary dichotomy for the physical reflection chamber

Run: `20260924T083635Z-fleet03-B14-QFORM-auto11`

Status: `SUPPORTING_LOCALIZATION_THEOREM_PROVED / PARTNER_APPLIED / FULL_QFORM_OPEN`.

Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and scope

The owner target remains open: for independent real coordinates with marginal densities bounded by one and symmetric A with at least three eigenvalues of modulus at least one, prove a universal density cap for X^T A X, or give a valid counterexample. No support, moment, log-concavity, connected-support or post-rotation independence assumption is used here.

This run changes mechanism from the preceding canonical approximation/cap-saturation reductions. It studies the exact random translation produced by Schur completion inside an already-paid physical reflection block and shows that the outside Schur remainder decides whether the ruled sheet boundary is automatically atomless under every deterministic translation.

## 2. Source-pinned inputs

The designated partner is `fleet04/B14`. Two completed partner results are used at their exact stated scopes.

1. `fleet04/B14` r10, `QFORM` scale-covariant three-coordinate Schur localization, source commit `deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`.
   For an invertible original-coordinate 3x3 block with least absolute eigenvalue sigma, it gives a full-output interval/density bound `6 sqrt(pi)/sigma`, uniformly in outside curvature, cross-couplings and translations.

2. `fleet04/B14` r11, moving-boundary theorem, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T071645Z-fleet04-B14-atomless-boundary-r11/REPORT.md`.
   In the physical reflection branch it supplies a majority-sheet conditional kernel in `C_0([0,infinity))` with height at most `pi sqrt(2)`, and proves that an atomless random sheet boundary makes the mixed majority-sheet density globally `C_0` with the same height. Its theorem explicitly permits the conditional kernel family to depend arbitrarily on the conditioning variable/boundary, provided the uniform height and atomlessness hypotheses hold.

For sheetwise continuity I also use the completed fixed-matrix same-constant regularity compiler recorded by fleet04/B15 at `a1654d5fe319f483999583921d127819e40bc868`, whose Theorem 6.1 says that once a rank-at-least-three target instance has an interval bound M, its exact rough-product law has a `C_0` density with the same height M.

For the flat-branch jump identity I use the later fleet04/B15 atomic-boundary theorem at source commit `68a56e5fdbdc5b2812c544824e4ca584ec014263`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260924T081140Z-fleet04-B15-atomic-boundary-r10/REPORT.md`, which proves the exact jump formula
`H(t0+)-H(t0-)=E[1_{b=t0} h_omega(0)]` for bounded one-sided kernels.

The elementary fact that a nonconstant polynomial of an absolutely continuous random vector is atomless is already present in the fleet corpus (for example fleet03/B15 run `20260923T122734Z-fleet03-B15-qform-auto18`), so it is imported rather than relabelled as new.

## 3. Algebraic localization identity

Let

`B_* = I_3 - (2/3) 1 1^T`.

Then `B_*` is symmetric, `B_*^2=I_3`, and its spectrum is `{1,1,-1}`. Split original coordinates as `X=(U,Z)`, where `U=(X_1,X_2,X_3)` and `Z` contains all remaining independent coordinates. Let

`A = [[B_*, C], [C^T, D]]`

with arbitrary real `C` and symmetric `D`. Define the Schur remainder

`S := D - C^T B_* C`.

For an arbitrary deterministic translation `t=(t_U,t_Z)`, write

`Y_U=U+t_U`, `Y_Z=Z+t_Z`.

Then the translated homogeneous quadratic form is exactly

`Q_t = (X+t)^T A (X+t)`

and, because `B_*^{-1}=B_*`, completion of the active three coordinates gives

`Q_t
 = (Y_U + B_* C Y_Z)^T B_* (Y_U + B_* C Y_Z)
   + Y_Z^T S Y_Z.`

Thus conditioning on `Z=z` creates:

- an arbitrary deterministic translation of the three original active coordinates,
- and a scalar sheet boundary

`b_t(z) = (z+t_Z)^T S (z+t_Z)`.

No norm of `t`, `C`, `D`, `z`, support radius or moment enters this identity.

## 4. Schur-boundary atomlessness dichotomy

### Theorem — `QFORM-REFLECTION-SCHUR-BOUNDARY-DICHOTOMY-v1`

Under the setup above:

**(a) Non-flat Schur branch.** If `S != 0`, then for every deterministic translation `t`, the random boundary `b_t(Z)` is atomless. Consequently the majority-sheet submeasure of `Q_t` has a canonical density `p_{+,t}` satisfying

`p_{+,t} in C_0(R)`,

and

`||p_{+,t}||_infinity <= pi sqrt(2)`.

The bound is uniform simultaneously in dimension, `C`, `D`, `t`, all fragment separations, all support diameters and all moments.

**(b) Schur-flat branch.** If `S=0`, then `b_t` is identically zero for every translation. Hence deterministic translation can never regularize the sheet boundary in this branch. Moreover block Gaussian elimination gives

`rank(A)=rank(B_*)+rank(S)=3`.

The full output nevertheless retains the completed partner bound

`||p_{Q_t}||_infinity <= 6 sqrt(pi)`

and, by the fixed-matrix regularity compiler, `p_{Q_t} in C_0(R)`.

### Proof

If `S != 0`, the map

`z -> (z+t_Z)^T S (z+t_Z)`

is a nonconstant quadratic polynomial for every fixed `t_Z`. The vector `Z` has an absolutely continuous joint law because its coordinates have densities. Therefore every level set has probability zero, so `b_t(Z)` is atomless.

Condition on `Z=z`. The active vector

`U + t_U + B_* C(z+t_Z)`

still consists of three independent translated cap-one marginals. By the completed fleet04/B14 ruled reflection theorem, the conditional majority-sheet law has a kernel `h_z in C_0([0,infinity))`, with

`0 <= h_z <= pi sqrt(2)`,

uniformly in the translation and in `z`. The fleet04/B14 moving-boundary theorem applies with boundary `b_t(z)` and therefore gives the asserted global `C_0` majority density and height bound.

If `S=0`, the displayed completion identity makes the boundary identically zero. The standard block congruence

`[[I, -B_* C], [0,I]]^T A [[I, -B_* C], [0,I]] = diag(B_*, S)`

(up to the equivalent conventional triangular factor) shows `rank(A)=rank(B_*)+rank(S)=3`. Independently, fleet04/B14 r10 applies directly to the physical block `B_*`, whose least absolute eigenvalue is one, and yields the full-output bound `6 sqrt(pi)` for every translation. The fixed-matrix regularity theorem then upgrades that exact full law to `C_0` with no increase of the height constant. QED.

## 5. A sharper sheetwise consequence when S != 0

The partner full-output theorem and the new majority conclusion can be combined without any direct two-sheet trace estimate.

When `S != 0`, let `nu_{+,t}` and `nu_{-,t}` be the majority and minority sheet submeasures after the conditional Schur completion. We have

`p_{Q_t} in C_0(R)`, `||p_{Q_t}||_infinity <= 6 sqrt(pi)`

and

`p_{+,t} in C_0(R)`, `||p_{+,t}||_infinity <= pi sqrt(2)`.

Since `nu_{-,t}=Law(Q_t)-nu_{+,t}`, the function

`p_{-,t}:=p_{Q_t}-p_{+,t}`

is a continuous `C_0` representative of the minority-sheet density. Equality of the measures implies `p_{-,t}>=0` almost everywhere; continuity then implies `p_{-,t}>=0` everywhere. Hence pointwise

`0 <= p_{-,t} <= p_{Q_t}`

and therefore

`boxed(||p_{-,t}||_infinity <= 6 sqrt(pi)).`

Thus in the non-flat Schur branch **both sheet submeasures are individually continuous**. The difficult two-sheet boundary singularity from the raw coarea parametrisation is neutralized here by the combination of an atomless Schur boundary and the already-paid full target interval estimate.

This is a scoped conclusion for the physical reflection chamber; it is not a universal two-sheet theorem.

## 6. Exact boundary matching when S=0

The flat branch gives a complementary identity. Here every conditional sheet boundary is zero. Let the fleet04/B14 majority kernels be `h_z`. The fleet04/B15 atomic-boundary theorem gives the right-edge jump

`J_+ = E[h_Z(0)]`,

with

`0 <= J_+ <= pi sqrt(2)`.

For positive output values near zero only the majority sheet contributes; for negative output values only the minority sheet contributes. The **full** density is continuous by the fixed-matrix rank-three theorem. Consequently the minority sheet has a finite left boundary trace and the two traces match:

`boxed(lim_{s up to 0} p_{-,t}(s)
      = lim_{s down to 0} p_{+,t}(s)
      = E[h_Z(0)]
      <= pi sqrt(2)).`

So in the exact Schur-flat rank-three chamber the apparent one-sided discontinuities are forced to cancel in the full density. Treating the two sheets independently would discard this cancellation. This gives a concrete reason not to absoluteize the two-sheet decomposition before the full density is assembled.

## 7. Actual designated-partner inequality

For every matrix

`A = [[B_*,C],[C^T,D]]`

and every independent cap-one product input, the principal block `B_*` has least absolute eigenvalue one. Hence the completed fleet04/B14 r10 theorem gives, for every deterministic translation `t`,

`boxed(P((X+t)^T A (X+t) in I) <= 6 sqrt(pi) |I|)`

and

`boxed(||p_{(X+t)^T A (X+t)}||_infinity <= 6 sqrt(pi)).`

This family is genuinely in the owner's target: by Cauchy interlacing, the principal spectrum `{1,1,-1}` forces the full A to have at least two eigenvalues `>=1` and at least one eigenvalue `<=-1`.

If in addition `S=D-C^T B_* C !=0`, the new localization theorem sharpens the majority sheet to

`boxed(p_{+,t} in C_0(R), ||p_{+,t}||_infinity <= pi sqrt(2))`

uniformly over the same arbitrary translations and rough outside laws.

Numerically,

`pi sqrt(2) = 4.442882938158366...`,

`6 sqrt(pi) = 10.634723105433096...`.

## 8. What is new and what is source-matched

Source-matched inputs, not claimed new here:

- exact zero-tax Schur completion for an invertible active block (fleet01/B14);
- the elementary fact that a nonconstant polynomial of an absolutely continuous vector is atomless (existing B15 corpus);
- the fleet04/B14 atomless moving-boundary theorem;
- the fleet04/B14 physical-triple full-output bound;
- the fleet04/B15 atomic-boundary jump formula;
- the fixed-matrix same-constant `C_0` compiler.

The new supporting synthesis proved here is the **translation-uniform Schur-boundary dichotomy** for the physical reflection chamber:

`S !=0` iff the completed outside quadratic boundary remains a nonconstant polynomial under every deterministic translation, hence is automatically atomless and regularizes the majority sheet;

`S=0` iff every translated boundary is deterministic, in which case the full matrix is exact rank three and the two sheet-edge traces must match by full-law continuity.

A targeted visible-code search for the combined `atomless` + `D-C^T B_* C` formulation returned no match before publication. Search misses are not treated as proof of external novelty.

## 9. Remaining implication

The full QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED.

This report does not derive a uniformly conditioned physical reflection block from the bare spectral hypothesis. The unresolved structural bridge is still to aggregate diffuse original-coordinate banks or otherwise preserve product provenance before paying small physical pivots/minors. The present theorem says that, once a reflection-type physical triple is paid, arbitrary deterministic shifts and arbitrary outside cross-couplings create no additional boundary regularity problem except the exact Schur-flat algebraic branch, where full-law continuity forces sheet cancellation.

A useful next B14 target is to identify an analogous Schur-boundary invariant for grouped/bank variables where the active 3x3 receiver is obtained by a product-preserving aggregation rather than an actual physical triple.
