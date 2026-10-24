# Round 163

Date: 2026-06-09

## Aim

Tighten the later volume-sensitive matched-count scale amplification so that it
uses the new volume-sensitive matched obstruction rather than the older
bounded-degree matched count.

## Main change

Updated
`cor:volume-sensitive-matched-scale-amplification`.

The old version used
\[
  \widehat\kappa_j(p)
  =
  \frac{\sigma_j^3}{16\Delta^3}\bar\chi_p^{1-6\theta}.
\]
The new version starts from
\[
  \widehat\kappa_j^{\rm vol}(p)
  =
  \frac{\sigma_j^3}{16C_{\rm vol}^3}
  \bar\chi_p^{1-2\theta-4\theta\log_\Delta\omega}.
\]
Consequently the scale contradiction now uses the sharper exponent condition
\[
  2B\log_\Delta\omega
  <
  1-2\theta-4\theta\log_\Delta\omega.
\]

## Constant and thinning issue

Starting from the volume-sensitive matched obstruction, the deterministic
packing and independent-set extractions after the matched stage lose at most
\[
  27\Delta^{13r_p+5}.
\]
Thus the final buffered count is at least
\[
  \frac{\sigma_j^3}{432C_{\rm vol}^3\Delta^5}
  \bar\chi_p^{1-15\theta-4\theta\log_\Delta\omega}.
\]
To compare this with the older buffered-tube count
\[
  \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-19\theta},
\]
the corollary now assumes \(\omega<\Delta\).  This gives the exponent margin
\[
  4\theta(1-\log_\Delta\omega)>0,
\]
which absorbs the \(C_{\rm vol}\)-dependent constant near criticality.

## Resulting parameter range

For \(\Delta\ge3\), the tree-volume estimate permits
\[
  \omega=\Delta-1,
\]
so the \(B\)-condition becomes
\[
  B<
  \frac{1-2\theta-4\theta\log_\Delta(\Delta-1)}
       {2\log_\Delta(\Delta-1)}.
\]

## Status

This is still not a full solution.  It improves the scale-amplification input
for the later buffered-tube branch and removes one dependence on the older
bounded-degree matched-count estimate.
