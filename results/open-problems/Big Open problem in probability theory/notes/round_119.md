# Round 119 log

## Goal

Keep the actual witness structure in the logarithmic annular obstruction,
rather than only keeping the resulting volume lower bound.

## Result

Added `cor:logarithmic-backscatter-fan`.

If far-leg tightness fails and \(G\) has maximum degree at most
\(\Delta\ge2\), then for every \(\eta>0\) and near-critical \(p_0\) there are
\(p\in[p_0,p_c)\), a finite set \(K\), an annulus
\(I_j=(2^j,2^{j+1}]\), a root \(x\in K\), and a set \(Z\) such that
\[
  2^j\ge \frac14\log_\Delta\bar\chi_p
\]
and, with
\[
  \sigma_j=\frac{\epsilon}{2}(1-2^{-\eta/2})^2 2^{-\eta(j-J)},
\]
\[
  |Z|\ge \frac{\sigma_j^2}{4}\bar\chi_p,
  \qquad d(x,z)\in I_j\quad(z\in Z).
\]
Every \(z\in Z\) also satisfies
\[
  \sum_{\substack{y\in K\\d(y,z)\in I_j}}\tau_p(y,z)
  \ge \frac{\sigma_j}{2}\bar\chi_p,
\]
and hence has at least \((\sigma_j/2)\bar\chi_p\) annular incidences with
\(K\).

## Interpretation

The remaining obstruction is a logarithmic-distance fan/backscatter pattern:
one root sees many remote annular centers, and each center sees
susceptibility-scale mass back into the same finite set.  This should be the
next target for any nonamenability, spectral, or two-replica decay input.
