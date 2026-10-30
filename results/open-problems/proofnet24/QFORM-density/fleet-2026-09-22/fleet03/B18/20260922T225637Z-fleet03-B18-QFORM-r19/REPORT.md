# fleet03/B18 r19 — independent-two-bank Fresnel transfer for diffuse rank-three curvature

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Target:** independent real coordinates with densities `0<=f_i<=1`; real symmetric `A`; at least three eigenvalues of modulus at least one.  
**Status:** supporting analytic theorem proved below; full conjecture **OPEN / NOT PROVED**.  
**Continuity:** proved for the direct rank-three theorem below; not promoted through the final dependent-square wrapper.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Primary-source hypotheses used

### Livshyts–Paouris–Pivovarov

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1.

For a product probability density `f(x)=prod_i f_i(x_i)` with each one-dimensional density bounded by one, every `k`-dimensional orthogonal marginal has essential supremum at most `2^(k/2)`. No Gaussianity, log-concavity, moment, compact-support, connected-support, symmetry or identical-law hypothesis is present.

I use only `k=3`. If a selected bank has exactly three coordinates, the theorem's proper-marginal formulation is unnecessary: after whitening, the coefficient matrix is an orthogonal `3x3` matrix, so the transformed product density has cap at most one, hence certainly at most `2^(3/2)`.

### Marcus–Spielman–Srivastava

A. Marcus, D. Spielman, N. Srivastava, *Interlacing Families II: Mixed Characteristic Polynomials and the Kadison–Singer Problem*, arXiv:1306.3969, Corollary 1.5.

If vectors `r_i` form a Parseval frame, `sum_i r_i r_i^T=I`, and `||r_i||^2<=delta`, then for every positive integer `r` there is a partition into `r` classes for which every partial frame operator has norm at most `(1/sqrt(r)+sqrt(delta))^2`. I use `r=2`. This source is purely deterministic linear algebra and adds no probabilistic hypothesis.

## 2. New analytic lemma: two independent three-dimensional density blocks

### Theorem A (`QFORM-TWOBLOCK-FRESNEL-v1`)

Let `Y_1,Y_2` be independent random vectors in `R^3` with probability densities `p_1,p_2` satisfying

`||p_1||_infinity <= M_1`,  `||p_2||_infinity <= M_2`.

Let `Lambda` be a real invertible symmetric `3x3` matrix. For arbitrary `h in R^3` and `c in R`, put

`T=(Y_1+Y_2)^T Lambda (Y_1+Y_2)+h^T(Y_1+Y_2)+c`.

Then `T` has a continuous density and

`||p_T||_infinity <= 3 (M_1 M_2)^(1/3) |det Lambda|^(-1/3).`  (A.1)

#### Proof

Write `Y=Y_1+Y_2` and `rho=p_1*p_2`. Use the Fourier convention

`hat f(xi)=int exp(i xi.y) f(y) dy`.

Since `p_j` is a probability density bounded by `M_j`,

`||p_j||_2^2 <= M_j`.

Plancherel gives

`||hat p_j||_2 <= (2pi)^(3/2) M_j^(1/2)`.

Independence gives `hat rho=hat p_1 hat p_2`; therefore Cauchy–Schwarz yields the crucial product-preserving estimate

`||hat rho||_1 <= (2pi)^3 (M_1 M_2)^(1/2)`.  (A.2)

Complete the square in the affine term. Translation of `rho` multiplies its Fourier transform by a modulus-one phase, so (A.2) is unchanged. It is therefore enough to treat `T=Y^T Lambda Y`.

Because `hat rho in L^1`, Fourier inversion is available. For `t!=0`, insert it into

`phi_T(t)=int exp(i t y^T Lambda y) rho(y) dy`.

To justify the Fresnel interchange without any smoothness or support assumption, first insert `exp(-epsilon |y|^2)`, `epsilon>0`. The inner Gaussian integral factors after orthogonally diagonalizing `Lambda`, and its absolute value is bounded uniformly in `epsilon` by

`pi^(3/2) |t|^(-3/2) |det Lambda|^(-1/2)`.

Dominated convergence in `xi`, using (A.2), then gives the exact Fresnel bound

`|phi_T(t)| <= pi^(3/2) (M_1 M_2)^(1/2) |det Lambda|^(-1/2) |t|^(-3/2).`  (A.3)

Indeed the factor `(2pi)^(-3)` from Fourier inversion cancels the `(2pi)^3` in (A.2). Set

`D=pi^(3/2)(M_1M_2)^(1/2)|det Lambda|^(-1/2)`.

Together with `|phi_T(t)|<=1`, (A.3) gives

`|phi_T(t)| <= min(1,D |t|^(-3/2))`.

The integral is exact:

`int_R min(1,D|t|^(-3/2)) dt = 6 D^(2/3)`.

Thus `phi_T in L^1`; Fourier inversion for the law of `T` supplies a continuous density and

`||p_T||_infinity <= (1/(2pi)) 6D^(2/3)
 =3(M_1M_2)^(1/3)|det Lambda|^(-1/3)`.

This proves (A.1). Notice that no pointwise one-dimensional van-der-Corput bound is used; the smoothing comes from convolving two genuinely independent three-dimensional product-derived blocks **before** the quadratic Fresnel transform.

## 3. Literature-to-proof transfer: diffuse exact-rank-three forms

### Theorem B (`QFORM-MSS-LPP-TWOBLOCK-RANK3-v1`)

Let `X_1,...,X_n` be independent with densities bounded by one. Let

`A=U Lambda U^T`,  `U^T U=I_3`,

where `Lambda` is invertible symmetric `3x3`; thus `A` has exact rank three. Write the physical row vectors of `U` as `r_i in R^3` and assume

`max_i ||r_i||^2 <= delta < (1-1/sqrt(2))^2`.

Define

`eta = 1-(1/sqrt(2)+sqrt(delta))^2 >0`.

Then `Q=X^T A X` has a continuous density satisfying

`||p_Q||_infinity <= 6 eta^(-1) |det Lambda|^(-1/3).`  (B.1)

In particular, if `delta<=1/32`, then `eta>=7/32` and

`||p_Q||_infinity <= (192/7) |det Lambda|^(-1/3).`  (B.2)

If additionally all three nonzero eigenvalues have modulus at least `s`, then

`||p_Q||_infinity <= 192/(7s)` for `delta<=1/32`.  (B.3)

#### Proof

The rows satisfy the Parseval identity `sum_i r_i r_i^T=I_3`. Apply MSS Corollary 1.5 with `r=2`. It partitions the original coordinate indices into disjoint sets `I,J` such that, with

`G_I=sum_{i in I} r_i r_i^T`, `G_J=sum_{j in J} r_j r_j^T`,

both `G_I` and `G_J` are at most

`alpha I_3`,  `alpha=(1/sqrt(2)+sqrt(delta))^2`.

Since `G_I+G_J=I_3`, the same two upper bounds imply

`G_I >= eta I_3`,  `G_J >= eta I_3`, `eta=1-alpha`.

Define the two independent physical-bank aggregates

`Y_I=sum_{i in I} r_i X_i`, `Y_J=sum_{j in J} r_j X_j`.

For each bank `B in {I,J}`, whiten by `G_B^(-1/2)`. The coefficient vectors `G_B^(-1/2)r_i` form a Parseval frame in `R^3`; hence this whitened aggregate is a three-dimensional orthogonal marginal of that bank's original product measure. LPP therefore gives density cap `2^(3/2)` (and, as noted above, the exactly-three-coordinate boundary case is even easier). Undoing the whitening yields

`||p_{Y_B}||_infinity <= 2^(3/2) / sqrt(det G_B)
 <= 2^(3/2) eta^(-3/2) =: M.`  (B.4)

The two aggregates are independent because `I,J` are disjoint sets of the **original independent coordinates**. Also

`U^T X=Y_I+Y_J` and `Q=(Y_I+Y_J)^T Lambda (Y_I+Y_J)`.

Apply Theorem A with `M_1=M_2=M`:

`||p_Q||_infinity <=3 M^(2/3)|det Lambda|^(-1/3)
=6 eta^(-1)|det Lambda|^(-1/3)`.

For `delta=1/32`,

`alpha=(1/sqrt(2)+1/sqrt(32))^2=25/32`, `eta=7/32`,

which gives (B.2). If `|lambda_k|>=s`, then `|det Lambda|>=s^3`, giving (B.3).

### Why this does not use a refuted interface

* It never treats an arbitrary three-dimensional joint density by coarea. The current correction `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1` therefore does not apply.
* It never conditions on an orthogonal spectral complement and never asks for a conditional projection-density moment.
* It never asserts independence after a general rotation. Independence is used only after MSS partitions the **original coordinate set** into `I` and `J`.
* It never invokes law-uniform pointwise one-dimensional quadratic-phase decay.

## 4. Explicit target-normalized stress family

Take 96 original coordinates. For each `k=1,2,3`, assign 32 row vectors equal to `e_k/sqrt(32)`. Then `U^T U=I_3` and every row leverage is exactly `1/32`. For

`Lambda=diag(1,1,-1)`,

the physical matrix `A=U Lambda U^T` has exact nonzero spectrum `{1,1,-1}` and hence matches the owner's three-large-eigenvalue threshold exactly, while every nonzero physical matrix entry has magnitude only `1/32`. Theorem B gives the distribution-free continuous-density bound

`||p_Q||_infinity <=192/7 =27.4285714285...`

for every choice of independent cap-one coordinate laws.

This is deliberately a diffuse check: the result is paid by two high-cardinality independent coordinate banks, not by a fixed favorable physical triple.

## 5. Required partner application: fleet04/B18 dependence-safe square smoothing

The completed fleet04/B18 r1 theorem is pinned at

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Its proved statement used here is: if `R` has density cap `M` and, conditional on `R=r`, a real variable `V` has density cap one (independence is not required), then for `a!=0`,

`||p_{R+aV^2}||_infinity <=2 sqrt(M/|a|)`.  (P)

### Corollary C (`QFORM-DIFFUSE-RANK3-SCHUR-SQUARE-v1`)

Select one original coordinate as a nonzero scalar pivot and write

`A=[[a,b^T],[b,C]]`, `a!=0`, `S=C-bb^T/a`.

Assume the **whole** Schur residual is exact rank three,

`S=U Lambda U^T`, `U^TU=I_3`,

its spectral-frame row leverage obeys `max_i ||r_i||^2<=1/32`, and every nonzero residual eigenvalue has modulus at least `s>0`. Then the full quadratic form has an essentially bounded density with

`||p_{X^TAX}||_infinity
 <= 16 sqrt(3/7) (|a|s)^(-1/2)
 =10.4744587313... (|a|s)^(-1/2).`  (C.1)

#### Proof

Completing the physical square gives

`Q=a(X_0+a^(-1)b^T Y)^2 + Y^T S Y`.

By Theorem B, `R=Y^TSY` has density cap

`M<=192/(7s)`.

Given `R`, the shifted pivot `V=X_0+a^(-1)b^T Y` is a mixture of translations of the original `X_0` density. Because `X_0` is independent of all `Y` and its density is at most one, this conditional mixture has density at most one. This is exactly the dependence-safe hypothesis of (P), so

`||p_Q||_infinity <=2 sqrt((192/(7s))/|a|)
=16 sqrt(3/7)(|a|s)^(-1/2)`.

No conditional independence is asserted. I record only essential boundedness for Corollary C because the partner r1 handoff states the density bound but does not supply a continuity claim for this wrapper.

## 6. What this closes and what remains unpaid

Theorem B gives a short source-valid proof of a **diffuse exact-rank-three** branch with an explicit continuous-density constant. Its mechanism is independent-two-bank convolution plus a three-dimensional Fresnel integral. It is narrower than the already completed spectral-window ridge theorem (which allows small spectral tails), but it provides a clean product-preserving interface with a better explicit constant on exact rank three and avoids the disproved arbitrary-joint coarea route.

Corollary C is an actual application of the designated fleet04/B18 result and closes the corresponding scalar-pivot + diffuse exact-rank-three Schur residual branch.

The full target is still open. The bare condition `s_3(A)>=1` does **not** automatically imply exact rank three, a leverage bound `<=1/32`, or a scalar pivot whose Schur residual has those properties. Existing correction families rule out replacing this by selection of one uniformly favorable fixed physical minor. The remaining high-value implication is therefore an exhaustive product-preserving decomposition that, from `s_3(A)>=1`, either:

1. enters the existing ridge/spectral-window branch;
2. exposes enough independent original-coordinate bank structure to use a two-block Fresnel estimate such as Theorem A; or
3. routes the high-leverage remainder into one of the completed grouped-coordinate / physical-pair / scalar-Schur mechanisms.

No claim of full solution or novelty is made.
