SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T11:32:53Z.
attacking: compact-kernel obstruction to transferring an exact-null or near-null result by law-uniform coefficient continuity; keep essential boundedness separate from continuity.

# QFORM B15 supplement — no law-uniform tent-mode matrix modulus, even full rank

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** account02/B15  
**Run:** `20260923T113253Z-account02-B15-qform-auto11`  
**Status:** `PROVED_SOURCE_VALID_OBSTRUCTION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

This supplements this run's `REPORT.md`, which already applies the owner-pinned ruled one-sheet theorem from `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` to the ambient rough majority-side inequality. The result below applies the completed partner account03/B15 balanced-tent compiler at `yspennstate/math-open-problems@fccc46ddffe0873ba2fccad767cce028ccef9fb8` to a new source-valid obstruction.

The unrestricted QFORM conjecture remains OPEN. The point proved here is narrower and negative: neither qualitative output regularity nor compact positive-kernel smoothing gives a **law-uniform modulus in the coefficient matrix** that could interpolate an exact-null/near-null endpoint. This remains false even when both compared matrices are full rank and have normalized third singular value exactly one.

## 1. The partner functional

Let

\[
\tau(u)=(1-|u|)_+,
\qquad
T(A;X):=\sup_{y\in\mathbb R}\mathbb E\,\tau(X^TAX-y).
\]

The completed account03/B15 theorem proves, after scalar homogeneity, that the sharp universal density constant satisfies

\[
C_* = \sup_{A,X} s_3(A)\,T(A;X),
\]

where the supremum is over all target product sources and rank-at-least-three symmetric matrices. Thus `T` is not an arbitrary regularizer: it is an exact compact positive-kernel normal form for the owner target after the global scale supremum.

## 2. Full-rank near-null pair

Fix `0<delta<1/2`. Let

\[
X_1,X_2,X_3\stackrel{\rm iid}{\sim}{\rm Unif}[-1/2,1/2],
\qquad
U\sim{\rm Unif}[0,1],
\qquad
X_4=\delta^{-1}+U,
\]

all independent. Every marginal is an admissible probability density bounded by one. Define

\[
A_\delta^-={\rm diag}(1,1,1,\delta^2),
\qquad
A_\delta^+={\rm diag}(1,1,1,\delta^2+\delta).
\]

Both matrices are full rank, both are target matrices, and

\[
s_3(A_\delta^-)=s_3(A_\delta^+)=1,
\qquad
\|A_\delta^+-A_\delta^-\|_{\rm op}=\delta.
\tag{2.1}
\]

Put

\[
Q_0=X_1^2+X_2^2+X_3^2.
\]

Then

\[
Q_\delta^- = Q_0 + 1+V_\delta,
\qquad
V_\delta=2\delta U+\delta^2U^2,
\qquad
0\le V_\delta\le2\delta+\delta^2.
\tag{2.2}
\]

For the plus matrix set

\[
Z_\delta=(\delta^2+\delta)(\delta^{-1}+U)^2.
\]

As a function of `U`,

\[
\frac{dZ_\delta}{dU}
=2(\delta^2+\delta)(\delta^{-1}+U)
=2(1+\delta)(1+\delta U)
\ge2(1+\delta).
\tag{2.3}
\]

Since `U` has density one on `[0,1]`, monotone change of variables gives

\[
\|p_{Z_\delta}\|_\infty\le\frac1{2(1+\delta)}.
\tag{2.4}
\]

The variable `Z_delta` is independent of `Q_0`; hence convolution yields

\[
\boxed{
\|p_{Q_\delta^+}\|_\infty
\le\frac1{2(1+\delta)}.
}
\tag{2.5}
\]

No continuity statement is used in this density-height payment.

## 3. A fixed positive tent gap

First obtain a lower bound on the base tent functional. We have

\[
0\le Q_0\le\frac34,
\qquad
\mathbb E Q_0=\frac14.
\]

Moreover, for `X~Unif[-1/2,1/2]`,

\[
\mathbb E X^2=\frac1{12},
\qquad
\mathbb E X^4=\frac1{80},
\qquad
{\rm Var}(X^2)=\frac1{180},
\]

so

\[
{\rm Var}(Q_0)=\frac1{60}.
\tag{3.1}
\]

Because `|Q_0-1/4|<=1/2`, the tent does not truncate at the center `1/4`, and Cauchy--Schwarz gives

\[
\begin{aligned}
T_0
&:=\sup_y\mathbb E\tau(Q_0-y)\\
&\ge \mathbb E\tau(Q_0-1/4)\\
&=1-\mathbb E|Q_0-1/4|\\
&\ge1-\sqrt{{\rm Var}(Q_0)}
=1-\frac1{\sqrt{60}}.
\end{aligned}
\tag{3.2}
\]

The function `tau` is one-Lipschitz. Evaluating the minus form at the translated center `y=1+1/4` and using (2.2),

\[
\boxed{
T(A_\delta^-;X)
\ge1-\frac1{\sqrt{60}}-(2\delta+\delta^2).
}
\tag{3.3}
\]

For the plus form, (2.5) and `int tau=1` give directly

\[
\boxed{
T(A_\delta^+;X)
\le\frac1{2(1+\delta)}.
}
\tag{3.4}
\]

Therefore

\[
\boxed{
T(A_\delta^-;X)-T(A_\delta^+;X)
\ge
1-\frac1{\sqrt{60}}-(2\delta+\delta^2)-\frac1{2(1+\delta)}.
}
\tag{3.5}
\]

As `delta downarrow0`, the right-hand side tends to

\[
\boxed{
\frac12-\frac1{\sqrt{60}}
\approx0.370900555>0.
}
\tag{3.6}
\]

Combining (2.1) and (3.5)--(3.6) proves:

### Theorem — `QFORM-NO-LAW-UNIFORM-TENT-MATRIX-MODULUS-v1`

There is no function `omega(r)->0` as `r->0` such that

\[
|T(A;X)-T(B;X)|\le\omega(\|A-B\|_{\rm op})
\]

for all admissible cap-one product sources and all full-rank target matrices `A,B` with `s_3(A)=s_3(B)=1`.

In particular, the exact compact tent normal form supplied by the completed partner theorem cannot be combined with a law-uniform matrix-continuity argument to pass from an exact-null or very-small-coefficient endpoint to a nearby nonzero coefficient.

## 4. Interpretation for the current proof graph

This is **not** a counterexample to QFORM. Both outputs above have bounded densities, and the plus output even has the explicit bound (2.5). The obstruction is to an intermediate mechanism.

It strengthens the same-run warning about critical-value/minority geometry in the exact owner-equivalent compact kernel. A near-null coefficient can act on a remote but perfectly admissible cap-one source interval and create order-one additional smoothing even though the coefficient matrices are arbitrarily close in operator norm. Thus any near-null interpolation must keep product-law geometry and the actual coefficient/source coupling; it cannot be paid by output continuity, fixed-kernel regularization, or a law-uniform coefficient modulus.

The first unpaid implication remains the product-provenance-sensitive control of the minority/two-sheet contribution (or a structural exit into a completed volume/grouped-coordinate branch). The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction continues to rule out replacing that geometry by a generic X-ray cap.

## 5. Logical regularity ledger

The three notions remain distinct.

1. Absolute continuity of the full quadratic pushforward follows from local coarea for every nonzero symmetric `A`; this has no universal height content.
2. Essential boundedness in the paid one-sheet/volume branches comes from direct interval/Fourier estimates and survives rough-source approximation without invoking continuity.
3. Continuity is stronger qualitative information about an individual density, but the theorem above shows that even the compact tent functional has no law-uniform matrix modulus on the target class.

Accordingly, continuity cannot be used to smuggle in either the missing universal height bound or a uniform near-null coefficient interpolation.
