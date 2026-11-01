# Round 431 defect lower bound and why it is insufficient

Round 431 records the direct defect bound for spread returns and explains why
it does not close the estimate.

Every exterior return through level \(u\) contains an inward step from
radius \(u\) to radius \(u-1\), namely the final step of its witness interval.
If a path has exterior returns through \(N\) distinct levels, these final
inward steps are distinct, since an inward step has a unique upper level.
Therefore
\[
  I_x(\gamma)\ge N,
  \qquad
  2I_x(\gamma)+H_x(\gamma)\ge 2N.
\]

For the spread-return event,
\[
  N>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H,
\]
so
\[
  2I_x(\gamma)+H_x(\gamma)
  >
  \frac{\theta_{\lambda,\sigma,\beta}}{2K}L_H.
\]
Equivalently, spread returns force a defect-density contribution
\[
  2\delta=\frac{\theta_{\lambda,\sigma,\beta}}{2K},
  \qquad
  \delta=\frac{\theta_{\lambda,\sigma,\beta}}{4K}.
\]

This is not enough for the current far-tail ladder.  The spread-return
profile already appears inside a radial profile whose summation range is
\[
  d>\lambda L_H.
\]
Since
\[
  \theta_{\lambda,\sigma,\beta}
  =
  \frac{\lambda}{J_{\sigma,\beta}},
\]
we have
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{2K}
  =
  \frac{\lambda}{2KJ_{\sigma,\beta}}
  \le \lambda
\]
for every \(K\ge1\).  Thus the direct inward-step count gives no stronger
defect threshold than the one already present in the far-tail profile.

The chain-disjoint reduction from Round 430 must therefore be used to get
structure, not merely to count inward steps.  A successful estimate has to
show that nested chains or disjoint excursions reduce the number of possible
self-avoiding witnesses beyond what is already paid for by the \(Q^d\) defect
weight.
