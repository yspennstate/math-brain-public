SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-22T20:40:46Z.
attacking: the exact-rank-three heavy-null overlap state; aggregate an arbitrary indefinite physical pair's full Schur determinant bank, then use a quantitative Witt dichotomy to close the nested-heavy branch left by B10 r15.

# account03/B10 r17 — aggregate pair-Schur bank + quantitative Witt dichotomy closes the nested-heavy near-null branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NESTED-HEAVY-OVERLAP-BRANCH-CLOSED / FULL_TARGET_OPEN`

The exact owner target remains open: for independent real physical coordinates with densities bounded by one and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal bound on the essential supremum of the density of `Q=X^T A X`, or give a target-valid counterexample. Continuity is a separate desired conclusion.

This report uses only original-coordinate independence. It does not use the refuted arbitrary-joint three-dimensional coarea bound, positive conditional spectral-density moments, a fiber supremum, or law-uniform pointwise Fresnel decay. It does not rotate the physical input law and then declare the rotated coordinates independent.

The exact named partner `account04/B10` still has no completed current-QFORM artifact in the fresh source tree; the visible account04/B10 reports remain from the earlier POS3 programme. I therefore do not fabricate a partner result. I apply the completed compatible account04/B16 determinant-bank theorem at

`yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`.

The other proof-level input used below is the completed logarithmic two-coordinate smoothing theorem at

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

## 1. First unpaid implication inherited from B10 r15

B10 r15 proved `QFORM-NULL-BANK-CAPONE-COMPRESSION-v1`. In its near-endpoint state, after compressing a whole exact null-ray bank before whitening, the same law of `Q` has an exact-rank-three Parseval representation

`A_hat=U_hat Lambda_hat U_hat^T`, `U_hat^T U_hat=I_3`,

with a distinguished synthetic original independent cap-one coordinate indexed by `0`. Its spectral row is

`u_0=sqrt(c) r`,

where `r` is unit and null for `Lambda_hat`, and in the near endpoint

`c>=7/9`, `sigma:=sigma_min(Lambda_hat)>=1/2`, `|det Lambda_hat|>=1/2`.

The full two-coordinate determinant mass leaving the null row is at least `7/16`. In the nested-heavy subbranch there is a complement row `u_j` whose residual Euclidean leverage transverse to `r` obeys

`h_j=||(I-r r^T)u_j||^2>1/2`.

Applying the completed compatible account04/B16 theorem gives the exact fixed-pair determinant-bank identity

`P_0j := sum_k |det (A_hat)_{ {0,j,k} }|
       = |det Lambda_hat| c h_j`,

and B10 r15's exact cancellation with the pre-compression variables sharpened this to

`P_0j>7/32`.                                                        (1.1)

The first unpaid step was to exploit this entire overlapping/diffuse bank before paying reciprocal individual minors.

## 2. New theorem: aggregate an arbitrary indefinite physical pair's whole rank-one Schur bank

### Theorem 2.1 — `QFORM-INDEFINITE-PAIR-SCHUR-BANK-v1`

Let `A` have exact rank three and let `i,j` be two ORIGINAL physical coordinates whose `2x2` principal block `B` is invertible and indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)`.

After conditioning on no coordinates, write the exact Schur complement of this pair as

`S=sigma_0 d d^T`, `||d||_2=1`,

on the complementary original coordinates. Define the full fixed-pair determinant-bank mass

`P_ij := sum_(k != i,j) |det A_{ {i,j,k} }|`.

Then

`P_ij=D |sigma_0|`.                                                 (2.1)

For arbitrary independent input coordinates with density caps one and arbitrary affine terms, the law of the full quadratic form has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity
 <= 8*2^(3/4) (kappa P_ij)^(-1/4).`                                 (2.2)

Numerically the front constant is

`8*2^(3/4)=13.4543426440594...`.

This theorem aggregates the **whole** fixed-pair determinant bank and therefore does not require a heavy third-coordinate atom.

### Proof

Block-decompose on the physical pair and its complement:

`A=[[B,C],[C^T,D_0]]`.

Because `rank A=3` and `rank B=2`, the Schur complement

`S=D_0-C^T B^(-1)C`

has rank one, so `S=sigma_0 d d^T` for a unit vector `d` and nonzero `sigma_0`.

For every complementary physical coordinate `k`, the principal `3x3` determinant identity gives

`det A_{ {i,j,k} }=det(B) S_kk=det(B) sigma_0 d_k^2`.

Taking absolute values and summing `sum d_k^2=1` proves (2.1).

Set the genuine original-coordinate projection bank

`L=sum_k d_k X_k`.

The completed fixed-pair projection-product result used by account04/B16 gives the safe density cap

`||p_L||_infinity <= M`, with `M=2`.                               (2.3)

For every target `t` and `rho>0`, the one-dimensional set

`{ell: |sigma_0 ell^2-t|<rho}`

has Lebesgue measure at most `2 sqrt(2 rho/|sigma_0|)`. Hence (2.3) implies the translation-uniform rank-one small-ball estimate

`sup_t P(|sigma_0 L^2-t|<rho)
 <= 2 sqrt(2) M sqrt(rho/|sigma_0|).`                               (2.4)

Now complete the physical pair `B`. The two selected original variables remain independent cap-one variables after deterministic translations depending on the complement. The pair-log theorem permits exactly this dependence of the shifts. Its general form states: if the remainder obeys

`sup_t P(|R-t|<rho)<=H sqrt(rho)`,

then

`||p_Q||_infinity <=4 sqrt(2H)(D kappa)^(-1/4)`.                    (2.5)

Insert

`H=2 sqrt(2) M / sqrt(|sigma_0|)`

from (2.4). This gives

`||p_Q||_infinity
 <=8*2^(1/4)*sqrt(M)*(D kappa |sigma_0|)^(-1/4)`
` =8*2^(1/4)*sqrt(M)*(kappa P_ij)^(-1/4)`                           (2.6)

by (2.1). With `M=2`, (2.2) follows. QED.

The key point is the order of payment: the normalized Schur bank is first compressed to the genuine product projection `L`; only the **total** determinant resource `P_ij` enters the reciprocal cost. No sum of `|det A_{ijk}|^(-alpha)` appears.

## 3. New quantitative Witt dichotomy at an exact null direction

### Lemma 3.1 — `QFORM-NULL-WITT-CROSS-OR-DIAGONAL-v1`

Let `Lambda` be a real symmetric invertible `3x3` matrix and put

`sigma=sigma_min(Lambda)>0`.

Let `r` be a unit null vector,

`r^T Lambda r=0`.

If `u` is any vector with `||u||<=1` and transverse leverage

`h=||(I-r r^T)u||^2>=1/2`,

then at least one of the following holds:

`boxed: |r^T Lambda u| > sigma/16`,                                (3.1)

or

`boxed: |u^T Lambda u| >= (61/256) sigma.`                          (3.2)

(The strict/non-strict choice at the threshold is immaterial.)

### Proof

Set

`S=||Lambda r||`, `w=Lambda r/S`.

Because `r` is null, `w` is unit and orthogonal to `r`. Complete `(r,w)` to an orthonormal basis `(r,w,m)`. In this basis

`Lambda = [[0,S,0],[S,a,b],[0,b,k]]`.                              (3.3)

Since `Lambda` is invertible, `k!=0`. Direct inversion gives

`Lambda^(-1)=
 [[(b^2-a k)/(S^2 k), 1/S, -b/(S k)],
  [1/S,                 0,    0      ],
  [-b/(S k),            0,    1/k    ]]`.                          (3.4)

Every entry of `Lambda^(-1)` has absolute value at most `1/sigma`. Therefore

`S>=sigma`, `|k|>=sigma`,

`|b|<=S|k|/sigma`,

and

`|a-b^2/k|<=S^2/sigma`.

Consequently

`|a|<=2 S^2 |k|/sigma^2`.                                         (3.5)

Write

`u=alpha r+beta w+gamma m`,

so `h=beta^2+gamma^2`. Put

`eta=S|beta|/sigma=|r^T Lambda u|/sigma`.

If `eta>1/16`, (3.1) holds. Otherwise `eta<=1/16`. Since `S>=sigma`,

`beta^2<=eta^2`.

Using (3.3)-(3.5), `|alpha|,|gamma|<=1`, and `|k|>=sigma`,

`|u^T Lambda u|`
`=|2S alpha beta+a beta^2+2b beta gamma+k gamma^2|`
`>=|k| gamma^2-2S|beta|-|a|beta^2-2|b||beta||gamma|`
`>=|k|[gamma^2-4eta-2eta^2]`
`= |k|[h-beta^2-4eta-2eta^2]`
`>=|k|[h-4eta-3eta^2]`
`>=sigma[1/2-4/16-3/256]`
`=(61/256)sigma`.

This is (3.2). QED.

This is a quantitative form of the Witt-index-one obstruction: a row carrying at least half of a transverse Euclidean direction cannot simultaneously have both tiny bilinear coupling to an exact null ray and tiny quadratic pivot, with constants depending only on the least spectral singular value and not on `||Lambda||`.

## 4. Direct application: the B10 r15 nested-heavy overlap state is uniformly paid

Return to the compressed near-endpoint state of Section 1. Thus

`c>=7/9`, `sigma>=1/2`, `|det Lambda_hat|>=1/2`, `h_j>1/2`,

and the completed compatible account04/B16 theorem has already supplied

`P_0j>7/32`.                                                        (4.1)

Apply Lemma 3.1 to `r` and `u_j`.

### Case A: the physical diagonal is large

If

`|A_jj|=|u_j^T Lambda_hat u_j| >=(61/256)sigma`,

then `||u_j||^2>=h_j>1/2`. The completed rank-three scalar-pivot consequence of `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` gives

`||p_Q||_infinity
 <=128 [ ||u_j||^2 |A_jj| |det Lambda_hat| ]^(-1/4)`.               (4.2)

The bracket is at least

`(1/2)*(61/512)*(1/2)=61/2048`,

so

`boxed: ||p_Q||_infinity
 <=128(2048/61)^(1/4)
 <308.113.`                                                         (4.3)

### Case B: the null-row cross coefficient is large

Otherwise Lemma 3.1 gives

`|r^T Lambda_hat u_j|>sigma/16`.

The actual physical off-diagonal coefficient from the synthetic null row is

`b=A_0j=sqrt(c) r^T Lambda_hat u_j`.

Hence

`|b|>g sigma`, `g:=sqrt(7)/48=0.0551198189805...`.                  (4.4)

If `|A_jj|>=g sigma`, the same scalar-pivot theorem gives

`||p_Q||_infinity
 <=128(8/g)^(1/4)
 <444.279.`                                                         (4.5)

It remains only the subcase

`|A_jj|<g sigma`.                                                   (4.6)

Then the physical pair on `{0,j}` is

`B=[[0,b],[b,A_jj]]`,

which is automatically invertible and indefinite. Its smaller singular value is

`kappa=[sqrt(A_jj^2+4b^2)-|A_jj|]/2`
` >=|b|-|A_jj|/2`
` >g sigma/2`
` >=g/4`.                                                          (4.7)

Now apply Theorem 2.1 to this **same fixed pair**, using the actual partner determinant bank (4.1):

`||p_Q||_infinity
 <=8*2^(3/4) (kappa P_0j)^(-1/4)`
` <8*2^(3/4) [128/(7g)]^(1/4)`
` <57.421.`                                                         (4.8)

This is the requested direct application of completed compatible account04 mathematics to an actual inequality: account04/B16 supplies the total bank lower bound `P_0j>7/32`, and the new aggregate Schur-bank theorem spends that total resource without selecting a heavy atom.

Combining (4.3), (4.5), and (4.8):

`boxed: the entire nested-heavy branch of the B10-r15 near-endpoint heavy-null overlap state has ||p_Q||_infinity <445.`             (4.9)

No support-separation condition and no zero diagonal on the second or third coordinates is needed.

## 5. What remains after this run

This run closes `QFORM-HEAVY-NULL-OVERLAP-AGGREGATION-v1` **in its nested-heavy subbranch**. The first exact-rank-three B10 debt is now the complementary one-heavy-row geometry:

`QFORM-HEAVY-NULL-NONNESTED-v1`: after the cap-one null-bank compression, the distinguished null row has leverage at least `7/9`, but every complement row has residual leverage at most `1/2` transverse to that null direction. The transverse residual frame is therefore two-dimensionally diffuse. A completion must exploit that diffuse product frame while retaining the correlated longitudinal leakage; it may not replace the three projected coordinates by an arbitrary joint density or take a worst conditional projection cap.

The arbitrary-extra-spectrum passage needed for the full owner target is also still separate and unpaid.

## 6. Status and regularity

Proved in this run:

- `QFORM-INDEFINITE-PAIR-SCHUR-BANK-v1`, the determinant-bank aggregate bound (2.2) for any invertible indefinite original-coordinate pair in exact rank three;
- `QFORM-NULL-WITT-CROSS-OR-DIAGONAL-v1`, the quantitative null-direction dichotomy (3.1)-(3.2);
- the universal `<445` essential-density bound for the complete nested-heavy near-endpoint overlap branch left by B10 r15.

Not proved: the nonnested heavy-null branch, arbitrary exact-rank-three closure, arbitrary additional spectral components, or the full owner conjecture. The arguments here prove **essential boundedness** in their stated branches; continuity is **not claimed**.

**Full QFORM conjecture: OPEN / NOT PROVED.**
