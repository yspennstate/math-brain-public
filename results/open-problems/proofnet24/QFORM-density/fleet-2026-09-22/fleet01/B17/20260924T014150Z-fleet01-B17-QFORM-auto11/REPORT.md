# QFORM B17 — target-spectrum forcing for the one-null-leaf class

Run: `20260924T014150Z-fleet01-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922` revision `2026-09-22.5`  
Classification: **NEW SUPPORTING ANALYTIC THEOREM + EXACT FINITE STRESS FAMILY. FULL QFORM OPEN / NOT PROVED / NOT DISPROVED.**  
Continuity: tracked separately; only the branchwise continuity already proved in the pinned partner theorem is used.

## 1. Pinned partner theorem used

The completed fleet02/B17 theorem at

- repository `yspennstate/math-open-problems`,
- commit `5358d1f4f32d64254b0234463015b42f1d36bc13`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260924T004826Z-fleet02-B17-QFORM-7c2f/REPORT.md`

proves the following in original independent coordinates. For arbitrary independent real probability densities bounded by one and

\[
Q=rX^2+2aXY+2cXZ+bZ^2+uX+vY+wZ+q_0,
\qquad a b\ne0,
\]

one has the global bound

\[
\|p_Q\|_\infty\le \mathcal C(a,b):=
\begin{cases}
\dfrac{2+\log(4|a|/|b|)}{|a|},&|b|\le4|a|,\\[1ex]
\dfrac4{\sqrt{|ab|}},&|b|\ge4|a|.
\end{cases}
\tag{1}
\]

The proof is an original-coordinate linear-root/parabola-preimage bathtub argument; no post-rotation independence is used.

This note applies (1) to the **actual three-dimensional QFORM target spectral condition**, rather than separately assuming `|a|,|b|>=1`, and obtains a rigidity statement for the coefficient geometry.

## 2. Spectral forcing lemma

Consider the physical symmetric matrix

\[
A=\begin{pmatrix}
r&a&c\\ a&0&0\\ c&0&b\end{pmatrix}.
\tag{2}
\]

Assume that **all three** eigenvalues of this 3-by-3 matrix satisfy

\[
|\lambda_j(A)|\ge1,\qquad j=1,2,3.
\tag{3}
\]

Then, because `A` is symmetric,

\[
A^2-I\succeq0.
\tag{4}
\]

Writing `x=|a|` and `y=|b|`, the `(2,2)` entry of (4) gives

\[
\boxed{x\ge1.}
\tag{5}
\]

The principal `(2,3)` minor is

\[
\det (A^2-I)_{\{2,3\}}
=(a^2-1)(b^2-1)-c^2\ge0.
\tag{6}
\]

Together with positivity of the `(3,3)` diagonal entry, (6) forces

\[
\boxed{y\ge1},
\qquad
\boxed{c^2\le(x^2-1)(y^2-1)}.
\tag{7}
\]

Likewise the principal `(1,2)` minor gives

\[
\boxed{r^2\le(x^2-1)(x^2+c^2-1)}.
\tag{8}
\]

These inequalities are exact consequences of the target spectrum in this three-coordinate null-leaf architecture.

**Scope warning.** The implication `A^2-I >= 0` is valid here because this is a 3-by-3 target matrix and all three of its eigenvalues have modulus at least one. It is *not* valid for a general ambient QFORM matrix that merely has at least three large eigenvalues and may have additional eigenvalues in `(-1,1)`. No ambient extension is claimed.

## 3. New global target-class barrier

Apply the fleet02/B17 theorem (1). By (5)--(7), `x,y>=1` automatically.

If `y>=4x`, then

\[
\mathcal C(a,b)=\frac4{\sqrt{xy}}
\le\frac4{\sqrt{4x^2}}
=\frac2x\le2.
\tag{9}
\]

If `1<=y<=4x`, put

\[
C_0:=2+\log4.
\]

Then

\[
\mathcal C(a,b)
=\frac{C_0+\log x-\log y}{x}
\le\frac{C_0+\log x}{x}.
\tag{10}
\]

For `x>=1`,

\[
\frac{d}{dx}\frac{C_0+\log x}{x}
=\frac{1-C_0-\log x}{x^2}<0,
\]

so its maximum is attained at `x=1`. Consequently every physical matrix (2) satisfying the full 3-dimensional target condition (3), for **arbitrary independent cap-one input laws**, obeys

\[
\boxed{
\|p_{X^TAX}\|_\infty\le C_0=2+\log4
=3.3862943611198906\ldots .
}
\tag{11}
\]

The known source-valid universal lower obstruction is

\[
3\sqrt2=4.242640687119285\ldots,
\]

so this complete one-null-leaf target class lies below that obstruction by the fixed gap

\[
\boxed{3\sqrt2-(2+\log4)=0.8563463259993949\ldots .}
\tag{12}
\]

Thus no sharp or near-sharp witness at the `3sqrt(2)` scale can live in this entire three-variable architecture.

## 4. Rigidity of the partner-certificate extremizer

The coefficient envelope in (11) has a unique target-compatible maximizing geometry. In the logarithmic branch equality in (10) requires

\[
x=y=1.
\]

Then (6) forces `c=0`. Since the `(2,2)` diagonal entry of `A^2-I` is zero, positivity of `A^2-I` forces the entire second row/column there to vanish; in particular `ra=0`, hence `r=0`. Therefore the only coefficient geometry at the envelope maximum is, up to signs,

\[
A_0=
\begin{pmatrix}
0&1&0\\1&0&0\\0&0&1
\end{pmatrix},
\qquad
\operatorname{spec}(A_0)=\{-1,1,1\}.
\tag{13}
\]

There is also a quantitative near-envelope statement. Suppose the partner certificate `B(A)` obtained from (1) obeys

\[
B(A)\ge C_0-\varepsilon,
\qquad 0<\varepsilon<C_0-2.
\tag{14}
\]

The second branch (9) is then impossible, so (10) applies. Exactly,

\[
C_0-B(A)
=\frac{C_0(x-1)-\log x+\log y}{x}.
\]

Using `log x <= x-1`,

\[
\frac{(C_0-1)(x-1)+\log y}{x}\le\varepsilon.
\tag{15}
\]

Hence

\[
\boxed{
x\le\frac{C_0-1}{C_0-1-\varepsilon},
\qquad
\log y\le\varepsilon x.
}
\tag{16}
\]

Combining (16) with the exact spectral inequalities (7)--(8) shows

\[
x\to1,\quad y\to1,\quad c\to0,\quad r\to0
\]

whenever the partner certificate approaches `C_0`. Thus even the best possible use of this exact null-leaf mechanism collapses toward the hyperbolic-pair-plus-square block (13), not toward a genuinely shared diffuse frame.

## 5. Strict-target sheared/curved family approaching the coefficient envelope

The strict inequalities `|lambda|>1` by themselves do not create a fixed improvement below `C_0`. For every `delta>0`, define

\[
A_\delta=
\begin{pmatrix}
\delta&1+\delta&\delta\\
1+\delta&0&0\\
\delta&0&1+\delta
\end{pmatrix}.
\tag{17}
\]

This has both nonzero same-side curvature and nonzero physical shear. Direct calculation gives, for `M_delta=A_delta^2-I`, the leading principal minors

\[
\Delta_1=\delta(3\delta+2),
\]
\[
\Delta_2=\delta^2(2\delta^2+6\delta+3),
\]
\[
\Delta_3=\delta^3(\delta+2)(\delta^2+4\delta+2).
\tag{18}
\]

They are all positive, so by Sylvester

\[
A_\delta^2-I\succ0,
\qquad
\boxed{|\lambda_j(A_\delta)|>1\ \text{for all }j.}
\tag{19}
\]

Also

\[
\det A_\delta=-(1+\delta)^3,
\]

so the signature is `(+,+,-)`. Since in (17) `|a|=|b|=1+delta`, the completed partner theorem gives the **actual global target inequality**

\[
\boxed{
\|p_{X^TA_\delta X}\|_\infty
\le\frac{2+\log4}{1+\delta}
}
\tag{20}
\]

for every independent cap-one product law. The right side tends upward to `C_0` as `delta downarrow 0`.

For the concrete strict target `delta=1/10`,

\[
A_{1/10}=
\begin{pmatrix}
0.1&1.1&0.1\\1.1&0&0\\0.1&0&1.1
\end{pmatrix},
\]

whose eigenvalues are approximately

\[
-1.05335474,\quad1.05038851,\quad1.20296623,
\]

and (20) gives

\[
\boxed{
\|p_{X^TA_{1/10}X}\|_\infty
\le3.0784494191999006\ldots .
}
\tag{21}
\]

This is the requested application of the completed fleet02/B17 theorem to a real target inequality, not merely a citation of the partner result.

## 6. Exact centered-cube stress family: the partner envelope is not attained there

The envelope `C_0` is an arbitrary-cap-one upper certificate. For the natural centered-unit-interval control one can solve the entire non-diagonal block family exactly.

Let `X,Y,Z` be iid `Uniform[-1/2,1/2]`, let `x,y>0`, and set

\[
Q_{x,y}=2xXY+yZ^2.
\tag{22}
\]

The physical matrix is

\[
H_{x,y}=\begin{pmatrix}0&x&0\\x&0&0\\0&0&y\end{pmatrix},
\qquad
\operatorname{spec}(H_{x,y})=\{-x,x,y\}.
\tag{23}
\]

### 6.1 Product density

For `V=2XY`, direct product transformation gives

\[
\phi(v)=-\log(2|v|)\,\mathbf 1_{\{0<|v|<1/2\}}.
\tag{24}
\]

Put `beta=y/x` and `T_beta=V+beta Z^2`. Scaling gives

\[
\|p_{Q_{x,y}}\|_\infty=x^{-1}\|p_{T_\beta}\|_\infty.
\tag{25}
\]

A density representative of `T_beta` is

\[
p_\beta(t)=2\int_0^{1/2}\phi(t-\beta z^2)\,dz.
\tag{26}
\]

### 6.2 Zero is the global mode

For `t<0`, on the active integration set the denominator `beta z^2-t` is positive, and differentiation of (26) gives `p_beta'(t)>0`.

For `t>0`, let

\[
D_t=\{0<z<1/2:\ |t-\beta z^2|<1/2\}=[L,U]
\]

when nonempty. Boundary terms vanish because `phi=0` at `|v|=1/2`. In principal-value form,

\[
p_\beta'(t)=2\,\mathrm{PV}\!\int_{D_t}\frac{dz}{\beta z^2-t}.
\tag{27}
\]

If the root `sqrt(t/beta)` lies to the right of `D_t`, the integrand is negative. If the root lies in `D_t`, use

\[
F_t(z)=\frac1{2\sqrt{\beta t}}
\log\left|\frac{\sqrt\beta z-\sqrt t}{\sqrt\beta z+\sqrt t}\right|
\tag{28}
\]

as the principal-value antiderivative. If `L=0`, then `F_t(L)=0>F_t(U)`. If `L>0`, put `q=1/(2t) in (0,1)`. The untruncated level endpoints correspond to

\[
\tau_L=\sqrt{1-q},\qquad \tau_U=\sqrt{1+q}.
\]

Their logarithmic ratios are

\[
R_L=\frac{q}{(1+\sqrt{1-q})^2},
\qquad
R_U=\frac{q}{(1+\sqrt{1+q})^2},
\]

so `R_U<R_L`. If the upper endpoint is truncated at `z=1/2`, its ratio is even smaller because `(tau-1)/(tau+1)` increases for `tau>1`. Thus in all cases `F_t(U)-F_t(L)<0`, hence

\[
\boxed{p_\beta'(t)<0\quad(t>0)}.
\tag{29}
\]

Therefore

\[
\boxed{\|p_{T_\beta}\|_\infty=p_\beta(0).}
\tag{30}
\]

### 6.3 Exact norm

At zero,

\[
p_\beta(0)
=2\int_0^{\min\{1/2,(2\beta)^{-1/2}\}}
-\log(2\beta z^2)\,dz.
\]

Using

\[
\int-\log(2\beta z^2)\,dz
=z\,[2-\log(2\beta z^2)],
\]

one obtains

\[
\boxed{
\|p_{Q_{x,y}}\|_\infty=
\begin{cases}
\dfrac{2+\log(2x/y)}{x},& y\le2x,\\[1.1ex]
\dfrac{2\sqrt2}{\sqrt{xy}},& y\ge2x.
\end{cases}}
\tag{31}
\]

The same formula depends only on `|x|,|y|` when either coefficient changes sign, because `2XY` is symmetric.

If (23) itself is a QFORM target, then `x,y>=1`. Optimizing (31) yields

\[
\boxed{
\sup_{x,y\ge1}\|p_{Q_{x,y}}\|_\infty
=2+\log2
=2.6931471805599453\ldots,
}
\tag{32}
\]

with equality only at `x=y=1`. Thus the exact centered-cube stress at the spectral envelope geometry (13) lies another `log 2` below the arbitrary-cap-one partner certificate:

\[
(2+\log4)-(2+\log2)=\log2.
\]

In particular it is far below the source-valid diffuse obstruction `3sqrt(2)`.

## 7. Source-valid lower obstruction and proof-design consequence

The lower obstruction used for comparison is pinned independently at

- repository `yspennstate/math-open-problems`,
- commit `8624982153e5a2154e4ae8922d2fe4dc77080efc`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`, Proposition `QFORM-BLOCK-CLT-LOWER-3SQRT2-v1`.

It proves

\[
\boxed{C_{\rm univ}\ge3\sqrt2}
\tag{33}
\]

using three diffuse independent centered-unit-interval banks and weak convergence to the Gaussian signature `(1,1,-1)` form. No convergence of density values is assumed there.

Combining (11), (20), (31), and (33) gives a clean witness constraint:

> The full three-coordinate one-null-leaf architecture, even with arbitrary same-side curvature, physical shear, affine terms, and arbitrary cap-one product laws, is separated by a fixed `0.8563...` from the known universal lower-obstruction scale. Strict target spectra do not change that conclusion, and near-maximal partner certificates rigidly collapse toward the simple block `2XY+Z^2`. Therefore a near-sharp `3sqrt(2)` witness must exploit a mechanism absent here: diffuse/shared rows, destruction of the exact null leaf (`Y^2` or `YZ`), a genuinely higher-dimensional multiscale product geometry, or an off-zero/two-sheet mechanism not reducible to this linear-root bathtub.

This is a supporting theorem only. It does **not** prove `C_univ=3sqrt(2)` and does **not** settle the unrestricted QFORM upper bound.

## 8. Integrity / correction compliance

- No rotation of the independent variables is used.
- No arbitrary-joint coarea density cap is used.
- No conditional-density-cap substitution is used.
- No bounded-support, moment, centering, log-concavity, connected-support, or finite-fragment assumption enters (11) or (20).
- The centered-interval assumption is used only in the explicit exact control family (22)--(32).
- The theorem is not an ambient reduction: the spectral forcing in Section 2 is explicitly restricted to a 3-by-3 matrix whose *entire* spectrum lies outside `(-1,1)`.
- The generic `pi` / `pi sqrt2` calculations are not used as a proof of this theorem.
- Full-target continuity remains separate.

Status: **FULL QFORM REMAINS OPEN / NOT PROVED / NOT DISPROVED.**
