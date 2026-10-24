# account03/B15 — deletion-stable continuity for rough product inputs

**Run:** `20260922T130923Z-account03-B15-qform-r11b`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
**Assignment:** Absolute continuity and regularity  
**Classification:** `ESSENTIAL_STEP_APPLIED / CONTINUITY-REDUCTION / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and separation of obligations

The live target is: for every `n`, every independent real `X_i` with measurable densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues satisfying `|lambda_j(A)|>=1`, prove a universal finite `C` such that the law of

`Q=X^T A X`

has a density `p_Q` with `||p_Q||_infinity<=C`. The owner's stronger request that the density have a continuous representative is tracked separately. No continuity, compact support, moment, log-concavity, or eigenbasis-independence assumption is added to the inputs.

The central universal `L^infinity` theorem remains open. The preceding account03/B15 run reduced that central theorem exactly to interval small-ball bounds on product-indicator finite-fragment laws. This run attacks the separate continuity obligation by a different mechanism.

Current corrections are retained: no law-uniform pointwise quadratic Fourier decay is assumed; rotated eigen-coordinates are not treated as independent; no fiber-supremum or single-cross-minor argument is used.

## 2. Completed partner mathematics consumed

The named compatible assignment partner result is account04/B15:

`yspennstate/math-open-problems@1d658cd8ef6386a8f8ef7e6b9aaf26fdafe68de3`.

It separates interval domination from continuity and applies the fixed-instance principal-block theorem. The underlying source-valid local estimates are account01/B15 at

`yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553`

and account02/B15 at

`yspennstate/math-open-problems@d5392d73398e2811f58b612fb8f191aa79d8ee5e`.

I also apply the completed account03/B14 definite-pair theorem at

`yspennstate/math-open-problems@e6a82375d007069e7e515cb682eaf430d8baa914`.

The exact local inputs used here are:

* every symmetric matrix of rank at least three has an invertible principal block of order three or four;
* conditioning on all other original coordinates, an invertible `3x3` block `B` gives an output-density bound `(2*pi+3*sqrt(3))/sigma_min(B)`, uniformly in all induced affine linear terms;
* an invertible `4x4` block gives `(4*pi+8)/sigma_min(B)`, again uniformly in all induced affine terms;
* a physical `2x2` principal block `B` with `det(B)>0` is definite and gives a conditional density bound `pi/sqrt(det B)`, uniformly in all outside couplings and induced affine terms.

No universal lower bound on any selected minor is asserted.

## 3. One-coordinate `L1 -> output-Linfinity` stability

### Lemma 3.1 — `QFORM-ROUGH-MARGINAL-STABILITY-v1`

Fix a real symmetric `A` and a physical coordinate `i`. Suppose there is a principal index set `J subset {1,...,n}\{i}` satisfying either

1. `|J| in {3,4}` and `B=A_{J,J}` is invertible, or
2. `|J|=2` and `det(B)>0`.

Define

`K(B)=(4*pi+8)/sigma_min(B)` in case 1,

and

`K(B)=pi/sqrt(det B)` in case 2.

Let two admissible product laws have identical marginals except at coordinate `i`, where the densities are `f_i` and `g_i`. Then their quadratic-form output measures have densities `p_f,p_g` satisfying

`||p_f-p_g||_infinity <= K(B) ||f_i-g_i||_1`.

### Proof

Condition on every coordinate outside `J`, including coordinate `i`. For each fixed outside vector `w`, the conditional polynomial in the original independent coordinates `X_J` is

`X_J^T B X_J + 2 b(w)^T X_J + c(w)`.

By the completed local theorem corresponding to the chosen block, its conditional output law `nu_w` obeys

`nu_w(E) <= K(B) |E|`

for every Borel `E`, uniformly in `w`; all outside couplings are absorbed into `b(w),c(w)`.

Let `h=f_i-g_i`. The signed difference `sigma` of the two unconditional output laws therefore satisfies

`|sigma(E)| <= integral |h(x_i)| [product of the other outside densities] nu_w(E) dw`

`<= K(B) ||h||_1 |E|`.

Hence the total-variation measure `|sigma|` is dominated by `K(B)||h||_1 dx`. Its Radon-Nikodym derivative is `p_f-p_g`, proving the claimed essential-supremum bound. QED.

This is the key regularity input: roughness of one marginal can be changed in `L1` without losing uniform control whenever a bounded-density smoothing block survives on physical coordinates disjoint from that marginal.

## 4. Smooth product inputs give `C_0` output densities

### Lemma 4.1 — smooth-input regularity

Let `A` have rank `r>=3`. If all input densities are `C_c^infinity`, then `X^TAX` has a density in `C_0(R)`.

### Proof

The joint density `F(x)=product_i f_i(x_i)` is `C_c^infinity`. Orthogonally diagonalize the quadratic form and integrate the transformed smooth compact amplitude along the null directions. This gives an amplitude `a in C_c^infinity(R^r)` and a nonsingular symmetric `r x r` matrix `Lambda` such that

`phi(t)=E exp(i t X^TAX)=integral exp(i t y^T Lambda y) a(y) dy`.

For a nondegenerate quadratic phase, quadratic stationary phase gives, for `|t|>=1`,

`|phi(t)| <= C(a,Lambda) |t|^{-r/2}`.

This is the standard nondegenerate quadratic estimate: after orthogonal diagonalization, a partition near the unique critical point plus integration by parts away from it gives the bound, while the near-critical scaling `y=|t|^{-1/2}z` supplies exactly `|t|^{-r/2}`. Since `r>=3`, the right side is integrable at infinity, while `|phi(t)|<=1` near zero. Thus `phi in L1(R)`. Fourier inversion produces a bounded continuous density, and the Riemann-Lebesgue theorem gives vanishing at infinity. QED.

This use of Fourier decay is only for each fixed smooth compact amplitude. It is not the refuted law-uniform pointwise decay claim.

## 5. Main theorem: continuity under a disjoint smoothing block for every marginal

### Theorem 5.1 — `QFORM-DISJOINT-SMOOTHING-CONTINUITY-v1`

Let `A` be real symmetric of rank at least three. Assume that for every physical coordinate `i`, the deletion `A_{-i,-i}` satisfies at least one of:

* `rank(A_{-i,-i})>=3`; or
* `A_{-i,-i}` contains a `2x2` principal block of positive determinant.

Let `X_1,...,X_n` be independent with arbitrary measurable probability densities `0<=f_i<=1`. Then `Q=X^TAX` has a density with a representative

`p_Q in C_0(R)`.

In particular `p_Q` is bounded and uniformly continuous. No continuity of any input density is assumed.

More quantitatively, choose for every `i` a disjoint block `J_i` supplied by the hypothesis and define its finite constant `K_i` as in Lemma 3.1. Then for any two admissible product laws `f=(f_1,...,f_n)` and `g=(g_1,...,g_n)`,

`||p_f-p_g||_infinity <= sum_i K_i ||f_i-g_i||_1`.

### Proof

If `rank(A_{-i,-i})>=3`, the principal-block lemma applied to that deletion supplies an invertible `3x3` or `4x4` block disjoint from `i`. In the second branch the required definite pair is already given. Lemma 3.1 and a coordinate-by-coordinate telescope prove the quantitative estimate.

It remains to remove all regularity from the inputs. For each measurable admissible density `f_i`, construct `f_i^(m) in C_c^infinity` with

`0<=f_i^(m)<=1`, `integral f_i^(m)=1`, and `||f_i^(m)-f_i||_1 ->0`.

An explicit construction is available. Truncate `f_i` to a large compact interval, losing mass `delta`; add the indicator of a disjoint bounded interval of length `delta`, restoring total mass while keeping the pointwise cap one; then convolve with a nonnegative compactly supported smooth probability mollifier. Convolution preserves total mass and the `L^infinity` cap, and the truncation and mollifier scales can be chosen so that the `L1` error tends to zero.

Let `p_m` denote the output density for the product of the `f_i^(m)`. Lemma 4.1 gives `p_m in C_0(R)`. The telescoping estimate gives

`||p_m-p_l||_infinity <= sum_i K_i ||f_i^(m)-f_i^(l)||_1 ->0`.

Because `p_m-p_l` is continuous, its essential supremum equals its ordinary supremum. Hence `{p_m}` is Cauchy in the uniform norm and converges uniformly to some `p in C_0(R)`.

At the same time the product input measures converge in total variation to the original product law, so their pushforwards under `x -> x^T A x` converge in total variation to the true output law. Therefore that output law is exactly `p(x) dx`. Thus `p=p_Q` is a `C_0` representative. QED.

The earlier deletion-stable criterion `rank(A_{-i,-i})>=3 for all i` is an immediate special case.

## 6. Consequences and exact remaining low-rank regularity branch

### Corollary 6.1 — every rank at least five instance has a continuous density

If `rank(A)>=5`, then Theorem 5.1 applies to every admissible product input. Indeed, deleting one row and one column decreases rank by at most two:

`rank(A_{-i,-i}) >= rank(A)-2 >=3`.

Therefore every target instance of rank at least five already has a bounded uniformly continuous `C_0` density under merely measurable coordinate densities bounded by one.

This includes arbitrary dimensions, signs, repeated eigenvalues, rotations, cross-couplings, and arbitrary extra small eigenvalues. It does not supply a dimension-free or matrix-free numerical bound.

The theorem also covers a low-rank deletion whenever the residual rank-two form is definite: a rank-two positive- or negative-semidefinite matrix has some nonzero `2x2` principal determinant, necessarily positive, so the definite-pair branch applies.

Consequently, a coordinate can remain genuinely exceptional for this continuity mechanism only when

`rank(A_{-i,-i})<=1`,

or when `A_{-i,-i}` has rank two and inertia `(1,1)`.

That is, the surviving deletion is at most one-dimensional or genuinely hyperbolic. This is much narrower than arbitrary rank-three/rank-four rotation.

For exact rank three, write `A=U Lambda U^T` with `U` having three orthonormal columns. Then `rank(A_{-i,-i})<3` can occur only if deleting row `i` lowers the rank of `U`, equivalently if the leverage `||u_i||^2` equals one, i.e. the physical coordinate vector `e_i` lies entirely in `Range(A)`. Thus the rank-three continuity debt is confined to a rigid leverage-one/physical-axis branch; among those, definite rank-two deletions are already closed above, leaving only the hyperbolic/rank-at-most-one residual cases.

## 7. What is proved and what remains unpaid

**PROVED here:**

1. a quantitative one-marginal `L1 -> output-Linfinity` stability theorem whenever a disjoint invertible `3x3`/`4x4` block or definite `2x2` block exists;
2. a full continuous-representative theorem under that disjoint-smoothing condition for arbitrary measurable independent coordinate densities bounded by one;
3. in particular, a `C_0` density for every target instance with matrix rank at least five;
4. a reduction of the remaining continuity problem to rank-three/rank-four configurations having a physical coordinate whose deletion is rank at most one or hyperbolic rank two; in exact rank three such a coordinate must have leverage one.

**NOT proved here:**

* a universal numerical `L^infinity` constant independent of `A,n`;
* the continuous-representative conclusion for the exceptional low-rank hyperbolic/rank-at-most-one deletion branch;
* the full QFORM conjecture.

The two obligations remain intentionally separate.

**Central essential-boundedness obligation:** prove a dimension-free interval small-ball estimate on the finite-fragment extreme product class from the preceding account03/B15 reduction. The current fixed-instance smoothing constants can diverge along flat rank-three frames and do not solve this.

**Continuity obligation after this run:** classify and control the remaining leverage-one rank-three/rank-four cases whose deletion is hyperbolic rank two or rank at most one. The next mechanism should exploit the actual bilinear coupling/one-dimensional square smoothing in those low-rank normal forms rather than repeat generic approximation.

Primary handoff recipient: `account04/B15` (regularity partner). Secondary useful recipients: rank-three coupled/synthesis workers (`B10`, `B19`).

Full universal QFORM remains **OPEN**. No novelty or publication-priority claim is made.
