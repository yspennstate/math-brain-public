# account01/B08 — conditional whitening and a diffuse-or-localized rank-three dichotomy

**Run:** `20260922T123722Z-account01-B08-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** diffuse eigenvector case  
**Outcome:** `ESSENTIAL_STEP_APPLIED / CONDITIONAL-WHITENING-CERTIFICATE`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**.

## 1. Exact scope and dependencies

The live target is the full universal statement: for arbitrary independent real coordinates with probability densities `0<=f_i<=1` and arbitrary real symmetric `A` with at least three eigenvalues of magnitude at least one, prove a dimension-free density bound for `X^T A X`, or give a valid counterexample. No moment, support, log-concavity, identical-law, or post-rotation independence hypothesis is introduced here.

Fresh source corrections were consumed, including the failures of law-uniform pointwise quadratic stationary-phase decay, unrestricted fiber-sup integration, cross-minor-only closure, and the claimed universal constant `pi`. None of those claims is used below.

The named partner result actually applied is account02/B08, theorem `QFORM-DIFFUSE-RANK3-BL-v1`, canonical source

`yspennstate/math-open-problems@0b5925a458d36c1ec1cf8ab344c9676260a97c8a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T113624Z-qform11/REPORT.md`.

Its proof gives the following determinant-scaled form, by the identical Hausdorff--Young / geometric Brascamp--Lieb / Fresnel calculation: if `V` has `k>=3` orthonormal columns, all row leverages are at most `1/2`, and `M` is real symmetric invertible, then for independent coordinate densities bounded by one,

`Z=(V^T X)^T M (V^T X)`

has a bounded continuous density satisfying

`||p_Z||_infinity <= [e k/(k-2)] |det M|^(-1/k)`.                         (1.1)

The same statement allows deterministic translations of the independent coordinates; equivalently, it applies to `(V^T X+a)^T M(V^T X+a)`. The previously proved account01/B08 separable-phase extension also allows arbitrary coordinate-separable perturbations without changing (1.1).

## 2. Main theorem: conditional-whitened diffuse frame

### Theorem 2.1 — `QFORM-CONDITIONAL-WHITENED-DIFFUSE-v1`

Let `U` be an `n x k` real matrix with orthonormal columns, `k>=3`, and let `Lambda` be real symmetric and invertible. Let `H` be any set of original coordinates, put `L=H^c`, and write `U_H,U_L` for the corresponding row restrictions. Define

`S_H = U_L^T U_L = I_k-U_H^T U_H`.

Assume `S_H` is positive definite and that the **conditional normalized leverages**

`ell_i(H) := u_i^T S_H^(-1) u_i`, `i in L`,                              (2.1)

obey

`max_{i in L} ell_i(H) <= 1/2`.                                          (2.2)

For independent real `X_i` with densities bounded by one, the exact-rank form

`Q=(U^T X)^T Lambda (U^T X)`

has a bounded continuous density and

`boxed{ ||p_Q||_infinity <= [e k/(k-2)] [det(S_H)|det Lambda|]^(-1/k). }`   (2.3)

More generally, (2.3) remains valid after adding arbitrary measurable coordinate-separable terms `sum_i V_i(X_i)`.

### Proof

Condition on `X_H`. Write

`m=U_H^T X_H`.

The remaining coordinates are still independent with their original density caps, and

`Q=(U_L^T X_L+m)^T Lambda (U_L^T X_L+m)`.                               (2.4)

Whiten the surviving frame by setting

`V=U_L S_H^(-1/2)`.

Then

`V^T V=S_H^(-1/2) U_L^T U_L S_H^(-1/2)=I_k`,                           (2.5)

and its row leverage is exactly

`||v_i||^2=u_i^T S_H^(-1)u_i=ell_i(H)<=1/2`.                            (2.6)

Also put

`a=S_H^(-1/2)m`,
`M=S_H^(1/2) Lambda S_H^(1/2)`.

Since `U_L^T=S_H^(1/2)V^T`, equation (2.4) becomes

`Q=(V^T X_L+a)^T M(V^T X_L+a)`.                                        (2.7)

Because `V^T V=I_k`, translate the **original independent coordinates** by the deterministic vector `Va`:

`X'_L=X_L+Va`.

The coordinates of `X'_L` remain independent, each density is merely translated and hence remains bounded by one, and

`V^T X'_L=V^T X_L+a`.                                                    (2.8)

Thus the partner diffuse theorem (1.1) applies conditionally, with the same bound for every value of `X_H`. Finally

`|det M| = det(S_H) |det Lambda|`.                                      (2.9)

This proves the conditional version of (2.3). Averaging the conditional laws preserves the same interval domination / `L^infinity` bound.

For continuity, the partner proof supplies the conditional characteristic-function envelope

`|phi_{Q|X_H}(t)| <= min(1, C_H |t|^(-k/2))`,                           (2.10)

where `C_H` depends only on `S_H,Lambda,k`, not on the realized value of `X_H`. Therefore the unconditional characteristic function is dominated by the same integrable function for `k>=3`; Fourier inversion gives a bounded continuous density.

If coordinate-separable terms are present, conditioning and the translation `X_L -> X'_L` merely replace each surviving `V_i` by another one-variable measurable function. The account01/B08 separable-phase extension therefore gives exactly the same estimate. `QED`.

### Rank-three consequence

If `k=3` and the three nonzero eigenvalues of `Lambda` have magnitude at least one, then `|det Lambda|>=1`, hence

`boxed{ ||p_Q||_infinity <= 3e det(S_H)^(-1/3). }`                      (2.11)

In particular, any such conditional-whitening step with `det S_H>=1/8` gives

`boxed{ ||p_Q||_infinity <= 6e. }`                                     (2.12)

This theorem is genuinely stronger than simply requiring the original row leverages `||u_i||^2<=1/2`: a physically heavy row may be conditioned away, after which the surviving spectral frame is renormalized and can become diffuse.

## 3. Exact Pluecker/DPP identities after deleting physical coordinates

Now specialize to `k=3`. For every three-set `I`, define

`w_I=det(U_I)^2`.

Cauchy--Binet gives

`sum_{|I|=3} w_I = det(U^T U)=1`.                                      (3.1)

For a conditioned coordinate set `H`, let `L=H^c`. Then

`boxed{ det S_H = sum_{I subset L, |I|=3} w_I. }`                      (3.2)

Thus `det S_H` is exactly the total Pluecker / determinantal-basis mass surviving deletion of `H`.

For `i in L`, use the matrix determinant lemma:

`det(S_H-u_i u_i^T)=det(S_H)(1-u_i^T S_H^(-1)u_i)`.                    (3.3)

The left-hand side is, again by Cauchy--Binet, the sum of `w_I` over triples contained in `L\{i}`. Subtracting this from (3.2) yields the exact identity

`boxed{
ell_i(H)
 = [sum_{I subset L, i in I} w_I] / [sum_{I subset L} w_I].
}`                                                                        (3.4)

So the conditional normalized leverage is literally the conditional inclusion probability of coordinate `i` under the rank-three projection DPP, conditioned on avoiding `H`. This gives a clean probabilistic interpretation of the analytic threshold `ell_i<=1/2`.

The same determinant lemma gives the exact update rule after conditioning one more coordinate:

`boxed{ det S_{H union {i}} = det S_H (1-ell_i(H)). }`                 (3.5)

## 4. A finite diffuse-or-localized dichotomy

### Theorem 4.1 — `QFORM-RANK3-DIFFUSE-OR-3COORD-LOCALIZATION-v1`

For every `n x 3` orthonormal frame `U`, there exists a set `H` of at most three original coordinates for which one of the following alternatives holds.

**(A) Conditional diffuse closure.**

`S_H` is positive definite,

`det S_H >=1/8`, and

`max_{i notin H} u_i^T S_H^(-1)u_i <=1/2`.                             (4.1)

Consequently every exact-rank-three quadratic form `U Lambda U^T` with all `|lambda_j|>=1` satisfies

`||p_Q||_infinity <=6e`,                                                (4.2)

and its density is continuous.

**(B) Three-coordinate spectral localization.**

There is a set `H`, `|H|<=3`, and a unit vector `v in R^3` such that

`boxed{ sum_{i in H} |u_i dot v|^2 >1/2. }`                            (4.3)

Equivalently, at most three physical coordinates contain more than half the squared mass of some spectral direction.

### Proof

Start with `H=empty`, so `S_H=I` and `det S_H=1`. As long as `det S_H>=1/8`, inspect the normalized leverages (2.1).

If all are at most `1/2`, stop: alternative (A) holds.

Otherwise choose an `i` with `ell_i(H)>1/2` and add it to `H`. By (3.5),

`det S_{H union {i}} < (1/2) det S_H`.                                 (4.4)

After three such deletions the determinant is strictly below `1/8`; therefore the procedure terminates after at most three deletions.

If it terminates because `det S_H<1/8`, then `S_H=I-U_H^T U_H` is positive semidefinite. If all three eigenvalues of `S_H` were at least `1/2`, their product would be at least `1/8`; hence there exists a unit vector `v` with

`v^T S_H v<1/2`.

Therefore

`sum_{i in H}|u_i dot v|^2
 = v^T U_H^T U_H v
 = 1-v^T S_H v
 >1/2`,                                                                  (4.5)

which is (B). The singular case `det S_H=0` is included. `QED`.

### Interpretation

This gives a deterministic bridge between the global diffuse theorem and local-coordinate mechanisms. There is no uncontrolled dimension-dependent search: after at most three exact determinant-loss steps, either the partner's Fourier--Brascamp--Lieb theorem closes the form with constant `6e`, or the remaining obstruction has a certified spectral direction concentrated by more than one half on at most three original coordinates.

This does **not** itself close alternative (B), especially in the indefinite case; it is a quantitative localization certificate to be handed to the local Schur/pivot workers.

## 5. Direct application to the existing heavy-row gap

The account01/B10 heavy-row theorem conditions/completes a leverage-heavy row and closes the branch when the Schur residual is diffuse and `|alpha|=|e^T Lambda e|>=1/2`. Its difficult residual-diffuse branch includes `|alpha|<1/2`, where strong spectral cross-coupling is present.

Theorem 2.1 closes an overlapping but different part of that branch **without any condition on `alpha`**. If a row `i` has leverage

`c=||u_i||^2>1/2`,

condition on `X_i`. Then

`S=I-u_i u_i^T`, `det S=1-c`.                                         (5.1)

If the normalized residual leverages

`u_j^T S^(-1)u_j <=1/2` for all `j!=i`,                               (5.2)

then

`boxed{ ||p_Q||_infinity <=3e[(1-c)|det Lambda|]^(-1/3). }`             (5.3)

Hence if additionally `c<=7/8` and `|det Lambda|>=1`,

`boxed{ ||p_Q||_infinity <=6e, }`                                     (5.4)

regardless of whether `alpha` vanishes or is small. This is a genuine extension of the current heavy-row decision tree: it uses conditioning plus frame whitening instead of division by the scalar pivot `alpha`.

If (5.2) fails, a second **conditionally heavy** coordinate appears, which is exactly the structural input needed by the heavy-pair / localized branch rather than another diffuse iteration.

## 6. Why this still does not prove the full conjecture

There are two separate remaining gaps.

1. **Localized exact-rank-three branch.** Alternative (B) of Theorem 4.1 gives a strong, finite physical localization certificate, but a source-valid universal output-density estimate for every indefinite matrix satisfying only (4.3) has not yet been derived. Existing local principal-block, binary-indefinite, hyperbolic-square, and Schur mechanisms cover substantial subbranches but not yet this entire certificate.

2. **Additional spectral directions.** The target permits an arbitrary symmetric residual beyond any chosen three large eigendirections. For a decomposition

`A=U Lambda U^T+C`, `CU=0`,

the residual phase `x^T Cx` is generally nonseparable in the original coordinates. The conditional-whitening theorem does not restore one-dimensional factorization for this arbitrary residual. Treating it as independent noise would be invalid.

Thus the full QFORM conjecture remains open.

## 7. First unpaid implication

The new first B08 implication is

`QFORM-3COORD-LOCALIZATION-TO-PIVOT-v1`:

> In the exact-rank-three indefinite case, start from a set `H`, `|H|<=3`, and a spectral unit direction `v` satisfying `sum_{i in H}|u_i dot v|^2>1/2`. Prove that one of the existing source-valid local smoothers (nonsingular principal triple, hyperbolic square, majority-pivot indefinite Schur, or a conditional-whitened diffuse residual) applies with a universal quantitative parameter; or derive a new local estimate that closes the remaining configuration.

After exact rank three is closed, the separate target-level implication is to make this dichotomy stable under an arbitrary additional spectral residual `C`.

## 8. Checks and status

The identities (3.1)--(3.5) were independently checked numerically on random orthonormal frames of sizes `n=6,8,12`: total Pluecker mass was one to floating precision; `det S_H` matched the surviving Pluecker mass; every conditional leverage matched its conditional inclusion ratio; and each determinant update matched `1-ell_i(H)` to floating error below `7e-16`. These checks are diagnostic only; the proofs above are exact.

**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`.
