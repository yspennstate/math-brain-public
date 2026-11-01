# Round 510 finite low-branching residual target

Round 509 shows that a plain two-sided tilted row sum fails only in the
low-branching cases \(q=2,\ldots,6\).  This turns the remaining scalar
obstruction into a finite residual target.

Use the same packet constant \(C=2\), but choose a weaker span decay
\[
  \alpha=0.99.
\]
This still gives \(\alpha<1\), while increasing the margin left after the
monotone trace contribution.  At \(z=M_q^{-1}\), the monotone transform from
Round 508 gives:
\[
\begin{array}{c|c|c}
q & H_{q,z,0.99}(2) & 2-H_{q,z,0.99}(2)\\
\hline
2 & 1.309916\ldots & 0.690084\ldots\\
3 & 1.114926\ldots & 0.885074\ldots\\
4 & 0.996553\ldots & 1.003447\ldots\\
5 & 0.818365\ldots & 1.181635\ldots\\
6 & 0.701502\ldots & 1.298498\ldots
\end{array}
\]

For \(q\ge7\), the two-sided tilted scalar supersolution from Round 509 has
positive discriminant, so nonmonotone traces are already compatible with a
coarse scalar closure.  Hence the only scalar trace obstruction left by the
current diagnostics is:

> Prove that the normalized contribution of valid nonmonotone trace families
> for \(q=2,\ldots,6\), with at least one height reversal, is bounded by the
> corresponding margin \(2-H_{q,z,0.99}(2)\).

This residual target should use the structure that the two-sided tilt
discarded.  A nonmonotone height trace has total variation
\[
  V=\sum_i |h_{i+1}-h_i|
\]
strictly larger than endpoint span \(S=|h_m-h_0|\); in fact \(V-S\ge2\).
Each reversal therefore carries extra metric cost.  In the full trace model,
reversals are further constrained by:

* distinct portal heights in the shared root column;
* vertical intervals being adjacent-gap matchings;
* the annular excess process staying nonnegative;
* mutual avoidance between packet traces.

The next proof attempt should be a reversal-cluster expansion: keep the
monotone bridge controlled by Round 508, and attach nonmonotone reversal
clusters weighted by their excess variation \(V-S\).  The finite list
\(q=2,\ldots,6\) and the explicit margins above make this a concrete
checkable inequality rather than an open-ended entropy problem.
