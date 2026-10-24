# Round 127 log

## Goal

Turn the one-gate product obstruction into a high-gate layer with pointwise
\(K\)-mass lower bounds.

## Result

Added `lem:high-one-gate-layer-extraction`.  If
\[
  \mathcal J_{p,r}^I(x,K,Z,a)\ge L
  \qquad\text{and}\qquad
  \sum_{z\in Z}\tau_p(x,a_z)\le\bar\chi_p,
\]
then the set
\[
  Z^\sharp=
  \left\{z:
    \sum_{\substack{y\in K\\d(y,z)\in I}}\tau_p(y,a_z)
    \ge \frac{L}{2\bar\chi_p}
  \right\}
\]
satisfies
\[
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)\ge \frac{L}{2\bar\chi_p}.
\]

Applied to the one-gate obstruction, this gives
\[
  \kappa_j(p)=
  \frac{p^{2r_p}\sigma_j^3}{16\Delta^3}\bar\chi_p^{1-4\theta}
\]
and a subfan \(Z^\sharp\) with
\[
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)\ge\kappa_j(p),
\]
while every \(z\in Z^\sharp\) satisfies
\[
  \sum_{\substack{y\in K\\d(y,z)\in(2^j,2^{j+1}]}}\tau_p(y,a_z)
  \ge\kappa_j(p).
\]

## Interpretation

The obstruction is now a high one-gate layer: a root-visible set of disjoint
boundary gates, each carrying large annular \(K\)-mass.  This is closer to a
finite-set incidence obstruction than to the original two-replica square mass.
