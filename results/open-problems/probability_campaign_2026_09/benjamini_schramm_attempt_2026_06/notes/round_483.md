# Round 483 corrected bubble subfamily gives \(\sqrt{q+1}\)

Round 483 extracts a clean explicit lower bound from the corrected
repeated-bubble variational target.

Start at \((o,u)\), the outward neighbor of \((o,u-1)\).  Choose a branch
path of tree depth \(R\), move outward along it at fixed line height \(u\),
then return to \(o\) at higher line height \(u+S\) by first stepping upward
at the leaf and then interleaving the remaining upward steps with the inward
tree steps.  This contributes
\[
  q^R\binom{R+S}{R}
\]
up to polynomial factors, has length \(2R+S\), and ends at \((o,u+S)\).

Now pay the missing exit cost.  Choose a terminal tree depth \(T=o(R)\)
in a branch avoiding the bubble path at the top height; in fact \(T=1\)
already suffices if the first tree edge is not the bubble's first edge.  Move
outward to that terminal column and descend from height \(u+S\) to height
\(u-T\).  This adds length
\[
  S+2T=S+o(R),
\]
keeps the path self-avoiding by using a fresh terminal column, and ends at a
vertex of radius \(u\) adjacent to the boundary sphere.  The terminal
endpoint normalization is only \(e^{o(R)}\).

Thus the exponential rate of this valid annular family is
\[
  \left(q^R\binom{R+S}{R}\right)^{1/(2R+2S+o(R))}.
\]
Put \(S=aR\).  The logarithmic rate is
\[
  \frac{\log q+(1+a)H(1/(1+a))}{2(1+a)}.
\]
This is maximized at
\[
  a=\frac1q,
\]
and the maximum value is
\[
  \sqrt{q+1}.
\]

Therefore
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  \sqrt{q+1}
  =
  \sqrt d.
\]
Combining with Round 479 gives the current explicit lower calibration
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  \max\{2q^{1/4},\sqrt{q+1}\}.
\]

The corrected variational expression from Round 482 may still improve this
slightly by taking terminal depth \(T\) proportional to \(R\), but
\(\sqrt{q+1}\) is the clean paid-exit bubble bound.  It remains below the
global product-shuffle scale \(\sqrt q+1\).
