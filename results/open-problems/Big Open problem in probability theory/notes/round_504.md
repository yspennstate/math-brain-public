# Round 504 scalar row-sum closure is too crude

Correction added in Round 505: the diagnostic below omits the two
parent-child crossing-edge costs \(z^2\) for each child atom.  With those
costs included, the scalar child-atom inventory is actually small at the
target scale.  This note is retained as a record of the failed convention,
not as a valid obstruction.

Round 501 suggests a pair-span kernel \(\alpha^{|a-b|}\).  The tempting next
step is to collapse this kernel to its row sum and try to prove a scalar
contraction.  This loses too much information in the low-branching cases.

Use the calibrated fresh-block multiplier from Round 502,
\[
  w_*(z)=\frac{2z}{1+z^2}.
\]
If one ignores packet-size fugacity, hard-core gap interactions, and the
precise excess walk, then a child atom has the crude height row sum
\[
  \sum_{d\ne0}\alpha^{|d|}
  =
  \frac{2\alpha}{1-\alpha}.
\]
Optimizing this crude bound means taking \(\alpha\downarrow z\), giving the
collapsed child inventory
\[
  C_{\rm row}(q,z)
  =
  q\,w_*(z)^2\,\frac{2z}{1-z}.
\]
At the target radius \(z=M_q^{-1}\), this is still larger than one for all
integer \(2\le q\le29\).  For example:
\[
\begin{array}{c|c|c|c}
q & M_q & z=M_q^{-1} & C_{\rm row}(q,z)\\
\hline
2 & 2.580088\ldots & 0.387584\ldots & 1.149759\ldots\\
3 & 2.815707\ldots & 0.355151\ldots & 1.314656\ldots\\
4 & 3 & 1/3 & 1.44
\end{array}
\]
The constant only drops below one at \(q=30\) in this crude diagnostic.

Therefore the desired \(M_q\) bound, especially for \(q=2,3,4\), cannot come
from a scalar \(\ell^\infty\)-type row-sum closure after summing away the
packet structure.  The proof must retain at least one of the following pieces
quantitatively:

* the exponential-generating packet-size fugacity \(\xi\);
* the adjacent-gap hard-core factor \(G_\eta(A)\);
* the killed excess-walk structure, rather than only the harmonic multiplier
  \(w_*\);
* mutual avoidance between packets using the same root column.

This is a useful negative calibration.  The packet norm is not cosmetic; it
is needed to avoid the same overcounting mechanism that broke the free-run
models in Rounds 493--494.
