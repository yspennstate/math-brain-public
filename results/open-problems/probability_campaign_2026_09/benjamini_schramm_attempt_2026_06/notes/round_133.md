# Round 133 log

## Goal

Use the localized gate set to improve the logarithmic lower bound on the
obstructing annular scale.

## Result

Added `cor:improved-logarithmic-gate-scale` and
`prop:improved-gate-scale-incidence-criterion`.

The localized obstruction has
\[
  |A|\ge\widehat\kappa_j(p)
  =
  \frac{\sigma_j^3}{16\Delta^3}\bar\chi_p^{1-6\theta},
\]
while all selected gates lie in
\[
  B(x,2^{j+1}+r_p).
\]
If \(2^j<a\log_\Delta\bar\chi_p\), then bounded degree gives
\[
  |A|\le \Delta^{2^{j+1}+r_p+1}
  < \Delta\bar\chi_p^{2a+\theta}.
\]
For \(a<(1-7\theta)/2\), this contradicts the lower bound on \(|A|\) near
criticality, after absorbing the logarithmic loss from \(\sigma_j\).

Therefore the obstruction can be chosen with
\[
  2^j\ge a\log_\Delta\bar\chi_p
  \qquad
  \text{for every }a<(1-7\theta)/2.
\]

## Interpretation

The obstruction is not merely logarithmic at scale \(1/4\log_\Delta\bar\chi_p\).
After localization, the scale is almost
\((1/2)\log_\Delta\bar\chi_p\) when \(\theta\) is small.
