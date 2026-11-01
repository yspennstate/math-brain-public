# fleet02/B07 — determinant-weighted disjoint-basis / entropy minor selection

**Run:** `20260922T123512Z-b07-qform-minors-11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Coordinate minor selection  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and current corrections

The target is the full arbitrary-product-law statement: for independent real `X_i` with densities `0<=f_i<=1` and real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal `L^infinity` density bound for `X^TAX`, or give a valid counterexample.

This report does not use the refuted law-uniform pointwise Fresnel decay, does not rotate the product law and pretend independence survives, does not use a fiber supremum, and does not infer a bound from one nonzero cross minor. The universal constant `pi` is also not assumed.

Source-pinned peer input actually used: fleet01/B08 `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, `yspennstate/math-open-problems@fce159beaecf924a3e500dc7865ae61f8b35c932`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260922T114116Z-fleet01-B08-qform-r11/REPORT.md`. I reuse its sharp Hausdorff--Young plus rank-one Brascamp--Lieb plus Fresnel inversion mechanism, but replace the leverage exponents by determinant-weighted basis marginals. Its classical analytic source is Brascamp--Lieb (1976), including the Gaussian variational formula for the rank-one BL constant.

The assigned partner is fleet03/B07. At the fresh check, the current `proofnet24/QFORM-density/fleet-2026-09-22/fleet03` tree had no B07 directory and the shared brain had no `memory/fleet03/B07/LATEST.json`; therefore no completed partner theorem was available to apply and none is fabricated.

## 2. Pluecker basis law

Let `U in R^{n x k}` have orthonormal columns and rows `u_i^T`. For every `k`-subset `I`, put

`w_I = det(U_I)^2`.

Cauchy--Binet gives

`sum_{|I|=k} w_I = det(U^T U)=1`.                                    (2.1)

Thus the nonzero coordinate minors define a probability law `w` on coordinate bases.

Let `pi` be any probability distribution on the same nonzero bases and define its inclusion marginals

`p_i = P_{I~pi}(i in I)`.

Then `sum_i p_i=k`. Write

`D(pi||w)=sum_I pi_I log(pi_I/w_I)`.                                 (2.2)

The point is that `pi` may differ from the canonical Pluecker law `w`; this permits us to cap all one-coordinate exponents at `1/2`, while the entropy cost records exactly how much determinant mass had to be reweighted.

## 3. Determinant-weighted Brascamp--Lieb lemma

### Lemma 3.1 (`QFORM-PLUCKER-ENTROPY-BL-v1`)

Assume `0<=p_i<=1/2` for every `i`. For arbitrary independent `X_i` with `0<=f_i<=1`, arbitrary measurable one-coordinate phases `V_i`, and

`a_{i,t}(x)=f_i(x) exp(i t V_i(x))`,

let `mu_t` be the pushforward under `x -> U^T x` of the complex product measure `prod_i a_{i,t}(x_i) dx_i`. Then, uniformly in `t`,

`||hat(mu_t)||_1 <= exp(D(pi||w)/2) (2 pi)^k e^{k/2}`.                (3.1)

#### Proof

For `p_i=0`, use `|hat a_{i,t}|<=||a_{i,t}||_1=1` and omit that factor. For positive `p_i`, apply rank-one Brascamp--Lieb to the linear maps `L_i(xi)=<u_i,xi>` with exponents `p_i`, taking

`g_i(s)=|hat a_{i,t}(s)|^{1/p_i}`.

The Gaussian variational formula gives

`BL(U,p)^2 = sup_{r_i>0} [prod_i r_i^{p_i}] / det(sum_i p_i r_i u_i u_i^T)`.

Set `s_i=p_i r_i`. Since

`det(sum_i s_i u_i u_i^T)=sum_I w_I prod_{i in I}s_i`,                (3.2)

weighted AM--GM with weights `pi_I` gives

`sum_I w_I s_I
 = sum_I pi_I (w_I/pi_I) s_I
 >= exp(-D(pi||w)) prod_i s_i^{p_i}`.                                (3.3)

Therefore

`BL(U,p) <= exp(D(pi||w)/2) prod_i p_i^{-p_i/2}`.                    (3.4)

Because `p_i<=1/2`, Beckner Hausdorff--Young in the convention used by fleet01/B08 gives

`||hat a_{i,t}||_{1/p_i}
 <= (2 pi)^{p_i} p_i^{p_i/2}(1-p_i)^{-(1-p_i)/2}`,                  (3.5)

since `||a_{i,t}||_{1/(1-p_i)}<=1`. Multiplying (3.4)--(3.5), the `p_i` powers cancel, `sum_i p_i=k`, and

`-(1-p) log(1-p) <= p`

implies

`prod_i (1-p_i)^{-(1-p_i)/2} <= e^{k/2}`.                            (3.6)

This proves (3.1). QED.

## 4. Density theorem from a balanced minor law

Let `Lambda` be a real symmetric `k x k` matrix with every eigenvalue of absolute value at least one, and put

`Y=(U^T X)^T Lambda (U^T X)+sum_i V_i(X_i)`.

Using (3.1) in the same Gaussian-regularized Fresnel inversion as fleet01/B08 gives

`|phi_Y(t)| <= min(1, exp(D/2) (pi e/|t|)^{k/2})`.                  (4.1)

For `k>=3`, the crossover is

`t0 = pi e exp(D/k)`,

and integration yields the explicit density bound

`||p_Y||_infinity <= e exp(D/k) k/(k-2)`.                            (4.2)

In particular for the assigned three-direction case,

`boxed{ ||p_Y||_infinity <= 3 e exp(D(pi||w)/3). }`                  (4.3)

This is a dimension-free coordinate-minor averaging criterion. It strictly extends the previous raw-leverage sufficient condition: the analytic exponents are the marginals of a reweighted coordinate-basis law, not necessarily `||u_i||^2`.

A useful special case is a subfamily `B0` of coordinate triples with total Pluecker mass

`eta=sum_{I in B0} w_I`.

If the normalized restriction `pi_I=w_I/eta` on `B0` has every inclusion marginal at most `1/2`, then `D(pi||w)=log(1/eta)` and

`||p_Y||_infinity <= 3 e eta^{-1/3}`.                                (4.4)

So no individual principal minor has to be large: a constant total mass of suitably balanced minors is enough.

## 5. Canonical disjoint-basis construction

Define the exact determinant-weighted disjointness mass

`delta = sum_{I cap J = empty} w_I w_J
       = P_{I,J iid~w}(I cap J=empty)`.                              (5.1)

If `delta>0`, condition an independent pair `(I,J)` of Pluecker bases on `I cap J=empty`, and let `pi` be the first marginal. By symmetry the first and second marginals coincide. For every coordinate `i`, the two disjoint bases cannot both contain `i`, hence

`2 p_i = P(i in I | disjoint)+P(i in J | disjoint) <=1`.            (5.2)

Thus `p_i<=1/2` automatically. Writing

`r_I=sum_{J: J cap I=empty} w_J`,

we have `pi_I=w_I r_I/delta`, and since `r_I<=1`,

`D(pi||w)=sum_I pi_I log(r_I/delta) <= log(1/delta)`.                (5.3)

Therefore for `k=3`,

`boxed{ ||p_Y||_infinity <= 3 e delta^{-1/3}. }`                     (5.4)

This is the requested determinant-weighted selection mechanism: the relevant quantity is not the largest tiny coordinate minor, but the total weight of *pairs of disjoint coordinate bases*.

There is also an exact complementary-minor identity. For each basis `I`,

`r_I = sum_{J subset I^c, |J|=3} det(U_J)^2
     = det(sum_{j notin I} u_j u_j^T)
     = det(I_3-U_I^T U_I)`.                                         (5.5)

Hence

`delta = sum_I det(U_I)^2 det(I_3-U_I^T U_I)`.                      (5.6)

So `delta` is an intrinsic determinant-weighted average of the residual spectral covariance after deleting a coordinate triple.

## 6. Small-delta branch gives an actual three-coordinate localized flag

Equation (5.6) also turns failure of the disjoint-basis smoothing into a sharp localization statement. Since `delta=sum_I w_I r_I` and `sum_I w_I=1`, some coordinate basis `I` satisfies

`r_I=det(S_I) <= delta`,

where

`S_I=sum_{j notin I} u_j u_j^T = I_3-U_I^T U_I`.                    (6.1)

If `s_1<=s_2<=s_3<=1` are the eigenvalues of `S_I`, then

`s_1^3 <= s_1 s_2 s_3 = det(S_I) <= delta`,

so for some unit spectral vector `v`,

`sum_{j notin I} |<u_j,v>|^2 = v^T S_I v <= delta^{1/3}`.           (6.2)

Equivalently, the same spectral direction has coordinate energy at least

`sum_{j in I}|<u_j,v>|^2 >= 1-delta^{1/3}`                           (6.3)

on only three physical coordinates.

Taking the concrete threshold `delta=1/8`, either

* `delta>=1/8`, in which case (5.4) gives the explicit bound `||p_Y||_infinity<=6e` on the exact-rank/separable-residual branch; or
* `delta<1/8`, in which case one spectral direction has more than half of its coordinate energy on a single three-coordinate block.

This improves the previous B07 `<=47` heavy-row flag on this branch: the determinant-weighted disjointness average either pays the Fourier smoothing cost directly or produces an actual three-coordinate localization witness.

## 7. Stress controls and limitation

The previous exact family with one perfectly localized row `e_1` and two diffuse coordinate clouds has every nonzero Pluecker basis containing the `e_1` row. Hence `delta=0`, so (5.4) correctly refuses to claim a diffuse density bound and (6.3) identifies perfect one-direction localization.

Conversely, in genuinely spread frames, `delta` can be positive even when an individual basis weight is arbitrarily small; this is exactly the high-cardinality regime for which fixed-principal-minor selection fails.

The theorem still inherits the separable-residual interface from fleet01/B08. For a fully arbitrary target matrix written `A=U Lambda U^T+C` with `CU=0`, the phase `x^T Cx` is generally nonseparable in the original coordinates, and (3.1) cannot simply absorb it. Therefore this is not a full proof.

## 8. Conditional end-to-end route and first unpaid implication

A compact route is now:

1. choose three large spectral directions and form their coordinate Pluecker law `w`;
2. compute/use the disjointness mass `delta` from (5.6);
3. if `delta` is bounded below, the determinant-weighted entropy BL theorem supplies dimension-free smoothing without selecting one large minor;
4. if `delta` is small, use (6.3) to reduce to a genuinely three-coordinate localized spectral direction plus the remaining two spectral directions;
5. combine that finite-coordinate localized direction with a source-valid two-direction mechanism while retaining arbitrary product laws and the nonseparable spectral complement.

The first unpaid B07 implication is therefore

`QFORM-THREECOORD-LOCALIZED-HYBRID-v1`:

> Given a selected three-dimensional large spectral subspace with a unit direction carrying at least `1-epsilon` of its coordinate energy on three original coordinates, prove a dimension-free small-ball/density estimate by combining those three physical coordinates with the complementary two spectral directions, uniformly over arbitrary symmetric residual coupling; or construct a valid counterexample.

The exact family `e_1 +` two diffuse coordinate clouds is a mandatory control. The separate global interface `QFORM-DIFFUSE-RESIDUAL-COUPLING-v1` remains unpaid.

## 9. Classification

`ESSENTIAL_STEP_APPLIED`: determinant weights are carried through a genuine basis-law Brascamp--Lieb argument. The exact disjoint-basis mass `delta` gives a dimension-free density bound when positive at constant scale, and its failure yields a three-coordinate localization witness.

`FULL_TARGET_OPEN`: the localized/diffuse hybrid with arbitrary nonseparable residual coupling is still missing. No target-level counterexample or complete universal proof is claimed.

No mathematical code was used in this run; all displayed identities are analytic derivations.