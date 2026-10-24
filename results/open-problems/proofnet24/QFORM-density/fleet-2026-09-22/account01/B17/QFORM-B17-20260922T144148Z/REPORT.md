# account01/B17 — one-heavy-coordinate mesoscopic saddle theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
**Run:** `QFORM-B17-20260922T144148Z`  
**Assignment:** sharp constant and witnesses  
**Classification:** `AUXILIARY_ONLY / MESOSCOPIC_LOCAL_NO_ESCAPE`  
**Full conjecture:** OPEN / NOT PROVED  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`

## 1. Source pins and corrections

Control was read from `yspennstate/math-research-brain` main; the coherent control state used for the derivation was commit `24015c84e6288c6138b68924f26f41e42c18b320`, with later correction commit `4db9b9207829d324d23e36afcf470b0ffb8b0951` also inspected before publication. No refuted pointwise-Fresnel, fiber-supremum, conditional-cap, single-Schur, local-cross-rank3, phase-Wiener, bounded-diameter, or bounded-fragment-count reduction is used.

Named partner actually applied: `account02/B17`, canonical report `yspennstate/math-open-problems@4ea3583ef79cc28fc933c9dc6870e63475f94ecd`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T141434Z-650545cc/REPORT.md`. Its exact per-bank saddle expectations and first-order coefficients are used below, and are independently rederived here from the Gaussian cone measure.

## 2. Source-valid mesoscopic family

Let all physical inputs be iid `U[-1/2,1/2]`, so every one-dimensional input density is exactly one. For each bank `j=1,2,3`, fix a leverage parameter `theta_j in [0,1)` and, for integer `m>=1`, define

\[
S_{j,m}=\sqrt{\theta_j}\,U_{j,0}+\sqrt{\frac{1-\theta_j}{m}}\sum_{k=1}^m U_{j,k}.
\]

The three banks are independent. The coefficient vector of each bank has squared norm

\[
\theta_j+m\frac{1-\theta_j}{m}=1.
\]

Hence, if `r_{j,m}` denotes that coefficient vector on bank `j`, the physical matrix

\[
A_m=r_{1,m}r_{1,m}^T+r_{2,m}r_{2,m}^T-r_{3,m}r_{3,m}^T
\]

has nonzero spectrum exactly `{1,1,-1}`. Therefore

\[
Q_m=S_{1,m}^2+S_{2,m}^2-S_{3,m}^2
\]

is an exact target-admissible finite-dimensional family for every `m`.

As `m -> infinity`, the diffuse part of each bank converges locally to a centered Gaussian of variance `(1-theta_j)/12`. Thus

\[
S_{j,m}\Longrightarrow H_{\theta_j}:=\sqrt{\theta_j}\,U_j+\sqrt{1-\theta_j}\,G_j,
\]

where `U_j~U[-1/2,1/2]`, `G_j~N(0,1/12)`, all independent. The Gaussian variable is only a limit object; every physical finite-`m` coordinate remains density-one uniform. The Gaussian-dominated local CLT/Edgeworth remainder used in the partner report survives convolution with the fixed heavy uniform coordinate, so the zero-density of `Q_m` converges to the cone-density functional `P(theta_1,theta_2,theta_3)` below, uniformly on compact subsets of `[0,1)^3`.

## 3. Exact small-leverage expansion of one bank

Put `sigma^2=1/12` and

\[
\gamma(x)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-x^2/(2\sigma^2)}=\sqrt{6/\pi}\,e^{-6x^2},
\qquad z=x/\sigma=\sqrt{12}\,x.
\]

The characteristic function of `H_theta` is

\[
\widehat h_\theta(t)=e^{-(1-\theta)t^2/24}\,\operatorname{sinc}(\sqrt\theta\,t/2).
\]

Relative to the baseline Gaussian,

\[
e^{\theta t^2/24}\operatorname{sinc}(\sqrt\theta\,t/2)
=1-\frac{\theta^2t^4}{2880}-\frac{\theta^3t^6}{181440}+O(\theta^4(1+|t|^8))
\]

in every Gaussian-weighted `L^1` Fourier seminorm on `0<=theta<=theta_0<1`. Fourier inversion therefore gives, in Schwartz norms,

\[
h_\theta(x)=\gamma(x)\left[
1-\frac{\theta^2}{20}H_4(z)+\frac{\theta^3}{105}H_6(z)+O(\theta^4 P(z))
\right],
\]

where

\[
H_4(z)=z^4-6z^2+3,
\qquad
H_6(z)=z^6-15z^4+45z^2-15,
\]

and `P` is a fixed polynomial with Gaussian-dominated remainder. The coefficient `-theta^2/20` is exactly the partner's bank Edgeworth coefficient `-1/(20m)` with the formal replacement `1/m -> theta^2`; this is because the standardized fourth cumulant is `-(6/5)theta^2`.

## 4. Exact cone functional

For even one-dimensional densities `f_1,f_2,f_3`, the density at zero of

\[
X_1^2+X_2^2-X_3^2
\]

is

\[
T(f_1,f_2,f_3)
=\int_0^\infty f_3(r)\int_0^{2\pi}f_1(r\cos\phi)f_2(r\sin\phi)\,d\phi\,dr.
\]

For the baseline Gaussian this gives

\[
T(\gamma,\gamma,\gamma)=\frac{1}{2\sqrt2\sigma^2}=3\sqrt2.
\]

Under the normalized Gaussian cone measure, write `z_3=sqrt(12)r`, `z_1=z_3 cos(phi)`, `z_2=z_3 sin(phi)`. Then

\[
E z_3^2=\frac12,\quad E z_3^4=\frac34,\quad E z_3^6=\frac{15}{8},
\]

and, using `E cos^2 phi=1/2`, `E cos^4 phi=3/8`, `E cos^6 phi=5/16`,

\[
E z_1^2=\frac14,\quad E z_1^4=\frac9{32},\quad E z_1^6=\frac{75}{128},
\]

with the same moments for `z_2`. Hence

\[
E H_4(z_1)=E H_4(z_2)=\frac{57}{32},\qquad E H_4(z_3)=\frac34,
\]

and

\[
E H_6(z_1)=E H_6(z_2)=-\frac{945}{128},\qquad E H_6(z_3)=-\frac{15}{8}.
\]

The `H_4` expectations are exactly the completed `account02/B17` saddle coefficients applied here; the `H_6` expectations provide the new third-order term.

## 5. Main theorem: strict local mesoscopic no-escape wedge

Let

\[
P(\theta_1,\theta_2,\theta_3)
:=T(h_{\theta_1},h_{\theta_2},h_{\theta_3}).
\]

As `eps=max(theta_1,theta_2,theta_3)->0`, multilinearity of `T` and the fact that every one-bank perturbation begins at quadratic order give

\[
\boxed{
\frac{P(\theta_1,\theta_2,\theta_3)}{3\sqrt2}
=1
-\frac{57}{640}(\theta_1^2+\theta_2^2)
-\frac{3}{80}\theta_3^2
-\frac{9}{128}(\theta_1^3+\theta_2^3)
-\frac{1}{56}\theta_3^3
+O(\varepsilon^4).
}
\]

Indeed the quadratic terms are `-(1/20) E H_4`, while the cubic terms are `(1/105) E H_6`. Cross-bank products first appear at order four.

In the symmetric one-heavy-coordinate path `theta_1=theta_2=theta_3=theta`,

\[
\boxed{
\frac{P(\theta,\theta,\theta)}{3\sqrt2}
=1-\frac{69}{320}\theta^2-\frac{71}{448}\theta^3+O(\theta^4).
}
\]

Every displayed nonzero coefficient is negative. Therefore the fully diffuse Gaussian endpoint `theta=0` is a strict local maximum along every source-valid one-heavy-coordinate mesoscopic direction. In particular, there exists `delta>0` such that

\[
0<\max_j\theta_j<\delta
\quad\Longrightarrow\quad
P(\theta_1,\theta_2,\theta_3)<3\sqrt2.
\]

Because `Q_m` is target-admissible and `p_{Q_m}(0)->P(theta_1,theta_2,theta_3)`, the same strict inequality holds for all sufficiently large finite `m` once a fixed nonzero small leverage triple is chosen.

## 6. Why this is new relative to the preceding B17 wedge

The partner theorem excluded first-order escapes produced by unequal diffuse bank sizes, `O(1/m)` interval translations and legal `O(1/m)` outward eigenvalue perturbations. Those are still Lindeberg perturbations.

The present family is different: a **single physical coordinate retains fixed leverage `theta_j` as `m->infinity`**, so the limit is genuinely non-Lindeberg/mesoscopic. The theorem proves that introducing such a heavy coordinate does not beat the current lower-bound ceiling infinitesimally; its first effect is second order and strictly downward, with exact anisotropic Hessian

\[
-\operatorname{diag}\left(\frac{57}{320},\frac{57}{320},\frac{3}{40}\right)
\]

for the normalized peak ratio.

Thus a witness above `3sqrt(2)`, if it exists, must leave not only the perturbative diffuse basin but also this local one-heavy-coordinate mesoscopic basin. Plausible remaining sharp-witness mechanisms are: finite heavy leverage bounded away from zero, several interacting heavy coordinates in one or more spectral directions, or fragmented density-one supports whose geometry survives aggregation.

## 7. Scope

This is a sharp supporting theorem, not a proof of the universal QFORM conjecture and not evidence that `3sqrt(2)` is globally sharp. It does not use bounded-fragment localization, pointwise oscillatory decay, conditional density caps after rotation, or any other currently refuted reduction. Continuity of the full target density remains separate.
