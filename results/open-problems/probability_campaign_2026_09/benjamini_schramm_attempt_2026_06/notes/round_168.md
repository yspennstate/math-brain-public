# Round 168

## Goal

Add the deterministic two-point-mass counterpart of the volume-sensitive
large-scale open-tube dichotomy.

## Result

Added
`cor:volume-sensitive-large-scale-tube-mass-dichotomy`.

Under the volume-sensitive endpoint-anchor hypotheses, the same large-scale
buffered obstruction can be chosen with
\[
  2^j>B\log_\Delta\bar\chi_p
\]
and, for every \(b>0\) with
\[
  \rho=1-20\theta-3\eta b>0,
\]
either
\[
  2^j>\bar\chi_p^b,
\]
or
\[
  \sum_{i=1}^t \tau_p(a_i,z_i)
  \ge
  d_{\epsilon,\eta,J,\Delta}\bar\chi_p^\rho,
\]
where
\[
  d_{\epsilon,\eta,J,\Delta}
  =
  \frac{1}{432\Delta^8}
  \left[\frac{\epsilon}{2}(1-2^{-\eta/2})^2\right]^3
  2^{3\eta J}.
\]

## Proof mechanism

Choose the volume-sensitive large-scale buffered tube configuration.  If the
scale is not polynomial, then \(j\le b\log_2\bar\chi_p\), which gives the same
lower bound on \(\sigma_j^3\) as in Round 167.  Near criticality \(p\ge
1/\Delta\), and each deterministic tube path has length \(r_p\), so
\[
  \tau_p(a_i,z_i)\ge p^{r_p}\ge\Delta^{-r_p}\ge\bar\chi_p^{-\theta}.
\]
Multiplying this by the buffered tube count
\[
  t\ge\frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-19\theta}
\]
gives the displayed polynomial tube-mass lower bound.

## Interpretation

Round 167 gives a high-probability statement about many opened short tubes.
Round 168 records the deterministic two-point version at the same
volume-sensitive large scale.  This is a cleaner input for later annular
operator comparisons, because it avoids carrying an auxiliary sampling event.
