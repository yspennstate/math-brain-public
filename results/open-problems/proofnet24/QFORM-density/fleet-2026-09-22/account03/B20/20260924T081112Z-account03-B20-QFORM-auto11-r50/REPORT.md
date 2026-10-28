SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-24T08:11:12Z.
attacking: the r52 retained diffuse-residual/tail endpoint by converting sufficiently high residual spectral multiplicity into a literal physical cross-E3 payment, while preserving the latent carrier and the genuine nonzero tail.

# account03/B20 r50 — diffuse residual rank-five payment and bounded-rank residual funnel

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW TARGET-RELEVANT PAYMENT / NEW STRUCTURAL FUNNEL / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Authenticated repository access and writes are not native learned-memory ingestion.

Regularity: the new payment below gives a continuous `C_0` density on its exact branch. Full-target continuity remains **OPEN**.

All coordinate sets below are literal ORIGINAL-coordinate sets. No random coordinate is rotated. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, arbitrary-joint coarea, fiber-supremum, or law-uniform pointwise quadratic-phase decay assumption is used. No nonzero coefficient tail is deleted.

## 1. Fresh source-pinned frontier


The immediate same-account frontier is account03/B19 r52:

`yspennstate/math-open-problems@5ec1cc2bf208bc0249ea89d86fd7298b62ac324e`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T070220Z-account03-B19-QFORM-r52/REPORT.md`.

On the common-plane / BL-compatible branch, after conditioning only literal heavy physical coordinates and coordinates outside the two surviving light banks, the active coefficient block has the form

`diag(q) + W H_L W^T + (E_R direct_sum E_C) + T_cross`,          (1.1)

where

- `W=diag(U~,V~)` has four orthonormal coefficient columns and every physical row leverage is at most `1/2`;
- on either light bank the restriction of `W H_L W^T` has rank at most two;
- the genuine cross tail satisfies `||T_cross||op<2^-16` (indeed its underlying rectangular tail has Frobenius norm `<2^-16`);
- the residual self blocks are restrictions of the r49 residuals.

The r49 source is

`yspennstate/math-open-problems@b3922fe080467f7f34a7dd248460fa2478bc03d2`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T040014Z-account03-B19-QFORM-r49/REPORT.md`.

For each residual self block `E=E^T`, r49 proves

`max_j ||E e_j||_2 <= eta_0`,                                    (1.2)

with

`eta_0=0.08541402203824304... < 11/128`,                          (1.3)

and, more generally, for the spectral projection `P_s=1_{|E|>=s}`,

`max_j (P_s)_{jj} <= eta_0^2/s^2`.                               (1.4)

Restriction to a light bank can only decrease each column norm, so (1.2)-(1.4) remain valid for the actual residuals in (1.1).

The analytic terminal used below is the completed marginal-free physical-third-volume theorem

`QFORM-CROSS-E3-MARGINALFREE-L1-v1`, source-pinned in account01/B07 r31. For every literal disjoint original-coordinate cross block `M=A[I,J]`,

`V_3=e_3(MM^T)>0`

implies a continuous `C_0` density for the FULL ambient law and

`||p_Q||_infinity <= C_E3 V_3^(-1/6)`,                           (1.5)

where

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`.                 (1.6)

Arbitrary same-bank curvature, outside couplings, affine terms and signs remain in the law.

## 2. Rank-five residual extraction

### Theorem 2.1 — `QFORM-R52-DIFFUSE-RESIDUAL-RANK5-CROSSE3-PAYMENT-v1`

Work in the r52 active light-bank normal form (1.1). Let `E` be either actual residual self block `E_R` or `E_C`. If

`boxed: s_5(E) >= 9/4,`                                          (2.1)

then there exist two disjoint literal original-coordinate subsets `I,J` of that same physical bank such that the ACTUAL ambient coefficient cross block satisfies

`boxed: s_3(A[I,J]) > 3/128.`                                    (2.2)

Consequently the full target law has a continuous `C_0` density and

`boxed: ||p_Q||_infinity < 451.`                                 (2.3)

No coefficient of (1.1) is discarded.

### Proof

Put

`t_0=9/16`,                                                       (2.4)

and let `P=1_{|E|>=t_0}`. By (1.3)-(1.4),

`max_i P_ii < ((11/128)/(9/16))^2=(11/72)^2=121/5184=:epsilon.`   (2.5)

Let `U` be an orthonormal frame for `range(P)`, so `sum_i u_i u_i^T=I` and `||u_i||^2=P_ii<=epsilon`. The two-part Marcus-Spielman-Srivastava frame partition used in the completed ridge-window theorem gives a literal partition of the residual bank

`I union J`, `I cap J=empty`,                                    (2.6)

such that both partial Gram matrices satisfy

`U_I^T U_I >= delta I`, `U_J^T U_J >= delta I`,                  (2.7)

where

`delta=1-(1/sqrt(2)+sqrt(epsilon))^2`
`     =1/2-121/5184-sqrt(242)/72`
`     =0.2605985452547277... .`                                  (2.8)

Write the spectral truncation

`E_H=U Lambda U^T`, `F=E-E_H`.                                   (2.9)

Then `||F||op<t_0`. By thin QR on `U_I,U_J`, the nonzero singular values of `E_H[I,J]` are those of

`(U_I^T U_I)^(1/2) Lambda (U_J^T U_J)^(1/2`),                    (2.10)

so (2.1),(2.7) imply

`s_5(E_H[I,J]) >= delta*(9/4)`.                                  (2.11)

Restriction cannot increase operator norm, hence Weyl gives

`s_5(E[I,J]) > (9/4)delta-9/16`
`             =(9/4)(delta-1/4)=:sigma_*`.                       (2.12)

This constant is strictly larger than `3/128`. Indeed, `sigma_*>3/128` is equivalent to

`sqrt(242)/72 < 1121/5184`,                                      (2.13)

and both sides are positive while

`242*5184=1254528 <1256641=1121^2`.                              (2.14)

Numerically `sigma_*=0.02384672682313746...`, while `3/128=0.0234375`.

Now examine the ACTUAL physical cross block of `A` between the same two subsets. The coordinate-separable diagonal contributes nothing across `I,J`. The r52/r49 aligned self carrier on this bank has rank at most two; call its cross restriction `K[I,J]`, still of rank at most two. The retained `T_cross` lives between the two main banks and therefore contributes nothing to a within-bank `I x J` block. Thus

`A[I,J]=E[I,J]+K[I,J]`, `rank K[I,J]<=2`.                         (2.15)

For approximation numbers, adding a rank-at-most-two matrix cannot move the fifth singular value below the third slot:

`s_3(A[I,J]) >= s_5(E[I,J]) >3/128`.                             (2.16)

Hence

`V_3=e_3(A[I,J]A[I,J]^T) >= s_1^2 s_2^2 s_3^2 > (3/128)^6`.      (2.17)

Apply the marginal-free physical-E3 theorem (1.5):

`||p_Q||_infinity`
` < C_E3*(3/128)^(-1)`
` =128*2^(4/3)*exp(1/3)`
` =450.140536796... <451`.                                       (2.18)

The source theorem gives continuity and vanishing at infinity. QED.

## 3. New unpaid normal form

The contrapositive is the useful compiler. If the new payment does not fire on either light bank, then

`boxed: s_5(E_R)<9/4,  s_5(E_C)<9/4.`                            (3.1)

For each residual take its top-four spectral truncation `G_R,G_C`. Then

`rank G_R,rank G_C<=4`,                                          (3.2)

and the exact remainders obey

`||E_R-G_R||op<9/4`, `||E_C-G_C||op<9/4`.                        (3.3)

Therefore the entire r52 light block can be rewritten exactly as

`A_light=diag(q)+K_12+F`,                                        (3.4)

where

`rank K_12<=4+4+4=12`                                            (3.5)

(the four-latent carrier plus the two residual top-four pieces), and

`boxed: ||F||op < 9/4 + 2^-16 =2.2500152587890625.`              (3.6)

Here `F` includes both block-diagonal low residuals and the genuine cross tail; it remains in the coefficient matrix and is not treated as a small random perturbation.

On the r52 determinant-collapse subbranch, the normalized four-latent matrix is within

`112*2^-20=0.0001068115234375`                                   (3.7)

of rank at most three. Pushing that coefficient-space approximation back through the orthonormal physical frame shows that (3.4) can be sharpened there to

`A_light=diag(q)+K_11+F_collapse`,                               (3.8)

with

`rank K_11<=11`,                                                  (3.9)

and

`||F_collapse||op < 9/4+2^-16+112*2^-20`
`                    =2.2501220703125.`                           (3.10)

Again, the retained operator tail is structural bookkeeping only, not permission to drop its random quadratic contribution.

Thus the first analytic debt in r52 has been narrowed: arbitrarily high spectral multiplicity in a row-small residual is no longer an unpaid case. Every unpaid residual has at most four singular directions above `9/4`.

## 4. Designated account04/B20 result applied at an actual inequality

The designated partner source is account04/B20 r13:

`yspennstate/math-open-problems@d2560a041fd91c05d7fddf50f5b5414ecd2680a2`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260924T051424Z-account04-B20-QFORM-r13/REPORT.md`.

On its transverse double-anchor branch at `epsilon=1/64`, it produces a literal original-coordinate cross block

`M=A[K,{i,j}]`                                                    (4.1)

with

`boxed: s_2(M)>=mu`,
`mu=4.6565947316667495e-10`                                      (4.2)

at target scale `L=1`. Because `M` has exactly two columns,

`Omega=e_2(MM^T)=s_1(M)^2 s_2(M)^2 >=mu^4`.                     (4.3)

Apply the completed marginal-free E2-lift overlap funnel `QFORM-E2-LIFT-MARGINALFREE-OVERLAP-FUNNEL-v1` at its concrete parameter `tau=1/144`. This yields the exhaustive actual inequality:

- either the FULL ambient law has a continuous density with

`||p_Q||infinity <48.307715 Omega^(-1/6)`
`                 <=48.307715 mu^(-2/3)`
`                 <8.05e7`;                                     (4.4)

- or a role-consistent physical overlap-one or overlap-two E3 packet survives with mass

`boxed: P > (5/12447) Omega >=(5/12447)mu^4`
`       >1.88e-41.`                                               (4.5)

The second number is tiny but strictly dimension-free and source-valid. This turns the partner's transverse double-anchor leaf into a terminal continuous payment or an explicit shared-coordinate third-volume packet; it is not replaced by a generic bounded-joint-density surrogate.

The partner's aligned collar and the already-separated strong-edge leaf remain distinct geometries. No claim is made that (4.5) by itself is terminal.

## 5. Compact proof assembly after this run

The best current route now reads:

1. existing principal-minimal descent and the completed diagonal, physical-pair, pair-log, principal-triple, marginal-free physical-E3, ridge/window, grouped, null-coloop and rank-two fractional receivers pay their exact branches;
2. r47-r51 reduce a major hard chamber to a BL-compatible robust physical rank-two crossing or finite physical hub/star exits;
3. r52 completely pays the exact nonsingular four-latent skeleton and turns determinant failure into an explicit near-rank-three latent collapse, while correctly retaining `E_R,E_C,T_cross`;
4. the present theorem pays every r52 residual carrying five singular values at least `9/4`, despite the arbitrary rank-two aligned self carrier on the same bank;
5. hence the still-unpaid retained-residual branch has the exact rank-12 plus bounded-operator-tail normal form (3.4)-(3.6), and rank-11 in the determinant-collapse subbranch.

The first remaining implication on this route is now

`QFORM-R52-LOWRESIDUAL-R12/R11-RETAINED-TAIL-ENDPOINT-v1`:

> pay the rank-at-most-12 (rank-at-most-11 in determinant collapse) carrier coupled to the retained operator tail in (3.6)/(3.10), or force an already-completed physical pair, physical-E3, grouped-star, hub+square, ridge/window or incident-volume receiver. The operator tail cannot be discarded, and its bound is still larger than the target spectral scale.

A second explicit subgoal is to spend the partner overlap packet (4.5) in its shared-coordinate geometry rather than trying to select one tiny minor.

## 6. Quantifiers and correction boundaries

The theorem is sign-free. It tolerates repeated eigenvalues and exact degeneracies. All partitions are of original physical coordinates; only coefficient-space spectral/SVD calculations are used. No independence is asserted after any coefficient rotation. The marginal-free physical-E3 theorem carries all same-bank curvature and outside couplings, so the payment is for the full ambient law rather than a projected surrogate.

The run does not use the refuted pointwise van-der-Corput claim, arbitrary-joint coarea, projection-density control of an indefinite pushforward, naive fiber-sup integration, Monte Carlo extremality, or deletion of a small coefficient tail.

Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.

Full universal continuous-density conclusion: **OPEN**.

New branch (2.1): **continuous `C_0` density, `||p_Q||infinity<451`**.
