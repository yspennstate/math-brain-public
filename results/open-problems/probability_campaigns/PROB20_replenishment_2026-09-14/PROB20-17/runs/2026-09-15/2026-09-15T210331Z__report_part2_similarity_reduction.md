# PROB20-17 — follow-up structural reduction for the sharp `2+2` pair target

**STATUS: PARTIAL SUPPLEMENT.**  This file supplements the already-delivered `2026-09-15T205502Z__report.md`; it does not replace it and makes no full-solution claim.

The sharp unresolved two-matrix target is
\[
\|A^2B^2\|\,\|ABAB\|\stackrel{?}{\ge}\|AB\|^4
\tag{1}
\]
for arbitrary PSD `A,B`.  This supplement records an exact similarity-orbit reformulation that emerged after the main report was committed.

Assume first `A>0`; the PSD boundary follows by regularization.  Put
\[
S:=A^{1/2},
\qquad
C:=A^{1/2}BA^{1/2}\succeq0,
\]
and define the full real similarity orbit
\[
T_t:=S^t C S^{-t}.
\tag{2}
\]
Then
\[
T_1=SCS^{-1}=AB,
\tag{3}
\]
while
\[
T_{-1}=S^{-1}CS=BA=(AB)^*=T_1^*.
\tag{4}
\]
Also
\[
T_3=S^3CS^{-3}=A^2BA^{-1}.
\tag{5}
\]
Therefore
\[
T_3T_1=A^2B^2,
\qquad
T_1^2=ABAB,
\tag{6}
\]
and
\[
T_{-1}T_1=(AB)^*(AB)=BA^2B.
\tag{7}
\]
Taking operator norms,
\[
\|T_{-1}T_1\|=\|AB\|^2.
\tag{8}
\]
Consequently (1) is **exactly equivalent** to
\[
\boxed{
\|T_3T_1\|\,\|T_1^2\|
\stackrel{?}{\ge}
\|T_{-1}T_1\|^2,
}
\tag{9}
\]
where the orbit has the special adjoint symmetry `T_{-1}=T_1^*`.

Equivalently, writing
\[
H:=A=S^2,
\qquad X:=T_1=AB,
\]
we have
\[
X^*=H^{-1}XH,
\tag{10}
\]
and the pair-product conjecture becomes the purely similarity-theoretic statement
\[
\boxed{
\|H X H^{-1}X\|\,\|X^2\|
\stackrel{?}{\ge}
\|X^*X\|^2,
\qquad
H>0,
\quad
X^*=H^{-1}XH.
}
\tag{11}
\]
Thus the missing theorem is not an arbitrary four-factor word inequality: it is a three-point inequality along a positive similarity orbit of an operator that is self-adjoint in the `H`-metric.

This reformulation is useful for two reasons.

1. It separates the positivity input from the word bookkeeping.  The only structural hypothesis on `X` in (11) is positive symmetrizability (`X` is similar to a PSD matrix), encoded by (10).
2. It suggests attacking (11) using convexity or three-lines estimates for the orbit `H^t X H^{-t}` rather than by manipulating `AABB` and `ABAB` directly.

A bounded computational search for a proof using only finite conic combinations of the elementary Horn–Mathias/Bhatia–Davis Cauchy inequality
\[
\|P^*YQ\|^2\le\|PP^*Y\|\,\|YQQ^*\|
\]
with short literal `A/B` words did **not** derive (1).  This is only a search obstruction, not a mathematical impossibility theorem, and no conclusion is drawn from it.

The next focused question is whether the function
\[
t\mapsto \log\|T_tT_1\|
\]
or a two-parameter variant has an additional convexity/monotonicity property under the adjoint constraint `T_{-1}=T_1^*` strong enough to imply (9).  Ordinary unconstrained log-convexity would not by itself give the required three-point direction, so the metric-self-adjoint symmetry must be used.

No universal constant is changed by this supplement.  The strongest verified arbitrary-dimensional `n=4` factor remains
\[
0.7303902120286716\ldots.
\]

**Verification level:** algebraic self-check only; no independent/formal review.
