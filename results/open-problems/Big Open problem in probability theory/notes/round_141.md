# Round 141 log

## Goal

Extract a deterministic two-point mass consequence from the buffered tube
configuration.

## Result

Added `cor:buffered-tube-mass-obstruction` and
`prop:buffered-tube-mass-criterion`.

Each selected path \(\gamma_i\) has length \(r_p\) and connects \(a_i\) to
\(z_i\), so
\[
  \tau_p(a_i,z_i)\ge p^{r_p}.
\]
Near criticality, \(p\ge1/\Delta\), and therefore
\[
  p^{r_p}\ge\Delta^{-r_p}\ge\bar\chi_p^{-\theta}.
\]
Combining this with the Round 139 buffered size gives
\[
  \sum_i \tau_p(a_i,z_i)
  \ge
  \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-20\theta}
  =:\kappa_j^{\rm tube}(p).
\]

## Interpretation

The open-tube count from Round 140 has a deterministic two-point version:
the same buffered configuration carries large total two-point mass along the
short gate-to-anchor tubes.  This is a cleaner object for later operator
arguments than the sampled open-tube random variable.
