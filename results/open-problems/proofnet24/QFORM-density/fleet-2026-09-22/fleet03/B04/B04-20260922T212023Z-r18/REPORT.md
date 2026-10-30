SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-22T21:20:23Z.
attacking: product-rearrangement closure for the genuinely rotated indefinite pure cross triangle, with arbitrary affine terms and cap-one independent laws.

# fleet03/B04 — a sharp logarithmic product-rearrangement bound for the three-edge cross triangle

**Run:** `B04-20260922T212023Z-r18`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Product Fourier rearrangement  
**Fresh owner control observed at start:** revision `2026-09-22.15`, brain commit `c4c4bc45982251b1901c653216fdb52b08947256` (later refresh required before publication)  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `NEW SUPPORTING TARGET-INSTANCE THEOREM / FULL QFORM OPEN`.

## 1. Target and correction discipline

The full owner target remains open: for every dimension, every product law with independent real coordinate densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential-supremum bound for the density of `X^T A X`, or give a valid counterexample. Continuity is a separate requested conclusion.

This run does **not** use law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, conditional projection-density moments, fiber suprema, a uniformly good principal minor, or leakage-free scalar-bank extraction. In particular it consumes the fresh correction `QFORM-TRIBANK-CROSS-CORE-LEAKAGE-CLOSURE-FALSE-v1`: a well-conditioned off-diagonal triangle plus arbitrary within-bank quadratic phases can collapse to rank one. The theorem below therefore keeps the exact scope **pure cross triangle plus arbitrary affine terms**. It does not silently treat arbitrary same-bank quadratic leakage as harmless.

The designated partner is `fleet04/B04`. A fresh direct lookup of its shared QFORM handoff directory returned no completed current-QFORM artifact, so no designated-partner result is fabricated. As a compatible completed peer control, this run applies the fleet02/B05 three-scalar theorem at its actual unit-triangle inequality below.

Peer/control sources actually used:

- fleet02/B05 `QFORM-THREE-BANK-GENERAL-CORE-v1`, `yspennstate/math-open-problems@a31006ef311ca9e937f37c62d602d21ada3b1139`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T202100Z-b05-qform-47d9c1a2/REPORT.md`. It gives `<36/sigma_min(M)` for an actual independent three-scalar quadratic core, uniformly in affine terms.
- fleet01/B01 rank-one-completion correction, `yspennstate/math-open-problems@bfb018ea3b3734eec6e051778c5671d954717b74`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260922T210642Z-b01-qform-auto11/REPORT.md`. It proves that arbitrary diagonal within-bank phases can rank-one-complete every nonzero cross triangle; the present theorem is deliberately scoped so that this obstruction is not ignored.

## 2. Product-density logarithmic envelope

We begin with a product-space inequality that uses only the density caps and probability normalization.

### Lemma 2.1 — tunable logarithmic product envelope

Let `X,Y` be independent real random variables with probability densities `f,g` satisfying `0<=f,g<=1`. Let `Z=XY`. Then `Z` is absolutely continuous and, for every `R>0` and almost every `z != 0`,

`p_Z(z) <= 2/R + 2 log_+(R^2/|z|)`.                 (2.1)

Here `log_+(x)=max(log x,0)`.

#### Proof

For `z != 0`, the usual product-density formula is

`p_Z(z)= integral_R f(x) g(z/x) dx/|x|`.             (2.2)

First suppose `|z|<R^2`. Split the integral into

`|x|<|z|/R`, `|z|/R <= |x| <= R`, and `|x|>R`.

On the last region, since `g<=1`,

`integral_(|x|>R) f(x)g(z/x) dx/|x| <= R^(-1) integral f <=1/R`.   (2.3)

On the first region substitute `y=z/x`. Then `|y|>R` and `dx/|x|=dy/|y|`, so, using `f<=1`,

`integral_(|x|<|z|/R) f(x)g(z/x) dx/|x|`
` <= integral_(|y|>R) g(y)dy/|y| <=1/R`.             (2.4)

On the middle region use both density caps:

`integral ... <= integral_(|z|/R <= |x| <=R) dx/|x|`
` =2 log(R^2/|z|)`.                                  (2.5)

This proves (2.1) when `|z|<R^2`.

If `|z|>=R^2`, split instead at `sqrt(|z|)`. The same direct/substitution argument gives

`p_Z(z)<=2/sqrt(|z|)<=2/R`,                           (2.6)

which is again (2.1), since the logarithmic term vanishes. There is no atom at zero because `X` and `Y` are absolutely continuous, hence `P(XY=0)=0`; (2.2) therefore supplies an absolutely continuous representative. QED.

This estimate is a product rearrangement, not a pointwise oscillatory estimate. Its logarithmic singularity is exactly the two-factor hyperbolic singularity one expects near `XY=0`.

## 3. Sharp moving-quadratic logarithmic integral

The next lemma pays the moving logarithmic singularity produced after conditioning on the third variable.

### Lemma 3.1 — uniform quadratic-log trace

For every `alpha !=0`, every `beta,u0 in R`, and every `R>0`,

`integral_R log_+( R^2 / |alpha (u-u0)^2 + beta| ) du`
` <= 4 R / sqrt(|alpha|)`.                            (3.1)

The constant `4` is sharp for this one-dimensional integral: equality is approached/attained at the normalized double-root case `beta=0` after scaling.

#### Proof

Scale

`y = sqrt(|alpha|)(u-u0)/R`.

It is enough to prove

`sup_(c in R) F(c) <=4`,
`F(c)=integral_R log_+(1/|y^2-c|)dy`.                 (3.2)

For `c<0`, write `c=-r^2`. If `r>=1`, `F(c)=0`. For `0<=r<1`,

`F(-r^2)=2 integral_0^(sqrt(1-r^2)) -log(y^2+r^2) dy`.  (3.3)

Differentiating in `r^2` is legitimate away from the endpoint and the endpoint term is zero because the logarithm vanishes there; the derivative is nonpositive. Hence this branch is maximized at `r=0`, where

`F(0)=2 integral_0^1 -log(y^2)dy =4`.                 (3.4)

For `c=r^2>=0`, first take `0<=r<=1`. An antiderivative of `-log|y^2-r^2|` is

`G_r(y)= -y log|y^2-r^2| +2y + r log |(y-r)/(y+r)|`.   (3.5)

With `b=sqrt(1+r^2)`, the support on the positive half-line is `[0,b]`. Since `b^2-r^2=1`,

`F(r^2)=2G_r(b)`
`      =4( sqrt(1+r^2) - r asinh(r) )`.              (3.6)

Its derivative with respect to `r` is `-4 asinh(r)<=0`, so it is at most `4`.

For `r>=1`, use layer cake. For `0<delta<=1`,

`m_r(delta)= |{y: |y^2-r^2|<delta}|`
` =2( sqrt(r^2+delta)-sqrt(r^2-delta) )`.             (3.7)

For each fixed `delta`, this decreases in `r`, so the whole layer-cake integral

`F(r^2)= integral_0^1 m_r(delta) ddelta/delta`         (3.8)

is maximized at `r=1`, already covered by (3.6), and is `<4`. This proves (3.2), and scaling gives (3.1). QED.

## 4. Main theorem: pure three-edge cross triangle

### Theorem 4.1 — `QFORM-CROSS-TRIANGLE-REARRANGEMENT-v1`

Let `U,V,W` be independent real random variables with probability densities bounded by one. Let `a,b,c` be nonzero real numbers and let `ell_1,ell_2,ell_3,d` be arbitrary real affine coefficients. Define

`Q = 2a U V + 2b V W + 2c W U`
`    + ell_1 U + ell_2 V + ell_3 W + d`.              (4.1)

Then `Q` is absolutely continuous and

`||p_Q||_infinity`
` <= 4 / ( |b|^(1/2) |ac|^(1/4) )`.                 (4.2)

By cyclic symmetry one may choose the best product edge, hence

`boxed( ||p_Q||_infinity`
` <= 4 / ( |abc| max{|a|,|b|,|c|} )^(1/4) ).`       (4.3)

No moment, centering, support, log-concavity, continuity, or post-rotation independence hypothesis is used.

#### Proof

Condition on `U=u`. Complete the `(V,W)` bilinear polynomial exactly. Put

`A(u)=(2c u+ell_3)/(2b)`,
`B(u)=(2a u+ell_2)/(2b)`.                             (4.4)

Then

`Q = 2b (V+A(u))(W+B(u)) + R(u)`,                    (4.5)

where direct expansion gives

`R(u)= -(2ac/b)u^2`
`      + [ell_1-(a ell_3+c ell_2)/b]u`
`      + d-ell_2 ell_3/(2b)`.                        (4.6)

Since `ac !=0`, complete the remaining scalar square:

`R(u)=kappa -(2ac/b)(u-u0)^2`                        (4.7)

for suitable real `u0,kappa`.

For fixed `u`, the translated variables `V+A(u)` and `W+B(u)` remain independent and have density caps at most one. Therefore Lemma 2.1 gives, for every free parameter `R0>0`,

`p_(Q|U=u)(q)`
` <= 1/(2|b|) [ 2/R0 + 2 log_+(R0^2/|z_q(u)|) ]`,   (4.8)

where

`z_q(u)=(q-R(u))/(2b)`
`      = beta_q + alpha (u-u0)^2`,
`alpha=ac/b^2 !=0`.                                  (4.9)

Average (4.8) against the density `f_U(u)`. Since `0<=f_U<=1`, Lemma 3.1 yields

`p_Q(q)`
` <= 1/(|b|R0)`
`    + (1/|b|) integral f_U(u) log_+(R0^2/|z_q(u)|)du`
` <= 1/(|b|R0) + 4R0/(|b|sqrt(|alpha|))`
` = 1/(|b|R0) + 4R0/sqrt(|ac|)`.                    (4.10)

The right side is independent of `q`. Optimize over `R0>0`. The minimum of `A/R0+B R0` is `2sqrt(AB)`, attained at

`R0^2 = sqrt(|ac|)/(4|b|)`.                           (4.11)

Thus

`||p_Q||_infinity <= 4/( |b|^(1/2)|ac|^(1/4) )`,     (4.12)

proving (4.2). Repeating the same argument with each variable as the outer conditioning variable gives the three cyclic estimates. Choosing the edge of largest modulus as the product edge gives (4.3). Absolute continuity follows from the conditional product-density representation and Fubini. QED.

## 5. Genuinely rotated indefinite target instance

Take

`A_triangle = [[0,1,1],[1,0,1],[1,1,0]]`.            (5.1)

Its eigenvalues are exactly

`{2,-1,-1}`,                                          (5.2)

so it is indefinite, not diagonal in the independent coordinates, and has **three eigenvalues of absolute value at least one**. For every independent triple of arbitrary real probability densities bounded by one,

`Q_triangle = X^T A_triangle X`
`           =2(X1 X2+X2 X3+X3 X1)`.                  (5.3)

Theorem 4.1 with `a=b=c=1` yields the explicit universal target-instance bound

`boxed( ||p_(Q_triangle)||_infinity <=4 ).`           (5.4)

The same `4` remains valid after adding an arbitrary affine function of `X1,X2,X3` and an arbitrary scalar constant.

This is a substantial sharpening of the completed fleet02/B05 three-scalar control when applied to the same actual matrix: since `sigma_min(A_triangle)=1`, that theorem gives

`||p_(Q_triangle+affine)||_infinity <36`,              (5.5)

whereas the product-rearrangement proof above gives `<=4`.

Equation (5.5) is the promised actual application of a completed compatible peer result, not merely a citation.

## 6. Why the fresh leakage correction matters

The theorem cannot be extended by simply replacing the affine terms in (4.1) with arbitrary one-variable quadratic phases. The fresh fleet01/B01 correction gives the exact obstruction:

`2(UV+VW+WU)+U^2+V^2+W^2=(U+V+W)^2`,                (6.1)

whose density is unbounded for iid `Unif[-1/2,1/2]`. The completed matrix in (6.1) has rank one, so this does **not** refute the full three-large-eigenvalue conjecture; it refutes only a cross-core-only leakage closure.

The present proof shows something complementary: when the same-bank quadratic leakage is genuinely absent (affine leakage is allowed), the hyperbolic product singularity and the moving quadratic singularity cancel quantitatively with a sharp rearrangement budget, producing the clean constant `4`.

Thus the next structural step should not ask whether a cross triangle alone survives arbitrary internal curvature. It should route the internal curvature into one of two buckets:

1. an actual rank-one completion plus **two defect curvatures**, as identified by fleet01/B01; or
2. a cross-triangle branch of the exact type in Theorem 4.1 after those defects are paid elsewhere by a ridge, rank-two half-Riesz, or grouped-bank estimate.

## 7. First unpaid implication

`QFORM-TRIBANK-DEFECT-REARRANGEMENT-ROUTING-v1`:

> Starting from a three-bank scalar cross triangle with arbitrary within-bank quadratic blocks, use the unique rank-one completion to expose the two defect curvatures forced by a genuinely three-dimensional spectral resource. Prove that either those defects can be paid inside disjoint original-coordinate banks by an existing ridge/rank-two theorem, or after their payment the residual cross triangle enters Theorem 4.1 with a uniform density-normalized edge product. The routing must aggregate before reciprocal minor payment and must not condition on orthogonal coordinates inside the same bank.

The scalar theorem above pays the analytic endpoint of this route with an explicit constant. The remaining difficulty is structural/product-preserving extraction, not the logarithmic product singularity itself.

## 8. Status

- Full QFORM conjecture: **OPEN**.
- `QFORM-CROSS-TRIANGLE-REARRANGEMENT-v1`: **PROVED in this report**.
- Unit pure cross triangle `A_triangle`: **target-valid, essential density bound `<=4` proved**.
- Arbitrary affine perturbations of that three-variable cross triangle: **same bound proved**.
- Arbitrary within-bank quadratic leakage: **not covered; cross-core-only closure is refuted by the fresh correction**.
- Continuity of the density under arbitrary merely measurable input densities: **not proved by this run**. Absolute continuity and an `L^infinity` representative are proved.

No numerical histogram, Gaussian approximation, moment assumption, compact support assumption, or diagonal-basis independence is used.
