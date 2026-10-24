# account02/B14 — three-point inverse-gap localization without fragments

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control revision:** `2026-09-22.5`  
**Run:** `20260922T150227Z-b14-qform-localization-r14`  
**Assignment:** Translations and localization  
**Status:** `SUPPORTING_LOCALIZATION_LEMMA / NEW_FRAGMENT-FREE_COMPILER / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The owner target remains the full arbitrary-dimensional statement: for independent real `X_i` with probability densities `0<=f_i<=1` and every real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove one universal finite `C` such that

`P{X^T A X in J} <= C |J|`

for every bounded interval `J`, or construct a genuine target-valid counterexample. No moments, bounded support, connected support, centering, post-rotation independence, or sign restriction is available.

The assigned partner `account03/B14` has now proved two facts that determine the localization interface:

1. `yspennstate/math-open-problems@2208c3f666582999f1fbc7e55921a4530cbe2789` proves **select-before-localize**: an original-coordinate active block may be left completely unfragmented; if its deterministic-outside estimate is uniform in the outside-induced affine/self terms, then arbitrary outside laws transfer with exactly the same constant.
2. `yspennstate/math-open-problems@54f2d04e936d0dfefe345d17ee18a46b35039d7e` proves there is **no universal fixed fragment-count cap** for the exact coordinatewise bathtub localization, even for `A=I_3`.

The preceding account02/B14 run supplied an acyclic fragment-packing compiler and showed that arbitrary component-dependent cycles can create logarithmic or power losses. The first unpaid implication was therefore to find a stronger mechanism that can keep a genuinely coupled active triple unfragmented while still paying the inverse-gap singularities that a shell/coarea calculation may generate.

This run proves such a mechanism for the natural three-point pair-gap singularities. It uses the original product law directly and is uniform under arbitrary deterministic shifts. No finite-fragment reduction is used inside the active triple.

## 2. Main theorem: a three-point inverse-gap moment bound

Let `X_1,X_2,X_3` be independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1`. Let

`a,b,c in [0,1)` and `s=a+b+c<2`.

Then

`E[ |X_1-X_2|^{-a} |X_2-X_3|^{-b} |X_3-X_1|^{-c} ] <= C(a,b,c)`,

where the finite explicit constant

`C(a,b,c)`

`= 1`

`  + 2/(1-a) + 2/(1-b) + 2/(1-c)`

`  + 4/((1-a)(1-b)) + 4/((1-a)(1-c)) + 4/((1-b)(1-c))`

`  + [2/(2-s)] * [ B(1-a,1-b) + B(1-a,1-c) + B(1-b,1-c) ]`.      (2.1)

Here `B` denotes the beta function. The set where two variables coincide has probability zero, so the displayed random variable is well defined almost surely.

The bound is completely independent of support locations, diameters, fragment counts, moments, or relative translations.

### 2.1 A one-pair truncated singularity bound

For `0<=theta<1`, independence and the cap `f_j<=1` give, for every fixed `x`,

`int_{|y-x|<=1} |y-x|^{-theta} f_j(y) dy`

` <= int_{-1}^1 |u|^{-theta} du = 2/(1-theta)`.               (2.2)

Hence

`E[ |X_i-X_j|^{-theta} 1_{|X_i-X_j|<=1} ] <= 2/(1-theta)`.     (2.3)

### 2.2 Two-edge terms

For example, condition on `X_2=y`. Independence of `X_1` and `X_3` gives

`E[ |X_1-X_2|^{-a} 1_{|X_1-X_2|<=1}`
`    * |X_2-X_3|^{-b} 1_{|X_2-X_3|<=1} | X_2=y ]`

` <= [2/(1-a)] [2/(1-b)]`.                                    (2.4)

Averaging in `y` yields `4/((1-a)(1-b))`; the other two pairs are identical after relabeling.

### 2.3 The genuinely three-edge term

It remains to bound

`T = E[ prod_edges |X_i-X_j|^{-theta_ij}`
`          * 1_{all three pair distances <=1} ]`,              (2.5)

with `theta_12=a`, `theta_23=b`, `theta_13=c`.

Split `R^3` into the six orderings of `(x_1,x_2,x_3)`. On one ordering, write the ordered coordinates as

`x_low=t`, `x_mid=t+u`, `x_high=t+u+v`,

with `u,v>=0`. The condition that all three pair distances are at most one is exactly `u+v<=1`. The Jacobian is one.

For fixed `u,v`, the integral of the three densities over the common translation `t` is at most one: their product is bounded pointwise by any one of the density factors, and translating that factor does not change its integral. Thus this ordering contributes at most

`int_{u,v>=0, u+v<=1} u^{-p} v^{-q} (u+v)^{-r} du dv`,         (2.6)

where `(p,q)` are the exponents on the two adjacent ordered gaps and `r` is the exponent on the long gap.

Set `rho=u+v`, `w=u/(u+v)`. Then `du dv = rho d rho d w`, so (2.6) equals

`[int_0^1 rho^{1-s} d rho] [int_0^1 w^{-p}(1-w)^{-q} dw]`

`= B(1-p,1-q)/(2-s)`.                                          (2.7)

The integral is finite exactly under `p<1`, `q<1`, `s<2`. Reversing an ordering leaves the adjacent exponent pair unchanged. Across the six orderings, each of the three unordered exponent pairs occurs twice. Therefore

`T <= [2/(2-s)] * [ B(1-a,1-b)+B(1-a,1-c)+B(1-b,1-c) ]`.       (2.8)

### 2.4 Finish by expanding only the near-diagonal pieces

For every `r>0` and `0<=theta<1`,

`r^{-theta} <= 1 + r^{-theta} 1_{r<=1}`.                       (2.9)

Multiply (2.9) over the three pair distances. The empty term contributes one, the three singleton terms are bounded by (2.3), the three two-edge terms by (2.4), and the full three-edge term by (2.8). This is exactly (2.1). QED.

## 3. Square-root triangle: an explicit universal constant below 99

For the shell-relevant symmetric choice

`a=b=c=1/2`,

we have `s=3/2` and `B(1/2,1/2)=pi`. Formula (2.1) becomes

`C(1/2,1/2,1/2) = 61 + 12 pi < 98.70`.                         (3.1)

Thus

`E prod_{i<j} |X_i-X_j|^{-1/2} <= 61+12pi`.                   (3.2)

This is a genuinely cyclic inverse-gap estimate. Unlike the previous arbitrary fragment-anchor compiler, it does **not** require an acyclic ordering, because the three singularities come from the actual common triple of independent coordinates rather than arbitrary mutually chosen fragment centers.

## 4. Sharpness of the exponent threshold

The condition `a+b+c<2` is sharp for a raw three-gap absolute-value compiler.

Take `X_1,X_2,X_3` iid `Uniform[0,1]`. Consider the ordering `x_1<x_2<x_3` and write

`u=x_2-x_1`, `v=x_3-x_2`.

On a fixed interior range of the translation variable `x_1`, the density product is one. Restrict additionally to `u,v>0`, `u+v<epsilon`, and `w=u/(u+v)` in `[1/3,2/3]`. On this region the angular factor

`w^{-a}(1-w)^{-b}`

is bounded below by a positive constant, while the radial integral is

`int_0^epsilon rho^{1-(a+b+c)} d rho`.                         (4.1)

It diverges logarithmically when `a+b+c=2` and by a power when the sum exceeds two. Hence for exponents individually below one but with total at least two,

`E prod_{i<j}|X_i-X_j|^{-theta_ij} = +infinity`                (4.2)

for this exact cap-one connected-support product law.

So the threshold in Section 2 is not an artifact of disconnected supports or of the proof. A future local shell argument that produces a raw pair-gap exponent budget at or above two cannot be closed merely by absolute integration against the original product law.

## 5. Uniformity under arbitrary shifts and outside conditioning

Let `tau_i` be arbitrary real constants and put `Y_i=X_i+tau_i`. The `Y_i` remain independent probability variables with densities bounded by one. Therefore the same constant gives

`E prod_{i<j}|(X_i+tau_i)-(X_j+tau_j)|^{-theta_ij}`

` <= C(theta_12,theta_23,theta_13)`                            (5.1)

uniformly in all three shifts.

More generally, if `z` is a deterministic outside vector and `tau_i=tau_i(z)` are arbitrary measurable functions of that vector, then (5.1) holds pointwise for every `z`, with the same constant. No bound on `|z|`, on the shifts, or on any moment is needed.

This is the exact localization feature needed after selecting an original-coordinate active triple before localizing its complement.

## 6. Target-level conditional compiler

Let `S={i,j,k}` be a fixed original-coordinate active triple selected from `A` before any localization. Suppose a source-valid shell/coarea argument proves, for every deterministic outside vector `z`, every bounded interval `J`, and every admissible product law on the three active coordinates, an estimate of the form

`P{ Q_A(X_S,z) in J | z }`

` <= K |J| * E_S[ prod_{r<s in S}`
`       |(X_r+tau_r(z))-(X_s+tau_s(z))|^{-theta_rs} ]`,         (6.1)

where `0<=theta_rs<1` and

`theta_ij+theta_jk+theta_ki < 2`.                               (6.2)

Then Sections 2 and 5 give, uniformly in `z`,

`P{ Q_A(X_S,z) in J | z } <= K C(theta) |J|`.                  (6.3)

Applying the completed account03/B14 deterministic-outside criterion (`2208c3f...`) and integrating the actual outside product law gives

`P{X^T A X in J} <= K C(theta) |J|`                            (6.4)

with no support, moment, translation, or fragment-count hypothesis. The active triple never needs to be fragmented. The partner's newest fixed-fragment-count obstruction (`54f2d04...`) is therefore automatically respected.

This is a target-level implication: **any** heavy/localized active-triple shell estimate of the exact form (6.1), with subcritical total pair-gap exponent, immediately extends to the owner's full arbitrary-support laws with one dimension-free constant.

## 7. Relation to the previous acyclic packing theorem

The preceding account02/B14 theorem treated arbitrary fragment-center singularities. Such anchors can be chosen adversarially and a two-cycle already develops a logarithmic loss when its two exponents sum to one.

The present theorem exploits additional structure that disappears after arbitrary fragment-label abstraction: the singularities are actual pairwise gaps of three *independent cap-one coordinates*. Their common translation costs one degree of freedom, leaving two relative dimensions; correspondingly the sharp cluster threshold is total exponent two.

This gives a clear design rule for the remaining shell proof:

- if singular centers are arbitrary fragment-dependent functions, retain the earlier acyclic compiler;
- if the local geometry can be rewritten in genuine pair-gap form before localization, leave the active triple unfragmented and use the stronger threshold `sum theta<2` from this report;
- do not replace a structured pair-gap cycle by arbitrary component-dependent anchors prematurely, because that can create a false logarithmic localization debt.

For three square-root pair singularities the structured route is safe by (3.2), while a purely componentwise treatment has no comparable automatic conclusion.

## 8. First remaining implication

Full QFORM remains open. The next B14-relevant implication is now concrete:

> In the remaining heavy/localized three-coordinate branch, derive a deterministic-outside small-ball/coarea inequality of the form (6.1), or prove that the actual quadratic shell singularities cannot be represented with a subcritical pair-gap budget. In particular, test whether sequential completion of squares can retain the active singular factors as genuine shifted pair gaps instead of arbitrary fragment centers.

If such a representation has three square-root factors, the present theorem pays them with the explicit universal factor `61+12pi`. If the raw total pair-gap exponent reaches two, Section 4 gives a genuine cap-one obstruction to this absolute-value compiler, so a different cancellation or aggregation mechanism would be required.

This is the first unpaid connection. No claim of full solution is made.

## 9. Source pins and correction status

- fresh control snapshot before scientific write: `yspennstate/math-research-brain@da8225a364f8b6ff706a10485f1f5ff7f1bf5729`;
- owner programme/control: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`;
- exact assignment: `scheduled_tasks/work/shared/qform-density-2026-09-22/assignments/account02/B14.json`;
- completed partner localization theorem actually applied: `yspennstate/math-open-problems@2208c3f666582999f1fbc7e55921a4530cbe2789`, account03/B14 select-before-localize;
- completed partner obstruction actually applied: `yspennstate/math-open-problems@54f2d04e936d0dfefe345d17ee18a46b35039d7e`, account03/B14 no-fixed-fragment-count theorem;
- preceding account02/B14 acyclic packing theorem: `yspennstate/math-open-problems@d358b89ba78735cee238c01e83c2c3ca9ec66352`.

The live correction inbox was reread immediately before publication. This proof uses no law-uniform pointwise Fourier decay, no post-rotation independence, no fiber-supremum argument, no bounded-diameter/fixed-fragment-count reduction, no conditional-density-cap surrogate for independence, and no phase-Wiener absolute-value interface.

Changed-file allowlist for the canonical mathematics is this report only. Manual content review found only mathematical statements, source pins, run metadata and no credentials/private archives/machine paths. No public release or paid/remote workflow was used.

No novelty or publication-priority claim is made.
