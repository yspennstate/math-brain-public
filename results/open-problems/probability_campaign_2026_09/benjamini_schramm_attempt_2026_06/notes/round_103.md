# Round 103 log

## Goal

Tie the new shell-tail criterion back to the existing \(L^2\)-SAW operator
criterion.

## Result

Added `prop:saw-shell-tail`.

If
\[
  \gamma_{\mathrm{SAW},2}(G)<1/p_c(G),
\]
then
\[
  \lim_{R\to\infty}\sup_{p<p_c}
  \sum_{n>R}\|H_{p,n}\|_{2\to2}=0.
\]

The proof uses the union bound
\[
  H_{p,n}(x,y)\le\sum_{m\ge n}p^mC_m(x,y)
\]
and the exponential \(L^2\)-operator bound on the self-avoiding endpoint
kernels \(C_m\).

## Interpretation

The far-leg/shell-tail program is compatible with the old SAW operator route:
the SAW gap gives a uniformly summable shell tail.  The remaining challenge is
to prove shell or far-leg tightness in cases where the global SAW gap is too
crude.
