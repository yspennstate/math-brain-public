SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T09:36:06.433119Z.
attacking: quantify the genuine one-/two-child hybrid under localized-coordinate conditioning, prove a conditioning-stable diffuse finite-range estimate, and identify exactly which mixed receiver is still missing when arbitrary complementary spectrum is restored.

# account02/B08 r25 — conditioning-stable diffuse hybrid and exact gate persistence

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / complementary constructions and source-valid counterexamples  
**Classification:** `NEW SUPPORTING ANALYTIC THEOREM + CONDITIONING-STABLE TARGET FAMILY + SHARP HYBRID OBSTRUCTION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source-pinned inputs

The full target remains OPEN: for arbitrary independent ORIGINAL coordinates with probability densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^TAX`, or give a valid counterexample. No moments, support regularity, log-concavity, identical laws, spectral-coordinate conditioning, or independence after rotation is used.

The current B08 predecessor is account02/B08 r24, which fixes the legitimate no-pivot gate

`tau_* = 1/4000000`

and shows that the actual `k=1,2` child/cross hybrid survives even in `N3(tau_*)`. Its target-valid Hadamard family has exactly three eigenvalues of modulus at least one and realizes exactly `k` actual child directions plus `3-k` actual cross directions at the current spectral gate.

The newest completed designated partner actually used below is account03/B08 r33:

`yspennstate/math-open-problems@6f8e99aec5b12f0e3a5f13d60e7da490ce491647`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T090721Z-account03-B08-qform-diffuse-r33/REPORT.md`.

Its full-ambient two-cross consequence says that for an ACTUAL original-coordinate cross cut `T`, with

`Delta = sigma_1(T) sigma_2(T)`,                                  (1.1)

one has

`H_(1/2)(Q) <= 8 Delta^(-1/4)`,                                 (1.2)

and

`||p_Q||_3 <= 6^(2/3) Delta^(-1/3)`.                            (1.3)

Arbitrary same-side quadratic blocks, affine terms, outside couplings and extra spectrum are retained. I apply (1.2)-(1.3) to the conditioned `k=1` hybrid in Section 5.

The required newest-Claude source actually applied to an `L^infinity` inequality is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

Its rank-`r` Fresnel--Brascamp--Lieb theorem gives, for an exact spectral representation with maximum physical row leverage at most `1/2`,

`||p_Q||_infinity <= [4r/(r-2)] |det Lambda|^(-1/r),  r>2,`      (1.4)

uniformly in affine terms and arbitrary cap-one product input laws, with a continuous `C_0` density.

## 2. First unpaid implication

The r24 tiny-`N3` pruning removes the partner's aligned physical-pivot descendant and greatly amplifies its determinant-core sibling, but it does **not** remove the actual spectral hybrids. The remaining mixed receiver can now be stated sharply:

* `k=1`: two actual cross singular directions are available, while one actual child eigendirection remains;
* `k=2`: one actual cross singular direction is available, while two actual child eigendirections remain.

The missing theorem must turn these mixed resources into a full-ambient `L^infinity` estimate **with arbitrary complementary spectrum**. The calculation below proves that the mixed receiver is completely stable when the whole nonzero spectral range is itself diffuse, even after conditioning a positive fraction of physical coordinates. It also proves that sparse localized-coordinate conditioning does not manufacture the missing cross singular directions. Thus the unpaid part is genuinely stability under arbitrary complementary spectral curvature, not a failure of the product law after physical conditioning.

## 3. A general conditioning-stable exact-range theorem

### Theorem 3.1 — `QFORM-EXACT-RANGE-CONDITIONING-FRESNEL-v1`

Let

`A = R D R^T`,                                                   (3.1)

where `R` is `n x r`, `R^T R=I_r`, `r>2`, and `D` is real symmetric and invertible. Assume

`max_i ||R_(i,:)||_2^2 <= delta`.                               (3.2)

Let `H` be any set of `h` ORIGINAL coordinates and `T=H^c`. If

`h delta < 1`,                                                   (3.3)

then the residual principal block `A_TT` has rank `r`. If moreover

`delta/(1-h delta) <= 1/2`,                                     (3.4)

then for every choice of the conditioned values `X_H=x_H`, every family of independent cap-one input densities on `T`, and every induced affine term,

`boxed:
 ||p_(Q | X_H=x_H)||_infinity
 <= [4r/(r-2)] (1-h delta)^(-1) |det D|^(-1/r).
`                                                                    (3.5)

The characteristic-function envelope in the source theorem is uniform in `x_H`, so the unconditional form also has a continuous `C_0` density with the same bound.

**Proof.** Put

`E=R_H^T R_H`, `G=R_T^T R_T=I-E`.                              (3.6)

Every row outer product in `E` has operator norm at most `delta`, hence

`0<=E<=h delta I`, `G>=(1-h delta)I`.                            (3.7)

Define

`W=R_T G^(-1/2)`.                                                (3.8)

Then `W^T W=I_r`, and

`A_TT = W K W^T`, `K=G^(1/2) D G^(1/2)`.                        (3.9)

For each surviving physical row,

`||W_(i,:)||^2 = R_i G^(-1) R_i^T
 <= delta/(1-h delta) <=1/2`.                                   (3.10)

Diagonalize the symmetric `r x r` matrix `K` by an orthogonal matrix. This preserves all row leverages in (3.10), so the rank-`r` Fresnel--Brascamp--Lieb theorem applies. Finally

`|det K| = det(G)|det D|
 >=(1-h delta)^r |det D|`.                                      (3.11)

Substitution into (1.4) gives (3.5). Conditioning on original coordinates creates only affine and constant terms, already allowed by the source theorem. QED.

This theorem is product-preserving: no spectral coordinate is declared independent. The orthogonal matrix diagonalizing `K` changes only the deterministic spectral frame used inside the Fresnel argument; the random variables remain the original independent coordinates.

## 4. The exact hybrid family after arbitrary physical conditioning

Let `m=2^q`, let `U` be the first three normalized columns of the `m x m` Sylvester--Hadamard matrix, and fix `k in {1,2}` and `0<d<=1/10`. Let `P=P_(k,d)` be diagonal with exactly `k` entries `1-d` and the other `3-k` entries `1/5`. Set

`A_(m,k,d)= [ UPU^T        U(I-P)U^T ]
             [ U(I-P)U^T  UPU^T       ]`.                       (4.1)

As in r24, the six-dimensional nonzero spectral frame is

`R_+ = (U;U)/sqrt(2)`, `R_-=(U;-U)/sqrt(2)`,                    (4.2)

with eigenvalues

`1,1,1`, and `k` copies of `1-2d` plus `3-k` copies of `-3/5`.   (4.3)

Hence the target has exactly three eigenvalues of modulus at least one and every row leverage of the entire six-dimensional range is exactly

`delta_range=3/m`.                                               (4.4)

Now condition on an **arbitrary** set `H` of `h` original coordinates across the two halves. By Theorem 3.1, whenever `m-3h>=6`,

`boxed:
 ||p_(Q | X_H=x_H)||_infinity
 <= 6(1-3h/m)^(-1)
    [(1-2d)^k (3/5)^(3-k)]^(-1/6).
`                                                                    (4.5)

Uniformly for `d<=1/10`,

`boxed:
 ||p_(Q | X_H=x_H)||_infinity
 <= 6(1-3h/m)^(-1)
    [(4/5)^k (3/5)^(3-k)]^(-1/6).
`                                                                    (4.6)

In particular, for

`h <= m/100`,                                                    (4.7)

we obtain the explicit universal conditional bounds

`k=1: ||p||_infinity < 7.612`,                                  (4.8)
`k=2: ||p||_infinity < 7.256`.                                  (4.9)

Thus the exact diffuse hybrid remains uniformly paid even after an adversary localizes and conditions up to one percent of one Hadamard half's coordinate count (equivalently at most `m/100` of the `2m` physical coordinates). This is far stronger than merely conditioning finitely many anchors.

## 5. The actual spectral gate itself survives the same conditioning

Write `H_L,H_R` for the conditioned coordinates in the two physical halves, with sizes `h_L,h_R`. Put

`G_L=I-U_(H_L)^T U_(H_L)`, `G_R=I-U_(H_R)^T U_(H_R)`.           (5.1)

Since every row of `U` has squared norm `3/m`,

`G_s >= (1-3h_s/m)I`, `s=L,R`.                                 (5.2)

Let

`eta_s=1-sqrt(1-3h_s/m)`.                                      (5.3)

### Child spectra

The nonzero eigenvalues of the conditioned left child are those of

`G_L^(1/2) P G_L^(1/2)`.                                       (5.4)

Because `||P||<=1`,

`||G_L^(1/2) P G_L^(1/2)-P||op <=2 eta_L`.                     (5.5)

For `h<=m/100`, each `eta_s` is at most

`eta_0=1-sqrt(0.97)=0.0151142198203895...`.                     (5.6)

At the actual gate

`c_1=(1/2)sqrt(3/5)=0.387298334620742...`,                      (5.7)

the `k` high child eigenvalues remain at least

`1-d-2eta_0 >=0.869771560359221...>c_1`,                        (5.8)

whereas the other `3-k` remain at most

`1/5+2eta_0 <=0.230228439640779...<c_1`.                        (5.9)

So each conditioned physical child still has **exactly `k` actual gate-large eigenvalues**.

### Cross singular values

The conditioned left-right cross block is

`B_T=U_(T_L)(I-P)U_(T_R)^T`.                                   (5.10)

Writing the polar factorizations of the two restricted Hadamard frames shows that its three nonzero singular values are exactly those of

`G_L^(1/2)(I-P)G_R^(1/2)`.                                     (5.11)

Since `||I-P||=4/5`,

`||G_L^(1/2)(I-P)G_R^(1/2)-(I-P)||op
 <=(4/5)(eta_L+eta_R)`.                                        (5.12)

Under (4.7), the right side is at most

`e_0=0.0241827517126232...`.                                   (5.13)

The `3-k` large cross singular values are therefore at least

`4/5-e_0=0.775817248287377...`,                                (5.14)

while the remaining `k` are at most

`d+e_0<=0.124182751712623...`.                                 (5.15)

The current cross gate is

`beta_1=(3/16)sqrt(3/5)=0.145236875482778...`.                  (5.16)

Hence (5.14)-(5.15) prove that, after **every** conditioning set satisfying (4.7), the residual form still realizes exactly the same hybrid count:

`boxed: k actual child directions + (3-k) actual cross directions.` (5.17)

Moreover, for every fixed `h` (or more generally `h=o(m)`), the error in (5.12) is `o(1)`. Consequently, by taking `m->infinity` and then `d->0`, the `k` missing cross singular values remain arbitrarily small **after the conditioning**. Sparse localized-coordinate conditioning cannot manufacture a third cross direction in the `k=1` branch or a second/third cross direction in the `k=2` branch.

This is a target-valid obstruction to the stronger reduction

`delocalized hybrid + bounded physical conditioning => three uniformly large cross singular values`.

It is not a QFORM counterexample, because (4.8)-(4.9) pay the same conditional laws uniformly.

## 6. Actual use of the newest partner theorem on the conditioned `k=1` branch

For `k=1`, (5.14) gives two actual cross singular values at least

`s_* =0.775817248287377...`.                                   (6.1)

Thus for the full conditioned ambient form

`Delta=sigma_1(B_T)sigma_2(B_T)>=s_*^2`.                        (6.2)

Apply account03/B08 r33's full-ambient two-cross inequalities (1.2)-(1.3):

`boxed:
 H_(1/2)(Q | X_H=x_H) < 9.083,
 ||p_(Q | X_H=x_H)||_3 < 3.911.
`                                                                    (6.3)

This is useful even without the exact-range assumption: it retains arbitrary same-side curvature and every unused coupling. In the present exact-rank-six family, Theorem 3.1 then gives the stronger `L^infinity` conclusion (4.8).

The comparison isolates the missing general compiler. In the `k=1` state, the robust source-valid currency is already

`two-cross L^3 / H_(1/2) + one actual child direction`.          (6.4)

What is not yet proved is a dimension-free, product-preserving upgrade of (6.4) to `L^infinity` under **arbitrary complementary spectral curvature**.

For `k=2`, only one cross singular value is forced by (5.14), while the other two can tend to zero by the last paragraph of Section 5. The missing compiler there is genuinely different:

`one cross direction + two actual child directions`.            (6.5)

## 7. Consequences for the tiny-N3 proof tree

The newest partner result and r24 already remove the aligned physical-pivot/Dodgson descendant inside the sufficient tiny-`N3(tau_*)` class. The present calculation says that the remaining hybrid cannot be removed by a strategy of conditioning finitely many, or even `o(m)`, localized coordinates and hoping the residual cross block acquires the missing singular directions.

At the same time, the whole-range diffuse Fresnel mechanism is remarkably stable under exactly that conditioning: the determinant payment loses only the factor `(1-3h/m)^(-1)`. Therefore a correct hybrid proof should seek a **remainder-stable mixed Fresnel/decoupling theorem**, not another cross-rank extraction.

The first unpaid implication is now stated more concretely as

**`QFORM-N3-MIXED-CHILD-CROSS-REMAINDER-STABILITY-v1` — OPEN.**  
Prove a full-ambient `L^infinity` estimate, with arbitrary complementary spectrum and original-coordinate product inputs, from either

1. `k=1`: two-cross currency of the type (6.3) plus one actual child eigendirection at scale `c_L`; or
2. `k=2`: one actual cross singular direction at scale `beta_L` plus two actual child eigendirections at scale `c_L`.

The theorem must reduce to (3.5) when the complementary spectrum is absent or contained in the same diffuse exact range, and it cannot assume that bounded physical conditioning increases the cross rank. The amplified determinant-core R1/E2/BICORE descendants from r24 remain a parallel tiny-N3 debt.

The unrestricted conjecture and global continuity remain OPEN.

## 8. Verification

The accompanying checker verifies the leverage-after-conditioning formula, the two gate margins, the `k=1,2` conditional `L^infinity` constants, and the partner `H_(1/2)` / `L^3` constants. It terminates `QFORM_B08_R25_CHECK_PASS`.

Repository transport is not native learned-memory ingestion. No FEI, installation, benchmark, task/schedule, notification/email, permission, paid-call, remote-workflow, cross-account authentication, or public-release mutation is part of this result.
