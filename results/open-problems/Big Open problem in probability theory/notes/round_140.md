# Round 140 log

## Goal

Use independence of the buffered gate tubes to obtain a probabilistic
open-tube count.

## Result

Added `lem:independent-path-opening-count` and
`cor:open-buffered-tube-obstruction`.

If \(\gamma_1,\ldots,\gamma_t\) are pairwise edge-disjoint paths of length
\(r_p\), then
\[
  N_{\rm open}=\#\{i:\gamma_i\text{ is open}\}
\]
is binomial with mean \(t p^{r_p}\), and the Chernoff lower-tail bound gives
\[
  \mathbf P_p(N_{\rm open}<\mu/2)\le e^{-\mu/8}.
\]

For the buffered obstruction, near criticality we can take \(p\ge1/\Delta\).
Thus
\[
  p^{r_p}\ge\Delta^{-r_p}\ge\bar\chi_p^{-\theta}.
\]
Since Round 139 gives
\[
  t\ge
  \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-19\theta},
\]
we get
\[
  \mathbf E_p N_{\rm open}
  \ge
  \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-20\theta}.
\]
With
\[
  \lambda_j^{\rm open}(p)
  =
  \frac{\sigma_j^3}{864\Delta^8}\bar\chi_p^{1-20\theta},
\]
the obstruction satisfies
\[
  \mathbf P_p\bigl(N_{\rm open}\ge\lambda_j^{\rm open}(p)\bigr)
  \ge
  1-\exp[-\lambda_j^{\rm open}(p)/4].
\]

## Interpretation

This is the first step after the deterministic packing reductions that uses
percolation independence.  The remaining obstruction can now be read as a
configuration where many local gate-to-anchor tubes open simultaneously with a
controlled lower-tail probability.  The next target is to use those open tubes
to push annular endpoint mass back to the separated anchors without losing the
buffered disjointness.
