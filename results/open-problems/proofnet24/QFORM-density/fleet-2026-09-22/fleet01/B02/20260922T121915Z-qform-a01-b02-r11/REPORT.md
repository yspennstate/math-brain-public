# fleet01/B02 — conditional subframe Fourier transfer and finite-heavy reduction

**Run:** `20260922T121915Z-qform-a01-b02-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Integrated Fourier estimate  
**Classification:** `ESSENTIAL_STEP_APPLIED / RANK3_ADVANCE / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport only.

## 0. Exact target and corrections used

The full target remains: independent real `X_i` with densities `0<=f_i<=1`, real symmetric `A` with at least three eigenvalues of absolute value at least one, and a universal bound on the density of `Q=X^TAX`. No moment, support, log-concavity, sign, or eigenbasis-independence assumption is used below.

This report consumes the live corrections `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE`. In particular, no law-uniform one-dimensional pointwise Fresnel estimate is assumed.

The named partner result actually used is fleet02/B02 `QFORM-DELOCALIZED-RANK3-INTEGRATED-FOURIER-v1`, canonical report

`yspennstate/math-open-problems@2d79dea715c2baa9e8ef6c0ac174eee1712d2888:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260922T114331Z-fleet02-B02-qform-r12/REPORT.md`.

It proves the following proof-level resource. If `V` is an `m x 3` frame with `V^T V=I_3` and every row has norm at most `1/2`, and `Z=V^T X` for independent inputs of density at most one, then

`||Phi_Z||_{L^1(R^3)} <= B_RV^3`,                                                    (0.1)

where `B_RV<infinity` is the absolute constant obtained from the small-coordinate Brascamp--Lieb part of Rudelson--Vershynin, IMRN 2015, DOI `10.1093/imrn/rnu243`. The partner then transfers (0.1) through a nondegenerate rank-three quadratic phase.

I also apply the newer fleet02/B02 physical-pivot theorem

`yspennstate/math-open-problems@400f82c8b98fc5623f567581b6ccb0b4298974e8:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/B02-20260922T120900Z-qform-r11/REPORT.md`,

which says that a rank-three original-coordinate cross block with singular-value product `Delta` gives

`||p_Q||_infinity <= 3 sqrt(2) Delta^(-1/3)`.                                      (0.2)

The new work below makes both resources compatible in one exact frame identity and extends the Fourier branch beyond the global `max row <=1/2` hypothesis.

## 1. Conditional subframe theorem

Let the quadratic form have rank exactly three:

`A = U Lambda U^T`, `U^T U=I_3`, `Lambda=diag(lambda_1,lambda_2,lambda_3)`, `|lambda_j|>=1`.

Write `u_i in R^3` for row `i` of `U`. Let `S` be any subset of physical coordinates and define

`M_S = sum_{i in S} u_i u_i^T`.

Assume

1. `M_S` is positive definite;
2. every normalized leverage obeys

`u_i^T M_S^{-1} u_i <= 1/4`, `i in S`.                                             (1.1)

### Theorem 1 (`QFORM-CONDITIONAL-SUBFRAME-FOURIER-v1`)

Under (1.1), for arbitrary independent input densities at most one,

`|phi_Q(t)| <= min(1, K_RV (|det Lambda| det M_S)^(-1/2) |t|^(-3/2))`,             (1.2)

where

`K_RV = B_RV^3/(8 pi^(3/2))`.

Consequently

`||phi_Q||_1 <= 6 K_RV^(2/3) (|det Lambda| det M_S)^(-1/3)`                         (1.3)

and `Q` has a bounded continuous density satisfying

`||p_Q||_infinity <= (3/pi) K_RV^(2/3) (|det Lambda| det M_S)^(-1/3)`.              (1.4)

Since `|det Lambda|>=1`, the right sides may drop this factor.

### Proof

Condition on every coordinate in `S^c`. Independence leaves the variables `(X_i)_{i in S}` independent with their original densities. The conditioned three-dimensional spectral variable has the form

`Y = U_S^T X_S + c`,                                                               (1.5)

where `c` is deterministic under the conditioning.

Put

`v_i=M_S^{-1/2}u_i`, `Z=sum_{i in S} v_i X_i`.

Then

`sum_{i in S} v_i v_i^T = I_3`, and by (1.1), `||v_i||<=1/2`.                       (1.6)

Moreover `U_S^T X_S=M_S^(1/2) Z`. Thus the conditioned phase is

`Q = Z^T B Z + 2 d^T Z + const`,                                                    (1.7)

with

`B=M_S^(1/2) Lambda M_S^(1/2)`, `d=M_S^(1/2)Lambda c`.                              (1.8)

Orthogonally diagonalize `B=R D R^T` and set `W=R^T Z`. The rows of the frame producing `W` are `R^T v_i`; they still resolve the identity and still have norm at most `1/2`. Therefore the partner/Rudelson--Vershynin Fourier-algebra estimate gives

`||Phi_W||_1 <= B_RV^3`.                                                            (1.9)

The linear term in (1.7) is harmless: completing the square translates `W` by a deterministic vector, and translation multiplies its characteristic function by a unimodular phase, leaving (1.9) unchanged. The regularized Fresnel calculation in the partner theorem therefore gives, uniformly in the conditioned value `c`,

`|E[exp(itQ) | X_{S^c}]| <= K_RV |det B|^(-1/2)|t|^(-3/2)`.                         (1.10)

Now

`det B = det(M_S) det(Lambda)`.                                                     (1.11)

Average (1.10) over `X_{S^c}` and combine with the trivial characteristic-function bound one to obtain (1.2).

For completeness, optimize the frequency split instead of fixing `|t|=1`. If

`C_0=K_RV (|det Lambda|det M_S)^(-1/2)`,

then the two bounds cross at `t_0=C_0^(2/3)`, and exactly

`integral_R min(1,C_0 |t|^(-3/2)) dt = 6 C_0^(2/3)`.                               (1.12)

This proves (1.3). Fourier inversion gives (1.4) and a continuous representative. QED.

A useful simplification is `K_RV^(2/3)=B_RV^2/(4pi)`, so (1.3) is equivalently

`||phi_Q||_1 <= (3 B_RV^2/(2pi)) (|det Lambda|det M_S)^(-1/3)`.                     (1.13)

## 2. A deterministic diffuse-versus-finite-heavy dichotomy

Theorem 1 converts a purely deterministic frame certificate into a universal Fourier bound. The next lemma shows that failure of a simple certificate forces one spectral direction to live substantially on only finitely many physical coordinates.

Fix any `c in (0,1)` and define

`L_c={i: ||u_i|| <= sqrt(c)/2}`, `H_c=L_c^c`,

`M_c=sum_{i in L_c} u_i u_i^T`.

Since `sum_i ||u_i||^2=3`, every `i in H_c` contributes more than `c/4`, hence

`|H_c| < 12/c`.                                                                     (2.1)

### Lemma 2 (`QFORM-FRAME-DIFFUSE-OR-FINITE-HEAVY-v1`)

Exactly one of the following useful alternatives occurs.

**Diffuse certificate:** `lambda_min(M_c)>=c`. Then every `i in L_c` obeys

`u_i^T M_c^{-1}u_i <= ||u_i||^2/c <=1/4`,                                          (2.2)

so Theorem 1 with `S=L_c` yields

`||phi_Q||_1 <= 6 K_RV^(2/3)c^(-1)`,                                                (2.3)

and

`||p_Q||_infinity <= (3/pi)K_RV^(2/3)c^(-1)`.                                      (2.4)

**Finite-heavy localization:** `lambda_min(M_c)<c`. Then for some unit vector `v`,

`sum_{i in H_c} <u_i,v>^2 = 1-v^TM_cv > 1-c`,                                      (2.5)

while `|H_c|<12/c`.

The proof is just (2.1)--(2.5), using `sum_i u_i u_i^T=I_3`.

At the concrete choice `c=1/2`, either

`||phi_Q||_1 <= 12 K_RV^(2/3)` and `||p_Q||_infinity <= 6K_RV^(2/3)/pi`,             (2.6)

or fewer than 24 physical coordinates carry more than half of the squared mass of one spectral-frame direction.

This is a genuine reduction of the large-leverage regime: a rank-three obstruction to the integrated-Fourier route cannot remain simultaneously diffuse in all physical coordinates.

## 3. Exact cross-block identity and application of the partner pivot theorem

The newer fleet02/B02 result (0.2) becomes especially transparent for rank three. Let `I` be exactly three physical coordinates, `J=I^c`, and write `U_I` and `U_J` for the corresponding row blocks. Put

`B_{I,J}=A[I,J]=U_I Lambda U_J^T`.

If this cross block has rank three, its singular-value product is

`Delta_{I,J}=sqrt(det(B_{I,J}B_{I,J}^T))`.

Using `U_J^TU_J=I-U_I^TU_I`,

`B_{I,J}B_{I,J}^T = U_I Lambda (I-U_I^TU_I) Lambda U_I^T`,

so the determinant factors exactly:

`boxed(Delta_{I,J}=|det Lambda| |det U_I| sqrt(det(I-U_I^TU_I))).`                  (3.1)

This is the promised structural bridge between physical localization and the residual spectral frame.

Applying the completed partner theorem (0.2) to (3.1) gives the actual inequality

`||p_Q||_infinity <= 3sqrt(2) |det Lambda|^(-1/3)|det U_I|^(-1/3)`

`                         * det(I-U_I^TU_I)^(-1/6)`.                                (3.2)

Thus a balanced triple closes the density problem even when neither the pivot triple nor its complement alone looks maximally favorable. Formula (3.1) also explains the two endpoint failures of this cross-block mechanism: a completely diffuse frame has tiny `det U_I`, while an almost fully localized triple makes the complement determinant tiny. Those endpoints are precisely where the delocalized Fourier theorem or physical principal-block/diagonal mechanisms are supposed to take over.

## 4. Explicit large-row family newly covered by conditionalization

The conditional theorem is not a restatement of the partner's global `max row<=1/2` result. Let `a in (1/2,1)` and `m>=4`, and take rows

`u_0=a e_1`,

`m` rows each equal to `sqrt((1-a^2)/m)e_1`,

`m` rows each equal to `e_2/sqrt(m)`, and

`m` rows each equal to `e_3/sqrt(m)`.

They resolve the identity in `R^3`, but the global frame has a row of norm `a>1/2`, so the partner's delocalized theorem cannot be invoked directly.

Condition on the single variable attached to `u_0` and take `S` to be all other coordinates. Then

`M_S=diag(1-a^2,1,1)`.                                                              (4.1)

After normalization, every row in `S` has norm exactly `1/sqrt(m)<=1/2`, so Theorem 1 gives

`||phi_Q||_1 <= 6K_RV^(2/3)[(1-a^2)|det Lambda|]^(-1/3)`.                           (4.2)

This is a concrete application of the partner's completed Fourier-algebra theorem to a class with a genuine large-leverage physical coordinate. It also shows quantitatively where the remaining atomic endpoint lies: the bound deteriorates only as the residual spectral mass `1-a^2` collapses.

## 5. Compact conditional end-to-end argument and first missing implication

For **rank exactly three**, a complete proof would now follow from a deterministic covering statement saying that every frame falls into one of the currently proved certificates:

1. a conditional diffuse subframe satisfying Theorem 1;
2. a rank-three physical cross block with `Delta` bounded below, handled by fleet02/B02 via (3.2);
3. a physical principal/atomic endpoint covered by the existing localized-coordinate theorems.

Lemma 2 proves the first nontrivial part of such a covering statement: if certificate 1 fails at scale `c`, then fewer than `12/c` physical coordinates capture more than `1-c` of one spectral direction. The **first essential unpaid implication** is therefore finite-dimensional and concrete:

> Starting from the finite-heavy alternative (2.5), prove that either three of those finitely many coordinates plus a residual set produce a cross-block singular product bounded below by an absolute constant, or the same finite set supplies enough atomic quadratic smoothing to compensate the residual two spectral directions.

The exact identity (3.1) is the natural algebraic quantity to track in that step.

For the **full owner target**, even a complete rank-three proof would not yet close arbitrary matrices with additional nonzero eigendirections: one cannot simply convolve a selected rank-three spectral piece with the rest because they depend on the same original coordinates. That dependence-preserving reduction remains separate.

## 6. Status

`ESSENTIAL_STEP_APPLIED`:

* proved the conditional-subframe integrated-Fourier theorem (1.2)--(1.4);
* optimized the partner tail transfer to the determinant-scale bound (1.3);
* proved the finite-heavy/diffuse frame dichotomy (2.1)--(2.6);
* derived the exact rank-three cross-block factorization (3.1) and applied the named partner theorem to obtain (3.2);
* exhibited a genuine `max row>1/2` family covered by the new conditional theorem.

`FULL_TARGET_OPEN`: the concentrated finite-heavy rank-three branch and the reduction from arbitrary additional eigendirections remain unpaid. The scoped theorem proves a **continuous** density; the owner-level continuity conclusion remains open together with the full target.

No pointwise law-uniform one-dimensional decay, Gaussianity, moments, compact support, log-concavity, or rotated-coordinate independence was used.
