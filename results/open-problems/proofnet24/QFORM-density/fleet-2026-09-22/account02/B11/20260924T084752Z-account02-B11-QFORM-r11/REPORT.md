SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-24T08:47:52Z.
attacking: the punctured indefinite collar through the latest partner r53 Schur-difference law; restore the sheared hub as a third source-valid frequency coordinate and quantify exactly how it removes the rank-two logarithmic criticality.

# account02/B11 — three-frequency Schur bathtub in the indefinite collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Continuity: **not proved by this run**.

The unrestricted owner target remains OPEN / NOT PROVED / NOT DISPROVED. No moment, support, log-concavity, iid, diagonal-basis, post-rotation-independence, conditional-cap-as-independence, arbitrary-joint coarea, or two-sheet X-ray-only hypothesis is used.

## 1. Setup and partner input

Let the exact-rank-three active form be

`A = R M R^T`, `R^T R = I_3`,                                  (1.1)

with

`s = min_k |lambda_k(M)| > 0`, `D = |det M|`.                  (1.2)

Fix an ORIGINAL physical coordinate `h` with nonzero pivot

`alpha = A_hh != 0`,                                            (1.3)

and leverage

`q = ||R^T e_h||^2 > 0`.                                       (1.4)

Block

`A = [[alpha,c^T],[c,B]]`,                                     (1.5)

and put

`S_h = B - c c^T/alpha`.                                       (1.6)

In the nondegenerate exact-rank-three branch, `S_h` has rank two. Let `E` have orthonormal columns spanning `range(S_h)`. Take an independent copy `X'` of the original independent cap-one source and write

`U = X-X'`, `U=(U_h,U_I)`.                                     (1.7)

Every `U_j` is independent with cap-one density `mu_j=f_j*tilde f_j`.

The latest completed compatible designated-partner result, account03/B11 r53, is `QFORM-SCHUR-DIFFERENCE-FLATTENING-v1`, canonical mathematics

`yspennstate/math-open-problems@76badd15bb5b007835da3c731f56430bb7eb19b6`.

For

`Z = E^T S_h U_I in R^2`,                                      (1.8)

it proves

`||p_Z||_infinity <= 2/Delta_2(S_h)`,                           (1.9)

where `Delta_2(S_h)` is the product of the two nonzero singular values. The same partner report imports the completed Schur pseudodeterminant identity

`Delta_2(S_h) = q D / |alpha|`.                                (1.10)

The present run spends these two facts at a new source-valid three-dimensional inequality.

## 2. The sheared hub restores a genuine third frequency coordinate

Define the Schur-sheared hub difference

`U_tilde = U_h + c^T U_I/alpha`.                                (2.1)

The exact decoupled Schur phase is

`U^T A V = alpha U_tilde V_tilde + Z dot Y`,                    (2.2)

with `V_tilde=V_h+c^T V_I/alpha` and `Y=E^T V_I`. Equation (2.2) is only algebra; no independence is asserted after this shear.

The important random vector is instead the **frequency coefficient vector**

`Xi = (alpha U_tilde, Z)
    = (alpha U_h + c^T U_I, Z) in R^3`.                         (2.3)

### Theorem 2.1 — `QFORM-SCHUR-THREEFREQUENCY-BATHTUB-v1`

`Xi` has a three-dimensional density satisfying

`boxed: ||p_Xi||_infinity <= 2/(qD).`                           (2.4)

Consequently, uniformly in the center `xi_0 in R^3` and `r>0`,

`boxed: P(||Xi-xi_0|| <= r)
        <= min(1, 8 pi r^3/(3 qD)).}`                           (2.5)

Moreover the inverse-square singularity is uniformly integrable:

`boxed: sup_(xi_0) E ||Xi-xi_0||^(-2)
        <= 4 * 3^(1/3) * pi^(2/3) * (qD)^(-2/3).}`              (2.6)

#### Proof

Put

`C = c^T U_I`.                                                  (2.7)

The pair `(C,Z)` may be highly dependent; no density cap for it is assumed. What matters is that `U_h` is an ORIGINAL-coordinate difference and is genuinely independent of the entire residual difference bank `U_I`. Its density `mu_h` satisfies `mu_h<=1`.

Disintegrate the residual law with respect to `Z`. Conditionally on the residual variables, the first coordinate of `Xi` is

`alpha U_h + C`,                                                (2.8)

so its conditional density is

`x -> |alpha|^(-1) mu_h((x-C)/alpha) <= |alpha|^(-1)`.          (2.9)

Mixing over the residual variables at fixed `Z=z` cannot increase that cap. Therefore, at almost every `(x,z)`,

`p_Xi(x,z) <= |alpha|^(-1) p_Z(z)`.                            (2.10)

Use (1.9) and then (1.10):

`p_Xi(x,z)
 <= 2/(|alpha| Delta_2(S_h))
 = 2/(qD)`.                                                     (2.11)

This proves (2.4). The ball estimate (2.5) is density cap times the volume `4 pi r^3/3`.

For (2.6), let `K=2/(qD)`. For any three-dimensional probability density bounded by `K`, the bathtub/layer-cake estimate gives

`E ||Y-y_0||^(-2)
 <= integral_0^infinity min(1,(4 pi K/3)t^(-3/2)) dt
 = 3^(1/3) (4 pi K)^(2/3).`                                    (2.12)

Substituting `K=2/(qD)` yields

`3^(1/3)(8 pi/(qD))^(2/3)
 = 4*3^(1/3)*pi^(2/3)*(qD)^(-2/3)`,                             (2.13)

as claimed. QED.

## 3. Uniform collar inequality: the small pivot cancels exactly

On the live near-coloop punctured collar used by the B11 programme,

`q >= 63/64`, `0<|alpha|<=s/64`, `D>=s^3`.                     (3.1)

Partner r53 already converts the small pivot into a large Schur area,

`Delta_2(S_h) >= 63 s^2`.                                      (3.2)

The new three-frequency vector has, more strongly,

`boxed: ||p_Xi||_infinity <= 128/(63 s^3),}`                    (3.3)

and

`boxed: sup_(xi_0) E||Xi-xi_0||^(-2)
        <= 12.5052757995... / s^2.}`                            (3.4)

There is **no residual power of `|alpha|`** in either estimate. The shrinkage of the scalar coefficient `alpha U_tilde` is exactly compensated by the `1/|alpha|` growth of the rank-two Schur pseudovolume in (1.10).

This is the quantitative source-preserving version of “the third direction survives the puncture”.

## 4. Rank-two logarithm retained exactly; why three dimensions remove it

The required opposite-sign rank-two control remains literal. If `X,Y` are independent centered unit uniforms, then

`p_(2XY)(t) = log(1/(2|t|)),     0<|t|<1/2`,                    (4.1)

so rank two has an unbounded logarithmic density at the saddle.

The same criticality appears in reciprocal-frequency form. Already for a genuine two-dimensional cap-one product law with density positive near the origin,

`E ||Z||^(-2) = infinity`,                                     (4.2)

because polar integration contains `integral_0 dr/r`. Thus a two-dimensional density cap cannot pay the inverse-square singularity; this is the same logarithmic threshold as (4.1).

The third source direction does **not** first make the rank-two saddle bounded. The new theorem instead adds the genuinely independent hub difference before normalization and forms the three-dimensional coefficient vector `(alpha U_tilde,Z)`. In dimension three,

`integral_(||x||<1) ||x||^(-2) dx < infinity`,                  (4.3)

and (2.6) makes this statement uniform under the exact spectral determinant currency. This is a precise dimension-threshold explanation of how the third direction removes the logarithmic obstruction while preserving the original product provenance.

## 5. Required pinned source applied at an actual sign-specific inequality

The required pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was read at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its completed ruled-level-set Theorem C says that for an exact-rank-three signature `(2,1)` with nonzero eigenvalue magnitudes at least `s`,

`boxed: p_Q(t) <= pi sqrt(2)/s,   t>=0.}`                       (5.1)

For signature `(1,2)`, applying it to `-Q` gives

`boxed: p_Q(t) <= pi sqrt(2)/s,   t<=0.}`                       (5.2)

These are real inequalities on the one-sheet side of the same indefinite chamber. I do **not** transfer them to the opposite two-sheet side: the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction remains binding. The new three-frequency bathtub (2.4)-(2.6) is a source-valid resource aimed specifically at that unpaid side; it is not itself yet a trace bound.

## 6. First unpaid implication

The first unpaid implication is now

`QFORM-SCHUR-3FREQ-MOYAL-COMPILER-v1`:

> Starting from the exact unnormalised independent-copy kernels
> `F_j(u,t)=int f_j(x)f_j(x-u) exp(it(2x-u)) dx`
> and the Schur phase (2.2), prove an `L^1_t` or equivalent linear small-ball estimate whose conditional singular cost is at most `C ||Xi||^(-2)` (or any smaller singularity). Then (2.6) closes the punctured exact-rank-three opposite-two-sheet branch uniformly.

This compiler must aggregate the ORIGINAL sum/difference product kernels before any conditional normalization. It may not replace the residual law by an arbitrary joint density, condition on a rotated same-bank coordinate as if its cap were preserved, or use line/X-ray control alone. The completed Moyal identity for each coordinate kernel and the pinned Fresnel/Brascamp-Lieb machinery are the natural interfaces.

Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate bridge to the full owner target.

## 7. Scope/status

This run proves the source-valid three-frequency density, cubic small-ball, and inverse-square estimates (2.4)-(2.6), and applies the completed ruled theorem on the correct sign side. It does not prove the full density theorem, does not prove the two-sheet trace compiler, and does not claim full continuity.
