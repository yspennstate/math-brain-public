# MOC4 account02/B07 — pair-curvature sandwich, conjugacy-class balance, and exact repeated-spectrum closure

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T053424Z-b07-45eeecdd`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## Sources actually consumed

- Fresh protected controls were read at `main` commit `fffe684ee8c52f2fbfe8ce45316d50d8fcb7a533`, OWNER CONTROL revision `2026-09-22.2`; a later compare through `db7810ef4f6510888517f25c36ed4872fa0bbaf7` showed no protected-control change.
- Campaign lead account03/B07 latest complete version found by UTC ordering: run `20260922T043708Z-account03-B07-MOC4-r11`, theorem `MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`, report blob `c286ea3e5ec5a72902fbff82e94db343f2bbc543`, shared handoff commit `68e6da319010c9611a6e7d647010689d72072670`.
- Named partner account03/B08: run `20260922T051819Z-account03-B08-MOC4-r11`, theorem `MOC4-PAIR-BLOCH-ENVELOPE-v1`, report blob `f39236fa1e63c1af4ebeb89a1f243a49a9aa44a6`, shared handoff commit `86ade870bb739fe4d52b3a54fe90e2c87522a807`.
- Essential inherited dependency explicitly used below: account04/B08 `MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`, report blob `ccc5358d81a9432f3764a9a89be9a01c6bb54e26`, handoff commit `db7322e4995935e482d4a8204c0ff07b42d8e5d7`.
- Additional current stationarity context read: account04/B09 `MOC4-CONTINUOUS-BIORIENTATION-STATIONARITY-v1`, handoff commit `f23b10b2d973e3290ebdf2d557699a06a8275922`.

No benchmark artifact or held-out answer was read or used.

## 1. Conditional end-to-end route

For a support direction `eta`, normalize `|eta|=1` and write

`h(U)=Re(eta det(A+U B U*))`, `M=max_sigma Re(eta prod_i(a_i+b_sigma(i)))`.

If MOC4 fails, compactness gives a true-unitary global maximizer `U_*` with `h(U_*)=M+gamma`, `gamma>0`. The lead subgroup cubature and current V4/pair ceilings already reduce the possible positive residual. The named partner gives an exact singular-safe Bloch-sphere formula on every embedded row-pair `SU(2)` orbit, hence exact pair stationarity at `U_*`. The first task here is to quantify those pair curvatures and remove repeated spectra without a limiting argument. After that, the only remaining target-level branch is a genuinely simple-spectrum, strict-pair-curvature stationary maximizer satisfying the lead subgroup ceilings and the current same-unitary `P-R-D`/Spin(6) stationarity constraints.

## 2. New theorem: `MOC4-PAIR-CURVATURE-SANDWICH-v1`

Let

`R=max_i |a_i| + max_j |b_j|`.

For a row transposition `tau=(r s)`, set `D=det(A+UBU*)` and `D_tau=det(A+P_tau U B U* P_tau*)`. Then

`|D-D_tau| <= 2 R^3 |a_r-a_s|`.                                      (2.1)

For a column transposition `tau=(p q)`, with `D_tau=det(A+U P_tau B P_tau* U*)`,

`|D-D_tau| <= 2 R^3 |b_p-b_q|`.                                      (2.2)

### Proof, including singular points

For the row case put `delta=a_r-a_s`, replace the two entries by their midpoint to obtain `A_0`, put `X_0=A_0+UBU*`, and set `H=E_rr-E_ss`. Then

`D=det(X_0+(delta/2)H)`, `D_tau=det(X_0-(delta/2)H)`.

Because `rank(H)=2`, `p(t)=det(X_0+tH)` has degree at most two. Hence its odd part is exactly linear and

`D-D_tau = delta tr(adj(X_0) H)`.                                    (2.3)

This is a polynomial identity; no inverse and no nonsingularity hypothesis is used. Since `||H||_*=2`, `||X_0||<=R`, and `||adj(X_0)||<=||X_0||^3<=R^3` (first for invertible matrices from singular values, then by continuity), (2.1) follows. For the column case replace the selected two `b` entries by their midpoint and use `H=U(E_pp-E_qq)U*`, which again has trace norm two; the same proof gives (2.2).

Now use account04/B08's exact pair-symmetrized common lift. For every row or column transposition,

`(h(U)+h(U_tau))/2 <= M`.                                             (2.4)

Thus at a hypothetical support-violating global maximizer `h(U)=M+gamma`,

`2 gamma <= h(U)-h(U_tau) <= 2 R^3 |spectral gap_tau|`.               (2.5)

Apply account03/B08's exact pair-Bloch envelope. Along either of the two orthogonal genuine `SU(2)` great-circle directions associated with the same pair, stationarity gives

`h''(0) = -2 (h(U)-h(U_tau))`.                                        (2.6)

Therefore every row pair and every column pair obeys the exact curvature sandwich

`4 gamma <= -h''(0) <= 4 R^3 |spectral gap_tau|`.                     (2.7)

### Consequences

1. **Repeated spectra are closed exactly.** If any `a_r=a_s`, then `P_tau` commutes with `A`, hence `D_tau=D`; by (2.4), `h(U)<=M` for every support direction. Equivalently, the common lift of the pair average is already a common lift of `D(U)` itself. The same argument applies if any two `b` eigenvalues coincide. Thus every MOC4 case with a repeated eigenvalue in either spectrum is proved directly, including singular determinant values. No perturbative repeated-spectrum branch remains.
2. **Quantitative simple-spectrum reduction.** Any positive-gap violator satisfies, for every pair,

   `|a_r-a_s| >= gamma/R^3`, `|b_p-b_q| >= gamma/R^3`.                 (2.8)

   In scale-free form, if `hat_gamma=gamma/R^4`, both normalized spectra are `hat_gamma`-separated. A sequence with a uniformly positive normalized violation cannot approach a repeated spectrum.
3. **Uniform strict pair curvature.** A positive-gap global maximizer is strongly concave in every one of the twelve row-pair tangent directions and every one of the twelve column-pair tangent directions, with curvature at most `-4 gamma` in the normalization of (2.6).

## 3. New theorem: `MOC4-CONJUGACY-CASIMIR-BALANCE-v1`

For every true `U`, every complex spectra, and every conjugacy class `C` of `S_4`,

`sum_{g in C} det(A+P_g U B U* P_g*)
 = sum_{g in C} det(A+U P_g B P_g* U*)`.                              (3.1)

Hence the same equality holds after any real support functional.

### Proof

Use the exact Cauchy-Binet/principal-minor expansion

`det(A+UBU*) = sum_{k=0}^4 sum_{|I|=|J|=k} a_{I^c} b_J W_k(I,J)`,

`W_k(I,J)=|det U[I,J]|^2`.                                             (3.2)

For `k=1` (and, by complementary minors, `k=3`), `W_k` is doubly stochastic. Every conjugacy-class sum on the natural four-point permutation module is `alpha I+beta J`, so it commutes with `W_k`.

For `k=2`, `W_2` is doubly stochastic and Jacobi complementarity gives

`W_2(I,J)=W_2(I^c,J^c)`;

therefore `W_2` commutes with the complement involution `C`. Exact enumeration gives every `S_4` class-sum operator on the six two-subsets in `span{I,J,C}`. Hence it too commutes with `W_2`. The `k=0,4` pieces are scalar. Moving the class-sum operator through `W_k` in (3.2) proves (3.1). This uses actual unitary minors and preserves all complex phases in the determinant coefficients.

For the transposition class `T`, define

`G_out=sum_{tau in T}(h(U)-h(P_tau U))`,
`G_in =sum_{tau in T}(h(U)-h(U P_tau))`.

Then (3.1) gives the exact same-unitary identity

`G_out=G_in=:G`.                                                       (3.3)

Combining the partner Bloch formula with the two explicit great-circle directions for each pair gives

`sum_(6 row pairs,2 axes) h''(0) = -4 G
 = sum_(6 column pairs,2 axes) h''(0)`.                               (3.4)

Thus the row and column pair-Hessian trace budgets are not independent residual variables. At a positive-gap global maximizer, (2.5) yields

`G >= 12 gamma`, and so each side of (3.4) is at most `-48 gamma`.      (3.5)

The same low-frequency representation also gives the exact central cubature identity

`h(U)=3 A_trans h - 2 A_3cycle h`,                                    (3.6)

where the averages are over the six transpositions and eight 3-cycles on either physical side. Equivalently `G=4(h(U)-A_3cycle h)`. This is an exact bridge from the continuous Hessian trace to the discrete `S_4` orbit used by the lead cubature.

## 4. Exact application to the named partner datum

The standard-library verifier reconstructs account03/B08's exact rational Cayley unitary for

`a=(18-17i,-20+2i,15-22i,-21+2i)`,
`b=(-19+4i,25-5i,18-i,-18+i)`,
`L(z)=-5782 Re z+19099 Im z`.

It exactly reproduces the partner's support gap to the uniquely exposed vertex,

`M-L(D)=2774999449515476249040000/431850208768934029`,

then verifies all five conjugacy-class row/column balances. For this datum

`G=1575414455627672838774521982/431850208768934029`,

and the common pair-Hessian trace is

`-4G=-6301657822510691355098087928/431850208768934029`.

It also verifies (3.6) exactly. This datum is inside the target hull and is not claimed stationary; it is used only as a dense, true-unitary, complex-spectrum regression for the identities.

## 5. Sharpened remaining implication

The parent MOC4 problem remains open. After this run there is no separate repeated-spectrum obligation: it is already closed by the pair common lift. Singular determinant points remain inside the exact algebra because (2.3), the pair-Bloch theorem, class balance, and the determinant expansion use no inverse.

The first remaining target-level implication can therefore be stated more narrowly:

**`MOC4-SIMPLE-STRICT-STATIONARY-RIGIDITY-v1` (OPEN).** Normalize `|eta|=1` and `R=1`. Exclude a genuine global support maximizer with `gamma>0` when both spectra are simple and every spectral pair is at least `gamma` apart, all row/column pair curvatures satisfy (2.7), the two pair-Hessian trace budgets agree by (3.4), and the same unitary satisfies the lead subgroup-cubature/V4 ceilings plus the current `P-R-D` and Spin(6) stationarity equations.

A proof of this implication closes the remaining support directions; repeated spectra need no limiting argument. A target-level disproof still must exhibit actual complex spectra and a true unitary in one common support direction.

## Status

`ESSENTIAL_STEP_APPLIED`. Full MOC4 is still **OPEN**. No arbitrary bistochastic surrogate, no common-lift assumption for an individual generic unitary, and no inverse-based singular argument was used.
