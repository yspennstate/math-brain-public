# QFORM B17 — exact tetrahedral rational-orientation witness

Run: `20260923T164038Z-account01-B17-QFORM-auto11`

Status: **supporting sharp-witness result only. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** Continuity for the unrestricted owner target remains separate. This note stays in the original physical product model and does not use the corrected-false arbitrary-joint coarea reduction, post-rotation independence, or conditional-cap claims.

## 1. Exact finite product construction

Let

\[
R=\frac12\begin{pmatrix}
1&1&1\\
1&-1&1\\
1&1&-1\\
1&-1&-1
\end{pmatrix},\qquad R^TR=I_3,
\]

and let `X_1,...,X_4` be independent `Unif[-1/2,1/2]`; every source density is exactly one on its support. Put `Y=R^T X`.

The kernel of `R^T` is spanned by `(1,-1,-1,1)`, and direct fiber-length calculation through the four-cube gives the exact three-dimensional density

\[
\rho(y)=2\bigl(1-H(y)\bigr)_+,
\qquad
H(y)=M_1(y)+M_2(y),
\]

where `M_1>=M_2>=M_3` are the ordered absolute coordinate magnitudes. Equivalently,

\[
H(y)=\max_{i<j}\max_{\varepsilon_i,\varepsilon_j\in\{\pm1\}}
(\varepsilon_i y_i+\varepsilon_j y_j).
\]

Choose the exact negative eigendirection

\[
n_* = \frac{(7,18,18)}{\sqrt{697}}.
\]

Set

\[
B_*=I_3-2n_*n_*^T
=\frac1{697}\begin{pmatrix}
599&-252&-252\\
-252&49&-648\\
-252&-648&49
\end{pmatrix}.
\]

Then `B_*^2=I_3` and `spec(B_*)={1,1,-1}`. The physical four-variable matrix is

\[
A_*=RB_*R^T
=\frac1{2788}\begin{pmatrix}
-1607&95&95&1797\\
95&1993&-795&1103\\
95&-795&1993&1103\\
1797&1103&1103&409
\end{pmatrix}.
\]

Every entry of `A_*` is nonzero and

\[
\operatorname{spec}(A_*)=\{1,1,-1,0\}.
\]

Thus this is a genuinely dense finite source-valid target instance, not a diagonal control.

## 2. Exact cone-tip formula

An orthonormal basis of `n_*^\perp` is

\[
e_1=\frac{(0,1,-1)}{\sqrt2},\qquad
 e_2=\frac{(-18\sqrt2,7/\sqrt2,7/\sqrt2)}{\sqrt{697}}.
\]

For `theta in [0,2pi)` define the positive-sheet unit null direction

\[
\omega(\theta)=\frac{n_*+\cos\theta\,e_1+\sin\theta\,e_2}{\sqrt2}.
\]

The two cone sheets contribute equally because `rho` is even. Integrating the Dirac delta of the homogeneous quadratic form radially gives

\[
\boxed{
 p_{X^TA_*X}(0)
 =\frac1{\sqrt2}\int_0^{2\pi}\frac{d\theta}{H(\omega(\theta))}.}
\]

This formula is exact and remains entirely in the original independent-cube source model.

## 3. Reproducible lower certificate

The function `H` is `sqrt(2)`-Lipschitz in Euclidean norm because it is the maximum of linear forms whose coefficient vectors have norm `sqrt(2)`. Also `|omega'(theta)|=1/sqrt(2)`, so

\[
h(\theta):=H(\omega(\theta))
\]

is 1-Lipschitz. Since `|omega|=1`, if `a>=b>=c>=0` are its ordered absolute coordinates then

\[
(a+b)^2=1-c^2+2ab\ge 1-c^2+2c^2\ge1,
\]

hence `h(theta)>=1`. Therefore `f(theta)=1/h(theta)` is also 1-Lipschitz.

For the `N`-point midpoint rule with mesh `Delta=2pi/N`, this gives the rigorous deterministic discretization bound

\[
\left|\int_0^{2\pi}f(\theta)d\theta
-\Delta\sum_{k=0}^{N-1}f((k+1/2)\Delta)\right|
\le \frac{\pi^2}{N}.
\]

The sibling checker evaluates every midpoint by outward interval arithmetic for the trigonometric/algebraic expressions, uses an upper enclosure for `H` to obtain a lower enclosure for `1/H`, and subtracts an additional floating accumulation safety margin. With `N=30000` it returns

\[
p_{X^TA_*X}(0)>3.5605.
\]

A high-resolution ordinary midpoint evaluation is

\[
p_{X^TA_*X}(0)\approx 3.5608355507075.
\]

Hence this exact rational orientation strictly strengthens the earlier certified tetrahedral statement `p(0)>3.56`. It does **not** improve the target-level lower obstruction `3 sqrt(2)` supplied by diffuse exact-spectrum cube frames.

## 4. Witness interpretation

The same tetrahedral range frame `R`, the same physical product cube, the same row leverages `3/4`, and the same nonzero eigenvalues `{1,1,-1}` support different cone-tip values as the signature is rotated inside the three-dimensional range. The rational direction above gives a finite dense stress above `3.5605`; therefore any candidate sharp argument that remembers only the nonzero eigenvalue multiset and range leverages loses real finite orientation information.

This remains only a cone-tip theorem. No claim is made that zero is the global mode for this orientation.

## 5. Required account02/B17 application to an actual inequality

Pinned partner source:

- canonical partner mathematics at `yspennstate/math-open-problems@2f227775f53ca554a645737b9dbad18e25437d74`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260923T151331Z-account02-B17-QFORM-auto11/REPORT.md`.

That completed theorem says that for arbitrary unit vectors `a,b`, arbitrary cap-one heavy law `X`, centered unit-interval bank coordinates, and eigenvalue magnitudes at least one,

\[
\|p_{\alpha X^2+\lambda S_a^2-\mu T_b^2}\|_\infty
\le K_*:=\frac\pi2(\sqrt2+2^{1/4})
=4.089443637123813\ldots <3\sqrt2.
\]

Apply it concretely with

\[
a=(1,1)/\sqrt2,\qquad b=(2,1,2)/3,\qquad
\alpha=\lambda=\mu=1,
\]

and any independent cap-one heavy `X` (in particular the centered unit interval). Then the exact physical block matrix

\[
A_{\rm sep}=\operatorname{diag}(1,aa^T,-bb^T)
\]

has nonzero spectrum exactly `{1,1,-1}`, and the actual global inequality is

\[
\boxed{
\|p_{X^2+((U_1+U_2)/\sqrt2)^2-((2V_1+V_2+2V_3)/3)^2}\|_\infty
\le4.089443637123813\ldots<3\sqrt2.}
\]

Thus the entire finite separated majority-heavy architecture is globally subcritical, while the tetrahedral family studied above is genuinely shared-coordinate/coupled. This directs the witness search toward coupled intermediate-leverage or off-tip mechanisms rather than separated rank-one controls.

## 6. Sharp-constant status

The strongest source-valid universal lower obstruction remains

\[
\boxed{C_{\rm univ}\ge3\sqrt2=4.242640687119\ldots.}
\]

This note supplies a stronger exact finite orientation stress and an analytic/certified witness constraint; it does not prove `C_univ=3 sqrt(2)` and does not prove the full universal bound.
