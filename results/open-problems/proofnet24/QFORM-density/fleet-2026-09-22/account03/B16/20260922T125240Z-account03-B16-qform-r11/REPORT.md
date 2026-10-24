# account03/B16 — diffuse rank-two L^3 transport and sign-free spectral-row smoothing

**Run:** `20260922T125240Z-account03-B16-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Projection-product interaction  
**Classification:** `ESSENTIAL_SUPPORTING_STEP / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval was authenticated, but no distinct native learned-memory receiver use was verified.

## 1. Exact target and corrections retained

The owner target remains: for independent real `X_i` with scalar densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal finite `L^infinity` bound on the density of `X^TAX`, or produce a valid counterexample.

This run does not use the refuted law-uniform one-dimensional Fresnel decay, does not assume independence after spectral rotation, does not use an unrestricted fiber supremum, does not use a cross minor by itself, and does not condition on a sum/difference variable while pretending its conditional density cap remains one. The live correction `QFORM-UV-CONDITIONAL-CAP-FALSE` is therefore respected.

The exact assigned partner `account04/B16` still had no completed current-QFORM artifact visible at the fresh snapshot, so no result is fabricated. I apply two compatible completed results:

1. **account04/B18**, run `20260922T113729Z-account04-B18-qform-r1`, theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`: a bounded base density plus a conditionally translated scalar square yields an explicit bounded output density without post-translation independence.
2. **account01/B11**, run `QFORM-B11-20260922T121344Z`, lemma `QFORM-DEPENDENT-SQUARE-L3-SMOOTHING-v1`: if a base variable has `L^3` density norm `M` and the translated scalar variable has conditional density cap one, then adding `dV^2` gives `L^infinity` norm at most `4 |d|^{-1/2} M^{3/4}`.

The second result is the exact endpoint needed after the new `L^3` theorem below; the first is applied to the definite residual subcase and supplies the sharper definite-branch constant.

## 2. New theorem: diffuse rank-two projected quadratics are uniformly L^3

### Theorem `QFORM-DIFFUSE-RANK2-L3-SEPARABLE-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1`. Let `U in R^{n x 2}` have orthonormal columns. Write the `i`th row as `u_i^T` and its leverage as

`c_i=||u_i||_2^2`.

Assume

`c_i<=1/2` for every `i`.

Let `B` be any real symmetric invertible `2x2` matrix, and let `V_i:R->R` be arbitrary measurable functions. Then

`Y = sum_i V_i(X_i) + (U^T X)^T B (U^T X)`

is absolutely continuous and its density obeys

`boxed( ||p_Y||_3 <= (3e)^(2/3) |det B|^(-1/3) ).`              (2.1)

No sign-definiteness of `B`, support, moment, centering, smoothness, log-concavity or connected-support assumption is used.

### Proof

Fix `t`. Put

`a_{i,t}(x)=f_i(x) exp(i t V_i(x))`.

Then `|a_{i,t}|=f_i`, `||a_{i,t}||_1=1`, and `||a_{i,t}||_p<=1` for every `p>=1`.

Let `mu_t` be the pushforward under `x -> U^T x` of the finite complex measure with density `prod_i a_{i,t}(x_i)`. Exactly as in the proven diffuse Fourier--Brascamp--Lieb argument of account01/B08, the leverage hypothesis `c_i<=1/2`, sharp one-dimensional Hausdorff--Young, and geometric rank-one Brascamp--Lieb give

`||hat mu_t||_1 <= (2pi)^2 e`.                                  (2.2)

The estimate is uniform in `t` and in all measurable `V_i`.

Let `g_t` denote the bounded continuous density of `mu_t`. The characteristic function of `Y` is

`phi_Y(t)=int_{R^2} exp(i t z^T B z) g_t(z) dz`.                 (2.3)

Using Fourier inversion for `g_t` and the two-dimensional Fresnel identity, for `t!=0`,

`| int_{R^2} exp(i t z^T B z + i xi dot z) dz |
 = pi |t|^(-1) |det B|^(-1/2)`.                                (2.4)

Hence (2.2)--(2.4) imply

`|phi_Y(t)| <= pi e /( |t| sqrt(|det B|) ).`                    (2.5)

Together with `|phi_Y(t)|<=1`, write

`A = pi e / sqrt(|det B|)`

and obtain

`|phi_Y(t)| <= min(1,A/|t|)`.

Therefore

`||phi_Y||_(3/2)^(3/2)
 <= 2[ int_0^A 1 dt + A^(3/2) int_A^infinity t^(-3/2) dt ]
 = 6A`,                                                         (2.6)

so

`||phi_Y||_(3/2) <= (6A)^(2/3)`.                               (2.7)

With the Fourier convention used above, interpolation between `L^1 -> L^infinity` and Plancherel gives the inverse Hausdorff--Young estimate

`||p_Y||_3 <= (2pi)^(-2/3) ||phi_Y||_(3/2)`.                    (2.8)

Combining (2.7) and (2.8) gives exactly

`||p_Y||_3 <= (3e)^(2/3) |det B|^(-1/3)`.

Since `phi_Y in L^(3/2)`, its inverse Fourier transform is an `L^3` function representing the output probability measure, proving absolute continuity. QED.

### Why this is not the refuted pointwise route

The false owner-message intermediate claim concerned one-dimensional arbitrary bounded densities and therefore allows phase-aligned fragmented supports. Here the decay comes only after a genuinely two-dimensional **diffuse product projection** with every row leverage at most `1/2`; the Brascamp--Lieb aggregation happens before the quadratic Fresnel integral. The theorem does not claim a one-dimensional law-uniform decay statement.

## 3. Sign-free spectral-row smoothing when the residual projection is diffuse

Now let

`A=R Lambda R^T`

have exact rank three, with `R^T R=I_3` and invertible symmetric `Lambda`. Write the selected physical row as `v=r_i`,

`ell=|v|^2`,

`a=v^T Lambda v=A_ii`,

and assume `a!=0`.

Let `E` be a `3x2` orthonormal basis for `v^perp`. Put

`K=Lambda-(Lambda v)(Lambda v)^T/a`,

`B=E^T K E`.

As in the already proved spectral-row Schur identity,

`det B = ell det(Lambda)/a`.                                    (3.1)

For `k!=i`, define residual rows

`w_k^T = r_k^T E`.

Then

`sum_{k!=i} w_k w_k^T=I_2`.                                    (3.2)

Assume the new residual-diffuse condition

`max_{k!=i} |w_k|^2 <= 1/2`.                                   (3.3)

Completing the square only in the original independent coordinate `X_i` gives

`Q = a ( X_i + m(Z) )^2 + D(Z)`,                               (3.4)

where

`D(Z)=xi^T B xi`,

`xi=sum_{k!=i} w_k X_k`.

By Theorem 2,

`||p_D||_3 <= (3e)^(2/3) |det B|^(-1/3)`.                       (3.5)

Conditional on `D=r`, the variable `X_i+m(Z)` is a mixture of translates of the original `X_i` law, because `X_i` is independent of all remaining coordinates. Its conditional density is therefore still bounded by one. Applying the completed account01/B11 dependent `L^3` square-smoothing lemma to (3.4) and (3.5) yields

`||p_Q||_infinity
 <= 4 |a|^(-1/2) [ (3e)^(2/3) |det B|^(-1/3) ]^(3/4)`

and hence, using (3.1),

`boxed(
 ||p_Q||_infinity
 <= 4 sqrt(3e) ( ell |det Lambda| |a| )^(-1/4).
)`                                                                  (3.6)

This theorem is **sign-free**: the Schur residual `B` may be definite or indefinite. It therefore pays the majority-pivot branch that the earlier elliptic spectral-row theorem could not pay, whenever the residual product projection is diffuse.

### Definite residual and the account04/B18 partner theorem

If `B` is definite, the two-dimensional product-marginal bound gives

`||p_D||_infinity <= 2pi / sqrt(|det B|)`.

Applying the completed account04/B18 theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` directly to (3.4) gives the sharper bound

`boxed(
 ||p_Q||_infinity
 <= 2 sqrt(2pi) ( ell |det Lambda| |a| )^(-1/4).
)`                                                                  (3.7)

Thus the new mechanism agrees with the existing definite branch and extends it across the indefinite residual by replacing `L^infinity` payment with the exact `L^3 -> L^infinity` smoothing exponent.

## 4. A previously live stress family is now fully paid

Consider the one-heavy-direction / two-delocalized-directions frame from the finite-core stress tests:

- one row is `e_1`;
- `m` rows are `e_2/sqrt(m)`;
- `m` rows are `e_3/sqrt(m)`;
- `m>=2`.

Then `R^TR=I_3`. Take

`Lambda=diag(alpha,beta,-gamma)`,

with `alpha,beta,gamma>=1`.

Choose the heavy row `v=e_1`. Then

`ell=1`, `a=alpha`,

and the residual frame has row leverages exactly `1/m<=1/2`. Its Schur residual is

`B=diag(beta,-gamma)`,

which is indefinite. Formula (3.6) gives

`||p_Q||_infinity
 <= 4 sqrt(3e) (alpha^2 beta gamma)^(-1/4)
 <= 4 sqrt(3e)
 = 11.4226760334... .`                                           (4.1)

This closes **both output sides** of this exact localized-plus-delocalized rank-three family. In particular, the opposite-sign rank-two residual may retain its logarithmic singularity; the heavy third square removes it through the `L^3 -> L^infinity` mechanism rather than by falsely making the rank-two piece bounded.

## 5. Attempted refutation and boundary

The theorem was stress-checked against the three mandatory mechanisms.

1. **Independent coordinate frame `R=I_3`.** After choosing one pivot, the residual `2x2` frame has rows of leverage `1`, so condition (3.3) fails. No false claim is made; local physical-block theorems already cover this localized case.
2. **Flat Walsh frame.** Every residual leverage is small, so the theorem is compatible with the already proved diffuse branch. It does not pay a reciprocal physical minor.
3. **Light-cone pivots.** The constant in (3.6) degenerates as `a=A_ii ->0`. This is a real surviving obstruction: exact-rank-three matrices with trace cancellation can have all physical diagonal entries small or zero. The present theorem does not claim otherwise.

No counterexample was found to Theorem 2 or (3.6), and their proofs expose exactly where each hypothesis is used.

## 6. What changed and what remains

### PROVED in this run

1. `QFORM-DIFFUSE-RANK2-L3-SEPARABLE-v1`: a two-dimensional diffuse product projection followed by any nonsingular quadratic form has a universal `L^3` density bound, even with arbitrary coordinate-separable phases.
2. `QFORM-SPECTRAL-ROW-DIFFUSE-RESIDUAL-v1`: for an exact-rank-three form, **either sign** of the scalar pivot and either inertia of the residual Schur form are paid whenever the residual two-dimensional product projection is diffuse.
3. The exact one-heavy-direction / two-delocalized-directions stress family is fully closed with explicit constant `4 sqrt(3e)<11.423`.
4. The account04/B18 dependent-square theorem is applied to the definite residual subcase; the account01/B11 `L^3` square-smoothing theorem is applied to the indefinite residual extension.

### OPEN

The full owner conjecture remains OPEN. The first target-relevant unpaid implication is now narrower:

> In an exact-rank-three localized branch, if every useful scalar pivot either lies near the spectral light cone (`|A_ii|` small) or leaves a residual two-frame containing one or more leverage `>1/2` rows, aggregate those at most three residual-heavy coordinates with the pivot **before** paying reciprocal local determinants. Then make the resulting rank-three argument stable under arbitrary additional spectral components of the full matrix.

Because a two-dimensional orthonormal frame has total leverage `2`, there can be at most three rows with leverage strictly greater than `1/2`. Thus the obstruction after this run is a genuinely finite residual core, not a diffuse high-cardinality cloud.

The next mechanism should be a finite-core hybrid theorem for those at most three residual-heavy coordinates plus the diffuse remainder; repeating the previous near/far fixed-principal-block estimate would not address the new residual.

**Full QFORM conjecture: OPEN / NOT PROVED.**
