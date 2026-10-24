# Round 466 branch-switch recursion in \(T_d\square K_2\)

Round 466 isolates the principal recursive family behind the
\(\sqrt{d-1}\) lower bound in \(T_d\square K_2\).

Root \(T_d\) and orient edges away from the root.  Let \(q=d-1\).  For a
tree vertex \(v\), consider paths in the descendant cone of \(v\), in the
two-layer graph, from
\[
  (v,0)\quad\text{to}\quad (v,1),
\]
without visiting the parent of \(v\).  Let \(S(z)\) be the generating
function for such self-avoiding layer-switch paths, weighted by length.

There are two possibilities.

1. Switch directly across the rung at \(v\), contributing \(z\).
2. Choose one of the \(q\) children \(w\) of \(v\), step to \((w,0)\), perform
   a layer-switch path from \((w,0)\) to \((w,1)\) inside the descendant cone
   of \(w\), and step back to \((v,1)\).  This contributes \(qz^2S(z)\).

Thus the principal branch-switch generating function satisfies
\[
  S(z)=z+qz^2S(z),
  \qquad
  S(z)=\frac{z}{1-qz^2}.
\]
Its growth exponent is
\[
  \sqrt q=\sqrt{d-1}.
\]

This exactly matches the out-and-back lower bound from Round 462.  It
explains why the tree contribution to \(\Gamma_{\rm ann}\) appears with a
square root: every outward choice in the tree must be paired with a return in
the other layer.

This is not yet a full upper bound for
\(\Gamma_{\rm ann}(T_d\square K_2)\).  A general exterior return may interact
with boundary vertices of both layer types and may pass through layer-shifted
ancestors before its final boundary edge.  Those cases require additional
types in the recursion.  However, the principal type suggests that a finite
or pushdown system with spectral radius \(\sqrt{d-1}\) may be possible.
