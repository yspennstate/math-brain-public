# Round 129 log

## Goal

Convert the expanded gate-annulus mass lower bound into deterministic
incidence.

## Result

Added `cor:root-weighted-gate-incidence-obstruction` and
`prop:gate-incidence-exclusion-criterion`.

The expanded gate-annulus obstruction gives
\[
  \sum_{\substack{y\in K\\d(y,a_z)\in I_{j,p}^{\rm gate}}}\tau_p(y,a_z)
  \ge \kappa_j(p)
\]
for every selected gate.  Since \(\tau_p(y,a_z)\le1\), this implies
\[
  |\{y\in K:d(y,a_z)\in I_{j,p}^{\rm gate}\}|
  \ge \kappa_j(p).
\]

The root-weighted part remains:
\[
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)\ge\kappa_j(p).
\]

## Interpretation

The obstruction is now mostly combinatorial: selected boundary gates are
root-visible in total, and each gate has many deterministic incidences with
\(K\) in the expanded annulus.
