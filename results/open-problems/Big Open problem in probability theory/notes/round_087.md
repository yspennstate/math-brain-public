# Round 087 log

## Goal

Test whether periodic tree-level separators give a useful small operator norm
for restricted sphere kernels.

## Result

Added `prop:periodic-tree-restriction-lower`.

Let \(T_d\) be rooted at \(o\), \(q=d-1\), and let
\[
  S_r^{(L)}=\{x: d(o,x)\equiv r\pmod L\}.
\]
If \(R_n\) is the distance-\(n\) sphere kernel, then
\[
  \|M_{S_r^{(L)}}R_n\|_{2\to2}\ge q^{n/2}
\]
for every \(L,r\), and every \(n\ge1\).

The proof is a one-vector test.  Choose a non-root vertex \(y\) with
\[
  d(o,y)+n\equiv r\pmod L.
\]
All \(q^n\) descendants of \(y\) at distance \(n\) lie in \(S_r^{(L)}\), so
\[
  \|M_{S_r^{(L)}}R_n\mathbf 1_{\{y\}}\|_2=q^{n/2}.
\]

## Consequence

The full tree sphere bound is
\[
  \|R_n\|_{2\to2}\le C_d(n+1)q^{n/2}.
\]
Thus periodic level restrictions can at best remove the Haagerup polynomial
factor in a pure operator-norm estimate; they cannot give a density gain
depending on \(L\).

This means `prop:restricted-shell-layer-square` is useful but not enough by
itself.  The separator-square route must exploit the finite test set, averaging
over shifts before taking a supremum over functions, or a percolation-specific
backscattering estimate for the fibre masses.
