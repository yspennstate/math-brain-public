# QFORM account01/B18 — literature-to-proof transfer

Run: `20260924T075805Z-account01-B18-qform-auto11-r50`

Status: **PROVED SOURCE-VALID SUPPORTING THEOREM + COMPLETED PARTNER APPLIED / FULL QFORM OPEN**.

## Target and scope

Owner target: for arbitrary independent real coordinates with probability densities bounded by one and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal finite `L^infinity` density bound for `X^T A X`; continuity is tracked separately.

This report does **not** claim the unrestricted theorem. It proves an all-rank original-coordinate bipartite packet theorem, identifies its qualitative geometric-mean dependence as already present in Banks--Garza Vargas--Kulkarni--Srivastava, Corollary 2.4 of arXiv:2005.08930, sharpens the constants in the present cap-one scalar setting using Rudelson--Vershynin and Livshyts--Paouris--Pivovarov, and applies the completed account02/B18 moving-square theorem to an exact target-valid family.

No post-rotation independence, arbitrary-joint coarea, conditional projected-density cap, positive conditional-density moment, pointwise quadratic van der Corput bound, deletion of a small nonzero remainder, or fixed-good-minor assertion is used.

## Primary-source audit

### Banks--Garza Vargas--Kulkarni--Srivastava

The relevant source is **not a standalone paper titled “Density of Quadratic Forms.”** It is Section 2, Theorem 2.1 (“Density of Quadratic Forms”) and Corollary 2.4 in

> J. Banks, J. Garza Vargas, A. Kulkarni, N. Srivastava, *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations*, arXiv:2005.08930.

For scalar output (`k=1`), Corollary 2.4 treats

`q(X,Y)=X^T ZY+X^T U+V^T Y+W`

for two independent product banks whose one-dimensional entries have bounded densities. It proves a bound governed by the geometric mean of the top `j>=2` singular values of `Z`. Thus the qualitative all-`j` zero-self cross theorem below is a **published prior solution of that scoped analytic packet**. No novelty is claimed for the qualitative packet or geometric-mean mechanism.

### Rudelson--Vershynin

Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492, Theorem 1.2: if independent real variables have densities bounded by `K` and `sum a_i^2=1`, then the density of `sum a_i X_i` is bounded by the sharp `sqrt(2) K`. No moments, iid assumption, centering, support restriction, symmetry, smoothness, or log-concavity are imposed.

### Livshyts--Paouris--Pivovarov

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1: if `f=prod_i f_i` and each one-dimensional probability density is bounded by one, then every `j`-dimensional orthogonal marginal has density bounded by `2^(j/2)` (indeed their theorem gives the minimum of this and another dimension-dependent bound). This is used only as a **joint marginal density cap**. No independence is asserted after projection.

A targeted search did not locate a published theorem closing all of the owner's unrestricted quantifiers. This is a scope statement, not a novelty claim.

## Theorem A — explicit Banks--LPP geometric-mean cross packet

Let `X=(X_i)_{i in I}` and `Y=(Y_j)_{j in J}` be independent product banks, with every scalar coordinate density bounded by one. Let `B` be a real `|I| x |J|` matrix of rank `r>=2`, with singular values

`sigma_1 >= ... >= sigma_r > 0`.

For arbitrary deterministic affine coefficients `alpha,beta,c`, set

`q = 2 X^T B Y + alpha^T X + beta^T Y + c`.

Let

`v_j = pi^(j/2) / Gamma(j/2+1)`

be the volume of the Euclidean unit ball in `R^j`. Then `q` has a density and

`||p_q||_infinity <= min_{2<=j<=r} [ j/(j-1) * v_j^(1/j) / (prod_{i=1}^j sigma_i)^(1/j) ].`       (A.1)

### Proof

Fix `j` with `2<=j<=r`, and condition on `Y=y`. Apart from a deterministic translation, the conditional random variable is the linear form

`(2By+alpha)^T X`.

By Rudelson--Vershynin Theorem 1.2, whenever the coefficient is nonzero its conditional density is bounded by

`sqrt(2) / ||2By+alpha||_2`.       (A.2)

Take an SVD `B=U Sigma V^T`; let `U_j,V_j` contain the top `j` singular vectors and `Sigma_j=diag(sigma_1,...,sigma_j)`. Then

`||2By+alpha|| >= ||2 Sigma_j V_j^T y + U_j^T alpha||`.       (A.3)

The random vector `V_j^T Y` is a genuine `j`-dimensional orthogonal marginal of the original cap-one product law. Livshyts--Paouris--Pivovarov therefore gives

`||p_{V_j^T Y}||_infinity <= 2^(j/2)`.

After the invertible linear map `z -> 2 Sigma_j z` and a translation, the vector

`W = 2 Sigma_j V_j^T Y + U_j^T alpha`

has density cap

`L_j = 2^(j/2) / det(2 Sigma_j)
     = 2^(-j/2) / prod_{i=1}^j sigma_i`.       (A.4)

For every probability density `f` on `R^j` satisfying `0<=f<=L`, the radial bathtub principle gives, for `j>1`,

`int ||z||^(-1) f(z) dz <= j/(j-1) * (L v_j)^(1/j)`.       (A.5)

Indeed, because `||z||^-1` is radially decreasing, the maximal integral under the cap and mass constraints is attained by `L 1_{||z||<=R}`, where `L v_j R^j=1`; direct radial integration yields (A.5).

Using (A.3)--(A.5),

`E ||2BY+alpha||^-1
 <= j/(j-1) * [v_j 2^(-j/2)/(prod sigma_i)]^(1/j)
 = 2^(-1/2) * j/(j-1) * v_j^(1/j)/(prod sigma_i)^(1/j)`.       (A.6)

The event `2BY+alpha=0` has probability zero because the `j`-dimensional projected vector in (A.4) is absolutely continuous. Averaging the conditional density bound (A.2), the factors `sqrt(2)` and `2^(-1/2)` cancel, giving (A.1).

Equivalently, one can state the proof at the small-ball level and then use absolute continuity. This avoids any concern about the null exceptional fiber.

### Relation to Banks et al.

Banks et al. Corollary 2.4 already proves the same **geometric-mean singular-value mechanism** for scalar bilinear-plus-affine forms, with a universal constant inherited from their projection theorem. Formula (A.1) is an explicit cap-one refinement obtained by inserting the sharp one-dimensional Rudelson--Vershynin constant, the sharp product-marginal cap of Livshyts--Paouris--Pivovarov, and the exact radial bathtub integral. I do not claim qualitative novelty for Theorem A.

For `j=2`, (A.1) becomes

`||p_q||_infinity <= 2 sqrt(pi) / sqrt(sigma_1 sigma_2)`,       (A.7)

exactly matching the already-used top-two cross certificate in the fleet.

## Corollary B — arbitrary ambient coefficients after original-coordinate conditioning

Let `A` be any real symmetric matrix, and suppose there are disjoint sets of ORIGINAL coordinates `I,J` such that

`A_II=0`, `A_JJ=0`, `B=A_IJ`, `rank B=r>=2`.

No restriction is placed on the complement block or on couplings between `I union J` and the complement. Condition only on the complementary ORIGINAL coordinates. The retained conditional polynomial has exactly the form in Theorem A, with affine coefficients depending on the conditioned values. Because (A.1) is uniform in all affine coefficients, averaging gives

`||p_{X^T A X}||_infinity
 <= min_{2<=j<=r} j/(j-1) * v_j^(1/j)/(prod_{i=1}^j sigma_i(B))^(1/j).`       (B.1)

This is a source-valid ambient implication. It does not assert that the bare hypothesis `s_3(A)>=1` forces such an original-coordinate zero-self packet.

## Diffuse cross regularizer

Take

`B_r = r^(-1/2) I_r`, `r>=2`.

Choosing `j=r` in (B.1) gives

`C_r := r/(r-1) v_r^(1/r) sqrt(r)`.       (C.1)

Using the standard lower bound `Gamma(x+1)>=(x/e)^x` for `x>=1`,

`v_r^(1/r) <= sqrt(2 pi e/r)`,

and hence

`C_r <= [r/(r-1)] sqrt(2 pi e) <= 2 sqrt(2 pi e) < 8.266`.       (C.2)

Thus an arbitrarily high-rank bipartite cross packet can have every individual singular value `r^-1/2 ->0` while still regularizing at a universal scale after the singular-volume is aggregated before inversion.

Exact sample values from the deterministic check are

`C_2=5.013256549262001`, `C_3=4.188077948623138`, `C_4=3.974533571810907`.

## Exact owner-target family and completed partner application

For every integer `r>=2`, take mutually independent cap-one scalar sources

`U_+, U_-, X_1,...,X_r, Y_1,...,Y_r, Z`

and define

`Q_r = U_+^2 - U_-^2 + (2/sqrt(r)) sum_{i=1}^r X_i Y_i + sqrt(r) Z^2`.       (D.1)

The symmetric physical matrix has exact spectrum

`{+1,-1,sqrt(r)} union {+r^(-1/2),-r^(-1/2)}^r`.       (D.2)

Therefore, for every `r>=2`, it has **exactly three** eigenvalues of modulus at least one. This is a literal owner-target family.

Theorem A applied to the cross bank in (D.1), followed by convolution with the independent remaining terms, gives

`||p_{Q_r}||_infinity <= C_r`.       (D.3)

This already yields a dimension-free bound by (C.2).

Now apply the latest **completed** account02/B18 theorem available at publication time, `QFORM-HS-MOVING-DIFFUSE-SQUARE-v1`, canonical scientific commit

`fd7c768025320fbb5e54e13a1acd00d329e8f8dd`.

That theorem states for disjoint original product banks

`T=X^T M Y + a(beta^T Z+H(Y))^2+c`

that, with `K_beta=||p_{beta^T Z}||_infinity`,

`||p_T||_infinity <= K_beta/sqrt(|a|) * min{K_HP/sqrt(||M||_HS), 8/sqrt(||M||_op)}`,

and gives a continuous `C_0` density.

In (D.1) take

`M=(2/sqrt(r)) I_r`, `a=sqrt(r)`, `beta=1`, `H=0`.

Because `Z` is one literal original coordinate, `K_beta<=1`. Also

`||M||_HS=2`, `||M||_op=2/sqrt(r)`.

Therefore the operator branch gives the **actual partner inequality**

`||p_{ (2/sqrt(r)) sum X_iY_i + sqrt(r)Z^2 }||_infinity
 <= [1/r^(1/4)] * 8/[sqrt(2) r^(-1/4)]
 = 4 sqrt(2).`       (D.4)

The partner theorem also gives a `C_0` density for this component. Convolution with the independent probability law of `U_+^2-U_-^2` preserves both the `L^infinity` bound and `C_0`: uniform continuity of a `C_0` function gives continuity after convolution with a finite measure, and tightness plus vanishing at infinity gives the `C_0` tail.

Consequently

`Q_r has a C_0 density and
 ||p_{Q_r}||_infinity <= min{C_r,4 sqrt(2)} <= 4 sqrt(2)`       (D.5)

for every `r>=2` and every admissible product input law.

This explicitly applies the designated completed partner result to an owner-target inequality and tracks continuity separately from Theorem A.

## What this closes and what remains

Closed here: a source-valid, all-rank, original-coordinate zero-self bipartite packet, including high-rank diffuse crossings whose individual singular values vanish; plus a concrete exact-three-large-eigenvalue family with a universal `C_0` density bound `4 sqrt(2)` using the designated partner theorem.

Still open: the bare spectral assumption `s_3(A)>=1` does **not** presently force a zero-self bipartite original-coordinate packet with a uniformly payable singular-volume currency. Existing live corrections already refute several naive local-minor and single-Schur extraction statements. The unresolved step is structural: compile every arbitrary symmetric three-large-eigenvalue matrix into one of the paid product-preserving packets (cross-volume, private-square/HS, grouped-hub, ridge, physical-pair, etc.) without deleting small nonzero curvature/cross tails.

Full unrestricted QFORM remains OPEN; unrestricted continuity remains OPEN.

## Deterministic check summary

For `r=2,3,10`, direct eigensolver checks of the matrix in (D.1) reproduce (D.2). The exact constants in (C.1) were evaluated numerically; the check bundle records them. These computations verify formulas only; the proof above is analytic.

## Corrections consumed

The argument preserves at least the following live corrections: law-uniform pointwise quadratic oscillatory decay is false; arbitrary-joint rank-three coarea is false; positive conditional projection-density moments are false; projected coordinates are not independent after rotation; a conditional density cap is not independence; fiber-sup arguments can lose dimension; single-Schur rank-two extraction and local cross-rank-three dichotomies are false; a fixed good minor is not guaranteed; small nonzero tails are not discarded.
