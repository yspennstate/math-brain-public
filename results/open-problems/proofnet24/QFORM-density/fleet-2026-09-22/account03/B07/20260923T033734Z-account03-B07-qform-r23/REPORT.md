SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T03:37:34Z.
attacking: the N3 four-bank survivor — route the near-rank-two and two-sided bounded-rank core branches into aggregate physical minors without selecting one tiny minor.

# account03/B07 QFORM r23 — low-tail E2/rank-one split and bicore-to-physical-minor compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** coordinate minor selection / GEOMETRY  
**Run:** `20260923T033734Z-account03-B07-qform-r23`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Classification:** `NEW DIMENSION-FREE PHYSICAL-MINOR ROUTING THEOREMS / FULL TARGET OPEN`.

## 1. Scope and correction boundary

The exact target remains unrestricted: independent real ORIGINAL coordinates, each with a probability density bounded by one, and an arbitrary real symmetric ambient matrix having at least three eigenvalues of modulus at least one. The goal is one universal finite essential-density bound for `Q=X^T A X`, or a valid counterexample. The stronger continuous-density conclusion is tracked separately.

This report uses no Gaussian, moment, compact-support, connected-support, log-concavity, iid, post-rotation independence, arbitrary-joint rank-three coarea bound, worst conditional projected-density bound, law-uniform pointwise quadratic-phase decay, small-random-quadratic-error replacement, or one-good-minor principle. In particular, the near-rank-one conclusion below is only a structural alternative: the small but nonzero orthogonal tail is NOT deleted.

The live correction inbox was reread immediately before this write. In particular, the `near-zero half-Riesz` correction forbids replacing a small nonzero quadratic coefficient by zero, and the cross-only Schur correction forbids treating an anchored cross-block Schur quantity as the true full-pair Schur quantity in the presence of arbitrary same-side couplings.

The designated `account04/B07` current-QFORM canonical directory and shared handoff were searched fresh and remain absent. No result is fabricated or attributed to that slot. A completed compatible account04/B18 product-projection theorem is applied at an actual inequality in Section 5.

## 2. Incoming four-bank theorem

The immediate source is this slot's r22 theorem,

`yspennstate/math-open-problems@ac54330d3df42a48098ef7c704ac268382accd7c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T030701Z-account03-B07-qform-r22/REPORT.md`.

Inside the current N3/O0 survivor, it supplies four mutually disjoint ORIGINAL-coordinate banks and a physical cross block `M` with

`C R F > kappa`,                                                (2.1)

where

`C=||c||_2`, `R=||r||_2`, `F=||M||_F`, `kappa=1/(256 sqrt(3))`. (2.2)

Write the squared singular values of `M` as

`lambda_1 >= lambda_2 >= ... >=0`,

and set

`S=sum_j lambda_j=F^2`,
`T=sum_{j>=3} lambda_j`.                                        (2.3)

For arbitrary `Lambda>0`, `0<theta<=1/2`, r22 proves that one of the following occurs:

1. `CR>Lambda`;
2. `T<theta F^2`;
3. the FULL ambient quadratic form has a continuous density with

   `||p_Q||_infinity <3456 e Lambda (6/theta^2)^(1/6)`;         (2.4)

4. `T>=theta F^2` and there are matched selected singular-core projections `P_L,P_R`, each of rank `<225/theta`, whose physical diagonals are heavy at some row `i` and column `a`. Their selected-core row and column norms obey

   `||e_i^T P_L M||_2, ||M P_R e_a||_2 > sqrt(T/450)`.          (2.5)

The omitted singular operator norm is at most `sqrt(T)/15`.

This run attacks alternatives 2 and 4 without selecting one local minor.

## 3. Low-tail branch: either aggregate E2 or a genuine rank-one tube

Define

`E_2(M)=e_2(MM^T)=sum_{|I|=|J|=2} det M[I,J]^2`.               (3.1)

The equality is Cauchy--Binet and is exactly the aggregate physical second-minor currency.

### Theorem 3.1 — `QFORM-LOWTAIL-E2-OR-RANKONE-v1`

Assume

`T<theta F^2`,                                                  (3.2)

and choose

`0<eta<(1-theta)/2`.                                           (3.3)

Then at least one of the following holds:

**A. Rank-one Frobenius tube**

`dist_F(M,{rank<=1}) < sqrt(theta+eta) F`.                      (3.4)

**B. Aggregate physical second-minor bank**

`boxed: E_2(M) >= eta(1-theta-eta) F^4.`                        (3.5)

#### Proof

If `lambda_2<eta F^2`, then by (2.3)

`dist_F(M,{rank<=1})^2
 =lambda_2+T
 <(eta+theta)F^2`,                                              (3.6)

which is (3.4).

Otherwise `lambda_2>=eta F^2`. Since

`lambda_1=F^2-lambda_2-T`,                                     (3.7)

we have

`E_2(M)>=lambda_1 lambda_2
 =lambda_2(F^2-T-lambda_2).`                                   (3.8)

The ordering `lambda_1>=lambda_2` places `lambda_2` in the interval from `eta F^2` to `(F^2-T)/2`. On this interval the right side of (3.8) is increasing up to the endpoint `(F^2-T)/2`, so its minimum is at `eta F^2`. Using `T<theta F^2` gives

`E_2(M)
 >= eta F^2[(1-theta-eta)F^2]`,                                (3.9)

proving (3.5). QED.

### Concrete r22 collar

Take

`theta=eta=1/16`.                                               (3.10)

Then either

`boxed: dist_F(M,{rank<=1}) < F/(2 sqrt(2))`,                   (3.11)

or

`boxed: E_2(M) >= (7/128)F^4.`                                 (3.12)

Thus the old phrase “near rank two” is sharpened: unless the block is already within relative Frobenius distance `1/(2sqrt(2))` of rank ONE, it carries a fixed fraction of `F^4` in the complete physical second-compound bank.

### Four disjoint original-coordinate banks from (3.12)

Independently two-color every physical row and every physical column of `M`. A fixed `2x2` minor is rainbow on both sides with probability `1/4`; hence some coloring has rainbow squared-determinant mass at least `E_2(M)/4`.

For that coloring, write the row banks `L_1,L_2` and column banks `R_1,R_2`. For each rainbow minor,

`det[[a,b],[c,d]]^2 <=2(a^2d^2+b^2c^2)`.                       (3.13)

After summing all rainbow minors,

`E_2(M)/4
 <=2[ ||M[L_1,R_1]||_F^2 ||M[L_2,R_2]||_F^2
      +||M[L_1,R_2]||_F^2 ||M[L_2,R_1]||_F^2 ].`               (3.14)

Therefore one matching `sigma in S_2` obeys

`boxed:
 ||M[L_1,R_sigma(1)]||_F^2
 ||M[L_2,R_sigma(2)]||_F^2
 >= E_2(M)/16.`                                                 (3.15)

Under (3.12),

`boxed:
 ||M[L_1,R_sigma(1)]||_F^2
 ||M[L_2,R_sigma(2)]||_F^2
 >=(7/2048)F^4.`                                                (3.16)

This is a dimension-free matching-bank statement in literal original coordinates. No single `2x2` minor is chosen or inverted.

### Actual analytic splice on the diffuse-range subbranch

The completed account03/B06 theorem

`yspennstate/math-open-problems@606257652f3c70e90c7b7f80ea7cb76c1abf689b`,

`QFORM-CROSS-E2-FRACTIONAL-L3-v1`, states that if one side of the physical range of `M` has maximum coordinate leverage at most `1/2`, then the full quadratic form has an `L^3` density with

`||p_Q||_3 <= K_E E_2(M)^(-1/6)`,                              (3.17)

where

`K_E=2.983366279540...` at its `q=1` endpoint. Thus (3.12) yields the actual inequality

`boxed: ||p_Q||_3 <=4.842377 F^(-2/3)`                          (3.18)

on that diffuse-range subbranch. This is an `L^3` resource, not a claim that the full target is already paid. The localized-range branch and the genuine rank-one tube (3.11) remain to be joined to another original-coordinate smoother.

## 4. Two-sided bicore: return from spectral truncation to ACTUAL physical rows

Now take r22 alternative 4, so `T>=theta F^2` and (2.5) holds.

Let `N=P_L M P_R` be the selected singular core and let `E=M-N` be the omitted singular part. Because these are disjoint singular-direction pieces, their row vectors are orthogonal on the right and their column vectors are orthogonal on the left. Therefore for every physical row `u` and column `v`,

`||e_u^T M||_2^2
 =||e_u^T N||_2^2+||e_u^T E||_2^2`,                            (4.1)

`||M e_v||_2^2
 =||N e_v||_2^2+||E e_v||_2^2`.                                (4.2)

Consequently the heavy core coordinates from (2.5) are also heavy for the ACTUAL physical block `M`:

`alpha:=||e_i^T M||_2 >sqrt(T/450)
                         >=sqrt(theta/450)F`,                   (4.3)

`beta :=||M e_a||_2 >sqrt(T/450)
                         >=sqrt(theta/450)F`.                   (4.4)

This is important: no truncated matrix is used as a fake quadratic coefficient block below. All remaining determinants are determinants of the actual original-coordinate matrix `M`.

## 5. Main new bicore theorem: physical edge or an incident E2 bank

Permute the actual physical row `i` and column `a` to the front and write

`M=[[b,r^T],[c,D]]`.                                            (5.1)

Thus

`alpha^2=b^2+||r||^2`,
`beta^2 =b^2+||c||^2`,
`F=||M||_F`.                                                     (5.2)

Define the complete squared mass of physical `2x2` minors incident to row `i` and column `a`:

`Z_ia
 :=sum_{k!=i,l!=a}
   det M[{i,k},{a,l}]^2
 =||bD-c r^T||_F^2.`                                           (5.3)

### Lemma 5.1 — `QFORM-PHYSICAL-ROWCOL-EDGE-OR-E2-v1`

For every real matrix `M` and every physical row/column pair `(i,a)`, one of

`|b| > alpha beta/(4F)`                                         (5.4)

or

`boxed:
 ||r|| ||c|| >=(15/16) alpha beta,
 sqrt(Z_ia) >=(11/16) alpha beta
`                                                                    (5.5)

holds.

#### Proof

Assume (5.4) fails. Since `alpha,beta<=F`,

`|b|<=alpha beta/(4F)<=alpha/4`,
`|b|<=alpha beta/(4F)<=beta/4`.                                 (5.6)

Hence

`||r||=sqrt(alpha^2-b^2)>=(sqrt(15)/4)alpha`,
`||c||=sqrt(beta^2-b^2)>=(sqrt(15)/4)beta`,                     (5.7)

which gives the first inequality in (5.5). Also `||D||_F<=F`, so by the reverse triangle inequality in (5.3),

`sqrt(Z_ia)
 >=||c r^T||_F-|b| ||D||_F
 =||c|| ||r||-|b| ||D||_F
 >=(15/16)alpha beta-(1/4)alpha beta
 =(11/16)alpha beta`.                                          (5.8)

QED.

This lemma is intentionally aggregate. The conclusion is a complete incident `2x2` determinant bank, not one selected minor.

### Theorem 5.2 — `QFORM-BICORE-TO-PHYSICAL-E2-OR-EDGE-v1`

In r22 alternative 4, the ACTUAL cross block `M` has original physical coordinates `i,a` for which one of the following occurs:

**E. Physical edge branch**

`boxed: |M_ia| > (theta/1800) F.`                               (5.9)

Since the inherited four-bank packet has `CRF>kappa`, this branch carries the completely dimension-free five-bank resource

`boxed: C R |M_ia| > theta kappa/1800.`                         (5.10)

**V. Incident-volume branch**

The row and column stars are both large,

`boxed: ||M[i,-a]||_2 ||M[-i,a]||_2 > (theta/480)F^2,`          (5.11)

and the aggregate incident second-minor bank obeys

`boxed: sqrt(Z_ia) > (11 theta/7200)F^2,`                       (5.12)

or equivalently

`boxed: Z_ia > [121 theta^2/51840000]F^4.`                      (5.13)

#### Proof

Equations (4.3)-(4.4) give

`alpha beta > (theta/450)F^2`.                                  (5.14)

If Lemma 5.1 takes its edge branch, then

`|b|>alpha beta/(4F)>(theta/1800)F`,                            (5.15)

which proves (5.9), and multiplying by (2.1) proves (5.10).

Otherwise (5.5) and (5.14) give

`||r||||c||
 >(15/16)(theta/450)F^2
 =(theta/480)F^2`,                                              (5.16)

and

`sqrt(Z_ia)
 >(11/16)(theta/450)F^2
 =(11theta/7200)F^2`.                                          (5.17)

Squaring (5.17) gives (5.13). QED.

This is the main progress of the run. The previous spectral bicore survivor is returned to two purely physical alternatives: one substantial actual matrix coefficient, or one complete actual incident second-compound bank plus two disjoint physical stars.

### Equation-level application of completed account04 mathematics

The row star `r` is supported on the physical column bank with `a` removed, while the column star `c` is supported on the disjoint physical row bank with `i` removed. Their source variables are therefore genuinely independent ORIGINAL-coordinate families.

The completed account04/B18 product-projection consequence gives, for every original-coordinate coefficient bank `u`,

`||p_(u^T X)||_infinity <=sqrt(2)/||u||_2`.                     (5.18)

Applying (5.18) to both actual stars in (5.11) yields

`boxed:
 ||p_( r^T X_R, c^T X_L )||_infinity
 <=2/(||r||||c||)
 <960/(theta F^2).`                                             (5.19)

This is the requested equation-level use of completed account04 mathematics. It is retained as a product-provenance resource and is NOT promoted to a generic indefinite quadratic pushforward theorem.

If r22 alternatives 1 and 2 have failed, then `CR<=Lambda` and (2.1) gives `F>kappa/Lambda`. Therefore (5.19) also gives

`boxed:
 ||p_( r^T X_R,c^T X_L )||_infinity
 <960 Lambda^2/(theta kappa^2).`                                (5.20)

For the concrete r22 collar `theta=1/16`, `Lambda=1`, `kappa=1/(256sqrt(3))`, this is

`||p_( r^T X_R,c^T X_L )||_infinity <3019898880.`               (5.21)

The constant is intentionally not optimized; finiteness and product provenance are the point.

## 6. Concrete compiler at theta=1/16

With the r22 choice `theta=1/16`, alternative 4 now implies one of:

**E. Edge-times-outer-stars**

`|M_ia|>F/28800`,                                               (6.1)

and

`CR|M_ia|>kappa/28800
 =1/(7372800 sqrt(3))
 =7.83081419...e-8.`                                            (6.2)

**V. Inner two-star plus incident second-volume**

`||M[i,-a]|| ||M[-i,a]|| >F^2/7680`,                            (6.3)

`sqrt(Z_ia)>11F^2/115200`,                                     (6.4)

`Z_ia>9.117597415...e-9 F^4`.                                  (6.5)

The corresponding product-projection joint cap is `<15360/F^2`, or `<3019898880` after using `F>kappa` in the `Lambda=1` collar.

Combining Sections 3 and 5, the formerly broad unpaid r22 branches are now reduced to:

1. a relative `1/(2sqrt(2))` physical rank-one Frobenius tube;
2. a fixed aggregate `E_2(M)>=7F^4/128` bank, with a two-matching-bank realization `>=7F^4/2048` and an `L^3` payment whenever one range side is diffuse;
3. an edge-times-two-outer-stars product `CR|b|>theta kappa/1800`; or
4. an incident `E_2` bank plus two disjoint physical stars, with the exact bounds (5.11)-(5.13).

No dimension-dependent coordinate pigeonhole and no reciprocal individual minor appear in this compiler.

## 7. What remains unpaid

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.** No continuity statement is added by the new structural alternatives; continuity continues to hold only on the previously paid r22 diffuse-volume branch.

The first B07 implication is now

`QFORM-N3-PHYSICAL-E2-EDGE-RANKONE-RECEIVER-v1`:

- pay the genuine rank-one Frobenius tube without deleting the nonzero tail;
- consume the aggregate `E_2` bank in the localized-range case after the diffuse-range `L^3` exit (3.18);
- consume the edge-times-outer-stars packet (5.10) using a physical chain/pair/square compiler that retains arbitrary same-bank curvature; or
- consume the incident-volume/two-star packet (5.11)-(5.13), again retaining the true full quadratic pair Schur rather than a cross-only Schur surrogate.

The new account02/B06 physical-chain theorem is a promising receiver when an exact zero edge is genuinely present, but the live near-zero correction forbids using it by simply discarding a small nonzero term. The new account03/B06 pair-log `L^p` receiver is compatible once the **true** full-pair Schur remainder, rather than merely a cross-only anchored Schur block, carries the required aggregate `E_2` resource.

## 8. Deterministic checks

`CHECKS.py` and captured `CHECKS.txt` are stored beside this report. They use exact integer arithmetic to verify:

- the non-edge implications in Lemma 5.1 on every `2x2`, `2x3`, and `3x2` matrix with entries in `{-1,0,1}` (3,008 non-edge row/column cases);
- the `theta=eta=1/16` low-tail dichotomy on 180 sorted nonnegative integer spectra of lengths three through six satisfying the low-tail gate;
- the exact collar constants, including the projection cap `3019898880`.

The checks are diagnostics, not substitutes for the analytic proofs above.

## 9. Provenance / delivery boundary

No scheduler state, enabled/paused state, notification flag, email workflow, public release, paid API/model/Codex call, remote workflow, permission, or cross-account native state is changed by this mathematics. Repository transport is authenticated GitHub use; native learned-memory ingestion was not verified, so execution remains `WITHOUT_VERIFIED_BRAIN`.
