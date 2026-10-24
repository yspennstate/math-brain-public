# Round 501 two-component gap weight

The excess-weighted packet norm still needs a concrete gap factor.  One
factor is not enough, because there are two different height-summation
problems.

For a packet
\[
  \Pi=((a_1,b_1),\ldots,(a_k,b_k)),
\]
let
\[
  L(\Pi)=\sum_{j=1}^k |a_j-b_j|
\]
be the total span of its boundary pairs.  Also let
\[
  A(\Pi)=\{a_1,b_1,\ldots,a_k,b_k\}
      =\{x_0<\cdots<x_m\}
\]
be the ordered portal set, and let \(g_i=x_{i+1}-x_i\) be its adjacent gaps.

The pair-span term controls summation over child jumps.  A child piece from
height \(a\) to height \(b\) must contain at least \(|a-b|\) line steps, so
its length generating function carries a factor at most \(z^{|a-b|}\).  In a
majorant norm it is natural to reserve a slightly weaker decay
\[
  \alpha^{L(\Pi)},\qquad z<\alpha<1.
\]
This makes the time-ordered portal sums finite, because the trace word is a
connected chain of height jumps.

The adjacent-gap term controls root-column vertical intervals.  For a fixed
ordered portal set \(A=\{x_0<\cdots<x_m\}\), Round 498 showed that vertical
runs form a hard-core matching on adjacent gaps.  Hence
\[
  \sum_{M\ \mathrm{matching}}
  \prod_{\{x_i,x_{i+1}\}\in M} z^{g_i}
  \le
  \prod_{i=0}^{m-1}(1+z^{g_i}).
\]
Thus choose \(z<\eta<1\) and include the gap gas
\[
  G_\eta(A)=\prod_{i=0}^{m-1}(1+\eta^{g_i}).
\]

The resulting candidate is
\[
  \Phi_{\alpha,\eta}(\Pi)
  =
  \alpha^{L(\Pi)}G_\eta(A(\Pi)).
\]
Together with the excess weight from Round 500, the norm becomes
\[
  \|E\|_{z,\xi,w,\alpha,\eta}
  =
  \sum_{k\ge0}\frac{\xi^k}{k!}
  \sup_{\Pi:|\Pi|=k}
  \frac{E_z(\Pi)}
       {w^{E_r(\Pi)}\alpha^{L(\Pi)}G_\eta(A(\Pi))}.
\]

This factorization separates the two uses of one-dimensional geometry:

1. \(\alpha^{L(\Pi)}\) is a summable kernel along the time-ordered child
   jumps.
2. \(G_\eta(A)\) dominates the hard-core matching partition function of
   vertical root-column intervals after the portal heights are sorted.

The remaining closure problem is now finite-parameter in spirit.  For
\[
  z<M_q^{-1},
\]
one needs to choose \(w,\xi,\alpha,\eta\) with \(B_q(z,w)<1\) and
\(z<\alpha,\eta<1\) so that the root trace transform is bounded in this norm.
The old free-run overcounts correspond to dropping either the pair-span decay
or the hard-core adjacent-gap factor.
