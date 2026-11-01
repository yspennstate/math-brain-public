SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-23T02:47:47Z.
attacking: the hub endpoint h=1 — derive a zero-diagonal star quarter-Riesz estimate and splice it into the partner indefinite-pair logarithmic transducer.

# fleet01/B03 r21 — zero-hub quarter-Riesz endpoint plus indefinite-pair splice

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Run: `20260923T024747Z-fleet01-B03-QFORM-r21`  
Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full universal QFORM conjecture remains open. This report closes one analytic endpoint which the latest designated partner leaves outside its k=1 decoupled-volume theorem: the **pure hub case h=1** when the hub has exactly zero physical diagonal. The proof is entirely in original coordinates. It never conditions one member of a dependent sum/difference pair on the other, and it does not use a law-uniform pointwise quadratic-phase estimate.

## 1. Fresh sources and correction boundary


The latest designated partner result actually used below is fleet02/B03:

`yspennstate/math-open-problems@fab77e73a6163b18eea08d2807aa1a38166279ff`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T021907Z-fleet02-B03-QFORM-auto11/REPORT.md`.

Its completed indefinite-pair transducer says: after completing an invertible indefinite ORIGINAL-coordinate pair `B`, write

`D=|det B|`, `kappa=sigma_min(B)`.

If the residual random variable `R` satisfies

`sup_t P(|R-t|<rho) <= H rho^(1/4)` for every `rho>0`,

then the full quadratic form has

`||p_Q||_infinity <= 3*2^(4/3) H^(2/3) D^(-1/3) kappa^(-1/6)`.      (1.1)

The source proves this by averaging the logarithmic singularity of the completed physical pair and permits arbitrary dependence of the pair shifts on `R`.

The one-dimensional original-product projection input is source-pinned to fleet02/B04:

`yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T181702Z-dac07509/REPORT.md`,

which records, for every nonzero coefficient vector `m` and independent cap-one original coordinates `Y`,

`||p_(m^T Y)||_infinity <= sqrt(2)/||m||_2`.                       (1.2)

The live corrections respected here include: no post-rotation independence; no conditional cap for a conjugate sum/difference variable; no law-uniform scalar pointwise Fresnel decay; no arbitrary-joint coarea lemma; no universal good local minor/cross-rank selection. The theorem below is a scoped original-coordinate packet, not an exhaustive structural reduction.

## 2. A scalar fractional bathtub inequality

### Lemma 2.1

Let `X` have a probability density `f` satisfying `0<=f<=M`, let `c!=0`, let `s` be arbitrary, and let `0<alpha<1`. Then

`E |cX-s|^(-alpha) <= [2^alpha/(1-alpha)] M^alpha |c|^(-alpha)`.    (2.1)

#### Proof

By translation and scaling it is enough to maximize

`integral |x|^(-alpha) f(x) dx`

among probability densities `0<=f<=M`. Since `|x|^(-alpha)` is symmetric decreasing, the bathtub principle places all mass at height `M` on the centered interval of length `1/M`. Hence

`integral |x|^(-alpha) f(x) dx`
` <= M * integral_{-1/(2M)}^{1/(2M)} |x|^(-alpha) dx`
` = [2^alpha/(1-alpha)] M^alpha`.

Scaling by `c` proves (2.1). QED.

No regularity or connected-support assumption is used; fragmented densities are allowed.

## 3. New zero-diagonal hub theorem

Let `X` be one original coordinate, independent of a vector `Y` of other original coordinates, all input densities bounded by one. Let `m!=0`, `beta in R`, and let `S(Y)` be **any** real measurable random function finite almost surely. Put

`R = X(2 m^T Y + beta) + S(Y)`.                                    (3.1)

In a quadratic form this is exactly the situation of a physical coordinate with zero diagonal whose entire cross row to a disjoint residual bank is `m`; arbitrary quadratic, linear and constant terms in that residual bank are absorbed into `S`.

### Theorem 3.1 — `QFORM-ZERO-HUB-FRACTIONAL-RIESZ-v1`

For every `0<alpha<1`,

`boxed:
 sup_z E|R-z|^(-alpha)
 <= [2^(3alpha/2)/(1-alpha)^2] ||m||_2^(-alpha).
`                                                                   (3.2)

In particular, at `alpha=1/4`,

`boxed:
 H_(1/4)(R):=sup_z E|R-z|^(-1/4)
 <= C_star ||m||_2^(-1/4),
 C_star=(16/9) 2^(3/8)=2.305492541601795... .
`                                                                   (3.3)

#### Proof

Condition on `Y`. For a fixed value `Y=y`, set

`c(y)=2m^T y+beta`.

The conditional variable is `c(y)X+S(y)`. Whenever `c(y)!=0`, Lemma 2.1 with `M=1` gives, uniformly in `z`,

`E_X |c(y)X+S(y)-z|^(-alpha)
 <= [2^alpha/(1-alpha)] |c(y)|^(-alpha)`.                           (3.4)

Let `L=m^T Y`. By the original-product projection theorem (1.2),

`||p_L||_infinity <= M_L:=sqrt(2)/||m||_2`.                         (3.5)

Therefore `V=2L+beta` has density cap `M_L/2`, and in particular `P(V=0)=0`. Applying Lemma 2.1 to `V` with `c=1`, `s=0`, and density cap `M_L/2` gives

`E |2L+beta|^(-alpha)
 <= [2^alpha/(1-alpha)] (M_L/2)^alpha
 = M_L^alpha/(1-alpha)`.                                            (3.6)

Average (3.4) over `Y`; the null set `c(Y)=0` is harmless (equivalently use truncation and Fatou). Combining (3.4)--(3.6),

`sup_z E|R-z|^(-alpha)
 <= [2^alpha/(1-alpha)^2] M_L^alpha`
` <= [2^(3alpha/2)/(1-alpha)^2] ||m||_2^(-alpha)`.

This is (3.2). Substituting `alpha=1/4` gives (3.3). QED.

### Scope note

The arbitrary term `S(Y)` is important: the theorem allows arbitrary in-bank quadratic curvature and arbitrary affine terms. What is exact is the **zero physical diagonal of the hub X**. The theorem does not silently replace a small nonzero diagonal by zero.

## 4. Dependence-safe independent-copy time integral

Let `R'` be an independent copy of `R`. Since (3.2) is translation-uniform,

`E|R-R'|^(-alpha)
 = E_{R'} E_R |R-R'|^(-alpha)
 <= [2^(3alpha/2)/(1-alpha)^2] ||m||_2^(-alpha).                    (4.1)

The one-dimensional Riesz-energy identity for `0<alpha<1` is

`integral_R |t|^(alpha-1) |phi_R(t)|^2 dt`
` = 2 Gamma(alpha) cos(pi alpha/2) E|R-R'|^(-alpha)`.               (4.2)

A rigorous justification uses the positive Gaussian regularization of the Riesz multiplier and monotone convergence on the Fourier side; finiteness follows from (4.1). Equation (4.2) is exactly the independent-copy identity `|phi_R|^2=phi_(R-R')` at the fractional-energy level.

At `alpha=1/4`, (4.1)--(4.2) yield

`boxed:
 integral_R |t|^(-3/4)|phi_R(t)|^2 dt
 <= C_time ||m||_2^(-1/4),
`

where

`C_time=2 Gamma(1/4) cos(pi/8) C_star`
`      =15.445079149508198... .`                                  (4.3)

This calculation never separates the dependent variables `X-X'` and `X+X'`; in fact it avoids conditioning on either member of that conjugate pair. All conditioning in Section 3 was on the disjoint original bank `Y` before introducing the independent copy.

## 5. Actual application of the latest fleet02/B03 result

Now suppose a full quadratic form contains an invertible indefinite ORIGINAL-coordinate physical pair with matrix `B`. Complete that pair exactly as in the fleet02/B03 source. Put

`D=|det B|`, `kappa=sigma_min(B)`.

Assume that the resulting residual has the zero-hub form (3.1) with cross vector `m!=0`. By Markov and (3.3), for every `rho>0`,

`sup_z P(|R-z|<rho)
 <= C_star ||m||_2^(-1/4) rho^(1/4)`.                              (5.1)

Thus the partner theorem (1.1) applies with

`H=C_star ||m||_2^(-1/4)`.

We obtain the new packet theorem

### Theorem 5.1 — `QFORM-INDEFINITE-PAIR-ZERO-HUB-v1`

`boxed:
 ||p_Q||_infinity
 <= C_hub D^(-1/3) kappa^(-1/6) ||m||_2^(-1/6),
`

where

`C_hub=3*2^(4/3) C_star^(2/3)`
`     =13.192802571602055... .`                                   (5.2)

Consequently every interval `I` satisfies the genuine linear small-ball estimate

`P(Q in I)
 <= C_hub D^(-1/3) kappa^(-1/6) ||m||_2^(-1/6) |I|`.              (5.3)

This is an actual equation-level use of the designated fleet02/B03 result. Their k=1 decoupled-volume theorem requires row-energy marginal `h<1`; the present theorem supplies a different analytic endpoint when the residual cross geometry is a pure star, for which the unique active row has `h=1`, provided the hub diagonal is exactly zero.

The conclusion here is absolute continuity with an essential `L^infinity` bound. **Continuity is not proved by this branch.**

## 6. Concrete target family at the previously excluded hub endpoint

Let

`B0=[[0,1],[1,1]]`.                                                (6.1)

Its eigenvalues are

`lambda_+=(1+sqrt(5))/2`, `lambda_-=(1-sqrt(5))/2`,

so

`D=|det B0|=1`,
`kappa=sigma_min(B0)=(sqrt(5)-1)/2`.                               (6.2)

On a disjoint block consisting of a singleton hub and an `m`-coordinate bank, take any unit vector `v in R^m` and the zero-diagonal star

`S_m=[[0,v^T],[v,0_m]]`.                                          (6.3)

Its nonzero eigenvalues are `+1,-1`. Set

`A_m=B0 direct_sum S_m`.                                           (6.4)

Therefore the nonzero spectrum of `A_m` is

`{(1+sqrt(5))/2, (1-sqrt(5))/2, +1, -1}`.                         (6.5)

Exactly three eigenvalues have absolute value at least one: `(1+sqrt(5))/2`, `+1`, and `-1`. Hence (6.4) is a genuine exact-threshold target family for every `m`.

For independent cap-one inputs the residual after the `B0` pair is simply

`R=2 X_0 v^T Y`,                                                  (6.6)

which is (3.1) with `m=v`, `beta=0`, `S=0`, and `||m||_2=1`. Its k=1 volume-sampling marginal is exactly `h=1`, so the partner's `h<1` one-volume theorem is at its excluded endpoint. Theorem 5.1 nevertheless gives

`boxed:
 ||p_(X^T A_m X)||_infinity
 <= C_hub ((sqrt(5)-1)/2)^(-1/6)
 =14.294479188689094...,
`                                                                   (6.7)

uniformly in `m`, in the choice of unit `v`, and in all admissible input laws.

Thus the analytic obstruction at the pure-hub volume marginal is not intrinsic when the hub is an exact zero-diagonal coordinate; its product-linear structure supplies all fractional orders `alpha<1` directly.

## 7. What remains unpaid

This does **not** solve the full conjecture. The first unpaid continuation in this mechanism is the **near-zero-diagonal hub bridge**: if the dominant residual cross geometry is a pure or nearly pure star but the hub carries an arbitrary small nonzero quadratic coefficient, Section 3 no longer conditions to a linear variable, and the present argument does not provide a scale-free replacement. A full proof also still needs an exhaustive product-preserving structural compiler from the bare three-large-eigenvalue hypothesis to one of the already paid ridge, multi-volume, physical-core, aggregate-square, mixed-hub, or zero-hub exits.

No source-matching published theorem ending the full target was identified in this run. No full-solution claim is made, and no independent end-to-end review is requested for this supporting lemma at this stage.

Claim IDs proposed for worker memory only:
- `QFORM-ZERO-HUB-FRACTIONAL-RIESZ-v1`;
- `QFORM-ZERO-HUB-WEIGHTED-COLLISION-v1`;
- `QFORM-INDEFINITE-PAIR-ZERO-HUB-v1`.
