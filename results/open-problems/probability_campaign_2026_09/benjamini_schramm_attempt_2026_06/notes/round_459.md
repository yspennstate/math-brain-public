# Round 459 annular gap plus endpoint support is a conditional endpoint theorem

Round 459 states the current spread-return endpoint as a conditional theorem
schema.

Fix a retained spread-return profile with density
\[
  \delta=\frac{\theta_{\lambda,\sigma,\beta}}{4K}>0.
\]
Choose \(\kappa>0\) small enough that
\[
  \beta H(2\kappa/\beta)<(2\delta-\kappa)|\log Q|.
\]
Then the coverage-root split gives:

1. a few-root branch, with low interval-cover entropy and root-span defect
   gain \((2\delta-\kappa)L_H\);
2. a many-root branch, with at least \(\kappa L_H\) time-disjoint root
   exterior returns.

If the annular boundary gap
\[
  \Gamma_{\rm ann}(G)<1/Q
\]
holds, then annular insertions in both branches are controlled by endpoint
\(L^2\) norms up to \(e^{o(L_H)}\) factors.  If, in addition, the deterministic
endpoint support-congestion profiles extracted in Round 456 have subcritical
logarithmic exponent for the relevant skeleton families, then the
spread-return profile has the desired fixed-density exponent bound.

This is not a proof of the open problem, because the endpoint
support-congestion estimate is still missing.  But it is a theorem-shaped
endpoint for the current route:

* annular transfer is reduced to the boundary exponent gap;
* endpoint concentration is isolated as deterministic support congestion;
* radial level entropy is paid by the coverage-root split.

The remaining question is whether endpoint support congestion can be bridged
to the percolative finite-set/two-replica escape machinery or controlled by a
new deterministic radial-profile estimate.
