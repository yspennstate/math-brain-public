# account02/B17 — finite tight-frame Poisson-location barrier

Run: `20260924T094416Z-account02-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `SUPPORTING_SHARP-WITNESS_THEOREM / FULL QFORM OPEN`

## 1. First unpaid implication attacked

The preceding B17 runs ruled out ordinary diffuse Gaussian banks, finite-variance satellite taxes, axis-aligned compound-Poisson satellites, and arbitrary random translations of a Gaussian core as mechanisms for exceeding the current lower obstruction `3 sqrt(2)`.

The first unpaid witness mechanism considered here is a **shared non-collinear macroscopic-jump array**: every original physical coordinate contributes simultaneously to several spectral directions, the source is genuinely non-Lindeberg, the remote fragments are at root-`m` distance, and after aggregation the surviving jumps point along a non-coordinate tight frame rather than along three disjoint banks.

This report proves that the whole finite-direction tight-frame version of that mechanism still cannot asymptotically overshoot `3 sqrt(2)`. The unrestricted rough-law QFORM theorem remains open; continuity for the unrestricted target remains separate.

No independence after spectral rotation is used. All independence below belongs to the original physical coordinates.

## 2. General rank-three tight-frame construction

Fix finitely many unit vectors `u_1,...,u_q in R^3` and positive weights `w_1,...,w_q` satisfying the Parseval identity

\[
\sum_{a=1}^q w_a u_a u_a^T=I_3. \tag{2.1}
\]

For each `m`, form a `qm x 3` synthesis matrix `T_m` with `m` copies of the row

\[
r_{a,k}=\sqrt{w_a/m}\,u_a,\qquad k=1,\dots,m. \tag{2.2}
\]

Then

\[
T_m^T T_m=I_3,
\qquad
\|r_{a,k}\|^2=w_a/m. \tag{2.3}
\]

Let `B=B^T` be any fixed `3 x 3` matrix with

\[
|\lambda_j(B)|\ge1,\qquad j=1,2,3, \tag{2.4}
\]

and put

\[
A_m=T_mBT_m^T. \tag{2.5}
\]

Because `T_m` is an isometry on `R^3`, the nonzero spectrum of `A_m` is exactly the spectrum of `B`:

\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\operatorname{spec}(B).} \tag{2.6}
\]

Hence every finite stage is an exact target matrix.

## 3. Exact cap-one root-m satellite laws

Fix for each frame direction constants

\[
\lambda_a>0,\qquad R_a>0. \tag{3.1}
\]

For `m>lambda_a`, set

\[
\ell_{a,m}=1-\lambda_a/m,
\qquad
D_{a,m}=2+R_a\sqrt m. \tag{3.2}
\]

On every original physical coordinate in group `a`, use the density

\[
\begin{aligned}
f_{a,m}(x)
={}&\mathbf1_{[-\ell_{a,m}/2,\ell_{a,m}/2]}(x)\\
&+\mathbf1_{[D_{a,m}-\lambda_a/(4m),D_{a,m}+\lambda_a/(4m)]}(x)\\
&+\mathbf1_{[-D_{a,m}-\lambda_a/(4m),-D_{a,m}+\lambda_a/(4m)]}(x).
\end{aligned} \tag{3.3}
\]

The three intervals are disjoint, their total length is exactly

\[
\ell_{a,m}+\frac{\lambda_a}{2m}+\frac{\lambda_a}{2m}=1, \tag{3.4}
\]

and therefore `f_{a,m}` is a probability density satisfying

\[
\boxed{0\le f_{a,m}\le1} \tag{3.5}
\]

with no normalization slack. Its remote support gap is `R_a sqrt(m)+O(1)`.

Let all `qm` physical variables be independent and define the active three-vector

\[
Y_m=T_m^T X. \tag{3.6}
\]

Then the actual physical quadratic form is

\[
Q_m=X^T A_mX=Y_m^TBY_m. \tag{3.7}
\]

## 4. This array is genuinely non-Lindeberg

Put

\[
c_a:=R_a\sqrt{w_a}. \tag{4.1}
\]

A satellite coordinate in group `a` produces an active-vector increment

\[
r_{a,k}X_{a,k}=\pm c_a u_a+o(1). \tag{4.2}
\]

The total satellite probability in one coordinate is `lambda_a/m`. Thus for any fixed `0<delta<c_a`, the aggregate Lindeberg tail in that frame group satisfies

\[
\sum_{k=1}^m
\mathbb E\Big[\|r_{a,k}X_{a,k}\|^2
\mathbf1_{\{\|r_{a,k}X_{a,k}\|>\delta\}}\Big]
\longrightarrow \lambda_a c_a^2>0. \tag{4.3}
\]

So ordinary triangular-array Gaussianization fails deliberately. The number of remote visits in group `a` converges to `Poisson(lambda_a)`, and the total probability of at least one remote visit converges to

\[
1-\exp\!\left(-\sum_a\lambda_a\right). \tag{4.4}
\]

The macroscopic jump component survives.

## 5. Exact aggregate limit: isotropic Gaussian core plus non-collinear compound Poisson

Fix `xi in R^3` and write

\[
s_{a,m}=\sqrt{w_a/m}\,\langle\xi,u_a\rangle. \tag{5.1}
\]

The characteristic function of one original coordinate in group `a`, evaluated at its contribution to `Y_m`, is

\[
\begin{aligned}
\chi_{a,m}(\xi)
={}&\ell_{a,m}\,\operatorname{sinc}\!\left(
\frac{s_{a,m}\ell_{a,m}}2\right)\\
&+\frac{\lambda_a}{m}\,
\operatorname{sinc}\!\left(\frac{s_{a,m}\lambda_a}{4m}\right)
\cos(s_{a,m}D_{a,m}).
\end{aligned} \tag{5.2}
\]

For fixed `xi`,

\[
s_{a,m}D_{a,m}
=c_a\langle\xi,u_a\rangle+O(m^{-1/2}), \tag{5.3}
\]

and the sinc expansion gives

\[
\chi_{a,m}(\xi)
=1+\frac1m\left[
\lambda_a\big(\cos(c_a\langle\xi,u_a\rangle)-1\big)
-\frac{w_a}{24}\langle\xi,u_a\rangle^2
\right]+o(m^{-1}). \tag{5.4}
\]

After the `m` independent copies in group `a`, and then multiplying the `q` independent groups,

\[
\begin{aligned}
\mathbb Ee^{i\langle\xi,Y_m\rangle}
\longrightarrow
\exp\Bigg(&-\frac1{24}
\sum_a w_a\langle\xi,u_a\rangle^2\\
&+\sum_a\lambda_a
[\cos(c_a\langle\xi,u_a\rangle)-1]\Bigg).
\end{aligned} \tag{5.5}
\]

The Parseval identity (2.1) turns the quadratic term into `-|xi|^2/24`. Consequently

\[
\boxed{Y_m\Rightarrow G+M,\qquad G\sim N(0,I_3/12),} \tag{5.6}
\]

where `G` is independent of

\[
M=\sum_{a=1}^q c_a(N_{a,+}-N_{a,-})u_a, \qquad
N_{a,\pm}\stackrel{ind}{\sim}\operatorname{Poisson}(\lambda_a/2). \tag{5.7}
\]

Thus the remote fragments survive as a genuinely non-Gaussian, generally off-axis random location. No rotated finite-stage variables were declared independent.

By the continuous mapping theorem,

\[
Q_m\Rightarrow Q_\infty:=(G+M)^TB(G+M). \tag{5.8}
\]

Weak convergence alone is not enough to control density peaks; the next step is the needed global anti-spike estimate.

## 6. Pinned Fresnel–Brascamp–Lieb theorem gives a finite-stage global envelope

This is the required direct use of the completed result at

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, Theorem F (also audited in `FOURIER_ROUTE_REPORT.md`).

Diagonalize only the fixed coefficient matrix,

\[
B=O\,\operatorname{diag}(\mu_1,\mu_2,\mu_3)O^T, \tag{6.1}
\]

and take the physical eigenframe

\[
V_m=T_mO. \tag{6.2}
\]

This does **not** rotate the product input law. It is only a representation of the physical matrix. We have

\[
V_m^TV_m=I_3,
\qquad
\|\operatorname{row}_{a,k}V_m\|^2=w_a/m. \tag{6.3}
\]

For all sufficiently large `m`, every row leverage is at most `1/2`. The residual quadratic block in Theorem F is exactly zero and its Gram matrix is `I_3`. Therefore, for the actual finite-stage characteristic function

\[
\Phi_m(t)=\mathbb Ee^{itQ_m}, \tag{6.4}
\]

Theorem F gives

\[
|\Phi_m(t)|
\le
(4\pi)^{3/2}|t|^{-3/2}
|\mu_1\mu_2\mu_3|^{-1/2}. \tag{6.5}
\]

Because every `|mu_j|>=1`,

\[
\boxed{
|\Phi_m(t)|\le
M_0(t):=\min\{1,(4\pi)^{3/2}|t|^{-3/2}\}.
} \tag{6.6}
\]

The majorant is integrable, with exact mass

\[
\int_{\mathbb R}M_0(t)\,dt=24\pi. \tag{6.7}
\]

This is a real obstruction inequality on the source-valid finite witnesses. It does not use the refuted law-uniform pointwise stationary-phase claim; it uses the proved tight-frame Fresnel–Brascamp–Lieb theorem under its actual leverage hypothesis.

## 7. Uniform convergence of the entire output density

From (5.8), for every fixed `t`,

\[
\Phi_m(t)\to\Phi_\infty(t). \tag{7.1}
\]

Passing to the limit in (6.6) gives `|Phi_infty(t)|<=M_0(t)`. Hence

\[
|\Phi_m(t)-\Phi_\infty(t)|\le2M_0(t), \tag{7.2}
\]

and dominated convergence yields

\[
\|\Phi_m-\Phi_\infty\|_{L^1(\mathbb R)}\to0. \tag{7.3}
\]

Fourier inversion therefore supplies continuous finite-stage and limiting densities in this **specific family**, together with the global all-output convergence

\[
\boxed{
\|p_m-p_\infty\|_\infty
\le\frac1{2\pi}\|\Phi_m-\Phi_\infty\|_1
\longrightarrow0.
} \tag{7.4}
\]

Thus a narrowing positive- or negative-output spike cannot hide from the weak limit.

This is a family-specific continuity statement; it is not a proof of the full target's continuous-density conclusion.

## 8. Latest account03/B17 comparator closes the random-location limit

The latest compatible designated partner result is account03/B17
`QFORM-GAUSSIAN-FULLTARGET-COMPARATOR-v1`, canonical source

`math-open-problems@ea855178c7771925095c4517c830888c9a8938ea`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260924T090408Z-account03-B17-QFORM-auto11/REPORT.md`.

It proves: if `H~N(mu,Sigma)`, `Sigma>=vI`, and a symmetric coefficient matrix has at least three eigenvalues of magnitude at least `s`, then

\[
\|p_{H^TAH}\|_\infty\le\frac1{2\sqrt2\,vs}. \tag{8.1}
\]

For the conditional law of `Q_infty` given `M=z`, the Gaussian is

\[
G+z\sim N(z,I_3/12), \tag{8.2}
\]

while `B` has spectral floor one. Therefore, uniformly in every possible compound-Poisson location `z`,

\[
\|p_{Q_\infty\mid M=z}\|_\infty\le3\sqrt2. \tag{8.3}
\]

Averaging the conditional densities gives the real global obstruction

\[
\boxed{\|p_\infty\|_\infty\le3\sqrt2.} \tag{8.4}
\]

Combining (7.4) and (8.4),

\[
\boxed{
\limsup_{m\to\infty}\|p_{Q_m}\|_\infty\le3\sqrt2.
} \tag{8.5}
\]

So a finite collection of shared, non-collinear, root-`m` Poissonized directions cannot yield a sharp-constant overshoot when their diffuse carrier is an isotropic cap-one central core.

## 9. Explicit tetrahedral entrywise-dense target witness

To make the construction maximally concrete, take

\[
\begin{aligned}
t_1&=(1,1,1)/\sqrt3, &
t_2&=(1,-1,-1)/\sqrt3,\\
t_3&=(-1,1,-1)/\sqrt3, &
t_4&=(-1,-1,1)/\sqrt3.
\end{aligned} \tag{9.1}
\]

Then

\[
\sum_{a=1}^4t_at_a^T=\frac43I_3. \tag{9.2}
\]

Choose `w_a=3/4` for all four groups, so every physical row is

\[
r_{a,k}=\sqrt{\frac{3}{4m}}t_a, \tag{9.3}
\]

and has leverage `3/(4m)`.

Take the dense reflection

\[
n=(1,2,3)^T/\sqrt{14},\qquad
B=I_3-2nn^T
=\frac17\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix}. \tag{9.4}
\]

Exactly,

\[
B^2=I_3,\qquad
\det B=-1,\qquad
\operatorname{spec}(B)=\{1,1,-1\}. \tag{9.5}
\]

The group coefficient table is

\[
(t_a^TBt_b)_{a,b=1}^4
=
\begin{pmatrix}
-5/7&17/21&5/21&-1/3\\
17/21&5/21&-5/7&-1/3\\
5/21&-5/7&17/21&-1/3\\
-1/3&-1/3&-1/3&1
\end{pmatrix}. \tag{9.6}
\]

Every entry is nonzero. Hence every one of the `(4m)^2` physical coefficients of

\[
A_m=T_mBT_m^T \tag{9.7}
\]

is nonzero, while

\[
\boxed{
\operatorname{spec}(A_m)=\{1,1,-1,0,\ldots,0\}.
} \tag{9.8}
\]

This is an entrywise-dense physical target, with each rare physical satellite creating a macroscopic jump in a tetrahedral direction that mixes the three active spectral coordinates.

For this witness, (6.6) holds for every `m>=2` and (8.5) applies for arbitrary fixed positive satellite intensities and amplitudes.

## 10. What this rules out — and what it does not

This theorem rules out a substantially broader witness mechanism than three disjoint banks:

- the source laws are disconnected cap-one sets with root-`m` remote fragments;
- Lindeberg fails by a fixed amount;
- macroscopic compound-Poisson jumps survive;
- the jumps lie along several non-coordinate, non-collinear tight-frame directions;
- the finite physical matrices are entrywise dense and have the exact target spectrum;
- a proved physical-frame Fourier envelope excludes hidden finite-stage spikes;
- the full limiting random-location mixture is globally capped by `3 sqrt(2)`.

It does **not** prove QFORM. The surviving sharp-witness frontier must break at least one of the key features used here: for example, infinitely many or scale-growing macroscopic directions rather than a fixed finite tight frame; a non-Gaussian diffuse carrier without covariance-floor Gaussian smoothing; dependence between the surviving jump component and the diffuse carrier generated before the independent-coordinate aggregation; or additional active spectrum/residual quadratic structure for which the exact-rank-three Theorem-F envelope no longer applies.

A failure of the present mechanism in those regimes would be only a proof-mechanism failure. A finite example with density peak above `3 sqrt(2)` would refute the proposed **sharp constant**, not the existence of some larger universal QFORM constant. A genuine counterexample to QFORM must make the essential density unbounded across a valid target family.

## 11. Source/correction ledger

Consumed at this run:

- current brain control revision `2026-09-22.15` and live QFORM correction inbox;
- pinned completed Theorem F and its audit at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`;
- latest compatible account03/B17 Gaussian full-target comparator at `math-open-problems@ea855178c7771925095c4517c830888c9a8938ea`.

The proof does not use the refuted arbitrary-joint coarea bound, law-uniform pointwise stationary phase, post-rotation input independence, generic two-sheet X-ray-only control, bounded-support localization, or a universal finite-fragment reduction.

Deterministic exact checks in this invocation verified the tetrahedral frame identity, `B^2=I`, `det B=-1`, the spectrum `{1,1,-1}`, and every entry of the group coefficient table (9.6).
