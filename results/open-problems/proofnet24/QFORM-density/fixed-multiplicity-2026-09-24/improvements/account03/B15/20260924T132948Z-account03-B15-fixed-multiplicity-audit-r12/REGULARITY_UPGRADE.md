# B15 regularity upgrade for the fixed-multiplicity theorem

Run: `20260924T132948Z-account03-B15-fixed-multiplicity-audit-r12`  
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## 1. Seventeen directions: same universal height, now with a canonical C0 representative

The audited baseline proves, for arbitrary independent coordinate densities bounded by `K`, arbitrary symmetric `A` with `s_17(A)>=s>0`, and arbitrary affine `b,c`,

\[
\Pr\{X^TAX+b^TX+c\in I\}\le(10^4K^2/s)|I|.
\tag{1}
\]

The completed affine fixed-instance theorem at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260924T092642Z-account03-B15-qform-auto11/REPORT.md`

proves that every fixed rank-at-least-three affine quadratic under cap-one product inputs has a canonical density in `C_0(R) cap L^infinity(R)`. Scaling handles general `K,s`. Since the present hypothesis forces `rank(A)>=17`, (1) implies on that continuous representative

\[
\boxed{
 p_Q\in C_0(\mathbb R),\qquad
 \|p_Q\|_\infty\le10^4K^2/s.
}
\tag{2}
\]

Indeed (1) gives `p_Q<=10^4K^2/s` almost everywhere. If the continuous representative exceeded that value at one point, it would exceed it on a nonempty interval, contradicting (1).

This strengthens the theorem at fleet level without changing its universal constant. It is not yet a self-contained amendment of the 790-line baseline source unless the fixed-instance `C_0` theorem is imported or reproved there.

## 2. Actual designated-partner application

Account04/B15's completed same-constant compiler at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`

states that for a fixed rank-at-least-three homogeneous quadratic form under cap-one product inputs, any interval inequality `P(Q in I)<=M|I|` upgrades to a canonical `C_0` density of height at most exactly `M`.

Normalize the homogeneous specialization of (1) by `Y=KX`, `A'=A/s`. The audited theorem gives

\[
\Pr\{Y^TA'Y\in I\}\le10^4|I|.
\tag{3}
\]

Applying the account04/B15 compiler to this actual inequality and scaling back gives

\[
\boxed{
 p_{X^TAX}\in C_0(\mathbb R),\qquad
 \|p_{X^TAX}\|_\infty\le10^4K^2/s.
}
\tag{4}
\]

No affine extension of the partner theorem is assumed; affine continuity in (2) uses the separate completed affine fixed-instance theorem.

## 3. Thirteen directions: critical regularity package

Assume the normalized no-pivot chamber: independent cap-one coordinates, arbitrary affine terms, no `eta=1/100` pivot, and `s_13(A)>=1`. The audited order-four spectral-to-volume argument supplies a physical cut with

\[
Z_4(M)^{-1/8}\le160.
\]

Set

\[
u=\pi eZ_4(M)^{-1/8}\le160\pi e.
\]

Then

\[
|\phi_Q(t)|\le\min\{1,u/|t|\}.
\tag{5}
\]

### Uniform negative-half-potential bound

The manuscript's Riesz inequality and (5) give

\[
\begin{aligned}
\sup_a\mathbb E|Q-a|^{-1/2}
&\le(2\pi)^{-1/2}\left(2\int_0^u t^{-1/2}dt+2u\int_u^\infty t^{-3/2}dt\right)\\
&=8\sqrt{u/(2\pi)}\\
&\le8\sqrt{80e}<118.
\end{aligned}
\tag{6}
\]

This improves the no-pivot half-potential constant `<200` when thirteen directions are present.

### Qualitative C0 plus universal finite-Lq control

A fresh account03/B01 improvement proves at `s_13>=1` that for every finite `q>=2`,

\[
\|p_Q\|_q\le\left(\max\{6010,160e q\}\right)^{1-1/q}
\tag{7}
\]

in normalized variables, and in the no-pivot chamber the sharper `(160e q)^{1-1/q}` bound holds. It also gives the critical `O(h log(1/h))` small-ball estimate.

Separately, the fixed-instance affine `C_0` theorem applies because `rank(A)>=13`. Thus the exact thirteen-direction regularity status is

\[
\boxed{
 p_Q\in C_0(\mathbb R)\cap\bigcap_{2\le q<\infty}L^q(\mathbb R),
}
\tag{8}
\]

with universal finite-`q` norms but no known universal `L^infinity` constant. Each fixed matrix does have a finite `L^infinity` height from the fixed-instance theorem; what is missing is a bound uniform over all `A` with `s_13(A)>=1`.

## 4. Why this still does not prove 13

The envelope (5) is exactly the nonintegrable endpoint. Generic `O(1/|t|)` control permits logarithmically unbounded densities, so (5), (6), and all finite-`q` bounds cannot by themselves produce a uniform essential supremum.

The newest leverage-interpolated determinant theorem closes the no-pivot thirteen-direction branch whenever the order-four volume-producing cut has maximum physical row leverage `h<1`, with a constant that diverges as `h->1`. Therefore the current threshold-reduction debt is sharply localized to the **high-leverage endpoint**. A valid `17 -> 13` proof needs a uniform receiver there (for example, a dependence-safe hub/slope mechanism or a second compatible crossing currency before taking absolute values).

No lower fixed multiplicity is claimed here. The unrestricted three-eigenvalue conjecture remains open.
