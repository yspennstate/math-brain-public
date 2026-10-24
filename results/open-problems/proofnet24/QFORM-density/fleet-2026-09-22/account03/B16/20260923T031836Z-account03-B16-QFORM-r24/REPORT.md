SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T03:18:36Z.
attacking: the dominant near-null transverse-diffuse star by deriving a dependence-preserving duplicated-slice Fresnel estimate and isolating the only surviving coloop-type leakage geometry.

# account03/B16 r24 — duplicated-slice Fresnel compiler and two-coloop reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING ANALYTIC THEOREM / STRONGER EXACT-RANK-THREE REDUCTION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository reads/writes were authenticated; native learned-memory receiver ingestion was not verified.  
**Continuity:** proved on the new duplicated-slice branch; not proved for the complete target.

## 1. Source-valid inherited chamber

The full owner target remains open: for arbitrary independent original coordinates with probability densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension- and law-independent `L^infinity` density bound for `X^T A X`, or give a genuine counterexample.

This run starts from account03/B16 r23, canonical source

`yspennstate/math-open-problems@bbb01a983ce6478003ccf8422198c87f44f52cea`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T025235Z-account03-B16-QFORM-r23/REPORT.md`.

In its exact-rank-three residual chamber write

`A=R Lambda R^T`, `R^T R=I_3`, `min_k |lambda_k|>=1`,

and choose the dominant heavy original coordinate `i` supplied by `QFORM-MIXED-PLUECKER-DOMINANT-STAR-v1`. Put

`c=||r_i||^2`, `e=r_i/sqrt(c)`, `c_*=643/7936`.

Then

`c>c_*`,
`|e^T Lambda e|<31/10288`,

and the completed designated-partner theorem account04/B16 is already applied at the disjoint-Pluecker parameter `d`: if `d>=1/64`,

`||p_Q||_infinity <= 12 |det Lambda|^(-1/3) d^(-1/6) <= 24`.       (1.1)

Hence this report works only on `d<1/64`. The same partner theorem also keeps its majority-sign one-sheet estimate `pi sqrt(2)` available. Its canonical source is

`yspennstate/math-open-problems@b111363ff02b67015d14db35482e0150591744cd`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T231542Z-account04-B16-QFORM-r1/REPORT.md`.

All current corrections are retained: no arbitrary-joint 3D coarea bound, no positive conditional projection-height moment, no independence after spectral rotation, no receiver-only fiber supremum, and no law-uniform pointwise one-dimensional Fresnel decay is used.

Rotate only the deterministic three-dimensional coefficient space so that `e=e_1`. For every residual original coordinate `j!=i`, write

`r_j=s_j e+w_j`, `w_j in R^2`, `h_j=||w_j||^2`.

Parseval gives the exact identities

`sum_j s_j^2=1-c=:a`,
`sum_j s_j w_j=0`,
`sum_j w_j w_j^T=I_2`.                                             (1.2)

No random-variable rotation has occurred.

## 2. First improvement: every transverse row above 1/64 is already paid

The preceding r23 report used the coarse trigger `h_j>1/2`. The same source-valid physical-pair calculation works at a much smaller fixed threshold.

### Lemma 2.1 — `QFORM-DOMINANT-STAR-TRANSVERSE-1OVER64-ESCAPE-v1`

In the r23 residual chamber, if some `j!=i` satisfies

`h_j>=1/64`,                                                        (2.1)

then

`||p_Q||_infinity <865`.                                           (2.2)

#### Proof

The two spectral rows have Gram determinant

`G_ij=||r_i wedge r_j||^2=c h_j >= g_0:=c_*/64=643/507904`.         (2.3)

Let `H_ij` be their `2x2` Gram matrix. Since `tr H_ij<=2`,

`lambda_min(H_ij)>=det(H_ij)/tr(H_ij)>=g_0/2=:m_0`.                (2.4)

Orthonormalize the two rows. By Cauchy interlacing, every two-dimensional compression of a three-dimensional symmetric matrix whose three eigenvalues have modulus at least one has operator norm at least one: in signature `(2,1)` its top Ritz value is at least the middle positive eigenvalue, and in signature `(1,2)` its bottom Ritz value has modulus at least the middle negative magnitude. Therefore the physical pair block

`B=A_{ {i,j},{i,j} }`

satisfies

`||B||_op >= m_0`.                                                 (2.5)

The r23 residual chamber also has `|A_kk|<delta:=1/4096` for every heavy coordinate. Since `h_j>=1/64`, coordinate `j` is heavy, so writing

`B=[[u,b],[b,v]]`

gives `|u|,|v|<delta`. From `||B||_op<=delta+|b|`,

`|b|>m_0-delta`.

Now

`m_0=643/1015808`,
`m_0-2delta=147/1015808=:kappa_0>0`.                              (2.6)

Thus `|b|>delta`, so `B` is invertible indefinite, and Weyl comparison with `[[0,b],[b,0]]` gives

`sigma_min(B)>kappa_0`.                                           (2.7)

For exact rank three the fixed-pair determinant bank is

`P_ij=sum_{k!=i,j}|det A_{ijk}|=|det Lambda| G_ij>=g_0`.          (2.8)

The source-valid B16 pair-log/rank-one-remainder theorem used in r23 then yields

`||p_Q||_infinity
 <=8 sqrt(5)(P_ij sigma_min(B))^(-1/4)
 <8 sqrt(5)(g_0 kappa_0)^(-1/4)
 =864.6517558...<865.`                                            (2.9)

QED.

Consequently, the only new branch that still needs analysis has

`boxed: h_j<1/64 for every j!=i.`                                 (2.10)

This is substantially stronger than the former transverse `1/2` diffuseness gate.

## 3. New analytic theorem: duplicated-slice Fresnel payment

The next theorem is independent of the special r23 constants. It is a general exact-rank-three projection-product statement. Its point is to retain the dependence caused by the common leakage coefficients `s_j` by squaring the transverse Fourier slice before applying Brascamp--Lieb.

### Theorem 3.1 — `QFORM-DUPLICATED-SLICE-FRESNEL-v1`

Let

`A=R Lambda R^T`, `R^T R=I_3`, `det Lambda!=0`,

and let the original coordinates be independent with densities `0<=f_j<=1`. Fix an original coordinate `i` with leverage `0<c=||r_i||^2<1`, write the residual rows as in (1.2), and define

`delta_j := h_j + s_j^2/[2(1-c)]`.                                (3.1)

Assume

`boxed: delta_j<=1/2 for every j!=i.`                              (3.2)

Then `Q=X^T A X`, and in fact any affine perturbation `Q+ell^T X+q_0`, has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <=3 e^(5/6) [2c(1-c)]^(-1/6) |det Lambda|^(-1/3).`               (3.3)

No independence of spectral coordinates is asserted or used.

### Proof

Use the Fourier convention

`hat f(theta)=int exp(i theta x)f(x)dx`.

The exact three-dimensional Fresnel identity gives, for `t!=0`,

`|phi_Q(t)|
 <=(4 pi |t|)^(-3/2)|det Lambda|^(-1/2) J_t`,                     (3.4)

where affine terms merely translate the one-dimensional Fourier arguments, and after the deterministic coefficient-space choice `r_i=sqrt(c)e_1`,

`J_t = int_R |hat f_i(sqrt(c) xi+q_i)| F_t(xi) dxi`,             (3.5)

`F_t(xi)
 =int_{R^2} product_{j!=i}
   |hat f_j(s_j xi+<w_j,eta>+q_j)| deta`.                         (3.6)

The shifts `q_j` may depend on `t`; all estimates below are translation-uniform.

The hub factor has the Plancherel bound

`||hat f_i(sqrt(c)·+q_i)||_2
 =c^(-1/4)||hat f_i||_2
 <=(2 pi)^(1/2)c^(-1/4)`,                                        (3.7)

because `int f_i^2<=int f_i=1`.

It remains to prove an `L^2` estimate for the *entire transverse slice* `F_t`. Squaring (3.6) before taking any fiber supremum gives

`||F_t||_2^2
 =int_{R^5} product_{j!=i}
   |hat f_j(s_j xi+<w_j,eta>+q_j)|
   |hat f_j(s_j xi+<w_j,eta'>+q_j)|
   dxi deta deta'.`                                               (3.8)

For every residual coordinate introduce the two five-dimensional row vectors

`v_{j,1}=(s_j,w_j,0)`,
`v_{j,2}=(s_j,0,w_j)`.

Using the three identities (1.2), their Gram sum is exactly

`sum_j (v_{j,1}v_{j,1}^T+v_{j,2}v_{j,2}^T)
 =diag(2(1-c),I_2,I_2)=:G_5`.                                    (3.9)

After whitening by `G_5^(-1/2)`, each of the two copies of row `j` has squared leverage exactly

`||G_5^(-1/2)v_{j,k}||^2
 =h_j+s_j^2/[2(1-c)]
 =delta_j`.                                                       (3.10)

Moreover the duplicated leverages sum to the ambient dimension:

`sum_{j,k} delta_j=5`.                                            (3.11)

Now apply the same sharp Hausdorff--Young plus geometric rank-one Brascamp--Lieb calculation used in the completed QFORM Fresnel-BL reports. Condition (3.2) is exactly the Hausdorff--Young admissibility gate. Arbitrary translations of each one-dimensional argument preserve all norms. Therefore

`||F_t||_2^2
 <=det(G_5)^(-1/2)(2 pi)^5
   product_{j,k}(1-delta_j)^(-(1-delta_j)/2).`                    (3.12)

Since `det G_5=2(1-c)` and

`-(1-d)log(1-d)<=d` for `0<=d<1`,

the product in (3.12) is at most

`exp[(1/2)sum_{j,k}delta_j]=e^(5/2)`.                             (3.13)

Thus

`||F_t||_2
 <=(2(1-c))^(-1/4)(2 pi)^(5/2)e^(5/4).`                        (3.14)

Cauchy--Schwarz in (3.5), together with (3.7), gives

`J_t
 <=(2 pi)^3 e^(5/4)[2c(1-c)]^(-1/4).`                         (3.15)

Substituting into (3.4),

`|phi_Q(t)|
 <=K |t|^(-3/2)`,                                                (3.16)

where

`K=pi^(3/2)e^(5/4)[2c(1-c)]^(-1/4)|det Lambda|^(-1/2).`          (3.17)

Together with `|phi_Q|<=1`,

`|phi_Q(t)|<=min(1,K|t|^(-3/2))`.

The exact integral is

`int_R min(1,K|t|^(-3/2))dt=6K^(2/3)`.                           (3.18)

Fourier inversion now yields

`||p_Q||_infinity
 <=(1/(2pi))6K^(2/3)
 =3e^(5/6)[2c(1-c)]^(-1/6)|det Lambda|^(-1/3)`,                  (3.19)

which is (3.3). Since `phi_Q in L^1`, Fourier inversion also supplies a continuous `C_0` representative. QED.

### Why this is source-valid

This theorem does **not** take an absolute Wiener norm of the full three-dimensional spectral projection. Such a norm is known to fail even in benign diagonal examples. Instead, it takes a two-dimensional transverse Fourier slice, duplicates that slice, and integrates the common leakage frequency only after the two copies have been coupled in the five-dimensional Brascamp--Lieb geometry. The original-coordinate product factors are never replaced by a bounded conditional density.

It also does not use pointwise decay of any one-dimensional quadratic transform. The `|t|^(-3/2)` factor is the exact three-dimensional Fresnel Jacobian; finiteness of its coefficient is paid by the duplicated source-product integral (3.8).

## 4. Application to the r23 near-null star

Remain in the residual chamber after the partner exit (1.1) and the pair escape of Lemma 2.1, so

`c>c_*`, `h_j<1/64` for every residual coordinate.                (4.1)

First suppose

`1-c>=1/64`.                                                       (4.2)

If every duplicated leverage satisfies (3.2), Theorem 3.1 and `|det Lambda|>=1` give

`||p_Q||_infinity
 <=3e^(5/6)[2(c_*)(1/64)]^(-1/6)
 =18.69778236...<18.7`.                                           (4.3)

This branch has a continuous density.

If (3.2) fails, there is some residual coordinate `j` such that

`h_j + s_j^2/[2(1-c)]>1/2`.

Because `h_j<1/64`, this forces the very strong one-coordinate leakage concentration

`boxed: s_j^2/(1-c)>1-2h_j>31/32.`                               (4.4)

Thus failure of the new analytic payment is no longer a generic dependence problem: more than `96.875%` of the entire residual `e`-direction Parseval mass lies on one original coordinate.

If (4.2) itself fails, then

`boxed: c>63/64`,                                                  (4.5)

so the dominant original row is already a spectral near-coloop.

Combining everything gives the new reduction.

### Corollary 4.1 — `QFORM-R23-TWO-COLOOP-REDUCTION-v1`

Inside the exact-rank-three r23 residual chamber, one of the following holds:

1. the designated partner has `d>=1/64`, and `||p_Q||_infinity<=24`;
2. some transverse leverage is at least `1/64`, and `||p_Q||_infinity<865`;
3. `c<=63/64` and every duplicated leverage is at most `1/2`, and `||p_Q||_infinity<18.7` with a continuous density;
4. `c>63/64` (one near-coloop); or
5. there is a unique possible leakage-dominant residual coordinate `j` with
   `s_j^2/(1-c)>31/32` and `h_j<1/64` (a second, almost-collinear source atom).

The word `unique possible` in item 5 follows from `sum_j s_j^2=1-c`: two distinct coordinates cannot each carry more than `31/32` of that mass.

Hence the former broad `dominant near-null star + arbitrary transverse-diffuse leakage` debt is reduced to a **one- or two-source coloop geometry**. The difficult product dependence cannot remain spread across many leakage coordinates.

## 5. Relation to the small nonzero Rayleigh coefficient

The theorem above is stable in the small but nonzero normalized Rayleigh coefficient `alpha=e^T Lambda e`; it never divides by `alpha`. This is the main difference from scalar-Schur completion, whose rank-two half-Riesz cost grows like `|alpha|^(-1/4)`.

There is also an exact algebraic cancellation worth retaining for the next run. Choose the transverse basis so

`Lambda=[[alpha,B,0],[B,r,s],[0,s,tau]]`,

and put

`S=sqrt(c)X_i+T`, `Y=sum y_jX_j`, `Z=sum z_jX_j`.

As a quadratic polynomial in the genuine independent coordinate `X_i`,

`Q=alpha c X_i^2+2sqrt(c)(alpha T+B Y)X_i+R(T,Y,Z)`.

At output level `t`, the root discriminant factor is

`D_t
 =c[(B^2-alpha r)Y^2-2alpha sYZ-alpha tau Z^2+alpha t]`.         (5.1)

Every occurrence of the common leakage variable `T` cancels **exactly**. Moreover the `2x2` matrix in `(Y,Z)`,

`K_alpha=[[B^2-alpha r,-alpha s],[-alpha s,-alpha tau]]`,

satisfies

`det K_alpha=alpha det Lambda`.                                   (5.2)

Taking absolute values of the resulting half-Riesz kernel loses uniformity as `alpha->0`, so (5.1) is not itself a closure. It does, however, show that the surviving coloop endpoint should be attacked by keeping the root-location/source overlap, not by controlling another arbitrary conditional projection height.

## 6. Partner mathematics actually used

The assigned partner account04/B16 is used at a real inequality, not bibliographically. Its completed ruled/Pluecker theorem gives

`||p_Q||_infinity
 <=12|det Lambda|^(-1/3)d^(-1/6)`.

Substitution of the actual threshold `d=1/64` gives `<=24`, so all of Sections 2--5 are performed only after that branch has been removed. Its one-sheet `pi sqrt(2)` estimate also remains available on the complementary indefinite side.

The new duplicated-slice proof additionally reuses only the already source-validated sharp Hausdorff--Young/geometric Brascamp--Lieb normalization from the completed hub-Fresnel package

`yspennstate/math-open-problems@a93d62ee254b5d17d8608a39f25aa3a5d87628f4`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260922T221830Z-account02-B11-QFORM-r16/REPORT.md`.

No theorem from that source is extended by assertion; the five-dimensional duplicated BL calculation is written explicitly above.

## 7. Remaining implication and target status

The first unpaid exact-rank-three implication is now

> **`QFORM-ONE-TWO-COLOOP-NEAR-NULL-CLOSURE-v1`.** In the r23 chamber, close the minority-sign density on the union of (a) `c>63/64`, and (b) `c<=63/64` with one residual coordinate carrying `>31/32` of the remaining longitudinal Parseval mass while its transverse leverage is `<1/64`. Retain the exact discriminant cancellation (5.1) and the product source; do not replace the surviving two-source overlap by an arbitrary joint density.

A natural next mechanism is to condition the leakage-dominant residual coordinate and exploit that the remaining active spectral Gram loses at most one row of leverage `<1-c+1/64`, so its smallest eigenvalue remains bounded below by `c_*-1/64>0`; this should be combined with a one-coloop nonlinear kernel rather than a perturbative deletion.

Arbitrary additional spectral components remain a separate full-target interface after exact rank three is closed.

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Exact rank three:** still OPEN, but the r23 broad diffuse-leakage chamber is now reduced to the explicit one/two-coloop endpoint above.  
**Continuity:** proved in Theorem 3.1 / branch 3 of Corollary 4.1; global continuity remains OPEN.

Finite constants and threshold identities are checked in `CHECK_OUTPUT.txt`; status `PASS`.
