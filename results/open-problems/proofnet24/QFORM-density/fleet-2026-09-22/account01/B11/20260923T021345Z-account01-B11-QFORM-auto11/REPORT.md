SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T02:13:45Z.
attacking: indefinite exact-rank-three zero/near-zero physical-diagonal chamber; derive a product-preserving five-null-ray bank compiler and isolate the remaining tangent-bank stability step.

# QFORM account01/B11 auto11 — finite null-ray bank compiler

## Status

`ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`.

This run proves a self-contained product-preserving compiler for exact-rank-three indefinite forms whose physical spectral rows lie on at most five projective null rays. The result is uniform in the number of original coordinates per ray, in all cap-one input laws, in all leverage patterns (including a near-coloop), and in both signatures `(2,1)` and `(1,2)`. It does **not** prove the near-ray tangent-leakage stability required for the unrestricted zero-diagonal chamber, and it does not address arbitrary extra spectrum.

The proof keeps the opposite-sign rank-two logarithmic singularity as a control. The third direction enters through a dependence-safe saddle-plus-square estimate. No post-rotation independence, arbitrary-joint coarea lemma, conditional-density-as-independence step, good-physical-minor hypothesis, moment/support/log-concavity assumption, or perturbative deletion is used.

## 1. Dependence-safe saddle-plus-square lemma

### Lemma 1 (`QFORM-ONE-SIDED-SADDLE-SQUARE-v1`)

Let `Z` be independent of the pair `(U,V)`. Assume `Z` has density `f_Z` with

`||f_Z||_infinity <= L`,

and `(U,V)` has a joint density `g` with

`||g||_infinity <= M`.

Let `alpha` be real and `beta != 0`, and set

`T = 2 Z U + alpha U^2 + beta V^2`.

Then `T` is absolutely continuous and

`||p_T||_infinity <= 3*2^(2/3) (L M)^(2/3) |beta|^(-1/3)`.

#### Proof

Fix `t` and a splitting radius `r>0`.

On `|U|>r`, integrate in `Z`. Since the derivative of `2ZU` with respect to `Z` is `2U`,

`p_>(t) <= L/(2r)`.

On `|U|<=r`, integrate first in `V`. For fixed `(z,u)`, solving

`t = 2zu + alpha u^2 + beta v^2`

produces at most two roots. Writing

`w = t - 2zu - alpha u^2`,

the two-root Jacobian estimate is

`sum_roots 1/|2 beta v| <= 1/(sqrt(|beta|) sqrt(|w|))`,

and roots exist only on the half-line where `w/beta >= 0`. Therefore

`p_<(t) <= M |beta|^(-1/2) integral_{|u|<=r} integral_{H(u,t)} f_Z(z) |t-2zu-alpha u^2|^(-1/2) dz du`.

For `u != 0`, let `z_0=(t-alpha u^2)/(2u)`. The root condition restricts `z` to one side of `z_0`, hence the one-sided bathtub bound gives

`integral_{one side} f_Z(z)|z-z_0|^(-1/2) dz <= 2 sqrt(L)`.

After the scale factor `(2|u|)^(-1/2)`,

`integral_{H(u,t)} f_Z(z)|t-2zu-alpha u^2|^(-1/2) dz <= sqrt(2L)|u|^(-1/2)`.

Thus

`p_<(t) <= 4 sqrt(2) M sqrt(L) |beta|^(-1/2) sqrt(r)`.

Combining,

`p_T(t) <= L/(2r) + 4 sqrt(2) M sqrt(L) |beta|^(-1/2) sqrt(r)`.

Optimizing in `r` yields

`r_* = 2^(1/3) L^(1/3)|beta|^(1/3)/(4 M^(2/3))`

and exactly

`p_T(t) <= 3*2^(2/3)(LM)^(2/3)|beta|^(-1/3)`.

The possible set `U=0` has probability zero because `(U,V)` has a joint density, so this conditional calculation also proves absolute continuity. QED.

### Why the rank-two logarithm is not being erased

If the transverse square `beta V^2` is removed, the small-`|U|` estimate has no one-sided half-order kernel to integrate. For independent centered unit uniforms the product term `2ZU` has

`p_{2ZU}(t)=log(1/(2|t|))`, `0<|t|<1/2`,

so the rank-two opposite-sign endpoint is genuinely unbounded. The extra square is exactly what replaces the reciprocal scale by an integrable half-order potential.

## 2. Three independent scalars with an invertible zero-diagonal Hessian

### Proposition 2 (`QFORM-ZERODIAG-3SCALAR-v1`)

Let `X_1,X_2,X_3` be independent real random variables with density caps `L_1,L_2,L_3`. Let

`H = [[0,a,b],[a,0,c],[b,c,0]]`

be invertible, and allow an arbitrary affine perturbation

`F = X^T H X + ell^T X + d`.

Then

`||p_F||_infinity <= 3*2^(2/3) (L_1 L_2 L_3)^(2/3) |det H|^(-1/3)`.

#### Proof

Because `H` is invertible, translating the three independent variables by the deterministic vector `(1/2)H^(-1)ell` removes the affine term. Translations preserve independence and all density caps, so it suffices to treat `ell=0`.

Since

`det H = 2abc`,

invertibility implies `abc != 0`. Define

`U = a X_2 + b X_3`,
`V = a X_2 - b X_3`.

The map `(X_2,X_3)->(U,V)` has absolute Jacobian determinant `2|ab|`, hence

`||p_(U,V)||_infinity <= L_2 L_3/(2|ab|)`.

Moreover `X_1` is independent of `(U,V)`, and the quadratic form is exactly

`X^T H X = 2X_1 U + [c/(2ab)](U^2-V^2)`.

Apply Lemma 1 with

`L=L_1`,
`M=L_2 L_3/(2|ab|)`,
`|beta|=|c|/(2|ab|)`.

The powers of `2|ab|` cancel to give

`||p_F||_infinity <= 3*2^(2/3)(L_1L_2L_3)^(2/3)|det H|^(-1/3)`.

QED.

For the normalized product-projection cap `L_1,L_2,L_3<=sqrt(2)`, this becomes

`||p_F||_infinity <= 6*2^(2/3)|det H|^(-1/3) < 9.525 |det H|^(-1/3)`.

The argument is sign-free; negating `H` just reflects the output variable.

## 3. Exact finite null-ray bank compiler

### Theorem 3 (`QFORM-FIVE-NULL-RAY-BANK-COMPILER-v1`)

Let

`A = R M R^T`, `R^T R = I_3`,

be an exact-rank-three real symmetric form, with every nonzero eigenvalue of `M` having magnitude at least `s>0`. Assume every physical diagonal vanishes,

`A_ii=0`,

and the nonzero spectral rows of `R` lie on at most `k` projective lines, where `3<=k<=5`.

Then for arbitrary independent original inputs with one-dimensional density caps at most one,

`||p_(X^T A X)||_infinity <= 6*2^(2/3) * C(k,3)^(1/3) / s`.

In particular for `k<=5`,

`||p_(X^T A X)||_infinity < 20.520/s`.

This holds for both indefinite signatures `(2,1)` and `(1,2)`.

#### Proof

Partition the original coordinates into the `k` disjoint ray banks `I_1,...,I_k`. For bank `a`, choose a Euclidean unit vector `q_a` spanning its projective row direction and write

`r_i = c_i q_a`, `i in I_a`.

Put

`h_a = sum_{i in I_a} c_i^2`,
`u_a = sqrt(h_a) q_a`,
`Y_a = h_a^(-1/2) sum_{i in I_a} c_i X_i`.

The `Y_a` are independent because they depend on disjoint sets of ORIGINAL independent coordinates. Their coefficient vectors have Euclidean norm one. The one-dimensional Rogozin/Ball projection bound therefore gives

`||p_{Y_a}||_infinity <= sqrt(2)`.

Also

`sum_a u_a u_a^T = R^T R = I_3`.

Let `U` be the `k x 3` matrix whose rows are `u_a^T`. Then `U^T U=I_3`, and

`R^T X = U^T Y`,

so

`Q = X^T A X = Y^T B Y`,
`B = U M U^T`.

Because every physical diagonal is zero and each ray is actually represented by a nonzero row,

`q_a^T M q_a=0`.

Hence every diagonal entry of `B` vanishes:

`B_aa = u_a^T M u_a = 0`.

Now apply Cauchy-Binet to `U^T U=I_3`:

`sum_{J subset {1,...,k}, |J|=3} det(U_J)^2 = det(U^T U)=1`.

Therefore some triple `J` satisfies

`det(U_J)^2 >= 1/C(k,3)`.

For that triple,

`B_J = U_J M U_J^T`

is an invertible zero-diagonal `3x3` Hessian and

`|det B_J| = |det M| det(U_J)^2 >= |det M|/C(k,3) >= s^3/C(k,3)`.

Condition on all independent bank variables `Y_a`, `a notin J`. The conditional form in the three remaining independent variables is

`Y_J^T B_J Y_J + ell(Y_{J^c})^T Y_J + d(Y_{J^c})`.

Proposition 2 applies uniformly in the conditioning, with all three density caps at most `sqrt(2)`. Hence

`||p_(Q | Y_{J^c})||_infinity <= 6*2^(2/3)|det B_J|^(-1/3)`

`<= 6*2^(2/3) C(k,3)^(1/3)/s`.

Averaging the conditional densities proves the same unconditional bound. For `k=5`, the numerical constant is

`6*2^(2/3)*10^(1/3) = 20.5197113601...`.

QED.

### Structural interpretation

The theorem explains why an exact finite null-ray cluster does **not** inherit the rank-two logarithm even when one bank becomes a near-coloop and every individual physical pair is tiny. One must aggregate the independent original-coordinate ray banks first. The Cauchy-Binet identity then forces one three-bank determinant to carry a fixed fraction of the full rank-three volume. The selected three bank variables remain independent; after a two-variable linear change, the form is a genuine saddle plus a transverse square, and Lemma 1 supplies the half-order smoothing.

This does not take a supremum over a near-coloop conditional slice. That distinction is essential because the partner counterexample below shows such a supremum can diverge.

## 4. Actual application of the designated partner account02/B11 result

The completed account02/B11 run `20260923T014922Z-account02-B11-QFORM-r19` is pinned at

`yspennstate/math-open-problems@184d15a9de851240ee31f0b62668577956c557bd`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T014922Z-account02-B11-QFORM-r19/REPORT.md`.

That result proves an exact three-projective-null-ray family with nonzero spectrum

`{1,1,-2}`,

and with disjoint-basis mass

`D0 = 2 epsilon(1-epsilon)(1-1/m)^2`,

which can tend to zero while every physical pair is simultaneously small. It also proves that worst-slice conditioning on the dominant null hub has a logarithmically diverging density, even though the full law stays bounded.

Apply Theorem 3 to this **actual partner family**. Here `k=3`, so Cauchy-Binet has only one triple and `|det M|=2`. Keeping the determinant rather than replacing it by `s^3` gives the sharper inequality

`||p_Q||_infinity <= 6*2^(2/3)*2^(-1/3)`

`= 6*2^(1/3)`

`= 7.559526299...`.

Thus

`boxed: ||p_Q||_infinity <= 7.560`

uniformly in `m`, in `0<epsilon<=1/2`, and in every admissible cap-one product law. This exactly reproduces the partner's global constant by a different bank-level compiler and shows explicitly why the bound does not deteriorate as `D0->0`: the ray aggregation is performed **before** paying a reciprocal determinant.

Negating the form gives the same bound for the dual `(1,2)` signature.

## 5. Relation to the five-near-ray theorem and the remaining implication

The previous account01/B11 run proved that in the zero-diagonal exact-rank-three chamber, small positive `D0` forces all but small Lorentz mass into at most five short angular arcs, and every row in a short arc has the exact decomposition

`q(theta0+tau) = cos^2(tau/2) q(theta0) + sin(tau)t(theta0) + sin^2(tau/2)q(theta0+pi)`.

Theorem 3 pays the **zero-width endpoint** of that structure uniformly: any exact union of at most five null rays has a universal density bound, with no leverage gate and no loss as one ray becomes a coloop.

What remains is not a finite-ray counting problem. It is the stability problem in which the tangent and opposite-null aggregates are nonzero and are dependent on the principal null aggregate inside the same original-coordinate bank. Coefficients of those leakage terms may be small, but arbitrary support/moment-free inputs forbid deleting them perturbatively. The partner's r19 family also rules out replacing an averaged near-coloop bank by the worst conditional slice.

The first unpaid implication is therefore

`QFORM-FIVE-NEAR-RAY-TANGENT-STABILITY-v2`:

Given at most five independent original-coordinate angular banks, each confined to a short Lorentz-null arc and carrying the exact principal/tangent/opposite-null decomposition above, prove a density/small-ball bound that is uniform as the arc widths tend to zero, while retaining the within-bank dependence of the three aggregate coordinates. A successful argument should reduce continuously to Theorem 3 at zero width, but must exploit the tangent leakage when it is non-negligible rather than discard it. A complementary pair/ridge/volume certificate is allowed when the leakage creates quantitative transversality.

Arbitrary additional spectrum remains a separate interface to the full target.

## 6. Continuity and full-target status

The arguments above prove existence of an essentially bounded density in the stated exact finite-ray scope. They do **not** establish a continuous representative in full generality. Continuity remains separately open for this theorem and for the unrestricted target.

The full conjecture remains OPEN.

## 7. Source/correction discipline


Repository transport is not native learned-memory ingestion. Status remains `WITHOUT_VERIFIED_BRAIN`.

Manual changed-file review: this report and its checker contain only mathematical derivations, source pins, constants, and nonsecret run metadata. No credentials, private personal data, scheduler IDs, financial/client material, or public-release action is included.
