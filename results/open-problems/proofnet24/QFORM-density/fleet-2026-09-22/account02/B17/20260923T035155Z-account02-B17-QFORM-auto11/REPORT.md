# QFORM B17 — exact m=1 and m=2 closure for the one-heavy majority-sign branch

Run: `20260923T035155Z-account02-B17-QFORM-auto11`  
Account/slot: `account02/B17`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `NEW_SUPPORTING_THEOREM`; full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact unpaid branch inherited from the preceding B17 theorem

For every integer `m>=1`, consider

\[
A_m=\operatorname{diag}(1,J_m/m,-J_m/m).
\tag{1.1}
\]

Since `J_m/m` has one eigenvalue `1` and all others zero,

\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}.}
\tag{1.2}
\]

Thus every finite matrix is in the exact target spectral class. Put an arbitrary probability density `0<=f<=1` on the singleton physical coordinate and independent centered unit intervals on the two `m`-coordinate banks. Write

\[
S_m=m^{-1/2}\sum_{j=1}^m U_j,\qquad
T_m=m^{-1/2}\sum_{j=1}^m V_j,
\]

where all `U_j,V_j` are independent `Unif[-1/2,1/2]`. Then

\[
Q_{m,f}=X_f^2+S_m^2-T_m^2.
\tag{1.3}
\]

The completed preceding same-slot theorem

`yspennstate/math-open-problems@189fc052089ae2d3237bc0865b290b01b26a6513`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260923T031047Z-account02-B17-QFORM-r11/REPORT.md`,

proves the exact finite extremizer identity

\[
\boxed{
C_m:=\sup_{0\le f\le1,\int f=1}\|p_{Q_{m,f}}\|_\infty
=p_{U^2+S_m^2-T_m^2}(0),
\quad U\sim\mathrm{Unif}[-1/2,1/2].
}
\tag{1.4}
\]

Therefore the only unpaid issue in this branch is the scalar sequence `C_m`; arbitrary fragmentation, translation, disconnected support and unbounded support of the heavy law have already been optimized out. The same theorem gives `C_m=C_maj^sharp-kappa/m+O(m^{-2})` with `kappa>0`, so sufficiently large `m` are below `3sqrt(2)`, but it left the intermediate finite values open.

This run closes the first two exact bank sizes.

## 2. New theorem

### `QFORM-ONE-HEAVY-MAJORITY-M1M2-EXACT-v1`

For the source-valid family (1.1)-(1.3), including optimization over every cap-one singleton law and every output level,

\[
\boxed{C_1=\pi<3\sqrt2,}
\tag{2.1}
\]

and

\[
\boxed{
C_2=-\frac73+\frac{\pi}{\sqrt2}+4\log(1+\sqrt2)
=3.413602483824021891105\ldots<3\sqrt2.
}
\tag{2.2}
\]

Thus no `m=1` or `m=2` finite-bank overshoot of the candidate sharp obstruction `3sqrt(2)` is possible in this entire arbitrary-heavy-law branch.

This is a supporting sharp-witness exclusion. It does **not** prove `C_m<=3sqrt(2)` for every `m`, does not prove that `3sqrt(2)` is the universal sharp constant, and does not prove the full QFORM conjecture.

## 3. Exact m=1 value

For `m=1`, `S_1,T_1` are centered unit intervals. By (1.4),

\[
C_1=p_{U^2+S_1^2-T_1^2}(0).
\]

Conditioning on `(U,S_1)=(u,s)` and writing `r=(u^2+s^2)^{1/2}`, the density of `T_1^2` at `r^2` is `1/r` for `0<r<=1/2`. The disk `r<=1/2` lies inside the square `[-1/2,1/2]^2`, hence

\[
C_1=\iint_{u^2+s^2\le1/4}\frac{du\,ds}{\sqrt{u^2+s^2}}
=\int_0^{2\pi}\int_0^{1/2}dr\,d\theta
=\pi.
\tag{3.1}
\]

The strict comparison `pi<3sqrt(2)` is immediate, for example from `pi<22/7<3sqrt(2)`.

## 4. Exact m=2 reduction

The normalized two-uniform bank has the triangular density

\[
h_2(s)=\sqrt2(1-\sqrt2|s|)\mathbf 1_{\{|s|\le1/\sqrt2\}}.
\tag{4.1}
\]

Again by (1.4),

\[
C_2=p_{U^2+S_2^2-T_2^2}(0).
\]

For a symmetric density `h`, the density of `T^2` at `r^2>0` is `h(r)/r`. Therefore, putting `r=(u^2+s^2)^{1/2}`,

\[
C_2=\int_{|u|\le1/2}\int_{\mathbb R}
 h_2(s)\frac{h_2(r)}r\,ds\,du.
\tag{4.2}
\]

The integrand vanishes unless `r<=1/sqrt(2)`. By fourfold symmetry in `(u,s)` and polar coordinates

\[
u=r\cos\theta,\qquad s=r\sin\theta,
\]

the Jacobian `r` cancels the factor `1/r`, while the two triangular-density prefactors contribute `2`. Hence

\[
C_2=8(I_1+I_2),
\tag{4.3}
\]

where

\[
I_1=\int_0^{\pi/4}\int_0^{1/(2\cos\theta)}
(1-\sqrt2 r\sin\theta)(1-\sqrt2 r)\,dr\,d\theta,
\tag{4.4}
\]

and

\[
I_2=\int_{\pi/4}^{\pi/2}\int_0^{1/\sqrt2}
(1-\sqrt2 r\sin\theta)(1-\sqrt2 r)\,dr\,d\theta.
\tag{4.5}
\]

The split at `theta=pi/4` is exactly where the physical heavy-coordinate constraint `u<=1/2` and the bank support constraint `r<=1/sqrt(2)` exchange roles.

## 5. Elementary integration

Expanding the quadratic polynomial in `r` and evaluating the elementary trigonometric antiderivatives gives

\[
\boxed{
I_1=-\frac5{24}+\frac12\log(1+\sqrt2)
}
\tag{5.1}
\]

and

\[
\boxed{
I_2=-\frac1{12}+\frac{\sqrt2\pi}{16}.
}
\tag{5.2}
\]

Substitution in (4.3) yields

\[
\boxed{
C_2=-\frac73+\frac\pi{\sqrt2}+4\log(1+\sqrt2).
}
\tag{5.3}
\]

No numerical integration is used in the theorem.

For a fully elementary strict certificate below `3sqrt(2)`, use

\[
\frac\pi{\sqrt2}<\frac{11\sqrt2}{7}
\quad(\pi<22/7),
\tag{5.4}
\]

and

\[
\log(1+\sqrt2)<1.
\tag{5.5}
\]

For (5.5), `sqrt(2)<3/2`, so `1+sqrt(2)<5/2`, whereas the exponential series gives `e>1+1+1/2=5/2`. Consequently

\[
C_2<\frac53+\frac{11\sqrt2}{7}<3\sqrt2,
\tag{5.6}
\]

because the last inequality is equivalent to `35<30sqrt(2)`, whose square is `1225<1800`.

The deterministic decimal values are only checks:

\[
C_2=3.41360248382402189110504446162\ldots,
\qquad
3\sqrt2-C_2=0.82903820329526325530002171101\ldots.
\tag{5.7}
\]

## 6. Required newest-Claude result applied to a real obstruction

At the required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`,

Theorem C proves for every exact rank-three `(+,+,-)` source-valid form on the one-sheet side `s>=0` that

\[
p_Q(s)\le\pi\sqrt2.
\tag{6.1}
\]

Applied to every finite member (1.1), this supplies a genuine finite-`m` one-sheet bound with no moment or support assumptions on the singleton law. It does not by itself reach the proposed sharp scale because `pi sqrt(2)>3sqrt(2)`.

The same required package also explains why its principal Fourier exits do not pay this family uniformly: every physical cross cut of (1.1) has rank at most two, so the 3-volume `Z` in Theorem D vanishes, while the singleton spectral row has leverage one and fails Theorem F's `<=1/2` leverage gate. Therefore (5.3) is not a duplicate of a paid Fourier branch: it gives an exact low-bank calculation precisely in a family that witnesses those structural gates.

Combining (6.1) with the preceding exact-extremizer theorem and (5.3) replaces the auxiliary one-sheet constant `pi sqrt(2)` by the exact **global** branch constant `C_2<3sqrt(2)` at `m=2`.

Failure to improve `pi sqrt(2)` by that Fourier theorem would only be a failure of that auxiliary constant, not a counterexample to QFORM; (5.3) makes this distinction explicit.

## 7. Latest designated partner result and witness map

The latest compatible completed `account03/B17` result is

`yspennstate/math-open-problems@0a23c8b4c6e8f1ce727bd99d55ed6258ce18ade2`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T033115Z-account03-B17-QFORM-r24/REPORT.md`.

It constructs a genuinely rotated source-valid three-bank family with order-`1/m` remote fragments at distance `Theta(sqrt(m))`, proves a global noncentral-Gaussian shift penalty, and obtains for the concrete `a=c=1` fragmented family

\[
\limsup_m\|p_{Q_m}^{\rm frag}\|_\infty
\le2.4870582495390534\ldots<3\sqrt2.
\tag{7.1}
\]

That result is complementary to the present finite-bank calculation. Together they yield the actual obstruction

\[
\max\{C_1,C_2,2.48705824954\ldots\}<3\sqrt2,
\tag{7.2}
\]

covering both the two smallest bank sizes of the one-heavy majority branch and the partner's first finite-activity remote-fragment escape mechanism. Neither statement is being extrapolated outside its proved architecture.

Thus a witness above `3sqrt(2)`, if one exists, must at least leave these mechanisms. Credible surviving directions include intermediate `m>=3` in the exact scalar sequence `C_m`, multiscale fragments whose activity/scale change jointly with `m`, or genuinely shared non-collinear macroscopic rows not reducible to independent bank shifts.

## 8. Remaining precise obligation

The same one-heavy family is now reduced to

\[
\boxed{
C_m=p_{U^2+S_m^2-T_m^2}(0)\stackrel{?}{\le}3\sqrt2,
\qquad m\ge3.
}
\tag{8.1}
\]

The preceding B17 theorem proves (8.1) for all sufficiently large `m` through a negative `1/m` correction; this run proves it exactly for `m=1,2`. The unpaid portion is therefore a finite/intermediate range, or a monotonic/comparison argument that bridges it. A violation of (8.1) would refute the **candidate sharp constant** `3sqrt(2)`, but would not by itself refute existence of a larger universal QFORM constant.

No hidden moment, bounded-support, log-concavity, spectral-coordinate independence, or rotation-independence assumption is introduced. All finite physical matrices and product sources are explicit.
