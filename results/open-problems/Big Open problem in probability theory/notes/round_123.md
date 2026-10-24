# Round 123 log

## Goal

Package the root-weighted separated fan as a bilinear energy obstruction.

## Result

Added `def:rooted-fan-energy` and
`prop:fan-energy-exclusion-criterion`, and strengthened
`cor:weighted-separated-fan`.

For a root \(x\), finite set \(K\), annulus \(I\), and remote set \(Z\), define
\[
  \mathcal W_p^I(x,K,Z)
  =
  \sum_{z\in Z}\tau_p(x,z)
  \sum_{\substack{y\in K\\d(y,z)\in I}}\tau_p(y,z).
\]

The weighted separated fan from Round 122 satisfies
\[
  \mathcal W_p^{I_j}(x,K,Z_\theta)
  \ge
  \frac{\sigma_j^3}{8\Delta}\bar\chi_p^{2-2\theta}.
\]
Therefore, excluding separated fans with this energy lower bound is enough to
force
\[
  \mathcal R_p^*/\bar\chi_p\to0,
\]
and hence \(p_c(G)<p_{2\to2}(G)\) under the existing mean-field input.

## Interpretation

The obstruction is now a bilinear two-point convolution through many separated
remote centers.  This is a cleaner analytic target than the raw combinatorial
fan formulation.
