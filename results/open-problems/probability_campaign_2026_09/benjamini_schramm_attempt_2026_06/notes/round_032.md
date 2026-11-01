# Round 032 log

## Goal

Look for a percolation-side comparison strong enough to pair with the current
finite-length SAW certificate for \(T_3\square\mathbb Z\):
\[
  1/\|C_{15}\|_{2\to2}^{1/15}=0.274159516989.
\]

## Depth-two tree-block process

Added `scripts/tree_block_branching_monte_carlo.py`, a screening tool for a
finite tree-block lower process.  From a retained vertical subset in one
fiber, the process exposes a depth-two forward binary tree of fibers and then
keeps a bounded-span reached subset in each of the four boundary fibers.  The
boundary fibers are disjoint for future generations, so an exact version of
this construction would give a finite-type Galton-Watson lower process.

The Monte Carlo mean matrix is not a proof, but it is the first diagnostic in
this project that reaches the SAW threshold scale.

With type width \(W=5\), margin \(2\), block depth \(2\), and cardinality
selector, the estimated spectral lower values were:

\[
\begin{array}{c|c|c}
p & \text{samples per type} & \widehat\rho_{\rm lower}\\
\hline
0.29545 & 3000 & 1.22196701019\\
0.28000 & 10000 & 1.07116952698\\
0.274159516989 & 10000 & 1.01188827097\\
0.274159516989 & 30000 & 1.00965759948\\
0.274159516989 & 30000 & 1.01436567177\\
0.27200 & 20000 & 0.984663250668\\
0.27000 & 20000 & 0.974724902935\\
0.26800 & 20000 & 0.949345580590
\end{array}
\]

Thus the sampled threshold appears to lie between \(0.272\) and
\(0.274159516989\), close enough that an exact certificate at the SAW
threshold may be possible.

## Exact-transfer attempts

Added two deterministic prototypes:

- `scripts/tree_block_branching_scan.py`, which keeps the best retained subset
  of the union of all reached boundary components;
- `scripts/tree_block_component_scan.py`, which conservatively keeps only the
  best single reached component in each boundary fiber.

Both are currently too slow even on very small depth-two windows.  The state
space is dominated by the row-frontier distribution over the seven fibers of
the depth-two tree block.

## Consequence

This is now the most promising \(T_3\square\mathbb Z\) route.  The next
technical target is an exact rational or interval-arithmetic transfer for the
depth-two tree-block process at
\[
  p=1/\|C_{15}\|_{2\to2}^{1/15}\approx0.274159516989.
\]
If successful, it would combine with the existing \(m=15\) SAW certificate to
prove
\[
  p_c(T_3\square\mathbb Z)<p_{2\to2}(T_3\square\mathbb Z),
\]
which would complete the remaining line-factor case in the current product
program.
