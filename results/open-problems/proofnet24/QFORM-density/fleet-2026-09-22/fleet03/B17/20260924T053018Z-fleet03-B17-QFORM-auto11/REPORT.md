# fleet03/B17 — symmetric-satellite near-diffusive sharp witness

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T053018Z-fleet03-B17-QFORM-auto11`  
Status: `NEW ANALYTIC WITNESS / PARTNER RESULT APPLIED / FULL TARGET OPEN`.

The unrestricted quadratic-form bounded-density conjecture remains open. This report proves a new source-valid stress family showing that the sharp known lower obstruction `3*sqrt(2)` survives even when, with probability tending one, a sample contains many coordinates in remote support components whose separation can be almost diffusive in scale. The construction stays fully within the owner's hypotheses: independent original coordinates, each density bounded by one, and an exact dense target matrix with three eigenvalues of modulus at least one.

The result is not a counterexample and does not prove that `3*sqrt(2)` is the sharp universal constant.

## 1. Exact dense target matrix

Fix
\[
n=\frac{(1,2,3)}{\sqrt{14}},\qquad
B_m=I-\left(2+\frac1m\right)nn^\top .
\]
Let `R_m` be the `3m x 3` synthesis matrix whose rows in bank `j` are `e_j/sqrt(m)`, and define
\[
A_m=R_m B_m R_m^\top .
\]
Because `R_m^T R_m=I_3`, the nonzero spectrum is exactly
\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-(1+1/m)\}.}\tag{1.1}
\]
All entries are nonzero. Indeed, the off-diagonal entries of `B_m` are nonzero and its diagonal entries are
\[
\frac{12-1/m}{14},\qquad \frac{3-2/m}{7},\qquad -\frac{4+9/m}{14}.
\]
Thus every finite `A_m` is an entrywise-dense exact target instance, with one eigenvalue strictly beyond threshold.

If
\[
Y_{m,j}=\frac1{\sqrt m}\sum_{k=1}^m X_{j,k},\qquad j=1,2,3,
\]
then
\[
X^\top A_mX=Y_m^\top B_mY_m.
\]
The three bank sums are independent because the physical banks are disjoint.

## 2. Symmetric three-component cap-one laws

Let `L_m` be any positive sequence such that
\[
L_m\to\infty,\qquad L_m=o(m),
\]
and choose a remote scale `R_m^*` satisfying
\[
R_m^*\to\infty,\qquad \frac{L_m}{m}(R_m^*)^2\to0.\tag{2.1}
\]
Set
\[
\varepsilon_m=\frac{L_m}{m},\qquad \ell_m=1-\varepsilon_m.
\]
For all sufficiently large `m`, define the even density
\[
\begin{aligned}
f_m(x)=&\;\mathbf 1_{[-\ell_m/2,\ell_m/2]}(x)\\
&+\mathbf 1_{[R_m^*-\varepsilon_m/4,\,R_m^*+\varepsilon_m/4]}(x)\\
&+\mathbf 1_{[-R_m^*-\varepsilon_m/4,\,-R_m^*+\varepsilon_m/4]}(x).
\end{aligned}\tag{2.2}
\]
The main interval has length `ell_m`; each satellite interval has length `eps_m/2`. Hence
\[
0\le f_m\le1,\qquad \int f_m=1,
\]
and the law is exactly centered by symmetry.

Use independent copies of this law in all `3m` physical coordinates.

## 3. Almost every product sample contains many remote coordinates

A physical coordinate lands in one of the two satellite components with probability `eps_m`. Let `N_m` be the total number of satellite coordinates among all `3m` inputs. Then
\[
N_m\sim \operatorname{Bin}(3m,\varepsilon_m),\qquad
\mathbb EN_m=3L_m,
\]
and
\[
\frac{N_m}{3L_m}\to1\quad\text{in probability}.\tag{3.1}
\]
Indeed `Var(N_m)/(3L_m)^2 <= 1/(3L_m) ->0`.

The all-main probability is
\[
\mathbb P(N_m=0)=\ell_m^{3m}
=\exp\bigl(-3L_m+o(L_m)\bigr)\to0.\tag{3.2}
\]
Thus asymptotically almost every sample contains remote coordinates, and in fact the number of remote coordinates tends to infinity in probability.

At the same time the support separation tends to infinity by `R_m^* -> infinity`.

A concrete near-diffusive choice is
\[
L_m=\log m,\qquad
R_m^*=\frac{\sqrt m}{(\log m)^{3/4}}.\tag{3.3}
\]
Then `E N_m=3 log m`, the all-main probability is `m^{-3+o(1)}`, and the support gap is of order `sqrt(m)/(log m)^{3/4}`. This scale is larger by a factor `(log m)^{1/4}` than the one-sided scale `sqrt(m)/log m` at which normalized mean drift becomes order one for the same satellite rate.

More generally, condition (2.1) is equivalent to
\[
R_m^*=o\!\left(\sqrt{m/L_m}\right),\tag{3.4}
\]
which is the natural variance-preserving remote scale for an exactly symmetric satellite pair.

## 4. Exact one-coordinate moment bookkeeping

Let `X_m` have density (2.2). Symmetry gives
\[
\mathbb EX_m=0.
\]
The variance is exactly
\[
\boxed{
\sigma_m^2
=\frac{\ell_m^3}{12}
+\varepsilon_m(R_m^*)^2
+\frac{\varepsilon_m^3}{48}.}\tag{4.1}
\]
Therefore under (2.1),
\[
\sigma_m^2\to\frac1{12}.\tag{4.2}
\]

The third absolute moment has the exact decomposition
\[
\boxed{
\mathbb E|X_m|^3
=\frac{\ell_m^4}{32}
+\varepsilon_m(R_m^*)^3
+\frac{\varepsilon_m^3R_m^*}{16}.}\tag{4.3}
\]
Condition (2.1) plus `m eps_m=L_m->infinity` implies
\[
\frac{R_m^*}{\sqrt m}\to0,
\]
because
\[
\frac{(R_m^*)^2}{m}
=\frac{\varepsilon_m(R_m^*)^2}{m\varepsilon_m}
\to0.
\]
Hence
\[
\frac{\mathbb E|X_m|^3}{\sqrt m}\to0.\tag{4.4}
\]
Indeed the leading satellite contribution factors as
\[
\frac{\varepsilon_m(R_m^*)^3}{\sqrt m}
=\bigl[\varepsilon_m(R_m^*)^2\bigr]
\frac{R_m^*}{\sqrt m}\to0,
\]
and the remaining `eps_m^3 R_m^*/sqrt(m)` term vanishes as well.

For the concrete choice (3.3),
\[
\varepsilon_m(R_m^*)^2=(\log m)^{-1/2},\qquad
\frac{\varepsilon_m(R_m^*)^3}{\sqrt m}=(\log m)^{-5/4}.
\]
Thus the bank variance tends to the minimum-variance value `1/12` while the Lyapunov remainder vanishes.

## 5. Uniform local CLT proved directly from the exact characteristic function

Let
\[
\phi_m(s)=\mathbb Ee^{isX_m}.
\]
From (2.2),
\[
\boxed{
\phi_m(s)=
\ell_m\,\operatorname{sinc}(\ell_m s/2)
+\varepsilon_m\,\operatorname{sinc}(\varepsilon_m s/4)
\cos(R_m^*s),}\tag{5.1}
\]
where `sinc(u)=sin(u)/u`.

Let `g_m` be the density of
\[
Y_m=\frac1{\sqrt m}\sum_{k=1}^mX_{m,k}.
\]
Its characteristic function is
\[
\Phi_m(t)=\phi_m(t/\sqrt m)^m.
\]
We prove
\[
\boxed{\|g_m-\gamma_{1/12}\|_\infty\to0,}\tag{5.2}
\]
where `gamma_{1/12}` is the centered Gaussian density of variance `1/12`.

### 5.1 Pointwise convergence

By the third-order Taylor remainder, for fixed `t`,
\[
\phi_m(t/\sqrt m)
=1-\frac{\sigma_m^2t^2}{2m}
+O\!\left(
\frac{\mathbb E|X_m|^3|t|^3}{m^{3/2}}
\right).
\]
Using (4.2)-(4.4),
\[
\Phi_m(t)\to e^{-t^2/24}.\tag{5.3}
\]

### 5.2 Uniform Fourier integrability

For all sufficiently large `m`, `ell_m>=3/4`. On `|s|<=1`, the elementary inequality
\[
\operatorname{sinc}(u)\le1-u^2/7\qquad(|u|\le1/2)
\]
and (5.1) give
\[
|\phi_m(s)|
\le \ell_m|\operatorname{sinc}(\ell_ms/2)|+\varepsilon_m
\le1-c_0s^2
\le e^{-c_0s^2}\tag{5.4}
\]
for one numerical `c_0>0` independent of `m`.

On `1<=|s|<=12`, the main interval has mass tending to one and `|sinc(ell_m s/2)|` is uniformly strictly below one; the satellite mass tends to zero. Hence there is `rho<1` such that eventually
\[
|\phi_m(s)|\le\rho,\qquad1\le|s|\le12.\tag{5.5}
\]

Each of the three interval Fourier transforms is bounded in absolute value by `2/|s|`, so
\[
|\phi_m(s)|\le\frac6{|s|},\qquad |s|\ge12.\tag{5.6}
\]
Consequently,
\[
|\Phi_m(t)|\le e^{-c_0t^2}\qquad(|t|\le\sqrt m),
\]
while
\[
\int_{\sqrt m\le|t|\le12\sqrt m}|\Phi_m(t)|dt
\le22\sqrt m\,\rho^m\to0,
\]
and
\[
\int_{|t|\ge12\sqrt m}|\Phi_m(t)|dt
\le
2\sqrt m\int_{12}^{\infty}(6/s)^m ds
=
\frac{24\sqrt m}{m-1}2^{-m}\to0.\tag{5.7}
\]
Pointwise convergence plus these uniform tails gives
\[
\int_{\mathbb R}|\Phi_m(t)-e^{-t^2/24}|dt\to0.
\]
Fourier inversion proves (5.2). In particular,
\[
\sup_{m\ge m_0}\|g_m\|_\infty<\infty\tag{5.8}
\]
for some `m_0`.

This argument is not the refuted law-uniform pointwise van-der-Corput claim. It is a direct local CLT for this explicit triangular array, using the dominant interval mass and exact characteristic function.

## 6. Exact cone formula and the sharp tip

Let `O` be a fixed orthogonal matrix whose third column is `n`. Then
\[
O^TB_mO=\operatorname{diag}(1,1,-c_m),\qquad c_m=1+1/m.
\]
In eigen-coordinates `z`, the latent density is
\[
\widetilde\rho_m(z)=\prod_{j=1}^3g_m((Oz)_j).
\]
The zero cone is
\[
z_1^2+z_2^2-c_mz_3^2=0.
\]
Resolving the two roots in `z_3` and writing `(z_1,z_2)=r(cos theta,sin theta)` gives the exact coarea identity
\[
\boxed{
 p_m(0)=
\frac1{2\sqrt{c_m}}
\sum_{\pm}
\int_0^{2\pi}\int_0^\infty
\widetilde\rho_m\!\left(
 r\cos\theta,r\sin\theta,\pm r/\sqrt{c_m}
\right)
\,dr\,d\theta.}\tag{6.1}
\]

Uniform convergence (5.2) handles every bounded radial range. The tail is uniform as well. Along any cone ray, after rotating back to the three independent bank coordinates, the ray vector has Euclidean norm at least one, so one coordinate coefficient has magnitude at least `1/sqrt(3)`. By (5.8), if that coefficient is `a`,
\[
\prod_{j=1}^3g_m(ra_j)\le C^2g_m(ra).
\]
Since `EY_m^2=sigma_m^2` stays bounded,
\[
\int_M^\infty g_m(ra)dr
\le\frac{\sigma_m^2}{|a|^3M^2}
\le\frac{C_1}{M^2}.\tag{6.2}
\]
Thus the cone tails in (6.1) are uniformly `O(M^{-2})`.

Passing to the Gaussian limit in (6.1) gives
\[
 p_m(0)-\frac{6}{\sqrt{2+1/m}}\to0.\tag{6.3}
\]
Indeed, for an isotropic Gaussian of variance `1/12` and signature `(1,1,-c_m)`, direct integration gives
\[
 p^{G}_{m}(0)=\frac{1}{2(1/12)\sqrt{1+c_m}}
=\frac6{\sqrt{2+1/m}}.
\]
Hence
\[
\boxed{p_m(0)\longrightarrow3\sqrt2.}\tag{6.4}
\]
In particular,
\[
\boxed{\liminf_m\|p_{X^TA_mX}\|_\infty\ge3\sqrt2.}\tag{6.5}
\]
This recovers the sharp known universal obstruction using a family in which the all-main product cell has probability tending zero and the number of remote coordinates tends to infinity.

For each sufficiently large fixed `m`, the bank density is an `m`-fold convolution of a finite linear combination of interval indicators, hence compactly supported and piecewise polynomial with increasing smoothness. Fixed-amplitude stationary phase for the nondegenerate three-dimensional latent quadratic form therefore supplies a continuous output density for this constructed family. The constants may depend on `m`; no law-uniform pointwise phase estimate is asserted. Full-target continuity remains open.

## 7. Completed fleet04/B17 result applied to an actual inequality

The designated completed partner result is:

- repository `yspennstate/math-open-problems`;
- commit `4be63022324b82f254f1d7a4353a3e883f08d10a`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260924T011922Z-fleet04-B17-QFORM-r6/REPORT.md`;
- theorem `QFORM-MACROFRAGMENTED-STRICTSLACK-DENSE-WITNESS-v1`.

Its exact positive-mixture inequality is
\[
\|p_Q\|_\infty
\ge \ell_m^{3m-2}\|p_{Q_m^0}\|_\infty,\tag{7.1}
\]
where `Q_m^0` uses the same matrix and centered unit-interval physical inputs.

The identical all-main argument applies to the present symmetric three-component law, because conditioning on every coordinate being in the main interval again gives exactly `X=ell_m U`. Therefore (7.1) holds here verbatim.

Now `m eps_m=L_m->infinity`, so
\[
\ell_m^{3m-2}
=\exp\bigl(-3L_m+o(L_m)\bigr)\to0.\tag{7.2}
\]
The completed centered-bank result gives `||p_{Q_m^0}||_infty ->3sqrt(2)`, so the partner certificate (7.1) itself decays to zero. In contrast, the direct cone analysis above proves
\[
p_m(0)\to3\sqrt2.
\]
For centered unit intervals the same cone/local-CLT argument gives `p_{Q_m^0}(0)->3sqrt(2)`, so the all-main contribution to the actual tip equals
\[
\ell_m^{3m-2}p_{Q_m^0}(0)
=\exp\bigl(-3L_m+o(L_m)\bigr)(3\sqrt2+o(1))\to0.
\]
Therefore the satellite-containing selection patterns contribute
\[
p_m(0)-\ell_m^{3m-2}p_{Q_m^0}(0)
\longrightarrow3\sqrt2.\tag{7.3}
\]
Equivalently, the ratio between the actual sharp tip and the all-main contribution grows as
\[
\boxed{\exp\bigl(3L_m+o(L_m)\bigr).}\tag{7.4}
\]
This quantitatively proves that a proof of the full conjecture cannot localize the sharp obstruction to a high-probability central product cell.

## 8. Why symmetry materially enlarges the stress regime

For a one-sided satellite of mass `eps_m=L_m/m` centered at distance `R_m^*`, the normalized bank mean is of order
\[
\sqrt m\,\varepsilon_mR_m^*
=\frac{L_mR_m^*}{\sqrt m}.
\]
Recovering the centered minimum-variance Gaussian requires
\[
R_m^*=o(\sqrt m/L_m).
\]

For the symmetric satellite pair used here, the mean vanishes exactly. The leading condition is only
\[
\varepsilon_m(R_m^*)^2\to0,
\]
which allows
\[
\boxed{R_m^*=o(\sqrt{m/L_m}).}\tag{8.1}
\]
This enlarges the admissible remote scale by a factor `sqrt(L_m)` at the boundary. Hence the present construction genuinely explores a more remote fragmentation regime than the one-sided almost-sure-satellite family.

## 9. Scope and remaining gap

This proves the supporting theorem

`QFORM-SYMMETRIC-SATELLITE-NEAR-DIFFUSIVE-SHARP-WITNESS-v1`:

> There exist entrywise-dense exact target matrices with nonzero spectrum
> `{1,1,-(1+1/m)}` and independent cap-one, three-component, disconnected
> input densities for which the number of remote coordinates tends to
> infinity in probability, the all-main product probability tends to zero,
> the remote support separation can be any divergent scale
> `R_m=o(sqrt(m/L_m))` with `L_m->infinity`, and nevertheless the
> quadratic-form density satisfies `p_m(0)->3sqrt(2)`.

The theorem constrains proof reductions based on compact support, connected support, fragment count, remote-support probability, or domination by a central cell. It does not improve the universal lower bound beyond `3sqrt(2)` and does not prove the full upper bound.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.  
Next B17 witness mechanisms: negative two-sheet off-tip peaks, several genuinely macroscopic non-collinear shared rows, or additional active spectrum that survives bank aggregation.
