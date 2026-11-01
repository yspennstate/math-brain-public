# QFORM B04 — product Fourier rearrangement

**Run:** `B04-20260922T114427Z-qform-product-rearrange-r1`  
**Status:** `ESSENTIAL_STEP_APPLIED`; full conjecture remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Assignment:** replace the refuted law-uniform pointwise Fourier decay route by decreasing-rearrangement/product-space estimates, with an explicit genuinely rotated indefinite case.

## 1. Source state and corrections consumed

The controlling programme is `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`. The target is the arbitrary-dimensional product-input conjecture: independent real coordinates with densities bounded by one, and a real symmetric quadratic form with at least three eigenvalues of modulus at least one, should have a universally bounded output density.

I used all three required corrections. The law-uniform pointwise stationary-phase bound is false for arbitrary bounded densities; a naive fiber supremum loses dimension; and diagonalizing the quadratic form does not preserve independence. None of those corrected routes is used below.

External source used exactly at its proved scope: Livshyts–Paouris–Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949. For a product density with one-dimensional factors bounded by one, every one-dimensional orthogonal marginal has density at most `sqrt(2)`.

Named partner `fleet03/B04` had begun its qform run at the fresh source read but had no completed handoff yet, so I did not wait. I substantively applied the complete OTHER-account result fleet01/B05, brain commit `5f703e4c639acefc3f33aa4d149fe5ff85814622`, handoff blob `028e99f4705e07fac0fb369efb7ed63ec8927c35`: its flat-Walsh calculation shows that best-chart and naive determinant-weighted reciprocal-Jacobian averaging lose polynomially in dimension. This is used below to delimit exactly what the new theorem does and does not solve.

For comparison I also read fleet02/B05 blob `c4768e1b2c204c6e24f6930802600102c1b4922b`, which records the exact one-square `L^{3/2}` scale and the failure of bare post-squaring `L^2`; I rederive the needed `L^{3/2}` estimate here so the proof is self-contained.

## 2. A private-block product-Fourier theorem

The useful structural hypothesis is not that the form is diagonal in physical coordinates. It is that, after conditioning a shared coordinate block, three quadratic spectral coordinates retain disjoint *private* product randomness.

### Theorem `QFORM-PRIVATE-BLOCK-FOURIER-v1`

Let the physical coordinates be partitioned into four disjoint sets

`S_1 ⊔ S_2 ⊔ S_3 ⊔ T = {1,...,n}`.

Assume the quadratic polynomial has the representation

`Q(x) = R(x_T) + sum_{j=1}^3 lambda_j ( a_j · x_{S_j} + b_j(x_T) )^2`,        (2.1)

where `lambda_j != 0`, each `a_j` is a fixed nonzero vector on `S_j`, `alpha_j := ||a_j||_2`, each `b_j` is a real linear functional of `x_T`, and `R` is any real quadratic polynomial in `x_T`. Let `X_i` be independent with probability densities bounded by one.

Then the characteristic function `phi_Q(t)=E exp(i t Q)` is integrable and

`||phi_Q||_1 <= 32 pi / [ (alpha_1 alpha_2 alpha_3)^(2/3) |lambda_1 lambda_2 lambda_3|^(1/3) ]`.      (2.2)

Consequently `Q(X)` has a continuous density and

`||p_Q||_infinity <= 16 / [ (alpha_1 alpha_2 alpha_3)^(2/3) |lambda_1 lambda_2 lambda_3|^(1/3) ]`.     (2.3)

If two coefficients, say `lambda_i,lambda_j`, have the same sign, then independently of the third coefficient one also has the sharper essential-supremum estimate

`||p_Q||_infinity <= 2 pi / [ alpha_i alpha_j sqrt(|lambda_i lambda_j|) ]`.                           (2.4)

Thus (2.2) supplies continuity while (2.4) can supply a better density constant.

### Proof

Condition on `X_T=t`. Then the three variables

`Y_j = a_j · X_{S_j} + b_j(t)`

are independent because their underlying coordinate blocks are disjoint.

By the one-dimensional marginal theorem of Livshyts–Paouris–Pivovarov applied after scaling `a_j = alpha_j theta_j` with `||theta_j||_2=1`, every `Y_j` has a conditional density bounded by

`K_j = sqrt(2)/alpha_j`.                                                        (2.5)

The additive shift `b_j(t)` does not change this bound.

We next record the exact averaged square estimate. If `Y` has density `g<=K` and

`Z = lambda (Y+c)^2`, `lambda != 0`,

then

`||p_Z||_{3/2} <= 2 K^(2/3) |lambda|^(-1/3)`.                                  (2.6)

For completeness, translate so `c=0` and reflect if `lambda<0`. Put

`G(r)=g(r)+g(-r)` for `r>0`.

Then `0<=G<=2K`, `int_0^infinity G(r)dr=1`, and for `z=lambda r^2`

`p_Z(z)=G(r)/(2 lambda r)`.

Therefore

`int p_Z(z)^(3/2) dz = (2 lambda)^(-1/2) int_0^infinity G(r)^(3/2) r^(-1/2) dr`.

Since the weight `r^(-1/2)` is decreasing, the bathtub/rearrangement principle maximizes the last integral under `G<=2K` and `int G=1` at `G=2K 1_[0,1/(2K)]`. Its value is `4K`. Hence

`int p_Z^(3/2) <= 2 sqrt(2) K / sqrt(lambda)`,

which is equivalent to (2.6).

Use the Fourier convention `hat f(s)=int exp(i s y) f(y)dy`. Interpolating the trivial `L^1 -> L^infinity` Fourier bound with Plancherel gives Hausdorff–Young in the sufficient form

`||hat f||_3 <= (2 pi)^(1/3) ||f||_{3/2}`.                                     (2.7)

Thus, for the conditional characteristic function `psi_{j,t}` of `lambda_j Y_j^2`, (2.5)--(2.7) give

`||psi_{j,t}||_3 <= 2 (2 pi)^(1/3) K_j^(2/3) |lambda_j|^(-1/3)`.               (2.8)

The bound is uniform in the conditioned value `t`. Conditional independence and Hölder now give

`int |phi_{Q|T=t}(s)| ds
 <= product_j ||psi_{j,t}||_3
 <= 16 pi (K_1 K_2 K_3)^(2/3) |lambda_1 lambda_2 lambda_3|^(-1/3).`            (2.9)

Substituting `K_j=sqrt(2)/alpha_j` gives (2.2), because

`(K_1 K_2 K_3)^(2/3)=2/(alpha_1 alpha_2 alpha_3)^(2/3)`.

For the unconditional characteristic function,

`|phi_Q(s)| <= E[ |phi_{Q|T}(s)| ]`.

Tonelli and (2.9) imply the same `L^1` bound for `phi_Q`. Fourier inversion then gives a continuous density and (2.3).

For (2.4), suppose `lambda_i,lambda_j` have the same sign. If `U=lambda_iY_i^2` and `V=lambda_jY_j^2`, their conditional densities satisfy, on the appropriate half-line,

`p_U(u) <= K_i / sqrt(|lambda_i| u)`,
`p_V(v) <= K_j / sqrt(|lambda_j| v)`.

Their convolution is therefore bounded by the beta integral

`K_i K_j / sqrt(|lambda_i lambda_j|) * int_0^w [u(w-u)]^(-1/2)du
 = pi K_i K_j / sqrt(|lambda_i lambda_j|)`.

Convolution with the third conditional summand and translation by `R(t)` cannot increase the `L^infinity` norm. Average in `t` and substitute (2.5) to obtain (2.4). QED.

## 3. Spectral corollary inside the target

Suppose `A` has three genuine orthonormal eigenvectors `r_1,r_2,r_3` with eigenvalues `lambda_j`, `|lambda_j|>=1`. Let

`B = A - sum_{j=1}^3 lambda_j r_j r_j^T`.

Assume there is a coordinate partition `S_1,S_2,S_3,T` such that

1. `r_k` vanishes on `S_j` whenever `k!=j`;
2. `alpha_j=||r_j|_{S_j}||_2>0`;
3. `B` is supported on `T x T`.

Then (2.1) holds with `a_j=r_j|_{S_j}`, `b_j(x_T)=<r_j|_T,x_T>`, and `R(x_T)=x_T^T B x_T`. Hence (2.2)--(2.4) are target-valid for this genuinely rotated class. The signs of the three large eigenvalues are arbitrary in the Fourier estimate; for the density-only bound, pigeonhole supplies a same-sign pair.

This is strictly more general than physical-coordinate diagonalization: all three large eigenvectors may overlap on the shared block `T`; only a positive amount of exact private product randomness is required.

## 4. Explicit genuinely rotated indefinite example

Take six physical coordinates. Let

`alpha=1/sqrt(2)`,
`u_1=(1,1,1)/sqrt(3)`,
`u_2=(1,1,-2)/sqrt(6)`,
`u_3=(1,-1,0)/sqrt(2)`

in the shared coordinates `4,5,6`, and define

`r_1 = alpha e_1 + alpha u_1`,
`r_2 = alpha e_2 + alpha u_2`,
`r_3 = alpha e_3 + alpha u_3`.

The `r_j` are orthonormal. Set

`A = 2 r_1 r_1^T - r_2 r_2^T - r_3 r_3^T`.

Its nonzero eigenvalues are exactly `(2,-1,-1)`, so it is indefinite and satisfies the target three-large-eigenvalue threshold. It is not diagonal in the physical coordinates: each private coordinate is coupled to the shared block, and the shared block has nonzero off-diagonal entries.

With `S_j={j}` and `T={4,5,6}`, one has `alpha_j=1/sqrt(2)`. The Fourier theorem gives a continuous density with

`||p_Q||_infinity <= 16 * 2^(2/3)`.

Using the same-sign pair `(-1,-1)` in (2.4) improves the bound to

`||p_Q||_infinity <= 4 pi`.                                                     (4.1)

This holds for every choice of independent physical-coordinate input laws with densities at most one; no moments, centering, support or smoothness are assumed.

## 5. Why this is a real advance but not the full conjecture

The theorem identifies a precise product-space mechanism that survives the pointwise-decay correction: do not ask each oscillatory factor for pointwise decay. Instead, obtain a one-square `L^{3/2}` density bound by decreasing rearrangement, convert it to an `L^3` Fourier budget, and spend three independent private blocks via Hölder. Three large quadratic directions are exactly what makes the exponents close: `1/3+1/3+1/3=1`.

The theorem also isolates the generic obstruction. A general rotated eigensystem need not have any coordinate on which two of the three eigenvectors vanish. In the flat-Walsh system from fleet01/B05, every coordinate participates in all three rows, and its exact minor calculation shows that naive best-chart or Cauchy–Binet reciprocal-Jacobian averaging loses a power of dimension. Therefore the remaining target-level implication is not another local chart estimate.

The first unpaid implication for this B04 pathway is now:

> **Soft-private-block / averaged rearrangement problem.** Replace the exact private-support hypotheses above by a dimension-free averaged inequality that tolerates simultaneous participation of each physical coordinate in all three large eigenvectors, while retaining the three `L^{3/2}` square budgets and not paying a reciprocal-minor or fiber-volume factor.

A valid solution could be a Brascamp–Lieb/rearrangement inequality directly for the coupled three-direction product amplitude, or a randomized conditioning scheme with a quantitatively bounded contamination term. The flat-Walsh family is the mandatory control: any proposed averaging that reduces to `sum |det R_J|` or to a fiber supremum is already ruled out by the consumed peer result.

## 6. Conditional end-to-end route

A compact conditional proof of the full conjecture is therefore:

1. Prove the soft-private-block averaged rearrangement implication for an arbitrary orthonormal triple of large eigenvectors, with a universal loss independent of dimension and of the input laws.
2. Condition all remaining spectral/coordinate structure in a way covered by that implication, preserving product normalization rather than rotated independence.
3. Apply the one-square `L^{3/2}` rearrangement estimate to the three large directions and Hölder in Fourier space, obtaining a universal `L^1` bound for the full characteristic function.
4. Fourier inversion gives a continuous bounded density with a universal constant.

Step 1 is the first essential missing inference. The present theorem proves it exactly when the three spectral directions possess disjoint private physical-coordinate blocks and gives explicit constants. It does not claim that generic orthonormal triples possess such blocks.

## 7. Integrity status

No pointwise stationary-phase estimate, rotated-coordinate independence, fiber supremum, best coordinate minor, benchmark answer, paid model/API call, or numerical histogram is used. The result is a restricted supporting theorem and an explicit genuinely rotated indefinite target instance, not a full solution of `QFORM-FULL`.
