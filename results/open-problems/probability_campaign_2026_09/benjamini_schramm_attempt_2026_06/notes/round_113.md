# Round 113 log

## Goal

Extract a deterministic geometric obstruction from the root-layer obstruction.

## Result

Added `def:annular-incidence-layers`, `lem:root-layer-incidence`, and
`prop:weighted-incidence-obstruction`.

For
\[
  \mathcal N^I(K,m)=
  \{z:|\{x\in K:d(x,z)\in I\}|\ge m\},
\]
we have
\[
  Z_p^I(K,\lambda)\subseteq\mathcal N^I(K,\lambda\bar\chi_p).
\]

Therefore failure of far-leg tightness forces macroscopic finite sets \(K\)
with many remote annular centers that each see at least
\[
  m_j\asymp 2^{-\beta(j-J)}\bar\chi_p
\]
points of \(K\) in the corresponding dyadic annulus.

## Interpretation

The obstruction now has a deterministic shell-incidence form.  This gives a
possible route to contradiction through pure graph geometry or expansion,
separate from percolation estimates.
