SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B11, 2026-09-22T19:17:27Z.
attacking: the weighted parabolic null-graph trace in the overlapping (+,+,-) branch.

# account04/B11 handoff — conditional caps do not pay the cone trace

Status: `AUXILIARY_ONLY / PRECISE_MISSING_FACTOR`; full QFORM remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems@797dcde430e982a020d7642b54cadc281cbc9bc1`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T191727Z-account04-B11-nullgraph-obstruction-r2/REPORT.md`. The exact checker in the same directory ends `QFORM_B11_NULLGRAPH_CHECK_PASS`.

New theorem `QFORM-PARABOLIC-CONDITIONAL-CAP-INSUFFICIENT-v1`: there is a probability density (g(v,w)le1), an independent (U\sim\mathrm{Unif}[0,1]), and
[
Z=-V^2/(2W)+U
]
such that every conditional density (p_{Z\mid V,W}) is a translate of (1_{[0,1]}), but
[
T=2ZW+V^2=2WU
]
has an unbounded density at zero.

The construction uses rectangles (W_k=(2^{-k-1},2^{-k})), (|V_k|=1/k), with total area (rac12\log2<1), plus a filler rectangle. For (t<2^{-K-1}),
[
p_T(t)\ge \frac{\log2}{2}\sum_{k=1}^K\frac1k\to\infty.
]
Thus a bounded transverse joint density plus a uniform conditional cap for the third coordinate does not control the ((+,+,-)) pushforward, even when the third coordinate is an independent uniform smoother plus a measurable shift.

The exact missing factor is the parabolic null-graph trace
[
\mathcal N(h)=\sup_t\int_{w\ne0}
h((t-v^2)/(2w),v,w)\,\frac{dv\,dw}{|w|},
qquad \|p_T\|_\infty=\mathcal N(h)/2.
]

The completed assigned-partner result account01/B11 r13 was applied to an actual inequality: for disjoint original-coordinate banks,
[
\|p_{2\alpha ZW+\beta V^2}\|_\infty
\le3\,2^{4/3}e
(|\alpha|\sigma\sqrt{|\beta|}\Delta)^{-2/3}.
]
That theorem explains how the third direction removes the rank-two logarithm in the separated branch. The new obstruction proves genuine bank independence cannot be replaced by the conditional and marginal caps available after overlap.

For the partner's antipodal independent-block representation, the remaining obligation is now exact: prove a dimension-free bound on (mathcal N(h)) from the product-linear provenance of the independent cap-one-half ((S_j,D_j)) blocks, thereby preventing multiscale tracking of (z=-v^2/(2w)). The counterexample is not a QFORM counterexample because its nonlinear dependence is not asserted to be a linear image of independent cap-one coordinates.

Control used: owner revision `2026-09-22.13`; correction inbox blob `6335a8d51fc8081123635a8d0848738b615cb082`. Essential boundedness is proved only in the separated partner branch; continuity remains open.
