# Round 130 log

## Goal

Remove the remaining root two-point weights from the gate-incidence
obstruction.

## Result

Added `cor:deterministic-gate-incidence-obstruction` and
`prop:deterministic-gate-incidence-exclusion-criterion`.

The root-weighted gate-incidence obstruction gives
\[
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)\ge\kappa_j(p).
\]
Since \(\tau_p(x,a_z)\le1\), this implies
\[
  |Z^\sharp|\ge\kappa_j(p).
\]

Thus any counterexample forces a deterministic anchored configuration:

- at least \(\kappa_j(p)\) selected gates;
- each gate lies in the expanded annulus of the root;
- each gate is anchored at distance \(r_p\) to a separated remote center;
- each gate is incident to at least \(\kappa_j(p)\) vertices of \(K\) in its
  expanded annulus.

## Interpretation

The obstruction has become combinatorial.  The remaining problem is to rule out
these anchored gate-incidence patterns near criticality.
