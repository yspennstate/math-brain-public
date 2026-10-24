# account01/B18 — zero-pivot 1+2 product trace closes two canonical rank-three cases

**Run:** `20260922T175509Z-qform-B18-a01-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Classification:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / ESSENTIAL_STEP_APPLIED`  
**Full target:** `OPEN / NOT PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and exact step attacked

The target remains: for every dimension `n`, independent real coordinates `X_i` with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal finite bound. Continuity is tracked separately.

This run uses the completed designated-partner result account02/B18, run `account02-B18-20260922T170013Z-r11`, canonical report

`yspennstate/math-open-problems@7045cf7745ad4f1bb04e5a6e4b3196aeb867a140`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/account02-B18-20260922T170013Z-r11/REPORT.md`.

That report proves the exact zero-pivot rank trichotomy for an exact-rank-three matrix and then compresses the residual physical variables to a two- or three-dimensional orthogonal projection. In the first two cases it leaves precisely a scalar independent input plus a dependent two-dimensional projection. The sharp marginal theorem of Livshyts--Paouris--Pivovarov gives density cap `2` for that two-dimensional projection, but the curved quadratic trace was still unpaid.

The first implication attacked here is therefore the following source-valid statement:

> if `X` is a cap-one scalar independent of a two-dimensional vector `Y` whose *joint* density is bounded by `M`, does every nonsingular zero-pivot quadratic form in `(X,Y)` have bounded density, with a scale-correct bound depending only on `M` and the determinant?

The answer is yes. Importantly, no independence between the two coordinates of `Y` is assumed.

## 2. Primary literature transfer and hypothesis audit

### 2.1 Livshyts--Paouris--Pivovarov

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889; arXiv:1507.07949.

For a product probability density `prod_i f_i(x_i)` with every `||f_i||_infinity<=1`, the density of every `k`-dimensional orthogonal marginal is bounded by `2^(k/2)`. There are no moment, centering, bounded-support, log-concavity, identical-law, or smoothness hypotheses. Hence the two-dimensional projection produced by the designated partner has a genuine joint density cap

`M <= 2`.

This theorem gives a joint cap only; it does not make projected coordinates independent.

### 2.2 Banks--Garza-Vargas--Kulkarni--Srivastava

Primary source checked: J. Banks, J. Garza-Vargas, A. Kulkarni, N. Srivastava, *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations*, arXiv:2005.08930; Ann. Inst. H. Poincare Probab. Statist. 60 (2024), 2736--2766. Their quadratic/bilinear-density estimates exploit two genuinely independent entry families and singular values of the cross matrix.

That source does not directly settle the partner's canonical form because after orthogonal compression the two coordinates of `Y` are generally dependent and the same side carries the self-quadratic term `Y^T B Y`. I therefore do not transfer its bilinear theorem outside its hypotheses. The new argument below uses only the source-valid LPP joint cap together with the genuine scalar-versus-vector independence that survives in original physical coordinates.

No exact prior theorem matching the full arbitrary-matrix target was located in this source check. This is not a novelty claim.

## 3. Main theorem: a zero-pivot 1+2 product trace bound

### Theorem 3.1 — `QFORM-ZEROPIVOT-1PLUS2-DENSITY-v1`

Let `X` be a real random variable with probability density `f` satisfying

`0 <= f <= 1`, `int f = 1`.

Let `Y=(Y_1,Y_2)` be independent of `X` and have an arbitrary joint probability density `g` satisfying

`0 <= g <= M`, `int_R2 g = 1`.

No independence between `Y_1,Y_2` is assumed. Let

`H = [[0, ell^T], [ell, B]]`

be a real symmetric nonsingular `3x3` matrix, where `ell in R^2` and `B` is symmetric. Then

`Q = (X,Y)^T H (X,Y)`

has a continuous density and

`||p_Q||_infinity <= 6 M^(2/3) |det H|^(-1/3)`.      (3.1)

The exponents are scale-correct: multiplying `H` by `c` multiplies the right-hand side by `|c|^(-1)`.

### Proof

Because `H` is nonsingular, `ell != 0`. Rotate only the two-dimensional `Y` coordinates by an orthogonal matrix. This preserves the joint density cap `M`, the determinant, and scalar-vector independence. We may therefore write

`ell=(L,0)`, with `L=||ell||>0`,

and

`B=[[b11,b12],[b12,b22]]`.

Thus, writing `Y=(u,v)`,

`Q = b11 u^2 + 2 b12 u v + b22 v^2 + 2 L X u`.      (3.2)

Expanding the determinant along the first row gives

`det H = -L^2 b22`.      (3.3)

Nonsingularity therefore implies `beta:=b22 !=0`.

Apply the determinant-one shear

`w = v + (b12/beta) u`.

The transformed joint density

`g_tilde(u,w)=g(u,w-(b12/beta)u)`

still satisfies `||g_tilde||_infinity<=M`; its `u`-marginal

`m(u)=int g_tilde(u,w) dw`

has total mass one. Equation (3.2) becomes

`Q = beta w^2 + alpha u^2 + 2 L X u`,      (3.4)

where `alpha=b11-b12^2/beta`.

For almost every `u !=0`, let `h_u(t)` denote the unnormalised output density at level `t` obtained by integrating the joint density `f(x) g_tilde(u,w)` over `(x,w)` under the map in (3.4). We derive two complementary estimates.

#### Estimate A: linearise in the original scalar

For fixed `(u,w)`, (3.4) is affine in `x` with slope `2Lu`. Therefore

`h_u(t)
 = int g_tilde(u,w) f((t-beta w^2-alpha u^2)/(2Lu)) /(2L|u|) dw
 <= m(u)/(2L|u|)`.      (3.5)

This is strong away from `u=0` and, crucially, spends the genuine original scalar-versus-residual independence rather than any invented independence inside `Y`.

#### Estimate B: keep the square singularity and average it against the scalar

For fixed `(x,u)`, the pushforward of the `w`-slice through `beta w^2` has pointwise density at most

`M /(sqrt(|beta|) sqrt(|s|))`      (3.6)

at nonzero compatible `s`: the two roots have total Jacobian exactly `1/(sqrt(|beta|) sqrt(|s|))`.

Hence

`h_u(t)
 <= M/sqrt(|beta|) int f(x) |t-alpha u^2-2Lux|^(-1/2) dx`.      (3.7)

We use the elementary sharp cap-one rearrangement

`sup_{a in R} int f(x)|a-cx|^(-1/2) dx
 <= 2 sqrt(2) |c|^(-1/2)`,      (3.8)

valid for every probability density `0<=f<=1`. Indeed, after factoring `|c|^(-1/2)`, the symmetric decreasing kernel `|x-x0|^(-1/2)` is maximised under the constraints `0<=f<=1`, `int f=1` by the indicator of the unit interval centred at its singularity, and

`int_{-1/2}^{1/2}|x|^(-1/2)dx=2sqrt(2)`.

Putting `c=2Lu` in (3.7)--(3.8) yields

`h_u(t) <= 2M / sqrt(|beta| L) * |u|^(-1/2)`.      (3.9)

This is integrable through the dangerous zero-coupling fiber.

#### Split and optimise

For any `r>0`, integrate (3.9) over `|u|<r` and (3.5) over `|u|>=r`. Since `int m=1`, uniformly in `t`,

`p_Q(t)
 <= 8M sqrt(r)/sqrt(|beta|L) + 1/(2Lr)`.      (3.10)

For `A/r+B sqrt(r)`, the minimiser satisfies `r^(3/2)=2A/B`. Here

`A=1/(2L)`, `B=8M/sqrt(|beta|L)`,

so (3.10) gives

`p_Q(t)
 <= 6 M^(2/3) / (|beta| L^2)^(1/3)`.      (3.11)

Using (3.3), this is exactly (3.1).

#### Continuity

For almost every fixed `u !=0`, the law in (3.4) is the convolution of the `L^1` density of `2LuX` with the `L^1` pushforward density of the `w`-slice under `beta w^2`, followed by a translation by `alpha u^2`. Hence `h_u` is continuous and vanishes at infinity.

For `|u|<1`, (3.9) supplies an integrable `u`-majorant. For `|u|>=1`, (3.5) is bounded by `m(u)/(2L)`, also integrable. Dominated convergence therefore shows that

`p_Q(t)=int h_u(t)du`

is continuous. This proves the theorem. QED.

## 4. Direct application of the designated account02/B18 result

The partner's `QFORM-ZEROPIVOT-RANK-TRICHOTOMY-v1` says that for an exact-rank-three symmetric matrix, after choosing a physical coordinate `i` with `A_ii=0` and writing

`A=[[0,b^T],[b,C]]`,

exactly one of three cases occurs. Its `QFORM-ZEROPIVOT-LPP-COMPRESSION-v1` then sets

`E=Ran(C)+span{b}`

and writes

`X^TAX = Y^T B Y + 2 X_i ell^T Y`,      (4.1)

where `X_i` is genuinely independent of the full vector `Y`, and `Y` is an orthogonal projection of the remaining original product source.

In the partner's first two cases,

1. `rank C=1` and `b_N !=0`, or
2. `rank C=2`, `b_N=0`, and `b^T C^+ b !=0`,

one has `dim E=2`. Thus (4.1) is exactly Theorem 3.1. LPP supplies

`||p_Y||_infinity <= 2`.      (4.2)

Moreover `A` vanishes on the orthogonal complement of `span{e_i} direct_sum E`, so the effective `3x3` matrix `H` in Theorem 3.1 has precisely the three nonzero eigenvalues of `A`. Therefore, under the target normalization `|lambda_j(A)|>=1` for those three eigenvalues,

`|det H| = product_{j=1}^3 |lambda_j(A)| >=1`.      (4.3)

Combining (3.1), (4.2), and (4.3) closes both partner cases with the explicit universal continuous-density estimate

`||p_(X^TAX)||_infinity <= 6 * 2^(2/3)
 = 9.524406311809196...`.      (4.4)

### Corollary 4.1 — `QFORM-ZEROPIVOT-CASES12-CLOSED-v1`

Every target-normalised exact-rank-three matrix possessing a zero physical pivot whose partner trichotomy is in the rank-one-deletion or rank-two-deletion case has a continuous output density bounded by `6*2^(2/3)<9.525` for every independent cap-one input law.

This is a target-level conclusion on those two canonical zero-pivot classes. It uses the actual designated partner result at an inequality, not merely as a citation.

## 5. Why this does not violate the live corrections

The proof never assumes independence after rotation: only the original scalar `X_i` is independent of the entire residual projected vector `Y`. The two coordinates of `Y` may be arbitrarily dependent.

The proof does not use an unrestricted fiber supremum. It alternates two exact source-valid integrations: affine conditioning in the original scalar away from the zero-coupling line and the square Jacobian plus the cap-one scalar rearrangement near that line.

It does not use a fixed good physical minor, a rank-three cross cut, a conditional-density-as-independence substitution, pointwise law-uniform Fresnel decay, or a perturbative operator-norm continuity argument.

The latest correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` is also respected. That correction shows that one square plus one heavy coupling can collapse to one square and remain singular. Here the effective `3x3` matrix is nonsingular, which forces the additional transverse square coefficient `beta` in (3.3) to be nonzero; the determinant identity is exactly the missing third curvature.

## 6. What remains unpaid

The designated partner's third zero-pivot case is not closed by Theorem 3.1:

`rank C=3`, `b in Ran(C)`, and `b^T C^+ b=0`.

Its compressed residual vector is three-dimensional rather than two-dimensional. Algebraically, after completing the border one obtains a rank-three Schur-isotropic form. A bare `L^infinity` cap `||p_Y||_infinity<=2sqrt(2)` is not enough by itself, because the correction archive already rules out replacing product-projection provenance by an arbitrary bounded joint law in indefinite curved traces.

Thus the next exact implication for this route is:

`QFORM-ZEROPIVOT-CASE3-PRODUCT-TRACE-v1`:

> for `X` cap-one and independent of an actual three-dimensional orthogonal projection `Y` of a cap-one product source, bound the density of `Y^T B Y+2X ell^T Y` uniformly in the Schur-isotropic case `B` invertible and `ell^T B^{-1}ell=0`, under target spectral normalisation.

The arbitrary-extra-spectrum problem also remains after all exact-rank-three branches: one still needs the owner's exhaustive product-preserving ridge-or-grouped-coordinate reduction for general `A`.

## 7. Status and source pins

- Full QFORM theorem: **OPEN / NOT PROVED**.
- New theorem `QFORM-ZEROPIVOT-1PLUS2-DENSITY-v1`: **PROVED**.
- New corollary `QFORM-ZEROPIVOT-CASES12-CLOSED-v1`: **PROVED** within the exact-rank-three target scope.
- Continuity: **PROVED for the new branch**, not for the full target.
- Designated partner: account02/B18 `account02-B18-20260922T170013Z-r11`, canonical commit `7045cf7745ad4f1bb04e5a6e4b3196aeb867a140`.
- LPP primary source: arXiv:1507.07949 / Israel J. Math. 216 (2016), 877--889.
- Banks--Garza-Vargas--Kulkarni--Srivastava primary source: arXiv:2005.08930 / Ann. Inst. H. Poincare Probab. Statist. 60 (2024), 2736--2766.
- Fresh control initially bound at `math-research-brain@b7325a4d01f03ddcd0dabbfbbdbecaec8e647a8d`; immediately before scientific publication main was refreshed to `63b776af052f2dfd524f1474959b8a7d7616380d`. Owner control remains QFORM-only; no later stop was observed.
- Relevant live correction closure re-read at the publication refresh; no correction contradicting Theorem 3.1 was present.

No claim of external novelty is made. Repository synchronization is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
