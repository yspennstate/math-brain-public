# account01/B08 — pointwise-decay obstruction and an L^3 replacement for the quadratic-form density problem

**Control:** owner revision `2026-09-22.4` (later redirect; supersedes FEI/MOC4 work)  
**Run:** `20260922T110731Z-account01-B08`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROPOSED_SUBGOAL_REFUTED / DIAGONAL_THEOREM_PROVED`  
**Full rotated quadratic-form conjecture:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Target and outcome

The owner target is: if `X_1,...,X_n` are independent real random variables whose densities are bounded by `1`, and a real quadratic form `Q(x)=x^T A x` has at least three eigenvalues of absolute value at least `1`, prove that `Q(X)` has a density bounded by a universal constant.

This report makes two rigorous changes to the proposed Fourier route.

1. The suggested intermediate statement

   `|E exp(i t X^2)| <= C |t|^{-1/2}` uniformly over all densities `f<=1`

   is **false in the strongest possible way**: for every fixed nonzero `t`, the supremum over such densities equals `1`.

2. Pointwise decay is unnecessary in the coordinate-diagonal case. A sharp-enough uniform integrability substitute holds:

   `|| E exp(i t X^2) ||_{L^3(dt)} <= 2 (2 pi)^(1/3)`.

   Three independent square factors are therefore in `L^1` by Holder. Consequently every coordinate-diagonal quadratic form with three coefficients `|lambda_j|>=1` has density bounded by the explicit universal constant `8`, for arbitrary independent input densities bounded by `1`, with arbitrary signs and all remaining coefficients unrestricted.

The genuine unsolved step is now a **rotation-stable/product-measure analogue of this L^3 mechanism**, not the false law-uniform pointwise `|t|^{-1/2}` estimate.

## 1. A decisive counterexample to law-uniform pointwise decay

### Proposition 1.1

For every `t != 0`,

`sup_f | integral_R exp(i t x^2) f(x) dx | = 1`,

where the supremum is over probability densities satisfying `0<=f<=1` a.e. In fact, for every `epsilon>0` there is a compactly supported indicator density `f=1_E`, `|E|=1`, for which the modulus is at least `1-epsilon`.

### Proof

Fix `0<delta<pi`. For definiteness replace `t` by `|t|`, since complex conjugation handles the other sign. For every sufficiently large integer `k`, set

`I_k = [ sqrt((2 pi k-delta)/t), sqrt((2 pi k+delta)/t) ]`.

These intervals are disjoint. On each `I_k`,

`dist(t x^2, 2 pi Z) <= delta`,

hence

`Re exp(i t x^2) >= cos(delta)`.

Their lengths are

`|I_k| = 2 delta / { sqrt(t) [sqrt(2 pi k+delta)+sqrt(2 pi k-delta)] }`.

Thus `|I_k|` is comparable to `delta/(sqrt(t) sqrt(k))`, so

`sum_k |I_k| = infinity`.

A finite union of these intervals therefore has measure exceeding `1`. Choose a measurable subset `E` of that finite union with `|E|=1` and put `f=1_E`. Then `f` is a probability density bounded by `1` and

`Re integral exp(i t x^2) f(x) dx >= cos(delta)`.

Letting `delta` tend to `0` proves that the supremum is at least `1`; the reverse inequality is trivial from `|exp(i t x^2)|=1` and `integral f=1`. `QED`

### Consequence

There is no universal estimate of the form

`|E exp(i t X^2)| <= C (1+|t|)^(-alpha)`

with any `alpha>0`, uniformly over all probability densities bounded by `1`.

This does **not** refute the target conjecture. The bad density in Proposition 1.1 is allowed to depend on the frequency `t`. For each fixed density the Fourier transform of `X^2` still tends to zero by the Riemann--Lebesgue lemma. What fails is precisely the proposed *law-uniform pointwise* stationary-phase sublemma.

## 2. Uniform L^{3/2} control of the square density

The correct replacement is an integral norm.

Let `X` have density `f`, with `0<=f<=1` and `integral f=1`, and put `Y=X^2`. For `y>0`, `Y` has density

`g(y) = [f(sqrt(y))+f(-sqrt(y))]/(2 sqrt(y))`.

Define for `x>0`

`h(x)=f(x)+f(-x)`.

Then

`0<=h<=2`,  and  `integral_0^infinity h(x) dx=1`.

Changing variables `y=x^2` gives

`integral_0^infinity g(y)^(3/2) dy
 = 2^(-1/2) integral_0^infinity h(x)^(3/2) x^(-1/2) dx`.

Since `h<=2`,

`2^(-1/2) h^(3/2) <= h`.

Hence

`integral g^(3/2) <= integral_0^infinity h(x) x^(-1/2) dx`.

The last integral is maximized, under `0<=h<=2` and `integral h=1`, by filling the decreasing weight `x^(-1/2)` from the origin: `h=2 1_[0,1/2]`. Therefore

`integral_0^infinity h(x) x^(-1/2) dx <= 2 integral_0^(1/2) x^(-1/2) dx = 2 sqrt(2)`.

Thus

`||g||_(3/2) <= (2 sqrt(2))^(2/3) = 2`.

We record this as:

### Theorem 2.1 — square-density endpoint

For every probability density `f<=1`, the density `g` of `X^2` satisfies

`boxed( ||g||_(3/2) <= 2 )`.

No support, moment, smoothness, symmetry or unimodality assumption is used.

## 3. Uniform L^3 Fourier control

Use the unnormalized Fourier transform

`g_hat(t)=integral exp(i t y) g(y) dy`.

Interpolation between

`||g_hat||_infinity <= ||g||_1`

and Plancherel

`||g_hat||_2 = sqrt(2 pi) ||g||_2`

gives the Hausdorff--Young estimate at `p=3/2`, `p'=3`,

`||g_hat||_3 <= (2 pi)^(1/3) ||g||_(3/2)`.

Combining with Theorem 2.1,

`boxed( || E exp(i t X^2) ||_L3(dt) <= 2 (2 pi)^(1/3) ).`

More generally, completing the square shows that for every real `beta` and every `lambda !=0`,

`lambda X^2 + beta X
 = lambda (X+beta/(2lambda))^2 - beta^2/(4lambda)`.

Translation preserves the density bound `<=1`, multiplication by the final unimodular phase does not change absolute values, and scaling `t -> lambda t` gives

`boxed(
 || E exp(i t(lambda X^2+beta X)) ||_3
 <= 2 (2 pi)^(1/3) |lambda|^(-1/3).
)`

This uniformity in the linear term will survive conditioning on other coordinates whenever the selected quadratic coordinates do not couple to each other.

## 4. Complete theorem for coordinate-diagonal quadratic forms

### Theorem 4.1

Let `X_1,...,X_n` be independent, each with a density bounded by `1`. Let

`Q(X)=sum_{j=1}^n lambda_j X_j^2`

and assume that three coefficients satisfy

`|lambda_1|,|lambda_2|,|lambda_3| >=1`.

Then `Q(X)` has a bounded continuous density `p_Q` and

`boxed( ||p_Q||_infinity <= 8 ).`

This is independent of `n`, of all input laws, of the signs of the coefficients, of repeated coefficients, and of every remaining `lambda_j`.

### Proof

Write

`psi_j(t)=E exp(i t X_j^2)`.

Independence gives

`phi_Q(t)=prod_j psi_j(lambda_j t)`.

All characteristic functions have modulus at most `1`, hence

`|phi_Q(t)| <= prod_{j=1}^3 |psi_j(lambda_j t)|`.

Holder with exponents `(3,3,3)` and the previous section yield

`||phi_Q||_1
 <= prod_{j=1}^3 ||psi_j(lambda_j .)||_3
 <= [2(2 pi)^(1/3)]^3 prod_{j=1}^3 |lambda_j|^(-1/3)
 <= 16 pi`.

Therefore `phi_Q` is integrable. Fourier inversion for finite measures implies that `Q(X)` has a bounded continuous density and

`||p_Q||_infinity <= (1/(2 pi)) ||phi_Q||_1 <= 8`.

`QED`

### Why the threshold three appears naturally here

Each square factor is uniformly controlled in `L^3`, not in `L^2`. Three factors are exactly enough for an `L^1` product by Holder. Two factors give only an `L^(3/2)` product from this endpoint. This matches the owner's two-opposite-sign warning at the level of the Fourier integrability mechanism.

## 5. Conditional-diagonal extension

The same proof gives a useful nontrivial extension beyond globally diagonal forms.

### Theorem 5.1

Write `Q(x)=x^T A x` in the independent coordinate basis. Suppose there are three coordinate indices `i,j,k` such that

- `|A_ii|,|A_jj|,|A_kk| >=1`, and
- `A_ij=A_ik=A_jk=0`.

Then `Q(X)` has density bounded by `8`.

### Proof

Condition on all coordinates except `X_i,X_j,X_k`. For each fixed outside vector, the phase in the three remaining independent variables is

`A_ii X_i^2 + beta_i X_i
 + A_jj X_j^2 + beta_j X_j
 + A_kk X_k^2 + beta_k X_k + constant`,

where the `beta`'s depend on the conditioned outside coordinates. The uniform linear-term `L^3` bound from Section 3 is independent of those `beta`'s. Therefore, for every conditioning value, the conditional characteristic function has `L^1(dt)` norm at most `16 pi`. Averaging over the outside coordinates and using `|E Z|<=E|Z|`, followed by Tonelli, preserves this bound. Fourier inversion again gives density at most `8`. `QED`

Thus the real difficulty is not small lower-order linear perturbations; it is the mutual coupling among the three smoothing directions after one insists on the original independent coordinate system.

## 6. A warning about rotating to the eigenbasis

A tempting next move is to rotate the vector `X` so that `A` is diagonal. That destroys independence. A mere dimension-free `L^infinity` bound on the joint density of the three projected eigen-coordinates is not, by itself, sufficient for an indefinite quadratic form: an arbitrary bounded joint density can place its mass in a thin large-radius neighborhood of a null cone, concentrating the value of an indefinite quadratic form in an arbitrarily short interval.

Therefore the remaining theorem must preserve more of the **product structure** of the original measure than just an `L^infinity` projection bound.

This is consistent with the standard Ball--Rogozin/Ball--Nazarov projection results: bounded coordinate densities imply dimension-free bounded densities for linear projections, but such a marginal-density statement alone does not encode the conditional product information needed after a nonlinear squaring map.

## 7. Corrected conditional end-to-end Fourier route

The false pointwise-decay chain should be replaced by the following:

1. **PROVED HERE:** for one independent coordinate square (even with an arbitrary linear term), its characteristic factor has a universal `L^3` norm.
2. **PROVED HERE:** if three such factors remain conditionally independent, their product is uniformly `L^1`, yielding the explicit density bound `8`.
3. **OPEN CRUX:** prove a rotation-stable product-measure oscillatory inequality that replaces factorization when the three `|lambda|>=1` eigendirections are coupled in the coordinate basis.
4. **THEN:** Fourier inversion gives the full conjecture with the corresponding explicit constant.

A clean exact formulation of the missing implication is:

### `QFORM-PRODUCT-OSCILLATORY-L1-v1` (open)

Find a universal `C_0` such that for every real symmetric `A` with at least three eigenvalues of absolute value at least `1`, every product density

`F(x)=prod_i f_i(x_i)`,  `0<=f_i<=1`, `integral f_i=1`,

and every real linear term `b`,

`boxed(
 integral_R | integral_R^n exp(i t (x^T A x + b.x)) F(x) dx | dt <= C_0.
)`

The target conjecture follows immediately with density bound `C_0/(2 pi)`. This formulation keeps exactly the product structure that a rotation would lose and avoids asking for the refuted law-uniform pointwise decay.

## 8. Next mathematical mechanisms worth testing

The next run should test one of two genuinely target-level mechanisms rather than redo stationary phase on a single arbitrary density.

**Mechanism A: oscillatory Brascamp--Lieb.** Treat the product amplitude as coordinate projections and seek an `L^1_t` oscillatory Brascamp--Lieb inequality whose transversality parameter depends only on the presence of three singular values `>=1`, not on a particular coordinate minor. A naive selection of a `3x3` principal minor is unlikely to be dimension-free for delocalized eigenvectors.

**Mechanism B: randomized coordinate blocking plus conditioning.** Use the three-dimensional large-eigenvalue spectral subspace to construct three disjoint coordinate blocks carrying a quantitative amount of the three directions, then apply a block version of the `L^3` square estimate together with the Ball--Rogozin projection theorem inside each block. Any proposed block extraction must be tested on maximally delocalized orthonormal eigenvectors, where fixed coordinate minors are of order powers of `n^{-1/2}`.

## 9. Scope and provenance

This report does **not** prove the full rotated conjecture and does not claim novelty from a search miss. It rigorously refutes one proposed universal Fourier sublemma, proves an explicit universal constant `8` for the full arbitrary-law coordinate-diagonal case (and the conditional-diagonal extension), and isolates a stronger rotation-stable `L^1` characteristic-function implication sufficient for the owner's full target.

A current literature check was used only for orientation. Standard sources confirm dimension-free projection-density bounds for linear combinations/projections of independent bounded-density variables (Rogozin; Ball; Ball--Nazarov as summarized in Rudelson's PCMI notes), while the searched Hanson--Wright literature concerns concentration under substantially stronger tail assumptions and does not supply the exact theorem claimed here. No external source was used as a premise in the proofs above.
