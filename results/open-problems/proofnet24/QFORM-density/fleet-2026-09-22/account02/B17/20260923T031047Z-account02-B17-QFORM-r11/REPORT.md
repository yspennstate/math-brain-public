# QFORM B17 — exact finite extremizer for the one-heavy majority-sign family

Run: `20260923T031047Z-account02-B17-QFORM-r11`  
Account/slot: `account02/B17`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `NEW_SUPPORTING THEOREM`; full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains separate.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target family and the unpaid point

For every integer `m>=1`, let

\[
A_m=\operatorname{diag}(1,J_m/m,-J_m/m).
\tag{1.1}
\]

Every `J_m/m` has spectrum `{1,0,...,0}`, so every finite matrix has exact nonzero spectrum

\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}.}
\tag{1.2}
\]

On the singleton coordinate put an arbitrary probability density `0<=f<=1`; it may be translated, disconnected, unbounded and arbitrarily fragmented. On the two `m`-coordinate banks put iid centered unit intervals, all physical coordinates independent. Write

\[
S_m=m^{-1/2}\sum_{j=1}^mU_j,\qquad
T_m=m^{-1/2}\sum_{j=1}^mV_j.
\]

Then exactly

\[
Q_{m,f}=X_f^2+S_m^2-T_m^2.
\tag{1.3}
\]

This is a source-valid original-coordinate product family; no spectral rotation is used to manufacture independence.

The preceding same-slot theorem
`yspennstate/math-open-problems@06aea167c49a7d7574f1c2f518c756f22413371a`
proved only the Gaussian-completion upper bound

\[
\sup_f\|p_{X_f^2+G_+^2-G_-^2}\|_\infty
\le C_{\rm old}
=\frac6\pi\left(\frac52+\log\frac43-\gamma_E\right)
<3\sqrt2,
\tag{1.4}
\]

with `G_+,G_- iid N(0,1/12)`. A newly completed finite-transfer result in the same slot shows eventual no-overshoot uniformly in `m`-dependent heavy laws, but does not identify the exact extremizing heavy law or the sharp branch constant.

The theorem below does both, for every finite `m` and for the Gaussian limit.

## 2. Main theorem

### `QFORM-ONE-HEAVY-MAJORITY-EXACT-EXTREMIZER-v1`

For every `m>=1`, among **all** heavy-coordinate probability densities `0<=f<=1` and all output levels,

\[
\boxed{
\sup_{0\le f\le1,\int f=1}\|p_{Q_{m,f}}\|_\infty
=p_{Q_{m,U}}(0),
\qquad U\sim\mathrm{Unif}[-1/2,1/2].
}
\tag{2.1}
\]

Thus arbitrary fragmentation, translations and remote support of the heavy majority-sign coordinate never improve this exact finite family. The sharp heavy law is the centered unit interval, and the sharp output level is zero.

The same statement holds when both diffuse banks are replaced by independent `N(0,1/12)` variables. The exact Gaussian-completion sharp constant is therefore

\[
\boxed{
C_{\rm maj}^{\sharp}
=\frac{12}{\pi}\int_0^{1/2}K_0(6x^2)\,dx
=3.5306641257709305771\ldots
<3\sqrt2.
}
\tag{2.2}
\]

This improves the earlier valid but nonsharp upper bound (1.4) by about `0.6910157378`; the actual gap from `3sqrt(2)` in this branch is about `0.7119765613`.

Moreover, as `m->infinity`,

\[
\boxed{
 p_{Q_{m,U}}(0)
 =C_{\rm maj}^{\sharp}-\frac{\kappa_{\rm maj}}m+O(m^{-2}),
}
\tag{2.3}
\]

where

\[
\boxed{
\kappa_{\rm maj}
=\frac{12}{\pi}\left[
\frac18K_0(3/2)
+\int_0^{1/2}\left(\frac1{20}+\frac{36}{5}x^4\right)K_0(6x^2)\,dx
\right]>0
}
\tag{2.4}
\]

and numerically `kappa_maj=0.3552683704782763559...` only as a check. Thus the exact finite branch approaches its Gaussian-completion sharp value from **below at first order**.

This does not prove that every finite value in the scalar sequence (2.1) is below `3sqrt(2)`, although `m=1` is the diagonal control and (2.3) excludes all sufficiently large `m`. The remaining finite-bank question has now been reduced to one explicit centered-interval sequence; no adversarial heavy-law optimization remains.

## 3. Monotonicity of the residual difference-square kernel

Let `h_m` be the density of `S_m`. The centered interval density is even and nonincreasing on `[0,infinity)`. Convolution preserves this property. One elementary induction is enough: if `h` is even decreasing and `I_a=1_{[-a,a]}`, then for `x>0`, wherever derivatives exist,

\[
(h*I_a)'(x)=h(x+a)-h(x-a)\le0,
\]

where for `x<a`, evenness gives `h(x-a)=h(a-x)>=h(a+x)`. Scaling preserves the property. Hence every `h_m` is even and nonincreasing on `[0,infinity)`.

The square `S_m^2` has density, for `u>0`,

\[
a_m(u)=\frac{h_m(\sqrt u)}{\sqrt u}.
\tag{3.1}
\]

Both numerator monotonicity and the factor `u^{-1/2}` show that `a_m` is nonincreasing. Therefore the iid difference-square density

\[
k_m(w):=p_{S_m^2-T_m^2}(w)
\tag{3.2}
\]

is even, and for `w>=0`,

\[
 k_m(w)=\int_0^\infty a_m(u)a_m(u+w)\,du.
\tag{3.3}
\]

The integrand decreases pointwise in `w`, so

\[
\boxed{k_m(w)\text{ is nonincreasing in }|w|.}
\tag{3.4}
\]

The logarithmic singularity at `w=0` is harmless for the integrations below; truncation and monotone convergence may be used whenever desired.

Exactly the same argument applies to the Gaussian limit, where

\[
\boxed{k_\infty(w)=\frac6\pi K_0(6|w|).}
\tag{3.5}
\]

## 4. Exact bathtub optimizer at every output

Condition on the heavy coordinate. For every real `s`,

\[
p_{Q_{m,f}}(s)=\int_{\mathbb R}f(x)k_m(s-x^2)\,dx.
\tag{4.1}
\]

For fixed `s`, (3.4) says the kernel is ordered solely by the distance `|s-x^2|`. Hence the exact cap-one bathtub optimizer is the measure-one set of points closest to the level `x^2=s`.

Define

\[
m_s(r)=|\{x:\ |x^2-s|\le r\}|.
\]

For `s>=0` and `r<s`,

\[
m_s(r)=2(\sqrt{s+r}-\sqrt{s-r}),
\tag{4.2}
\]

and for `r>=s`, `m_s(r)=2\sqrt{s+r}`. Solving `m_s(r)=1` yields:

* for `s<=1/8` (including every negative `s` after observing that `|s-x^2|=|s|+x^2`), the optimizer is
  \[
  E_s=[-1/2,1/2];
  \tag{4.3}
  \]
* for `s>=1/8`, the optimizer is
  \[
  E_s=[-a,-b]\cup[b,a],
  \qquad a-b=1/2,\quad a^2+b^2=2s,
  \tag{4.4}
  \]
  equivalently `b=(-1+sqrt(16s-1))/4`, `a=b+1/2`.

Thus

\[
\sup_f p_{Q_{m,f}}(s)=\int_{E_s}k_m(s-x^2)\,dx.
\tag{4.5}
\]

This two-shell description is **specific to this kernel and this one-coordinate bathtub problem**. It does not contradict the live correction ruling out a universal fixed-fragment-count localization theorem.

## 5. The outer shells can never win

Set `s_0=1/8`. For `s>=s_0`, equip `E_s` with Lebesgue measure (its total mass is one) and let

\[
R_s=|x^2-s|.
\]

For `0<=r<s_0<=s`, (4.2) gives

\[
\Pr(R_s\le r)=2(\sqrt{s+r}-\sqrt{s-r}),
\]

and differentiation in `s` gives

\[
\frac1{\sqrt{s+r}}-\frac1{\sqrt{s-r}}<0.
\tag{5.1}
\]

For `r>=s_0`, `Pr(R_{s_0}<=r)=1`, since on `[-1/2,1/2]` one has `|x^2-s_0|<=s_0`. Therefore

\[
\boxed{R_s\text{ is stochastically larger than }R_{s_0},\qquad s>=s_0.}
\tag{5.2}
\]

Since `k_m` is decreasing,

\[
\sup_f p_{Q_{m,f}}(s)
\le \int_{-1/2}^{1/2}k_m(s_0-x^2)\,dx
=p_{Q_{m,U}}(s_0),
\qquad s>=1/8.
\tag{5.3}
\]

For `s<0`, the centered interval is already the exact optimizer, so

\[
\sup_f p_{Q_{m,f}}(s)=p_{Q_{m,U}}(s).
\tag{5.4}
\]

For `0<=s<=1/8`, the same identity holds by (4.3).

## 6. Applying the completed separated symmetric-unimodal theorem

The completed same-slot theorem

`yspennstate/math-open-problems@84ffc0f291ae192f4d82742ae6909943f6710bc7`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T235536Z-r12-symmetric-unimodal/REPORT.md`,

proves that if independent `Y_1,Y_2,Y_3` have even densities nonincreasing on `[0,infinity)`, then

\[
\|p_{Y_1^2+Y_2^2-Y_3^2}\|_\infty=p(0).
\tag{6.1}
\]

Apply it to

\[
Y_1=U\sim\mathrm{Unif}[-1/2,1/2],\qquad Y_2=S_m,\qquad Y_3=T_m.
\]

All three densities have the required monotonicity by Section 3. Therefore

\[
p_{Q_{m,U}}(s)\le p_{Q_{m,U}}(0)\quad\text{for every }s.
\tag{6.2}
\]

Combining (5.3), (5.4), and (6.2) proves the upper inequality in (2.1). Equality is attained by taking the centered unit interval heavy law and output `s=0`. Hence (2.1) is exact.

This is stronger than the preceding Gaussian-completion bound: it identifies the actual branch extremizer rather than merely a universal envelope.

## 7. Exact Gaussian sharp constant

For independent `G_+,G_-~N(0,1/12)`,

\[
G_+^2-G_-^2=(G_++G_-)(G_+-G_-),
\]

and the two factors are independent `N(0,1/6)`. Thus (3.5) holds. Applying (2.1) in the limiting kernel gives

\[
C_{\rm maj}^{\sharp}
=\int_{-1/2}^{1/2}\frac6\pi K_0(6x^2)\,dx
=\frac{12}{\pi}\int_0^{1/2}K_0(6x^2)\,dx.
\tag{7.1}
\]

The earlier theorem (1.4) already proves analytically that every cap-one Gaussian-completion heavy law has density below `3sqrt(2)`, hence in particular

\[
C_{\rm maj}^{\sharp}<3\sqrt2.
\tag{7.2}
\]

The deterministic checker records only for scale that

\[
C_{\rm maj}^{\sharp}=3.5306641257709305771\ldots,
\]

so the true branch gap is much larger than the old envelope suggested.

## 8. First finite-bank correction

The latest completed designated partner `account03/B17` theorem is

`yspennstate/math-open-problems@f593cf73a4e7547eac4183f8e61062fca5176706`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T021034Z-account03-B17-QFORM-r22/REPORT.md`.

Its Section 4.1 proves the source-valid uniform local CLT for the normalized centered-uniform bank:

\[
\|h_m-\gamma\|_\infty\to0,
\qquad \gamma(y)=\sqrt{6/\pi}\,e^{-6y^2},
\tag{8.1}
\]

using the exact characteristic function

\[
\widehat h_m(\xi)=\operatorname{sinc}(\xi/(2\sqrt m))^m,
\tag{8.2}
\]

together with the central domination `|hat h_m(xi)|<=e^{-xi^2/24}` and the explicit outer Fourier-tail bound

\[
\frac{4\sqrt m}{(m-1)\pi^{m-1}}.
\tag{8.3}
\]

I apply those exact partner bounds to one further term of the same Fourier expansion. Since

\[
\log\operatorname{sinc}z=-\frac{z^2}{6}-\frac{z^4}{180}+O(z^6),
\]

(8.2) gives on the partner's expanding central interval

\[
\widehat h_m(\xi)
=e^{-\xi^2/24}\left[1-\frac{\xi^4}{2880m}+O\left(\frac{\xi^6+\xi^8}{m^2}\right)\right].
\tag{8.4}
\]

The partner's Gaussian central domination and exponentially small outer tail make Fourier inversion of (8.4) legitimate with a weighted `O(m^{-2})` remainder. With `sigma^2=1/12` and `H_4(z)=z^4-6z^2+3`, this yields

\[
 h_m(y)=\gamma(y)\left[1-\frac1{20m}H_4(y/\sigma)\right]
 +O(m^{-2})(1+|y|)^{-8}.
\tag{8.5}
\]

This is an actual use of the completed partner local-limit proof: its central and tail estimates supply the domination needed to promote the formal sinc expansion to a weighted local statement.

For the square density, put

\[
q(u)=-\frac1{20}(144u^2-72u+3)
=-\frac{36}{5}u^2+\frac{18}{5}u-\frac3{20}.
\tag{8.6}
\]

Then

\[
a_m(u)=a_\infty(u)[1+q(u)/m]+O(m^{-2})u^{-1/2}(1+u)^{-4},
\]

where

\[
a_\infty(u)=\sqrt{\frac6{\pi u}}e^{-6u}.
\tag{8.7}
\]

For `w>0`, insert (8.7) into (3.3). Set `x=u+w/2`, `a=w/2`, `z=6w`. The classical integral representation of `K_nu` gives

\[
\int_a^\infty\frac{e^{-12x}}{\sqrt{x^2-a^2}}dx=K_0(z),
\]

\[
\int_a^\infty\frac{x e^{-12x}}{\sqrt{x^2-a^2}}dx=aK_1(z),
\]

and

\[
\int_a^\infty\frac{x^2 e^{-12x}}{\sqrt{x^2-a^2}}dx
=\frac{a^2}{2}[K_0(z)+K_2(z)].
\]

Since

\[
q(u)+q(u+w)
=-\frac{72}{5}x^2+\frac{36}{5}x-\frac{18}{5}w^2-\frac3{10},
\]

and `K_2(z)=K_0(z)+2K_1(z)/z`, the first correction collapses to

\[
\boxed{
 k_m(w)=\frac6\pi\left[
 K_0(6w)+\frac1m\left(
 3wK_1(6w)-\left(\frac{36}{5}w^2+\frac3{10}\right)K_0(6w)
 \right)
 \right]+O(m^{-2})
}
\tag{8.8}
\]

in the integrable weighted sense needed below.

By (2.1), the sharp finite branch constant is

\[
C_m:=p_{Q_{m,U}}(0)=2\int_0^{1/2}k_m(x^2)dx.
\tag{8.9}
\]

Let

\[
c(x)=3x^2K_1(6x^2)-\left(\frac{36}{5}x^4+\frac3{10}\right)K_0(6x^2).
\]

Using

\[
\frac d{dx}K_0(6x^2)=-12xK_1(6x^2),
\]

integration by parts gives the exact sign identity

\[
\begin{aligned}
\int_0^{1/2}c(x)dx
&=-\frac18K_0(3/2)\\
&\quad-\int_0^{1/2}
\left(\frac1{20}+\frac{36}{5}x^4\right)K_0(6x^2)dx
<0.
\end{aligned}
\tag{8.10}
\]

Equations (8.8)--(8.10) prove (2.3)--(2.4). The sign is analytic; the numerical checker is only a consistency test.

## 9. Required newest-Claude result applied to a real inequality

The required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`,

proves Theorem C: every exact rank-three `(+,+,-)` source-valid form with unit large eigenvalues obeys on the ruled side, including the cone `s=0`,

\[
p_Q(s)\le\pi\sqrt2,\qquad s\ge0.
\tag{9.1}
\]

Apply it to the exact finite matrices (1.1) and then use the exact extremizer identity (2.1):

\[
\boxed{
C_m
=\sup_f\|p_{Q_{m,f}}\|_\infty
=p_{Q_{m,U}}(0)
\le\pi\sqrt2
\qquad\text{for every }m.
}
\tag{9.2}
\]

This is a genuine target-level inequality obtained by applying the newest-Claude theorem after the new extremal reduction. It also cleanly identifies the remaining sharp-constant gap: `pi sqrt(2)` is larger than `3sqrt(2)` by `sqrt(2)(pi-3)`, so Theorem C alone cannot settle whether a small finite `m` in this branch exceeds `3sqrt(2)`. Failure to improve the auxiliary constant `pi sqrt(2)` is not a counterexample to QFORM.

The same e5f source's Theorem D/5-volume extensions do not directly resolve this family: its rank is three and the live correction already records that every coordinate cut can have cross rank at most two. The correct sharp analysis here is the aggregate-bank extremization above, not reciprocal payment of one physical minor.

## 10. Applying the designated partner result to the witness frontier

The same completed `account03/B17` r22 report proves a genuinely nonseparable two-heavy/shared-bank Gaussian-completion bound

\[
\|p_{V^2-2UG}\|_\infty
\le 2^{13/6}\sqrt{3/\pi}\,\Gamma(5/4)^{2/3}
=4.1092705664\ldots<3\sqrt2
\tag{10.1}
\]

for every heavy-plane joint density `rho<=1`, and transfers it uniformly to its exact finite source-valid shared-bank family.

Combining (10.1) with the present exact one-heavy extremizer theorem gives a real obstruction to the next witness search: neither (a) arbitrary fragmentation of one majority-sign macroscopic coordinate with two separated diffuse banks nor (b) the partner's lightlike two-heavy/shared-bank geometry can beat `3sqrt(2)`. A sharper witness must leave both geometries—for example by using a genuinely non-lightlike pair of noncollinear macroscopic rows, three or more interacting heavy rows, coupled spectral tails, or a finite multiscale geometry not reducible to one decreasing residual kernel.

## 11. Scope, corrections, and remaining obligation

This report does **not** prove the universal sharp constant `3sqrt(2)` and does not prove the full QFORM conjecture. It proves an exact extremal classification for one source-valid family.

The live corrections were respected. In particular:

* no post-rotation independence is used;
* no arbitrary-joint three-dimensional coarea bound is used;
* no worst conditional projection-density moment is used;
* no pointwise law-uniform quadratic-phase decay is used;
* the two-shell bathtub support is derived only for the explicit monotone kernel `k_m(s-x^2)` and therefore does not conflict with `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`;
* no claim is made that centered intervals are extremal for arbitrary rotated QFORM matrices.

The first unpaid implication inside the present family is now extremely concrete:

\[
\boxed{
C_m=p_{U^2+S_m^2-T_m^2}(0)\stackrel{?}{\le}3\sqrt2
\quad\text{for every finite }m.
}
\tag{11.1}
\]

Here all physical laws are fixed centered unit intervals and `A_m` has spectrum exactly `{1,1,-1}`. `m=1` is controlled by the diagonal theorem; (2.3) controls all sufficiently large `m`. Any violation of (11.1) would disprove **only the candidate sharp constant `3sqrt(2)`**, not the existence of some larger universal QFORM constant. Conversely, proving (11.1) would completely close this one-heavy majority-sign family for every finite bank size.

The deterministic sibling checker verifies the Bessel correction identity, positivity of `kappa_maj`, the sharp Gaussian-limit value, and its gap from `3sqrt(2)`.
