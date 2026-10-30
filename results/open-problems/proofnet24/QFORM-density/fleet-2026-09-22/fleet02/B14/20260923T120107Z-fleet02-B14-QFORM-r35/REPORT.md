SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T12:01:07Z.
attacking: protected-anchor localization and high-leverage Schur curvature—retain one whole physical anchor while localizing every other slope coordinate at zero mass tax, and turn a heavy row of an arbitrary diagonal-plus-rank-two Schur bank into a whole-bank random-slope certificate before reciprocal payment.

# fleet02/B14 r35 — protected-anchor localization and high-leverage rank-two Schur slope

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control revision consumed: `2026-09-22.15`  
Status: **NEW SUPPORTING TARGET-LEVEL THEOREMS / FULL QFORM OPEN / CONTINUITY SEPARATE**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 0. First unpaid implication and result

The inherited unpaid implication was `QFORM-SCHUR-LEAKAGE-OR-WHOLE-VOLUME-EXIT-v1`: in a surviving no-pivot/N3 state, expose before active-law fragmentation either a useful whole-bank Schur leakage or a whole-law volume/ridge/bank exit. The preceding fleet02/B14 r34 theorem already removed the exact-zero-self restriction. If an outer original-coordinate invertible indefinite pair `C` is completed, with

`D=|det C|`, `kappa=sigma_min(C)`,

and an active bank submeasure of mass `m` drives

`Y=hX^2+X S(V)+R(V)`

with arbitrary real `h`, arbitrary same-bank `R`, and unnormalised slope-density cap `L`, then

`||p_Q^sub||_inf <= 8 sqrt(mL/kappa) + C_* m/sqrt(D)`,            (0.1)

where

`C_* = 2+log 2+sqrt(2 pi e) erfc(1/sqrt 2)`
`    = 4.004506265397...`.                                        (0.2)

This run proves two complementary statements.

1. **Protected-anchor localization.** Once a scalar Schur slope has one original-coordinate coefficient that is kept whole, every other slope-active coordinate may be fragmented/localized arbitrarily, even countably and at arbitrarily remote locations, with **exactly zero loss** in the random-slope constant.

2. **High-leverage diagonal-plus-rank-two Schur theorem.** If a completed Schur bank has quadratic matrix `Delta+RGR^T`, with arbitrary diagonal `Delta`, `R` having two orthonormal columns, and `sigma_min(G)>=s`, then every leverage maximum `c=max_i ||r_i||^2` with `0<c<1` produces a whole-bank slope of norm at least `s sqrt(c(1-c))`. Consequently

`boxed:`
`||p_Q||_inf`
` <= 8/[sqrt(kappa s) {c(1-c)}^(1/4)] + C_*/sqrt(D).`            (0.3)

The theorem is sign-free in the two rank-two eigenvalues and uniform in all diagonal and affine twists. The only leverage endpoint not uniformly controlled by this mechanism is `c -> 1`.

A strict rational-skeleton family also shows that **fragmenting the final protected anchor too** can create a spurious `sqrt(N)` divergence in the proof certificate even though both the whole random-slope argument and a completed Claude three-dimensional theorem give dimension-free true-law bounds. Thus the countable rational-skeleton reduction and active cellwise normalization are mathematically different operations.

## 1. Sources consumed and actually applied

### 1.1 Required Claude source

Required immutable source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

`RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` were read. Two completed results are actually used below:

- the Fourier lemma

  `int |psi(t)|^p dt <= 4 pi/sqrt(p),   p>=2`,                   (1.1)

  for every characteristic function of a cap-one one-dimensional density; and

- Theorem A: every three-dimensional quadratic form whose three eigenvalues have modulus at least `sigma`, with arbitrary linear terms, has

  `||p||_inf <= 6 sqrt(pi)/sigma`.                               (1.2)

Equation (1.1) proves the whole-bank scalar slope cap in Section 4. Equation (1.2) independently controls the strict-skeleton obstruction family in Section 6.

### 1.2 Previous fleet02/B14 compiler

Source:

`yspennstate/math-open-problems@ee5472663f2f7934749ac90f2a0305a4cbda37b0`

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T112750Z-fleet02-B14-QFORM-r34/REPORT.md`.

The result actually composed is (0.1), `QFORM-ARBITRARY-SELF-RANDOM-SLOPE-MASS-v1`. It is uniform in arbitrary residual self curvature `h`, arbitrary same-bank dependence of `R` on the slope variables, arbitrary translations, fragment positions, support diameter and moments.

### 1.3 Newest completed designated partner

Newest completed compatible fleet03/B14 result available before publication:

`yspennstate/math-open-problems@c236343d243b355155e5bc9a5c57edc42b2d301a`

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T114804Z-fleet03-B14-QFORM-r34/REPORT.md`.

Its theorem `QFORM-COUNTABLE-RATIONAL-SKELETON-LOCALIZATION-v1` proves that the exact optimal affine interval-concentration constant over the full QFORM target equals the optimum on a countable skeleton where each marginal is the indicator of a compact finite union of rational-endpoint intervals of total measure one, `A` has rational entries/simple nonzero spectrum with at least three eigenvalues strictly outside `[-1,1]`, affine coefficients and test intervals are rational. The equality has zero constant loss and retains arbitrary fragment count, separation and diameter.

Section 6 applies this completed partner result to a real obstruction: the cellwise-loss family is built **inside that strict skeleton**, so global rational-skeleton localization cannot be used to justify fragment-first reciprocal payment.

## 2. Protected-anchor slope localization

### Theorem 2.1 — `QFORM-PROTECTED-ANCHOR-SLOPE-LOCALIZATION-v1`

Let `V_1,...,V_d` be independent original-coordinate probability variables with densities `f_j<=1`. Let

`S(V)=beta+sum_{j=1}^d c_j V_j`,                                (2.1)

and choose an anchor `k` with `c_k !=0`.

For every `j != k`, take an arbitrary finite or countable positive decomposition

`f_j = sum_{r in R_j} g_{j,r}`,                                  (2.2)

and put `m_{j,r}=int g_{j,r}`. The anchor density `f_k` is left whole. For a multi-index `alpha=(r_j)_{j!=k}`, let `nu_alpha` be the corresponding product submeasure and

`m_alpha=prod_{j!=k} m_{j,r_j}`.                                 (2.3)

Then the unnormalised pushforward of `nu_alpha` under `S` has a density satisfying

`boxed: ||d(S_#nu_alpha)/ds||_inf <= m_alpha/|c_k|.`             (2.4)

The statement remains valid with arbitrary additional unfragmented probability-bank coordinates and arbitrary translations `beta`.

### Proof

Condition on every bank coordinate except the anchor. For a fixed non-anchor configuration, the conditional `S`-density coming from `V_k` is

`|c_k|^(-1) f_k((s-beta-sum_{j!=k}c_jv_j)/c_k) <= |c_k|^(-1).`  (2.5)

Integrating (2.5) against the non-anchor product submeasure of total mass `m_alpha` proves (2.4). No support radius, moment, fragment count, fragment position or separation occurs. QED.

### Corollary 2.2 — exact mass restoration after a physical pair

Suppose exact completion of an original-coordinate invertible indefinite pair leaves

`Y=hX^2+X S(V)+R(V)`,                                            (2.6)

where `X` is another genuine independent cap-one coordinate, `h` is arbitrary, and `R` is an arbitrary same-bank measurable remainder. Apply (0.1) to every `nu_alpha`, with

`L_alpha <= m_alpha/|c_k|`.                                      (2.7)

Then

`||p_{Q,alpha}^sub||_inf`
` <= m_alpha[8/sqrt(kappa |c_k|)+C_*/sqrt(D)].`                  (2.8)

Since `sum_alpha m_alpha=1`, positive summation gives

`boxed:`
`||p_Q||_inf <= 8/sqrt(kappa |c_k|)+C_*/sqrt(D).`                (2.9)

For the common Schur slope

`S(V)=beta+2a^T V`,                                               (2.10)

choosing physical anchor `k` yields

`boxed:`
`||p_Q||_inf <= 4 sqrt(2)/sqrt(kappa |a_k|)+C_*/sqrt(D).`        (2.11)

Thus all non-anchor slope-active coordinates can be localized at zero tax. Equation (2.11) is not intended as a diffuse-bank bound when all `|a_k|` are tiny; in that regime one must pay the whole-bank projection/Fourier certificate before selecting a coordinate.

## 3. High-leverage row of a diagonal-plus-rank-two Schur bank

### Theorem 3.1 — `QFORM-RANK2-HEAVY-ROW-SCHUR-SLOPE-v1`

Let an original-coordinate invertible indefinite physical pair have block `C` and parameters `D,kappa` as above. After exact completion, suppose a remaining independent product bank `V=(V_1,...,V_d)` has quadratic coefficient

`S_VV = Delta + R G R^T`,                                       (3.1)

where

- `Delta` is an arbitrary real diagonal matrix;
- `R` is a real `d x 2` matrix with `R^T R=I_2`;
- `G` is real symmetric invertible with `sigma_min(G)>=s>0`.

All affine terms are arbitrary. Let `r_i` denote the rows of `R` and put

`c=max_i ||r_i||_2^2`.                                           (3.2)

If `0<c<1`, then

`boxed:`
`||p_Q||_inf`
` <= 8/[sqrt(kappa s) {c(1-c)}^(1/4)] + C_*/sqrt(D).`            (3.3)

In particular, if `1/2<c<=1-delta`, then

`||p_Q||_inf`
` <= 8(2/delta)^(1/4)/sqrt(kappa s)+C_*/sqrt(D).`                (3.4)

The signs of the two eigenvalues of `G` are arbitrary.

### Proof: exact row-to-bank leakage

Choose `i` with `||r_i||^2=c`, let `T=RGR^T`, and define the off-diagonal row vector

`a_j=T_ij=r_i^T G r_j,   j != i`.                                (3.5)

Since the columns of `R` are orthonormal,

`sum_j r_j r_j^T=I_2`.                                          (3.6)

Hence

`||a||_2^2`
` = sum_{j!=i}(r_i^T G r_j)^2`
` = r_i^T G(I_2-r_ir_i^T)G r_i`
` = ||G r_i||_2^2-(r_i^T G r_i)^2.`                             (3.7)

Write `r_i=sqrt(c)e`, `||e||=1`. Then

`||a||_2^2`
` = c||Ge||^2-c^2(e^TGe)^2`
` >= c(1-c)||Ge||^2`
` >= c(1-c)s^2.`                                                 (3.8)

Therefore

`boxed: ||a||_2 >= s sqrt(c(1-c)).`                              (3.9)

The scaling is sharp at the level of this leakage identity: for example, rows `(sqrt(c),0)`, `(sqrt(1-c),0)`, `(0,1)` and `G=sI_2` give equality in (3.9).

Keep the physical bank coordinate `X=V_i`. The arbitrary diagonal twist only changes its self coefficient. Thus the bank polynomial has the exact form

`hX^2+X[beta+2a^T V_{-i}]+R_0(V_{-i}),`                         (3.10)

with arbitrary `h,beta,R_0`.

## 4. Claude `L^p` lemma pays the whole slope

We derive a source-valid projection cap directly from (1.1): for every nonzero vector `a` and independent cap-one original-coordinate bank,

`boxed: ||p_{a^T V}||_inf <=2/||a||_2.`                         (4.1)

If some `|a_j|>=||a||/sqrt(2)`, condition on all other coordinates and obtain density cap

`1/|a_j| <= sqrt(2)/||a|| <2/||a||`.                            (4.2)

Otherwise set

`alpha_j=a_j^2/||a||^2 <=1/2`.                                  (4.3)

Generalized Holder with exponents `1/alpha_j`, followed by the Claude lemma (1.1), gives

`int |phi_{a^TV}(t)|dt <=4pi/||a||`.                             (4.4)

Fourier inversion yields (4.1).

Consequently the slope `beta+2a^TV` in (3.10) has density cap

`H <=1/||a|| <=1/[s sqrt(c(1-c))].`                              (4.5)

Apply the arbitrary-self compiler (0.1) with `m=1`. Equations (4.5) and (3.9) give (3.3).

### Protected second-stage localization

If the slope vector `a` itself has a physical coordinate `k` satisfying

`|a_k|>=||a||/2`,                                                (4.6)

then retain only `V_k` whole and arbitrarily fragment/localize every other coordinate in `V_{-i}`. On a subproduct cell of mass `m`, Theorem 2.1 gives slope cap

`L <= m/(2|a_k|) <= m/||a||`.                                   (4.7)

Thus the same value `H=1/||a||` used in the whole-bank estimate survives cellwise with a full mass factor and summation preserves (3.3) exactly. In this heavy-second-stage case only the hub coordinate `i` and one slope anchor `k` need remain unfragmented after the outer pair.

If (4.6) fails, the slope is genuinely diffuse; it should be paid by the whole-bank Fourier/projection certificate before active fragmentation.

## 5. Near-coordinate endpoint is a real branch boundary

The factor `[c(1-c)]^(-1/4)` diverges only as `c->1` (the diffuse `c<=1/2` regime belongs to the previously completed diffuse Fresnel branch). This is not merely a proof artifact of (3.7): when the rank-two frame becomes coordinate-supported, an arbitrary diagonal twist can cancel its collective curvature exactly. For instance, with `R=I_2`, `G=sI_2` and `Delta=-sI_2`, the bank quadratic matrix is zero. Therefore a theorem depending only on the low-rank eigenvalue scale `s` cannot remain uniformly informative at `c=1` under arbitrary diagonal twists. A full QFORM proof must switch at that endpoint to curvature supplied elsewhere (physical pair/ridge/volume/rank-one mechanisms); coefficient-to-output-law continuity is not available for arbitrary unbounded inputs.

## 6. Strict rational-skeleton barrier to fragmenting the final anchor

Let

`E_N = union_{j=1}^N [4^j,4^j+1/N]`.                             (6.1)

Take `U_1,U_2,X` uniform on `[0,1]`, and let `V_1,V_2` have density `1_{E_N}`. Define

`Q_N=4U_1U_2-3X^2+2XV_1+2XV_2+V_1^2+V_2^2.`                    (6.2)

Its rational symmetric matrix is the direct sum of

`C=[[0,2],[2,0]]`                                                (6.3)

and

`B=[[-3,1,1],[1,1,0],[1,0,1]].`                                 (6.4)

The spectra are

`spec(C)={-2,2}`,                                                (6.5)

`spec(B)={1,-1-sqrt(6),-1+sqrt(6)}.`                            (6.6)

Thus the full matrix has simple nonzero spectrum and four eigenvalues of modulus strictly greater than one. Every marginal in (6.1) is a rational-endpoint finite-fragment indicator of total measure one. Hence this family lies directly in the strict rational skeleton supplied by the designated partner theorem.

Completing `C` gives `D=4`, `kappa=2`, and leaves

`h=-3`,
`S(V)=2(V_1+V_2)`,
`R(V)=V_1^2+V_2^2`.                                              (6.7)

Since `V_1+V_2` has density cap at most one, `S` has density cap at most `1/2`. Equation (0.1) therefore yields

`boxed: ||p_{Q_N}||_inf <=4+C_*/2=6.002253132698...`             (6.8)

uniformly in `N` and in the exponentially growing fragment separation.

Now fragment only `V_1` into its `N` component intervals and keep `V_2` whole. Each piece has mass `m=1/N`, and Theorem 2.1 gives unnormalised slope cap `L<=m/2`; (0.1) is exactly `m(4+C_*/2)`, and summing recovers (6.8) with no loss.

In contrast, split **both** `V_1` and `V_2` into their `N` intervals and apply (0.1) separately on all `N^2` cells. Each cell has mass

`m=N^(-2)`,                                                     (6.9)

and the pushforward of `2(V_1+V_2)` is a scaled triangular convolution with exact peak

`L=1/(2N)`.                                                       (6.10)

The cellwise certificate is

`4N^(-3/2)+(C_*/2)N^(-2)`,                                      (6.11)

so summing the `N^2` black-box cell bounds gives

`boxed: 4 sqrt(N)+C_*/2.`                                       (6.12)

It diverges although (6.8) is uniform. This proves

`QFORM-STRICT-SKELETON-TWOSIDED-SLOPE-FRAGMENT-BARRIER-v1`.

It is a proof-order obstruction only, not a QFORM counterexample and not a lower bound on the true output density.

### Independent Claude check on the same family

Condition on `U_1,U_2`. The remaining three-variable homogeneous block is exactly `B`, whose three eigenvalues all have modulus at least one. Claude Theorem A (1.2) therefore gives

`boxed: ||p_{Q_N}||_inf <=6 sqrt(pi)=10.6347231054...`            (6.13)

for every `N` and all conditioning-generated linear terms. This is an actual completed-source inequality showing that the growth in (6.12) is entirely an artifact of fragment-first reciprocal payment.

## 7. How the newest partner theorem is used

The designated partner r34 result is a global extremal localization theorem: to prove a uniform affine interval bound it is enough, with **no constant loss**, to prove it on the strict rational skeleton. It does not say that a proof may normalize every active fragment and apply a nonlinear reciprocal certificate independently on each product cell.

The family (6.2) makes this distinction concrete inside the partner's own skeleton:

- whole skeleton law: (6.8) is uniform;
- one-sided active fragmentation with one protected physical anchor: exact same constant;
- two-sided active fragmentation before slope payment: certificate grows as `sqrt(N)`;
- independent Claude theorem: the actual law remains uniformly bounded.

Therefore rational/TV localization should occur at the level of the **whole interval-concentration problem**, while branch-specific reciprocal smoothing must retain enough original-coordinate mass homogeneity internally.

## 8. Sharpened remaining implication

The first unpaid implication is now

`QFORM-PROTECTED-ANCHOR-OR-WHOLE-BANK-EXIT-v1`:

> In every remaining N3/no-pivot state, after exposing an original-coordinate physical pair or equivalent product-safe core, force one of the following **before active cellwise normalization**: (i) a quantitatively useful Schur slope with a physical anchor retained whole, after which Theorem 2.1 allows every other slope coordinate to be localized at zero tax; (ii) a diffuse whole-bank projection/Fresnel certificate; (iii) a whole-law D'/D5/ridge/mixed-hub/bank exit; or (iv) a near-coordinate endpoint whose missing third curvature is paid by a different physical/rank-one mechanism.

For diagonal-plus-rank-two Schur curvature, Theorem 3.1 closes every high-leverage regime bounded away from `c=1`, while the previous diffuse branch covers the spread regime. The remaining structural debt is the near-coordinate endpoint and, more generally, Schur curvature that is not quantitatively captured by a diagonal-plus-rank-two model.

No bounded-support, bounded-diameter, fixed-fragment-count, moment, log-concavity, post-rotation independence, or coefficient-to-output-law continuity hypothesis has been introduced.

## 9. Source integrity

Fresh owner control and live correction inbox were reread during the run; revision `2026-09-22.15` remained QFORM-only and no later correction invalidating the arguments above was found. The required Claude source and the newest completed designated partner source were read directly at the immutable commits stated in Section 1. The partner had begun a later invocation by the final source refresh but no newer completed compatible result was available at that point.

The full QFORM conjecture remains **OPEN**. Essential boundedness is the target here; continuity remains a separate open requirement. Native authenticated receiver-memory ingestion was not observed, so execution remains `WITHOUT_VERIFIED_BRAIN`.
