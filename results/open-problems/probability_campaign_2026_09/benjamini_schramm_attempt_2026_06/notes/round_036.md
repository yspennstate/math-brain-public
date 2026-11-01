# Round 036 log

## Goal

Improve the operator-side diagnostics by applying the tree spherical
\(\ell^2\) transform to finite-memory walk classes, rather than using only
row-sum growth.

## Finite-memory spherical endpoint bounds

Added `scripts/memory_walk_spherical_bound.py`.  A memory-\(m\) walk is
forbidden to step onto any of its previous \(m\) vertices, so every
self-avoiding walk is counted by this class.  The script quotients recent
tree-label histories by permutation symmetry, aggregates endpoint counts by
tree radius and vertical height, and evaluates the same spherical bound used
for the exact SAW diagnostics:
\[
  D_n^{(m)}=\sum_{r,h} a_{r,h}^{(m)} R_r\otimes S^h.
\]

Validation:

- memory \(1\), length \(6\), gives root \(4.82842712474619=2\sqrt2+2\), the
  unrestricted walk operator scale;
- memory \(2\), length \(6\), gives root \(3.93197897021346\), consistent with
  a finite nonbacktracking bound.

Longer finite-memory spherical bounds:

\[
\begin{array}{c|c|c|c}
m & n & \#\text{states at }n & \|D_n^{(m)}\|_{2\to2}^{1/n}\\
\hline
4 & 12 & 37558 & 3.72912495963039\\
4 & 16 & 603902 & 3.69947391546724\\
6 & 12 & 135704 & 3.69916541538674\\
6 & 16 & 2225136 & 3.66431090701598\\
8 & 12 & 457984 & 3.68832795340348\\
8 & 14 & 1980898 & 3.66622361402831
\end{array}
\]

For comparison, the exact SAW quotient computation gives
\[
  \|C_{15}\|_{2\to2}^{1/15}\le 3.64751153264.
\]

## Consequence

The spherical \(L^2\) evaluation is much stronger than the row-sum
finite-memory diagnostic, but accessible finite-memory classes still overcount
too much.  They do not approach the current target
\[
  20000/5909\approx3.38467.
\]
The operator-side route still needs either a genuinely asymptotic
self-avoidance mechanism or a sharper exact SAW computation, not just local
memory constraints.
