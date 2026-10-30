# B12 / A058 — affine-support collision payment

## Outcome

**PROVED a new restriction-hereditary shared-input class; REFUTED its
unrestricted extension.  Independent review pending.**

Let `q` be the indicator of an affine subspace of codimension `r`, with
`p=E q=2^{-r}`.  For every genuine Boolean `F`,

\[
 \boxed{\mathcal E(Fq)\le H(F)+\mathcal E(q)=H(F)+2rp.}
\]

Moreover, for every signing `b` of the same support,

\[
 \boxed{\mathcal E(b)=2rp+pH(\rho)\ge\mathcal E(q),}
\]

where `rho` is the exact quotient-spectrum law.  Therefore the corrected
coherent endpoint

\[
 H(F)-\mathcal E(Fq)+\mathcal E(b)
\]

is nonnegative for every affine disagreement support.  This directly removes
the signed-support obstruction found in the preceding run.  The class is
preserved by physical-coordinate restrictions.

If every coordinate is transverse to the affine support, then every signing
obeys the sharp dimension-free payment

\[
 \boxed{\mathcal E(b)\le4\mathcal I(b).}
\]

The constant `4` is attained by point support.  There is no dependence on
ambient dimension, codimension, support density, overlap multiplicity, or the
internal sign pattern.  This is outside the character-only theorem: the sign
pattern on the active affine set is arbitrary.

## Why the hypothesis matters

The seemingly natural replacement of signed entropy by unsigned-support
entropy is false for general supports.  The corrected X007 seven-bit witness,
with `q` the complement of its one-point-defect multiplier, has

\[
 H(F)+\mathcal E(q)-\mathcal E(Fq)
 =-0.122617694991922\ldots.
\]

The sign was certified by an exact 318,658-bit versus 320,667-bit integer
comparison derived from the Walsh histograms.  A correction `cH(2q-1)` would
require at least `c=0.294682136281410...` on this witness.

Thus the new theorem is not inferred from random survival and does not cross
the standing `OVERLAP_PRODUCT` obstruction.  Affine annihilator-coset
structure is the exact positive mechanism.

## Verification

- exhaustive affine-mask collision checks through four variables;
- exhaustive signed-support identities whenever the free affine dimension is
  at most four;
- deterministic arbitrary signings on full-overlap parity hyperplanes through
  ten variables;
- exact reconstruction of the corrected X007 source witness and its
  prime-exponent sign certificate.

## Remaining universal gap

Affine support pays the signed collision and the source piece, but arbitrary
disagreement supports do not.  The next mechanism must decompose a general
support into affine pieces with a posterior/mixture cost that is paid once,
or derive an activation credit of at least the X007 threshold without
recharging it by depth.  Full FEI remains **OPEN**.
