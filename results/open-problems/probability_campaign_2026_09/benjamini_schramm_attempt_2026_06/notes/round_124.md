# Round 124 log

## Goal

Decompose the bilinear fan energy through spherical gates around each remote
center.

## Result

Added:

- `def:gated-fan-energy`
- `lem:gate-decomposition`
- `cor:gated-fan-obstruction`
- `prop:gate-energy-exclusion-criterion`

For \(r<\inf I\), the gate decomposition gives
\[
  \mathcal W_p^I(x,K,Z)
  \le
  \mathcal G_{p,r}^I(x,K,Z),
\]
where \(\mathcal G\) sums over sphere gates \(a,b\) with \(d(a,z)=d(b,z)=r\).
The proof uses BK on the first-hit decomposition of paths entering the ball
around \(z\).

With \(r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor\) and
\(\theta<1/4\), the Round 123 obstruction implies
\[
  \mathcal G_{p,r_p}^{(2^j,2^{j+1}]}(x,K,Z_\theta)
  \ge
  \frac{\sigma_j^3}{8\Delta}\bar\chi_p^{2-2\theta}.
\]

## Interpretation

The obstruction is now pushed out to disjoint logarithmic gate spheres.  A
future proof can try to bound the total gate energy across those disjoint
balls rather than working directly with connections into the remote centers.
