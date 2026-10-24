# Round 089 log

## Goal

Tie the new two-replica profile \(\mathcal R_p(K)\) to actual percolation
objects and differential inequalities.

## Cluster Interpretation

Let \(\omega_1,\omega_2\) be independent Bernoulli-\(p\) configurations, and
let \(C_i(z)\) be the cluster of \(z\) in \(\omega_i\).  Added
`lem:two-replica-cluster-interpretation`:
\[
  \bar\chi_p|K|\mathcal R_p(K)
  =
  \sum_z
  \mathbb E_p^{\otimes2}
  \bigl[
    |K\cap C_1(z)|\,|K\cap C_2(z)|
  \bigr].
\]
Thus \(\mathcal R_p(K)\) measures whether two independent clusters rooted at
the same vertex \(z\) can both collect a large amount of mass from \(K\).

## Differential Inequality

Added `prop:two-replica-differential`.  If the maximum degree is \(\Delta\),
then for every finite non-empty \(K\) and \(0\le p\le q<p_c\),
\[
  \frac{S_q^{\rm amb}(K)}{|K|}
  \le
  \frac{S_p^{\rm amb}(K)}{|K|}
  +
  \Delta\int_p^q \bar\chi_s\,\mathcal R_s(K)\,ds,
\]
where
\[
  S_p^{\rm amb}(K)=\sum_{x,y\in K}\tau_p(x,y).
\]
The proof works in finite volume, uses Russo's formula and BK to get
\[
  \frac{d}{dp}T_p^W\le T_p^W A_WT_p^W,
\]
then tests against \(\mathbf 1_K\) and uses
\[
  \langle h,A_Wh\rangle\le \Delta\|h\|_2^2.
\]

## Significance

The two-replica target is now connected to standard percolation tools.  A
future proof can try to bound \(\mathcal R_p^*\) using sharpness,
backscattering, or differential inequalities rather than treating it as a
purely spectral condition.
