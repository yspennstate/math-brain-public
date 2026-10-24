# QFORM cap-one variance rigidity and disconnected sharp rotated witnesses

Run: `20260924T065245Z-account01-B17-QFORM-auto11b`  
Worker: `account01/B17`  
Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
Status: **PROVED SUPPORTING SHARP-WITNESS / RIGIDITY THEOREM; FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains open: arbitrary independent one-dimensional probability densities bounded by one, arbitrary dimension, and an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one. Continuity for that full target remains separate.

This report proves a sharp one-dimensional stability inequality behind the known `3 sqrt(2)` diffuse obstruction, transfers it through a source-pinned product/Fourier theorem to a three-bank Lindeberg chamber, and constructs an exact entrywise-dense rotated target family with disconnected physical supports. It does not use independence after spectral rotation, the false arbitrary-joint coarea estimate, a uniform pointwise quadratic-phase estimate, or a fiber-supremum argument.

## 1. Sharp cap-one variance stability

### Theorem 1 (`QFORM-CAPONE-VARIANCE-STABILITY-v1`)

Let `X` have a probability density `f` on `R` with `0 <= f <= 1` and finite variance. Let
`mu = E X` and
`I_mu = [mu-1/2, mu+1/2]`.
Then

\[
\boxed{
\operatorname{Var}(X)-\frac1{12}
\ge
\frac18\left\|f-\mathbf 1_{I_\mu}\right\|_1^2.}
\tag{1.1}
\]

The constant `1/8` is sharp.

### Proof

Translate so `mu=0`, and write `I=[-1/2,1/2]`. Define

\[
\delta=\int_{I^c}f(x)\,dx.
\]

Since `|I|=1` and `int f=1`,

\[
\delta=\int_I(1-f(x))\,dx,
\qquad
\|f-\mathbf 1_I\|_1=2\delta .
\tag{1.2}
\]

Now

\[
\operatorname{Var}(X)-\frac1{12}
=
\int_{I^c}x^2 f(x)\,dx
-
\int_I x^2(1-f(x))\,dx .
\tag{1.3}
\]

For a function `0<=g<=1` of mass `delta` supported on `I^c`, the smallest possible integral of `x^2 g(x)` is obtained by filling the points of `I^c` closest to the origin. Hence

\[
\int_{I^c}x^2 f(x)\,dx
\ge
2\int_{1/2}^{1/2+\delta/2}x^2\,dx.
\tag{1.4}
\]

Likewise, among `0<=h<=1` of mass `delta` supported in `I`, the largest possible integral of `x^2 h(x)` is obtained by filling the two boundary strips. Thus

\[
\int_Ix^2(1-f(x))\,dx
\le
2\int_{1/2-\delta/2}^{1/2}x^2\,dx.
\tag{1.5}
\]

Subtracting,

\[
2\left[
\int_{1/2}^{1/2+\delta/2}x^2\,dx
-
\int_{1/2-\delta/2}^{1/2}x^2\,dx
\right]
=\frac{\delta^2}{2}.
\tag{1.6}
\]

Equations (1.2)--(1.6) give (1.1).

For `0<=delta<=1`, equality is attained by the explicit symmetric boundary-swap density

\[
f_\delta(x)=
\mathbf1_{[-1/2+\delta/2,\,1/2-\delta/2]}(x)
+\mathbf1_{[1/2,\,1/2+\delta/2]}(x)
+\mathbf1_{[-1/2-\delta/2,\,-1/2]}(x).
\tag{1.7}
\]

It has total support length one, `0<=f_delta<=1`, mean zero,

\[
\|f_\delta-\mathbf1_{[-1/2,1/2]}\|_1=2\delta,
\qquad
\operatorname{Var}(f_\delta)=\frac1{12}+\frac{\delta^2}{2}.
\tag{1.8}
\]

So the factor `1/8` cannot be improved. QED.

This is only a one-dimensional variance statement. It does **not** assert that intervals are extremal for an arbitrary rotated quadratic form and does not conflict with the live correction forbidding a global bounded-diameter/finite-fragment localization reduction.

## 2. A diffuse three-bank rigidity theorem

Let `m>=2`. Split `3m` independent physical coordinates into three banks. Let
`X_{j,k}^{(m)}`, `j=1,2,3`, `1<=k<=m`, have densities bounded by one and finite second moments. Put

\[
Y_{j,m}=m^{-1/2}\sum_{k=1}^mX_{j,k}^{(m)}.
\tag{2.1}
\]

Assume, bank by bank,

\[
m^{-1/2}\sum_{k=1}^m E X_{j,k}^{(m)}\to0,
\qquad
v_{j,m}:=\frac1m\sum_{k=1}^m\operatorname{Var}(X_{j,k}^{(m)})\to v_j<\infty,
\tag{2.2}
\]

and the standard triangular-array Lindeberg condition

\[
\frac1m\sum_{k=1}^m
E\!\left[
|X_{j,k}^{(m)}-EX_{j,k}^{(m)}|^2
\,\mathbf1_{\{|X_{j,k}^{(m)}-EX_{j,k}^{(m)}|>\varepsilon\sqrt m\}}
\right]\to0
\tag{2.3}
\]

for every `epsilon>0`.

Let `B_m` be real symmetric `3 x 3` matrices of signature `(2,1)`, with all three eigenvalue magnitudes at least one, and suppose `B_m -> B`. Let `T_m` be the `3m x 3` synthesis matrix having `m` copies of `e_j/sqrt(m)` in bank `j`, and set

\[
A_m=T_mB_mT_m^T,\qquad Q_m=X^TA_mX=Y_m^TB_mY_m.
\tag{2.4}
\]

Then `A_m` has exactly the three nonzero eigenvalues of `B_m`, because `T_m^TT_m=I_3`.

### Theorem 2 (`QFORM-DIFFUSE-LINDEBERG-RIGIDITY-v1`)

Under (2.1)--(2.4), `Q_m` has a bounded continuous density for every `m>=2`, and

\[
p_{Q_m}\longrightarrow p_\infty
\quad\text{uniformly on }\mathbb R,
\tag{2.5}
\]

where

\[
Q_\infty=G^TBG,\qquad
G\sim N(0,V),\quad V=\operatorname{diag}(v_1,v_2,v_3).
\tag{2.6}
\]

Moreover,

\[
\boxed{\limsup_{m\to\infty}\|p_{Q_m}\|_\infty\le3\sqrt2.}
\tag{2.7}
\]

If equality holds in the limit,
`||p_{Q_m}||_infty -> 3 sqrt(2)`, then necessarily

\[
v_1=v_2=v_3=\frac1{12},
\qquad
|\lambda_1(B)|=|\lambda_2(B)|=|\lambda_3(B)|=1,
\tag{2.8}
\]

and, writing `f_{j,k}^{(m)}` for the physical marginal density and
`mu_{j,k}^{(m)}=EX_{j,k}^{(m)}`,

\[
\boxed{
\frac1m\sum_{k=1}^m
\left\|
f_{j,k}^{(m)}
-
\mathbf1_{[\mu_{j,k}^{(m)}-1/2,\,
          \mu_{j,k}^{(m)}+1/2]}
\right\|_1^2
\longrightarrow0
}
\tag{2.9}
\]

for each bank `j`.

### Proof of the density transport

The Lindeberg theorem and physical-bank independence give

\[
Y_m\Rightarrow G\sim N(0,V).
\tag{2.10}
\]

For the density upgrade use the source-pinned Fresnel--Brascamp--Lieb Theorem F:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Diagonalize `B_m=O_m Lambda_m O_m^T`. The physical eigenframe is `T_mO_m`. Every physical row has squared leverage exactly `1/m`, its full Gram matrix is `I_3`, and there is no residual quadratic part. Hence Theorem F applies with all physical coordinates in its set `I` and gives

\[
|\phi_m(t)|
\le
\min\{1,(4\pi)^{3/2}|t|^{-3/2}\},
\tag{2.11}
\]

because `prod_r |lambda_r(B_m)|>=1`. The right side belongs to `L^1(R)` and is independent of `m`.

By (2.10), `Q_m=>Q_infty`, so `phi_m(t)->phi_infty(t)` pointwise. The same envelope holds for the pointwise limit. Dominated convergence yields

\[
\|\phi_m-\phi_\infty\|_1\to0.
\tag{2.12}
\]

Fourier inversion gives bounded continuous densities and

\[
\|p_{Q_m}-p_\infty\|_\infty
\le(2\pi)^{-1}\|\phi_m-\phi_\infty\|_1\to0.
\tag{2.13}
\]

### Gaussian barrier and equality case

By Theorem 1, every physical marginal variance is at least `v_0=1/12`, so `v_j>=v_0`. Put

\[
C=V^{1/2}BV^{1/2}.
\tag{2.14}
\]

Since every singular value of `B` is at least one,

\[
s_{\min}(C)\ge v_0.
\tag{2.15}
\]

By Sylvester inertia, `C` has eigenvalues `a,b,-c` with `a,b,c>=v_0`. The completed account02/B17 Gaussian global-max argument is source-pinned at

`yspennstate/math-open-problems@cdd0eb22227a505e827a658038a1512897c0ad56`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260924T054220Z-account02-B17-QFORM-auto11/REPORT.md`.

Its monotone-convolution argument gives global maximality at zero, and its cone integral gives

\[
\|p_\infty\|_\infty=p_\infty(0)
\le\frac1{2\sqrt2\,v_0}
=3\sqrt2.
\tag{2.16}
\]

Together with (2.13), this proves (2.7).

If equality occurs in (2.16), the partner cone inequality forces
`a=b=c=v_0`. Therefore

\[
v_0^3
=|\det C|
=(v_1v_2v_3)|\det B|.
\tag{2.17}
\]

Each `v_j>=v_0`, and each eigenvalue magnitude of `B` is at least one. Thus equality in (2.17) forces
`v_1=v_2=v_3=v_0` and `|det B|=1`; the latter, together with the three threshold inequalities, forces all three eigenvalue magnitudes of `B` to equal one. This proves (2.8).

Finally apply Theorem 1 to every physical coordinate. With
`d_{j,k}^{(m)}` equal to the `L^1` distance in (2.9),

\[
\frac1m\sum_k (d_{j,k}^{(m)})^2
\le
8\left(v_{j,m}-\frac1{12}\right)\to0.
\tag{2.18}
\]

This proves (2.9). QED.

The conclusion is a **Gaussian-basin rigidity theorem**, not a universal upper bound for arbitrary rough arrays. A witness above `3 sqrt(2)`, if one exists, must escape at least one ingredient of this chamber: Lindeberg/Gaussianization, three diffuse independent banks, or the threshold/near-unit-interval rigidity.

## 3. Exact disconnected, entrywise-dense rotated stress family

The preceding stability inequality is attained by an exact rotated target family.

Let

\[
n=\frac{(1,2,3)}{\sqrt{14}},
\qquad
B=I-2nn^T
=
\frac17
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix}.
\tag{3.1}
\]

Then

\[
B^2=I,\qquad
\operatorname{spec}(B)=\{1,1,-1\},
\tag{3.2}
\]

and every entry of `B` is nonzero. For every `m`, define
`A_m=T_mBT_m^T`. Every one of the `(3m)^2` physical entries of `A_m` is nonzero, and

\[
\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}.
\tag{3.3}
\]

Now take all physical coordinates iid with density `f_delta` from (1.7). Their support is a union of three separated intervals for every `0<delta<1`; nevertheless it is a valid cap-one probability density. Put

\[
v_\delta=\frac1{12}+\frac{\delta^2}{2}.
\tag{3.4}
\]

The ordinary CLT plus the common Theorem-F envelope gives uniform density convergence to the isotropic Gaussian reflection law. Applying the completed account02/B17 Gaussian formula at variance `v_delta` gives the **exact asymptotic peak**

\[
\boxed{
\lim_{m\to\infty}\|p_{X^TA_mX}\|_\infty
=
\frac1{2\sqrt2\,v_\delta}
=
\frac{3\sqrt2}{1+6\delta^2}.}
\tag{3.5}
\]

Thus the sharp one-dimensional variance penalty propagates into an exact quadratic-form peak penalty.

In particular, choose `delta=1/3`. Then the partner theorem is applied to the actual dense target family (3.1)--(3.4) with

\[
v_{1/3}=\frac5{36},
\qquad
\boxed{
\lim_{m\to\infty}\|p_{X^TA_mX}\|_\infty
=
\frac{9\sqrt2}{5}
=2.545584412271571\ldots .}
\tag{3.6}
\]

Consequently there is an `m_0` such that for every `m>=m_0`,

\[
\boxed{
\|p_{X^TA_mX}\|_\infty<2.55<3\sqrt2.}
\tag{3.7}
\]

This is the requested actual-inequality use of a completed account02/B17 result.

At the other extreme, take any sequence `delta_m>0` with `delta_m->0`, for example
`delta_m=m^{-1/4}`, and use `f_{delta_m}` in the `m`-th member. The variables are uniformly bounded, so Lindeberg is automatic, while `v_{delta_m}->1/12`. The same density transport gives

\[
\boxed{
\|p_{X^TA_mX}\|_\infty\to3\sqrt2.}
\tag{3.8}
\]

Every finite physical input density in this sequence still has disconnected support, and every finite physical matrix is entrywise dense with exact nonzero spectrum `{1,1,-1}`. Therefore this family by itself reconfirms the source-valid universal lower obstruction

\[
\boxed{C_{\rm univ}\ge3\sqrt2.}
\tag{3.9}
\]

It also shows that a proposed sharp proof cannot require connected supports, exact interval marginals, sparse physical matrices, or diagonal alignment. What it may legitimately use near the diffuse sharp face is the quantitative conclusion of (2.9): average squared `L^1` distance from *some translated unit interval* must vanish if this Gaussian-bank mechanism actually saturates `3 sqrt(2)`.

## 4. Corrections and scope

The proof keeps original-coordinate product structure throughout. Spectral rotation is used only inside Theorem F to describe the three-dimensional coefficient frame and, after the physical CLT, inside a centered Gaussian calculation where orthogonal invariance is legitimate.

No law-uniform pointwise `|t|^{-1/2}` estimate is asserted. The only frequency estimate used is the already proved **joint** Theorem-F `|t|^{-3/2}` envelope in the exact three-bank physical frame. No arbitrary-joint coarea cap or positive conditional-density-moment interface is used. The boundary-swap extremizer is a one-dimensional variance extremizer only; it is not promoted to a global extremal-law theorem for QFORM.

Full unrestricted QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN. The remaining sharp-witness search should concentrate on non-Lindeberg or genuinely mesoscopic rough arrays, several non-collinear macroscopic shared rows, or additional active spectrum that survives aggregation; all Gaussian three-bank limits covered above are capped at `3 sqrt(2)`.
