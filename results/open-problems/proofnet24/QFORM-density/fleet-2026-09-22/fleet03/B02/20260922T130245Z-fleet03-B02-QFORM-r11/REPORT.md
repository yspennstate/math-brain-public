# fleet03/B02 — integrated Fourier / coupled 2+1 and aggregate-star update

Run: `20260922T130245Z-fleet03-B02-QFORM-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## Full target and corrections respected

The target remains: for every dimension, every independent real input with coordinate densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential density bound for `Q=X^TAX`, or give a valid counterexample. Continuity is a separate stronger conclusion.

This report does **not** use law-uniform pointwise quadratic-phase decay, post-rotation independence, a fixed well-conditioned coordinate minor, or a universal single Schur-pivot extraction. The last mechanism is now explicitly refuted by the live correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`.

The exact assigned partner `fleet04/B02` still had no completed current-programme handoff at the fresh pre-work check. Compatible completed peer results actually applied below are fleet02/B02 (physical cross-block Plancherel) and fleet02/B10 (hyperbolic-square smoothing), with fleet01/B19's hard star family used as the stress case.

---

## Result A: remove the previous run's zero-coupling hypothesis

### Theorem `QFORM-SCHUR-2PLUS1-POTENTIAL-v1`

Fix five distinct original coordinates, split as two-coordinate sets `I,J` and a pivot coordinate `k`. Condition on every other original coordinate. Write the resulting quadratic-affine form in variables `x in R^2`, `y in R^2`, `z in R` as

`q(x,y,z)=q_I(x)+q_J(y)+2 x^T B y + d z^2 + 2 z(a^T x+b^T y+c)`,

where the two within-side quadratic-affine functions are arbitrary and `d != 0`. Define the Schur cross block

`C = B - a b^T/d`,  `Delta = |det C|`.

If `Delta>0`, then for arbitrary independent coordinate densities bounded by one,

`||p_q||_infinity <= 4^(7/4) 3^(-1/4) |d|^(-1/2) Delta^(-1/4)`.

Numerically the universal prefactor is about `8.59656`. The estimate is uniform in all conditioned outside coordinates, so the same bound holds before conditioning. It proves essential boundedness on this branch; continuity is not claimed here.

### Proof, step 1: exact completion of the coupled pivot

Complete the square in the original physical pivot:

`q = d [z+(a^T x+b^T y+c)/d]^2 + R(x,y)`,

where the cross block of the residual `R` between the two physical pairs is exactly `C=B-ab^T/d`. Thus arbitrary couplings of the pivot to both pairs are absorbed without creating any post-rotation independence assumption.

### Proof, step 2: rank-two cross Plancherel gives an L^3 residual density

Let `eta(t)=E exp(i t R)`, conditional on the outside coordinates. Put all within-`I` phases into a two-dimensional amplitude `F_t(x)` and all within-`J` phases into `G_t(y)`. Since each physical coordinate density is at most one,

`||F_t||_2 <=1`, `||G_t||_2<=1`.

With the unnormalised Fourier convention `Fhat(xi)=int exp(i xi.x)F(x)dx`,

`eta(t)=int G_t(y) Fhat_t(2t C y) dy`.

Cauchy-Schwarz, the change of variables `xi=2tCy`, and Plancherel give

`|eta(t)| <= pi/(|t| sqrt(Delta))`.

Together with `|eta(t)|<=1`,

`int_R |eta(t)|^(3/2) dt <= 6 pi Delta^(-1/2)`.

Inverse Hausdorff-Young therefore supplies a density `h` for `R` satisfying

`||h||_3 <= (2pi)^(-2/3) [6pi Delta^(-1/2)]^(2/3) = 3^(2/3) Delta^(-1/3)`.

This is the exact two-physical-pair endpoint of the fleet02/B02 cross-block Plancherel mechanism.

### Proof, step 3: a one-dimensional square potential closes L^infinity

Conditional on `(x,y)`, the shifted physical coordinate `z+(a^Tx+b^Ty+c)/d` still has a density bounded by one. Hence the conditional density of its `d times square` is bounded by

`|d|^(-1/2) |v|^(-1/2)`

on the appropriate half-line. Consequently, for every real `s`,

`p_q(s) <= |d|^(-1/2) int h(r) |s-r|^(-1/2) dr`.

Write `H=||h||_3`. For any `rho>0`, split the potential into `|s-r|<=rho` and its complement. Holder on the near part and probability mass one on the far part give

`int h(r)|s-r|^(-1/2)dr <= 4 H rho^(1/6) + rho^(-1/2)`.

The optimum satisfies `rho^(2/3)=3/(4H)`, yielding

`<= 4^(7/4) 3^(-3/4) H^(3/4)`.

Substituting `H<=3^(2/3)Delta^(-1/3)` proves

`||p_q||_infinity <= 4^(7/4)3^(-1/4)|d|^(-1/2)Delta^(-1/4)`.

This removes the exact decoupling condition `A_{k,I union J}=0` from the preceding B02 result. It is also a slightly smaller physical-pair constant than the previously reported `4 sqrt(6)` Schur-pivot bound, but it does **not** imply a universal pivot exists.

---

## Result B: change mechanism on the newly exposed low-cross-rank branch

The live correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` shows that the spectral hypothesis does not force Result A to apply. The hard family from fleet01/B19 has spectrum `{1,-1,1}` but every available scalar Schur pivot leaves only a rank-one star. Therefore this run changes mechanism from local reciprocal minors to high-cardinality aggregation.

### Theorem `QFORM-AGGREGATED-HYPERBOLIC-SQUARE-v1`

Let `X` be independent of two disjoint product-coordinate groups. Form linear aggregates

`U=sum_i alpha_i Y_i`, `V=sum_j beta_j Z_j`,

where all underlying coordinates are independent and have densities bounded by one, and `alpha,beta` are nonzero coefficient vectors. Let `a,b` be nonzero real numbers and let `H,theta` be arbitrary measurable real functions for which the displayed random variable is finite almost surely. Then

`T = 2 a X U + H(U) + b [V+theta(U)]^2`

has an essentially bounded density and

`||p_T||_infinity <= 2^(11/4) / ( sqrt(|a b|) ||alpha||_2^(1/2) ||beta||_2 )`.

### Proof

Rudelson--Vershynin, *Small ball probabilities for linear images of high-dimensional distributions*, Theorem 1.2, gives the sharp one-dimensional projection estimate

`||p_U||_infinity <= sqrt(2)/||alpha||_2`,
`||p_V||_infinity <= sqrt(2)/||beta||_2`.

For completeness, the source theorem states that if independent coordinates have densities bounded by `K` and the coefficient vector has Euclidean norm one, then the density of their linear combination is bounded by `sqrt(2) K`; it follows from Rogozin's comparison theorem and Ball's cube-slicing theorem.

Now use the completed fleet02/B10 hyperbolic-square theorem, whose physical-space proof was independently rechecked in this run: if independent `X,Y,Z` have density caps one, then

`2 a X Y + H(Y) + b[Z+theta(Y)]^2`

has density at most `4/sqrt(|ab|)`. More generally, if the density caps are `K_X,K_Y,K_Z`, scaling gives

`||p||_infinity <= 4 K_Z sqrt(K_X K_Y)/sqrt(|ab|)`.

Here `K_X=1`, `K_U=sqrt(2)/||alpha||_2`, and `K_V=sqrt(2)/||beta||_2`. Substitution gives exactly the displayed constant `2^(11/4)`.

### Target-level star corollary

For the rank-three star-plus-square matrix

`Q = 2 X_0 (alpha.Y) + (beta.Z)^2`

on disjoint physical coordinate groups, the three nonzero eigenvalues are

`+||alpha||_2`, `-||alpha||_2`, `||beta||_2^2`.

Thus, whenever this matrix itself satisfies the target spectral threshold, `||alpha||_2>=1` and `||beta||_2>=1`, so

`||p_Q||_infinity <= 2^(11/4) < 6.728`.

This closes the entire arbitrary-coefficient star-plus-square family, not merely the equal-weight stress example. For the exact `A_m` family used to refute single-pivot extraction, it sharpens the previously archived `<19.1` bound to `<6.728` by using the sharp one-dimensional projection constant instead of the weaker aggregate cap used in that handoff.

The result is a genuine target-level branch and directly applies a completed peer theorem to the live low-cross-rank obstruction. It is not a proof that every remaining rank-three matrix reduces to this form.

---

## What this pays and what remains unpaid

Paid this run:

1. The prior B02 unpaid implication "survive nonzero coupling of the third pivot" is paid on the full physical `2+1` Schur branch: arbitrary pivot-to-pair couplings are allowed.
2. The new live falsifier against universal single-pivot extraction is applied, not ignored.
3. The exact hard star family is handled by a product-preserving aggregation theorem with a substantially improved constant.

First unpaid universal implication now:

`QFORM-SCHUR-OR-AGGREGATE-STRUCTURE-v1`: starting only from the hypothesis that `A` has at least three eigenvalues of modulus at least one, prove a dimension-free structural/analytic dichotomy that yields either

- a physical pivot plus two disjoint physical pairs with `|d|^(2) Delta` bounded below strongly enough for Result A, **or**
- a low-cross-rank product-preserving aggregate channel controlled by Result B (or the already proved diffuse/separable-phase theorem),

without paying the reciprocal of one tiny coordinate minor.

The current counterexample evidence rules out the naive statement that the first alternative must always occur. Extra nonseparable residual eigen-directions remain an additional full-target debt after exact-rank-three closure.

## Status discipline

`FULL_TARGET_OPEN`. Result A proves essential boundedness on a coupled Schur `2+1` branch. Result B proves essential boundedness on a high-cardinality star-plus-square branch. Neither proves the universal structural dichotomy. No continuity claim is made for these two new branches, although other existing Fourier branches do yield continuous representatives when their characteristic functions are integrable.

## Sources consumed

- fleet02/B02, `B02-20260922T120900Z-qform-r11`, canonical math-open-problems commit `400f82c8b98fc5623f567581b6ccb0b4298974e8`.
- fleet02/B10, `20260922T1147Z-qform-rank3-coupled-B10-r1`, canonical math-open-problems commit `1eba911614ef9f6683f8eacb5d6608a0f9a4b833`.
- fleet01/B19, `20260922T121338Z-b19-qform-r11`, canonical math-open-problems commit `072cf685a12893b44d555f14e4e610bcf2154037`.
- live correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, canonical falsifier commit `17dec75dc10459933f8bfde30daa86d1c6d90a6a`.
- Mark Rudelson and Roman Vershynin, *Small ball probabilities for linear images of high-dimensional distributions*, IMRN 2015, Theorem 1.2, DOI `10.1093/imrn/rnu243`, arXiv `1402.4492`.

No paid remote computation, no model/API call, and no native-memory-ingestion claim was used.
