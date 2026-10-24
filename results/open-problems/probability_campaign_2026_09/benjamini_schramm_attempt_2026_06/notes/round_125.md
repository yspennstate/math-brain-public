# Round 125 log

## Goal

Remove the remaining spherical averaging from the gated fan obstruction.

## Result

Added the point-gated fan energy
\[
  \mathcal H_{p,r}^I(x,K,Z,a,b)
  =
  \sum_{z\in Z}\tau_p(x,a_z)\tau_p(a_z,z)\tau_p(b_z,z)
  \sum_{\substack{y\in K\\d(y,z)\in I}}\tau_p(y,b_z).
\]

The gate-pair selection lemma says that if
\[
  M_r=\sup_z |\{v:d(v,z)=r\}|,
\]
then some gate maps \(a,b:Z\to V\) satisfy
\[
  \mathcal H_{p,r}^I(x,K,Z,a,b)
  \ge
  M_r^{-2}\mathcal G_{p,r}^I(x,K,Z).
\]

At the logarithmic gate radius
\[
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor,
\]
we have \(M_{r_p}\le\Delta\bar\chi_p^\theta\).  Combining this with the
gated fan obstruction gives
\[
  \mathcal H_{p,r_p}^{(2^j,2^{j+1}]}(x,K,Z_\theta,a,b)
  \ge
  \frac{\sigma_j^3}{8\Delta^3}\bar\chi_p^{2-4\theta}.
\]

## Interpretation

The obstruction can be forced through one ordered pair of boundary gates in
each disjoint logarithmic ball.  A future exclusion proof can now target
point-gated pairs rather than averages over whole spheres.
