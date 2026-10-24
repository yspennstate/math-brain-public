# Round 487 sharp upper target for \(T_d\square\mathbb Z\)

Round 487 turns the one-ended product calibration into a concrete upper-bound
target.

Let \(q=d-1\).  The natural target is
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\le \sqrt q+1.
\]
This is sharp relative to the global product-shuffle lower bound and is
consistent with all portal lower-bound families found so far.

It is also strong enough for the desired annular gap.  If \(q\ge3\), then
\[
  \sqrt q+1<q\le 1/\pc(T_d\square\mathbb Z),
\]
using the embedded copy of \(T_d\).  For \(q=2\), Round 486 gives
\[
  1/\pc(T_3\square\mathbb Z)
  \ge
  3.0523003446\ldots
  >
  \sqrt2+1.
\]
Thus the single estimate \(\Gamma_{\rm ann}\le\sqrt q+1\) would prove the
annular gap for every \(T_d\square\mathbb Z\), \(d\ge3\).

A precise sufficient estimate is the following tree-line split.  Let
\(C_{n,a}^{X_u}\) count self-avoiding paths in the exterior \(X_u\) of total
length \(n\), with exactly \(a\) tree-coordinate steps and \(n-a\)
\(\mathbb Z\)-steps.  It would be enough to prove, uniformly over roots,
levels, and boundary subsets \(U,V\),
\[
  \frac{
    \langle \nu_U,C_{n,a}^{X_u}\nu_V\rangle
  }{\sqrt{|U||V|}}
  \le
  e^{o(n)}
  \binom{n}{a}q^{a/2}.
\]
Summing over \(a\) gives
\[
  \frac{
    \langle \nu_U,C_n^{X_u}\nu_V\rangle
  }{\sqrt{|U||V|}}
  \le
  e^{o(n)}(\sqrt q+1)^n,
\]
and hence \(\Gamma_{\rm ann}\le\sqrt q+1\).

The obstacle is now clearly localized.  A naive count pays \(q^a\) for tree
steps.  The required estimate asks for Haagerup-type square-root tree
branching \(q^{a/2}\), even though annular paths may backtrack in the tree at
different \(\mathbb Z\)-heights.  The self-avoidance condition must force
those backtracks to be paid by line motion or by endpoint \(L^2\) averaging.

The portal lower bounds calibrate this target:

* one-portal staircases realize \(2q^{1/4}\), below \(\sqrt q+1\);
* corrected repeated bubbles realize \(\Lambda_q=\sqrt q+O(q^{-1/2})\);
* none of the identified families exceeds the proposed \(\sqrt q+1\) upper
  scale.

Thus \(T_d\square\mathbb Z\) has been reduced to a specific annular
Haagerup-with-height-memory estimate.
