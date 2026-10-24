# Partner refresh addendum — account03/B11 r45 supersedes r44 as latest compatible input

This addendum was created after the main r45 report because account03/B11 published a newer compatible result during this invocation. The earlier report is preserved immutably; this file updates only the dependency frontier.

Latest designated partner:

- brain handoff commit: `3067048bad2acf11890d060b8e6298384e5c4892`
- math commit: `12e2174445fbc824279bf1376da1346454d7060a`
- report: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260924T002432Z-account03-B11-QFORM-r45/REPORT.md`
- result: `QFORM-NULL-PUNCTURE-ONEPARAMETER-NORMALFORM-v1` plus a source-valid interface falsifier.

## Exact normal form consumed

For exact rank three `A=RMR^T`, an original coordinate `i` with leverage `q=||r_i||^2`, `0<q<1`, and exact physical null pivot `A_ii=0`, partner r45 proves a product-valid representation

\[
Q=2\kappa(\sqrt q\,H+\sqrt{1-q}\,T)W+dW^2+2eWV+cV^2,
\tag{A.1}
\]

where `H=X_i` is genuinely independent of the residual original-coordinate product bank, while `(T,W,V)` is an orthonormal three-dimensional projection of that residual product source and is generally internally dependent. Moreover

\[
\boxed{\kappa^2|c|=|\det M|\ge s^3},
\tag{A.2}
\]

and the overlap-to-independent-saddle ratio is exactly

\[
\boxed{\sqrt{(1-q)/q}}.
\tag{A.3}
\]

At the live near-coloop threshold `q>=63/64`, this is at most `1/sqrt(63)`, but the `TW` term may not be deleted perturbatively.

## Partner result applied to the new L2 receiver: exact obstruction to the missing extension

The main report proves

\[
\|p_{cXY+dY+R(X)}\|_2^2\le 4FG/|c|
\tag{A.4}
\]

only when `X` and `Y` are genuinely independent source variables. A tempting route to (A.1) would be to replace that independence by a three-dimensional joint density cap for `(T,W,V)` and then apply the same overlap estimate conditionally. Partner r45 proves this interface is false in exactly the needed strength.

For every `0<epsilon<1`, let `H` be independent `Uniform[0,1]` and let `(T,V,W)` have joint density one on the volume-one box

\[
0\le T\le\epsilon^{-3/2},\qquad
0\le V\le\sqrt\epsilon,\qquad
0\le W\le\epsilon.
\]

Then for

\[
Q_\epsilon=V^2+2HW
\]

the coefficient matrix has eigenvalues `{-1,0,1,1}`, yet `0<=Q_epsilon<=3epsilon` almost surely. Hence

\[
\boxed{
\sup_t\frac{\Pr(Q_\epsilon\in[t,t+3\epsilon])}{3\epsilon}
\ge \frac1{3\epsilon}\to\infty.
}
\tag{A.5}
\]

Thus the new hyperbolic-pair L2 theorem cannot be compiled into the r45 puncture model by forgetting the residual product-projection provenance and retaining only a joint `L-infinity` cap. This is a genuine analytic obstruction, not a QFORM counterexample, because the box law is not asserted to be an orthogonal projection of independent cap-one coordinates.

Equation (A.5) is the latest-partner result applied to the exact proof interface left by the main report.

## Updated first unpaid implication

The precise next lemma is now

`QFORM-R45-ORTHOGONAL-PROJECTION-HYPERBOLIC-L2-COMPILER-v1`:

> For the exact partner normal form (A.1), exploit that `(T,W,V)` is an **orthonormal projection of a cap-one original product source**, not an arbitrary joint density, to obtain a uniform linear small-ball / bounded-density estimate through the puncture `q->1`, while retaining the `TW` overlap term and arbitrary `d,e`. Equivalently, prove a product-provenance analogue of the new L2 overlap estimate that survives same-bank projection dependence, or force a source-disjoint physical-pair/volume/square exit.

The invariant (A.2) supplies the target scale and (A.3) identifies the only small overlap parameter. Partner r45's falsifier (A.5) proves that any valid compiler must use more than an ambient projection-density cap. The earlier r44 rank-two/same-bank interpolation problem is subsumed by this sharper null-puncture formulation in the exact-zero-pivot near-coloop branch.

Arbitrary additional nonseparable spectrum remains a separate full-target bridge. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.
