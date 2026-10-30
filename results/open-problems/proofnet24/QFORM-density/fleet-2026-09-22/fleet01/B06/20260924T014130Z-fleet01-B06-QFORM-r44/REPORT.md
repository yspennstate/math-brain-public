SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-24T01:41:30Z.
attacking: shared-bank diagonal-plus-rank-one-square averaging — retain the original-coordinate quadratic curvature, obtain a translation-uniform square-root small-ball profile without a fiber supremum, and feed it to fleet02/B06's completed physical-pair logarithmic receiver.

# fleet01/B06 r44 — physical-curvature small-ball receiver for the fully shared rank-one-square bank

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `NEW SUPPORTING ANALYTIC THEOREM + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full unrestricted conjecture and the requested global continuity conclusion remain OPEN. This report proves essential boundedness only in the stated branches.

## 1. Source boundary


The designated partner input actually used is fleet02/B06:

- `yspennstate/math-open-problems@f3cb7a2b4cd43febe06534df231125fbd13a138d`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260924T003626Z-7f1a9c2d/REPORT.md`,
- theorem `QFORM-PAIR-RANK1SQUARE-WEIGHTED-v1`.

Its completed theorem pays an invertible indefinite literal physical pair once the exact remainder is a rank-one square on one original-coordinate bank plus arbitrary curvature on a disjoint bank. Its explicit bound is

`||p_Q||_infinity <= 8 sqrt(2) [|det B| sigma_min(B) |lambda| ||w||_2^2]^(-1/4)`.

The second analytic dependency is the completed physical-pair logarithmic theorem

- `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
- `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

If the post-pair remainder `R` satisfies

`sup_t P(|R-t|<rho) <= H sqrt(rho)`

for every `rho>0`, then

`||p_Q||_infinity <= 4 sqrt(2H) [|det B| sigma_min(B)]^(-1/4)`.

I also use the completed physical two-original-coordinate affine half-Riesz estimate from

- `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
- `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`:

`sup_t E |Y^T C Y+2 beta^T Y-t|^(-1/2) <=16 sqrt(30) |det C|^(-1/4)`

for an invertible symmetric `2 x 2` physical block `C` on two independent original cap-one coordinates.

No pointwise law-uniform quadratic-phase decay, no independence after rotation, no arbitrary-joint coarea bound, no positive moment of worst conditional projection-density heights, and no unrestricted curved-fiber supremum are used.

## 2. Physical-curvature square-root small-ball theorem

### Theorem `QFORM-PHYSICAL-CURVATURE-SQRT-SMALLBALL-v1`

Let `Y_1,...,Y_m` be independent real variables with probability densities at most one, and let

`S(Y)=Y^T M Y+2 ell^T Y+c`,

where `M=M^T` is nonzero. Define the original-coordinate physical-curvature scale

`chi(M) := max { max_i |M_ii|,
                 max_{i<j} |det M_{ {i,j},{i,j} }|^(1/2) }.`       (2.1)

Then `chi(M)>0` and, for every `rho>0`,

`boxed:
 sup_t P(|S-t|<rho)
 <=16 sqrt(30) chi(M)^(-1/2) sqrt(rho).`                           (2.2)

The estimate is translation-uniform in `ell` and `c`.

### Proof

If `chi(M)=0`, every physical diagonal vanishes. For `i!=j`, the `2 x 2` principal determinant is then `-M_ij^2`, so every off-diagonal entry also vanishes, contradicting `M!=0`.

If some diagonal obeys `|M_ii|=chi(M)`, condition on all original coordinates except `Y_i`. The conditional polynomial is

`a y^2+b y+c_0`, `|a|=chi(M)`.

After completing the square, the inverse image of an interval of radius `rho` has total Lebesgue length at most

`2 sqrt(2 rho/|a|)`.

Since the conditional input density is at most one,

`P(|S-t|<rho | Y_{-i}) <=2 sqrt(2) chi(M)^(-1/2) sqrt(rho)`,

uniformly in the conditioning and in `t`. This is stronger than (2.2).

Otherwise choose `i<j` with

`|det C|^(1/2)=chi(M)`, `C=M_{ {i,j},{i,j} }`.

Condition on all original coordinates outside this pair. The pair remains independent with density caps one; all conditioned couplings produce only an affine vector and a constant. The completed physical-pair half-Riesz theorem therefore gives

`sup_t E[ |S-t|^(-1/2) | Y_{-(i,j)} ]
 <=16 sqrt(30) |det C|^(-1/4)
 =16 sqrt(30) chi(M)^(-1/2).`                                    (2.3)

On `{|S-t|<rho}`, one has `|S-t|^(-1/2)>rho^(-1/2)`. Hence (2.3) implies the same conditional right side as (2.2) after multiplication by `sqrt(rho)`. Average the conditioning. QED.

This theorem does not select or invert a spectral-coordinate minor. It uses either one literal original scalar curvature or one literal original physical pair, and the rest of the product law is averaged before the outer curved-pair singularity is paid.

## 3. Compiler with an outer indefinite physical pair

### Theorem `QFORM-OUTERPAIR-PHYSICALCURVATURE-WEIGHTED-v1`

Let `X_1,X_2` be a literal original-coordinate pair, independent of the remaining product bank `Y`. Suppose after exact completion of that pair

`Q=((X_1,X_2)+m(Y))^T B ((X_1,X_2)+m(Y)) + S(Y)`,              (3.1)

where `B` is invertible indefinite, `m(Y)` is arbitrary, and `S` has quadratic matrix `M!=0` as in Section 2. Put

`D_B=|det B|`, `kappa_B=sigma_min(B)`.

Then

`boxed:
 ||p_Q||_infinity
 <= C_pc [D_B kappa_B chi(M)]^(-1/4),`                            (3.2)

where

`C_pc = 4 sqrt(32 sqrt(30)) = 52.95601471434997... .`

### Proof

Theorem (2.2) supplies the pair-log theorem with

`H=16 sqrt(30) chi(M)^(-1/2)`.

Substitution into

`4 sqrt(2H)(D_B kappa_B)^(-1/4)`

gives (3.2). The outer pair theorem explicitly permits the center `m(Y)` to depend arbitrarily on the remainder, so no conditional-independence shortcut is used. QED.

## 4. Exact application to the shared diagonal plus rank-one square

The partner's first unpaid equation was

`S(Y)=sum_j d_j Y_j^2 + lambda (w dot Y)^2`,                      (4.1)

where the diagonal terms and `w` can use the SAME original coordinates. Set

`M=diag(d)+lambda w w^T`,
`a_i=d_i+lambda w_i^2`.

Then the exact physical `2 x 2` determinants are

`boxed:
 det M_{ {i,j},{i,j} }
 =d_i d_j+lambda(d_i w_j^2+d_j w_i^2)
 =a_i a_j-lambda^2 w_i^2 w_j^2.`                                 (4.2)

Therefore the fully shared bank is paid whenever its physical-curvature scale

`chi_sh = max{ max_i |a_i|,
               max_{i<j}|a_i a_j-lambda^2 w_i^2 w_j^2|^(1/2) }`  (4.3)

is nonzero:

`boxed:
 ||p_Q||_infinity
 <=52.956015 [D_B kappa_B chi_sh]^(-1/4).`                        (4.4)

There is no disjointness assumption between `d` and `w` in (4.4).

### A cancellation-resistant two-heavy-coordinate corollary

For every `i<j`, put `b_ij=|lambda w_i w_j|`. If either `|a_i|` or `|a_j|` is at least `b_ij/sqrt(2)`, then `chi_sh>=b_ij/sqrt(2)`. Otherwise

`|a_i a_j|<b_ij^2/2`,

and (4.2) gives

`|det M_{ij}|>b_ij^2/2`,

so again `chi_sh>b_ij/sqrt(2)`. Hence

`boxed:
 chi_sh >= (|lambda|/sqrt(2)) max_{i<j}|w_i w_j|.`                (4.5)

Let `p_i=w_i^2/||w||_2^2`, ordered `p_1>=p_2>=...`. Then

`max_{i<j}|w_i w_j|=||w||_2^2 sqrt(p_1 p_2)`,

and therefore

`boxed:
 ||p_Q||_infinity
 <=57.748944
 [D_B kappa_B |lambda| ||w||_2^2 sqrt(p_1 p_2)]^(-1/4).`         (4.6)

In particular if `p_2>=eta`, then

`||p_Q||_infinity
 <=57.748944 eta^(-1/4)
 [D_B kappa_B |lambda| ||w||_2^2]^(-1/4).`                       (4.7)

Thus arbitrary shared diagonal curvature cannot hide a rank-one square whose coefficient vector has two quantitatively heavy original coordinates: either a physical diagonal survives or a physical `2 x 2` determinant survives.

## 5. Direct designated-partner application: zero-diagonal subbank

There is a second exact endpoint that uses fleet02/B06's completed theorem itself, not merely its proof ingredients.

Let

`J_0={j:d_j=0}`

and suppose `w_{J_0}!=0`. Condition on every coordinate in `K=J_0^c`. Then (4.1), as a function of the remaining product bank, is

`lambda (w_{J_0} dot Y_{J_0}+c_K)^2 + C_K`,                      (5.1)

while the outer physical-pair center may still depend arbitrarily on `Y_{J_0}`. Choose a deterministic vector `s_K` on `J_0` with

`w_{J_0} dot s_K=c_K`

and translate the remaining original variables by `s_K`. Translation preserves their independence and density caps. Conditional on `Y_K`, equation (5.1) is therefore exactly in the hypotheses of fleet02/B06's theorem with coefficient vector `w_{J_0}` and with no disjoint remainder needed. It gives the actual inequality

`||p_{Q | Y_K}||_infinity
 <=8 sqrt(2)
 [D_B kappa_B |lambda| ||w_{J_0}||_2^2]^(-1/4).`                 (5.2)

The right side is independent of the conditioned values. Averaging yields

`boxed:
 ||p_Q||_infinity
 <=8 sqrt(2)
 [D_B kappa_B |lambda| ||w_{J_0}||_2^2]^(-1/4).`                 (5.3)

This strictly extends the useful partner endpoint in the present shear-flat equation: `w` may have arbitrary additional mass on the coordinates carrying the diagonal curvature. Those coordinates are frozen first, and the genuinely zero-diagonal product subbank is retained as the curved third resource. No worst fiber density is taken.

## 6. What remains

The partner's fully shared debt is now reduced to a rigid chamber in which all three easy exits can fail simultaneously:

1. the zero-diagonal part of `w` has negligible or zero norm, so (5.3) is weak;
2. `w` has no quantitatively large second coordinate, so the cancellation-resistant two-heavy estimate (4.7) is weak;
3. the aggregate physical-curvature scale `chi_sh` in (4.3) is small, meaning the diagonal coefficients nearly cancel the rank-one square both on physical diagonals and on all useful `2 x 2` minors.

This remaining case is not a counterexample. It is the precise next obligation:

`QFORM-R48-FULLYSHARED-DIFFUSE-RANK1SQUARE-AGGREGATE-v1`:
aggregate the many small physical minors of `diag(d)+lambda ww^T` before reciprocal payment, or prove that simultaneous cancellation in (1)-(3) quantitatively forces the existing r48 two-heavy-hub / projected-crossing receiver to fire. A proof must preserve arbitrary fragmented cap-one product laws and arbitrary higher-rank tails.

The unrestricted QFORM conjecture remains OPEN. No target counterexample was found. Global continuity remains OPEN; the present theorems establish essential boundedness only in the stated branches.

## 7. Numerical constants and algebra audit

The only decimal constants used above are evaluations of exact closed forms:

`4 sqrt(32 sqrt(30)) = 52.95601471434997...`,

`4 sqrt(32 sqrt(30)) 2^(1/8) = 57.74894353713381...`.

The determinant identity (4.2) is exact; no numerical experiment is used as proof.
