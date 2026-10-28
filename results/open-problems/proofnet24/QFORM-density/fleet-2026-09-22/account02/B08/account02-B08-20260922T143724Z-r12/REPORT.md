# account02/B08 — separator conditioning for diffuse large eigenspaces

**Run:** `account02-B08-20260922T143724Z-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Diffuse eigenvector case`  
**Classification:** `ESSENTIAL_STEP_APPLIED / QFORM-DIFFUSE-SEPARATOR-CONDITIONING-v1`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**.

## 0. Fresh scope and source pins

The target is unchanged: for arbitrary independent real coordinates with probability densities `0<=f_i<=1` and every real symmetric `A` having at least three eigenvalues of absolute value at least `1`, prove one universal bound for the density of `X^T A X`, or give a valid counterexample. No moment, compact-support, identical-law, sign, continuity, or post-rotation-independence hypothesis is added.


Completed mathematics actually consumed:

1. **Named partner account03/B08, block-remainder theorem.** Canonical report `yspennstate/math-open-problems@55d185b63ba44f172d9342b5d89e0875e850e17`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T122924Z-account03-B08-qform-diffuse-v2/REPORT.md`. If `A=R Lambda R^T+C`, `R^TR=I_r`, and `C` is block diagonal in original-coordinate blocks whose selected-frame masses have maximum `mu<1/r`, then

   `||p_Q||_infinity <= [4r/((r-2)(1-sqrt(r mu)))] |det Lambda|^(-1/r)`.

   Its proof uses an actual union-of-physical-blocks cut and the original-coordinate cross-block Fourier theorem, so arbitrary within-block phases are retained.

2. **Named partner account03/B08, optimized full-range diffuse theorem.** Canonical report `yspennstate/math-open-problems@f6bc73f719d1e9dbcaeb06df49913bb84dd274b6`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T142426Z-account03-B08-qform-diffuse-v3/REPORT.md`. This controls matrices whose **entire range projection** has small coordinate leverage, including arbitrary extra small eigenvalues. The present run constructs a source-valid family where that full-range hypothesis fails maximally while a localized-coordinate separator still gives a uniform bound.

3. **Original-coordinate cross-block Fourier theorem.** `yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`, path `proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`. For a physical cut with rank-`r>2` cross block and singular-value product `Delta`, it gives

   `||p_Q||_infinity <= [2r/(r-2)] Delta^(-1/r)`

   and explicitly allows arbitrary added linear and constant terms. This matters after conditioning a separator.

4. **This slot's whitened physical-block theorem.** `yspennstate/math-open-problems@84657e690f8411d99602ddc772b622686c3874ed`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T124007Z-r11/REPORT.md`. If a physical principal block is `D+R Lambda R^T` with `D` diagonal, `M=R^TR`, and the whitened rows of `R M^{-1/2}` have leverage at most `1/2`, then

   `||p_Q||_infinity <= [e r/(r-2)] [det(M)|det Lambda|]^(-1/r)`.

All these source reports preserve the original independent-coordinate product structure.

## 1. First unpaid implication attacked

The preceding full-range diffuse theorem leaves a sharp structural debt. Selecting three diffuse large eigenvectors gives the exact spectral split

`A = R Lambda R^T + C`, `R^T R=I_3`, `C R=0`, `|lambda_j|>=1`,

but the remainder `C` may make the entire range highly localized. One cannot simply discard it, and a dense off-diagonal `C` destroys the coordinatewise phase factorization used by the rank-three diffuse proof.

The first question attacked here is therefore:

> Can localized original coordinates be conditioned away so that the **remaining interaction components** of the spectral remainder are small enough for the partner's block-remainder theorem, while paying exactly the selected-frame mass lost to conditioning?

The answer is yes. The resulting theorem is a quantitative separator/conditioning bridge between the localized and diffuse mechanisms.

## 2. Main theorem: condition a localized separator, then whiten

### Theorem 2.1 — `QFORM-DIFFUSE-SEPARATOR-CONDITIONING-v1`

Let

`A = R Lambda R^T + C`,

where `R` is an `n x r` real matrix with orthonormal columns, `r>2`, and `Lambda` is real symmetric and invertible. Let `H` be any set of **original physical coordinates** and put `T=H^c`. Suppose the principal compression `C[T,T]` is block diagonal for a partition

`T = G_1 union ... union G_m`.

Define

`eta = ||R_H^T R_H||_op`,

`mu = max_k ||R_{G_k}^T R_{G_k}||_op`.

Assume

`eta<1`,

`r mu < 1-eta`.

Then for arbitrary independent real inputs with one-dimensional densities bounded by `1`, the full quadratic form `Q=X^T A X` has a bounded continuous density satisfying

`||p_Q||_infinity
 <= [4r / ((r-2)(1-eta)(1-sqrt(r mu/(1-eta))))]
    |det Lambda|^(-1/r).`                                      (2.1)

No restriction is imposed on `C[H,H]`, `C[H,T]`, the conditioned coordinate values, or the signs of `Lambda`.

### Proof

Condition on the original coordinates `X_H=x_H`. Because the original law is a product law, the coordinates `X_T` remain independent with their original density caps. The conditional polynomial is

`Q_{x_H}(X_T)
 = X_T^T (R_T Lambda R_T^T + C[T,T]) X_T
   + 2 b(x_H)^T X_T + c(x_H)`,                                  (2.2)

for some deterministic `b(x_H),c(x_H)`. The arbitrary cross couplings to `H` have become only linear terms; they do not change the surviving quadratic cross blocks.

Put

`M=R_T^T R_T = I_r - R_H^T R_H`.

By the definition of `eta`,

`M >= (1-eta) I_r`,                                              (2.3)

so `M` is positive definite. Whiten the selected frame on `T`:

`W = R_T M^{-1/2}`,

`Lambda_T = M^{1/2} Lambda M^{1/2}`.

Then

`W^T W=I_r`,

`R_T Lambda R_T^T = W Lambda_T W^T`.                            (2.4)

For each surviving residual block `G_k`, its whitened selected-frame mass is

`W_{G_k}^T W_{G_k}
 = M^{-1/2} R_{G_k}^T R_{G_k} M^{-1/2}`,

hence

`||W_{G_k}^T W_{G_k}||_op
 <= mu/(1-eta) =: mu'.`                                         (2.5)

The hypothesis is exactly `r mu'<1`.

Now apply the named partner theorem `QFORM-DIFFUSE-BLOCK-REMAINDER-v1` to the conditional form (2.2), with selected orthonormal frame `W`, spectral matrix `Lambda_T`, and block-diagonal residual `C[T,T]`. The partner proof passes unchanged in the presence of the conditional affine term because its underlying cross-block Fourier theorem explicitly absorbs arbitrary linear terms into the two self phases. Therefore, uniformly for every `x_H`,

`||p_{Q|X_H=x_H}||_infinity
 <= [4r/((r-2)(1-sqrt(r mu')))] |det Lambda_T|^(-1/r).`          (2.6)

But

`|det Lambda_T| = det(M) |det Lambda|`,                         (2.7)

and (2.3) gives

`det(M) >= (1-eta)^r`.                                          (2.8)

Substituting (2.5), (2.7), (2.8) into (2.6) yields (2.1).

The same partner proof supplies a uniform integrable characteristic-function envelope depending only on the displayed parameters, not on `x_H`. Averaging conditional characteristic functions therefore preserves that envelope. Fourier inversion gives a bounded continuous unconditional density. No conditional density is renormalized and no moment assumption is used. QED.

### Rank-three target corollary

Take `R` to be any three genuine eigenvectors of `A` whose eigenvalues form

`Lambda=diag(lambda_1,lambda_2,lambda_3)`, `|lambda_j|>=1`,

and take `C=A-R Lambda R^T`. Then `C R=0` and `|det Lambda|>=1`. If a separator `H` satisfies the theorem's hypotheses, then

`||p_Q||_infinity
 <= 12 / [(1-eta)(1-sqrt(3 mu/(1-eta)))].`                       (2.9)

Thus arbitrarily large, indefinite, high-rank remainder interactions are permitted on the conditioned separator and inside each surviving block; only the selected-frame mass of the separator and surviving components is paid.

## 3. Delocalized combinatorial corollary

Suppose now the selected three-eigenvector frame is `epsilon`-delocalized:

`max_i ||r_i||^2 <= epsilon`,                                   (3.1)

where `r_i^T` is row `i` of `R`. Let `H` have at most `h` coordinates, and suppose every connected component of the off-diagonal interaction graph of `C[T,T]` has at most `s` coordinates. Taking these components as the blocks `G_k`,

`eta <= tr(R_H^T R_H) <= h epsilon`,

`mu <= s epsilon`.                                               (3.2)

Hence if

`(h+3s) epsilon < 1`,                                           (3.3)

the target rank-three form obeys

`||p_Q||_infinity
 <= 12 / [(1-h epsilon)
          (1-sqrt(3s epsilon/(1-h epsilon)))].`                 (3.4)

This is a genuine localized/diffuse bridge: one may delete a small physical separator even when the residual interaction graph is globally connected before deletion. The bound depends only on the selected large-eigenspace delocalization and the separator/component geometry, never on the magnitudes or signs of the spectral remainder.

A particularly useful case is a **vertex cover**: if every off-diagonal remainder edge touches `H`, then `C[T,T]` is diagonal, so `s=1` in (3.4). In that diagonal-compression subcase the stronger whitened physical-block theorem from this slot's earlier run gives a better estimate whenever

`epsilon/(1-eta) <= 1/2`:

`||p_Q||_infinity
 <= 3e [det(I-R_H^T R_H)|det Lambda|]^(-1/3)
 <= 3e/(1-eta).`                                                (3.5)

Equation (3.5) still permits **arbitrary** `C[H,H]` and `C[H,T]`, because those terms become constants and linear potentials after conditioning.

## 4. Exact source-valid family separating the mechanisms

The next family shows that Theorem 2.1 is not a disguised instance of the partner's latest full-range diffuse theorem, and that conditioning can be essential even for a genuinely spectral remainder.

Take `n=16`. Let `H_16` be the Sylvester Hadamard matrix and let `U` be its first three columns divided by `4`. Thus `U^T U=I_3` and every row has selected-frame leverage

`||u_i||^2=3/16`.                                               (4.1)

Let the separator be the first three rows, denoted again by `H`, and `T=H^c`. Then

`U_H=(1/4) M`,

where

`M=[[1,1,1],[1,-1,1],[1,1,-1]]`.

A direct exact computation gives

`spectrum(U_H^T U_H)={1/16,1/4,1/4}`,                           (4.2)

so

`eta=1/4`,

`det(U_T^T U_T)=(15/16)(3/4)^2=135/256`.                       (4.3)

Because `U_H` is invertible, set

`K=U_T U_H^{-1}`

and define the symmetric residual in the physical `H,T` ordering by

`C = [[K^T K, -K^T],[-K, I_T]].`                               (4.4)

This is an exact genuine spectral remainder:

`C = [-K, I_T]^T [-K, I_T] >=0`,                               (4.5)

and since `U_T=K U_H`,

`C U=0`.                                                        (4.6)

Moreover `rank(C)=13`, so `ker C=range(U)`. Take

`Lambda=diag(1,1,-1)`,

`A=U Lambda U^T+C`.                                             (4.7)

Then `U` consists of actual eigenvectors of `A` with eigenvalues `1,1,-1`; on `U^perp`, `A=C` is positive definite. Consequently `A` is **full rank**. Its entire range projection is therefore the identity, with maximum full-range coordinate leverage `1`. Thus the partner's latest optimized full-range diffuse theorem cannot apply at all.

The residual `C` is also not globally block-decomposable into small physical components: its off-diagonal graph is connected. In particular the unconditioned partner block-remainder theorem sees only one residual component, with selected-frame mass `1`, and its condition `3 mu<1` fails.

After conditioning only the three separator coordinates, however,

`C[T,T]=I_T`                                                     (4.8)

is diagonal. Thus the residual interaction collapses completely. The partner separator theorem (2.9) applies with

`eta=1/4`, `mu=3/16`,

and gives the explicit actual inequality

`||p_Q||_infinity
 <= 12 / [(3/4)(1-sqrt(3/4))]
 = 32(2+sqrt(3))
 = 119.425625842204... .`                                      (4.9)

This is a direct quantitative application of the named account03/B08 block-remainder result after the new conditioning/whitening step.

The stronger diagonal-compression theorem (3.5) is much sharper here. Since every surviving whitened leverage is at most

`(3/16)/(3/4)=1/4<1/2`,                                        (4.10)

it yields

`||p_Q||_infinity
 <= 3e (256/135)^(1/3)
 = 10.093717265270426... .`                                    (4.11)

This family therefore sits in a regime simultaneously excluded by:

- the partner's **full-range** diffuse theorem (`full-range leverage=1`), and
- the partner's **unconditioned block-remainder** theorem (the residual graph is connected),

but is uniformly controlled by conditioning a tiny physical separator and whitening the surviving selected frame.

The exact arithmetic verifier for (4.2)--(4.11) is `verify_separator_family.py` in this immutable run directory; archived output terminates with `QFORM_B08_SEPARATOR_CHECK_PASS`. The checker uses rational arithmetic for all matrix identities. Its floating-point numbers are only displays of the already-proved exact constants.

## 5. General Hadamard hub family

The same construction works for every Sylvester order `n=2^m>=16` using the first three normalized Hadamard columns and the same three row patterns in `H`. The selected leverage is `3/n`, while

`spectrum(U_H^T U_H)={1/n,4/n,4/n}`,

so

`eta=4/n`,

`det(U_T^T U_T)=(1-1/n)(1-4/n)^2`.                             (5.1)

Define `K=U_TU_H^{-1}` and `C` exactly by (4.4). Then `C>=0`, `CU=0`, `C[T,T]=I`, `rank(C)=n-3`, and the residual off-diagonal graph is connected. The full matrix `A=U diag(1,1,-1)U^T+C` is full rank, so the full-range leverage is again `1` for every `n`.

The hybrid partner bound becomes, for `n>13`,

`||p_Q||_infinity
 <= 12 / [(1-4/n)(1-3/sqrt(n-4))],`                            (5.2)

whereas the diagonal-compression sharpening gives

`||p_Q||_infinity
 <= 3e [(1-1/n)(1-4/n)^2]^(-1/3).`                             (5.3)

As `n` tends to infinity, (5.3) tends to `3e`. Thus a spectral remainder may make the total matrix full rank and globally maximally localized while the three selected large eigenvectors remain diffuse enough for a product-preserving localized-conditioning proof.

## 6. What this does and does not close

### Proved in this run

1. `QFORM-DIFFUSE-SEPARATOR-CONDITIONING-v1`, Theorem 2.1: condition an arbitrary localized coordinate separator, whiten the surviving selected large-eigenvector frame, and apply the named partner's block-remainder theorem with an exact determinant-volume payment.
2. The explicit delocalized combinatorial criterion `(h+3s)epsilon<1` and bound (3.4).
3. The vertex-cover/diagonal compression sharpening (3.5), allowing arbitrary outside and cross couplings.
4. A true spectral, full-rank Hadamard hub family on which both unconditioned partner diffuse mechanisms fail their hypotheses but the new conditioned estimate is finite, with exact `n=16` bound (4.11).

### Not proved

- the unrestricted three-large-eigenvalue conjecture;
- existence, for every arbitrary dense spectral remainder, of a separator `H` with simultaneously small selected-frame mass and small post-deletion interaction components;
- any stability principle under small operator-norm remainder perturbations;
- a transfer from delocalization of only the selected eigenspace to small leverage of the entire range.

The latest B12 counterexample to relative `L^infinity` stability under small operator-norm perturbations is consistent with this limitation: the present proof never truncates the remainder by norm.

## 7. First remaining implication

The new boundary is now precise:

`QFORM-DIFFUSE-SEPARATOR-EXTRACTION-v1` — given only a delocalized three-large-eigenvector frame and an arbitrary spectral remainder `C R=0`, either extract a physical separator `H` for which the selected mass `eta` and the post-deletion component mass `mu` satisfy `3mu<1-eta`, **or** exploit the absence of such a separator to obtain a different aggregate cross-block / bank-smoothing certificate directly from the dense residual interaction.

The explicit full-rank Hadamard hub family proves that one must allow full-range leverage `1`; therefore the remaining implication cannot be replaced by another theorem that assumes the entire range projection is diffuse.

This is a supporting theorem, not a full candidate. Full QFORM remains **OPEN**.
