SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-23T10:46:13Z.
attacking: non-lightlike two-heavy/source-valid fragmented stress families with residual bank curvature; seek a finite or mesoscopic peak above `3 sqrt(2)`, or a sharp no-escape inequality.

# QFORM-NONLIGHTLIKE-TWO-PARTIAL-HEAVY-GLOBAL-BARRIER-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: account02/B17, sharp constant and witnesses  
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution context: `WITHOUT_VERIFIED_BRAIN`

The unrestricted theorem for arbitrary independent cap-one densities and arbitrary symmetric matrices with three absolute eigenvalues at least one remains open. This report closes a new source-valid stress class: **two macroscopic physical rows plus three diffuse banks in a genuinely non-lightlike rank-three orientation**, at small heavy leverage. The result is global in the output level, not just a cone-tip calculation.

## 1. Exact finite source-valid family

Let

\[
B_u=I_3-2uu^T,\qquad u\in S^2.
\]

Then `B_u` is symmetric orthogonal and has spectrum `{1,1,-1}`. Fix `0<=ell<1` and an integer `m>=1`. Define a `3 x (3m+2)` synthesis matrix `C_{m,ell}` whose physical columns are

\[
\sqrt\ell e_1,\quad \sqrt\ell e_2,
\]

followed by `m` copies of each of

\[
\sqrt{(1-\ell)/m}\,e_1,\qquad
\sqrt{(1-\ell)/m}\,e_2,\qquad
m^{-1/2}e_3.
\]

Exactly,

\[
C_{m,\ell}C_{m,\ell}^T=I_3.
\tag{1.1}
\]

Therefore

\[
A_{m,\ell,u}=C_{m,\ell}^T B_u C_{m,\ell}
\tag{1.2}
\]

has exact nonzero spectrum

\[
\boxed{\{1,1,-1\}}
\tag{1.3}
\]

for every finite `m`: the isometry `y -> C^T y` intertwines `B_u` with the restriction of `A` to its range. Put independent `Uniform[-1/2,1/2]` laws on **every physical coordinate**. Thus every input density is exactly one and no independence is asserted after a spectral rotation.

Writing `U_1,U_2` for the two heavy coordinates and `S_{jm}` for the three normalized uniform banks,

\[
Y_{m,\ell}=
\left(
\sqrt\ell U_1+\sqrt{1-\ell}S_{1m},
\sqrt\ell U_2+\sqrt{1-\ell}S_{2m},
S_{3m}
\right),
\qquad
Q_{m,\ell,u}=Y_{m,\ell}^TB_uY_{m,\ell}.
\tag{1.4}
\]

For fixed `ell`, the bank CLT gives the latent limit

\[
Y_\ell=
\left(
\sqrt\ell U_1+\sqrt{1-\ell}G_1,
\sqrt\ell U_2+\sqrt{1-\ell}G_2,
G_3
\right),
\tag{1.5}
\]

where `G_1,G_2,G_3` are independent `N(0,sigma^2)`, `sigma^2=1/12`, independent of the uniforms. Let

\[
Q_{\ell,u}=Y_\ell^TB_uY_\ell
\]

and write its density as `p_{ell,u}`.

A particularly useful orientation is

\[
u_*=(1,1,1)/\sqrt3,
\qquad
B_*={1\over3}
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix}.
\tag{1.6}
\]

All entries are nonzero and `(B_*)_{33}=1/3`: the third diffuse bank has genuine square curvature and also couples to both heavy axes. This is therefore outside the preceding lightlike form `V^2-2US`, where the diffuse bank enters only linearly.

## 2. Main theorem: the GLOBAL peak has a uniform negative quadratic correction

### Theorem

Uniformly over `u in S^2`, as `ell downarrow 0`,

\[
\boxed{
\|p_{\ell,u}\|_\infty
=3\sqrt2\,[1-c_{12}(u)\ell^2+o(\ell^2)]
}
\tag{2.1}
\]

with

\[
\boxed{
c_{12}(u)
={114+6(u_1^2+u_2^2)-39(u_1^4+u_2^4)\over640}.}
\tag{2.2}
\]

Moreover

\[
\boxed{c_{12}(u)\ge {81\over640}}
\tag{2.3}
\]

for every orientation. Hence there is an absolute `ell_0>0` such that

\[
\boxed{
0<\ell\le\ell_0
\quad\Longrightarrow\quad
\|p_{\ell,u}\|_\infty<3\sqrt2
\quad\text{for every }u\in S^2.}
\tag{2.4}
\]

For the fully coupled non-lightlike orientation (1.6),

\[
\boxed{
c_{12}(u_*)={41\over240},}
\tag{2.5}
\]

so

\[
\boxed{
\|p_{\ell,u_*}\|_\infty
=3\sqrt2\left[1-{41\over240}\ell^2+o(\ell^2)\right].}
\tag{2.6}
\]

Thus two genuine macroscopic physical rows can approach the diffuse `3 sqrt(2)` obstruction to **quadratic order**, even with nonzero residual bank curvature and every effective matrix entry nonzero, but they approach it from below.

## 3. Density expansion

The predecessor used here is the completed B17 partial-heavy theorem

`yspennstate/math-open-problems@0feb5b58d53a266b5df517982780448aa9b6daf5`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T232912Z-r11-partial-heavy/REPORT.md`.

For

\[
Z_\ell=\sqrt\ell U+\sqrt{1-\ell}G,
\qquad U\sim\operatorname{Unif}[-1/2,1/2],\quad
G\sim N(0,\sigma^2),\quad \sigma^2=1/12,
\]

its one-dimensional density has the weighted expansion

\[
f_\ell(y)=\gamma_\sigma(y)
\left[1-{\ell^2\over20}H_4(y/\sigma)\right]
+O(\ell^3)(1+|y|)^{-8},
\tag{3.1}
\]

uniformly in `y`. The missing linear term is the exact variance-match cancellation

\[
e^{\ell\xi^2/24}\operatorname{sinc}(\sqrt\ell\xi/2)
=1-{\ell^2\xi^4\over2880}-{\ell^3\xi^6\over181440}+O(\ell^4\xi^8).
\]

Only the first two axes in (1.5) are perturbed, so their joint product gives

\[
\rho_{\ell}(y)
=\gamma_\sigma^{(3)}(y)
\left[1-{\ell^2\over20}
\{H_4(y_1/\sigma)+H_4(y_2/\sigma)\}\right]
+O(\ell^3)(1+|y|)^{-8}.
\tag{3.2}
\]

Let `T_u` be quadratic pushforward by `q_u(y)=y^TB_uy`. The radial remainder is harmless **uniformly in the output level and in `u`**. Orthogonal invariance reduces it to `q_0=z_1^2+z_2^2-z_3^2`; cylindrical coordinates give, for

\[
w(y)=(1+|y|)^{-8},
\]

\[
T_u w(s)
=\pi\int_{z^2+s\ge0}
(1+\sqrt{2z^2+s})^{-8}\,dz
\le \pi\int_{\mathbb R}(1+|z|)^{-8}dz
={2\pi\over7}.
\tag{3.3}
\]

Consequently

\[
p_{\ell,u}(s)=p_0(s)-{\ell^2\over20}J_u(s)+O(\ell^3)
\tag{3.4}
\]

uniformly in `(u,s)`, where

\[
J_u=T_u\left[\gamma_\sigma^{(3)}
\{H_4(y_1/\sigma)+H_4(y_2/\sigma)\}\right].
\tag{3.5}
\]

The same cylindrical formula, with a polynomial-Gaussian integrand, shows that `J_u(s)` is jointly continuous in `(u,s)`; local smooth orthogonal frames suffice, and compactness of `S^2` gives a uniform modulus near `s=0`.

## 4. Cone coefficient and its uniform positivity

The normalized cone moments computed in the predecessor theorem apply coordinate by coordinate. If

\[
x_j=u_j^2,
\]

then on the isotropic `(2,1)` Gaussian cone

\[
{J_{u,j}(0)\over p_0(0)}
={57+6x_j-39x_j^2\over32}.
\tag{4.1}
\]

Summing only `j=1,2` and multiplying by `1/20` from (3.4) gives exactly (2.2).

For the uniform lower bound set

\[
s=x_1+x_2\in[0,1].
\]

Since `x_1^2+x_2^2<=s^2`,

\[
640c_{12}(u)
\ge114+6s-39s^2.
\tag{4.2}
\]

The right side is concave on `[0,1]`, so its minimum is at an endpoint:

\[
\min\{114,114+6-39\}=81.
\]

This proves (2.3), sharply (e.g. `u=e_1`). For `u_*`, `x_1=x_2=1/3`, so (2.5) follows exactly.

## 5. Why the local cone calculation controls the GLOBAL maximum

At `ell=0`, orientation disappears because the Gaussian is isotropic. In a spectral basis

\[
Q_0=G_1^2+G_2^2-G_3^2.
\]

Set `M=3sqrt(2)`. Since `G_1^2+G_2^2` is exponential of rate `6`, while `G_3^2` has density

\[
b(z)=\sqrt{6/\pi}\,z^{-1/2}e^{-6z},\qquad z>0,
\]

one has the exact positive-side formula

\[
\boxed{p_0(s)=M e^{-6s},\qquad s\ge0.}
\tag{5.1}
\]

For `r>0`,

\[
p_0(-r)=\int_0^\infty 6e^{-6w}b(w+r)\,dw
<\int_0^\infty6e^{-6w}b(w)\,dw=M,
\tag{5.2}
\]

because `b` is strictly decreasing. Thus `s=0` is the **unique global maximizer** of `p_0`.

Equation (3.4) implies `p_{ell,u}->p_0` uniformly at rate `O(ell^2)`. Hence every maximizing point of `p_{ell,u}` tends to zero uniformly in `u`. Joint continuity of `J_u(s)` then gives

\[
J_u(s_{\ell,u})=J_u(0)+o(1)
\]

uniformly for any choice of maximizer `s_{ell,u}`. Since `p_0(s)<=M`, (3.4) gives

\[
\|p_{\ell,u}\|_\infty
\le M-{\ell^2\over20}J_u(0)+o(\ell^2),
\]

while evaluating at zero gives the reverse asymptotic inequality. Therefore

\[
\|p_{\ell,u}\|_\infty
=M-{\ell^2\over20}J_u(0)+o(\ell^2),
\]

uniformly in `u`, which is exactly (2.1). The positive lower bound (2.3) then yields an absolute `ell_0` and (2.4).

This is the key new implication over the predecessor: **the off-zero loophole is closed to second order, uniformly over orientation**, for the two-partial-heavy Gaussian-completion class.

## 6. Required pinned Claude result applied to the actual finite matrices

The required source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `FOURIER_ROUTE_REPORT.md`.

Its completed **Theorem F (Fresnel–Brascamp–Lieb)** is used here as an actual finite-matrix inequality, not merely cited. Diagonalize `B_u=O^T diag(1,1,-1)O` and set

\[
R=C_{m,\ell}^TO^T.
\]

Then `R^TR=I_3`. The physical row leverages are exactly

\[
\ell,\ \ell,\ {1-\ell\over m}\text{ (twice `m` rows)},\ {1\over m}\text{ (`m` rows)}.
\]

Therefore, for

\[
0\le\ell\le1/2,\qquad m\ge2,
\]

every leverage is at most `1/2`, and Theorem F gives for the **actual cap-one finite witness**

\[
\boxed{
|\phi_{m,\ell,u}(t)|
\le \min\{1,(4\pi)^{3/2}|t|^{-3/2}\}.}
\tag{6.1}
\]

The right side is integrable and independent of `m,ell,u`. For fixed `ell`, the vector bank CLT gives pointwise convergence of the quadratic characteristic functions. Dominated convergence applied to (6.1) gives

\[
\|\phi_{m,\ell,u}-\phi_{\ell,u}\|_{L^1(dt)}\to0,
\]

and Fourier inversion therefore gives the **uniform output-density convergence**

\[
\boxed{
\|p_{m,\ell,u}-p_{\ell,u}\|_\infty\to0.}
\tag{6.2}
\]

Consequently, for every fixed `0<ell<=ell_0` and every fixed orientation `u`, all sufficiently large finite `m` satisfy

\[
\boxed{
\|p_{Q_{m,\ell,u}}\|_\infty<3\sqrt2.}
\tag{6.3}
\]

In particular, the explicit fully coupled non-lightlike `u_*` family consists of exact finite target matrices with exact cap-one physical inputs, and it cannot asymptotically produce a small-leverage overshoot above `3 sqrt(2)`.

This is the requested application of a completed `e5f...` result to a real obstruction: Theorem F supplies the integrable majorant that rules out an unseen narrowing finite-bank spike when passing from the exact finite witnesses to the limiting sharp calculation.

## 7. Designated partner result applied: what it proves, and what it does NOT

The latest completed partner result is

`account03/B17`,
`yspennstate/math-open-problems@c1d4b2518211f8a5ea1dc173722a453e02e6a31c`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T100331Z-account03-B17-QFORM-auto11/REPORT.md`.

It proves a weighted local limit for cap-one finite-activity remote fragments: a normalized bank tends to `G+aN`, with `G~N(0,1/12)` and `N` Poisson. Its worker-owned Gaussian input is

`yspennstate/math-open-problems@dcf8885d5153370cacfa246ad1e29fb06d971769`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T070310Z-account03-B17-QFORM-r25/REPORT.md`,

which proves the sharp arbitrary-mean Gaussian ceiling

\[
\|p_{G^TAG}\|_\infty\le {1\over2\sqrt2\,\sigma_0^2}
\]

whenever the Gaussian covariance is at least `sigma_0^2 I` and `A` has three absolute eigenvalues at least one.

Apply those results to the present two-heavy geometry. Split the third Gaussian as

\[
G_3\stackrel d=\sqrt{1-\ell}\,G_{3a}+\sqrt\ell\,G_{3b}
\]

with independent variance-`1/12` Gaussians. Then

\[
Y_\ell=\sqrt{1-\ell}\,G+H,
\]

where `G~N(0,I_3/12)` and

\[
H=(\sqrt\ell U_1,\sqrt\ell U_2,\sqrt\ell G_{3b})
\]

is independent. Conditional on `H=h`, the covariance floor is `(1-ell)I_3/12`, so the partner theorem gives

\[
\boxed{
\|p_{Q_{\ell,u}\mid H=h}\|_\infty
\le {3\sqrt2\over1-\ell}.}
\]

Averaging yields the real global inequality

\[
\boxed{
\|p_{\ell,u}\|_\infty\le {3\sqrt2\over1-\ell}.}
\tag{7.1}
\]

The same conditioning applies after replacing any of the diffuse banks by the partner's finite-activity remote-fragment law: condition also on the limiting Poisson shifts. Together with its bank local limit and the finite Theorem-F majorant, this gives

\[
\boxed{
\limsup_m\|p^{\rm frag}_{m,\ell,u}\|_\infty
\le {3\sqrt2\over1-\ell}.}
\tag{7.2}
\]

This application is deliberately interpreted correctly. The right side has **positive linear slack** `3sqrt(2) ell+O(ell^2)` above the candidate sharp constant. It therefore cannot prove the sharp `3sqrt(2)` bound in this class. That is a failure of the Gaussian-floor conditioning constant, **not** evidence for a QFORM counterexample. The exact expansion (2.1) shows that the unfragmented source-valid family actually moves in the opposite direction, by a negative amount of order `ell^2`.

So any sharp proof charging a linear *penalty* merely for two heavy rows is also incompatible with this family, while any proof that loses a linear *upper-bound slack* through covariance-floor conditioning is nonsharp by an entire order.

## 8. Sharp-witness consequence and unpaid class

What is now excluded:

- the preceding lightlike two-heavy/shared-bank family, including growing remote fragmentation, was already below `3sqrt(2)`;
- this run excludes the **small-leverage, non-lightlike, two-heavy plus three-diffuse-bank family globally**, uniformly in orientation in the limiting model and for all sufficiently large exact finite banks at each fixed small leverage;
- finite-activity remote fragmentation of the diffuse banks remains globally bounded by (7.2), though that auxiliary ceiling is not sharp enough to exclude a `3sqrt(2)` overshoot by itself.

The first genuinely unpaid B17 witness mechanism is therefore no longer “two heavy rows” in general. It must exploit at least one feature absent from the theorem above: **intermediate rather than perturbative leverage**, a finite/mesoscopic bank before the diffuse limit, a surviving non-Gaussian component dependent on the Gaussian core, multiple non-collinear macroscopic rows not representable as two axis heavies plus independent banks, or a fragmentation scale that changes the second-order signed correction itself.

A future explicit finite peak above `3sqrt(2)` would refute the proposed sharp constant, but would still not refute the existence of a larger universal QFORM constant. Nothing in this report proves or disproves the unrestricted conjecture.

## 9. Deterministic checks

`check_two_partial_heavy.py` checks the exact rational non-lightlike matrix `B_*`, `B_*^2=I`, `tr(B_*)=1` and hence spectrum `{1,1,-1}`, the exact coefficient `41/240`, the uniform coefficient floor `81/640`, and the radial remainder constant `2pi/7`. The recorded output is `CHECK_OUTPUT.txt` and begins

`PASS QFORM-NONLIGHTLIKE-TWO-PARTIAL-HEAVY-GLOBAL-BARRIER-v1`.

No refuted arbitrary-joint coarea inequality, post-rotation independence, fixed-fragment-count reduction, conditional-density positive moment, pointwise stationary-phase envelope, or universal good-minor principle is used.
