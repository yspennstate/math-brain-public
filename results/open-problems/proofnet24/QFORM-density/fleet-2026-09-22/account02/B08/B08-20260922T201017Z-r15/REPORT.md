SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-22T20:10:17Z.
attacking: consume the designated partner's two-sided near-coloop determinant bank before reciprocal inversion, and apply the partner theorem to an explicit delocalized full-rank target family.

# account02/B08 — regularized bicolloop Schur-star reduction

**Run:** `B08-20260922T201017Z-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control used:** revision `2026-09-22.15`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING STRUCTURAL THEOREM / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, corrections, and first unpaid implication

The target is the unrestricted product-source statement: for independent real coordinates with probability densities bounded by one and any real symmetric matrix with at least three eigenvalues of modulus at least one, prove a dimension-free essential-supremum bound for the density of `X^T A X`, or construct a target-valid counterexample. No moment, support, continuity, identical-law, log-concavity, or post-rotation independence hypothesis is added.

This run consumes the current corrections. In particular it does **not** use law-uniform pointwise Fresnel decay, unrestricted fiber suprema, the false arbitrary-joint rank-three coarea inequality, positive conditional projection-density moments, or a selected reciprocal minor. It also uses the newer correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`: an exact-zero affine half-Riesz endpoint cannot be extended to merely small Schur diagonal using only a cross-row norm.

The designated partner source actually used is account03/B08, run `20260922T194215Z-account03-B08-qform-diffuse-r19`, canonical report

`yspennstate/math-open-problems@86cbf124545c3457b0037b49151f4f641391fc76`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T194215Z-account03-B08-qform-diffuse-r19/REPORT.md`.

Its theorem `QFORM-SYMMETRIC-RIDGE-OR-BICOLOOP-v1` closes two nonzero-pivot branches by explicit density estimates and leaves only a two-sided near-coloop branch. In that branch, at scale `g=gamma/16`, the actual physical cross block `H` gives

`Z = H(g^2 I+H^T H)^(-1/2) = (g^2 I+H H^T)^(-1/2)H`,

`K_L=ZZ^T`, `K_R=Z^T Z`, and

`256/129 <= theta:=||Z||_F^2 < 201/100`.

There are a physical row `j` and physical column `r` with

`ell=(K_L)_{jj}>99/100`, `m=(K_R)_{rr}>99/100`,

and the partner proves the aggregate-before-inversion certificate

`sum_{k!=j,s!=r} det Z[{j,k},{r,s}]^2 > 2349/5000`.            (1.1)

The first unpaid implication is to consume this determinant bank without choosing one potentially tiny minor. This report derives the exact first algebraic reduction of that bank.

## 2. Exact intersection-minor identity

Permute only the original physical row and column labels so that the heavy row and column are first. Write

`Z = [ z   a^T ]`
`    [ b    C  ]`,                                             (2.1)

where `z=Z_{jr}`, `a` is the remainder of heavy row `j`, `b` is the remainder of heavy column `r`, and `C` is the complementary physical block.

For each remaining row `k` and column `s`, the `2x2` minor incident to both heavy indices is

`det Z[{j,k},{r,s}] = z C_{ks} - b_k a_s`.                    (2.2)

Consequently the **entire** partner bank is one Frobenius norm:

`boxed( B_{jr} := sum_{k!=j,s!=r} det Z[{j,k},{r,s}]^2`
`      = ||zC-ba^T||_F^2. )`                                  (2.3)

This identity is exact, dimension-free, and takes the aggregate before any inversion.

The two ridge leverages and total effective dimension simultaneously give

`||a||_2^2 = ell-|z|^2`,
`||b||_2^2 = m-|z|^2`,                                        (2.4)

and

`||C||_F^2 = theta-ell-m+|z|^2`.                              (2.5)

In particular, in the unpaid partner branch,

`||a||^2 > 99/100-|z|^2`,
`||b||^2 > 99/100-|z|^2`,
`||C||_F^2 < 3/100+|z|^2`.                                   (2.6)

Equations (2.3)-(2.6) are the key new reduction.

## 3. Quantitative Schur-or-star dichotomy

### Theorem — `QFORM-REGULARIZED-BICOLOOP-SCHUR-STAR-v1`

Under the unpaid branch hypotheses above, exactly one of the following two alternatives holds.

**A. Regularized Schur branch.** If `|z|>=1/10`, then `z` is nonzero and the normalized Schur residual

`S_Z := C - b a^T/z`                                           (3.1)

satisfies

`boxed( |z| ||S_Z||_F = ||zC-ba^T||_F > sqrt(2349/5000), )`    (3.2)

hence, because `|z|<=1`,

`||S_Z||_F > sqrt(2349/5000) = 0.6854195795...`.               (3.3)

Thus a non-negligible regularized heavy intersection entry forces a dimension-free **aggregate Schur remainder**. No single physical minor has been selected.

**B. Hyperbolic-star branch.** If `|z|<1/10`, then

`||a||^2 > 49/50`, `||b||^2 > 49/50`, `||C||_F^2 < 1/25`.      (3.4)

Let

`T = [ 0  a^T ]`
`    [ b   0  ]`.                                              (3.5)

Then

`||Z-T||_F^2 = |z|^2+||C||_F^2 < 1/20`.                       (3.6)

The two nonzero singular values of `T` are exactly `||a||` and `||b||`, so Weyl's inequality yields

`sigma_2(Z) > sqrt(49/50)-1/sqrt(20)`
`           = 0.7663426959...`.                               (3.7)

Moreover the determinant bank is in fact much larger than the partner's generic lower bound. Indeed

`||ba^T||_F=||a||||b||>49/50`,
`|z| ||C||_F < (1/10)(1/5)=1/50`,

so by the reverse triangle inequality in (2.3),

`boxed( ||zC-ba^T||_F > 24/25,`
`       B_{jr} > 576/625 = 0.9216. )`                          (3.8)

Hence the near-zero normalized heavy intersection does not make the bank disappear: it forces a product-shaped two-arm star carrying more than `0.9216` units of squared determinant mass, while the complementary core has Frobenius norm below `1/5`.

### Proof

Identity (2.3) gives (3.2) immediately when `z!=0`, using the partner's bound (1.1). A ridge kernel is a positive contraction, hence every entry of `Z` has modulus at most one, which gives (3.3).

For `|z|<1/10`, substitute `|z|^2<1/100` into (2.6): both arm energies exceed `99/100-1/100=49/50`, while the core energy is below `3/100+1/100=1/25`. This proves (3.4) and (3.6). Matrix `T T^T` is block diagonal with scalar block `||a||^2` and rank-one block `bb^T`; therefore its two nonzero singular values are `||a||,||b||`. The operator perturbation is at most the Frobenius perturbation, giving (3.7). Finally, (3.8) follows from

`||zC-ba^T||_F >= ||ba^T||_F-|z|||C||_F >49/50-1/50=24/25`.

QED.

## 4. Why this is useful, and what it does not prove

The partner's near-coloop certificate was a large sum of normalized physical-coordinate minors. Theorem 3 converts it into two canonical aggregate objects:

1. a regularized Schur remainder whose Frobenius mass remains bounded below after the heavy intersection is pivoted; or
2. an almost pure original-index two-arm star, with each arm carrying squared norm `>49/50` and the non-star core carrying `<1/25`.

This is stronger than saying merely that some minor is nonzero, and it is compatible with the programme's aggregate-before-inversion requirement. It is also deliberately stated at the level of `Z`, not silently transferred to `H`: the regularizers in `Z=H(g^2I+H^TH)^(-1/2)` mix physical columns, so a product-law argument must still return to original coordinates before applying one-dimensional density caps.

The hyperbolic-star alternative must likewise not be paid by the now-refuted statement “a near-zero scalar plus one cross row is enough.” The live correction gives a rank-one counterexample to that interface. Any next step must use the **whole two-arm bank** together with a genuinely independent third smoothing source or an already proved grouped/ridge mechanism.

Thus the exact next implication is

`QFORM-DIFFUSE-BICOLOOP-GROUPED-PAYMENT-v1`:

> Transfer either (3.2) or (3.8), without selecting a reciprocal minor and without rotating the product law, into a bounded-density estimate for the original physical quadratic form. In the star branch the payment must retain both arms (or a third independent smoother), not only a near-zero pivot plus one arm.

## 5. Designated-partner result applied to an actual delocalized target family

The structural theorem above is not itself a density estimate. To apply the designated partner's completed result to an actual target inequality, consider the following full-rank family.

Let `m=2^q>=4` and let `U_m` be the normalized Sylvester-Hadamard matrix, so every entry of every column `u_nu` has modulus `m^{-1/2}`. Choose distinct numbers

`s_nu = 1 + nu/(2m)`, `nu=0,...,m-1`,                              (5.1)

and set

`H_m = U_m diag(s_0,...,s_{m-1}) U_m^T`,                       (5.2)

`A_m = diag(1, [0 H_m; H_m 0])`.                              (5.3)

The spectrum is

`spec(A_m)={1} union {+s_nu,-s_nu:0<=nu<m}`,                   (5.4)

so every eigenvalue has modulus at least one. The eigenvectors

`w_nu^+ = (0,u_nu,u_nu)/sqrt(2)`                               (5.5)

have eigenvalues `+s_nu`. Select any three distinct such vectors. Their physical-coordinate frame leverage is exactly

`max_i sum_{nu in selected}|w_nu^+(i)|^2 = 3/(2m) ->0`.        (5.6)

Thus the three selected large eigendirections are genuinely delocalized in the original independent coordinates, while the matrix is full-rank and has arbitrary dimension.

Apply account03/B08 r19 with the uncoupled original-coordinate pivot `a=1`, residual cross block `H=H_m`, and `gamma=1`. Since every singular value of `H_m` is `s_nu>=1`, the inherited transverse reserve is automatic (`x_nu=min(1,s_nu^2)=1`, hence `e_2(x)>=6` for `m>=4`). At the partner's scale `g=1/16`,

`theta = sum_nu s_nu^2/(1/256+s_nu^2)`
`      >= m*(256/257)`
`      >= 1024/257`
`      = 3.984435797... > 201/100`.                            (5.7)

Therefore the **first branch** of the designated partner theorem applies, for every choice of independent input laws with densities bounded by one:

`boxed( ||p_{X^T A_m X}||_infinity <1543. )`                  (5.8)

No moment, centering, support, continuity, or independence-after-rotation assumption occurs. The constant is independent of `m`, while the selected-three-frame leverage tends to zero. This is a concrete source-valid delocalized estimate, not a numerical experiment.

This family is intentionally complementary to localized principal-coordinate conditioning: its selected spectral directions become arbitrarily diffuse, but a global original-coordinate cross block retains enough effective ridge dimension for the partner mechanism to pay uniformly.

## 6. Conditional end-to-end position

A compact conditional proof architecture now reads as follows. Completed localized-pair/scalar/ridge results pay matrices whenever a uniformly strong original-coordinate smoother is exposed. In the inherited nonzero-pivot O0 reduction, account03/B08 r19 pays every branch except the two-sided near-coloop case. Theorem 3 above canonically reduces that case to either a regularized Schur bank or an almost-pure two-arm star. If `QFORM-DIFFUSE-BICOLOOP-GROUPED-PAYMENT-v1` is proved in original coordinates, the nonzero-pivot O0 debt is closed. A distinct zero-pivot branch remains and must respect the live near-zero half-Riesz correction. Separately, the fleet still must justify that the global full-target reduction reaches one of these paid branches for every symmetric `A` with `s_3(A)>=1`.

Therefore this run is **not** a full proof candidate. It supplies one exact new algebraic reduction and one actual dimension-free density estimate on a delocalized full-rank family.

## 7. Exact finite check

The sibling `verify.py` checks all rational thresholds and displayed numerical constants only. Its passing output is stored in `CHECK.txt`. The checker is not an independent proof review.