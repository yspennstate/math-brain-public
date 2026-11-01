# Round 511 neutral reversal-bubble inventory closes the scalar margins

Round 510 leaves a finite residual problem: control nonmonotone traces for
\(q=2,\ldots,6\).  A reversal-cluster calculation gives a plausible scalar
closure with explicit room.

Keep
\[
  C=2,\qquad \alpha=0.99,\qquad z=M_q^{-1},
\]
and write
\[
  c_q(z)=qz^2w_*(z)^2.
\]
Consider a neutral reversal bubble attached to a monotone bridge.  It leaves
the current monotone frontier, moves backward in height, and then returns to
the frontier.  The output endpoint span is unchanged, so the extra variation
is paid by raw \(z\)-weights, not by \(z/\alpha\).  Put
\[
  P_0(z)=\frac{z}{1-z}.
\]
The two legs of the bubble have inventory \(P_0(z)^2\).

The no-consecutive-vertical rule forces at least one of the two legs to be a
child atom.  A child leg carries the recursive packet factor \(C\) and the
child cost \(c_q(z)\).  Thus the color inventory of the two legs, excluding
the forbidden vertical-vertical pair, is
\[
  (1+Cc_q(z))^2-1.
\]
The neutral reversal-bubble inventory is therefore
\[
  D_q(z)
  =
  P_0(z)^2\bigl((1+Cc_q(z))^2-1\bigr).
\]
Allowing any number of independent such bubbles gives the geometric factor
\[
  \frac{D_q(z)}{1-D_q(z)}.
\]

The numeric check is favorable in every residual case:
\[
\begin{array}{c|c|c|c|c}
q & H_{q,z,0.99}(2) & 2-H & D_q & H\,D_q/(1-D_q)\\
\hline
2 & 1.309916\ldots & 0.690084\ldots
  & 0.248450\ldots & 0.433037\ldots\\
3 & 1.114926\ldots & 0.885074\ldots
  & 0.210147\ldots & 0.296636\ldots\\
4 & 0.996553\ldots & 1.003447\ldots
  & 0.185600\ldots & 0.227113\ldots\\
5 & 0.818365\ldots & 1.181635\ldots
  & 0.140046\ldots & 0.133273\ldots\\
6 & 0.701502\ldots & 1.298498\ldots
  & 0.110034\ldots & 0.086733\ldots
\end{array}
\]
So
\[
  H_{q,z,0.99}(2)\frac{D_q(z)}{1-D_q(z)}
  <
  2-H_{q,z,0.99}(2)
\]
for every \(q=2,\ldots,6\).

This gives a concrete sufficient combinatorial lemma:

> Every valid nonmonotone trace family can be injected, with no larger
> weight, into a monotone trace family decorated by a sequence of neutral
> reversal bubbles whose total inventory is bounded by \(D_q/(1-D_q)\).

If this lemma is proved, the scalar packet transform closes at \(C=2\),
\(\alpha=0.99\), and \(z=M_q^{-1}\) for all integer \(q\ge2\).  The remaining
task is purely combinatorial: justify the bubble decomposition under
distinct portal heights, adjacent-gap vertical matchings, and packet-family
avoidance.
