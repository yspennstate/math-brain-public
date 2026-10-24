# Round 115 log

## Goal

Test whether the finite-window high-incidence alternative can actually occur
near criticality.

## Result

Added `lem:incidence-layer-volume-bound` and
`prop:fixed-window-obstruction-escapes`.

For
\[
  V(I)=\sup_x|\{z:d(x,z)\in I\}|,
\]
the deterministic double-counting bound is
\[
  |\mathcal N^I(K,m)|/|K|\le V(I)/m.
\]

Combining this with the finite-window alternative shows that, for fixed
\(J,H,\alpha\), the high-incidence window case is impossible sufficiently
close to \(p_c\).  Therefore the obstruction must escape beyond that fixed
window:
\[
  \sum_{j>J+H}2^{\alpha(j-J)}
  \mathcal R_p^{(2^j,2^{j+1}]}(K)/\bar\chi_p
  \ge c/2.
\]

## Interpretation

The incidence route does not close the problem directly, but it removes one
possible obstruction mode.  What remains is an iterated escaping-tail
phenomenon: near criticality, no bounded dyadic window can carry the
same-witness obstruction.
