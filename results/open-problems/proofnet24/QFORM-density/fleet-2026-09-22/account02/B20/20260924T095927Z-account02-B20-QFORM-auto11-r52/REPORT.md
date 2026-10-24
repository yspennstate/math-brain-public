SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-24T09:59:27Z.
attacking: the pair-free moderate-residual frontier by closing the previously untreated definite physical-pair sign, then re-optimizing the row-small residual split before testing whether the surviving rank-three diffuse obstruction is genuinely pair-free.

# account02/B20 r52 — all-sign physical-pair gate + sharper moderate-residual funnel

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW COMPLETE DEFINITE-PAIR RECEIVER / ALL-SIGN PAIR-FREE GATE / RESIDUAL THRESHOLD SHARPENED / TARGET-VALID DIFFUSE SURVIVOR / FULL QFORM OPEN**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Authenticated repository retrieval/writeback is not native learned-memory receiver ingestion.

All coordinate sets below are literal ORIGINAL-coordinate sets. No random coordinate is rotated. No Gaussianity, log-concavity, moments, compact/connected support, iid hypothesis, arbitrary-joint coarea, worst-fibre supremum, conditional density-cap inheritance after projection, or law-uniform pointwise quadratic-phase decay is used. Every nonzero coefficient tail is retained.

## 1. Fresh source-pinned frontier

Fresh `math-research-brain/main` startup control was read at `9fe4d883b7cb59a26dbc1f20faeca18ec9cb7cab`; OWNER CONTROL remains revision `2026-09-22.15` and QFORM is the sole active programme.

Newest compatible completed designated partner: account03/B20 r51,

`yspennstate/math-open-problems@ceb973b9c1549a8247baf169db9152844b9decde`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T091209Z-account03-B20-QFORM-auto11-r51/REPORT.md`.

Its live strong-edge certificate is a literal original-coordinate invertible indefinite principal pair `P` with

`D=|det P| >= D0 = 9.530157744638501e-7`,

`kappa=s_min(P) >= kappa0 = 6.075614261408114e-5`.

The preceding account02/B20 r51 closure applied the arbitrary-rank physical-pair theorem to that exact pair and proved

`||p_Q||_infinity < 9763`.

Thus the partner's later ultrathin rank-six bookkeeping is not an unpaid endpoint. The global synthesis frontier returns to the r50/r52 moderate-residual branch, but until now the quantitative pair-free gate recorded only **indefinite** pairs. The first result below closes the missing definite sign and turns that into an all-sign physical-pair gate.

The inherited r50/r52 light-bank normal form is

`A_light = diag(q) + W H_L W^T + (E_R direct_sum E_C) + T_cross`,

where `W` has four orthonormal coefficient columns, each physical row leverage is at most `1/2`, each same-bank aligned carrier has rank at most two, `||T_cross||op<2^-16`, and each symmetric residual satisfies

`max_j ||E e_j||_2 <= eta0`,

`eta0 = 20865 sqrt(2)/4194296 + 2629953/33554368`
`     = 0.08541402203824304...`.

The preceding account02/B20 r50 paid `s_5(E)>=43/20=2.15`, leaving an exact rank-12 carrier plus retained tail `<2.1500152587890625` (rank 11, tail `<2.1501220703125` on latent determinant collapse). Section 3 improves this threshold.

The owner-required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

`RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` were read. Its unrestricted physical fifth-volume theorem D5 is applied at the actual residual-bank cuts in Section 4, and its product-preserving Theorem H is applied to the stress family in Section 5.

## 2. Definite physical pairs are terminal

### Theorem 2.1 — `QFORM-FULL-MATRIX-DEFINITE-PAIR-v1`

Let `A=A^T` be arbitrary, let `X_1,...,X_n` be independent real variables with densities at most one, and let two ORIGINAL coordinates have an invertible **definite** principal block `B`. Put

`D=|det B|>0`.

Then for arbitrary remaining blocks, couplings, affine terms and constants, the full quadratic polynomial

`Q=X^T A X+b^T X+d`

has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <= pi D^(-1/2).`                         (2.1)

No spectral hypothesis on the rest of `A` is needed.

#### Proof

Write the chosen original coordinate pair as `Y in R^2` and all remaining original coordinates as `Z`. Conditional on `Z=z`,

`Q = Y^T B Y + 2 h(z)^T Y + r(z)`.

Because the two selected coordinates are original independent coordinates, their joint conditional density is their original product density and is pointwise at most one. Complete the square:

`Q = (Y+B^{-1}h)^T B (Y+B^{-1}h) + R(z)`.

If `B` is positive definite, put `U=B^(1/2)(Y+B^{-1}h)`; if negative definite use `U=(-B)^(1/2)(Y+B^{-1}h)`. In either case the conditional density of `U` is at most `D^(-1/2)`, and the random scalar is `+|U|^2+R(z)` or `-|U|^2+R(z)`.

For every `s>0`,

`integral_{R^2} delta(|u|^2-s) du = pi`.

Equivalently, the pushforward of a planar density bounded by `M` under `u -> |u|^2` has density bounded by `pi M`. Hence every conditional law of `Q|Z=z` has density bounded by `pi D^(-1/2)`. Mixing over `z` preserves this bound by Tonelli. The negative-definite case is identical after reflection. QED.

### Corollary 2.2 — `QFORM-R51-ALLSIGN-PHYSICAL-PAIR-GATE-v1`

At the newest partner's exact determinant scale

`D0=9.530157744638501e-7`,

any literal definite physical principal pair with `|det B|>=D0` pays the full ambient law by

`boxed: ||p_Q||_infinity <= pi/sqrt(D0)`
`                         = 3218.1021692528298... <3219.`          (2.2)

Combining this with the already-completed r51 indefinite-pair closure at the partner's exact

`kappa0=6.075614261408114e-5`

gives the following necessary condition for every still-unpaid target instance:

1. every invertible definite literal physical pair `B` satisfies `|det B|<D0`;
2. every invertible indefinite literal physical pair `B` satisfies either `|det B|<D0` or `s_min(B)<kappa0`.

This is strictly stronger than the preceding indefinite-only pair-free gate. It is a target-level gate on the **actual coefficient matrix A**, not on a rotated or residual surrogate.

## 3. Re-optimizing the row-small residual extraction

The previous residual threshold `43/20=2.15` is not intrinsic. Keeping the same MSS mechanism but choosing the spectral cutoff near its optimum improves the funnel.

### Theorem 3.1 — `QFORM-R52-ROWSMALL-S5-2P1455-CROSSE3-PAYMENT-v1`

In the inherited r50/r52 normal form, let `E` be either actual residual self block. If

`boxed: s_5(E) >= S0 := 4291/2000 = 2.1455,`                     (3.1)

then there are disjoint literal physical subsets `I,J` of that same bank such that the ACTUAL ambient cross block has

`boxed: s_3(A[I,J]) > m1 > 4.2961e-5,`                           (3.2)

and consequently the completed marginal-free physical-E3 theorem gives the full ambient law a continuous `C_0` density with

`boxed: ||p_Q||_infinity <245574.`                               (3.3)

No coefficient tail is deleted.

#### Proof

First use exact arithmetic to record the safe rational row bound

`eta0 < 17083/200000 =0.085415`.                                 (3.4)

Indeed, after moving the rational term in `eta0`, the difference is positive because both sides are positive and the difference of their squares is

`2254631/163839687500000 >0`.

Choose the spectral cutoff

`t0=1403/2500=0.5612`,                                           (3.5)

and let `P=1_{|E|>=t0}`. Functional calculus gives

`P_jj <= ||Ee_j||_2^2/t0^2 < r^2`,

where

`r=(17083/200000)/(1403/2500)=17083/112240`.                    (3.6)

Let `U` be an orthonormal frame for `range(P)`. The same two-part MSS frame partition already used in r50 gives a literal partition `I union J` of the bank with

`U_I^T U_I >= delta I`, `U_J^T U_J >= delta I`,                 (3.7)

where the explicit safe lower bound is

`delta = 1-(1/sqrt(2)+r)^2`
`      = 1/2-r^2-r sqrt(2)`
`      =0.2615907533458146... .`                                 (3.8)

Write `E_H=U Lambda U^T`, `F=E-E_H`. Then `||F||op<t0`. If (3.1) holds, thin QR gives

`s_5(E_H[I,J]) >= delta S0`,                                     (3.9)

and restriction plus Weyl gives

`s_5(E[I,J]) > delta S0-t0 =:m1`.                               (3.10)

The margin is rigorously positive. Writing

`m1 = A0-B0 sqrt(2)`,

one has

`A0=11636589423861/25195635200000`,
`B0=73303153/224480000`,

and

`A0^2-2B0^2`
`=25190585886196418150521/634820033131479040000000000 >0`.

Numerically

`m1=0.000042961303445...`.

Across this within-bank cut, the physical coordinate diagonal contributes zero, `T_cross` lies between the two main banks and contributes zero, and the aligned same-bank carrier has rank at most two. Thus

`A[I,J]=E[I,J]+K[I,J]`, `rank K[I,J]<=2`.

Approximation-number interlacing yields

`s_3(A[I,J]) >= s_5(E[I,J]) >m1`.                               (3.11)

Therefore

`e_3(A[I,J]A[I,J]^T) >m1^6`.

The completed marginal-free physical-E3 receiver has

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`,

so

`||p_Q||_infinity < C_E3/m1 =245573.7603... <245574`.

The large numerical constant is harmless; the point is the lower structural threshold. QED.

### Corollary 3.2 — sharpened unpaid carrier/tail form

If Theorem 3.1 does not fire on either residual, then

`s_5(E_R)<2.1455`, `s_5(E_C)<2.1455`.

Taking the top four spectral directions of each residual gives exactly

`boxed: A_light=diag(q)+K_12+F, rank K_12<=12,`
`       `||F||op<2.1455+2^-16`
`                =2.1455152587890625.`                           (3.12)

On the latent determinant-collapse branch the already-proved `112*2^-20` rank-three approximation gives

`boxed: A_light=diag(q)+K_11+F_collapse, rank K_11<=11,`
`       `||F_collapse||op<2.1455+2^-16+112*2^-20`
`                         =2.1456220703125.`                      (3.13)

The genuine tails remain in the coefficient matrix and are not interpreted as small random perturbations.

For reference, optimizing the same one-parameter argument formally with the exact `eta0` gives cutoff ratio

`t/eta0 = 2 sqrt(2)+sqrt(14)`

and limiting threshold `2.1453112039853264...`; thus `2.1455` is a safe rationalized gate close to the best available from this unchanged MSS mechanism. Further attempts should change mechanism rather than chase this constant.

## 4. Required pinned fifth-volume theorem applied to the actual live cuts

For either literal MSS residual-bank split `I,J` constructed in Section 3, put

`Z5=e_5(A[I,J]^T A[I,J])`.

The pinned `e5f71d79eff325201dd0274053d20268ce65b837` Theorem D5 is marginal-free and applies to the **full ambient quadratic law** on this actual original-coordinate cut:

`||p_Q||_infinity <=5 sqrt(2e) Z5^(-1/10)`.                     (4.1)

Hence

`Z5>=1/1024`

implies

`boxed: ||p_Q||_infinity <=10 sqrt(2e)`
`                         =23.316439815971243...<23.317.`          (4.2)

Therefore every state surviving both Theorem 3.1 and the pinned D5 exit may additionally be assumed to have `Z5<1/1024` on both constructed residual-bank splits. This is an equation-level application of the required pinned completed result.

## 5. The previous rank-three stress is not all-sign pair-free; a larger diffuse stress is

The r50 report used a Walsh rank-three residual family to show that the target does not force a fifth residual singular direction. The new definite-pair theorem reveals a useful correction: at the old dimension `m=1024`, that family is **not** pair-free in the strengthened all-sign sense.

### Proposition 5.1 — semidefinite rank-three pair-volume identity

If `E=E^T>=0` has at least three eigenvalues at least `sigma>0`, then

`sum_{i<j} det E[{i,j}] = e_2(E) >=3 sigma^2`.                   (5.1)

Consequently, if all its physical `2x2` principal determinants are below `D0`, an `m x m` such matrix must satisfy

`binom(m,2) D0 >3 sigma^2`,                                      (5.2)

so

`m > (1+sqrt(1+24 sigma^2/D0))/2`.                              (5.3)

At `sigma=1` and the partner determinant scale `D0`, the right side is

`2509.644017...`,

hence `m>=2510` is necessary.

Proof: (5.1) is the standard principal-minor formula for `e_2`; positivity of the spectrum makes every term in the eigenvalue expression nonnegative and the three unit-scale eigenvalues contribute at least three pair products. QED.

In the old flat three-Walsh projection at `m=1024`, a suitable physical pair has determinant

`8/m^2 =7.62939453125e-6 >D0`,

so Theorem 2.1 already pays it. The construction remains a valid obstruction to “force a fifth residual mode”, but it is not a survivor of the stronger all-sign pair-free gate.

### Proposition 5.2 — `QFORM-R52-PAIRFREE-DIFFUSE-R3-STRESS-v1`

The all-sign gate still does **not** eliminate diffuse rank-three residual geometry. Take instead `m=4096`; choose five flat orthonormal Walsh vectors `u_1,...,u_5` on a bank `R` and two flat orthonormal Walsh vectors `v_1,v_2` on a disjoint bank `C`. Put

`U=(u_1,u_2)`, `V=(v_1,v_2)`, `c=1/64`,

`E_R=u_3u_3^T+u_4u_4^T+u_5u_5^T`,

and

`A=[[E_R, c U V^T],[c V U^T,0]]`.                              (5.4)

Then:

1. the nonzero spectrum is exactly `{1,1,1,c,c,-c,-c}`, so `s_3(A)=1`;
2. `E_R` is a rank-three orthogonal projection with `s_5(E_R)=0`;
3. `max_j ||E_R e_j||=sqrt(3/m)=sqrt(3)/64=0.0270632938...<eta0`;
4. every definite physical pair inside `R` has determinant at most
   `8/m^2=4.76837158203125e-7<D0`;
5. every cross-bank principal pair is indefinite or singular and has determinant magnitude at most
   `1/(1024 m^2)=5.820766091346741e-11<D0`;
6. pairs inside `C` are singular.

Thus the exact target and the strengthened all-sign pair-free gate can coexist with a genuinely diffuse rank-three residual. This is a counterexample only to the stronger structural shortcut “the all-sign pair gate eliminates moderate rank-three residuals”; it is **not** a QFORM counterexample.

Indeed the pinned Theorem H pays this family directly. The seven coefficient vectors form an orthonormal physical frame with maximum row leverage `5/m<1/2`, and the coefficient eigenvalues are `1,1,1,c,c,-c,-c`. The same exact calculation as in r50 gives

`|phi_Q(t)| <=(4 pi)^(7/2)c^(-2)|t|^(-7/2)`

and after integrating `min(1,K|t|^-7/2)`,

`boxed: ||p_Q||_infinity <=(28/5)c^(-4/7)`
`                         =(28/5)64^(4/7)`
`                         =60.2963286299...<61.`                 (5.5)

This exhibits the mechanism the unpaid branch still needs: very diffuse rank-three/rank-four residual energy can itself be a product-preserving Fresnel smoothing resource when combined before taking absolute values.

## 6. Strongest current conditional assembly and first unpaid implication

After consuming account03/B20 r51 and the new results above, the strongest current synthesis branch is:

1. all previously completed diagonal, physical-pair, pair-log, principal-triple, marginal-free physical-E3, D5, ridge/window, grouped-star, hub+square, null-coloop and fractional receivers retain their exact scopes;
2. newest partner r51's strong-edge leaf is fully terminal by the arbitrary-rank indefinite-pair receiver, `<9763` at its exact `D0,kappa0`;
3. Theorem 2.1 closes the missing definite-pair sign, so every unpaid target state satisfies the all-sign physical-pair gate of Corollary 2.2;
4. on the r50/r52 common-plane moderate-residual branch, Theorem 3.1 lowers the residual fifth-singular threshold from `2.15` to `2.1455`, yielding the exact rank-12/rank-11 retained-tail ceilings (3.12)-(3.13);
5. the pinned D5 exit may be assumed failed on the two actual optimized MSS residual-bank splits;
6. Proposition 5.2 proves that even these strengthened conditions do not force a large physical pair or fifth residual mode: the surviving obstruction can be an extremely diffuse rank-three Fresnel resource.

The first unpaid universal implication is therefore sharpened to

`QFORM-R52-ALLSIGN-PAIRFREE-MODERATE-RESIDUAL-JOINT-FRESNEL-ENDPOINT-v1`:

> Under the full independent cap-one product hypotheses and the r52 common-plane/BL-compatible normal form, assume the all-sign physical-pair gate at `(D0,kappa0)`, both row-small residuals satisfy `s_5<2.1455`, the two concrete optimized residual-bank D5 currencies are `<1/1024`, and retain the genuine cross tail `<2^-16`. Pay the resulting rank-at-most-12 carrier plus retained tail (rank at most 11 on determinant collapse), or source-preservingly convert a diffuse rank-three/rank-four residual together with the four-latent crossing into a product-preserving Fresnel/BL, grouped-star/hub, ridge/window, physical-E3, D5, or incident-volume receiver.

The next mechanism should be **joint Fresnel aggregation**, not a fourth round of threshold tuning: Section 3 is within `0.00019` of the optimum obtainable from the same MSS cutoff calculation, while Proposition 5.2 gives a target-valid pair-free family that is paid precisely by retaining several diffuse coefficient directions jointly.

## 7. Correction boundaries and status

No projected random vector is treated as independent. Coefficient spectral/SVD operations are used only to choose literal physical subsets and estimate singular values. No worst-fibre supremum, conditional density cap after projection, arbitrary-joint rank-three coarea, generic fractional-small-ball-to-`L^infinity` interpolation, or law-uniform pointwise scalar oscillatory decay is used. Small operator norm is never interpreted as a small random quadratic perturbation.

Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

No valid counterexample to the owner target was found.

Unrestricted continuity: **OPEN**. The E3/D5/Theorem-H branches quoted above provide continuity only on their exact scopes; Theorem 2.1 asserts essential boundedness for the definite-pair branch without separately claiming a continuous representative.

This is not a full candidate proof, so the two-independent-end-to-end-review requirement is not triggered.
