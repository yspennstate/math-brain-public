SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B05, 2026-09-24T01:58:48Z.
attacking: the surviving exact-rank-three isotropic shear; put it into an exact physical Witt normal form, compile the aggregate determinant star into one scale-invariant curvature product, and pay the moderate-coloop/diffuse-residual subbranch.

# fleet01/B05 auto11 — physical Witt compiler for the isotropic-shear survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Assignment:** quadratic coarea / equivalent interval bound preserving arbitrary product densities.  
**Status:** `NEW_STRUCTURAL_THEOREM_PROVED / MODERATE-COLOOP_DIFFUSE-RESIDUAL_BRANCH_PAID / DESIGNATED_PARTNER_CURRENCY_APPLIED / FULL_QFORM_OPEN`.  
**Regularity:** essential boundedness is proved only in the stated paid branch. Full-target continuity remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Starting point and first unpaid implication

The preceding B05 run reduced the exact-rank-three high-leverage zero-pivot problem to the single survivor

`A=[[0,l^T],[l,C]],  rank(A)=rank(C)=3,  l in Ran(C),  l^T C^+ l=0`,

or equivalently

`Q(H,Z)=(Z+Hw)^T C(Z+Hw),  w=C^+l,  w^T Cw=0`.

The generic arbitrary-joint coarea estimate is false, so the remaining proof has to retain the original product provenance of the shear. This run derives an exact physical/spectral normal form which makes the surviving dependence one-dimensional and exposes all usable determinant currency before any conditioning.

## 2. Exact physical Witt normal form

### Theorem 2.1 — `QFORM-ISOTROPIC-SHEAR-WITT-CURRENCY-COMPILER-v1`

Let `A` be a real symmetric matrix of rank exactly three. Write

`A=R M R^T,  R^T R=I_3`,

where `M` is an invertible real symmetric `3 x 3` matrix. Fix an original coordinate `i`, let `r_i^T` be the `i`th row of `R`, and put

`c=||r_i||_2^2`.

Assume

`A_ii=0,   0<c<1`,

and that the complementary principal block `C=A_{-i,-i}` has rank three. Then, after an orthogonal change of basis **inside the three-dimensional spectral subspace only** (no probabilistic independence claim), there are real numbers

`beta !=0, alpha, gamma, delta !=0`

such that

`r_i=(sqrt(c),0,0)`

and

`M = [[0,beta,0],
      [beta,alpha,gamma],
      [0,gamma,delta]].`                                             (2.1)

Moreover

`det M=-beta^2 delta`,                                               (2.2)

so if

`Delta_3=|det M|`

is the product of the three nonzero eigenvalue magnitudes of `A`, then

`Delta_3=beta^2 |delta|`.                                            (2.3)

Write the three columns of `R` after deleting row `i` as residual coefficient vectors `x,y,z`. Then

`||x||_2^2=1-c,   ||y||_2=||z||_2=1`,
`<x,y>=<x,z>=<y,z>=0`.                                               (2.4)

Hence, with `tau=sqrt(1-c)` and independent original inputs `X`, define the literal heavy coordinate

`H=X_i`

and residual linear forms

`U=tau^{-1} x^T X_{-i},  V=y^T X_{-i},  W=z^T X_{-i}`.               (2.5)

Then `(U,V,W)` are three orthonormal linear projections of the residual original-coordinate product law; they are **not asserted independent**, while `H` is genuinely independent of the entire residual triple. The quadratic form is exactly

`boxed{
 Q=2 beta sqrt(c) H V
   +2 beta sqrt(1-c) U V
   +alpha V^2+2 gamma V W+delta W^2.
}`                                                                    (2.6)

Equivalently, if

`a=beta sqrt(c),  kappa=sqrt((1-c)/c)`,                              (2.7)

then

`boxed{
 Q=2a V(H+kappa U)+alpha V^2+2gamma V W+delta W^2,
 0<kappa<infinity.
}`                                                                    (2.8)

In the high-leverage chamber `c>1/2`, one has `0<kappa<1`.

### Proof

Rotate the three-dimensional spectral basis so that `r_i=(sqrt(c),0,0)`. Since

`A_ii=r_i M r_i^T=c M_11=0`,

we have `M_11=0`. Rotate only the last two spectral coordinates so that the vector `(M_12,M_13)` becomes `(beta,0)`. If `beta=0`, then the first row and column of `M` would vanish, contradicting invertibility. Thus `beta!=0`, and the matrix has form (2.1). Direct expansion gives

`det M=-beta^2 delta`;

therefore `delta!=0`, proving (2.2)-(2.3).

Because `R^T R=I_3`, deleting the row `(sqrt(c),0,0)` leaves residual column Gram matrix

`diag(1-c,1,1)`,

which is exactly (2.4). Substituting the spectral linear coordinates

`S=sqrt(c)H+sqrt(1-c)U,  V,  W`

into `[S,V,W] M [S,V,W]^T` gives (2.6), and (2.8) follows from (2.7). QED.

## 3. Exact curvature conservation: star mass versus residual pseudodeterminant

### Theorem 3.1 — `QFORM-ISOTROPIC-SHEAR-CURVATURE-SPLIT-v1`

Under Theorem 2.1, let

`S_i=sum_{T: |T|=3, i in T} |det A_T|`                               (3.1)

be the aggregate principal-determinant star through the heavy physical coordinate. Let

`Delta_C`

be the product of the absolute values of the three nonzero eigenvalues of the complementary rank-three block `C`. Then

`boxed{ S_i = c Delta_3 = c beta^2 |delta| = a^2 |delta|, }`          (3.2)

`boxed{ Delta_C=(1-c) Delta_3, }`                                    (3.3)

and therefore

`boxed{ S_i+Delta_C=Delta_3. }`                                      (3.4)

### Proof of the star identity

For residual physical rows

`r_j=(x_j,y_j,z_j),  r_k=(x_k,y_k,z_k)`,

Cauchy-Binet at the literal physical triple gives

`det A_{\{i,j,k\}}=det(M) det([r_i;r_j;r_k])^2`.

Since `r_i=(sqrt(c),0,0)`,

`det([r_i;r_j;r_k])=sqrt(c)(y_j z_k-y_k z_j)`.

Hence

`|det A_{\{i,j,k\}}|
 =c Delta_3 (y_j z_k-y_k z_j)^2`.

Summing over `j<k` and using the two-dimensional Cauchy-Binet identity together with `||y||=||z||=1`, `<y,z>=0`, gives

`sum_{j<k}(y_j z_k-y_k z_j)^2=1`,

which proves `S_i=c Delta_3`. Combining with `a=beta sqrt(c)` and (2.3) proves the last equality in (3.2).

This is exactly the designated partner fleet02/B05 cofactor/star currency `S_i=c_i Delta_3`, now applied to the actual isotropic-shear survivor and resolved into the concrete Witt coefficients `a,delta`.

### Proof of the residual pseudodeterminant identity

Let

`D=diag(sqrt(1-c),1,1)`

and let `R_0` be the normalized residual frame whose rows are

`(x_j/sqrt(1-c), y_j,z_j)`.

Then `R_0^T R_0=I_3` and

`C=R_0 (D M D) R_0^T`.                                               (3.5)

The three nonzero eigenvalues of `C` are therefore exactly the eigenvalues of the symmetric `3 x 3` matrix `DMD`. Consequently

`Delta_C=|det(DMD)|=(1-c)|det M|=(1-c)Delta_3`,

which proves (3.3), and (3.4) is immediate. QED.

### Target-normalized consequence from the designated partner currency

If the three nonzero eigenvalues of `A` satisfy the target normalization `|lambda_j(A)|>=1`, then `Delta_3>=1`. In the high-leverage chamber `c>=1/2`, the actual partner-star inequality becomes

`boxed{ a^2 |delta| = S_i = c Delta_3 >= 1/2. }`                      (3.6)

Thus the remaining isotropic-shear problem has **no loss of total third-order curvature** as `c->1`: the hub slope and transverse square satisfy a fixed scale-invariant product. What degenerates is only the source-sharing coefficient

`kappa=sqrt((1-c)/c)`.                                                (3.7)

At the formal endpoint `kappa=0`, the completed fleet02/B05 theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` applied to `L=aV` and transverse variable `W` gives

`||p_Q||_(infinity,ess)
 <= 7.761982175235 (2/|a|)^(2/3)|delta|^(-1/3)
 =12.3213786703265 (a^2|delta|)^(-1/3),`                              (3.8)

so (3.6) would give `<15.524`. For every genuine survivor `0<c<1`, however, the extra shared term `2a kappa U V` remains and cannot be discarded as a small perturbation under the allowed arbitrary unbounded input laws.

Equation (3.8) is included only as the exact paid endpoint and partner application; it is not asserted for `kappa>0`.

## 4. A new paid branch: moderate coloop plus diffuse normalized residual frame

The normal form also gives a second genuine exit before the hard `kappa->0` endpoint.

### Theorem 4.1 — `QFORM-ISOTROPIC-SHEAR-MODERATE-DIFFUSE-RESIDUAL-v1`

Continue under Theorem 2.1 and suppose the normalized residual frame `R_0` in (3.5) has physical row leverages

`max_{j != i} ||(R_0)_{j,*}||_2^2 <= 1/2`.                           (4.1)

Then, for independent cap-one original inputs,

`boxed{
 ||p_Q||_(infinity,ess)
 <= 12 [(1-c) Delta_3]^(-1/3).
}`                                                                    (4.2)

In particular, at target normalization `Delta_3>=1`, if

`1/2 < c <= 7/8`,                                                     (4.3)

then

`boxed{ ||p_Q||_(infinity,ess) <=24. }`                               (4.4)

### Proof

Condition on the literal original coordinate `H=X_i`. This is legitimate original-coordinate conditioning. The remaining quadratic part is exactly the complementary rank-three block `C`; the fixed value of `H` contributes only an arbitrary affine term in the residual original variables.

By (3.5), `C` is an exact-rank-three form with normalized spectral frame `R_0` and eigenvalue product

`Delta_C=(1-c)Delta_3`.

The source-pinned Fresnel--Brascamp--Lieb Theorem F (`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`) allows arbitrary affine terms and gives, under (4.1),

`||p_{Q|H=h}||_(infinity,ess) <=12 Delta_C^(-1/3)`

uniformly in `h`. Averaging over `H` proves (4.2). If `Delta_3>=1` and `c<=7/8`, then `1-c>=1/8`, and (4.4) follows. QED.

A useful side identity is the singular-value floor

`min_k |lambda_k(C)| >= (1-c) min_k |lambda_k(A)|`,                  (4.5)

because `DMD` satisfies

`sigma_min(DMD)>=sigma_min(D)^2 sigma_min(M)=(1-c)sigma_min(M)`.

Equation (4.5) is not needed for (4.2), but confirms directly that the residual rank-three curvature only collapses at the near-coloop endpoint `c->1`.

## 5. What remains after this run

Inside the **exact-rank-three high-leverage zero-pivot survivor**, the remaining obstruction can now be stated without hidden scales.

After choosing a heavy zero-pivot row and applying the exact Witt compiler, the form is

`Q=2aV(H+kappa U)+alpha V^2+2gamma V W+delta W^2`,                   (5.1)

where

- `H` is one literal original coordinate and is independent of the residual product bank;
- `(U,V,W)` are three orthonormal projections of that residual product bank, not independent;
- `0<kappa<1` in the high-leverage chamber;
- the target gives `a^2|delta|>=1/2` by the designated-partner star identity;
- if the normalized residual frame is diffuse and `kappa^2=(1-c)/c >=1/7` (equivalently `c<=7/8`), Theorem 4.1 already pays the branch by `24`.

Thus an unpaid survivor must satisfy at least one of:

1. **near-coloop/shared-multiplier endpoint:** `c>7/8`, equivalently `kappa<1/sqrt(7)`, where the independent-hub endpoint is quantitatively close but small-coefficient perturbation is forbidden by the live corrections; or
2. **residual heavy row:** the normalized residual frame `R_0` itself has a row leverage `>1/2`, so the problem must use a second physical heavy coordinate rather than a diffuse residual estimate.

The exact next analytic obligation for B05 is therefore

`QFORM-WITT-SHARED-MULTIPLIER-ENDPOINT-v1`:

> prove a shell/coarea estimate for (5.1) which is uniform in `0<=kappa<1/sqrt(7)` and depends on `(a,delta)` only through `(a^2|delta|)^(-1/3)`, while retaining that `(U,V,W)` are a single three-dimensional orthogonal projection of the residual original-coordinate product law.

A bound of the form

`||p_Q||_infinity <= C (a^2|delta|)^(-1/3)`                          (5.2)

would immediately close the near-coloop part by (3.6). The live arbitrary-joint coarea and conditional-cap counterexamples show why replacing the residual projection by only a joint `L^infinity` cap is insufficient.

## 6. Scope audit

**Proved here:** exact Witt normal form (2.6)-(2.8); exact curvature split (3.2)-(3.4); target-normalized partner currency (3.6); diffuse-normalized-residual density estimate (4.2), including the explicit `<=24` branch (4.4).

**Not proved:** the uniform shared-multiplier endpoint (5.2); the residual-heavy-row branch; arbitrary higher-rank matrices with additional spectrum; the full QFORM theorem; or full-target continuity.

No post-rotation independence, moment, support, compactness, Gaussianity, log-concavity, arbitrary-joint coarea theorem, conditional projection cap, unrestricted fiber supremum, or small-random-tail deletion is used. The only conditioning in Theorem 4.1 is on the literal original coordinate `X_i`.
