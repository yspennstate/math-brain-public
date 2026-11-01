# fleet02/B05 — coarea Riesz-potential closure for a localized rank-three block

**Run:** `20260922T115002Z-b05-qform-9c3a2d7e`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
**Assignment:** B05, quadratic coarea bound / equivalent interval bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_BLOCK_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh target and peer input

The later owner control suspends FEI and all previous targets. The active target is the universal bounded-density conjecture for `Q=X^TAX` with independent input densities bounded by one and at least three eigenvalues of `A` of absolute value at least one.

This run directly applies two current other-worker results.

1. **Named partner fleet03/B05**, run `20260922T113800Z-fleet03-B05-qform-r11`, canonical report commit `c828d2ee2f8acef5eb96892bc8a9a25594db0f51`. It proves a delocalized spectral-subspace theorem: if the active spectral projection `P` has `max_j ||Pe_j||_2 <= 1/2`, then a Rudelson--Vershynin / Fresnel argument gives a universal continuous-density bound (in the rank-`r` setting described there). Thus the high-coherence localized regime is a genuine complementary geometry problem, rather than a reason to repeat the delocalized Fourier estimate.

2. **fleet03/B01**, run `20260922T113140Z-fleet03-B01-qform-r1`, canonical report commit `c7a1ce265139092705e86c5a577523798291b964`. For independent `U,V` with densities bounded by one, the product `UV` has a common pointwise envelope
   `H(w)=4 log(1+1/(2 sqrt(|w|)))`,
   with `||H||_3 < 6.266`. Hence the density of `2 kappa UV` has `L^3` norm at most
   `(2|kappa|)^(-2/3) ||H||_3`.

The previous fleet02/B05 run had already shown that taking a fiberwise supremum over a spectral plane can lose `Theta(n)`. The present run therefore keeps a product-distributed two-coordinate residual and only uses coarea in the remaining coordinate.

## 2. Coarea-to-Riesz transfer

### Lemma 2.1 (`QFORM-COAREA-RIESZ-v1`)

Let `X` be independent of a random element `Y`, with density `f_X <= 1`. Suppose, after conditioning on all other variables and removing affine terms by coordinatewise translations, a quadratic expression has the form

`Q = a (X + m(Y))^2 + R(Y)`,  `a != 0`.

If `R(Y)` has a density `p_R`, then for almost every `t`,

`p_Q(t) <= |a|^(-1/2) int_R |t-s|^(-1/2) p_R(s) ds`.

**Proof.** For fixed `Y=y`, the conditional density of `a(X+m(y))^2` is at most
`|a|^(-1/2)|u|^(-1/2)` on its allowed half-line. Translating by `R(y)` and averaging in `y` gives the displayed bound. No independence between `X+m(Y)` and `R(Y)` is used.

### Lemma 2.2 (an `L^p` Riesz-potential bound)

If `p>2`, `g` is a probability density in `L^p(R)`, and `M=||g||_p`, then

`sup_t int |t-s|^(-1/2) g(s) ds <= 2 (C_p M)^(p/(2(p-1)))`,

where `p'=p/(p-1)` and
`C_p = [2/(1-p'/2)]^(1/p')`.

For `p=3`, `C_3=4`, hence

`sup_t int |t-s|^(-1/2) g(s) ds <= 2^(5/2) ||g||_3^(3/4)`.

**Proof.** Split at radius `rho`. On `|t-s|<=rho`, Hölder gives
`C_p M rho^(1/2-1/p)`. On the complement use total mass one to get `rho^(-1/2)`. Choose `rho=(C_pM)^(-p')`, making the two terms equal.

This is the precise coarea mechanism missing from the naive fiber-supremum route: one does not maximize the full product density on each fiber; one pays a square-root singularity in one coordinate and asks the residual two-coordinate law for an averaged `L^p`, `p>2`, bound.

## 3. A new localized three-coordinate block theorem

Let a symmetric selected principal block be

`B = [[a, d, e], [d, b, f], [e, f, c]]`,  with `a != 0`,

and assume its two principal minors adjacent to the first coordinate vanish:

`a b - d^2 = 0`,  `a c - e^2 = 0`.

Write

`r=d/a`,  `s=e/a`,  `kappa=f-de/a`.

Then `b=a r^2`, `c=a s^2`, and exactly

`x^T B x = a (x + r y + s z)^2 + 2 kappa y z`,
`det B = -a kappa^2`.

The block is invertible iff `kappa != 0`.

### Theorem 3.1 (`QFORM-ZERO-SCHUR-DIAGONAL-COAREA-v1`)

For arbitrary independent selected-coordinate inputs with densities bounded by one, arbitrary dimension, and arbitrary couplings from the selected coordinates to all outside coordinates, the full quadratic form has a density satisfying

`||p_Q||_infinity <= 4 ||H||_3^(3/4) / sqrt(|a kappa|)`

for every selected block of the above form.

Using `||H||_3<6.266`,

`||p_Q||_infinity < 15.842 / sqrt(|a kappa|)`.

**Proof.** Condition on all outside variables. Since `B` is invertible, the resulting affine perturbation in `(x,y,z)` is removed by a coordinatewise translation depending on the conditioned variables; the three selected inputs remain independent translated densities bounded by one. The homogeneous block then has the displayed square-plus-product decomposition.

Apply Lemma 2.1 in the first coordinate. The residual law is `R=2 kappa YZ`. By the fleet03/B01 product-envelope theorem,

`||p_R||_3 <= (2|kappa|)^(-2/3) ||H||_3`.

Lemma 2.2 with `p=3` yields

`sup_t I_{1/2}p_R(t)
 <= 2^(5/2) [(2|kappa|)^(-2/3)||H||_3]^(3/4)
 = 4 ||H||_3^(3/4) |kappa|^(-1/2)`.

Multiplying by `|a|^(-1/2)` proves the theorem. Mixing the uniform conditional density bound over the outside variables preserves the same cap.

This theorem is genuinely outside the fleet03/B01 zero-diagonal-pair block: here all three original diagonal entries may be nonzero. The zero diagonals appear only in the **Schur residual after coarea in one original coordinate**, so the square variable is not independent of the residual product. Lemma 2.1 is what permits that dependence.

## 4. Spectral closure of this family

Assume additionally that every eigenvalue of the selected `3x3` block `B` has absolute value at least one. Then `||B^{-1}||_op <= 1`.

For the parametrization above, direct algebra gives

`B^{-1} =
 [[1/a + 2rs/kappa, -s/kappa, -r/kappa],
  [-s/kappa, 0, 1/kappa],
  [-r/kappa, 1/kappa, 0]]`.

Every entry of `B^{-1}` therefore has absolute value at most one. Hence

`|kappa| >= 1`,
`|r| <= |kappa|`,
`|s| <= |kappa|`,

and from the `(1,1)` entry,

`1/|a| <= 1 + 2|rs|/|kappa| <= 1 + 2|kappa|`.

Consequently

`|a kappa| >= |kappa|/(1+2|kappa|) >= 1/3`.

Thus the whole special family satisfies the universal numerical bound

`||p_Q||_infinity < 15.842 sqrt(3) < 27.44`.

This is a target-level rank-three principal-block subclass with arbitrary bounded input densities and arbitrary outside couplings.

## 5. Decisive falsifier to a stronger principal-minor shortcut

The matrix

`M = [[1,1,1],[1,1,-1],[1,-1,1]]`

has characteristic polynomial

`(lambda-2)^2(lambda+1)`,

so its eigenvalues are `2,2,-1`. All three satisfy the target spectral threshold. Yet **every `2x2` principal minor equals zero**. Therefore the stronger shortcut

> three eigenvalues of magnitude at least one force a nondegenerate, let alone definite, original-coordinate `2x2` principal block

is false even in dimension three.

The new theorem nevertheless handles this exact matrix. Its quadratic form is

`x^T M x = (x+y+z)^2 - 4yz`.

Here `a=1` and `kappa=-2`, so

`||p_{X^TMX}||_infinity < 15.842/sqrt(2) < 11.21`

for arbitrary independent one-dimensional input densities bounded by one.

This example is maximally localized (`P=I` in dimension three), so the named partner's delocalized condition `max_j||Pe_j||<=1/2` does not apply. The two results are complementary rather than overlapping.

## 6. Conditional end-to-end argument and first unpaid implication

A viable conditional route now has two rigorously closed ends.

- **Delocalized spectral support:** use the named partner fleet03/B05 theorem.
- **A localized selected block with two vanishing adjacent principal minors:** use Theorem 3.1 above; if its three block eigenvalues satisfy the target threshold, the constant is universal.

The first essential missing implication is the **generic localized Schur-residual bound**. After pivoting on a nonzero diagonal coefficient,

`Q = a (X + rY+sZ)^2 + [beta Y^2 + 2 gamma YZ + delta Z^2]`.

Coarea reduces the problem to a uniform bound on the half-Riesz potential of the binary residual law while retaining the inverse-matrix constraints inherited from `||B^{-1}||_op<=1`. The exact-product residual `beta=delta=0` is now closed. What remains is to prove a dimension-free estimate for nonzero `beta,delta`, or construct a product-density counterexample to such an estimate. A bound that merely uses a joint-density supremum is invalid because it again discards product geometry.

This is narrower than the previous B05 residual: the `Theta(n)` spectral-plane fiber loss is avoided entirely in this local mechanism, and a fully rotated three-large-eigenvalue matrix with all principal pair determinants zero is no longer an obstruction.

## 7. Exact checker

The accompanying exact symbolic checker verifies

- `det B = -a kappa^2`;
- the displayed inverse identity;
- all three `2x2` principal minors of `M` vanish;
- `charpoly(M)=(lambda-2)^2(lambda+1)`;
- the numerical constants quoted above.

The checker is diagnostic only; all mathematical implications used above are proved symbolically in the text.

## 8. Status

`ESSENTIAL_STEP_APPLIED`.

The full arbitrary-dimension conjecture remains open. The named partner's spectral-truncation issue, generic localized Schur residuals, and the passage from three global large eigenvalues to a universally controllable original-coordinate local structure remain unpaid.
