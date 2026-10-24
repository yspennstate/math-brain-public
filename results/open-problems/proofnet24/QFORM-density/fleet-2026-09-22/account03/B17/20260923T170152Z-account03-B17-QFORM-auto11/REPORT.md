# QFORM B17: global zero-pivot one-heavy ceiling below the 3 sqrt(2) obstruction

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T17:01:52Z.  
attacking: the exact zero-physical-pivot one-heavy/two-diffuse endpoint, globally in the output level, and its exact finite cap-one bank approximants.

Status: **new supporting theorem; full QFORM remains OPEN / NOT PROVED**.  
Continuity: proved for the Gaussian endpoint and, for all sufficiently large bank sizes, for the exact finite family below; full-target continuity remains open.  
Memory/runtime status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is genuine but no authenticated native learned-memory receiver-use event was observed.

## 1. Source and correction scope

Fresh controls were read from `yspennstate/math-research-brain` main under OWNER CONTROL revision `2026-09-22.15`, including `AGENTS.md`, the full `scheduled_tasks/README.md` OWNER MESSAGE, `fleet.json`, `roles.json`, `PROTOCOL.md`, the QFORM manifest/current research/claims/live correction inbox/memory protocol, and `assignments/account03/B17.json`. The current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` and the current Claude continuation were also read.

This argument does **not** use any of the refuted interfaces: no law-uniform pointwise quadratic-phase decay, no independence after a spectral rotation, no arbitrary-joint coarea cap, no fiber-supremum dimension bound, no conditional projection-density moment, and no interval-extremality assumption. The only rearrangement used below is a one-dimensional bathtub inequality for an explicitly positive Gaussian reward in an original independent coordinate.

The designated completed partner result actually applied is:

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`.

It supplies both (i) the weighted local Edgeworth expansion for normalized uniform banks and (ii) the exact source-valid rotated lower witness proving that every valid universal constant must satisfy `C_* >= 3 sqrt(2)`.

---

## 2. The zero-pivot Gaussian endpoint theorem

Let `X` be any real random variable with probability density `f` satisfying

`0 <= f <= 1`, `integral f = 1`.

Let `B,C` be independent centered Gaussians, independent of `X`, with variances

`v_B >= 1/12`, `v_C >= 1/12`.

For

`Q = 2 X B + C^2`,

the law of `Q` has a bounded continuous density and

\[
\boxed{\|p_Q\|_\infty < 4.240061 < 3\sqrt2.}
\tag{2.1}
\]

The same bound remains valid if `B,C` have arbitrary means: the mean of `B` contributes only a unit-modulus linear phase in `X`, and the noncentral-square factor for `C` has modulus no larger than its centered counterpart. It also remains valid under arbitrary added linear terms in the three variables after completing/translating the corresponding one-dimensional Gaussian factors. I keep the proof below in the centered no-linear-term normalization because that is the exact stress family used later.

### 2.1 Exact characteristic-function factorization

Write first `v_B=v_C=v=1/12`; larger variances only decrease the pointwise majorant below. Conditioning on `X=x`,

\[
\mathbf E_B e^{it(2xB)}=e^{-2vt^2x^2},
\]

while

\[
\left|\mathbf E_C e^{itC^2}\right|
=(1+4v^2t^2)^{-1/4}.
\]

Therefore

\[
|\phi_Q(t)|
=(1+4v^2t^2)^{-1/4}
\int_{\mathbb R}f(x)e^{-2vt^2x^2}\,dx.
\tag{2.2}
\]

For fixed `t`, the reward `x -> exp(-2 v t^2 x^2)` is even and decreases with `|x|`. The elementary bathtub principle under `0<=f<=1`, `integral f=1` gives

\[
\int f(x)e^{-2vt^2x^2}\,dx
\le
\int_{-1/2}^{1/2}e^{-2vt^2x^2}\,dx.
\tag{2.3}
\]

This is valid for arbitrary fragmented/disconnected support; no connected-support or interval-law hypothesis is assumed for `X`.

For `v_B,v_C >=1/12`, the two factors in (2.2) are separately decreasing in the relevant variance, so the minimum-variance case controls all larger variances.

### 2.2 Fourier ceiling

At `v=1/12`, put `u=t/6` and `k=sqrt(3/2)`. From (2.2)-(2.3),

\[
\|p_Q\|_\infty
\le {1\over2\pi}\int_{\mathbb R}|\phi_Q(t)|\,dt
\le \sqrt{6\over\pi}\,I,
\tag{2.4}
\]

where

\[
I:=\int_0^\infty
{\operatorname{erf}(ku)\over u(1+u^2)^{1/4}}\,du.
\tag{2.5}
\]

In particular the characteristic function is integrable, so Fourier inversion gives a continuous density representative.

---

## 3. Fully analytic strict comparison with `3 sqrt(2)`

The point of this section is that the strict gap in (2.1) is not a Monte Carlo or quadrature assertion. The companion checker certifies it using exact rational arithmetic only.

Set

\[
w=2^{-1/4}.
\]

### 3.1 Head `0 <= u <= 1`

Because `k^2=3/2`, the alternating series for `erf(ku)` has decreasing term magnitudes throughout `0<=u<=1`. Ending after the positive `n=4` term gives

\[
\operatorname{erf}(ku)
\le {2\over\sqrt\pi}
\sum_{n=0}^4 {(-1)^n(ku)^{2n+1}\over n!(2n+1)}.
\tag{3.1}
\]

Also `z -> (1+z)^(-1/4)` is convex on `[0,1]`, hence lies below its secant:

\[
(1+u^2)^{-1/4}\le1-(1-w)u^2.
\tag{3.2}
\]

Multiplying (3.1)-(3.2) and integrating term by term gives the exact bound

\[
I_{[0,1]}
\le
2\sqrt{3\over2\pi}
\left(
{1580209\over2587200}
+{38243\over147840}w
\right).
\tag{3.3}
\]

### 3.2 Tail `u >= 1`

Using only `erf <= 1`,

\[
I_{[1,\infty)}
\le
\int_1^\infty {du\over u(1+u^2)^{1/4}}.
\]

With `z=(1+u^2)^(-1/4)`, this integral is elementary:

\[
\int_1^\infty {du\over u(1+u^2)^{1/4}}
=
\operatorname{atanh}(w)+\arctan(w).
\tag{3.4}
\]

Combining (3.3)-(3.4),

\[
I\le
2\sqrt{3\over2\pi}
\left(
{1580209\over2587200}
+{38243\over147840}2^{-1/4}
\right)
+\operatorname{atanh}(2^{-1/4})+\arctan(2^{-1/4}).
\tag{3.5}
\]

The exact-rational checker proves from Machin's formula for `pi`, alternating `atan` bounds, a positive-series remainder for `atanh`, and algebraic rational enclosures that

\[
I<3.06811,
\qquad
\sqrt{6/\pi}<1.381978.
\]

Consequently

\[
\boxed{
\|p_Q\|_\infty
< 1.381978\cdot3.06811
=4.24006052158
<4.240061
<3\sqrt2.
}
\tag{3.6}
\]

The checker verifies the last comparison by the exact rational inequality `(4.240061)^2 < 18`. A direct high-precision evaluation of the sharper Fourier-majorant integral in (2.4) is about `4.2058248326`; this decimal is only a diagnostic and is not needed for the proof.

---

## 4. Exact finite source-valid no-pivot family

The Gaussian variables in Section 2 are **not** being substituted for target inputs. They arise as the limit of an exact finite product family satisfying every source input condition.

Let

\[
J=\operatorname{diag}(1,1,-1),
\quad
r={1\over\sqrt2}(1,0,1),
\quad
b={1\over\sqrt2}(1,0,-1),
\quad
c=(0,1,0).
\]

For each `m`, form a `(2m+1) x 3` matrix `R_m` whose rows are

- one heavy row `r`,
- `m` copies of `b/sqrt(m)`,
- `m` copies of `c/sqrt(m)`.

Then

\[
R_m^TR_m=rr^T+bb^T+cc^T=I_3.
\]

Set

\[
A_m=R_m J R_m^T.
\]

Therefore the exact nonzero spectrum of `A_m` is

\[
\boxed{\{1,1,-1\}}
\tag{4.1}
\]

for every finite `m`.

Take independent original coordinates: one arbitrary heavy input `X` with density `<=1`, and two banks of `m` independent `Unif[-1/2,1/2]` variables. Define

\[
B_m={1\over\sqrt m}\sum_{k=1}^m U_k,
\qquad
C_m={1\over\sqrt m}\sum_{k=1}^m V_k.
\]

The exact physical quadratic form is

\[
\boxed{Q_m=2XB_m+C_m^2.}
\tag{4.2}
\]

Indeed `r^T J r=b^T J b=0`, `r^T J b=1`, `c^T J c=1`, and all other pairings among `r,b,c` vanish.

This is a genuine no-fixed-pivot stress family: the heavy physical diagonal is zero, each heavy/bank cross entry is `1/sqrt(m)`, the corresponding 2x2 determinant is `-1/m`, and the transverse square is spread over a rank-one bank with entries `1/m`. Thus fixed physical principal minors degenerate as `m` grows although the matrix retains three unit eigenvalues exactly.

---

## 5. Partner Edgeworth theorem removes hidden finite-bank spikes

This section is where the completed `account04/B17` result is used at an actual estimate.

Let `g_m` be the density of either normalized uniform bank and let `gamma` be the `N(0,1/12)` density. The partner theorem proves the weighted local Edgeworth expansion

\[
g_m(y)=\gamma(y)
\left[1-{H_4(y/\sigma)\over20m}\right]
+O(m^{-2})(1+|y|)^{-8},
\qquad \sigma^2=1/12.
\tag{5.1}
\]

In particular

\[
\delta_m:=\|g_m-\gamma\|_1=O(m^{-1}),
\tag{5.2}
\]

and `g_m(0)->gamma(0)<2`.

Let

\[
\psi_m(s)=\mathbf E e^{isB_m},
\qquad
\chi_m(t)=\mathbf E e^{itC_m^2},
\]

and let `psi_infty`, `chi_infty` denote the corresponding Gaussian functions. For a heavy density `f`,

\[
\phi_{m,f}(t)
=\chi_m(t)\int f(x)\psi_m(2tx)\,dx.
\tag{5.3}
\]

From (5.2), uniformly in the frequency,

\[
|\psi_m-\psi_\infty|\le\delta_m,
\qquad
|\chi_m-\chi_\infty|\le\delta_m.
\tag{5.4}
\]

Hence on every fixed compact time interval,

\[
\sup_{0\le f\le1,\ \int f=1}
|\phi_{m,f}(t)-\phi_{\infty,f}(t)|
\le2\delta_m.
\tag{5.5}
\]

It remains to justify a uniform integrable tail rather than merely compact convergence.

### 5.1 Uniform tail for the bilinear bank

Exactly,

\[
\psi_m(s)=\operatorname{sinc}\!\left({s\over2\sqrt m}\right)^m.
\]

For `m>=3` and `t!=0`, using only `f<=1`,

\[
\left|\int f(x)\psi_m(2tx)\,dx\right|
\le {\sqrt m\over|t|}
\int_{\mathbb R}|\operatorname{sinc}y|^m\,dy.
\tag{5.6}
\]

Euler's product for `sin y/y` gives `|sinc y|<=exp(-y^2/6)` on `|y|<=1`; on `|y|>1`, `|sinc y|<=|y|^{-1}`. Therefore

\[
\sqrt m\int|\operatorname{sinc}y|^m\,dy
\le\sqrt{6\pi}+{2\sqrt m\over m-1}<7,
\qquad m\ge3.
\tag{5.7}
\]

Thus the first factor in (5.3) is at most `min(1,7/|t|)`.

### 5.2 Uniform tail for the square bank

The normalized sum of centered uniforms has a symmetric unimodal density. For all sufficiently large `m`, (5.1) gives `g_m(0)<2`. Layer-cake decomposition into centered interval superlevel sets and the elementary Fresnel bound

\[
\sup_{R>0}\left|\int_{-R}^R e^{itx^2}\,dx\right|
\le {4\over\sqrt{|t|}}
\tag{5.8}
\]

therefore imply

\[
|\chi_m(t)|\le\min\left(1,{8\over\sqrt{|t|}}\right).
\tag{5.9}
\]

For completeness, (5.8) follows after scaling from splitting at `1`: the central integral has modulus at most `1` on each half, while integration by parts gives modulus at most `1` for the tail `integral_1^T exp(iu^2)du`.

Combining (5.7) and (5.9),

\[
|\phi_{m,f}(t)|\le 56|t|^{-3/2}
\tag{5.10}
\]

for all sufficiently large `|t|`, uniformly over every admissible heavy density `f` and all sufficiently large `m`. The Gaussian endpoint has an analogous `O(|t|^{-3/2})` majorant directly from (2.2)-(2.3).

Now split the `L^1(dt)` difference between a compact interval and its complement. Equations (5.5) and (5.10) imply

\[
\boxed{
\sup_f\int_{\mathbb R}
|\phi_{m,f}(t)-\phi_{\infty,f}(t)|\,dt\longrightarrow0.
}
\tag{5.11}
\]

Fourier inversion then gives the **uniform output-density transfer**

\[
\boxed{
\sup_f\|p_{Q_m(f)}-p_{Q_\infty(f)}\|_\infty\longrightarrow0.
}
\tag{5.12}
\]

Here the supremum allows the heavy cap-one law itself to depend on `m`; the Gaussian comparison in each term uses that same heavy law. Thus no narrow finite-bank spike can escape the endpoint estimate by choosing a different fragmented heavy marginal at each dimension.

Combining (2.1) and (5.12),

\[
\boxed{
\limsup_{m\to\infty}
\sup_{0\le f\le1,\int f=1}
\|p_{Q_m(f)}\|_\infty
\le4.240061
<3\sqrt2.
}
\tag{5.13}
\]

Moreover (5.10) gives an integrable characteristic function, so these finite-bank laws have continuous density representatives for all sufficiently large `m`.

---

## 6. Actual sharp-constant comparison with the designated partner

The designated `account04/B17` exact rotated family proves

\[
C_*\ge3\sqrt2
\tag{6.1}
\]

for every finite universal constant `C_*` satisfying the owner conjecture; every member of that partner sequence is an exact cap-one product input with exact nonzero spectrum `{1,1,-1}`.

Applying (6.1) to the new exact zero-pivot family (5.13) gives the strict source-valid inequality

\[
\boxed{
\limsup_m\sup_f\|p_{Q_m(f)}\|_\infty
\le4.240061
<3\sqrt2
\le C_*.
}
\tag{6.2}
\]

So the canonical **one macroscopic zero-diagonal hub + one diffuse bilinear bank + one diffuse transverse square** architecture cannot be a sharp lower witness, even after allowing the macroscopic input law to be arbitrary, fragmented, disconnected, and dimension-dependent, and even after taking the global supremum over output levels rather than only the cone tip.

This is materially stronger than a Gaussian weak-limit observation because (5.12) rules out hidden finite-dimensional density spikes uniformly over the heavy law.

---

## 7. What this does and does not settle

Proved here:

1. A global all-level continuous-density ceiling `<4.240061<3sqrt(2)` for the zero-pivot one-heavy/two-Gaussian endpoint, with arbitrary cap-one heavy law.
2. An exact finite `(2m+1)`-dimensional cap-one product family with nonzero spectrum exactly `{1,1,-1}` realizing that zero-pivot geometry.
3. Using the completed partner Edgeworth theorem, uniform `L^1` characteristic-function and hence uniform `L^infinity` density convergence from those exact finite families to the Gaussian endpoint, uniformly over arbitrary heavy laws.
4. Therefore the entire exact family is asymptotically globally subcritical relative to the already-proved `3sqrt(2)` universal lower obstruction.

Not proved:

- the unrestricted QFORM conjecture;
- any bound for two or more macroscopic shared rows;
- the interior nonzero-pivot one-heavy family uniformly over all output levels;
- arbitrary non-Gaussian surviving diffuse components outside the uniform-bank CLT regime;
- the full target's continuity assertion.

The next nonredundant B17 mechanism is therefore a **two-heavy/multiple-shared-row exact no-pivot construction**, or a genuinely non-Gaussian surviving component coupled to the diffuse core. The single-heavy zero-pivot star-plus-square route is now excluded at the sharp-constant level.

---

## 8. Checker and numerical status

`check_zero_pivot_global.py` contains the exact-rational certificate for (3.6) and the aggregate-basis involution check. `CHECK_OUTPUT.txt` records the passing execution. No Monte Carlo or histogram is used anywhere in the proof.

The sharper decimal `4.2058248326` for the Fourier majorant was evaluated only as a diagnostic; all theorem comparisons use the exact-rational certified `4.240061` ceiling.
