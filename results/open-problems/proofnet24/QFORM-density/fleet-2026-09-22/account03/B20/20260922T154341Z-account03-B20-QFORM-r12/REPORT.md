# QFORM proof closure: conditioning plus one-scale ridge removes the nonlocalized high-window branch

**Run:** `20260922T154341Z-account03-B20-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Classification:** `TARGET_LEVEL_BRANCH_PROVED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and scope

Let `X_1,...,X_n` be independent real random variables with Lebesgue densities `0<=f_i<=1`, and let `A` be real symmetric with at least three eigenvalues of absolute value at least one. The full conjecture asks for one universal finite `C` such that `X^T A X` has density bounded by `C`; continuity is a separate desired conclusion.

This report proves a new **continuous-density branch** of that exact target. It adds no moment, support, sign, log-concavity, or rotated-independence assumption.

The two source inputs are:

1. `QFORM-RIDGE-DENSITY-v1` / `QFORM-SPECTRAL-WINDOW-DENSITY-v1`, interactive report `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, which proves the free-regularizer graph estimate, its ridge criterion, the perturbation lemma, and the MSS spectral-window construction.
2. Assigned partner `account04/B20`, `QFORM conditioned-whitened diffuse extraction`, `yspennstate/math-open-problems@94bf446b8547b1124a37033e940ef594c460b64f`. Its exact conditioning identity and residual-frame whitening are applied below to an actual inequality. Its final theorem uses the entire range; here the same proved whitening step is spliced to the one-scale ridge argument so arbitrary small nonseparable spectrum is retained.

## 2. New theorem: conditioned spectral-window closure

Let

`P = 1_{|A| >= 1/64} = U U^T`,

where the columns of `U` form an orthonormal basis of the spectral subspace, and write

`A = U Lambda U^T + E`,  with  `||E||op < 1/64`.

Because `A` has at least three eigenvalues of modulus at least one, `s_3(Lambda)>=1`.

Choose any set `H` of **original coordinates**, let `R=H^c`, write `u_i^T` for row `i` of `U`, and set

`S = U_R^T U_R = I - U_H^T U_H`,  `delta = lambda_min(S)`.

Assume

`delta >= 1/2`                                                   (2.1)

and the exact whitened residual leverage bound

`max_{i in R} u_i^T S^{-1} u_i <= 1/32`.                         (2.2)

Then for every cap-one product input law, `Q=X^T A X` has a **continuous `C_0` density** and

`||p_Q||_infinity <= 96 sqrt(3e/2) < 194`.                       (2.3)

The statement remains true after conditioning on arbitrary values of `X_H`; hence averaging gives the unconditional bound.

### Proof

Condition on `X_H`. Independence and the original density caps remain on the coordinates in `R`; the conditioned terms involving `H` contribute only coordinate-separable linear terms plus a constant.

By the partner's exact whitening identity, with

`V = U_R S^{-1/2}`,

we have `V^T V=I` and

`U_R Lambda U_R^T = V B V^T`,  where  `B=S^{1/2} Lambda S^{1/2}`.

Moreover the row leverage of `V` is exactly

`||e_i^T V||_2^2 = u_i^T S^{-1}u_i <=1/32`.                     (2.4)

The product singular-value inequality gives

`s_3(B) >= delta s_3(Lambda) >= delta`.                          (2.5)

Apply the two-part MSS partition to the Parseval frame `V`, exactly as in the source spectral-window proof. There is a partition `R=I union J` with

`M_I=V_I^T V_I >= (7/32)I`,  `M_J=V_J^T V_J >= (7/32)I`.

For the high-window cross block

`B_0=(V B V^T)[I,J]`,

its nonzero singular values are those of `M_I^{1/2} B M_J^{1/2}`, so from (2.5)

`s_3(B_0) >= (7/32) delta`.                                     (2.6)

The full conditional cross block is

`C=A_RR[I,J]=B_0+E_RR[I,J]`.

Since `||E_RR[I,J]||op<=1/64`, min-max gives

`s_3(C) >= sigma := (7 delta)/32 - 1/64 = (14 delta-1)/64`.

Under `delta>=1/2`,

`sigma >= 3/32`.                                                (2.7)

Because both `M_I,M_J` are positive definite and `B` is invertible, `range(B_0)=range(V_I)`. Hence its projection leverage is at most

`(1/32)/(7/32)=1/7`.                                            (2.8)

Use the source ridge-perturbation lemma on `C=B_0+F`, `||F||<=eta=1/64`. Set

`gamma = sigma/sqrt(3)`.

Then every diagonal ridge leverage satisfies

`(K_gamma)_{ii} <= [1/sqrt(7) + eta/gamma]^2`

`<= [1/sqrt(7) + sqrt(3)/6]^2 < 4/9 < 1/2`.                    (2.9)

For completeness, the strict inequality in (2.9) is exact: `1/sqrt(7)+sqrt(3)/6<2/3`; after isolating and squaring, it is equivalent to `9409>9408`.

The ridge effective dimension obeys

`theta_gamma >= 3 sigma^2/(sigma^2+gamma^2) = 9/4 > 2`.         (2.10)

Thus the ridge density criterion applies with `q=1`. Its second bound gives

`||p_{Q | X_H}||_infinity`
` <= [sqrt(e)/(sqrt(2) gamma)] * theta/(theta-2)`
` <= 9 sqrt(3e/2)/sigma`
` <= 96 sqrt(3e/2) <194`.                                     (2.11)

The criterion gives a continuous `C_0` conditional density uniformly in the conditioning value. Averaging these densities preserves the bound; dominated convergence preserves continuity. This proves (2.3). QED.

## 3. New exhaustive localization corollary

Use the same high-window frame `U` and define the source-measurable heavy-coordinate set

`H_* = { i : P_ii = ||u_i||_2^2 > 1/64 }`.                     (3.1)

If

`||U_{H_*}^T U_{H_*}||op <= 1/2`,                              (3.2)

then `S=I-U_{H_*}^T U_{H_*} >=(1/2)I`, and for every `i` outside `H_*`,

`u_i^T S^{-1}u_i <= 2||u_i||^2 <=1/32`.                        (3.3)

Therefore Theorem 2 applies and gives a continuous density with norm `<194`.

Consequently **every unresolved full-target counterexample must satisfy**

`boxed: ||U_{H_*}^T U_{H_*}||op > 1/2`.                        (3.4)

Equivalently, there is a unit vector `z` in the `|lambda(A)|>=1/64` spectral coefficient space such that

`sum_{i in H_*} |u_i dot z|^2 >1/2`.                            (3.5)

So more than half of some high-window spectral direction is forced onto physical coordinates that each have high-window leverage `>1/64`.

This is a genuine target-level reduction: the fresh ridge theorem already closes the fully diffuse window `max_i P_ii<=1/32`; the present result closes a much larger localized-but-not-too-localized region. Any survivor is now quantitatively **spectrally localized on its heavy physical coordinates**.

## 4. Integration with the current proof tree

The preceding account03/B19 reduction leaves only low-offdiagonal-stable-rank / mixed-aggregate residuals after its near-diagonal branches. The preceding account03/B20 result supplies pivot-Schur two-direction closure and identifies cross-dominated/localized Schur states as the remaining mechanisms.

The present theorem adds an independent global localization certificate before choosing a scalar pivot: a survivor must satisfy (3.4). This is exactly the kind of physical localization needed by the aggregate/hyperbolic-square route, and it is obtained without rotating the product law.

The assigned partner `account04/B20` is used at the precise inequality (3.3): its proved conditioning/whitening identity converts the raw post-conditioning frame into the exact residual leverage `u_i^T S^{-1}u_i`. The new ridge splice then handles the arbitrary low spectral tail that the partner's entire-range theorem did not cover.

## 5. First unpaid implication

`QFORM-HEAVY-WINDOW-AGGREGATE-SPLICE-v1`:

Given (3.4), combine the heavy-window localization with the existing low-stable-rank/offdiagonal residual and the product-preserving hyperbolic-square machinery. Either

1. extract disjoint original-coordinate banks carrying a universal fraction of the localized high-window direction and a second independent large direction, with enough square/cross strength to invoke the completed aggregate theorem; or
2. show that the localization forces a definite physical two-plane / conditioned-whitened branch already controlled by existing results.

A failure must be exhibited as an actual symmetric matrix satisfying the three-large-eigenvalue hypothesis, not as an arbitrary projection/frame counterexample.

## 6. Status

- New theorem (2.3): **PROVED in stated scope**.
- Localization corollary (3.4): **PROVED**.
- Density continuity: **PROVED in this branch**.
- Full arbitrary-dimension QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- No claim of native brain ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
