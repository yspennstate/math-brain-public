# fleet03/B12 — spectral-window enlargement and an exhaustive high-leverage physical-row reduction

**Run:** `20260922T154709Z-qform-window-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Additional eigenvalue control  
**Classification:** `ESSENTIAL_STEP_APPLIED / PARAMETRIC_STABILITY_THEOREM / TARGET-LEVEL_DICHOTOMY / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write is not authenticated native learned-memory receiver use.

## 1. Exact target, source state, and mechanism change

The sole target is the full arbitrary-dimensional statement: for independent real coordinates `X_i` with probability densities bounded by one and an arbitrary real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has an essentially bounded density with one dimension-independent finite constant, or give a valid target counterexample. Continuity is a separately requested strengthening.

Fresh control at the start of this run was `yspennstate/math-research-brain@a024fc6d01d9af0a0503bd76732e41014c3166a4`, revision `2026-09-22.5`. The live corrections used here include: no law-uniform pointwise Fresnel decay for arbitrary cap-one densities; no independence after spectral rotation; no unrestricted fiber-supremum argument; no universal single-Schur-pivot/rank-two extraction; no universal local cross-rank-three dichotomy; and no reduction to one physical triple with uniformly bounded reciprocal aggregate cost.

The preceding B12 runs concentrated on local principal blocks, one exceptional eigenvalue, cross-rank cancellation and spike/tail stability. This run changes mechanism. It starts from the newly supplied one-scale ridge-leverage theorem and asks an exhaustive question at a spectral threshold: **how far can arbitrary additional eigenvalues of either sign be absorbed before one is forced to expose a quantitatively heavy original coordinate?**

The result has two parts.

1. A parameterized spectral-window theorem improves the published supporting cutoff `1/64` to the clean cutoff `1/39` at the same leverage threshold `1/32`, while preserving arbitrary signs, arbitrary numbers of extra eigenvalues and nonseparable small tails.
2. Failure of that diffuse-window condition forces a dimension-free **original-coordinate** certificate: one physical column of `A` has either a scalar pivot or an off-diagonal cross bank of norm strictly larger than `1/312`.

Thus the unrestricted target is reduced to a ridge-certified diffuse branch plus a quantitative heavy physical-row branch, without rotating the independent variables.

## 2. Completed source theorem consumed

The main completed supporting input is the interactive theorem `QFORM-RIDGE-DENSITY-v1`, source

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,

path

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an original-coordinate cross block `B=A[I,J]`, `gamma>0`, define

`K_gamma = B B^T (gamma^2 I + B B^T)^(-1)`,

`theta_gamma = tr K_gamma`,

`D_gamma = det(I+B B^T/gamma^2)`.

If, for some `1<=q<=2`,

`max_i (K_gamma)_ii <= q/2`,  and  `theta_gamma>2q`,

then the full quadratic form, with arbitrary self blocks and outside couplings, has a continuous `C_0` density and

`||p_Q||_infinity
 <= e/(sqrt(2q) gamma) * theta_gamma/(theta_gamma-2q)
    * D_gamma^(-1/(2 theta_gamma))
 <= sqrt(e)/(sqrt(2q) gamma) * theta_gamma/(theta_gamma-2q).`        (2.1)

In particular, if `s_3(B)>=sigma`, take `gamma=sigma/sqrt(6)`. Then `theta_gamma>=18/7`; if `max diag K_gamma<=1/2`, the `q=1` case gives

`||p_Q||_infinity <= 9 sqrt(3e)/(2 sigma).`                           (2.2)

The same source proves the perturbation estimate: if `B=B_0+F`, `||F||_op<=eta`, and `S=range(B_0)` has projection diagonal at most `ell`, then

`max_i (K_gamma)_ii <= (sqrt(ell)+eta/gamma)^2.`                      (2.3)

These statements retain arbitrary self blocks and outside couplings and are proved in original coordinates. The supplied source is a complete supporting analytic argument but its newest extension was still awaiting the specified independent end-to-end reviews at the source snapshot; the present theorem should inherit that review status rather than being promoted as independently reviewed.

The exact assigned partner `fleet04/B12` had no completed **current-QFORM-compatible** result at the source-bound refresh. Its visible completed B12 result is an older FEI codimension-staircase theorem and is incompatible with the present owner target, so it is not revived or falsely cited as QFORM input. A compatible completed fleet04 theorem actually applied in Section 6 is fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, source commit `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`.

## 3. Parameterized spectral-window theorem

Let `0<tau<1` and `eps>0`. Define

`delta(eps)=1/2-eps-sqrt(2 eps).`                                      (3.1)

Assume `delta>tau` and put

`sigma=delta-tau.`                                                     (3.2)

Let `P_tau` denote the spectral projection of `A` onto the direct sum of all eigenspaces with

`|lambda|>=tau.`

### Theorem 3.1 — `QFORM-PARAMETRIC-SPECTRAL-WINDOW-v1`

Assume:

1. `A` has at least three eigenvalues of modulus at least one;
2. `max_i (P_tau)_ii <= eps`;
3. `delta(eps)>tau`; and
4.

`sqrt(eps/delta) + sqrt(6) tau/(delta-tau) <= 1/sqrt(2).`              (3.3)

Then, for every independent cap-one input law, `Q=X^TAX` has a bounded continuous `C_0` density and

`boxed( ||p_Q||_infinity <= 9 sqrt(3e) / [2(delta-tau)]. )`            (3.4)

The theorem allows arbitrarily many additional eigenvalues, of either sign and arbitrary magnitude. Every eigenvalue with modulus at least `tau` is retained in the high part; every remaining eigenvalue may be nonzero and arbitrarily oriented.

### Proof

Write the spectral truncation

`A=A_H+E`,

where `A_H=U Lambda_H U^T` contains **all** eigenvalues with modulus at least `tau`. Thus `U` has orthonormal columns,

`max_i ||u_i||_2^2 = max_i(P_tau)_ii <= eps`,                          (3.5)

`Lambda_H` is invertible on its spectral subspace, has at least three singular values at least one, and

`||E||_op <= tau.`                                                     (3.6)

Apply the two-part Marcus-Spielman-Srivastava frame partition to the rows of `U`. There is a partition of the original coordinates into `I,J` for which each partial Gram matrix satisfies

`M_I=U_I^T U_I <= (1/sqrt(2)+sqrt(eps))^2 I`,

and the same for `M_J`. Since `M_I+M_J=I`, both also satisfy

`M_I,M_J >= delta I`,

because

`delta = 1-(1/sqrt(2)+sqrt(eps))^2
       = 1/2-eps-sqrt(2eps).`                                         (3.7)

Consider the high-window cross block

`B_0=(A_H)[I,J]=U_I Lambda_H U_J^T.`                                  (3.8)

Since `M_I,M_J>=delta I`, both restricted frames have full column rank. The nonzero singular values of `B_0` are those of

`M_I^(1/2) Lambda_H M_J^(1/2)`

up to orthogonal partial isometries. The min-max inequality therefore gives

`s_3(B_0)>=delta s_3(Lambda_H)>=delta.`                               (3.9)

For the full cross block

`B=A[I,J]=B_0+E[I,J]`,

Weyl's singular-value inequality and (3.6) imply

`s_3(B)>=delta-tau=sigma.`                                            (3.10)

There is no assumption that `E` is independent noise; it remains part of the same deterministic matrix.

Next, because `Lambda_H` is invertible and `U_J` has full column rank,

`range(B_0)=range(U_I).`                                               (3.11)

The projection onto this range is

`P_S=U_I M_I^(-1) U_I^T`,

so each physical-coordinate leverage obeys

`(P_S)_ii <= ||u_i||^2/delta <= eps/delta.`                            (3.12)

Take

`gamma=sigma/sqrt(6).`                                                 (3.13)

Apply the ridge perturbation estimate (2.3) with `F=E[I,J]`, `eta=tau` and `ell=eps/delta`. It gives

`max_i(K_gamma)_ii
 <= [sqrt(eps/delta)+tau/gamma]^2
 =  [sqrt(eps/delta)+sqrt(6)tau/sigma]^2
 <= 1/2`                                                               (3.14)

by hypothesis (3.3).

Meanwhile (3.10) supplies three singular values at least `sigma`, hence

`theta_gamma >= 3 sigma^2/(gamma^2+sigma^2)=18/7>2.`                  (3.15)

The `q=1` ridge theorem (2.2) now gives (3.4). Its Fourier envelope lies in `L^1`, so the density is continuous and vanishes at infinity. All conditioning in the ridge proof is on original independent coordinates. QED.

## 4. Clean enlargement: cutoff `1/39` at leverage `1/32`

Take

`eps=1/32`, `tau=1/39`.

Then

`delta=1/2-1/32-1/4=7/32`,                                           (4.1)

and

`sigma=7/32-1/39=241/1248
      =0.193108974358974... .`                                        (4.2)

The leverage term in (3.14) is exactly

`1/sqrt(7) + 32 sqrt(6)/241.`                                         (4.3)

A fully rational strict certificate is

`1/sqrt(7)<19/50`,

`32 sqrt(6)/241<163/500`.

Therefore

`1/sqrt(7)+32 sqrt(6)/241 < 353/500`,

and

`(353/500)^2=124609/250000=0.498436<1/2.`                             (4.4)

Thus Theorem 3.1 applies and gives the following.

### Corollary 4.1 — `QFORM-SPECTRAL-WINDOW-1OVER39-v1`

Let `P` project onto **all** eigenspaces of `A` with `|lambda|>=1/39`. If `A` has at least three eigenvalues of modulus at least one and

`max_i P_ii <= 1/32`,                                                  (4.5)

then `X^TAX` has a continuous `C_0` density with

`boxed(
 ||p_Q||_infinity
 <= 5616 sqrt(3e)/241
 = 66.5453823693691... .
)`                                                                     (4.6)

Every eigenvalue below `1/39` in modulus may be nonzero, of either sign, arbitrarily numerous and arbitrarily oriented. Every eigenvalue above the cutoff is retained exactly, including arbitrarily large additional eigenvalues of either sign.

The preceding source theorem used cutoff `1/64` at the same leverage threshold `1/32`. The present clean cutoff is larger by the exact factor

`(1/39)/(1/64)=64/39=1.64102564... .`                                 (4.7)

For orientation, at `eps=1/32` the exact boundary of condition (3.3) is

`tau_* = delta a/(sqrt(6)+a),`

`a=1/sqrt(2)-1/sqrt(7)`,                                               (4.8)

which is

`tau_*=0.025911987839088... = 1/38.592176... .`                        (4.9)

So `1/39` is a simple rational cutoff close to the limit of this exact MSS-plus-ridge mechanism.

## 5. Exhaustive target-level consequence: diffuse window or heavy physical row

The spectral-window theorem becomes more useful when its failure is translated back to the original coordinates.

Let `P=P_{1/39}`. Since every target matrix has at least three eigenvalues of modulus at least one, either

**(D) diffuse window:** `max_i P_ii<=1/32`, in which case Corollary 4.1 closes the matrix with the continuous density bound (4.6); or

**(H) high spectral leverage:** there exists an original coordinate `i` with

`P_ii>1/32.`                                                           (5.1)

In branch (H), write the spectral decomposition of the physical column `Ae_i`. Then

`||Ae_i||_2^2
 = e_i^T A^2 e_i
 = sum_j lambda_j^2 |<e_i,r_j>|^2
 >= (1/39^2) P_ii
 > 1/(32*39^2)
 = 1/48672.`                                                           (5.2)

But in original coordinates

`||Ae_i||_2^2 = A_ii^2 + ||A_{-i,i}||_2^2.`                           (5.3)

The identity

`1/48672 = 2/312^2`                                                    (5.4)

therefore proves:

### Theorem 5.1 — `QFORM-WINDOW-OR-PHYSICAL-ROW-v1`

Every matrix satisfying the owner's three-large-eigenvalue hypothesis obeys at least one of the following:

1. `Q=X^TAX` already has a continuous density bounded by `66.546` via Corollary 4.1; or
2. there is an original physical coordinate `i` with

`boxed( |A_ii|>1/312 )`                                                (5.5)

or

`boxed( ||A_{-i,i}||_2>1/312 ).`                                      (5.6)

No rotation of the input variables is used in this dichotomy. The second branch is a fixed-scale physical pivot/cross-bank certificate and is stable under arbitrary extra eigenvalues because it was derived from the entire `|lambda|>=1/39` spectral window.

This does **not** by itself close branch (H): one heavy off-diagonal row is rank one as a cross block and the ridge theorem requires effective dimension strictly above two. The point is that the residual full-target bridge has been moved to an original-coordinate heavy-row problem with an explicit universal threshold rather than a vague spectral-localization debt.

## 6. Actual fleet04 theorem application on the heavy-pivot branch

The exact assigned partner `fleet04/B12` has no completed current-QFORM theorem visible at the source-bound refresh, so no incompatible FEI artifact is reused. To keep the fleet04 collaboration mathematical rather than nominal, apply the completed fleet04/B18 theorem

`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`,

source `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Suppose branch (H) produces a physical pivot

`a=A_ii !=0`.

Write

`A = [[a,b^T],[b,C]]`

in that original coordinate and set

`S=C-bb^T/a.`                                                         (6.1)

Completing the square gives the exact identity

`Q = X_{-i}^T S X_{-i}
    + a (X_i+a^(-1)b^T X_{-i})^2.`                                   (6.2)

Assume, as a **further checkable condition**, that `S` has at least three eigenvalues of modulus at least `L>0` and that its spectral projection onto `|lambda(S)|>=L/39` has maximum physical-coordinate diagonal at most `1/32`. Applying Corollary 4.1 to `S/L` gives a base density bound

`M <= C_win/L`,

`C_win=5616 sqrt(3e)/241.`                                             (6.3)

Conditioned on the base value `R=X_{-i}^T S X_{-i}`, the translated variable

`V=X_i+a^(-1)b^T X_{-i}`

has a density bounded by one: it is a mixture of translations of the original density of `X_i`, which is independent of `X_{-i}`. It is generally **not independent** of `R`; this is exactly where the fleet04 theorem is needed. Its dependent-square lemma gives

`boxed(
 ||p_Q||_infinity
 <= 2 sqrt(C_win/(|a|L)).
)`                                                                     (6.4)

For the heavy-pivot threshold `|a|>1/312` and `L=1`, this is

`||p_Q||_infinity < 288.182.`                                         (6.5)

This is a genuine application of completed fleet04 mathematics to an actual current-QFORM inequality. It is conditional on the stated Schur-complement window and does not claim that the original three-large-eigenvalue hypothesis automatically passes three large eigenvalues to `S`; such a claim would revive a refuted single-Schur structural shortcut.

## 7. What arbitrary extra eigenvalues now cost

The mechanism can be summarized quantitatively.

* All eigenvalues with `|lambda|>=1/39`, regardless of sign or magnitude, are retained in `A_H`; they are **not** treated as perturbative noise.
* The entire complementary spectral tail, regardless of rank, sign pattern or orientation, costs only its operator norm `1/39` in the cross singular-value and ridge-leverage estimates.
* If this full high spectral window is diffuse in physical coordinates, the density is already bounded continuously.
* If it is not diffuse, the failure itself pays a fixed physical-row energy, producing the `1/312` pivot/cross-bank branch.

This is stronger than a theorem that allows only one exceptional eigenvalue or a bounded-rank perturbation. The remaining difficulty is not the mere presence of additional eigenvalues; it is the product-preserving treatment of the forced heavy physical row when the high spectral space is localized.

## 8. Checker and exact constants

`CHECK.py` uses exact rational arithmetic for the strict certificate (4.4), the identity (5.4), and the rational value `sigma=241/1248`. It also prints the numerical ridge leverage, density constant and limiting cutoff. The archived output is:

```text
QFORM_B12_WINDOW_CHECK_PASS
sigma=241/1248=0.19310897435897437
ridge_sqrt_exact=0.7032079243331346
ridge_leverage_exact=0.49450138484491557
rational_ridge_upper=353/500 square=0.498436
C_window=66.5453823693691
tau_star=0.025911987839088085 reciprocal=38.592176185398856
cutoff_gain=64/39=1.641025641025641
heavy_row_energy_floor=1/48672=2.05456936226167e-05
partner_pivot_corollary_C_if_abs_a_ge_1_over_312_and_L_1=288.1816045429906
```

The computation checks constants only; the theorem is the analytic argument above.

## 9. Exact status and next unpaid implication

**Proved in the stated supporting scope, conditional on the supplied ridge theorem's analytic proof:**

* `QFORM-PARAMETRIC-SPECTRAL-WINDOW-v1`;
* `QFORM-SPECTRAL-WINDOW-1OVER39-v1`;
* `QFORM-WINDOW-OR-PHYSICAL-ROW-v1`;
* the dependent-square heavy-pivot corollary (6.4), by actual application of fleet04/B18.

**Continuity:** proved in the diffuse spectral-window branch through the `L^1` characteristic-function estimate. The dependent-square corollary is asserted only as an essentially bounded-density conclusion here. Continuity for the unrestricted target remains open.

**Full QFORM:** `OPEN / NOT PROVED`.

The first unpaid implication is now:

`QFORM-HEAVY-PHYSICAL-ROW-CLOSURE-v1` — starting from an original coordinate satisfying either `|A_ii|>1/312` or `||A_{-i,i}||_2>1/312`, while retaining the sole global hypothesis of three eigenvalues of modulus at least one and arbitrary additional spectrum, derive a dimension-free density bound or reduce to an already paid aggregate branch. The proof must aggregate before paying reciprocal local minors and must not assume that a scalar Schur complement inherits three large eigenvalues.

The natural next attempt is to combine the physical-row certificate with the existing rank-two `L^3` diffuse theorem and dependent-square smoothing, splitting according to whether the Schur complement retains a diffuse rank-two spectral bank; the complementary branch should feed the Pluecker collar/localized-chain mechanism rather than another one-minor extraction.

No novelty or publication-priority claim is made.
