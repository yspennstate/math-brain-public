# B12 / A058 — complete shared-telescope obstruction

## Outcome

**REFUTED, by an exact Boolean family:** neither two-query grouping nor a
complete shared-coordinate telescope repairs the gauge-corrected coherent
potential.

The preceding A058 run left open whether the negative one-query defect of

\[
 \widetilde J=\mathcal E(a+hb)-\mathcal E(hb)+\mathcal E(b)
\]

could be repaired by grouping the next shared query.  A four-bit Boolean
triple now gives

\[
 \widetilde J=\frac{6-9\log_2(64/9)}{64}
 =-0.3042292966721747\ldots,
\]

while every nonempty restricted face has potential exactly zero.  Hence
every one-, two-, three-, or four-coordinate block has this same negative
decrement.  The complete restriction tree has negative total charge.

The witness comes from an unsigned support mask `q` of size six and a signing
`g` of the same mask.  The positive mask has spectral magnitudes
`{6/16, 2/16 (15 times)}`, while the signing has six magnitudes `4/16` and
ten zeros.  Signing therefore lowers raw spectral entropy from
`1.8042292966721747...` to `3/2`.  The Boolean realization has
`b=g`, `hb=q`, and realised output `F=1`.

Tensor powers give a dimension-`4m` family with exact defect

\[
 m(3/8)^{m-1}\frac{6-9\log_2(64/9)}{64}<0.
\]

This converts a finite obstruction into an all-dimensional parametric
family.  It does not disprove FEI; every realised output in the family is
constant.  It does prove that the complete changing coherent remainder
cannot be paid by this endpoint potential, by nodewise nonnegative charges,
or by any fixed regrouping of its shared-coordinate increments.

## Exact scope movement

- **Previous:** character-only overlap closed exactly; the natural shared
  potential failed at one node, but a larger block or endpoint telescope was
  not excluded.
- **New:** the same potential is negative at the root, every nonempty face
  is zero, and tensor powers preserve a strict negative endpoint for all
  dimensions `4m`.
- **Not implied:** no claim about unbounded `H/I`; no contradiction with the
  accepted disjoint or character-overlap theorems.
- **Next unpaid step:** introduce a joint signed-support/posterior collision
  credit that detects the entropy reduction from `|b|` to a signing of `b`,
  then prove that credit is paid once by physical source influence or a
  terminal reserve.

## Verification

`CHECK.py` uses exact rational Walsh transforms to certify the root spectra,
all 80 nonempty faces, all 15 coordinate blocks, and direct tensor powers
through 16 variables.  The analytic tensor identity proves the family for
all `m`.

## Source and correction check

The current B12 contract and owner control were reread.  The newer B19/A094
review accepts a distinct negative-point-defect tower only at its stated
fresh/common-core scope and explicitly excludes reused variables and changing
overlapping cores, so it does not repair or conflict with this witness.

Full FEI remains **OPEN**.  Independent review of this A058 obstruction has
not yet been observed.
