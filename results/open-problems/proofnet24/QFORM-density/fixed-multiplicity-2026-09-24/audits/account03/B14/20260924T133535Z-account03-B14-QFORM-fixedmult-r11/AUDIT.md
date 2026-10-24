# account03/B14 r11 — fixed-multiplicity end-to-end audit, rough-law closure, and 2582 constant

**Run:** `20260924T133535Z-account03-B14-QFORM-fixedmult-r11`  
**Objective:** `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
**Baseline manuscript:** `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
**Nine-direction source:** account03/B04 at `8ff490c177d0cd7d6f33130f1431785e312a9d10`  
**Latest constant source consumed:** account03/B10 at `636863855ed4c6c976785e35fae8d855f49450ea`  
**B14 partner localization consumed:** account04/B14 cap-preserving compact completion, report `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T171953Z-account04-B14-QFORM-r2/REPORT.md`.

## Verdict

**PASS** for the baseline seventeen-eigenvalue theorem in this independent B14 read. I read the complete 790-line manuscript and the current proof map, source manifest, checker source and recorded checker output. I found no fatal mathematical defect. The one local wording issue already independently reported elsewhere remains harmless: after dropping rows with `b_i=0` in the product-projection proof, the displayed equality `sum_i(1-b_i)=d` should be read as `sum_{b_i>0}(1-b_i)<=d` (or as equality before dropping those rows). The argument only needs the upper bound, so no theorem or constant changes.

I also independently checked the nine-eigenvalue reduction through its self-contained B04 grouped-crossing compiler and the manuscript pivot machinery. The reduction is mathematically compatible with arbitrary rough coordinate laws and arbitrary affine terms. This run sharpens the currently written `<2600 K^2/s` nine-direction constant to

\[
\boxed{\quad s_9(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}<2582\,K^2/s.\quad}
\]

No moment, support, log-concavity, smoothness, sign, exact-rank, leverage, diagonal-basis, or post-rotation-independence assumption is introduced. Global continuity is **not** proved; the no-pivot crossing branch is `C_0`, while the pivot branches are used through measure domination.

The unrestricted three-eigenvalue conjecture remains **OPEN**.

## 1. End-to-end baseline ledger

I rechecked the source in the order recorded by `proof_map.csv`.

- **Fourier/Riesz layer — PASS.** The Fourier convention, Gaussian regularization, Plancherel constant, inversion constant and half-Riesz normalization agree. The order-three Fourier envelope is used only with the `|t|^{-1/2}` Riesz weight, never incorrectly as an `L^1` density envelope.
- **Schur/rank layer — PASS.** The principal-pivot Schur count is valid, including the singular-`A` approximation. The nonsymmetric singular-value perturbation is used legitimately.
- **Geometric BL and projections — PASS with the nonfatal wording repair above.** Random coordinates are never rotated and then declared independent. Orthogonal transformations occur only inside deterministic integrals/Jacobians.
- **Decoupling/determinant layer — PASS.** Original-coordinate two-copy decoupling, the regularized frame, entropy cancellation and fourth-root determinant exponent `-1/8` are consistent. Cauchy–Binet gives the stated crossing volumes.
- **Square/definite/hyperbolic kernels — PASS.** These are conditional measure-dominating calculations. Exceptional critical levels for rough densities are avoided by testing against nonnegative Borel functions and using Tonelli.
- **Quarter-power concentration — PASS.** It uses the determinant estimate on an original-coordinate cross block and therefore does not invoke the refuted law-uniform van-der-Corput claim.
- **Disjoint-minor interpolation — PASS.** The bordered-minor identity, singular-seed inequality, `rank R<=3r`, sharper `rank R[L,L]<=r`, zero diagonal of `E`, and vanishing of `D` on the seed are all consistent. The exact diagonal-dominance margin is `371/400-23/28=297/2800>0`.
- **Final seventeen-direction branches — PASS.** No pivot gives `<2400`; scalar pivot gives `6010`; definite pair `<40`; indefinite pair `<251`; scaling gives the advertised `10^4 K^2/s` statement.

The repository packaging gap seen in an earlier B14 invocation is now repaired on current master: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py` and `checks.json` are present. I read the checker source and the recorded PASS output; this is reproducibility evidence, not a proof certificate.

## 2. Rough-law / localization closure with zero constant loss

The B14 issue is whether pointwise density representatives, exceptional fibers, arbitrary translations, distant fragments or unbounded support can silently enter the fixed-multiplicity proof. They do not need to.

### Lemma — smooth-compact reduction for interval bounds

Fix a Borel map `T:R^n->R` (in particular any quadratic polynomial with arbitrary affine term). For independent coordinate probability densities `0<=f_i<=1` and every `epsilon>0`, there exist independent `C_c^infinity` probability densities `g_i` with `0<=g_i<=1` such that

\[
 d_{TV}\!\left(T_\#\bigotimes_i f_i\,dx,\;T_\#\bigotimes_i g_i\,dx\right)<\epsilon.
\]

**Proof.** Account04/B14's cap-preserving compact completion first replaces each `f_i` by a compactly supported cap-one density with arbitrarily small coordinate TV error. Convolution with a compactly supported smooth probability mollifier preserves nonnegativity, total mass and the `L^infinity` cap, gives `C_c^infinity`, and converges in `L^1` to that compact density. Product TV is bounded by the sum of coordinate TVs, and measurable pushforward contracts TV. QED.

Consequently, any interval estimate

\[
\Pr\{T(X)\in I\}\le C|I|
\]

proved uniformly for smooth compact cap-one product densities passes to **all** cap-one product densities with exactly the same `C`. There is no common support radius, fragment count, fragment separation, translation bound or moment bound. This reduction transfers essential `L^infinity` density bounds, but not continuity: total-variation limits of continuous densities need not have continuous representatives.

This supplies an alternative rigorous closure of every rough-law branch in the baseline and nine-direction arguments. One may therefore perform all pointwise coarea manipulations on smooth compact approximants and pass the final interval inequality, rather than choosing exceptional-slice representatives for the original rough laws.

## 3. Independent check of the nine-direction mechanism

Normalize to `K=s=1`, `eta=1/100`, `kappa=1/80^2`.

### No pivot

The audited spectral-to-volume proposition at order three uses exactly `4*3-3=9` directions:

\[
V_3(A)\ge\kappa^3.
\]

A fair original-coordinate cut yields `E_3(M)>=4^{-3}kappa^3`. The B04 marginal-free third-crossing compiler then gives a continuous bounded density `<2400`. Its proof aggregates physical crossing volume before paying reciprocal local minors; its weighted-subset entropy inequality is the standard ordered-subset subadditivity identity

\[
H(w)+\sum_i\alpha_i\log\alpha_i\le \ell\log\ell-\log(\ell!).
\]

No conditional marginal cap and no rotated independence are used.

### Scalar pivot

If `|A_hh|>=eta`, the Schur complement retains at least eight unit spectral directions. If that Schur complement has no `eta`-pivot, it has at least five unit directions, so the order-two crossing/half-Riesz receiver gives full half potential `<153`. If it has a pivot, Section 4 below gives the sharper uniform full half-potential bound `<258.2`. The scalar-square profile therefore costs at most a factor `eta^{-1/2}=10`.

### Pair pivots

A definite physical pair gives `<10 pi<32`. An indefinite pair leaves at least seven unit spectral directions in its Schur complement, hence at least one unit operator-norm direction; the manuscript hyperbolic/log-potential calculation gives `<251`. These branches are unchanged.

Thus nine directions suffice once the scalar-pivot full half potential is controlled.

## 4. New constant sharpening: `2600 -> 2582`

The current B10 proof already improves the quarter-power Gaussian coefficient to the rational upper bound

\[
C_q:=2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8)
<\frac{174933}{40000}.
\]

I sharpen only the bookkeeping after this point.

### 4.1 Exact singular-convolution constant

For

\[
J(d)=\int_{-1}^1|x|^{-1/2}|x-d|^{-1/2}\,dx,
\]
`J(-d)=J(d)`. For `0<d<=1`, putting `x=d^{-1/2}>=1`, direct integration gives

\[
J(d)=2\operatorname{asinh}x+\pi+2\operatorname{acosh}x.
\]

The function

\[
2\operatorname{asinh}x+2\operatorname{acosh}x-4\log x
\]

is increasing on `[1,infinity)` because

\[
\frac1{\sqrt{x^2+1}}+\frac1{\sqrt{x^2-1}}\ge\frac2x
\]

by convexity of `u -> u^{-1/2}` at `u=x^2+-1`. Its limit is `4 log 2`. For `d>=1`, the alternative formula

\[
J(d)=2\operatorname{asinh}(d^{-1/2})+2\arcsin(d^{-1/2})
\]

is maximal at `d=1` and is also below `pi+4 log2`. Hence, for every `d!=0`,

\[
\boxed{\quad J(d)\le \pi+4\log2+2\log_+(1/|d|).\quad}
\]

### 4.2 Rational logarithm certificates

Set

\[
q_2=\frac{1733}{2500},\qquad q_c=\frac{73777}{50000}.
\]

The positive Taylor partial sums of `e^x` give exact rational certificates

\[
\sum_{k=0}^{6}\frac{q_2^k}{k!}-2
=\frac{15635577084913721569}{175781250000000000000000}>0,
\]

and

\[
\sum_{k=0}^{9}\frac{q_c^k}{k!}-\frac{174933}{40000}>0.
\]

Therefore

\[
\log2<q_2=0.6932,
\qquad
\log(174933/40000)<q_c=1.47554.
\]

Together with `pi<22/7`, the quarter-power small-ball estimate implies the uniform logarithmic potential bound

\[
L_{\log}<4+4q_c.
\]

At a scalar pivot, the improved `J` envelope yields truncated half potential

\[
H_{\rm scalar}
<10\left(\frac{22}{7}+4q_2+2(4+4q_c)\right)
=\frac{1125249}{4375}
=257.1997714\ldots.
\]

Adding the tail `|Q-a|>1`, whose half-Riesz kernel is at most one, gives

\[
\sup_a\mathbb E|Q-a|^{-1/2}
<\frac{1129624}{4375}
=258.1997714\ldots.
\]

The optimized `q=2/9` hyperbolic-pair calculation from the B10 source has truncated half potential `<242` (and hence full half potential `<243`); the definite-pair branch is `<161` after adding the tail. Thus `258.1998` controls every pivot under the two-direction hypothesis.

For the **outer** scalar pivot in the nine-direction theorem, multiply by `eta^{-1/2}=10`:

\[
10\cdot\frac{1129624}{4375}
=\frac{2259248}{875}
=2581.997714\ldots
<2582,
\]

with exact margin `2/875`. The no-pivot branch is `<2400`, the main definite pair is `<32`, and the main indefinite pair is `<251`. Hence the normalized nine-direction theorem has density `<2582`; scaling gives `<2582 K^2/s`.

## 5. Partner result applied to an actual inequality

Apply account04/B14's cap-preserving compact completion to an arbitrary translated, fragmented, unbounded-support product law. Let `A=A^T` satisfy `s_9(A)>=s>0`, let `t in R^n` be arbitrary, and let the original independent coordinate densities be bounded by `K`. Since

\[
(X+t)^TA(X+t)=X^TAX+2(At)^TX+t^TAt,
\]

the translation is exactly an allowed affine term. Prove the interval bound first on the smooth compact approximants above and use product-TV plus pushforward contraction. The result is the actual translation-uniform inequality

\[
\boxed{\quad
\sup_{t\in\mathbb R^n}
\|p_{(X+t)^TA(X+t)}\|_{\infty,\mathrm{ess}}
<2582\,K^2/s.
\quad}
\]

The constant is independent of support location, diameter, number/separation of fragments and all moments. This is a genuine application of the completed account04/B14 localization theorem to the current fixed-multiplicity result.

## 6. Status and next obstruction

- Baseline `s_17`: **PASS** in this run; no fatal gap found.
- Nine-direction theorem: **PASS** in this run; this report independently sharpens the constant to `<2582 K^2/s`.
- Rough-law/localization closure: **PROVED with zero constant loss** for interval/essential-density estimates.
- Global continuity: **OPEN** outside the Fourier-integrable no-pivot branch.
- Multiplicity eight: **OPEN**. The current interpolation mechanism saturates at the order-two seed in the order-three no-pivot argument; lowering `9 -> 8` needs a new structural or endpoint mechanism, not a tail/translation regularization.
- Full three-eigenvalue conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

Execution classification remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval and mathematical readback occurred, but no native receiver-memory ingestion was observed.
