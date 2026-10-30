# QFORM B17 report — parallel-pair plus orthogonal-heavy central no-escape

Status: `AUXILIARY_ONLY / SHARP-WITNESS_EXCLUSION`. The full unrestricted quadratic-form bounded-density conjecture remains OPEN / NOT PROVED. Continuity is separate and is not claimed here.


Designated partner actually applied: fleet02/B17, theorem `QFORM-TWO-ORTHOGONAL-SAMESIGN-HEAVY-NOESCAPE-v1`, handoff commit `bfce8a62af9b865ff5ae0fa6a7ed3234707d14a0`, canonical report `yspennstate/math-open-problems@26ab15f7356940c8c4ef5c6eab412a38f5bb9498:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/B17-20260922T184751Z-r12/REPORT.md`. The exact input used below is its one-coordinate cap-one square-Laplace inequality

\[
 \mathbf E\exp\{-a(\sqrt{12\ell}\,X+\sqrt{1-\ell}\,G)^2\}\le (1+2a)^{-1/2},\qquad a\ge0,
\]
for every density-\(\le1\) real `X`, every `ell in [0,1]`, and an independent standard Gaussian `G`.

## Theorem

Let `X1,X2,X3` be independent real random variables with probability densities bounded by one. Let `G2,G3` be independent standard Gaussians, independent of the `Xi`. Fix `ell in [0,1]` and define

\[
 H_1=\sqrt6\,(X_1+X_2),\qquad
 H_2=\sqrt{12\ell}\,X_3+\sqrt{1-\ell}\,G_2,\qquad
 H_3=G_3,
\]
\[
 Z=H_1^2+H_2^2-H_3^2.
\]
Then `Z` has a density at zero and

\[
 p_Z(0)\le {1\over\pi}\int_0^1(1-s)K_0(3s^2)\,ds
 < {1\over 2\sqrt2}.
\]
More explicitly,

\[
 p_Z(0)\le {1\over\pi}\left[
 {\Gamma(1/4)^2\over 2^{5/2}\sqrt3}-{\pi\over12}
 +\sqrt{\pi\over6}{e^{-3}\over6}
 \right]
 <0.345626,
\]
whereas `1/(2sqrt(2))=0.353553...`.

Consequently, in physical variance-`1/12` scaling, every exact finite-frame approximation described below has limiting central density at most

\[
 C_{\rm parallel}\le {12\over\pi}\left[
 {\Gamma(1/4)^2\over 2^{5/2}\sqrt3}-{\pi\over12}
 +\sqrt{\pi\over6}{e^{-3}\over6}
 \right]
 <4.147511<3\sqrt2=4.242640\ldots .
\]

This excludes a genuinely nonorthogonal three-heavy-row mechanism: two macroscopic physical rows are parallel and jointly saturate one positive spectral direction, while a third arbitrary cap-one macroscopic row deforms the orthogonal positive direction. The theorem is central (`t=0`) and does not control all off-center peaks.

## Proof

### 1. Positive half-Riesz representation and actual partner application

Condition on `(H1,H2)`. Since `H3^2` has density

\[
 q\mapsto (2\pi q)^{-1/2}e^{-q/2},\qquad q>0,
\]
we have

\[
 p_Z(0)= {1\over\sqrt{2\pi}}\,
 \mathbf E\left[{e^{-(H_1^2+H_2^2)/2}\over\sqrt{H_1^2+H_2^2}}\right].
\]
Using

\[
 {e^{-r^2/2}\over r}={1\over\sqrt\pi}
 \int_0^\infty u^{-1/2}e^{-(u+1/2)r^2}\,du,
\]
Tonelli gives

\[
 p_Z(0)= {1\over\pi\sqrt2}\int_0^\infty u^{-1/2}
 L_1(u+1/2)L_2(u+1/2)\,du,
\]
where `Li(a)=E exp(-a Hi^2)`.

Apply the completed fleet02/B17 inequality to `H2`:

\[
 L_2(a)\le(1+2a)^{-1/2}.
\]
Because the integral kernel is nonnegative, this replacement is legitimate pointwise under the integral. The right-hand side is exactly the same formula with `H2` replaced by a standard Gaussian. Therefore, if `G` is a standard Gaussian independent of `H1,G3`,

\[
 p_Z(0)\le p_{H_1^2+G^2-G_3^2}(0).
\]
Now `G^2-G_3^2=(G-G_3)(G+G_3)` is the product of two independent `N(0,2)` variables, hence has density

\[
 d\mapsto {1\over2\pi}K_0(|d|/2).
\]
Thus

\[
 p_Z(0)\le {1\over2\pi}\mathbf E K_0(H_1^2/2)
 ={1\over2\pi}\mathbf E K_0(3(X_1+X_2)^2).
\]

### 2. Arbitrary fragmented heavy laws reduce to centered unit intervals

The function

\[
 \Phi(s)=K_0(3s^2)
\]
is even and strictly decreasing in `|s|` for `s>0`, because `K_0'(x)=-K_1(x)<0`.

For densities `0<=f_i<=1`, `int f_i=1`, the bilinear functional

\[
 \iint f_1(x)f_2(y)\Phi(x+y)\,dx\,dy
\]
is separately linear in each density. By the bathtub principle its supremum over each density-cap-one probability class is attained at indicator densities of measurable sets of Lebesgue measure one. The one-dimensional Riesz rearrangement inequality then moves those sets to centered intervals (opposite common translations are immaterial for the sum). Hence

\[
 \mathbf E\Phi(X_1+X_2)
 \le \int_{-1/2}^{1/2}\int_{-1/2}^{1/2}
       \Phi(x+y)\,dx\,dy
 =2\int_0^1(1-s)K_0(3s^2)\,ds.
\]
Combining with the previous step proves

\[
 p_Z(0)\le {I\over\pi},\qquad
 I:=\int_0^1(1-s)K_0(3s^2)\,ds.
\]

### 3. Explicit strict gap below the Gaussian `3sqrt(2)` benchmark

Write

\[
 I=\int_0^\infty(1-s)K_0(3s^2)\,ds
   +\int_1^\infty(s-1)K_0(3s^2)\,ds.
\]
The standard Mellin integrals give

\[
 \int_0^\infty K_0(3s^2)\,ds
 ={\Gamma(1/4)^2\over2^{5/2}\sqrt3},
\]
\[
 \int_0^\infty sK_0(3s^2)\,ds={\pi\over12}.
\]
For the positive tail, use the elementary representation

\[
 K_0(x)=\int_0^\infty e^{-x\cosh t}\,dt
 \le e^{-x}\int_0^\infty e^{-xt^2/2}\,dt
 =e^{-x}\sqrt{\pi\over2x},
\]
since `cosh t>=1+t^2/2`. Therefore

\[
 \int_1^\infty(s-1)K_0(3s^2)\,ds
 \le\sqrt{\pi\over6}\int_1^\infty {s-1\over s}e^{-3s^2}\,ds
 \le\sqrt{\pi\over6}\,{e^{-3}\over6}.
\]
Consequently

\[
 I\le U:=
 {\Gamma(1/4)^2\over2^{5/2}\sqrt3}-{\pi\over12}
 +\sqrt{\pi\over6}{e^{-3}\over6}.
\]
The accompanying outward-rounded interval checker certifies

\[
 U<1.085816<1.1107207<\pi/(2\sqrt2).
\]
Hence `p_Z(0)<1/(2sqrt(2))` and, after multiplying density by twelve under `Q=Z/12`, the physical bound is `<4.147511<3sqrt(2)`.

For the centered-interval pair `X1,X2~Unif[-1/2,1/2]`, the exact scalar integral itself equals

\[
 I=1.08037237300178765\ldots,
\]
so the corresponding physical limiting zero density is

\[
 {12I\over\pi}=4.12671848503573044\ldots .
\]

## Exact finite target-admissible frames

For each `m>=1`, use the physical-to-spectral rows in `R_m`:

- two heavy rows `(1/sqrt(2)) e1` and `(1/sqrt(2)) e1`;
- one heavy row `sqrt(ell) e2`;
- `m` rows `sqrt((1-ell)/m) e2`;
- `m` rows `m^(-1/2) e3`.

Then exactly

\[
 R_m^T R_m=I_3.
\]
Therefore

\[
 A_m=R_m\,\operatorname{diag}(1,1,-1)\,R_m^T
\]
has nonzero spectrum exactly `{1,1,-1}` for every finite `m`; all coordinates are original independent physical coordinates. Put arbitrary cap-one laws on the three heavy coordinates and centered unit intervals on every diffuse coordinate. The standardized diffuse `e2,e3` banks converge locally to independent standard Gaussians. Standard Fourier local CLT for centered uniforms gives uniform convergence of their one-dimensional densities; after conditioning on the heavy coordinates, the zero-density kernel is locally integrable (`r^{-1}` in two positive variables), so truncation plus dominated convergence yields the limiting model above.

Thus this is a source-valid exact-rank-three rotated stress family, not a post-rotation independence surrogate.

## Scope and next unpaid implication

This theorem closes only the central peak for the stated parallel-pair/orthogonal-third-heavy Gaussian-completion geometry. It does not prove the unrestricted QFORM conjecture and does not prove the sharp constant is `3sqrt(2)`. Unpaid witness mechanisms include genuinely nonparallel/nonorthogonal two-heavy geometry, several interacting macroscopic rows spanning all three spectral directions, finite-row local spikes, off-center peaks for fragmented heavy laws, and effects of extra spectral directions/full matrices.

The natural next B17 attack is the continuously nonorthogonal two-heavy interpolation: preserve the positive half-Riesz integral rather than the already-refuted pointwise radial-Laplace domination, and try to prove a uniform bound on the angle interval between this parallel endpoint and the fleet02/B17 orthogonal endpoint.
