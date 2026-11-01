SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-24T09:12:56Z.
attacking: fleet03/B20 r50's first unpaid low-residual rank-12/rank-11 retained-tail endpoint by lowering the row-small residual fifth-singular payment threshold with exact MSS/Weyl bookkeeping, then isolating the genuinely moderate-rank residual obstruction.

# fleet02/B20 r50 — sharpened row-small residual payment and moderate-rank obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW TARGET-RELEVANT PAYMENT / RETAINED-TAIL CONSTANT IMPROVED / TARGET-VALID STRUCTURAL OBSTRUCTION / FULL QFORM OPEN**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Authenticated repository retrieval/writeback is not native learned-memory receiver ingestion.

All coordinate sets below are literal ORIGINAL-coordinate sets. No random variable is rotated. No Gaussianity, log-concavity, moments, compact/connected support, iid hypothesis, arbitrary-joint coarea, worst-fibre supremum, conditional cap, or law-uniform pointwise quadratic-phase decay is used. Every nonzero coefficient tail is retained.

## 1. Source-pinned frontier


Newest compatible completed designated partner: fleet03/B20 r50,

`yspennstate/math-open-problems@46b6315c1980f6c0d76644cc4bb52a812c611496`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260924T081112Z-fleet03-B20-QFORM-auto11-r50/REPORT.md`.

Its active r52 light-bank normal form is

`A_light = diag(q) + W H_L W^T + (E_R direct_sum E_C) + T_cross`,

where `W` has four orthonormal coefficient columns, every physical row leverage of `W` is at most `1/2`, the aligned self carrier on either bank has rank at most two, and `||T_cross||op<2^-16`. For either symmetric residual self block `E`, the partner imports the exact row-small estimate

`max_j ||E e_j||_2 <= eta_0`,

with

`eta_0 = 20865 sqrt(2)/4194296 + 2629953/33554368`
`      = 0.08541402203824304...`.

The partner r50 theorem paid `s_5(E)>=9/4` by a physical cross-E3 exit, leaving the exact unpaid compiler

`A_light = diag(q)+K_12+F`, `rank K_12<=12`, `||F||op<9/4+2^-16`,

and rank `<=11`, tail `<9/4+2^-16+112*2^-20` on the determinant-collapse subbranch.

The pinned source required by the owner is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. I use its proved Theorem H and its proved unrestricted fifth-volume Theorem D5 below at actual physical cuts.

## 2. Exact constant sharpening of the r50 residual split

### Theorem 2.1 — `QFORM-R50-ROWSMALL-S5-2P15-CROSSE3-PAYMENT-v1`

In the partner r50/r52 normal form above, let `E` be either actual residual self block. If

`boxed: s_5(E) >= 43/20 = 2.15,`

then there are disjoint literal physical subsets `I,J` of that same bank for which the ACTUAL ambient cross block obeys

`boxed: s_3(A[I,J]) > m_0,`

where

`m_0 = (578533 - 408500 sqrt(2))/1250000`
`    = 0.000661407816472538... >0`.

Consequently the completed marginal-free physical-E3 theorem gives the FULL ambient law a continuous `C_0` density and

`boxed: ||p_Q||_infinity < 15952.`

No coefficient tail is deleted.

### Proof

The exact partner expression for `eta_0` gives the clean rational bound

`eta_0 < 171/2000 =0.0855`.

Indeed

`171/2000-eta_0 = 3(9956061-6955000 sqrt(2))/4194296000 >0`,

and positivity follows after squaring because

`9956061^2 - 2*6955000^2 = 2379100635721 >0`.

Use the same physical spectral cutoff as partner r50,

`t_0=9/16`.

Let `P=1_{|E|>=t_0}` and let `U` be an orthonormal frame for `range(P)`. Row-smallness gives

`P_jj <= eta_0^2/t_0^2 < (19/125)^2`.

The same proved two-part MSS frame partition used by partner r50 therefore gives a literal partition `I union J` of the bank such that

`U_I^T U_I >= delta_0 I`, `U_J^T U_J >= delta_0 I`,

with the explicit lower bound

`delta_0 = 1-(1/sqrt(2)+19/125)^2`
`        = 1/2 - 19 sqrt(2)/125 -361/15625`
`        = 0.26193553851928955...`.

Write the spectral truncation `E_H=U Lambda U^T` and `F_0=E-E_H`; then `||F_0||op<t_0`. If `s_5(E)>=43/20`, then the fifth singular value of `Lambda` is at least `43/20`. Thin QR on `U_I,U_J`, exactly as in partner r50, gives

`s_5(E_H[I,J]) >= delta_0*(43/20)`.

Restriction does not increase operator norm, so Weyl gives

`s_5(E[I,J]) > (43/20)delta_0 -9/16 = m_0`.

The displayed closed form for `m_0` follows by direct simplification. It is strictly positive because

`578533^2 - 2*408500^2 = 955932089 >0`.

Across this within-bank physical cut, the coordinate diagonal contributes nothing, the genuine `T_cross` lies between the two main banks and contributes nothing, and the aligned self carrier has rank at most two. Hence

`A[I,J]=E[I,J]+K[I,J]`, `rank K[I,J]<=2`.

The rank-two approximation-number shift gives

`s_3(A[I,J]) >= s_5(E[I,J]) >m_0`.

Therefore

`e_3(A[I,J]A[I,J]^T) >= s_1^2 s_2^2 s_3^2 > m_0^6`.

The completed marginal-free physical-E3 receiver used by partner r50 has constant

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`,

so

`||p_Q||_infinity < C_E3/m_0 =15951.079755... <15952`.

The receiver retains arbitrary same-bank curvature, outside couplings, affine terms, signs, extra spectrum and all nonzero tails. QED.

### Corollary 2.2 — sharpened unpaid normal form

If Theorem 2.1 does not fire on either light-bank residual, then

`s_5(E_R)<43/20`, `s_5(E_C)<43/20`.

Taking the top-four spectral truncation of each residual gives exactly

`boxed: A_light=diag(q)+K_12+F, rank K_12<=12, ||F||op<43/20+2^-16}`

and therefore

`boxed: ||F||op<2.1500152587890625.`

On the determinant-collapse branch, incorporating the already-proved `112*2^-20` latent rank-three approximation gives

`boxed: A_light=diag(q)+K_11+F_collapse, rank K_11<=11,`
`       `||F_collapse||op<2.1501220703125.`

This strictly improves the partner r50 tail ceilings `2.2500152587890625` and `2.2501220703125` while preserving the tail as an actual coefficient matrix.

## 3. Required pinned fifth-volume application at the same actual cut

For each MSS physical split `I,J` above, put

`Z_5=e_5(A[I,J]^T A[I,J])`.

The pinned `e5f71d79...` Fourier-route Theorem D5 is marginal-free and applies to the full ambient quadratic law on any literal disjoint physical cut:

`||p_Q||_infinity <=5 sqrt(2e) Z_5^(-1/10)`.

Thus on these actual residual-bank splits,

`Z_5>=1/1024`

implies

`boxed: ||p_Q||_infinity <=10 sqrt(2e)=23.3164398159...<23.317.`

Hence every state surviving both the pinned D5 exit and Theorem 2.1 may additionally be assumed to have `Z_5<1/1024` on both constructed residual-bank splits. This is an equation-level use of the required pinned source, not a background citation.

## 4. Why forcing a fifth residual mode cannot close the endpoint

### Proposition 4.1 — `QFORM-R50-MODERATE-RANK3-RESIDUAL-OBSTRUCTION-v1`

The full three-large-eigenvalue target does not force `s_5(E)>0`, even inside a quantitatively compatible common-plane/rank-two-crossing normal form with row-small residual and zero cross tail.

Take `m=1024` and choose five flat orthonormal Walsh vectors `u_1,...,u_5` on a physical row bank `R`, and two flat orthonormal Walsh vectors `v_1,v_2` on a disjoint bank `C`. Put

`U=(u_1,u_2)`, `V=(v_1,v_2)`, `c=1/64`,

`E_R = u_3u_3^T+u_4u_4^T+u_5u_5^T`, `E_C=0`,

and

`A = [[E_R, c U V^T], [c V U^T, 0]]`.

Then:

1. `A[R,C]` has singular values exactly `c,c`, so the robust physical rank-two crossing is present and its tail is exactly zero.
2. The four-latent crossing frame `diag(U,V)` has physical row leverage at most `2/m<1/2`.
3. `E_R` is a rank-three orthogonal projection, so
   `s_1(E_R)=s_2(E_R)=s_3(E_R)=1` and `s_5(E_R)=0`.
4. Since `E_R^2=E_R` and every Walsh row has squared norm `3/m` in the residual three-plane,
   `max_j ||E_R e_j||_2=sqrt(3/m)=sqrt(3)/32=0.0541265...<eta_0`.
5. On the seven mutually orthogonal coefficient directions `(u_3,u_4,u_5,u_1,u_2,v_1,v_2)`, the nonzero spectrum of `A` is exactly
   `{1,1,1,c,c,-c,-c}`.
   Hence the owner target holds: `s_3(A)=1`.

Thus no target-level closure may assert that the r50 low-residual survivor must acquire five target-scale residual singular directions, or that the four-latent crossing carrier itself must carry the third target-scale eigenvalue. Here all three unit modes sit in a rank-three diffuse residual.

This is **not** a counterexample to QFORM. In fact it is source-validly paid by the pinned Theorem H. The seven coefficient vectors form an orthonormal physical frame whose maximum row leverage is `5/m<1/2`; applying Theorem H with zero hubs and rank `r=7` gives

`|phi_Q(t)| <= (4 pi)^(7/2) c^(-2) |t|^(-7/2)`.

Integrating `min(1,K|t|^-7/2)` exactly yields

`||p_Q||_infinity <= (28/5)c^(-4/7)`
`                 = (28/5)64^(4/7)`
`                 =60.2963286299...<61`.

So the construction is a rigorous obstruction only to the stronger structural shortcut; it simultaneously exhibits the mechanism that a future closure must capture: a moderate-rank diffuse residual can itself be a valid Fresnel smoother when kept jointly with the latent carrier.

## 5. Best current conditional assembly and first unpaid implication

After incorporating the newest fleet03/B20 r50 theorem and the sharpening above, the strongest current branch of the closure graph is:

1. previously completed diagonal, physical-pair, pair-log, physical-E3, D5, ridge/window, grouped-star, hub+square, null-coloop and fractional receivers pay their exact branches;
2. r47-r52 reduce a major robust physical-rank-two chamber to a BL-compatible four-latent skeleton plus physically row-small residual self blocks and a genuine cross tail `<2^-16`;
3. the exact nonsingular four-latent skeleton is paid by the completed Fresnel/BL endpoint, while determinant collapse is quantitatively rank-three in latent coefficient space;
4. partner r50 paid residual fifth singular value `>=9/4`; Theorem 2.1 strengthens that payment to `>=43/20`;
5. every still-unpaid instance in this branch therefore has the exact rank-12/rank-11 carrier representation with retained tail ceilings `2.1500152587890625` / `2.1501220703125`, together with the pinned D5 failures on the concrete residual-bank splits.

The first unpaid universal implication is now

`QFORM-R50-MODERATE-RESIDUAL-R12/R11-RETAINED-TAIL-ENDPOINT-v2`:

> under the full independent cap-one product hypotheses and the r52 common-plane/BL-compatible normal form, assume both row-small residuals have `s_5<43/20`, the two concrete residual-bank D5 currencies are `<1/1024`, and retain the genuine cross tail `<2^-16`; pay the resulting rank-at-most-12 (rank-at-most-11 on determinant collapse) carrier plus retained operator tail, or source-preservingly route a moderate rank-three/rank-four residual into an existing physical-pair, E3, grouped-star, hub+square, ridge/window, incident-volume or joint Fresnel receiver.

Proposition 4.1 rules out resolving this by forcing a fifth residual mode or by forcing the third target eigenvalue into the latent four-carrier. The next mechanism has to spend a rank-three/rank-four diffuse residual jointly with the latent crossing before taking absolute values, or find a product-preserving physical cut that converts that joint geometry into a completed receiver.

## 6. Correction boundaries

The proof never uses post-rotation independence. Coefficient SVD/spectral decompositions are used only to choose literal physical partitions and estimate singular values. Pointwise law-uniform oscillatory decay, arbitrary-joint rank-three coarea, worst-fibre/conditional-cap transfer, and generic interpolation from fractional small-ball bounds to `L^infinity` are not used. Small operator norm is never interpreted as a small random quadratic perturbation.

Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

Unrestricted continuity: **OPEN**.

Theorem 2.1 branch: continuous `C_0` density, `||p_Q||infinity<15952`.

Stress family in Proposition 4.1: continuous density with the pinned Theorem-H bound `<61`; not a QFORM counterexample.
