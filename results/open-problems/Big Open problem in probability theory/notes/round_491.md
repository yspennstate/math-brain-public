# Round 491 corrected master upper target for \(T_d\square\mathbb Z\)

Round 491 replaces the over-strong Round 487 upper target with the corrected
scale suggested by Round 490.

Let
\[
  M_q=
  \max\{\sqrt q+1,\sqrt{1+4\sqrt q}\}.
\]
The new upper target is
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\le M_q.
\]
This target is compatible with all lower-bound families currently identified:

* product-shuffle and stack-return mechanisms are expected at scale
  \(\sqrt q+1\);
* fresh-column vertical-run excursions from Round 490 have scale
  \(\sqrt{1+4\sqrt q}\);
* the corrected repeated-bubble family from Rounds 482--485 lies below these
  scales.

It is also still sufficient for the desired annular gap.  If \(q\ge4\), then
\[
  M_q=\sqrt q+1<q\le1/\pc(T_d\square\mathbb Z).
\]
If \(q=3\), then
\[
  M_3=\sqrt{1+4\sqrt3}<3\le1/\pc(T_d\square\mathbb Z).
\]
If \(q=2\), then Round 486 gives
\[
  M_2=\sqrt{1+4\sqrt2}
  <
  3.0523003446\ldots
  \le
  1/\pc(T_3\square\mathbb Z).
\]

The corresponding operator target is
\[
  \frac{
    \langle\nu_U,C_n^{X_u}\nu_V\rangle
  }{\sqrt{|U||V|}}
  \le
  e^{o(n)}M_q^n
\]
uniformly over roots, levels, and boundary subsets \(U,V\).

The missing combinatorial proof should encode every annular exterior SAW by
two coupled excursion mechanisms:

1. a stack-return mechanism, where endpoint \(L^2\) averaging supplies the
   tree Haagerup factor and the expected scale is \(\sqrt q+1\);
2. a fresh-column vertical-run mechanism, where monotone vertical runs in
   never-reused tree columns are controlled by the block inventory
   \[
     B_q(z,w)=
     \sqrt q\,z\,w
     \left(1+\frac{zw}{1-zw}+\frac{z/w}{1-z/w}\right)
   \]
   and the scale is \(\sqrt{1+4\sqrt q}\).

The key remaining issue is interaction.  A path can alternate between stack
returns and fresh-column runs.  The desired upper proof must show that this
alternation does not create a third exponential scale larger than \(M_q\).
Equivalently, transitions between the two mechanisms must be chargeable to
the same annular excess budget \(d_T(o,v)+|z|-u\) and to the same endpoint
\(L^2\) tree averaging.
