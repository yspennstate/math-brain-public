# QFORM universal assembly: off-diagonal stable-rank cross-cut theorem

Run: `20260922T140323Z-fleet03-B19-QFORM-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Worker: `fleet03/B19` — Universal proof assembly  
Status: `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_BRANCH_PROVED / FULL_CONJECTURE_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository reads/writes are not native learned-memory ingestion.

## 1. Exact target and correction discipline

The target remains: for arbitrary dimension, independent real coordinates with densities `0 <= f_i <= 1`, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal essential density bound for `Q=X^T A X` (and separately determine continuity), or give a valid counterexample.

No moment, support-shape, Gaussian, log-concave, diagonal-basis, or eigen-coordinate independence hypothesis is used below. In particular, this run does **not** use the refuted law-uniform pointwise van-der-Corput claim, fiberwise trace supremum, conditional-density-cap surrogate for independence, a fixed rank-three cross cut, or a fixed well-conditioned principal triple.

## 2. Completed sources actually used

1. **Designated partner fleet04/B19.** `QFORM-FINITE-UNION-CORE-v1`, canonical report `yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T122030Z-fleet04-B19-QFORM-r1/REPORT.md`. It proves that, for every measurable map, interval concentration over arbitrary independent cap-one densities has the same supremum as over product indicators of bounded finite unions of intervals of measure one.

2. **Regularized cross-block determinant theorem.** Canonical report `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, path `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`. For every disjoint original-coordinate cut `I,J`, with `C=A[I,J]`,

   `|phi_Q(t)| <= det(I + 4 t^2 C C^T/(pi^2 e^2))^(-1/8)`.

   This retains arbitrary self blocks, outside couplings, signs, extra spectrum, and arbitrary independent cap-one input laws.

3. **Independent review of source 2.** fleet03/B04, `yspennstate/math-open-problems@55e0a30b6ac56934614a5416056cae2e4a6dc77e`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260922T135303Z-r11/REPORT.md`, gives `INDEPENDENT_SCOPE_PASS` on the determinant theorem's graph Brascamp--Lieb normalization, decoupling orientation, and full-spectrum passage.

4. **Near-diagonal full-matrix branch.** fleet01/B19, canonical report `yspennstate/math-open-problems@072cf685a12893b44d555f14e4e610bcf2154037`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260922T121338Z-b19-qform-r11/REPORT.md`. If `D=diag(A)` and `delta=||A-D||op < 1/2`, then under the target three-large-eigenvalue hypothesis,

   `||p_Q||inf <= pi/sqrt(1-2 delta)`.

The designated partner theorem is applied below to an actual small-ball inequality, not just cited.

## 3. Partner reduction applied to the target concentration inequality

For a fixed symmetric `A` and `h>0`, write

`S_A(h) = sup_{(f_i),t} P_f(t <= X^T A X <= t+h)`,

where the supremum is over all independent densities `0<=f_i<=1`. By fleet04/B19's finite-union core theorem,

`S_A(h) = sup_{E_1,...,E_n,t} | {x in E_1 x ... x E_n : t <= x^T A x <= t+h} |`,

where every `E_i` is a bounded finite union of intervals with `|E_i|=1`.

Therefore any law-independent density estimate proved below for these product indicators immediately gives the **same** interval inequality for all admissible input laws. Concretely, if the product-indicator right side is at most `C h`, then `S_A(h)<=C h`, hence the output law is absolutely continuous with Radon--Nikodym density at most `C` almost everywhere. In the stable-rank branch below we in fact prove the stronger statement `phi_Q in L^1` directly for every admissible law, which also supplies a continuous representative.

## 4. New deterministic cut lemma

Let

`H = A - diag(A)`.

Then `H` is symmetric with zero diagonal. For a coordinate cut `I \sqcup J = {1,...,n}`, put `C=H[I,J]=A[I,J]`. If `I` is chosen by independent fair Bernoulli labels, then

`E ||C||_F^2 = (1/4) ||H||_F^2`.

Indeed,

`||C||_F^2 = sum_{i in I, j in J} H_ij^2`,

and each ordered pair `i!=j` lands in `I x J` with probability `1/4`. Hence some deterministic cut satisfies

`||C||_F^2 >= (1/4)||H||_F^2`.                                            (4.1)

Also compression cannot increase operator norm:

`||C||op <= ||H||op`.                                                        (4.2)

For a nonzero matrix `M`, define stable rank

`sr(M)=||M||_F^2/||M||op^2`.

For a cut satisfying (4.1), (4.2) imply

`sr(C) >= sr(H)/4`.                                                           (4.3)

This step has no sign assumption and no spectral-basis rotation.

## 5. New stable-rank sharpening of the regularized determinant theorem

Let `C` be any nonzero physical cross block and let its singular values be `sigma_j`. Set

`L=||C||op`, `F=||C||F`, `r=sr(C)=F^2/L^2`,

and

`alpha = 4/(pi^2 e^2)`.

The reviewed regularized determinant estimate gives

`|phi_Q(t)| <= prod_j (1 + alpha t^2 sigma_j^2)^(-1/8)`.                     (5.1)

Put `u_j=sigma_j^2/L^2 in [0,1]`, so `sum_j u_j=r`, and `x=alpha L^2 t^2`. Since `u -> log(1+xu)` is concave on `[0,1]`, lies above its endpoint chord, and vanishes at zero,

`log(1+xu) >= u log(1+x)`.

Summing over `j` gives the exact deterministic bound

`det(I+alpha t^2 C C^T) >= (1+alpha L^2 t^2)^r`,

hence

`|phi_Q(t)| <= (1+alpha L^2 t^2)^(-r/8)`.                                    (5.2)

Assume now `r>=8` and put `p=r/8>=1`. For

`J_p = integral_R (1+s^2)^(-p) ds`,

split at `|s|=1`. On `|s|<=1`, `log(1+s^2)>=s^2/2`, while on `|s|>=1`, `(1+s^2)^(-p)<=|s|^(-2p)`. Therefore

`J_p <= sqrt(2 pi/p) + 2/(2p-1)`

`     <= (sqrt(2 pi)+2)/sqrt(p)`.                                            (5.3)

Using `s=sqrt(alpha)Lt` and `L sqrt(p)=F/sqrt(8)`, (5.2)--(5.3) give

`integral_R |phi_Q(t)| dt`

` <= sqrt(8)(sqrt(2 pi)+2)/(sqrt(alpha) F)`.                                 (5.4)

Thus **cross-block stable rank at least eight pays the time integral through Frobenius mass, without selecting or paying a reciprocal individual minor**. Fourier inversion gives a bounded continuous density vanishing at infinity and

`||p_Q||inf <= [sqrt(8)(sqrt(2 pi)+2)]/[2 pi sqrt(alpha) F]`.                (5.5)

This is the first new supporting theorem of this run.

## 6. Target-level off-diagonal stable-rank branch

Assume now the full target hypotheses on `A`: at least three eigenvalues have modulus at least one. Put

`delta=||H||op`, `H=A-diag(A)`.

There are two solved cases.

### Case A: `delta <= 1/4`

Apply the completed near-diagonal theorem. Since `delta<1/2`,

`||p_Q||inf <= pi/sqrt(1-2delta) <= pi sqrt(2)`.                              (6.1)

This establishes an essentially bounded density. The cited localized branch does not by itself promote continuity for arbitrary rough input densities, so continuity is **not claimed here** solely from (6.1).

### Case B: `delta > 1/4` and `sr(H) >= 32`

Choose the cut from Section 4. Then

`sr(C)>=8`,

and

`F=||C||F >= ||H||F/2 >= ||H||op/2 > 1/8`.                                  (6.2)

Insert (6.2) into (5.5). Since `sqrt(alpha)=2/(pi e)`,

`||p_Q||inf`

` < 2 e sqrt(8)(sqrt(2 pi)+2)`

` = 69.2980809828627... < 70`.                                               (6.3)

Moreover `phi_Q in L^1`, so this branch has a **bounded continuous density** (indeed the Fourier inverse vanishes at infinity).

Notice that Case B does not need the three-large-eigenvalue hypothesis at all; that hypothesis is needed only to guarantee Case A via the near-diagonal theorem.

### Corollary: exact residual for any counterexample

Any counterexample to the full conjecture must simultaneously satisfy

`||A-diag(A)||op > 1/4`                                                       (6.4)

and

`sr(A-diag(A)) < 32`.                                                        (6.5)

By the partner reduction, a counterexample can additionally be witnessed at the level of interval concentration by product indicators of bounded finite unions of intervals of measure one.

This is an exhaustive target-level reduction, not a solution of the remaining branch.

## 7. Compact conditional end-to-end assembly after this run

A full proof can now be organized without any retired mechanism as follows.

- Arbitrary admissible laws reduce exactly, for interval concentration, to the partner's finite-union product core.
- If the physical off-diagonal part has norm at most `1/4`, the near-diagonal theorem gives `pi sqrt(2)`.
- If that norm is larger but its stable rank is at least `32`, the new random-cut + reviewed determinant argument gives a continuous density `<70`.
- Independently, the reviewed full-range diffuse theorem applies whenever the entire range projection has sufficiently small physical leverage (fleet03/B04 sharpens the reviewed threshold beyond the original `1/32`).
- Rank-exactly-three definite forms and several localized indefinite branches are already closed by the existing B08/B19/B10 chain; these are compatible supporting branches but are not needed for Sections 4--6.

The remaining full-matrix state is therefore no longer an arbitrary high-dimensional cross-cancellation problem. It is concentrated in a low-effective-rank physical off-diagonal interaction.

## 8. First unpaid implication after the new theorem

`QFORM-LOW-STABLERANK-OFFDIAGONAL-BRIDGE-v1`:

> Let `A` satisfy the exact target hypotheses and put `H=A-diag(A)`. In the residual state
> 
> `||H||op > 1/4`, `sr(H)<32`,
> 
> prove a dimension-free small-ball/density bound by aggregating original-coordinate banks before any reciprocal minor is paid.

Any valid proof must include the known star-plus-square / high-cardinality examples where every physical rank-three cross cut or well-conditioned principal triple can fail. It also may not condition on a projected leakage variable and replace true independence by a conditional density cap; that route is explicitly refuted in the correction inbox.

The natural next mechanism is finite-bank low-stable-rank decomposition: exploit that all large off-diagonal Frobenius energy lives in fewer than 32 operator-norm units, while the diagonal is a separable quadratic phase. The goal is to turn this into a bounded number of product-preserving banks feeding either (i) a hyperbolic-square channel, (ii) a same-sign physical elliptic pair, or (iii) a reviewed regularized-determinant block, without selecting a single tiny coordinate minor.

## 9. What is and is not proved

**Proved here:** the cross-block stable-rank Fourier lemma (5.4)--(5.5), the random-cut stable-rank extraction (4.1)--(4.3), and the target-level dichotomy (6.1)--(6.5), including a `<70` continuous-density bound in the high-stable-rank off-diagonal branch.

**Applied partner result:** fleet04/B19 finite-union core is used explicitly to transfer the interval inequality from finite-union product indicators to all admissible densities with no loss.

**Not proved:** the residual low-stable-rank off-diagonal branch; therefore the full conjecture remains `OPEN / NOT PROVED`. A continuous density is proved in Case B, while Case A is recorded only as the essential bounded-density conclusion supplied by its cited source. No universal `C=pi` claim is made.

## 10. Regression computation

A small deterministic checker in this run directory verifies the displayed numerical constant and stress-tests the stable-rank chord inequality on random finite singular spectra. It is a regression aid only; the proof is the analytic argument above.
