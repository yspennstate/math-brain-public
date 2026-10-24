# Round 120 log

## Goal

Extract a separated subfan from the logarithmic backscatter fan.

## Result

Added `lem:separated-subfan-extraction` and
`cor:separated-logarithmic-backscatter-fan`.

The deterministic packing lemma says that every finite \(Z\subset V\) contains
a \(2r\)-separated subset \(Z_r\) with
\[
  |Z_r|\ge \frac{|Z|}{V_{2r}},
  \qquad
  V_{2r}=\sup_v |B(v,2r)|.
\]

Applying this to the Round 119 fan with
\[
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor,\qquad 0<\theta<1/2,
\]
gives a subset \(Z_\theta\) with pairwise disjoint \(r_p\)-balls and
\[
  |Z_\theta|
  \ge
  \frac{\sigma_j^2}{4\Delta}\bar\chi_p^{1-2\theta}.
\]
Each selected center still lies in the same annulus from the root and still
receives annular two-point mass at least \((\sigma_j/2)\bar\chi_p\) from the
same finite set \(K\).

## Interpretation

The obstruction now has spatial spread at logarithmic scale: it contains
polynomially many disjoint remote regions, not merely a single crowded annular
cluster.  This is a better input for future BK, separator, or spectral
backscattering estimates.
