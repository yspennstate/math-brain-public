# Round 135 log

## Goal

Thin the matched obstruction until the anchor, gate, and matched-vertex
coordinates are separated.

## Result

Added `lem:bounded-degree-packing-extraction`,
`cor:separated-matched-incidence-obstruction`, and
`prop:separated-matched-incidence-criterion`.

Starting with the matched triples from Round 134, greedily pack the anchors at
radius \(4r_p\), then greedily pack the matched \(Y\)-vertices at radius
\(2r_p\).  The bounded-degree loss is
\[
  \Delta^{4r_p+1}\Delta^{2r_p+1}
  \le \Delta^2\bar\chi_p^{6\theta}.
\]
Since Round 134 gives
\[
  m\ge
  \frac{\sigma_j^3}{16\Delta^3}\bar\chi_p^{1-6\theta},
\]
the separated matched obstruction has size at least
\[
  \widetilde\kappa_j(p)=
  \frac{\sigma_j^3}{16\Delta^5}\bar\chi_p^{1-12\theta}.
\]

## Interpretation

The remaining obstruction is now a separated family of anchored annular
quadrilaterals:
\[
  (z_i,a_i,y_i),\qquad 1\le i\le n,
\]
where the anchors are \(4r_p\)-separated, the gates are \(2r_p\)-separated, and
the \(y_i\)'s are \(2r_p\)-separated.  The improved lower scale
\[
  2^j\ge a\log_\Delta\bar\chi_p
\]
is preserved.

This may be the right form for a future probabilistic contradiction, because
the \(r_p\)-neighbourhoods around the gate and endpoint coordinates can now be
treated as disjoint local blocks.
