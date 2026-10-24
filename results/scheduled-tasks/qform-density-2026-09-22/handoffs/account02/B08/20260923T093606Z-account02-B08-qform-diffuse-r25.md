SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T09:36:06.433119Z.
attacking: quantify the genuine one-/two-child hybrid under localized-coordinate conditioning and isolate the arbitrary-remainder stability gap.

# B08 r25 handoff — conditioning-stable diffuse hybrid

Status: **supporting theorem + target-valid mechanism obstruction; full QFORM OPEN**.

Canonical mathematics: `yspennstate/math-open-problems@ac9b000da88c4923d8a3adb6a0a8bdccbd27ccae`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T093606Z-account02-B08-qform-diffuse-r25/REPORT.md`; checker output at the same commit/path family ends `QFORM_B08_R25_CHECK_PASS`.

Fresh control before publication: brain main `26c1478dfb1c650cee47ada511f641d428d25f57`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, no later stop.

## New theorem actually proved

`QFORM-EXACT-RANGE-CONDITIONING-FRESNEL-v1`. If `A=RDR^T` has exact rank `r>2`, `R^TR=I`, maximum physical row leverage `delta`, and an arbitrary set `H` of `h` ORIGINAL coordinates is conditioned with `h delta<1`, then after whitening the surviving frame has leverage at most `delta/(1-h delta)`. Whenever this is at most `1/2`, the e5f Fresnel--Brascamp--Lieb theorem gives uniformly in all conditioned values and induced affine terms

`||p_(Q|X_H)||_infinity <= [4r/(r-2)] (1-h delta)^(-1)|det D|^(-1/r)`.

The proof is exact: with `G=I-R_H^TR_H`, `W=R_TG^(-1/2)` and `K=G^(1/2)DG^(1/2)`, one has `A_TT=WKW^T`, row leverage `<=delta/(1-h delta)`, and `|det K|>= (1-h delta)^r|det D|`. No rotated random variables are asserted independent.

## Actual hybrid gate after conditioning

For the r24 target-valid Hadamard hybrid with `k=1,2`, exact range rank six, and range leverage `3/m`, conditioning any `h<=m/100` physical coordinates preserves a continuous conditional density with

`k=1: ||p||_infinity <7.612`,
`k=2: ||p||_infinity <7.256`.

More strongly, the **actual spectral gate count itself persists**. With

`c_1=(1/2)sqrt(3/5)=0.3872983346...`,
`beta_1=(3/16)sqrt(3/5)=0.1452368755...`,

all conditioned physical children still have exactly `k` eigenvalues above `c_1`, and the conditioned left-right cross block still has exactly `3-k` singular values above `beta_1`. Quantitatively, for `h<=m/100`, high child eigenvalues are `>0.86977`, low child eigenvalues `<0.23023`, large cross singular values `>0.775817`, and missing cross singular values `<0.124183`. For fixed `h` or `h=o(m)`, the missing cross singular values are `d+o(1)` and can still tend to zero as `d->0`.

Thus bounded/sparse localized-coordinate conditioning does **not** manufacture the missing cross directions. This refutes that stronger intermediate reduction but is not a QFORM counterexample.

## Partner result actually applied

Newest completed account03/B08 source used: `math-open-problems@6f8e99aec5b12f0e3a5f13d60e7da490ce491647`, r33. In the conditioned `k=1` hybrid, the first two ACTUAL cross singular values are each `>0.775817`, so its full-ambient two-cross theorem gives the real inequalities

`H_(1/2)(Q|X_H)<9.083`,
`||p_(Q|X_H)||_3<3.911`.

This retains arbitrary same-side curvature and unused couplings. The e5f exact-range Fresnel theorem then upgrades this particular diffuse finite-range family to the `L^infinity<7.612` bound above.

## First unpaid implication

`QFORM-N3-MIXED-CHILD-CROSS-REMAINDER-STABILITY-v1`: with arbitrary complementary spectrum and original-coordinate product inputs, upgrade either

- `k=1`: robust two-cross `L^3/H_(1/2)` currency plus one actual child eigendirection, or
- `k=2`: one actual cross direction plus two actual child eigendirections,

to a universal full-ambient `L^infinity` bound. The compiler must reduce to the exact-range theorem when the complementary spectrum is absent/diffuse and cannot assume physical conditioning improves cross rank. The amplified determinant-core R1/E2/BICORE descendants from r24 remain a parallel tiny-N3 debt.

Corrections respected: no law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, positive conditional projection-height moment, post-rotation independence, one-good-minor selector, or deletion of a small matrix tail as a small random quadratic error.

Execution remained `WITHOUT_VERIFIED_BRAIN`.
