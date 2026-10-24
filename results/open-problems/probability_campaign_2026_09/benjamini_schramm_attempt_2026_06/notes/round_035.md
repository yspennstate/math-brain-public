# Round 035 log

## Goal

Test whether finite-memory local self-avoidance can give an operator-side
upper bound strong enough for \(T_3\square\mathbb Z\).

## Memory-walk diagnostic

Added `scripts/memory_walk_row_bound.py`.  A memory-\(m\) walk is forbidden to
step onto any of its previous \(m\) vertices.  Every self-avoiding walk is a
memory-\(m\) walk, so the row-sum growth of this finite-state class is a crude
upper bound for \(\gamma_{\rm SAW,2}\).

The finite-state chain records the last \(m\) vertices relative to the current
position in \(T_3\square\mathbb Z\), quotienting only by permutations of the
three tree generators.  The resulting row-growth spectral radii are:

\[
\begin{array}{c|c|c}
m & \#\text{states} & \rho_{\rm row}(m)\\
\hline
1 & 4 & 5.00000000000\\
2 & 11 & 4.00000000000\\
3 & 31 & 4.00000000000\\
4 & 93 & 3.87971935539\\
5 & 311 & 3.87971935539\\
6 & 1105 & 3.84797493536\\
7 & 4099 & 3.84797493536\\
8 & 15445 & 3.83468427516\\
9 & 58793 & 3.83468427516\\
10 & 224263 & 3.82813327169
\end{array}
\]

The first improvement occurs at memory \(4\), when the walk is forbidden from
closing an elementary square.  The improvements then occur in pairs and are
slow.

## Consequence

This row-sum route is far too weak for the current target
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)
  <\frac{20000}{5909}\approx3.38467.
\]
Local finite-memory self-avoidance, at least at accessible memory sizes and
with row-sum estimates, cannot close the operator side.  A useful operator
bound must exploit \(L^2\) cancellation/radial structure rather than ordinary
connective growth.
