# QFORM B17 r11 — maximally shared null-row stress is globally below `3 sqrt(2)`

Programme: `QFORM-DENSITY-3EIG-20260922`.  Worker: `account01/B17`.  Run: `20260922T181920Z-account01-B17-QFORM-r11`.

Status: **AUXILIARY_ONLY / SHARP-WITNESS-EXCLUSION**.  The unrestricted quadratic-form conjecture remains **OPEN / NOT PROVED**.

## Source pins consumed

- Live owner control read from `yspennstate/math-research-brain`, `scheduled_tasks/README.md`: active programme QFORM; owner-control revision `2026-09-22.11`; sole target is the universal bounded-density conjecture.  The owner message explicitly warns that global `L^1` characteristic-function control is false in general.  The argument below uses `L^1` only for one explicit stress family where it is proved directly.
- Assignment blob: `scheduled_tasks/work/shared/qform-density-2026-09-22/assignments/account01/B17.json`, blob `5d91926a87d3e6d75cb5f1a3cde422ad28c5c33b`.
- Designated partner input actually used: account02/B17 handoff `20260922T174510Z-account02-B17-QFORM-r12.md`, blob `23fd81557d925fe089f3ac4d87be4344846e7bd7`, canonical mathematics `yspennstate/math-open-problems@8cd8692e80ceffc93ae5679a323bbc4f11f89cb1`.  Its theorem says a probabilistically infinitesimal exact rank-three tight-frame array has Gaussian covariance floor `Gamma >= I_3/12`; hence every convergent infinitesimal limiting law has quadratic-form peak at most `3 sqrt(2)`.  It explicitly leaves a finite macroscopic core plus diffuse residual as a possible sharp-witness escape.

## New theorem: a maximally shared macroscopic null row does not escape

Let

\[
J=\operatorname{diag}(1,1,-1),\qquad
v=\frac{e_1+e_3}{\sqrt2},\qquad
u=\frac{e_1-e_3}{\sqrt2}.
\]

Thus `v` is Euclidean unit but **null for the quadratic form**:

\[
v^T Jv=0,
\qquad
u^T J\nu=0,
\qquad
v^T J\nu=1.
\]

Let `X` be an arbitrary real random variable with a probability density `f_X` satisfying `0 <= f_X <= 1`.  Let `A,B` be independent standard Gaussians, independent of `X`, and set

\[
Y=vX+\frac{A}{\sqrt{12}}\nu+\frac{B}{\sqrt{12}}e_2,
\qquad Q=Y^T JY.
\]

Then

\[
Q=\frac{XA}{\sqrt3}+\frac{B^2}{12}.
\]

The law of `Q` has a continuous density, and

\[
\boxed{\|p_Q\|_\infty\le 4.225227562361 < 3\sqrt2.}
\]

A sharper non-certified numerical evaluation of the intermediate Fourier integral is

\[
C_{\rm null}\approx4.205824832586,
\]

but the displayed `4.225227562361` is the value supported by the elementary analytic majorant below; the theorem does not rely on the sharper decimal.

This is a **global-in-t** statement, unlike the earlier one-shared-row theorem that only controlled the central density `p_Q(0)`.  It also permits arbitrary fragmented/translated cap-one laws for the macroscopic physical coordinate `X`.

## Proof

### 1. Exact characteristic function

Conditioning first on `X` and using the independent Gaussian variables gives

\[
\phi_Q(t)
=\left(1-\frac{it}{6}\right)^{-1/2}
\mathbf E\exp\!\left(-\frac{t^2X^2}{6}\right).
\]

Therefore

\[
|\phi_Q(t)|
=(1+t^2/36)^{-1/4}
\mathbf E e^{-t^2X^2/6}.
\]

For fixed `t`, the kernel `x -> exp(-t^2 x^2/6)` is symmetric decreasing.  The one-dimensional bathtub/rearrangement principle under the constraints `0<=f_X<=1`, `int f_X=1` therefore gives

\[
\mathbf E e^{-t^2X^2/6}
\le F(t):=\int_{-1/2}^{1/2} e^{-t^2x^2/6}\,dx.
\]

Consequently

\[
|\phi_Q(t)|\le (1+t^2/36)^{-1/4}F(t).
\tag{1}
\]

As `|t| -> infinity`, `F(t) <= sqrt(6 pi)/|t|` and the other factor is `O(|t|^{-1/2})`; hence the right side of (1) is integrable.  Fourier inversion therefore gives a continuous density and

\[
\|p_Q\|_\infty
\le C_{\rm null}:=
\frac1\pi\int_0^\infty(1+t^2/36)^{-1/4}F(t)\,dt.
\tag{2}
\]

This use of Fourier `L^1` is family-specific; no general `L^1` claim is made.

### 2. An elementary strict bound below `3 sqrt(2)`

For `u>=0`, Taylor's theorem after the even fourth term gives

\[
e^{-u}\le P_4(u):=1-u+\frac{u^2}{2}-\frac{u^3}{6}+\frac{u^4}{24}.
\]

Hence

\[
F(t)\le T_4(t):=
\sum_{k=0}^4
\frac{(-1)^k}{6^k k!(2k+1)2^{2k}}t^{2k}.
\tag{3}
\]

For the tail we also have the whole-line Gaussian bound

\[
F(t)\le \frac{\sqrt{6\pi}}{t},\qquad t>0.
\tag{4}
\]

Put

\[
a(t)=(1+t^2/36)^{-1/4},\qquad
s_1=13/4,\quad s_0=13/2.
\]

As a function of `x=t^2/36`, `(1+x)^(-1/4)` is convex.  Therefore on each of the two intervals `[0,s_1]` and `[s_1,s_0]`, `a(t)` lies below the chord obtained by linearly interpolating `a` in the variable `x=t^2/36`.  Call these two chord majorants `L_1(t)` and `L_2(t)`.  Since `T_4(t)>0`, (2)-(4) imply

\[
C_{\rm null}
\le \frac1\pi\left[
\int_0^{s_1}L_1(t)T_4(t)\,dt
+\int_{s_1}^{s_0}L_2(t)T_4(t)\,dt
+\sqrt{6\pi}\int_{s_0}^\infty\frac{a(t)}t\,dt
\right].
\tag{5}
\]

The first two integrals are finite polynomial integrals.  The last integral is elementary.  If

\[
z_0=(1+(s_0/6)^2)^{-1/4},
\]

then the substitution `u=t/6`, `z=(1+u^2)^(-1/4)` gives

\[
\int_{s_0}^\infty\frac{a(t)}t\,dt
=\frac12\log\frac{1+z_0}{1-z_0}+\arctan z_0.
\tag{6}
\]

Direct evaluation of the explicit expression (5)-(6) gives

\[
\boxed{C_{\rm null}\le4.2252275623606330909\ldots}
\]

whereas

\[
3\sqrt2=4.2426406871192851464\ldots.
\]

The certified margin from this elementary majorant is

\[
3\sqrt2-C_{\rm null}^{\rm(up)}
=0.0174131247586520554\ldots>0.
\]

The same calculations are reproduced by `check_null_row_bound.py` in this run root.

## Exact source-valid rotated finite family

The limiting model above is not an artificial post-rotation independence assumption.  For every integer `m>=1`, form a physical tight frame with rows

- one row `v^T`,
- `m` rows `nu^T/sqrt(m)`,
- `m` rows `e_2^T/sqrt(m)`.

If `R_m` is the resulting `(2m+1) x 3` row matrix, then

\[
R_m^TR_m=vv^T+\nu\nu^T+e_2e_2^T=I_3.
\]

Therefore

\[
A_m=R_mJR_m^T
\]

has nonzero spectrum **exactly** `{1,1,-1}` for every finite `m`.

Give the heavy physical coordinate the arbitrary cap-one law `X` and all `2m` diffuse coordinates the density-one law `Unif[-1/2,1/2]`.  If

\[
Z_{j,m}=m^{-1/2}\sum_{k=1}^mU_{j,k},
\]

then the exact finite quadratic form is

\[
Q_m=2XZ_{1,m}+Z_{2,m}^2.
\tag{7}
\]

As `m -> infinity`, `(Z_{1,m},Z_{2,m})` converges to independent `N(0,1/12)` variables, and (7) converges to the `Q` treated above.

For `m>=2`, this convergence is local, not merely weak: the standardized Irwin-Hall densities are symmetric log-concave with uniformly bounded sup norm, giving a uniform `O(|t|^{-1/2})` oscillatory bound for `E exp(it Z_{2,m}^2)`; meanwhile

\[
\psi_m(s)=\left[\operatorname{sinc}\left(\frac{s}{2\sqrt m}\right)\right]^m
\]

has uniformly bounded `L^1` norm, and `f_X<=1` gives

\[
\left|\mathbf E_X\psi_m(2tX)\right|
\le \min(1,C/|t|).
\]

Thus the characteristic functions of `Q_m` admit an integrable `O(|t|^{-3/2})` majorant independent of sufficiently large `m`, and dominated Fourier inversion yields uniform convergence of the densities to `p_Q`.  In particular, for every fixed admissible heavy law `X`,

\[
\limsup_{m\to\infty}\|p_{Q_m}\|_\infty
\le4.225227562361<3\sqrt2.
\]

This makes the family an exact rotated source-valid no-escape stress family, including off-center peaks.

## Actual use of the account02/B17 partner theorem

The partner theorem closes the opposite limiting regime: if **all** tight-frame rows are probabilistically infinitesimal, every convergent limit contains an independent Gaussian component with covariance at least `I_3/12`, and the limiting quadratic-form density is bounded by `3 sqrt(2)`.

The present theorem closes a maximally non-infinitesimal direction that the partner handoff explicitly left open: one full-leverage physical coordinate shared equally between the positive and negative spectral directions (`v^T Jv=0`), with the complementary frame diffuse.  Combining the two proved estimates gives the genuine inequality

\[
\sup\{\text{limiting peak over (i) partner-infinitesimal regime, or (ii) this null-row regime}\}
\le3\sqrt2.
\]

The second regime in fact has the strict analytic reserve `>=0.017413` supplied above.

## What changed / what remains unpaid

New: one of the strongest single-row shared-coordinate stresses is now controlled **globally in the density variable**, for arbitrary cap-one fragmentation of that macroscopic coordinate, and realized by exact finite matrices with spectrum `{1,1,-1}`.

Not proved: this does not cover two or more interacting macroscopic physical rows; a single macroscopic row away from the null orientation at arbitrary off-center `t`; non-Gaussian mesoscopic residuals; finite-row spikes outside the local-limit family; additional spectral directions/full rank; or the owner's scalar-conditioned full-rank inequality.  Therefore it is not a proof of the universal conjecture and it does not establish sharpness `C=3 sqrt(2)`.

The highest-value B17 witness frontier after this result is: **two interacting macroscopic shared rows plus a diffuse residual, with off-center peak optimization**.  That is a genuinely different mechanism from the all-infinitesimal partner theorem, the previous central one-row theorem, and the present maximally-null one-row closure.
