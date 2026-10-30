# fleet02/B11 — weak-L^{3/2} parabolic smoothing at the null-heavy endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T152031Z-fleet02-B11-qform-r18-a91c`  
**Assignment:** Indefinite signatures / complementary constructions and source-valid counterexamples  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL CONJECTURE OPEN`  

## 1. Target, first unpaid implication, and correction boundary

The sole target is the full arbitrary-dimensional statement: independent real coordinates with marginal densities at most one, symmetric `A` with at least three eigenvalues of magnitude at least one, and one universal bound on the density of `X^T A X`.

The previous B11 run reduced the exact-rank-three near-null heavy chamber to a stable-bank problem. In the canonical signature

`H0 = [[0,0,1],[0,1,0],[1,0,0]]`,

write a heavy physical spectral row as `r0=(sqrt(c),0,0)`, `c>=1/2`. The first unpaid implication was to control arbitrary residual Parseval frames without assuming the four exact Walsh banks used in the previous proof.

This run changes mechanism: instead of rounding rows into banks, it proves the exact endpoint `c=1` by a weak-`L^{3/2}` estimate for the physical parabolic kernel. It then combines the current full-spectrum diffuse-range theorem with the residual Schur spectrum to pay a second, genuinely arbitrary rotated subbranch for `c<1`.

The proof explicitly respects the live corrections `QFORM-UV-CONDITIONAL-CAP-FALSE` and `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`: no conditional cap for a conjugate rotated variable is asserted. The endpoint theorem uses genuine independence of one untouched original coordinate; at `c<1` that independence is lost and is not fabricated.

## 2. Source-pinned premises actually consumed

1. **Two-dimensional Parseval projection density.** fleet02/B11 run `20260922T135203Z-b11-qform-6080e0b3`, canonical report commit `245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`, proves: if independent density-cap-one variables are projected by vectors `b_i in R^2` with `sum b_i b_i^T=I_2`, the resulting two-dimensional random vector has density at most `e`.

2. **Named partner fleet03/B11.** Canonical report commit `860d849b7f2e0198bf7c3531a71b14e59f03e430`, run `20260922T121353Z-fleet03-B11-QFORM-r11`, proves the indefinite binary half-potential and the majority-sign physical-pivot consequence

`||p_Q||_infinity <= 8 / |a det B|^(1/4)`

for an invertible indefinite physical `3x3` block `B` with nonzero majority-sign scalar pivot `a`. Its proof keeps original-coordinate translations and supplies the correct Abel interpretation of how a third square removes the opposite-sign rank-two logarithmic singularity.

3. **Diffuse full-range supporting theorem.** Interactive canonical report commit `a302aab3477c64757b511e80d3907f982e04873a` proves that if the entire range projection of a symmetric matrix has coordinate leverage at most `1/32` and there are at least three eigenvalues of magnitude at least one, then the output density is at most

`C_diff = 96 e/(7 sqrt(2)) < 27`,

with arbitrary additional small spectrum and arbitrary coordinate-separable linear/measurable phases allowed.

The full conjecture is still open in the shared claim state; these are supporting premises only.

## 3. Main new theorem: parabolic weak-L^{3/2} smoothing

### Theorem 3.1

Let `Z` be independent of the pair `(V,W)`. Assume `Z` has a probability density `f` with `0<=f<=L`, and `(V,W)` has a joint probability density `g` with `0<=g<=M`. Then

`T = 2 Z W + V^2`

has an essentially bounded density and

`||p_T||_infinity <= 3 * 2^(4/3) * (L M)^(2/3)`.

No independence between `V` and `W` is required.

### Proof

Condition on `(V,W)=(v,w)`. For `w != 0`, the conditional density at level `t` is

`K_t(v,w) = (1/(2|w|)) f((t-v^2)/(2w))`.

The set `w=0` is null under the absolutely continuous pair law, so

`p_T(t) = integral_R2 g(v,w) K_t(v,w) dv dw`.

We prove the distribution estimate

`|{(v,w): K_t(v,w)>lambda}| <= 4 L lambda^(-3/2)`                         (3.1)

uniformly in `t` and `lambda>0`.

For fixed `v` away from the null set `t=v^2`, make the change of variables

`x=(t-v^2)/(2w)`,  `w=(t-v^2)/(2x)`,  `|dw|=|t-v^2|/(2x^2) dx`.

Then

`K_t = |x| f(x)/|t-v^2|`.

Thus, with `a_x=|x|f(x)/lambda`, the measure in (3.1) is

`integral [1/(2x^2)] J(t,a_x) dx`,

where

`J(t,a)=integral_{|t-v^2|<a} |t-v^2| dv`.

For every `t` and `a>0`,

`J(t,a) <= 2 sqrt(2) a^(3/2)`.                                           (3.2)

Indeed scale `t=a tau`, `v=sqrt(a)y`. If `tau<-1` there is no contribution. Otherwise the allowed `y`-set has length at most `2sqrt(2)` when `-1<=tau<=1`, and for `tau>=1` it is the two intervals with `y^2 in (tau-1,tau+1)`, whose total length is also at most `2sqrt(2)` (maximal at `tau=1`); on the allowed set the normalized integrand is at most one.

Using (3.2),

`|{K_t>lambda}| <= sqrt(2) lambda^(-3/2) integral |x|^(-1/2) f(x)^(3/2) dx`.

Since `f<=L`, `f^(3/2)<=sqrt(L) f`. The standard bathtub/rearrangement bound for the decreasing kernel `|x|^(-1/2)` gives

`integral |x|^(-1/2) f(x) dx <= 2 sqrt(2L)`;

hence the last display is at most `4L lambda^(-3/2)`, proving (3.1).

Finally use layer cake and both `integral g=1` and `g<=M`:

`p_T(t) <= integral_0^infinity min(1, 4LM lambda^(-3/2)) d lambda`.

With `lambda_0=(4LM)^(2/3)`, this equals

`lambda_0 + 8LM lambda_0^(-1/2)
 = 3 * 2^(4/3) * (LM)^(2/3)`.

The bound is uniform in `t`. QED.

### Why this is the correct third-direction mechanism

The rank-two saddle `2ZW` can have a logarithmically unbounded density for independent uniform `Z,W`; that control example remains intact. The square `V^2` is not being treated as a bounded-density summand. Instead it changes the reciprocal hyperbolic kernel into a parabolic kernel whose level sets have the critical decay `lambda^(-3/2)`. A bounded **two-dimensional** projection density can then be integrated against that weak-`L^{3/2}` kernel. This is precisely where the third direction pays the logarithmic singularity.

## 4. Corollary: every arbitrary rotated exact null endpoint `c=1`

Let `R` have orthonormal columns and put `A=R H0 R^T`. Suppose one physical row is exactly

`r0=(1,0,0)`.

Then Parseval gives, for every other row `ri=(a_i,b_i,c_i)`,

`sum_{i!=0} a_i^2 = 0`,

so `a_i=0` for every residual row. Hence

`Z1=X0`,
`V=Z2=sum b_i X_i`,
`W=Z3=sum c_i X_i`,

where `X0` is genuinely independent of `(V,W)` and the residual vectors `(b_i,c_i)` form a two-dimensional Parseval frame. The source-pinned projection lemma gives `||p_(V,W)||_infinity<=e`, while `||p_X0||_infinity<=1`. Theorem 3.1 therefore yields

`boxed( ||p_{X^T A X}||_infinity <= 3*2^(4/3)*e^(2/3) < 14.724 ).`

The residual two-dimensional spectral coordinates may share every residual original coordinate and may be strongly dependent for non-Gaussian laws. Thus this is a genuinely rotated endpoint result, not a diagonal or post-rotation-independent theorem. Negating `A` gives the dual `(+,-,-)` signature with the same constant.

This removes the exact endpoint `c=1` from the previous stable-bank debt without constructing any banks.

## 5. Second branch: arbitrary residual rotation with diffuse whitened range

Now take the same canonical null-heavy exact-rank-three geometry with

`r0=(sqrt(c),0,0)`, `1/2<=c<1`, and set `delta=sqrt(1-c)`.

The residual row Gram matrix is

`D = diag(delta^2,1,1)`.

The residual quadratic matrix, after conditioning on `X0`, has the same three nonzero eigenvalues as

`D^(1/2) H0 D^(1/2)
 = [[0,0,delta],[0,1,0],[delta,0,0]],`

namely

`{-delta, delta, 1}`.

Whiten the residual frame by `q_i=D^(-1/2) r_i`. It is Parseval. Assume its coordinate leverage satisfies

`max_i ||q_i||^2 <= 1/32`.                                                (5.1)

Conditional on `X0`, the only new term in the residual variables is linear, hence coordinate-separable. Divide the conditional polynomial by `delta`. Its three nonzero eigenvalue magnitudes are `{1,1,1/delta}`, all at least one, and its entire range projection is exactly that of the whitened residual frame. The source-pinned diffuse-range theorem therefore applies conditionally, uniformly in `X0`, and averaging gives

`boxed( ||p_Q||_infinity <= [96e/(7sqrt(2))] / sqrt(1-c) ).`              (5.2)

In particular, under (5.1), every `c<=3/4` obeys

`||p_Q||_infinity < 52.721`.

This branch permits completely arbitrary residual rotations and arbitrary bounded-density product inputs. Its deterioration as `c->1` is real in this proof and is exactly where Theorem 3.1 supplies a different endpoint mechanism.

## 6. Named partner result applied to the complementary local-chart branch

For the same exact-rank-three `H0` signature, every nonsingular physical principal triple `B=R_I H0 R_I^T` is congruent to `H0`, hence has inertia `(2,1)`. If such a triple has a nonzero majority-sign diagonal pivot `a`, the named fleet03/B11 theorem applies directly:

`||p_Q||_infinity <= 8 / |a det B|^(1/4)`.

Thus any subbranch with a dimension-free lower bound on `|a det B|^(1/4)` is already closed by the partner. The endpoint theorem above is complementary: at `c=1`, Cauchy-Binet determinant mass can be spread among arbitrarily many individually tiny triples, yet the weak-`L^{3/2}` argument closes the whole endpoint without selecting one of them. This is an actual use of the partner result in the conditional branch decomposition, not an attribution of the new endpoint theorem to that result.

The opposite-sign rank-two logarithmic example remains a mandatory control in both arguments; the partner pays it by a half-order potential plus Abel square kernel, while Theorem 3.1 pays it by a parabolic weak-`L^{3/2}` kernel plus a two-dimensional projection cap.

## 7. Source-valid falsifier to a tempting endpoint perturbation

One cannot extend the `c=1` proof to `c<1` merely by saying that the residual first-spectral coefficient has norm `delta=sqrt(1-c)` and is therefore a small random perturbation. There are no moment or scale assumptions on the inputs.

For every `0<delta<=1`, let `Y_delta` have density

`f_delta(y)=delta * 1_[0,1/delta](y)`.

This is a probability density bounded by one, but `delta Y_delta` is exactly uniform on `[0,1]`, independent of how small `delta` is. Hence coefficient-smallness does not imply distributional smallness uniformly over the target class. Any near-endpoint argument must retain exact product-linear provenance rather than invoke a moment-based perturbation limit.

This falsifies only that proof shortcut, not QFORM.

## 8. What remains genuinely unpaid

For the exact-rank-three null-heavy chamber, the residual is now narrower:

- `1/2<=c<1`;
- the whitened residual frame violates the diffuse leverage condition (5.1);
- no available physical triple has a dimension-free partner pivot/determinant scale;
- one may not perturb from `c=1` using coefficient norm alone;
- and one may not replace the lost independence of the heavy spectral coordinate by a conditional density cap, by the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`.

The next essential implication is therefore a **dependence-safe near-endpoint compiler**: exploit the fact that `(U,V,W)` are three linear projections of the same independent product source to obtain an analogue of Theorem 3.1 when `Z1=sqrt(c)X0+U`, without assuming conditional independence; or give a genuine target-level counterexample. Extra nonzero spectrum outside the exact-rank-three chamber remains a separate nonseparable debt in the full conjecture.

## 9. Exact computation used

`CHECK.py` and `CHECK.out` are in this immutable run folder. The checker evaluates the exact elementary formula for `J(t,a)` on a dense normalized grid against the proved coarse constant `2sqrt(2)`, evaluates the endpoint constant, evaluates the diffuse constant and its `c<=3/4` specialization, and checks the residual eigenvalue formula at representative values. It terminates

`QFORM_NULL_ENDPOINT_WEAKL32_CHECK_PASS`.

The numerical grid is regression evidence only; the theorem is proved symbolically above and no finite computation is used as closure.

## 10. Status

`ESSENTIAL_STEP_APPLIED` in the stated exact-rank-three indefinite scope. The full arbitrary-dimension, arbitrary-spectrum QFORM conjecture remains **OPEN / NOT PROVED**. No continuity claim is made beyond existence of an essentially bounded density in the proved branches.
