# Round 033 log

## Goal

Convert the depth-two tree-block Monte Carlo observation from Round 032 into a
valid regenerative lower process, or identify precisely why it cannot be used
as stated.

## Factorization of the mean matrix

Added `scripts/tree_block_factorized_scan.py`.  The mean matrix of a valid
two-generation block does not require the full joint law of the four boundary
fibers.  It can be factorized through the full reached set in an intermediate
fiber:

\[
  S\longrightarrow R_{\rm middle}\longrightarrow T_{\rm leaf}.
\]

This avoids the seven-fiber row-frontier explosion.  In the version where the
state is already vertically expanded at block entry and the boundary leaves are
also vertically expanded before retention, the type-width \(5\), margin \(2\)
threshold is
\[
  p=0.308089193427.
\]
This is a valid finite-window mean computation for that convention, but it is
not competitive.

## Regenerative convention

Added `scripts/tree_block_regenerative_scan.py`.  Here the state is a raw seed
set in a boundary fiber whose vertical edges have not yet been exposed.  A
block:

1. expands vertically in the root fiber,
2. crosses to the two middle fibers and expands vertically there,
3. crosses to the four boundary fibers but does not expose boundary vertical
   edges.

This is genuinely regenerative: the boundary seed sets start independent
copies of the same process.  For type width \(5\), margin \(2\), the threshold
is
\[
  p=0.304900973287.
\]
At the current SAW threshold
\[
  p=0.274159516989
\]
the lower ratio is only
\[
  0.758932096832.
\]
For type width \(6\), margin \(2\), a probe at \(p=0.28\) gives ratio
\[
  0.815985271421.
\]

## Correction to Round 032

The Round 032 Monte Carlo block exposed vertical edges in both the incoming
root fiber and the outgoing boundary fibers.  Iterating that block would reuse
boundary-fiber vertical randomness, so it is not a clean Galton-Watson lower
process as stated.  It remains useful only as a heuristic for what full
connectivity in a finite block looks like; it is not evidence for a valid
certificate at \(p=0.274159516989\).

## Consequence

The valid depth-two block variants tested here do not improve the existing
percolation-side certificates.  The remaining \(T_3\square\mathbb Z\) case
still needs either:

- a different regenerative block state that keeps enough boundary information
  without reusing exposed vertical edges;
- a sharper SAW/operator bound;
- or a direct \(p_{2\to2}\) argument avoiding the global SAW union bound.
