# Round 112 log

## Goal

Convert the root-layer obstruction into a first-moment crossing obstruction.

## Result

Added `def:annular-crossing-mass` and
`prop:weighted-crossing-obstruction`.

For
\[
  \mathcal B_p^I(K,Z)
  =
  |K|^{-1}\sum_{z\in Z}
  \sum_{\substack{x\in K\\d(x,z)\in I}}Q_p(x,z),
\]
failure of far-leg tightness forces, for every \(0<\alpha<\beta\), a
macroscopic \(K\) and annular receiving sets \(Z_j\) with
\[
  \sum_{j\ge J}2^{(\alpha+\beta)(j-J)}
  \mathcal B_p^{(2^j,2^{j+1}]}(K,Z_j)
  \ge
  \frac{\epsilon^2}{4}(1-2^{-\alpha})^2(1-2^{\alpha-\beta}).
\]

## Interpretation

The obstruction can now be stated using first moments of the normalized
two-point kernel.  A counterexample must sustain weighted annular connections
from one macroscopic test set into remote receiving layers.
