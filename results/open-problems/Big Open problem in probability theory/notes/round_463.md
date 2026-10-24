# Round 463 product annular gap remains plausible after correction

Round 463 updates the product stress test after Round 462.

For \(G=T_d\square H\), the current lower bound is
\[
  \Gamma_{\rm ann}(G)
  \ge
  \max\{\sqrt{d-1},\sqrt{g_{\rm geo}(H)}\}.
\]
This does not contradict the desired annular gap in the standard tree-product
cases.  Since \(G\) contains \(T_d\),
\[
  \pc(G)\le \frac1{d-1},
  \qquad
  \frac1{\pc(G)}\ge d-1,
\]
and \(d-1>\sqrt{d-1}\) for \(d\ge3\).  Thus the tree out-and-back lower bound
alone remains below the target threshold.

For \(H=\mathbb Z^r\), the geodesic-growth lower bound contributes roughly
\(\sqrt r\).  This may be nontrivial, but it is still qualitatively different
from the global SAW product obstruction.  The global route sees unrestricted
forward propagation in both factors, while the annular route sees paths that
must return to the same ball boundary.

The corrected product lesson is:

* \(\Gamma_{\rm ann}\) is not purely cyclic in the factor; tree branching can
  contribute through out-and-back returns in a shifted fibre;
* the contribution is square-root in the tree branching because the return
  must retrace tree depth in a different fibre coordinate;
* no product counterexample to the annular gap is visible from these basic
  lower bounds.

The next useful calculation is an upper bound for \(T_d\square\mathbb Z\).
Even a non-sharp transfer-matrix bound below \(d-1\) would strongly support
the annular boundary exponent target.
