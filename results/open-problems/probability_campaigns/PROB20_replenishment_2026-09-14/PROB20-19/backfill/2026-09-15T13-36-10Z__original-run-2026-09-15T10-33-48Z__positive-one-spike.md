# PROB20-19 backfill — original run 2026-09-15T10-33-48Z

**Recovery provenance.** This file preserves authentic mathematical work from an earlier completed task response in the current conversation. That earlier run attempted a GitHub write but no successful commit receipt/readback was exposed. The text below is reconstructed from the exact prior task-response content available in this conversation; no missing tool results or unavailable local files are invented.

**Original status: PARTIAL.** The universal Mallat–Zeitouni/Bandeira conjecture remained open.

## Positive one-spike theorem for every retained dimension

For every `p>=2`, every `1<=d<p`, every `a>=0`, every `c>=0`, and every unit vector `u in R^p`, let
\[
\Sigma_u=aI_p+c\,uu^T.
\]
If `X~N(0,Sigma_u)`, then
\[
\mathbb E\operatorname{Top}_d(X_1^2,\ldots,X_p^2)
\le
\mathbb E\operatorname{Top}_d(Y_1^2,\ldots,Y_p^2),
\]
where
\[
Y\sim N\!\left(0,\operatorname{diag}(a+c,a,\ldots,a)\right).
\]
Thus an eigenbasis is globally optimal on the full orthogonal orbit of every spectrum `(a+c,a,...,a)`, for every `d`.

### Shift functional

For `x in R^p`, define
\[
f_d(x)=\operatorname{Top}_d(x_1^2,\ldots,x_p^2),
\qquad
H_d(m)=\mathbb E f_d(Z+m),\ Z\sim N(0,I_p).
\]
By signed-permutation symmetry, `H_d(m)` depends only on the unordered squared mean vector `y=(m_i^2)`. Write
\[
\Psi_d(y)=H_d(\sqrt{y_1},\ldots,\sqrt{y_p}).
\]

### Theorem A — Schur-convexity in squared mean coordinates

For every `p>=2` and `1<=d<p`, `Psi_d` is Schur-convex on `R_+^p`.

It suffices to prove monotonicity under equalizing two coordinates. Fix all coordinates except `1,2`, let
\[
m_1=r\cos\theta,\qquad m_2=r\sin\theta,\qquad 0\le\theta\le\pi/4.
\]
Condition on the outside coordinates and use polar coordinates for the first pair,
\[
x_1=\rho\cos\phi,\qquad x_2=\rho\sin\phi.
\]
For fixed outside values let `C_k` denote the sum of the `k` largest outside squared coordinates. Then the conditional top-`d` objective is exactly
\[
h_{\rho,w}(\phi)
=
\max\{C_d,\ C_{d-1}+M(\phi),\ C_{d-2}+\rho^2\},
\]
where
\[
M(\phi)=\max(x_1^2,x_2^2)=\frac{\rho^2}{2}(1+|\cos2\phi|).
\]
Hence `h` is nonnegative, even, `pi/2`-periodic, and nonincreasing on `[0,pi/4]`.

The angular factor of the shifted Gaussian pair at fixed radius is `exp(a cos(phi-theta))`, with `a=r rho`. Periodizing over the `pi/2` symmetry gives
\[
K_a(t)=\sum_{k=0}^3e^{a\cos(t+k\pi/2)}
=2\cosh(a\cos t)+2\cosh(a\sin t).
\]
For `0<t<pi/4`,
\[
K_a'(t)=2a[-\sin t\sinh(a\cos t)+\cos t\sinh(a\sin t)]<0.
\]
The last sign follows because `x -> sinh(ax)/x` is strictly increasing for `a>0`.

Thus both `h` and `K_a` are symmetric decreasing functions on the circle of circumference `pi/2`. By the circular layer-cake rearrangement lemma, their convolution is again symmetric decreasing, so the conditional expectation is nonincreasing as `theta` increases from `0` to `pi/4`. Integrating over radius and outside coordinates proves the two-coordinate T-transform inequality, hence Schur-convexity.

Strictness holds for a genuine equalization with nonzero moved mean by restricting to a positive-probability region where `h=constant+M(phi)`.

### One-spike covariance consequence

For `a>0`, write
\[
X=\sqrt a Z+\sqrt c G u=\sqrt a(Z+\tau G u),\qquad \tau=\sqrt{c/a},
\]
with `Z~N(0,I_p)` and `G~N(0,1)` independent. Conditioning on `G=g`, the squared mean vector is
\[
\tau^2g^2(u_1^2,\ldots,u_p^2).
\]
Since `(1,0,...,0)` majorizes `(u_i^2)`, Theorem A gives pointwise in `g`
\[
\mathbb E_Zf_d(Z+\tau gu)
\le
\mathbb E_Zf_d(Z+\tau ge_1).
\]
Integrate over `g` and use degree-two homogeneity. For `a=0`,
\[
f_d(\sqrt c G u)=cG^2\operatorname{Top}_d(u_1^2,\ldots,u_p^2)\le cG^2,
\]
with equality at a coordinate spike.

## Exact sphere representation

For every positive-definite covariance `C`,
\[
\mathcal F_d(C)
=\frac{\Gamma((p+2)/2)}{\pi^{p/2}\sqrt{\det C}}
\int_{S^{p-1}}f_d(\theta)
(\theta^TC^{-1}\theta)^{-(p+2)/2}\,dS(\theta).
\]
This follows by polar integration and the radial identity
\[
\int_0^\infty r^{p+1}e^{-qr^2/2}\,dr
=2^{p/2}\Gamma((p+2)/2)q^{-(p+2)/2}.
\]

For a two-eigenvalue covariance `aI+cP`, the weight depends only on `||P theta||^2`; this motivates a Grassmannian polarization attack.

## Boundary extension

For a degenerate rank-`r` projection covariance `C=cP`, if `d>=r`, then
\[
f_d(PG)\le\|PG\|_2^2,
\]
so the expectation is at most `r`, with equality for a coordinate rank-`r` projection. Thus this boundary case is solved exactly.

## Gaps recorded in the original run

The Schur-convex shift theorem does not by itself settle rank-`r>1` positive spikes: conditioning produces a random mean `PG`, and no pointwise or stochastic majorization theorem comparing its squared coordinates with a coordinate projection was proved. Arbitrary covariance reduction `C=lambda_min I+B` leaves the same obstruction. Negative one-spike spectra are also not covered by the positive scalar-factor argument.
