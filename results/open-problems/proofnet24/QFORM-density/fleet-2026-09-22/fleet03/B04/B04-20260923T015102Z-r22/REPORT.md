SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T01:51:02Z.
attacking: a two-sided-leakage Fourier-Plancherel rearrangement for an original-coordinate cross bank of dimension at least three.

# fleet03/B04 r22 — finite-bank Plancherel closure with arbitrary two-sided quadratic leakage

Programme `QFORM-DENSITY-3EIG-20260922`; assignment `Product Fourier rearrangement`; run `B04-20260923T015102Z-r22`. Execution status `WITHOUT_VERIFIED_BRAIN`. Outcome `NEW SUPPORTING THEOREM / CONTINUOUS DENSITY IN STATED SCOPE / FULL QFORM OPEN`.

## 1. Scope and premise actually used

All inputs are original independent real coordinates with densities bounded by one. No Gaussianity, log-concavity, moment, compact-support, connected-support, post-rotation independence, arbitrary-joint coarea, or law-uniform pointwise oscillatory decay is used.

Completed peer input used at equation level: fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, source `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. In the form needed here: if `R` has `r` orthonormal columns and `X` is an original-coordinate cap-one product vector, then `R^T X` has an `r`-dimensional density bounded by `exp(r/2)`.

The designated partner `fleet04/B04` had current QFORM start/login records but no completed QFORM handoff or canonical report visible at the fresh lookup used for this run, so no designated-partner theorem is fabricated.

## 2. Fourier-Plancherel bank theorem

Let `X` be an original-coordinate product vector in `R^m` and let `Y=(Y_1,...,Y_r)` consist of `r>=3` further original coordinates, independent of `X`, with each one-dimensional density at most one. Let `B` be an `m x r` real matrix of full column rank, with singular values `sigma_1,...,sigma_r>0`. Let `C` and `D` be arbitrary real symmetric matrices of the matching dimensions, and allow arbitrary affine terms. It is enough to write

`Q = F(X) + 2 X^T B Y + Y^T D Y + b^T Y`,                     (2.1)

where `F` may be any measurable real function of `X` (in the quadratic-form application it contains `X^T C X` and all affine terms on the X side).

### Theorem 2.1 — QFORM-FINITE-BANK-PLANCHEREL-v1

The law of `Q` has a bounded continuous density vanishing at infinity, and

`||p_Q||_infinity <= [r sqrt(e)/(r-2)] (prod_{j=1}^r sigma_j)^(-1/r)`.    (2.2)

In particular, for `r=3`,

`||p_Q||_infinity <= 3 sqrt(e) (sigma_1 sigma_2 sigma_3)^(-1/3)`
`                     = 4.946163812100385... (sigma_1 sigma_2 sigma_3)^(-1/3)`.   (2.3)

This permits arbitrary quadratic leakage on BOTH sides of the cross bank.

### Proof

Absorb the fixed affine term by

`Z = B^T X + b/2`.                                               (2.4)

Take an SVD `B=U Sigma V^T`, where `U` has `r` orthonormal columns. By the completed fleet02/B06 projection theorem, `U^T X` has density at most `exp(r/2)`. Therefore `Z` has density `rho_Z` satisfying

`||rho_Z||_infinity <= K := exp(r/2)/(prod sigma_j)`.            (2.5)

Fix `t` and push the complex measure `e^{itF(X)} dP_X` through `Z`. Its density has the form

`eta_t(z)=rho_Z(z) E[e^{itF(X)} | Z=z]`,                         (2.6)

hence pointwise

`|eta_t(z)| <= rho_Z(z)`.                                        (2.7)

Let `g(y)=prod_{j=1}^r f_j(y_j)` and

`q_t(y)=g(y) exp(it y^T D y)`.                                   (2.8)

Using the Fourier transform convention

`hat q(xi)=integral exp(i xi.y) q(y) dy`,                         (2.9)

define

`h_t(z)=integral exp(it y^T D y + i 2t z.y) g(y)dy`
`      =hat q_t(2tz)`.                                            (2.10)

Then

`phi_Q(t)=integral eta_t(z) h_t(z) dz`.                           (2.11)

Cauchy-Schwarz with the probability density `rho_Z` gives

`|phi_Q(t)| <= integral rho_Z |h_t|`
`             <= (integral rho_Z |h_t|^2)^(1/2)`
`             <= K^(1/2) ||h_t||_2`.                              (2.12)

Because every one-dimensional input density is at most one and integrates to one,

`||g||_2^2 = prod_j integral f_j^2 <=1`.                          (2.13)

The quadratic phase in (2.8) has modulus one, so Plancherel and scaling yield

`||h_t||_2`
` = (2|t|)^(-r/2) ||hat q_t||_2`
` = (2|t|)^(-r/2) (2pi)^(r/2) ||q_t||_2`
` <= (pi/|t|)^(r/2)`.                                            (2.14)

Consequently, with

`A = pi^(r/2) K^(1/2)`,                                          (2.15)

we have the integrated, not pointwise-law-uniform, estimate for this fixed product law

`|phi_Q(t)| <= min(1, A |t|^(-r/2))`.                            (2.16)

For `r>2`, set `t_0=A^(2/r)`. An exact integration gives

`integral_R |phi_Q(t)|dt`
` <= 2 [t_0 + A integral_{t_0}^infinity t^(-r/2)dt]`
` = 2 [r/(r-2)] A^(2/r).                                        (2.17)

Since

`A^(2/r)=pi K^(1/r)=pi sqrt(e)(prod sigma_j)^(-1/r)`,            (2.18)

Fourier inversion gives

`||p_Q||_infinity <= (1/(2pi)) integral |phi_Q|`
` <= [r sqrt(e)/(r-2)] (prod sigma_j)^(-1/r)`.                   (2.19)

Moreover `phi_Q` is integrable, so the inverse Fourier transform is a bounded continuous `C_0` density. This proves (2.2). QED.

### Original-coordinate corollary

For a general symmetric physical matrix `A`, choose an original-coordinate subset `J` with `|J|=r>=3`, put `I=J^c`, and let

`B=A_{I,J}`.                                                      (2.20)

If `B` has full column rank, then conditioning is unnecessary: (2.1) is exactly the physical block decomposition, with arbitrary `A_{I,I}` and arbitrary `A_{J,J}`. Therefore (2.2) applies with the singular values of the ORIGINAL-coordinate cross block `A_{J^c,J}`. No eigenbasis independence is asserted.

## 3. Genuinely rotated indefinite target family with diffuse physical couplings

For each `m>=2`, split `3m` original X-coordinates into three disjoint blocks and let `u_1,u_2,u_3` be the flat unit vectors on those blocks. Put `U=[u_1 u_2 u_3]`, let `Y in R^3` be three further original coordinates, and define the symmetric matrix on `R^(3m+3)` by

`A_m = [[(1/2) U U^T, U], [U^T, (1/2) I_3]]`.                  (3.1)

On `span(U) direct_sum R^3`, this is three copies of

`[[1/2,1],[1,1/2]]`,                                            (3.2)

so its active eigenvalues are

`3/2,3/2,3/2,-1/2,-1/2,-1/2`.                                  (3.3)

Thus the matrix is indefinite and has exactly three eigenvalues of absolute value at least one. It is genuinely nonseparable in the original independent coordinates. Every X-to-Y physical coupling has size `1/sqrt(m)`, and every nonzero same-X-block quadratic coefficient has size `1/(2m)`, both tending to zero with dimension.

The cross block `B=U` has all three singular values equal to one. Hence Theorem 2.1 gives, for EVERY admissible cap-one product input law and every `m`,

`||p_(X^T A_m X)||_infinity <= 3 sqrt(e)`
`                              =4.946163812100385...`.            (3.4)

The density is continuous and vanishes at infinity. This is an aggregate-before-local-inversion estimate: no individual `1/sqrt(m)` physical coefficient is inverted.

## 4. What this pays and what remains

Paid in this run: any original-coordinate bank of size `r>=3` whose complement-to-bank cross block has full column rank has a universal continuous-density estimate depending only on the geometric mean of those cross singular values, with completely arbitrary quadratic leakage on both sides. In the critical `r=3` case the exact explicit coefficient is `3 sqrt(e)`.

This strictly removes the one-clean-side hypothesis from the earlier r20 cross-bank theorem when three physical bank coordinates can be retained. It also gives an explicit family satisfying the target with only three large eigenvalues while all diffuse cross entries tend to zero.

Not paid: the bare hypothesis `s_3(A)>=1` does not force one three-coordinate physical bank with `prod sigma_j` bounded below. The known `1 direct_sum J_m/m direct_sum (-J_m/m)` family has every coordinate cut of cross rank at most two, so a universal proof still needs a rank-one/rank-two grouped-bank or ridge route in those structural survivors.

Next exact debt: `QFORM-THREE-COLUMN-CROSSBANK-OR-LOW-CROSSRANK-ROUTING-v1`: from `s_3(A)>=1`, either expose a three-original-coordinate bank with quantitatively nontrivial aggregate cross determinant and apply Theorem 2.1, or prove that failure of every such bank forces a globally low-cross-rank/grouped-star geometry that routes to the already-paid rank-one/rank-two bank, ridge, or Schur mechanisms.

Full QFORM remains OPEN. No target counterexample is claimed.
