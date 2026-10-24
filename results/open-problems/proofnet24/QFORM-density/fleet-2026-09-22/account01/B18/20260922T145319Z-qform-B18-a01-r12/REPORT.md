# account01/B18 — LPP projection transfer to definite two-bank quadratic compression

**Programme:** QFORM-DENSITY-3EIG-20260922, owner revision 2026-09-22.5  
**Assignment:** Literature-to-proof transfer  
**Partner consumed:** account02/B18, immutable report `9147722aa884488601e7c039c6de5b0e0cdb77af`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260922T143051Z-account02-B18-qform-r11/REPORT.md`  
**Full target:** OPEN / NOT PROVED  
**Execution context:** WITHOUT_VERIFIED_BRAIN

## 1. Source-valid literature input

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877–889; arXiv:1507.07949, Theorem 1.1.

For a product density `f(x)=prod_i f_i(x_i)` with `||f_i||_infinity<=1`, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. In particular, for every unit vector `u`,

`||p_{<u,X>}||_infinity <= sqrt(2)`.

For a one-coordinate bank this improves trivially to `1`.

This source matches the present arbitrary cap-one product laws: it assumes no moments, centering, connected support, identical laws, Gaussianity, or log-concavity. It controls linear marginals only; I do not replace the product source by a generic bounded spectral marginal, which is invalid by the current shell correction.

## 2. Partner theorem, scaled exactly

The completed account02/B18 theorem `QFORM-PHYSICAL-DEFINITE-2X2-v1` states that if two independent cap-one real variables `(U,V)` enter a quadratic expression with a positive- or negative-definite `2 x 2` coefficient matrix `B`, with arbitrary linear terms depending on independent outside variables and arbitrary outside remainder, then the resulting scalar law has density

`||p||_infinity <= pi / sqrt(|det B|)`.

Its proof conditions on the outside variables, completes the square, applies the linear map `|B|^(1/2)`, and uses polar coarea.

A scaling consequence needed below is the following. If instead

`||p_U||_infinity <= M_1`, `||p_V||_infinity <= M_2`,

then

`||p||_infinity <= pi M_1 M_2 / sqrt(|det B|)`.                    (2.1)

Indeed put `U'=M_1 U`, `V'=M_2 V`. Their densities are cap one, and the quadratic matrix in `(U',V')` is `D^{-1} B D^{-1}`, `D=diag(M_1,M_2)`, whose determinant is `det(B)/(M_1^2 M_2^2)`. This is a direct application of the completed partner theorem, not merely a citation.

## 3. New transfer theorem: definite two-bank compression

### Theorem — `QFORM-LPP-TWO-BANK-DEFINITE-v1`

Let the physical coordinates be partitioned into three disjoint sets `I,J,K`. Let `u in R^I` and `v in R^J` be unit vectors. Suppose the quadratic form has the exact structure

`Q = b_11 Y^2 + 2 b_12 Y Z + b_22 Z^2
     + 2 Y ell_1(X_K) + 2 Z ell_2(X_K) + R(X_K)`,                (3.1)

where

`Y=<u,X_I>`, `Z=<v,X_J>`,

`ell_1,ell_2` are arbitrary real linear forms of the remaining coordinates, `R` is an arbitrary real quadratic form on `K`, and

`B=[[b_11,b_12],[b_12,b_22]]`

is positive or negative definite. All physical coordinates are independent and have densities bounded by one.

Then `Q` has an essentially bounded density satisfying

`||p_Q||_infinity <= 2 pi / sqrt(|det B|)`.                     (3.2)

If `I` is a singleton, the constant improves to

`||p_Q||_infinity <= pi sqrt(2) / sqrt(|det B|)`,               (3.3)

and if both `I,J` are singletons it improves to the partner bound

`||p_Q||_infinity <= pi / sqrt(|det B|)`.                       (3.4)

In particular, whenever `|det B|>=1`, this branch has the universal cap `2 pi`.

### Proof

Because `I,J,K` are disjoint physical coordinate sets, `Y`, `Z`, and `X_K` are mutually independent. By LPP Theorem 1.1,

`M_1:=||p_Y||_infinity <= sqrt(2)`,
`M_2:=||p_Z||_infinity <= sqrt(2)`.

If a bank is a singleton, its corresponding cap is at most one.

Condition on `X_K=z`. Equation (3.1) becomes a two-variable definite quadratic polynomial in the independent variables `(Y,Z)` with the same fixed quadratic matrix `B` and arbitrary fixed linear coefficients. Apply the scaled partner estimate (2.1): every conditional density is bounded by

`pi M_1 M_2 / sqrt(|det B|) <= 2 pi/sqrt(|det B|)`.

Averaging the conditional densities over `X_K` preserves this same `L^infinity` bound. The singleton improvements follow by replacing the corresponding `sqrt(2)` by `1`. QED.

### Matrix form of the hypothesis

The theorem is an original-coordinate statement. Equation (3.1) is equivalent to

`A_II=b_11 u u^T`, `A_JJ=b_22 v v^T`, `A_IJ=b_12 u v^T`,

with the `I-K` and `J-K` cross blocks having column spaces contained respectively in `span(u)` and `span(v)`. The `K-K` block is arbitrary. Thus the result allows arbitrary dimension, arbitrary small/large remaining eigenvalues, arbitrary signs in `R`, and arbitrary aligned outside coupling. It does not rotate the full product law.

## 4. Continuity in the diagonal-bank subcase

The full target asks that continuity be tracked separately. Under the additional condition `b_12=0`, the density in this theorem has a continuous representative.

After conditioning on `X_K=z` and completing the two scalar squares, the two terms are independent translated-square transforms. Each scalar square transform has an `L^1` density. The convolution of two `L^1(R)` densities belongs to `C_0(R)`. Its `L^infinity` norm is uniformly bounded by the estimate above. Hence the conditional density is continuous for every fixed `z`; dominated convergence using the uniform cap gives continuity after averaging over `z`.

I do not claim this continuity argument for arbitrary `b_12!=0`: after diagonalizing a non-diagonal `B`, independence of `(Y,Z)` is lost, and a generic coarea density need not be continuous for merely measurable input densities.

## 5. Concrete application: the rank-three correction family

Apply the theorem to the exact stress family from `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`,

`A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`,

whose nonzero spectrum is `{1,1,-1}`. Write

`U = m^(-1/2) sum_{i=1}^m Y_i`,
`V = m^(-1/2) sum_{i=1}^m Z_i`.

Then

`Q_m = X_0^2 + U^2 - V^2`.

The first positive bank is a singleton, so `||p_{X_0}||_infinity<=1`; LPP gives `||p_U||_infinity<=sqrt(2)`. With `B=I_2`, (3.3) gives

`||p_{X_0^2+U^2}||_infinity <= pi sqrt(2)`.

The random variable `-V^2` is independent of the positive part, so convolution with its probability law cannot increase the `L^infinity` norm. Therefore

`||p_{Q_m}||_infinity <= pi sqrt(2) = 4.442882938...`            (5.1)

for every `m` and every cap-one choice of the independent input densities. The positive two-bank density is continuous, and convolution with the independent probability law of `-V^2` preserves continuity, so `Q_m` has a continuous density as well.

This gives an explicit source-pinned constant for the correction family. It is not asserted to be new; the correction already records that this family is uniformly controlled by bank aggregation.

## 6. Relation to the full conjecture

This theorem strictly extends the literal physical-coordinate definite `2 x 2` theorem to **linear aggregates of disjoint coordinate banks**, using the sharp LPP marginal estimate to retain the product provenance. It covers non-diagonal physical blocks such as `J_m/m` uniformly, where any fixed physical `2 x 2` determinant degenerates like `1/m`.

It does **not** close the unrestricted three-large-eigenvalue conjecture. The spectral hypothesis alone does not currently force two disjoint coordinate banks through which all relevant couplings factor as in (3.1). The correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` specifically rules out replacing that missing aggregation step by a uniformly good local principal block or rank-three coordinate cut.

The first unpaid implication for this pathway is therefore:

**BANK-EXTRACTION/AGGREGATION GAP.** Starting only from at least three eigenvalues with absolute value at least one, prove that either an existing diffuse/cross-block branch applies, or construct a source-valid aggregation of physical coordinate banks that yields a definite two-dimensional compression with determinant bounded below, without conditioning away the product-density caps.

A generic bounded spectral marginal is not enough, a single cross minor is not enough, and conditional sum/difference density caps are not available; all three are live corrections respected here.

## 7. Literature audit status

The primary theorem actually transferred in this run is LPP Theorem 1.1. Rudelson–Vershynin's linear-image small-ball theory is compatible background but does not itself give the required interval-linear quadratic pushforward estimate. The literature checked in this pathway has not supplied an exact theorem matching the full arbitrary-product, rotated-indefinite quadratic target, so no prior-solution or novelty claim is made.

## 8. Status

- `QFORM-LPP-TWO-BANK-DEFINITE-v1`: **PROVED supporting target-level branch**.
- Exact family `A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`: **PROVED density cap `pi sqrt(2)` and continuity** under arbitrary independent cap-one inputs.
- Partner account02/B18 theorem: **substantively applied** through the exact scaled inequality (2.1).
- Full QFORM conjecture: **OPEN / NOT PROVED**.
