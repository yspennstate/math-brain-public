# account03/B18 QFORM r14 — zero-Schur-row fractional trace from source-valid projection anticoncentration

**Run:** `20260922T170831Z-account03-B18-QFORM-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** revision `2026-09-22.8`; proof-first continuation `QFORM-PROOF-FIRST-20260922T161801Z`  
**Assignment:** literature-to-proof transfer  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED

## 1. Target and mechanism change

The target is the unrestricted statement: for every dimension, every independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a dimension- and law-independent `L^infinity` density bound for `X^T A X`, or produce a genuine counterexample.

This run changes mechanism from the preceding B18 cross-block/group-selection sequence. The new mechanism is a **translation-uniform fractional trace through an exactly isotropic Schur row**. It directly pays a zero physical Schur pivot with a half-negative moment rather than selecting a uniformly good minor. It uses the completed account04/B18 dependence-safe square-smoothing lemma on an actual conditional residual and then pays the remaining `|L|^{-1/2}` singularity using a primary product-marginal theorem.

## 2. Primary-source hypothesis audit

### 2.1 Livshyts–Paouris–Pivovarov transfers exactly

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949v2, Theorem 1.1 and the preceding one-dimensional Rogozin–Ball discussion.

For a product probability density `f(x)=prod_i f_i(x_i)` with `||f_i||_infinity <= 1`, every one-dimensional orthogonal marginal has density at most `sqrt(2)`. Therefore, for any nonzero coefficient vector `ell`,

`L = ell^T Y + beta`

has

`||p_L||_infinity <= sqrt(2)/||ell||_2`,

uniformly in a deterministic translation `beta`. No moment, centering, identical-law, Gaussian, log-concavity, compact-support, connected-support, or smoothness assumption is used. If only one coefficient is nonzero, the elementary scaling bound `||p_L||_infinity <= 1/||ell||_2` is even sharper, so the displayed `sqrt(2)` statement remains valid in that boundary case.

### 2.2 Banks–Garza Vargas–Kulkarni–Srivastava does not directly close this branch

Primary source checked: J. Banks, J. Garza Vargas, A. Kulkarni, N. Srivastava, arXiv:2005.08930, Section 2, Theorem 2.1 (`Density of Quadratic Forms`). Its theorem concerns

`q(X,Y)=X^T Z Y + X^T U + V^T Y + W`

for two independent random arrays with entry densities bounded by `K`. For scalar output (`k=1`) its stated non-Gaussian estimate has content only when `rank(Z)>3` and depends quantitatively on a singular value `sigma_j(Z)`. Thus it is a genuine bounded-density theorem under bounded-density inputs, but it does **not** justify replacing the current arbitrary same-side quadratic remainder by a rank-three bilinear form, nor does it yield a universal three-eigenvalue theorem. I do not transfer it beyond its hypotheses.

## 3. Partner theorem consumed exactly

Completed compatible partner: account04/B18, canonical scientific commit

`441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Its Lemma `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` states:

> If `R` has density at most `M`, and conditional on `R=r` a square variable `V_r` has density at most one (no independence required), then for `a != 0`, `R+a V_r^2` has density at most `2 sqrt(M/|a|)`.

This run applies that lemma conditionally with the exact value

`M(y)=1/(2 |L(y)|)`.

The dependence-safe part is essential: after a physical square completion, the shifted square coordinate depends on the linear coordinate being smoothed.

## 4. New analytic lemma: linear coefficient plus a dependent translated square

### Lemma 4.1 — `QFORM-LINEAR-COEFFICIENT-SQUARE-v1`

Let `G` be a sigma-field. Let `V` and `X` be original independent coordinates, each with density at most one and independent of `G`. Let `L,R,c,d` be `G`-measurable real quantities with `L` finite. Fix `a != 0` and set

`T = R + 2 L V + a (X + c V + d)^2`.

Assume the marginal law of `L` has a density bounded by `M_L < infinity`. Then `T` is absolutely continuous and

`boxed( ||p_T||_infinity <= 4 sqrt(M_L/|a|) ).`

No independence between `L` and `R` is assumed.

#### Proof

Fix `G=g` and write `l=L(g)`, `r=R(g)`, `c=c(g)`, `d=d(g)`. For `l != 0`, the residual

`R_0 = r + 2 l V`

has density at most

`M(g)=1/(2|l|)`.

Conditioning further on `R_0` fixes `V` because `v -> r+2lv` is injective. Hence

`X+cV+d`

conditional on `R_0` is a translate of the original `X`, and its density is still at most one. Applying the account04/B18 square-smoothing lemma gives

`||p_{T | G=g}||_infinity <= 2 sqrt( 1/(2 |a| |l|) ) = sqrt(2)/sqrt(|a l|).`  (4.1)

Because `L` has an absolutely continuous law, `P(L=0)=0`. Mixing the conditional densities yields

`||p_T||_infinity <= sqrt(2/|a|) E |L|^{-1/2}.`  (4.2)

It remains to pay the half-negative moment. If a real random variable `Z` has density at most `M`, then uniformly in every translation `u`,

`P(|Z-u|<r) <= min(1,2Mr)`.

By layer cake,

`E |Z-u|^{-1/2}
 = integral_0^infinity P(|Z-u| < t^{-2}) dt
 <= integral_0^{sqrt(2M)} 1 dt
    + integral_{sqrt(2M)}^infinity 2M t^{-2} dt
 = 2 sqrt(2M).`  (4.3)

Apply (4.3) to `L` with `u=0`. Combining with (4.2) gives

`||p_T||_infinity <= sqrt(2/|a|) * 2 sqrt(2 M_L)
 = 4 sqrt(M_L/|a|).`

This also constructs an `L^infinity` density by mixing the conditional densities. QED.

**Continuity:** not claimed. The partner lemma proves absolute continuity and an essential-supremum bound, but arbitrary bounded input densities plus the dependence created by the random translation are not promoted here to a continuous representative without an additional argument.

## 5. New physical theorem: an exactly isotropic Schur row is paid in every ambient dimension

### Theorem 5.1 — `QFORM-ZERO-SCHUR-ROW-FRACTIONAL-TRACE-v1`

Select original-coordinate indices

`I = {j,i} union K`

with `K` nonempty, and condition on all coordinates outside `I`. Write the selected quadratic principal block with `j` first as

`B = [[a, b^T], [b, C]]`,   `a != 0`,

and let

`S = C - b b^T/a`

be its physical Schur complement on `{i} union K`. Suppose

`S_ii = 0`

and define the transverse Schur-row norm

`s = ( sum_{k in K} S_ik^2 )^(1/2) > 0`.

Then for the **full ambient quadratic form**, with all coefficients involving coordinates outside `I` completely arbitrary,

`boxed( ||p_{X^T A X}||_infinity <= 2^(9/4) / sqrt(|a| s) ).`  (5.1)

This theorem uses no spectral-sign assumption and no restriction on the remaining quadratic block. Consequently, whenever the owner's three-large-eigenvalue target matrix contains such a selected block with `|a| s >= eta`, that entire target instance is paid by the universal-in-dimension constant `2^(9/4)/sqrt(eta)`.

#### Proof

Condition on all outside coordinates `O`. They create only affine and constant terms in the selected variables. Write `z=(x_i,y)` for the selected variables after `j`. Completing the square only in `x_j` gives

`Q_O = a (x_j + a^{-1} b^T z + gamma_O)^2
      + z^T S z + 2 d_O^T z + c_O`.

Since `S_ii=0`, the second line is affine in `x_i`:

`z^T S z + 2 d_O^T z + c_O
 = R_O(y) + 2 x_i ( ell^T y + beta_O),`

where

`ell=(S_ik)_{k in K}`,  `||ell||_2=s`.

For each fixed outside value `O`, the selected `Y=(X_k)_{k in K}` still has its original product density with coordinate caps one. By the Livshyts–Paouris–Pivovarov one-dimensional marginal theorem,

`||p_{ell^T Y + beta_O}||_infinity <= sqrt(2)/s`,  (5.2)

uniformly in the translation `beta_O`.

Now take `G=sigma(O,Y)` in Lemma 4.1, `V=X_i`, and

`X + cV+d = X_j + a^{-1} b_i X_i + a^{-1} b_K^T Y + gamma_O`.

The dependence of this shifted square on `X_i` is permitted by the partner theorem and was the reason for using its conditional formulation. Equations (5.2) and Lemma 4.1 imply, uniformly in `O`,

`||p_{Q | O}||_infinity
 <= 4 sqrt( (sqrt(2)/s)/|a| )
 = 2^(9/4)/sqrt(|a|s).`

Averaging over `O` preserves the same bound. QED.

### Sharper single-transverse-coordinate endpoint

If `K` consists of one coordinate, then the affine coefficient has density at most `1/s` by direct scaling, so the same proof improves (5.1) to

`boxed( ||p_Q||_infinity <= 4/sqrt(|a|s) ).`  (5.3)

Thus an indefinite `2 x 2` Schur block of the form `[[0,s],[s,d]]` is uniformly paid once it arises after a nonzero physical pivot; arbitrary outside couplings remain allowed.

## 6. Exact fully coupled target example

Let

`S = 2 * [[0,1,0],[1,0,0],[0,0,1]]`,

`a=2`, and `b=(1/10,1/10,1/10)^T`. Define the full four-dimensional matrix

`A = [[a,b^T],[b,S + b b^T/a]].`

Then the Schur complement at the first coordinate is exactly `S`. Taking `i` to be the first Schur coordinate and `K` the other two gives

`S_ii=0`, `s=2`, `|a|s=4`.

Therefore Theorem 5.1 gives

`||p_{X^T A X}||_infinity <= 2^(5/4) = 2.3784142300...`  (6.1)

for every admissible independent cap-one product input.

This is a genuine target matrix. The unperturbed `diag(2,S)` has eigenvalues `2,2,2,-2`. The perturbation

`E=[[0,b^T],[b,b b^T/2]]`

has operator norm at most

`2||b||_2 + ||b||_2^2/2
 = sqrt(3)/5 + 3/200 < 0.362`.

Weyl therefore places every eigenvalue of `A` outside `(-1.638,1.638)`, so in particular at least three eigenvalues have modulus at least one. All three pivot couplings `b_k` are nonzero. No diagonalization of the input law is used.

## 7. Relation to current corrections

This theorem does **not** assert that three large eigenvalues force one good physical minor, one good triple, or one zero Schur row. Those extraction claims are already refuted by current exact families. It also does not use the false law-uniform pointwise van-der-Corput/Fresnel decay, conditional-cap-as-independence, fiberwise trace supremum, or universal cross-minor routes.

The dependence issue is handled at the exact place where it occurs: after square completion the shifted `X_j` depends on `X_i`, but the completed account04/B18 theorem needs only a conditional density cap. Conditional on the affine residual `2L X_i+R`, `X_i` is fixed whenever `L != 0`, so the shifted square variable is literally a translate of the untouched original `X_j` density.

## 8. What this closes and what remains

**Closed in this run:** the exact zero-Schur-diagonal branch with nonzero transverse Schur-row norm, in arbitrary ambient dimension and with arbitrary outside quadratic/cross coefficients. This is a source-valid answer to part of the live `zero/near-isotropic physical-pivot` priority.

**Still unpaid:** the bare three-large-eigenvalue hypothesis does not currently force a selected block satisfying `|a|s >= eta`, and exact correction families prohibit simply asserting such a fixed-minor extraction. The next target-level implication should be a quantitative **near-isotropic Schur-row** version or an aggregate/grouped-coordinate version: if `|S_ii|` is small rather than zero, retain the same `|L|^{-1/2}` fractional-trace payment while controlling the added `S_ii X_i^2` term, or combine this branch with the ridge-certified diffuse alternative before selecting a single coordinate.

The full universal QFORM conjecture remains **OPEN / NOT PROVED**. Continuity of the full target remains open; this run proves an essentially bounded density, not a continuous representative, in the new branch.

## 9. Source pins

- Livshyts–Paouris–Pivovarov, arXiv:1507.07949v2, Theorem 1.1 / one-dimensional Rogozin–Ball consequence: source-valid linear projection density cap.
- Banks–Garza Vargas–Kulkarni–Srivastava, arXiv:2005.08930, Section 2, Theorem 2.1: audited but not overextended; scalar non-Gaussian statement requires sufficiently high bilinear rank and Q-dependent singular-value control.
- account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`: `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, exact path cited above.
- Current orientation-free rank-two affine half-Riesz supporting theorem remains compatible but is not needed for Theorem 5.1; this run deliberately changed mechanism rather than repeating the preceding cross-block proof.
