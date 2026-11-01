# Round 114 log

## Goal

Separate the incidence obstruction into a finite-window alternative.

## Result

Added `prop:finite-window-incidence-alternative`.

For fixed \(\alpha>0\), window length \(H\), and tail start \(J\), failure of
far-leg tightness yields near-critical \(p\) and macroscopic \(K\) such that
either the weighted annular square mass has moved beyond the window,
\[
  \sum_{j>J+H}2^{\alpha(j-J)}
  \mathcal R_p^{(2^j,2^{j+1}]}(K)/\bar\chi_p
  \ge c/2,
\]
or the window itself has many deterministic high-incidence centers,
\[
  \sum_{j=J}^{J+H}2^{\alpha(j-J)}
  \frac{|\mathcal N^{(2^j,2^{j+1}]}(K,\lambda_j\bar\chi_p)|}{|K|}
  \ge c/4.
\]

For fixed \(H\), the incidence thresholds \(\lambda_j\bar\chi_p\) can be
made arbitrarily large by taking \(p\) sufficiently close to \(p_c\).

## Interpretation

The obstruction now splits into two concrete cases: mass keeps escaping to
more distant annuli, or a bounded dyadic window contains many centers with
large deterministic incidence into \(K\).  This avoids relying on trivial
low-threshold layers.
