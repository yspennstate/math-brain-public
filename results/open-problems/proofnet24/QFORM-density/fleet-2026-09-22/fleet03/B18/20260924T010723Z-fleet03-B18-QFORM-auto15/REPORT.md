SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-24T01:07:23Z.
attacking: Rudelson--Vershynin stable-rank small-ball transfer to a negative-moment cross-bank density bound, with a diffuse third spectral direction.

# fleet03/B18 — stable-rank cross-bank transfer

Run: `20260924T010723Z-fleet03-B18-QFORM-auto15`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `NEW SOURCE-VALID SUPPORTING THEOREM / TARGET-VALID FAMILY CLOSED / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains open. This report does **not** claim a literature novelty. Its main contribution is a direct transfer of a published small-ball theorem into an all-law quadratic-form density receiver which pays aggregate cross-bank stable rank without multiplying small singular values.

## 1. Primary literature and hypothesis match

The source is Mark Rudelson and Roman Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, International Mathematics Research Notices 2015, no. 19, 9594--9617; arXiv:1402.4492.

Two results are used exactly at their stated hypotheses.

1. **Theorem 1.2 (densities of sums).** If independent real random variables have densities bounded by `K`, then every normalized scalar linear combination has density at most `sqrt(2) K`.
2. **Corollary 8.6 (lossless stable-rank concentration).** If `Y=(Y_1,...,Y_n)` has independent coordinates with densities bounded by `K`, and `M` is a real matrix, then for every `tau>0`

   `L(MY, tau ||M||op) <= (C_RV K tau)^{r(M)}`,

   where

   `r(M)=floor(||M||HS^2/||M||op^2)`

   and `C_RV` is the absolute constant in that corollary.

The paper itself notes immediately before Corollary 8.6 that the lossless small-ball power can be useful for estimating negative moments of `||MY||`.

These results require independence and bounded one-dimensional densities, but **no** Gaussianity, log-concavity, moments, compact support, connected support, identical distribution, centering, symmetry, or smoothness. In the application below they are invoked only on genuine disjoint original-coordinate product banks. No rotated coordinates are declared independent.

For scope comparison, Herry--Malicet--Poly, arXiv:2303.09488, studies regularity of quadratic forms for iid inputs whose common law admits a sufficiently smooth Gaussian-field representation. That is a valuable quadratic-form regularity theorem but does not match the present arbitrary rough, non-iid cap-one target, so it is not used to enlarge the scope here.

## 2. New fleet theorem: stable-rank cross negative moment

### `QFORM-STABLERANK-CROSS-NEGATIVE-MOMENT-v1`

Let `X in R^m` and `Y in R^n` be independent original-coordinate product banks. Assume every one-dimensional coordinate density is bounded by one. Let `M` be a nonzero real `m x n` matrix and define

`r = floor(||M||HS^2 / ||M||op^2)`.

Assume `r>=2`. Let `alpha in R^m` be arbitrary and let `G:R^n->R` be any measurable function for which the displayed random variable is finite almost surely. Then

`R = X^T M Y + alpha^T X + G(Y)`

has a probability density and

`||p_R||infinity <= sqrt(2) C_RV [r/(r-1)] ||M||op^{-1}`.      (2.1)

In particular,

`||p_R||infinity <= 2 sqrt(2) C_RV ||M||op^{-1}`.             (2.2)

Only essential boundedness is claimed in this theorem; continuity is not claimed for arbitrary rough input laws.

### Proof

Set

`Z = ||MY+alpha||_2`.

For fixed `Y=y` with `My+alpha != 0`, the conditional variable

`R | {Y=y} = <My+alpha,X> + G(y)`

is a scalar linear combination of the genuine independent coordinates of `X`. Rudelson--Vershynin Theorem 1.2, after normalization, gives

`||p_{R|Y=y}||infinity <= sqrt(2)/||My+alpha||_2 = sqrt(2)/Z`.  (2.3)

Corollary 8.6 applies to the independent coordinates of `Y` with `K=1`. Since its concentration function is a supremum over centers, for every `t>0`

`P(Z<=t) <= min{1,(C_RV t/||M||op)^r}`.                        (2.4)

In particular `P(Z=0)=0`. Hence conditional densities exist for almost every `y` and may be averaged.

The remaining issue is the reciprocal moment. For any positive random variable,

`E Z^{-1} = integral_0^infinity P(Z<=t) t^{-2} dt`.

Put `t0=||M||op/C_RV`. Using (2.4),

`E Z^{-1}`
` <= integral_0^{t0} (C_RV t/||M||op)^r t^{-2} dt + integral_{t0}^infinity t^{-2} dt`
` = C_RV/[(r-1)||M||op] + C_RV/||M||op`
` = C_RV [r/(r-1)] ||M||op^{-1}`.                              (2.5)

Average (2.3) and use (2.5). This proves (2.1). Since `r>=2`, `r/(r-1)<=2`, which gives (2.2). No conditional cap is promoted to independence; the only independence used is the original `X`/`Y` product structure. QED.

## 3. Ambient quadratic lift

Let a real symmetric matrix be written in **original coordinates** split as `I sqcup J sqcup K`, and suppose

`A_{I,I}=0`.

Set `B=A_{I,J}` and

`r_B=floor(||B||HS^2/||B||op^2)`.

If `r_B>=2`, then the full ambient quadratic form, with arbitrary `A_{J,J}`, arbitrary `A_{K,K}`, arbitrary `J-K` and `I-K` couplings, and arbitrary additional spectrum, has a density satisfying

`||p_{X^T A X}||infinity <= (C_RV/sqrt(2)) [r_B/(r_B-1)] ||B||op^{-1}`.   (3.1)

In particular,

`||p_{X^T A X}||infinity <= sqrt(2) C_RV ||B||op^{-1}`.                 (3.2)

### Proof

Condition only the original coordinates `X_K=x_K`. The remaining `I` and `J` banks stay independent cap-one product banks, and

`X^T A X`
` = 2 X_I^T B X_J + 2 X_I^T A_{I,K}x_K + G_{x_K}(X_J)`

for a completely arbitrary measurable quadratic-affine function `G_{x_K}` on the `J` bank. Apply (2.1) with

`M=2B`, `alpha=2A_{I,K}x_K`.

Stable rank is scale invariant and `||2B||op=2||B||op`, so the conditional density is bounded by the right side of (3.1), uniformly in `x_K`. Averaging over `X_K` proves (3.1). QED.

This is a different currency from the determinant/product-of-selected-singular-values receiver proved in the preceding fleet03/B18 run. It can stay uniform when the second, third, ... individual singular values tend to zero, provided their **aggregate squared mass** keeps the floored stable rank at least two.

## 4. Concrete target-valid diffuse-third-direction family

Fix integers `N>=2` and `m>=2`. Let

`B_N = diag(1, N^{-1/2},...,N^{-1/2})`

with `N` copies of `N^{-1/2}`, and let

`D_m = (1/m) 1_m 1_m^T`.

On three disjoint original-coordinate banks define

`A_{N,m} = [[0,B_N,0],[B_N,0,0],[0,0,D_m]]`.                   (4.1)

Its spectrum is

`{+1,-1,+1, +N^{-1/2} (N copies), -N^{-1/2} (N copies), 0 (m-1 copies)}`.

Thus for every `N,m>=2` it has **exactly three** eigenvalues of absolute value at least one. No moment or support condition is imposed on any input density.

For the cross block,

`||B_N||op=1`,

`||B_N||HS^2 = 1 + N*(1/N) = 2`,

so `r(B_N)=2`. The ambient theorem (3.2) therefore gives the uniform all-law estimate

`boxed: ||p_{Q_{N,m}}||infinity <= sqrt(2) C_RV`,              (4.2)

independent of both `N` and `m`.

This closes a concrete target-level implication in a regime where the preceding selected-two-singular-value estimate is not uniform. Indeed its two largest cross singular values are `1` and `N^{-1/2}`, so that earlier bound becomes

`2 sqrt(pi) N^{1/4}`,

which diverges with `N`. The stable-rank theorem spends the whole cloud of `N` weak directions at once instead of selecting one weak direction and paying its reciprocal.

For this block-diagonal family, continuity can also be recorded separately. The cross-bank part has an `L^1 cap L^infinity` density by (2.1). The independent `D_m` contribution is

`(m^{-1/2} sum_{j=1}^m W_j)^2`,

which has an `L^1` density. Convolution with this independent `L^1` density preserves the `L^infinity` bound and is uniformly continuous; because the result is also integrable it lies in `C_0`. Hence the family (4.1) has a **continuous `C_0` density** satisfying (4.2). This continuity statement is only for this independent-additive family, not for the generic ambient theorem (3.1).

## 5. Designated partner fleet04/B18 applied to the same family

The completed partner theorem is fleet04/B18 `QFORM-4COORD-NULLHUB-WINDOW-EDGE-DICHOTOMY-v1`, scientific commit `84fa5922df082f90064dea4d22a600a60e799803`, path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260923T221534Z-fleet04-B18-QFORM-r5/REPORT.md`.

For an original-coordinate exact-rank-three `4x4` null-hub principal core whose nonzero eigenvalues lie in `s<=|mu_j|<=L`, and with a hub edge of magnitude at least `a`, it gives the full ambient bound

`||p_Q||infinity <= 576^{1/3} L^{2/3}/(s a^{2/3})`.             (5.1)

Apply it to (4.1) using the four physical coordinates consisting of the `1`-singular-value cross pair and two coordinates from the diffuse `D_m` bank. The principal core is

`[[0,1,0,0],`
` [1,0,0,0],`
` [0,0,1/m,1/m],`
` [0,0,1/m,1/m]]`,

whose eigenvalues are

`{1,-1,2/m,0}`.

Taking the first coordinate as hub gives `a=1`, `s=2/m`, and `L=1`. Therefore the partner theorem supplies the actual full-ambient inequality

`||p_{Q_{N,m}}||infinity <= (576^{1/3}/2) m`
`                         = 4.1601676461038... m`.              (5.2)

This is a valid source-pinned bound, but it deteriorates as the third spectral direction is diffused across more physical coordinates. The new stable-rank transfer (4.2) is uniform in exactly that parameter. This comparison is not a criticism of the partner theorem: the two receivers spend different geometry, and (5.2) confirms why aggregate-before-selection is necessary in the diffuse branch.

## 6. Scope, corrections, and remaining implication

The proof uses no law-uniform pointwise quadratic-phase decay, no arbitrary-joint coarea lemma, no independence after spectral rotation, no conditional-density-cap-as-independence step, no fixed-good-minor assertion, and no perturbative deletion of small nonzero coefficients. The stable-rank small-ball theorem is applied only to a genuine original-coordinate product bank.

The unrestricted conjecture remains **OPEN / NOT PROVED**, and unrestricted continuity remains open. The new theorem does **not** show that the bare spectral condition `s_3(A)>=1` forces a zero-self-curvature block `A_{I,I}=0` with `r(A_{I,J})>=2` and `||A_{I,J}||op` bounded below. That structural extraction, or a routing of its failure into the already-paid projected-crossing, ridge, grouped-hub, pair-log, or finite-core mechanisms, remains the missing connection to the full target.

A targeted literature check found no source in the examined papers that already states the full arbitrary-rough-law, arbitrary-sign, arbitrary-rank owner theorem. This is only a scope report, not a novelty claim.
