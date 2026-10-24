# Worker 054 — exact mathematical excerpt from early P13

Source repository: yspennstate/math-open-problems.

Baseline commit: 8861ffde776a1dbf842e918590cc1003492ff296.

Source path: proofnet24/P13-fourth-moment-rmt/runs/2026-09-14/2026-09-14_16-24-25__run-report.md.

Returned Git blob SHA-1: ff5169b61c93ceb1429c309373e85c08d49544d2.

Fetched through the GitHub connector on 2026-09-14. Only the directly relevant mathematical sections 8 and 13.1–13.4 are retained below, verbatim. This is an archive excerpt, not an endorsement of other source claims.

# 8. New P24 input: finite-variance singular-edge control

The previous P13 report listed low-overlap pair anti-alignment as one of the two major finite-variance obstacles.

The newest P24 theorem changes that diagnosis.

Condition on a shared block whose residual dimension is \(D\), and on the first residual unit normal \(v\). Let \(w\) be the second private residual normal and define
\[
Y
=
1-(v\cdot w)^2.
\tag{8.1}
\]

For one fixed centered variance-one bounded-density coordinate law with finite variance only, P24 proves:

### Ultra-edge

There are constants
\[
a_0>0,\qquad C_0<\infty
\]
such that
\[
\boxed{
P\{Y\le y\mid A,v\}
\le
[C_0(Dy)^{1/3}]^{D-1},
\qquad
0<y\le a_0/D,
}
\tag{8.2}
\]
with
\[
C_0a_0^{1/3}\le1/2.
\tag{8.3}
\]

### Mesoscopic edge

There are
\[
y_*>0,\qquad c_\xi>0
\]
such that for all sufficiently large \(D\)
\[
\boxed{
P\{Y\le y\mid A,v\}
\le
e^{-c_\xi D},
\qquad
0<y\le y_*.
}
\tag{8.4}
\]

These estimates are uniform in the realized apex and in the first line \(v\).

---


### 13.1 Conditional geometry

Given the shared apex and first line \(v\), the second private rows remain fresh independent original product-law rows. The projected coordinates are not declared iid.

If
\[
1-(v\cdot w)^2\le y,
\]
then after sign choice
\[
\|v-w\|\le\sqrt{2y}.
\]
Each fresh row obeys
\[
|\langle X_i,q\rangle|
\le
\sqrt{2y}\|P_EX_i\|.
\]
This is exact.

### 13.2 Ultra-edge

For one fresh row,
\[
p(y)
=
P\{
|\langle X,q\rangle|
\le
\sqrt{2y}\|P_EX\|
\}.
\]

Split at
\[
\|P_EX\|\le R\sqrt D.
\]

The one-dimensional product-marginal density theorem gives
\[
P\{
|\langle X,q\rangle|
\le
R\sqrt{2Dy}
\}
\le
C K R\sqrt{Dy}.
\]

Markov gives
\[
P\{\|P_EX\|^2>R^2D\}\le R^{-2}.
\]

Optimizing
\[
R=(Dy)^{-1/6}
\]
gives
\[
p(y)\le C_K(Dy)^{1/3}.
\]

Independence across the \(D-1\) fresh rows gives the stated power.

### 13.3 Finite-variance step loss

P24 proves uniform integrability of
\[
(q^\top X)^2
\]
over all unit \(q\), via fixed-law truncation.

It separately proves
\[
E|X^\top PX-k|=o(k)
\]
uniformly over rank-\(k\) projectors.

These imply a fixed law-dependent positive probability of
\[
(q\cdot U_E)^2\ge1/(8k).
\]

No higher moment is hidden.

### 13.4 Adapted Chernoff

The residual projection recursion gives exactly
\[
(v\cdot w)^2
=
\prod_{k=2}^D(1-Z_k).
\]

The fresh-row structure makes the lower success-probability bound conditional on the past, so the Laplace-transform iteration is legitimate.

A near-parallel outcome forces too few successful angular losses; hence the mesoscopic probability is
\[
e^{-c_\xi D}.
\]


