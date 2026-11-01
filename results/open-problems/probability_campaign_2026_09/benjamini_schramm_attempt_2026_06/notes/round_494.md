# Round 494 signed run inventory still overcounts without support memory

Round 494 tests the next natural refinement after Round 493 and shows it is
still too crude.

Instead of counting fixed-height tree runs only by length, track their signed
change in rooted tree depth.  With \(s=\sqrt q\), the Haagerup-weighted
inventory of a nonempty tree run is
\[
  T_s(z,w)
  =
  \sum_{m\ge1}(sz)^m\sum_{j=0}^m w^{m-2j}
  =
  \frac{1}{(1-szw)(1-sz/w)}-1.
\]
The signed vertical-run inventory is
\[
  V(z,w)=\frac{zw}{1-zw}+\frac{z/w}{1-z/w}.
\]

If one ignores support-tree memory and allows signed tree runs and vertical
runs to concatenate freely, the excursion kernel is
\[
  C_s(z,w)=T_s(z,w)+V(z,w).
\]
The critical equations \(C_s=1\), \(\partial_wC_s=0\) have the symmetric
solution \(w=1\).  The resulting rate is very large; for example,
\[
  R_{\rm signed}(2)=6.4859\ldots,\qquad
  R_{\rm signed}(3)=7.4914\ldots.
\]
This is far above both the corrected target \(M_q\) and the available
inverse-\(\pc\) benchmarks.

The reason is structural.  A signed tree run inventory forgets which support
tree edges have already been used at which heights.  It therefore permits
successive fixed-height tree runs to reuse tree columns and tree edges as if
they were fresh, even when the corresponding product vertices would already
have been visited.  The annular excess constraint alone cannot repair this
overcount.

Thus the upper proof cannot be based only on an excursion kernel in the
scalar excess variable
\[
  e=d_T(o,v)+|z|-u.
\]
It must retain at least enough support-tree memory to distinguish:

1. fresh-edge moves, where vertical-run entropy of Round 490 is real;
2. repeated-edge moves, where crossing heights are constrained by the
   previously used height set \(H_e\);
3. transitions between these two regimes.

This strengthens the Round 491 roadmap: the corrected master target \(M_q\)
requires a support-memory transfer, not merely a signed run/excess transfer.
