# fleet01/B18 — literature-to-proof transfer: one-sided-zero rank-two cross block

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T135329Z-qform-B18-a01-r11`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_THEOREM / ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and live constraints

The full target remains OPEN: for every `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one dimension/law/matrix-independent finite `L^infinity` bound. Continuity is tracked separately.

This run respects all live corrections through brain main `fd0b705b5049bd5b12d42fa0b2bb27d59a0043e5`, including: no law-uniform pointwise Fresnel decay, no independence after spectral rotation, no unrestricted fiber-supremum argument, no forced single cross minor / single Schur rank-two extraction, no false conditional cap after sum/difference, and no fiberwise indefinite trace bound. The result below works only in original physical coordinates and is not promoted to a spectral-extraction theorem.

## 2. Primary literature transferred exactly

### Livshyts--Paouris--Pivovarov

G. Livshyts, G. Paouris, P. Pivovarov, **On sharp bounds for marginal densities of product measures**, Israel J. Math. 216 (2016), 877--889, DOI `10.1007/s11856-016-1431-5`, arXiv `1507.07949`.

Their Theorem 1.1 states: if `f(x)=prod_i f_i(x_i)`, each `f_i` is a probability density, and `E` is a `k`-dimensional subspace of `R^n`, `1<=k<n`, then

`||pi_E f||_infinity <= min{ (n/(n-k))^((n-k)/2), 2^(k/2) } prod_i ||f_i||_infinity^(gamma_i)`

for suitable `gamma_i in [0,1]`, `sum gamma_i=k`. Hence under the owner's normalization `||f_i||_infinity<=1`, every one-dimensional orthogonal projection has density at most `sqrt(2)` and every two-dimensional orthogonal projection has joint density at most `2`. If the ambient dimension equals the projection dimension (needed below only when `|J|=2`), orthogonal change of variables preserves the full product density and its pointwise cap is at most `1`, so the bound `2` remains valid.

### Kwan--Sauermann screening

M. Kwan, L. Sauermann, **Resolution of the quadratic Littlewood--Offord problem**, arXiv `2312.13826` (later Compos. Math.). Their main result gives the essentially optimal `O(m^{-1/2})` *point-concentration* estimate for quadratic polynomials in independent Rademacher variables under robust dependence, with an extension to arbitrary discrete independent variables. This is not an interval-small-ball theorem for the owner's arbitrary continuous densities and therefore cannot replace the scale-dependent Meka--Nguyen--Vu transfer used by the partner. No target-level conclusion is imported from it.

No exact published theorem matching the full owner quantifiers was found in this source pass. This is not a novelty claim.

## 3. New theorem: one-sided-zero physical cross block

### Theorem `QFORM-LPP-ONESIDED-CROSS2-v1`

Let the physical coordinates be partitioned as disjoint sets `I,J,K`. Write the corresponding symmetric matrix blocks and assume only

`A[I,I]=0`.

Let `B=A[I,J]` and suppose its two largest singular values satisfy

`sigma_1(B)=s_1 >= s_2=sigma_2(B)>0`.

There is **no restriction** on `A[J,J]`, `A[K,K]`, `A[J,K]`, or the cross block `A[I,K]`. If all original coordinates are independent and have densities at most one, then `Q=X^T A X` has a density satisfying

`||p_Q||_infinity <= 2 sqrt(2 pi) / sqrt(s_1 s_2).`                      (3.1)

Numerically `2 sqrt(2 pi)=5.0132565492620005...`. In particular, if `s_2>=1`, then

`||p_Q||_infinity <= 2 sqrt(2 pi).`                                    (3.2)

Moreover, under the same rank-two hypothesis `s_2>0`, `Q` has a continuous density (indeed a continuous representative vanishing at infinity).

### Proof

Condition on `Y=X_J` and `Z=X_K`. Because the `I-I` block is exactly zero, as a function of the still-independent vector `X_I` the quadratic form is linear:

`Q = 2 < X_I, B Y + C Z > + R(Y,Z)`,                                  (3.3)

where `C=A[I,K]` and `R` contains no `X_I`. Put

`v=v(Y,Z)=BY+CZ`.

For fixed `(Y,Z)` with `v!=0`, apply Livshyts--Paouris--Pivovarov in dimension one to the normalized direction `v/||v||`. The density of `<v,X_I>` is bounded by `sqrt(2)/||v||`; scaling by the factor two in (3.3) gives

`||p_{Q | Y,Z}||_infinity <= sqrt(2)/(2 ||v||).`                       (3.4)

It remains to average the reciprocal norm without losing dimension.

Take a singular-value decomposition of `B` and let `u_1,u_2` and `w_1,w_2` be its first two left and right singular vectors. Let `U_2=[u_1,u_2]` and let `W_2^T Y=(<w_1,Y>,<w_2,Y>)`. Orthogonal projection can only decrease norm, so, conditional on `Z=z`,

`||BY+Cz|| >= || U_2^T(BY+Cz) ||`

`             = || diag(s_1,s_2) W_2^T Y + c_z ||`.                  (3.5)

By the two-dimensional Livshyts--Paouris--Pivovarov marginal theorem, `W_2^T Y` has a density bounded by `2` when `|J|>2`; when `|J|=2`, an orthogonal coordinate change preserves the original joint density cap `<=1`, so the same upper bound `2` still holds. Therefore

`T_z := diag(s_1,s_2) W_2^T Y + c_z`

has a two-dimensional density bounded by

`L = 2/(s_1 s_2)`, uniformly in `z`.                                  (3.6)

For any planar random vector `T` with density at most `L`, and every `R>0`,

`E[1/||T||]`
` <= L integral_{||x||<=R} dx/||x|| + (1/R) P(||T||>R)`
` <= 2 pi L R + 1/R`.                                                  (3.7)

Optimizing at `R=(2 pi L)^(-1/2)` gives

`E[1/||T||] <= 2 sqrt(2 pi L)`.                                       (3.8)

Using (3.5)--(3.6), uniformly in `Z`,

`E_Y[1/||v|| | Z] <= 4 sqrt(pi/(s_1 s_2)).`                            (3.9)

Average (3.4), then use (3.9):

`||p_Q||_infinity`
` <= (sqrt(2)/2) E[1/||v||]`
` <= (sqrt(2)/2) * 4 sqrt(pi/(s_1 s_2))`
` = 2 sqrt(2 pi)/sqrt(s_1 s_2).`

This proves (3.1).

For continuity, conditional on `Z=z`, the random two-dimensional projection in (3.5) has a Lebesgue density. Hence with probability one `v(Y,z)` does not lie in the finite union of physical coordinate axes in `R^I` (their images under `U_2^T` are null one-dimensional sets). Thus almost surely at least two physical coefficients of the linear form `<v,X_I>` are nonzero. The convolution of the corresponding two scaled `L^1` densities is continuous and vanishes at infinity; convolution with the remaining independent factors preserves this. So `p_{Q|Y,Z}` admits a continuous representative almost surely. Its sup norm is dominated by the integrable random variable on the right of (3.4), whose expectation is finite by (3.9). Dominated convergence therefore makes `p_Q(q)=E p_{Q|Y,Z}(q)` continuous in `q` (and the same argument gives vanishing at infinity). QED.

## 4. Comparison with the completed Banks branch

The completed fleet03/B18 source transfer from Jesse Banks' 2022 thesis proves

`||p_Q||_infinity <= 2 sqrt(e pi)/sqrt(sigma_1(B)sigma_2(B))`

when the physical principal block on `I union J` is *pure bipartite*, i.e. both `A[I,I]=0` and `A[J,J]=0`, with arbitrary outside couplings. The theorem above improves the constant from

`2 sqrt(e pi)=5.84456...`

to

`2 sqrt(2 pi)=5.01326...`

and removes the condition `A[J,J]=0`: only one side must have zero self block. The proof uses only the sharp marginal-density theorem and original-coordinate conditioning. This comparison is scoped; it does not imply a rank-two block can always be extracted from three large eigenvalues.

The newer regularized-determinant theorem is complementary: it allows arbitrary self blocks on both sides, but at its unconditional exponent needs five large cross singular directions; with range leverage `<=1/2` it closes three cross singular directions. In the latter `q=1,r=3,sigma=1` case its stated formula gives `3e/sqrt(2)=5.7663465...`; with five unconditional singular directions it gives `5e/2=6.7957046...`. These branches do not subsume the new two-direction / one-zero-side branch.

## 5. Partner fleet02/B18 applied to an actual inequality

The assigned partner fleet02/B18 proved `QFORM-MNV-SWITCHING-MATCHING-v1` at scientific commit

`a6c63522402f375f1cae5194b1f9fc9bb667b9ce`,

report path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260922T130234Z-fleet02-B18-qform-r11b/REPORT.md`.

At the partner's specialization `a=1/4`, let `r_h` be the matching number of the physical graph

`G_h = { {i,j}: |A_ij| >= 8h }`.

For `r_h>=24`, the partner theorem gives, for every interval `[t,t+h]`,

`P(Q in [t,t+h]) <= exp(-r_h/32) + Psi_B(floor(r_h/8)),`               (5.1)

where `B` is the source's unspecified universal Meka--Nguyen--Vu constant and `Psi_B` is the exact decreasing-tail envelope defined in the partner report.

Set

`C_0 = 2 sqrt(2 pi)`

and, for `u>0`, define the finite source-dependent threshold

`R_B(u) = min { r>=24 : exp(-r/32)+Psi_B(floor(r/8)) <= u }`.          (5.2)

(The set is nonempty because the partner bound tends to zero as `r->infinity`.)

Now suppose at some scale `h>0` a form has

`sup_t P(Q in [t,t+h]) > C_0 h`.                                      (5.3)

Then two rigorous necessary conditions follow simultaneously:

1. There are no disjoint physical sets `I,J` with `A[I,I]=0` and `sigma_2(A[I,J])>=1`, because Theorem (3.1) would imply `sup_t P(Q in [t,t+h])<=C_0 h`.

2. The partner theorem applied with `u=C_0h` gives

`r_h < R_B(C_0 h)`.                                                    (5.4)

Therefore the endpoints of a maximal matching form a physical vertex cover `S_h` with

`|S_h| < 2 R_B(C_0 h)`,                                               (5.5)

and every off-diagonal coefficient `|A_ij|>=8h` touches `S_h`.

This is a concrete combined implication: **any scale-`h` violation of the new linear constant is forced into a bounded scale-dependent physical core and simultaneously avoids every one-sided-zero rank-two cross branch.** It materially uses the completed partner result rather than merely citing it.

It is not a full proof: `R_B(C_0h)` deteriorates as `h->0`, and the cloud of entries below `8h` can still have large aggregate operator norm. The live correction against forced single-minor/Schur extraction prevents deleting that diffuse remainder.

## 6. What the primary-source screen rules out / leaves open

Kwan--Sauermann's optimal quadratic Littlewood--Offord theorem controls atoms for discrete variables; it does not supply the interval-linear estimate needed to make (5.2) scale uniformly in `h`. Meka--Nguyen--Vu remains source-valid for the switch representation but only yields the scale-dependent core above.

The first unpaid implication remains an exhaustive heavy/nonseparable bridge from the spectral assumption (three eigenvalues `|lambda|>=1`) to one of the already-paid product-preserving branches, or an aggregate estimate that handles the residual cloud directly. In particular, a proof must cope with the known rank-three families for which every single small principal block or cross cut is weak.

A promising sharpened target suggested by (3.1) is not to demand a pure bipartite principal block: it is enough to find, after conditioning a physical set rather than rotating it, **one side with zero residual self-interaction and two cross singular directions with controlled product**. Failing that, the regularized determinant theorem handles arbitrary self interactions if three suitably diffuse cross directions appear. A valid full reduction between these alternatives is not yet proved.

## 7. Status

- `QFORM-LPP-ONESIDED-CROSS2-v1`: **PROVED_SUPPORTING_THEOREM** in this report; independent review not yet performed.
- Continuous-density conclusion for that branch: **PROVED_SUPPORTING_THEOREM**.
- Partner MNV matching theorem: **CONSUMED AND APPLIED** via (5.4)--(5.5).
- Exact prior full solution under the owner quantifiers: **NOT FOUND IN THIS SOURCE PASS**; no novelty inference is made.
- Full `QFORM-DENSITY-THREE-LARGE-EIGENVALUES`: **OPEN / NOT PROVED**.
