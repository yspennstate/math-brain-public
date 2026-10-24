# Round 085 log

## Goal

Check that the tree-grid layer-square estimate is not an automatic consequence
of periodic separators and susceptibility normalization.

## Amenable sanity check

On \(G=\mathbb Z\), \(p_c=1\) and
\[
  \tau_p(x,y)=p^{|x-y|},
  \qquad
  \bar\chi_p=\frac{1+p}{1-p}.
\]
Fix a grid spacing \(L\) and take \(K=\{1,\ldots,N\}\) with
\(N\gg (1-p)^{-1}\).  For any residue class \(S_a=\{z:z\equiv a\pmod L\}\),
a positive fraction of the points of \(K\cap S_a\) are far from the endpoints
of \(K\), and at each such point
\[
  T_p\mathbf 1_K(z)=\sum_{x=1}^N p^{|z-x|}
  \asymp \bar\chi_p .
\]
Thus
\[
  \sum_{z\in S_a}(T_p\mathbf 1_K(z))^2
  \gtrsim
  \frac{N}{L}\bar\chi_p^2,
\]
and therefore
\[
  \frac{1}{\bar\chi_p |K|}
  \sum_{z\in S_a}(T_p\mathbf 1_K(z))^2
  \gtrsim
  \frac{\bar\chi_p}{L}.
\]
For every fixed \(L\), this diverges as \(p\uparrow1\).

## Conclusion

The layer-square target fails even with perfectly regular periodic separators
on an amenable graph.  A proof for nonamenable product-like graphs must use
the nonamenable direction in a genuine way, matching the role of
backscattering in Hutchcroft--Pan rather than relying on separator averaging
alone.
