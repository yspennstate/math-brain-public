SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T17:14:30Z.
attacking: the exact-zero-edge endpoint inside the heavy null-hub branch left by account04/B18 r4; transfer the primary product-marginal theorem into a conditional linear-plus-square smoother, then splice with the partner's moderate-edge pair-log estimate.

# account03/B18 r31 — zero-edge linear-square averaging closes the exact endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** literature-to-proof transfer  
**Status:** `NEW SUPPORTING FULL-MATRIX THEOREM + EXACT NULL-HUB ENDPOINT CLOSED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved for the new theorem and its exact-zero-edge null-hub corollary; still open for the unrestricted target.

## 1. Control, live gap, and sources

Fresh owner control remains QFORM-only. The full conjecture remains OPEN: for independent real original-coordinate inputs with one-dimensional densities bounded by one and an arbitrary symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal finite output-density bound, or give a valid target counterexample.

This proof respects the live correction boundary. It uses no independence after spectral rotation, no arbitrary-joint coarea theorem, no conditional-density-as-independence substitution, no positive moment of a worst conditional projection cap, no law-uniform pointwise quadratic-phase decay, no fixed-good-minor extraction, and no deletion of a small random quadratic term.

### Primary literature input

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949. For a product probability density with every one-dimensional factor bounded by one, every k-dimensional orthogonal marginal has density at most `2^(k/2)`. I use only k=1. No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, symmetry, centering, or smoothness assumption is added.

### Designated partner actually applied

Latest compatible account04/B18 result, corrected immutable report commit:

`yspennstate/math-open-problems@3460488b1a730f54dbac848cddc3e2761d3f348e`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260923T162049Z-account04-B18-QFORM-r4/REPORT.md`.

In the target-normalized exact-rank-three null-hub N3(1/64) branch, if a heavy witness `q_i>1/2` has `|g_i|>=1/64`, that report proves

`||p_Q||_infinity < 64.1795826152`.                                (1.1)

It explicitly leaves the tiny-edge branch `|g_i|<1/64`, including the singular endpoint `g_i=0`. The present run closes that exact endpoint.

The structural identities used to identify the endpoint are source-pinned in account01/B18:

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260923T145330Z-account01-B18-qform-auto11-r34/REPORT.md`.

In its null-hub normal form,

`Q = 2 (X_0 + ell.X_L)(g.X_L) + d (beta.X_L)^2`,                  (1.2)

with `||beta||_2=1`, `beta.g=0`, `gamma=||g||_2>0`, and

`|d| gamma^2 = h D`,                                               (1.3)

where `h` is the hub spectral leverage and `D=|pdet A|` for the exact-rank-three matrix. The heavy score is

`q_i=beta_i^2+g_i^2/gamma^2`.                                      (1.4)

## 2. Main theorem: a full-matrix zero-edge receiver

The null-hub application is a corollary of a more general original-coordinate theorem.

### Theorem 2.1 — `QFORM-ZEROPIVOT-ZEROEDGE-LINEAR-SQUARE-v1`

Let `U,V,Z_1,...,Z_m` be mutually independent real random variables, every one-dimensional density bounded by one. Let `g in R^m`, `gamma=||g||_2>0`, let `a!=0`, `eta in R`, and let `B(Z),C(Z)` be arbitrary real measurable functions. Put

`T = 2 U ( <g,Z> + eta ) + a V^2 + B(Z)V + C(Z)`.                 (2.1)

Then `T` has a continuous density vanishing at infinity and

`boxed:
 ||p_T||_infinity <= 6 e^(-1/3) ( |a| gamma^2 )^(-1/3).`          (2.2)

Equivalently, for an arbitrary real symmetric physical matrix and arbitrary affine term, if two distinct original coordinates `u,v` obey

`A_uu=0`, `A_uv=0`, `A_vv=a!=0`,                                  (2.3)

and

`gamma^2 = sum_{j notin {u,v}} A_uj^2 >0`,                        (2.4)

then the full quadratic-plus-affine form has a continuous `C_0` density satisfying (2.2), regardless of every other coefficient of the matrix and regardless of dimension.

This is not a rank-three theorem: all residual self-curvature, all residual cross-couplings, and all couplings of `v` to the rest are absorbed in `B(Z),C(Z)`.

### 2.1 The projected hub coefficient has an exact source-valid density cap

Set

`H=<g,Z>+eta`.                                                      (2.5)

Normalize `g/gamma`. By the k=1 Livshyts--Paouris--Pivovarov theorem,

`||p_H||_infinity <= M := sqrt(2)/gamma`.                          (2.6)

If the active source bank contains only one nonzero coefficient, the elementary scaled-coordinate cap is at most `1/gamma`, so (2.6) remains valid. Translation by `eta` does not change the cap.

No independence between projected spectral coordinates is asserted: `H` is one scalar marginal of the original product source.

### 2.2 Conditional linear-plus-square smoothing

Fix `Z=z` and write `h=H(z)`. The event `h=0` has probability zero because `H` has a density, so take `h!=0`. The two active original coordinates remain genuinely independent and cap one. Up to an irrelevant output translation, the conditional random variable is

`T_z = 2 h U + a V^2 + b V`,                                      (2.7)

where `b=B(z)` is arbitrary.

Let `Y=aV^2+bV`. Completing the square and using the two inverse branches gives, for a.e. `y` on the appropriate one-sided support,

`p_Y(y) <= [ |a| |y-y_0| ]^(-1/2)`,                               (2.8)

where `y_0=-b^2/(4a)` is the quadratic critical value. This envelope is uniform in `b`.

The density `k_h` of `2hU` satisfies

`||k_h||_infinity <= 1/(2|h|)`, `||k_h||_1=1`.                    (2.9)

Since the conditional density is the convolution `k_h*p_Y`, Young immediately gives

`||p_{T_z}||_infinity <= 1/(2|h|)`.                               (2.10)

For the second estimate, substitute the one-sided coordinate `x=|y-y_0|`. On that half-line the function `x^(-1/2)` is decreasing. Among nonnegative functions of mass at most one capped by

`m_h=1/(2|h|)`,                                                     (2.11)

the integral against `x^(-1/2)` is maximized by height `m_h` on `[0,1/m_h]`. Hence

`int_0^infinity x^(-1/2) q(x) dx <= 2 sqrt(m_h)`                  (2.12)

for every such `q`. Combining (2.8)--(2.12),

`||p_{T_z}||_infinity
 <= sqrt(2) |a|^(-1/2) |h|^(-1/2)`.                               (2.13)

Therefore, with

`F(r)=min( (2r)^(-1), sqrt(2)|a|^(-1/2) r^(-1/2) )`,              (2.14)

we have the pointwise conditional certificate

`||p_{T|Z=z}||_infinity <= F(|H(z)|)`.                             (2.15)

This is a real conditional-density statement followed by averaging; it is not a claim that a conditional cap creates independence.

### 2.3 Exact bathtub integration over the projected coefficient

The function `F(|x|)` is even and decreasing in `|x|`. For every probability density capped by `M`, the bathtub principle therefore yields

`E F(|H|) <= 2M int_0^L F(r) dr`, `L=1/(2M)`.                     (2.16)

The two terms in (2.14) cross exactly at

`r_0=|a|/8`.                                                       (2.17)

If `L<=r_0`, equivalently `|a|M>=4`, direct integration gives

`E F(|H|) <= 4 sqrt(M/|a|)`.                                      (2.18)

If `L>r_0`, equivalently `|a|M<4`, then

`E F(|H|)
 <= M [ 2 + log(4/(|a|M)) ]`.                                     (2.19)

There is no support assumption in (2.16); only the density cap and total mass one are used.

### 2.4 Optimize exactly in the LPP scale

Put

`A_*=|a| gamma^2`.                                                 (2.20)

Use the source-valid cap `M=sqrt(2)/gamma` from (2.6).

In the first regime, the constraint `|a|M>=4` is

`gamma^3 <= A_*/(2sqrt(2))`;                                      (2.21)

substitution into (2.18) gives

`E F(|H|) <=4 A_*^(-1/3)`.                                        (2.22)

In the second regime define

`z=gamma^3/(sqrt(2) A_*) >1/4`.                                   (2.23)

Then (2.19) becomes

`E F(|H|)
 <=2^(1/3) A_*^(-1/3) z^(-1/3) [2+log(4z)].`                      (2.24)

The scalar function on the right is maximized at

`z=e/4`,                                                           (2.25)

where its dimensionless factor is

`2^(1/3) * 3(4/e)^(1/3)=6e^(-1/3)`.                              (2.26)

Since `6e^(-1/3)>4`, equations (2.22) and (2.24)--(2.26) prove (2.2).

### 2.5 Existence, continuity, and vanishing at infinity

For every `z` with `H(z)!=0`, the conditional density in (2.7) is a convolution of two `L^1` densities and therefore belongs to `C_0(R)`. Equation (2.15), together with (2.16)--(2.26), supplies an integrable dominating function of `z`. Hence

`p_T(t)=E[p_{T|Z}(t)]`                                             (2.27)

is a probability density; dominated convergence gives continuity and `p_T(t)->0` as `|t|->infinity`. This proves the theorem.

## 3. Exact-zero-edge null-hub endpoint

Return to (1.2). Fix a heavy anchor `i` and suppose

`g_i=0`.                                                           (3.1)

Then (1.4) reduces to

`q_i=beta_i^2`.                                                     (3.2)

Take

`U=X_0`, `V=X_i`, `Z=X_{L\{i}}`.                                  (3.3)

Because `g_i=0`, the hub-to-anchor physical edge vanishes exactly. Expanding (1.2) shows that the coefficient of `V^2` is

`a=d beta_i^2`,                                                    (3.4)

while every other term involving `V` is linear in `V` with a coefficient depending only on `Z`, and every remaining term is a function only of `Z`. The hub coefficient is `2(g_-.Z)U`, and

`||g_-||_2=gamma`.                                                  (3.5)

Arbitrary affine terms are harmless: an affine term in `U` merely translates `g_-.Z` by a constant, an affine term in `V` is absorbed into `B(Z)`, and all other conditioned terms are absorbed into `C(Z)`.

Thus Theorem 2.1 applies and, using (1.3), gives

`boxed:
 ||p_Q||_infinity
 <= 6 e^(-1/3) [ beta_i^2 hD ]^(-1/3).`                           (3.6)

Call this corollary `QFORM-NULLHUB-HEAVY-ZEROEDGE-v1`.

It proves a continuous `C_0` density.

### Target-normalized compiler constant

In the live exact-rank-three compiler with shear `r>=1/2`,

`h=r^2/(1+r^2)>=1/5`, `D>=1`.                                     (3.7)

A heavy zero-edge witness has

`beta_i^2=q_i>1/2`.                                                 (3.8)

Hence

`beta_i^2 hD>1/10`,                                                (3.9)

and (3.6) yields the explicit universal bound

`boxed:
 ||p_Q||_infinity
 < 6 (10/e)^(1/3)
 = 9.262319471965087... .`                                        (3.10)

No N3 small-diagonal assumption is needed for (3.6) or (3.10); exact zero hub-edge plus the null-hub determinant currency suffices.

## 4. Actual splice with designated partner account04/B18

Account04/B18 r4 proves, in the same target-normalized null-hub N3(1/64) state,

`q_i>1/2`, `|g_i|>=1/64`
`=> ||p_Q||_infinity <64.1795826152`.                              (4.1)

The present theorem proves

`q_i>1/2`, `g_i=0`
`=> ||p_Q||_infinity <9.262319472`,                                (4.2)

with continuity.

Therefore the combined source-valid heavy-witness payment is

`q_i>1/2`, `g_i in {0} union {x:|x|>=1/64}`
`=> ||p_Q||_infinity <64.18`.                                     (4.3)

This is the requested application of the completed designated-partner result to an actual inequality. Together with the previously completed diffuse branch `max_j q_j<=1/2`, the only heavy-witness state still unpaid by these mechanisms is now the genuinely punctured interval

`boxed: 0<|g_i|<1/64`.                                             (4.4)

The exact singular endpoint is no longer part of that debt.

## 5. Why this does not violate the live corrections

1. The only projected random variable is the scalar `H=<g,Z>+eta`; its density cap comes directly from the primary product-marginal theorem. No rotated coordinates are declared independent.
2. The independent variables used in conditional smoothing are the two original coordinates `U,V`.
3. The square coefficient is not replaced by a nearby coefficient and no small edge is deleted. The theorem is specifically an exact-zero-edge theorem.
4. No arbitrary joint-density coarea estimate is used.
5. No conditional density cap is treated as an independence assertion.
6. No pointwise characteristic-function decay is asserted.
7. No individual good principal minor is inferred from aggregate determinant mass.
8. Fragmented and unbounded supports are fully allowed.

## 6. Literature status

The primary LPP theorem matches the only external probabilistic input exactly. A targeted literature check found no source whose stated hypotheses directly solve the full arbitrary non-iid cap-one quadratic-form conjecture. Stronger-looking quadratic-form concentration results generally impose additional moment, subgaussian, Gaussian-functional, log-concave, or convexity hypotheses and therefore were not transferred. This is a hypothesis audit, not a novelty claim from absence.

## 7. Remaining debt

The unrestricted conjecture remains **OPEN / NOT PROVED**, and unrestricted continuity remains open.

Locally, the account04/B18 null-hub heavy branch has been reduced from `|g_i|<1/64` to the genuinely punctured collar

`0<|g_i|<1/64`.                                                     (7.1)

At nonzero `g_i`, the active conditional two-coordinate form contains the hyperbolic term `2g_i X_0X_i`; the clean convolution used in Theorem 2.1 is no longer available. The partner pair-log theorem pays that term with a physical-pair singular-value cost, but that cost degenerates as `g_i->0`. The next useful mechanism should interpolate the zero-edge linear-square average proved here with the nonzero pair-log envelope without treating `2g_iX_0X_i` as a small random perturbation. The newest projected-crossing theorem may help only when its explicit rank/volume/marginal gates can be verified; those gates are not automatic in this punctured collar.

Arbitrary additional spectrum and the global product-preserving compiler remain separate full-target debts.

## 8. Deterministic checks

The sibling `CHECK.json` records: exact symbolic expansion of the null-hub endpoint into (2.1); the crossover `r_0=|a|/8`; the two bathtub integrals; the optimizer `z=e/4`; the constant `6e^(-1/3)`; the target constant `6(10/e)^(1/3)=9.262319471965087...`; and the partner splice threshold. These are regression checks only; the proof is the analytic derivation above.
