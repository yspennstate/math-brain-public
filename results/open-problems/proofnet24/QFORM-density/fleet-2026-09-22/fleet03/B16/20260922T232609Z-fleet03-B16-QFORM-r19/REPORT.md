# fleet03/B16 — QFORM null-coloop projection-product closure

Run ID: `20260922T232609Z-fleet03-B16-QFORM-r19`  
Classification: `SUPPORTING_THEOREM / EXACT NULL-COLOOP ENDPOINT PAID / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: **not proved by the new theorem**. The conclusion below is absolute continuity with an essentially bounded density.

## Exact target and live restrictions

The owner target remains the following universal statement: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a single finite dimension-independent bound for the density of the quadratic form, or produce a valid counterexample.

This report does not assume moments, compact or connected support, log-concavity, Gaussianity, identical laws, or independence after rotating to a spectral basis. It does not use the refuted law-uniform pointwise van-der-Corput estimate, an arbitrary-joint 3D coarea estimate, a positive conditional projection-height moment, or a receiver-only fiber supremum.

## New theorem: a null scalar pivot plus a bounded two-dimensional product projection

### Theorem `QFORM-NULL-COLOOP-PROJECTION-PRODUCT-v1`

Let `X` be a real random variable with density `f` satisfying `0<=f<=1`, and let `Y=(U,V)` be an R^2-valued random vector, independent of `X`, with a (not necessarily product) joint density `rho` satisfying

`0 <= rho(u,v) <= M`.

Let
\[
B=\begin{pmatrix}0&b^{\mathsf T}\\ b&C\end{pmatrix}
\]
be an invertible real symmetric `3x3` matrix. Put `D=|det B|`. Then the quadratic random variable
\[
Q=(X,Y)^{\mathsf T}B(X,Y)
\]
is absolutely continuous and admits an essentially bounded density satisfying
\[
\boxed{\|p_Q\|_\infty \le 6 M^{2/3}D^{-1/3}.}
\]

The theorem is invariant under orthogonal changes of coordinates inside the two-dimensional `Y`-plane: such a rotation changes `rho` by unit Jacobian and does not assert independence of the two rotated coordinates. Therefore rotate only the `Y`-plane so that `b=(beta,0)` with `beta>0`. Writing
\[
C=\begin{pmatrix}c_{11}&c_{12}\\c_{12}&c_{22}\end{pmatrix},
\]
we have
\[
Q=2\beta XU+c_{11}U^2+2c_{12}UV+c_{22}V^2.
\]
Invertibility gives the exact identity
\[
\det B=-\beta^2c_{22},\qquad D=\beta^2|c_{22}|,
\]
so `c22 != 0`.

### Proof

Fix a target value `t` and a splitting scale `delta>0`. Split the pushforward into the regions `|U|>=delta` and `|U|<delta`.

#### 1. Far from the scalar-product singularity

For fixed `(u,v)` with `u!=0`, `Q` is affine in `x` with derivative `2 beta u`. The cap `f<=1` therefore gives the conditional density bound
\[
p_{Q\mid U=u,V=v}(t)\le {1\over 2\beta |u|}.
\]
Integrating the unnormalised `(u,v)` slice and using only that `rho` is a probability density,
\[
p_{\rm far}(t)
 \le \int_{|u|\ge\delta}{\rho(u,v)\over2\beta|u|}\,du\,dv
 \le {1\over2\beta\delta}.
\]

#### 2. Near the scalar-product singularity

For fixed `(x,u)`, complete the square in `v`:
\[
c_{22}v^2+2c_{12}uv
=c_{22}\left(v+{c_{12}\over c_{22}}u\right)^2
-{c_{12}^2\over c_{22}}u^2.
\]
Since the unnormalised slice density in `v` is at most `M`, the one-dimensional square pushforward gives
\[
p_{Q\mid X=x,U=u}^{\rm (slice)}(t)
\le {M\over\sqrt{|c_{22}|}}\,
{1\over\sqrt{|t-2\beta ux-\kappa u^2|}},
\qquad
\kappa=c_{11}-{c_{12}^2\over c_{22}}.
\]
The only dependence retained in this step is the actual joint density of `(U,V)`; no independence of `U,V` is introduced.

For each fixed `u!=0`, the bathtub/rearrangement bound for a one-dimensional cap-one probability density is
\[
\int_{\mathbb R} f(x)|a x-r|^{-1/2}\,dx
\le 2\sqrt2\,|a|^{-1/2}.
\]
With `a=2 beta u`, this becomes exactly
\[
\int f(x)|t-2\beta ux-\kappa u^2|^{-1/2}\,dx
\le {2\over\sqrt{\beta|u|}}.
\]
Hence
\[
p_{\rm near}(t)
\le {M\over\sqrt{|c_{22}|}}
\int_{|u|<\delta}{2\,du\over\sqrt{\beta|u|}}
={8M\sqrt\delta\over\sqrt\beta\sqrt{|c_{22}|}}.
\]
Using `D=beta^2|c22|` and setting `z=beta delta`,
\[
p_Q(t)
\le 8M\sqrt{z/D}+{1\over2z}.
\]
The right side is minimised at
\[
z={D^{1/3}\over4M^{2/3}},
\]
where the two contributions are respectively `4 M^(2/3) D^(-1/3)` and
`2 M^(2/3) D^(-1/3)`. Thus
\[
p_Q(t)\le6M^{2/3}D^{-1/3}
\]
for almost every `t`, uniformly in `t`. Tonelli plus the preceding one-dimensional pushforward formulas gives absolute continuity. This proof does not by itself produce a continuous representative.

## Equation-level application of the completed fleet04/B16 result

The compatible partner result used here is fleet04/B16,
`QFORM-RULED-PLUECKER-ENDPOINT-v1`, source

`yspennstate/math-open-problems@b111363ff02b67015d14db35482e0150591744cd:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260922T231542Z-fleet04-B16-QFORM-r1/REPORT.md`.

In its exact-rank-three `d=0` endpoint, the unresolved geometry is a leverage-one original-coordinate coloop plus a rank-two spectral plane. Write that original coordinate as `X0`. The remaining original coordinates are independent of `X0`, and their orthogonal two-dimensional spectral projection is `Y`.

The partner's ruled proof explicitly uses the completed bounded-density product-projection theorem and records the normalized two-dimensional projection cap
\[
\|\rho_Y\|_\infty\le 2.
\]
This is precisely the `M=2` hypothesis above; it is applied before the nonlinear quadratic pushforward, not substituted as a receiver-only conditional density.

At the exact **null-coloop** endpoint `A_{00}=0`, choose an orthonormal spectral basis whose first vector is the coloop direction. The resulting `3x3` spectral matrix `B` has
\[
|\det B|=|\det\Lambda|\ge1.
\]
Therefore the new theorem gives the two-sided estimate
\[
\boxed{
\|p_Q\|_\infty
\le 6\,2^{2/3}|\det\Lambda|^{-1/3}
\le 6\,2^{2/3}
<9.525.
}
\]
This closes the previously unpaid convex/two-sheet side at the **exact** null-coloop endpoint. The partner's one-sheet ruled bound `pi sqrt(2)` remains valid and is stronger on that side, but is not needed for the two-sided conclusion above.

## What this does and does not resolve

This is stronger than a bounded projection-density statement by itself because it proves the nonlinear integration theorem needed at a genuine singular endpoint while preserving the original product grouping: `X0` is independent of the entire remaining coordinate bank, and only the two-dimensional **unconditional** product projection is compressed to the density cap `M=2`.

It does **not** close:
1. the near-null but nonzero coloop regime `0<|A_{00}|<<1`, where the exact `a=0` affine-in-`X0` argument must be fused quantitatively with the existing nonzero scalar-pivot half-Riesz theorem;
2. arbitrary higher-rank spectral remainders, where additional spectrum changes the same nonlinear fibers;
3. the full continuity conclusion.

The next target-relevant implication is therefore a quantitative **null-to-nonnull interpolation**:
\[
aX_0^2+2X_0L(Y)+q_2(Y),\qquad |a|\ll1,
\]
with a bound uniform as `a->0`, using the present product-projection estimate at `a=0` and the orientation-free scalar-pivot half-Riesz estimate away from zero without paying a reciprocal power that diverges in the overlap. Only after that should the result be fused with the higher-rank/cross-block branches.

## Correction discipline

Consumed live corrections include the failure of law-uniform pointwise quadratic phase decay, dimension-free fiber-sup integration, arbitrary-joint 3D coarea, positive conditional projection-height moments, conditional cap-as-independence, and local fixed-minor/cross-rank dichotomies. None is used as a premise here.

## Verification notes

An exact algebra/constant checker accompanies this report. It verifies:
- `det([[0,b,0],[b,c11,c12],[0,c12,c22]]) = -b^2 c22`;
- the bathtub scaling constant;
- the near/far optimizer;
- the final coefficient `6`;
- the partner specialization `M=2,D>=1`, numerically `6*2^(2/3)<9.525`.

A narrowly scoped fallback privacy scan was run over the report/checker text for credential-like strings and machine-local paths. It found none. This is not a substitute for a repository-wide secret scanner; only the newly generated B16 files were scanned.

## Status

`SUPPORTING_THEOREM / EXACT NULL-COLOOP ENDPOINT PAID / FULL QFORM OPEN`.

No counterexample to the owner conjecture is supplied. A universal constant for every allowed matrix is not yet proved.
