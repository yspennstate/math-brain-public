# Round 212

Round 212 packages the subdivision reduction as a working criterion.

For \(H=\operatorname{Sub}(G)\) and \(q=p^2\), the susceptibilities satisfy
\[
  \bar\chi_q^G\le \bar\chi_p^H
  \le C_\Delta(1+\bar\chi_q^G).
\]
The lower bound is the old-vertex restriction.  The upper bound sums the
old-old, old-midpoint, and midpoint-midpoint contributions using the bounded
incidence operator / bounded degree.

Since
\[
  p_c(G)-p^2=(p_c(H)-p)(p_c(H)+p),
\]
the mean-field susceptibility input transfers from \(G\) to its subdivision.

Therefore, for a nonamenable quasi-transitive bounded-degree graph \(G\), it
is enough to verify the bipartite inward-tail criterion on
\(\operatorname{Sub}(G)\).  The conclusion then transfers back by
\[
  p_c(\operatorname{Sub}(G))=\sqrt{p_c(G)},\qquad
  p_{2\to2}(\operatorname{Sub}(G))=\sqrt{p_{2\to2}(G)}.
\]

This focuses the remaining global target on canonical bipartite subdivisions:
finite-excess control plus inward-return tail control.
