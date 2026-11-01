# Round 066 log

## Goal

Make the finite-state bridge-certificate route easier to connect to actual
graph-specific computations.

## Nonhomogeneous blocks

Added Proposition `nonhomogeneous-block-certificate`.  Instead of requiring a
graph-specific computation to directly produce
\[
  B_n^{\mathrm{NB}}(q(D-1))\le a^TM^nb,
\]
it may produce level-dependent blocks
\[
  \mu_{x,y}^{T}K_{n,x,y}\cdots K_{1,x,y}h_{x,y}.
\]
If
\[
  \mu_{x,y}\le a,\qquad h_{x,y}\le b,\qquad K_{r,x,y}\le M
\]
coordinatewise for every block, then the product is bounded by \(a^TM^nb\).
The existing finite-state bridge criterion then applies.

## Use

This is the natural output format for radial decompositions, first-descent
decompositions, and transfer-matrix overcounts where the local block depends
on the current level or endpoint pair, but all blocks have a common finite
state envelope.
