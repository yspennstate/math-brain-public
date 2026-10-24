# Round 490 fresh-column vertical-run obstruction to the \(\sqrt q+1\) target

Round 490 shows that the Round 487 upper target
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\le \sqrt q+1
\]
is too strong in the low-branching cases \(q=2,3\).  The obstruction is
vertical-run entropy in fresh tree columns.

Start from \((o,u)\), the outward neighbor of \((o,u-1)\), and use only
outward tree steps.  After each outward tree step, take a monotone vertical
run in the new tree column.  Since each tree column is visited only once, the
vertical direction can change from column to column without revisiting a
vertex.  Let
\[
  e=d_T(o,v)+z-u
\]
be the excess above the annular boundary, with \(u\) large enough that
\(z\ge0\) throughout.  The path is in the exterior exactly when \(e\ge0\),
and it exits to the annular boundary when \(e=0\).

After endpoint \(L^2\) normalization, an outward tree step carries weight
\(\sqrt q\).  The step inventory for one fresh-column block, with \(z\)
marking length and \(w\) marking excess, is
\[
  B_q(z,w)
  =
  \sqrt q\,z\,w
  \left(
    1+\frac{zw}{1-zw}+\frac{z/w}{1-z/w}
  \right).
\]
The three terms correspond to no vertical run, an upward run, and a downward
run.  Positive excursions built from this block inventory give annular
self-avoiding paths.

The excursion growth is governed by the standard critical equations
\[
  B_q(z,w)=1,\qquad \partial_w B_q(z,w)=0.
\]
Solving gives
\[
  z^{-1}=\Xi_q=\sqrt{1+4\sqrt q}.
\]
Hence
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  \Xi_q
  =
  \sqrt{1+4\sqrt q}.
\]

Comparison with the product-shuffle scale:
\[
  \Xi_q\le\sqrt q+1
  \quad\Longleftrightarrow\quad
  q\ge4.
\]
Thus the \(\sqrt q+1\) upper target can only be correct for \(q\ge4\); it is
false for \(q=2,3\).

The corrected target scale for \(T_d\square\mathbb Z\) is therefore
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \le
  \max\{\sqrt q+1,\sqrt{1+4\sqrt q}\}.
\]
This would still imply the annular gap.  For \(q\ge4\), the right-hand side
is \(\sqrt q+1<q\le1/\pc\).  For \(q=3\), it is
\(\sqrt{1+4\sqrt3}<3\le1/\pc\).  For \(q=2\), it is
\[
  \sqrt{1+4\sqrt2}=2.5800880313\ldots
  <
  3.0523003446\ldots
  \le
  1/\pc
\]
by the column-cluster comparison from Round 486.

This correction clarifies the role of Round 489: vertical-run entropy is not
a technical nuisance; it changes the sharp low-branching upper scale.
