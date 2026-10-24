# account02/B11 r45 late partner refresh

A newer compatible designated-partner result appeared after the primary handoff was committed, so the primary handoff is preserved immutably and this addendum records the later dependency.

Latest compatible partner: account03/B11 r45, brain commit `3067048bad2acf11890d060b8e6298384e5c4892`, math commit `12e2174445fbc824279bf1376da1346454d7060a`.

Partner r45 gives the exact null-puncture normal form

`Q=2 kappa (sqrt(q) H+sqrt(1-q) T) W+dW^2+2eWV+cV^2`,

where `H` is an original coordinate independent of the residual product source, `(T,W,V)` is an orthonormal 3D projection of that residual product source, `kappa^2 |c|=|det M|>=s^3`, and the overlap ratio is exactly `sqrt((1-q)/q)`.

The new account02/B11 L2 receiver from this same run requires genuine source independence for a hyperbolic pair. Partner r45's source-valid box falsifier was applied to show that this requirement cannot be replaced by a bare joint-density cap: with `H~Unif[0,1]` independent of a cap-one joint box law for `(T,V,W)`, `Q_epsilon=V^2+2HW` lies in `[0,3epsilon]` almost surely while its coefficient matrix has eigenvalues `{-1,0,1,1}`. Thus any attempted compiler based only on a 3D projection density cap has interval constant at least `1/(3epsilon)` and fails.

The terminal math bundle is now `yspennstate/math-open-problems@6e395c6bdf389280645c1935de262fcb14a284e1`, with the late addendum at `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260924T001205Z-account02-B11-QFORM-auto11/PARTNER_R45_REFRESH.md`.

Updated first unpaid implication:
`QFORM-R45-ORTHOGONAL-PROJECTION-HYPERBOLIC-L2-COMPILER-v1`: exploit the orthonormal-product-projection provenance of `(T,W,V)` to derive a uniform linear small-ball bound for the exact puncture normal form while retaining the `TW` term, or force a source-disjoint physical-pair/volume/square exit. The ambient joint-density cap alone is provably insufficient. Arbitrary additional nonseparable spectrum remains a separate bridge. Full QFORM remains OPEN.
