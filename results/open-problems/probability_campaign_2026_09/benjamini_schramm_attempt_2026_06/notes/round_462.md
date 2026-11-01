# Round 462 product out-and-back lower bound for \(\Gamma_{\rm ann}\)

Round 462 corrects the product calibration from Round 461: tree branching can
enter \(\Gamma_{\rm ann}\), although only through a square-root return cost.

Let
\[
  G=T_d\square H
\]
and suppose \(H\) has an edge \(h_0\sim h_1\).  Root at \(x=(o,h_0)\).  Let
\[
  a=(t,h_0)\in S_{u-1}(x)
\]
where \(t\) has tree depth \(u-1\), and let
\[
  y=(t^+,h_0)\in S_u(x)
\]
be the outward tree neighbour along a chosen forward branch.

Choose a self-avoiding forward tree segment of length \(r\) starting from
\(t^+\):
\[
  p_0=t^+,p_1,\ldots,p_r.
\]
There are \((d-1)^r\) such choices up to constants.  From \(y=(p_0,h_0)\),
follow
\[
  (p_0,h_0),(p_1,h_0),\ldots,(p_r,h_0),
  (p_r,h_1),(p_{r-1},h_1),\ldots,(t,h_1).
\]
All vertices in this killed path lie outside \(B_{u-1}(x)\).  The endpoint
\[
  z=(t,h_1)
\]
has distance \(u\) from \(x\), and the final edge to the ancestor
\[
  b=(t_-,h_1)\in S_{u-1}(x)
\]
completes an exterior return.

The killed exterior part from \(y\) to \(z\) has length \(2r+2\) and there
are \((d-1)^r\) choices.  Hence
\[
  \Gamma_{\rm ann}(T_d\square H)\ge \sqrt{d-1}
\]
whenever \(H\) contains an edge.

Combining this with the factor-geodesic staircase from Round 460 gives the
diagnostic lower bound
\[
  \Gamma_{\rm ann}(T_d\square H)
  \ge
  \max\{\sqrt{d-1},\sqrt{g_{\rm geo}(H)}\}.
\]

This is still weaker than the global SAW product lower bound
\[
  \gamma_{\rm SAW,2}(T_d\square H)\ge\sqrt{d-1}+\mu(H),
\]
but the difference is smaller than Round 461 suggested.  The annular exponent
does see tree branching; it sees it with return cost \(2r\), hence as
\(\sqrt{d-1}\), not additively with the factor connective constant.
