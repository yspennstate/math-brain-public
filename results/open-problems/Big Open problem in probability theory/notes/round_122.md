# Round 122 log

## Goal

Strengthen the separated fan obstruction so the root retains substantial
two-point mass into the separated remote centers.

## Result

Added:

- `lem:weighted-separated-subfan-extraction`
- `cor:weighted-separated-fan`
- `def:root-weighted-separated-fans`
- `prop:weighted-fan-exclusion-criterion`

The weighted packing lemma says that if \(a_z\ge0\) on a finite set \(Z\),
then there is a \(2r\)-separated subset \(Z_r\) with
\[
  \sum_{z\in Z_r}a_z
  \ge
  \frac{1}{V_{2r}}\sum_{z\in Z}a_z.
\]

Applied with \(a_z=\tau_p(x,z)\), failure of far-leg tightness produces a
root-weighted separated fan with
\[
  \sum_{z\in Z_\theta}\tau_p(x,z)
  \ge
  \frac{\sigma_j^2}{4\Delta}\bar\chi_p^{1-2\theta}.
\]
Each selected \(z\) still receives annular mass at least
\((\sigma_j/2)\bar\chi_p\) from \(K\).

## Interpretation

The remaining obstruction now has both spatial separation and root-weighted
two-point mass.  A future exclusion argument can aim directly at remote
weighted sums from one root into many separated logarithmic-scale regions.
