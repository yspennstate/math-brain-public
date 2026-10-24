# B07 / A034 — row-marginal-floor closure for K3

**Status:** PROVED proper-class theorem, pending independent review. Full FEI
remains **OPEN**.

## Mathematical movement

The preceding complete K3 address ledger left exactly the conditional data-row
entropy

`R_Y = sum_T w_T H(q_T)`

unpaid. This run pays that term on a class substantially larger than the
row-monomial class. Product structure is not needed.

If every nonzero spectral-coordinate marginal of every conditional row law is
at least `beta`, entropy subadditivity and the monotonicity of `h2(x)/x` give

`R_Y <= [h2(beta)/beta] I_Y`.

Inserting this into the checked K3 address ledger proves

`H(f) <= 4 I_A(f) + [8+h2(beta)/beta] I_Y(f)`.

For fair/frozen row marginals `{0,1/2,1}`, this becomes

`H(f) <= 4 I_A(f)+10 I_Y(f) <= 10 I(f)`.

The constant is independent of data dimension, row support size, correlation,
Fourier phase, overlap, and the number of active data coordinates. In
particular, correlated row laws uniform on arbitrary affine spectral
subspaces are covered; they need not be coordinate products.

## Previous and new class

- Previous: row-monomial K3, `R_Y=0`, constant 8.
- New: exponentially supported and correlated rows with a fixed marginal
  floor, constant `8+h2(beta)/beta`; fair/frozen rows have constant 10.
- Explicit growing family: substitute disjoint bent Boolean blocks into the
  three inputs of an arbitrary three-bit gate. The general theorem applies,
  while an exact calculation improves this family to constant 4.

## Parameter-removal attempt

The proof keeps the dependence on `beta` exact:

`h2(beta)/beta = log2(1/beta)+log2(e)+o(1)`.

This logarithm is sharp for the scalar entropy-subadditivity step. It cannot
be dropped without a separate Boolean-coupled reserve. A genuine four-bit
point defect already realizes row marginal `1/50`, so fair/frozen marginals
are not automatic even with one data bit.

The next unpaid lemma is to pay rare row marginals through the already visible
address/granularity reserves without spending the complete truth-table label
charge again. Even a full K3 closure would not remove the general-k
truth-table distance loss.

## Verification

`verify_row_marginal_floor.py` exhausts all 65,536 Boolean functions on three
address bits and one data bit. It checks the address-marginal ledger, exact
entropy chain rule, fair/frozen row payment, and the resulting constant 10.
It also checks all 256 base gates under three disjoint two-bit bent
substitutions and 50,000 scalar marginal-floor inequalities.

The all-dimensional theorem is analytic; the finite checks are an independent
algebra audit, not an extrapolation.

## Sources

- Owner control revision `2026-10-12.1`, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- Exact K3 fiber trichotomy and point-defect constant-four theorem.
- Immediate prior complete K3 address-marginal package
  `20261012T100659Z-account01-B07-a034-k3-marginal`.
- Immediate prior joint fiber-code package `20261012T090803Z`.

## Scope and handoff

This is not the unrestricted conditional-product K3 theorem, a uniform
recurrence in `k`, or full FEI. Route to A088/A094 for independent review and
to B20 for candidate assembly. The next A034 attempt should attack the rare
marginal regime, not repeat finite K3 fiber classification.
