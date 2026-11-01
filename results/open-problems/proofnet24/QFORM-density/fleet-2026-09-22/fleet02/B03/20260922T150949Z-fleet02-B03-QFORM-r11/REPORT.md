# fleet02/B03 — multiplicative collision packet and critical Riesz endpoint

**Run:** `20260922T150949Z-fleet02-B03-QFORM-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Decoupled time integral  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full conjecture remains open. This report proves two correction-safe supporting theorems. The first gives a finite-collision-order-to-`L^infinity` upgrade for a genuine indefinite rotated packet `hyperbolic product + square`. The second applies the designated partner's new half-Riesz endpoint theorem to the critical boundary of the regularized-determinant estimate, where the residual characteristic function has exactly `1/|t|` decay and direct Fourier inversion is logarithmically divergent.

## 1. Sources and corrections consumed

Fresh owner/control state was read from `yspennstate/math-research-brain` main. The target is: independent real coordinates with one-dimensional densities at most one; real symmetric `A`; at least three eigenvalues of modulus at least one; prove one universal essential density bound for `X^TAX` or a valid counterexample. No moments, connected support, definite signature, diagonal-basis independence or post-rotation independence are assumed.

Corrections consumed before publication include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, and the newer `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`. None of their challenged premises is used below.

Completed designated-partner results actually applied:

1. fleet03/B03 all-order collision hierarchy, canonical report  
   `yspennstate/math-open-problems@719c114f8dad72a6780b194cbea124cfa4cf6d44:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T123410Z-fleet03-B03-QFORM-r11b/REPORT.md`.
   In particular, for Gaussian mollification `p_eps`, `J_m(eps)=int p_eps^m`, and `||p||_infinity<=B` is equivalent to `J_m(eps)<=B^(m-1)` for all `m>=2,eps>0`. At `m=2`,
   `J_2=(2pi)^(-1)int |phi(t)|^2 e^{-eps^2t^2}dt` and the exact independent-copy bilinearization retains the dependence of each sum/difference pair.
2. fleet03/B03 half-Riesz endpoint theorem, canonical report  
   `yspennstate/math-open-problems@f1e0ffb295dd293cf7bb2e401fa0f24659a26c6d:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T142410Z-fleet03-B03-QFORM-r13/REPORT.md`.
   If `Q=d(Z+h(W))^2+R(W)`, `Z` is independent of `W`, `f_Z<=1`, and `|eta_R(t)|<=min(1,K/|t|)`, then
   `||p_Q||_infinity <= 4 sqrt(2/pi)|d|^(-1/2)K^(1/2)`.

A second completed source used below is the regularized determinant theorem
`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.
For an original-coordinate cross block `B`, if `1<=q<2` and the coordinate leverage of `range(B)` on one side is at most `q/2`, then

`|eta(t)| <= det(I+2q t^2 BB^T/(pi^2 e^2))^(-1/(4q))`.

For `q=2` the same formula is valid without a leverage assumption. The report also pins the sharp one-dimensional Young constant of Beckner, which is used in Section 2.

## 2. A multiplicative `L^p` lemma for independent cap-one laws

### Lemma 2.1 (`QFORM-MULTIPLICATIVE-YOUNG-LP-v1`)

Let `X,Y` be independent real random variables with probability densities bounded by one. For every `s>1`, the product `H=XY` has a density in `L^s`. For the one exponent needed below,

`boxed( ||p_H||_3 <= 2 sqrt(3). )`                                           (2.1)

At the independent-copy level,

`boxed( ||p_H||_2^2 <= 3 sqrt(3). )`                                         (2.2)

Hence, if `psi(t)=E exp(itXY)`, Plancherel gives the genuinely integrated, dependence-safe estimate

`boxed( (2pi)^(-1) int_R |psi(t)|^2 dt <= 3 sqrt(3). )`                       (2.3)

Equivalently the left side is the zero-mollifier limit of the fleet03/B03 two-copy quantity, and

`|psi(t)|^2=E exp(it(XY-X'Y'))`

with no claim that any sums and differences formed from the copies are independent.

#### Proof of (2.1)

Split the densities into positive and negative half-line pieces. For one fixed sign quadrant, write its nonnegative subdensities on `(0,infinity)` as `f,g`, with masses `a,b`. The product density on the positive half-line is

`h(z)=int_0^infinity f(x)g(z/x) dx/x`.

Put `z=e^w` and define

`F(u)=e^(u/3)f(e^u)`, `G(v)=e^(v/3)g(e^v)`.

Then exactly

`e^(w/3) h(e^w) = (F*G)(w)`,

so `||h||_3=||F*G||_3`. Also

`||F||_(3/2)^(3/2)=int_0^infinity x^(-1/2) f(x)^(3/2) dx`
` <= int_0^infinity x^(-1/2)f(x) dx`
` <= int_0^a x^(-1/2)dx = 2 sqrt(a)`.                              (2.4)

The last step is the elementary bathtub/rearrangement inequality for the decreasing weight `x^(-1/2)`, using `0<=f<=1` and mass `a`. Thus

`||F||_(3/2) <= 2^(2/3)a^(1/3)`, and similarly for `G`.

Sharp Young in one dimension for `L^(3/2)*L^(3/2)->L^3` has constant `sqrt(3)/2`. Therefore the quadrant contribution obeys

`||h||_3 <= sqrt(3) 2^(1/3) (ab)^(1/3)`.                          (2.5)

Let the positive/negative masses of `X` be `a_+,a_-` and those of `Y` be `b_+,b_-`. Positive products are the sum of the `++` and `--` quadrant densities; negative products are the sum of `+-` and `-+`. Since the positive and negative output supports are disjoint, (2.5) and

`(x^(1/3)+y^(1/3))^3 <= 4(x+y)`

give

`||p_H||_3^3`
` <= 24 sqrt(3)[a_+b_+ + a_-b_- + a_+b_- + a_-b_+]`
` = 24 sqrt(3) = (2sqrt(3))^3`.                                    (2.6)

This proves (2.1).

#### Proof of (2.2)

Repeat the same logarithmic argument with output exponent `s=2` and input Young exponent `4/3`. For one quadrant,

`||F||_(4/3) <= (3/2)^(3/4) a^(1/2)`.

The sharp Young constant `L^(4/3)*L^(4/3)->L^2` is `2*3^(-3/4)`. Combining quadrants as above yields

`||p_H||_2 <= 3^(3/4)`, hence (2.2). Scaling gives, for `c!=0`,

`||p_(cXY)||_3 <= 2sqrt(3)|c|^(-2/3)`,
`||p_(cXY)||_2^2 <= 3sqrt(3)|c|^(-1)`.                             (2.7)

### Collision interpretation

The designated partner's hierarchy now applies to an actual inequality. For `H=cXY`, Gaussian convolution cannot increase the `L^3` norm, so

`boxed( J_3^H(eps) <= 24 sqrt(3)|c|^(-2) )`                        (2.8)

for every `eps>0`. This is a genuine third-order collision bound. It is not by itself an `L^infinity` bound, in agreement with the partner's warning that one fixed collision order only gives a sublinear Holder small-ball exponent.

## 3. A square packet in `L^(3/2)`

### Lemma 3.1

Let `Z` have density at most one, let `a!=0`, and let `b` be arbitrary. Then `S=a(Z-b)^2` has a density satisfying

`boxed( ||p_S||_(3/2) <= 2 |a|^(-1/3). )`                          (3.1)

#### Proof

Assume `a>0`; reflection handles `a<0`. Split the law of `Z-b` on the two half-lines, with masses `m_+,m_-`. Each inverse branch `u>0 -> au^2` contributes

`g_+(y)=f(b+sqrt(y/a))/(2sqrt(a y))`.

Changing variables `y=au^2` gives

`int g_+(y)^(3/2)dy`
` = 2^(-1/2)a^(-1/2) int_0^infinity f(b+u)^(3/2)u^(-1/2)du`
` <= sqrt(2)a^(-1/2)sqrt(m_+)`,                                    (3.2)

again by the decreasing-weight bathtub bound. Thus

`||g_+||_(3/2) <= 2^(1/3)|a|^(-1/3)m_+^(1/3)`,

and likewise for the minus branch. Minkowski plus
`m_+^(1/3)+m_-^(1/3)<=2^(2/3)` proves (3.1).

## 4. Main theorem: dependence-safe hyperbolic product plus square

### Theorem 4.1 (`QFORM-DECOUPLED-SADDLE-SQUARE-v1`)

Let `X,Y,Z` be independent real variables with densities at most one and independent of an arbitrary random element `W`. Let `alpha(W), beta(W), h(W), R(W)` be arbitrary measurable real functions, and let `c,a` be nonzero constants. Define

`Q = c (X+alpha(W))(Y+beta(W)) + a (Z+h(W))^2 + R(W)`.             (4.1)

No independence is assumed among the shifts and `R(W)`. Then `Q` has an essentially bounded density and

`boxed( ||p_Q||_infinity <= 4 sqrt(3)|c|^(-2/3)|a|^(-1/3). )`       (4.2)

Consequently every interval `I` obeys the linear small-ball estimate

`P(Q in I) <= 4sqrt(3)|c|^(-2/3)|a|^(-1/3)|I|`.                    (4.3)

#### Proof

Condition on `W=w`. Translations preserve both independence of the three active variables and their density caps. By Lemma 2.1 the hyperbolic term has `L^3` density norm at most

`2sqrt(3)|c|^(-2/3)`.

By Lemma 3.1 the square term has `L^(3/2)` density norm at most

`2|a|^(-1/3)`.

The two terms are conditionally independent. Ordinary Young convolution with `1/3+2/3=1` gives the conditional `L^infinity` bound (4.2), uniformly in `w`; the additive `R(w)` merely translates the density. Averaging the conditional densities preserves the same essential supremum. QED.

This is a finite-collision-order-to-`L^infinity` upgrade of exactly the type left open in fleet03/B03's all-copy report: the third-order multiplicative collision estimate is paired with the dual `L^(3/2)` square packet. No law-uniform pointwise Fresnel estimate is used.

### Matrix corollary

Let `A=A^T`. Suppose three distinct ORIGINAL coordinates can be ordered as `(i,j,k)` so that their principal block is

`A[{i,j,k}] = [[0,b,0],[b,0,0],[0,0,a]]`, with `ab!=0`.             (4.4)

All entries of `A` involving coordinates outside this triple are arbitrary. Conditioning on every outside original coordinate turns them only into linear terms in `X_i,X_j,X_k` plus a constant. Completing affine shifts gives exactly (4.1) with `c=2b`. Hence

`boxed( ||p_(X^TAX)||_infinity <= 2^(4/3)sqrt(3)|a b^2|^(-1/3). )`  (4.5)

The determinant of the displayed principal block is `-ab^2`, and its eigenvalues are exactly `a,b,-b`. Therefore, if `|a|>=1` and `|b|>=1`, that principal triple itself has three eigenvalues of modulus at least one; Cauchy interlacing places the full matrix inside the owner's target class, and

`boxed( ||p_(X^TAX)||_infinity <= 2^(4/3)sqrt(3) < 4.365. )`        (4.6)

This is a genuinely rotated indefinite source packet: for `a=b=1`, the form on the active coordinates is `2XY+Z^2`, not a diagonal form in the independent coordinate basis.

### Aggregate-bank extension

If the three independent active variables have density caps `M_1,M_2,M_3` instead of one, rescaling gives

`||p_Q||_infinity <= 4sqrt(3)(M_1M_2M_3)^(2/3)|c|^(-2/3)|a|^(-1/3).` (4.7)

Thus the same packet survives replacement of each active scalar by a disjoint normalized original-coordinate aggregate, provided those aggregates remain independent and their marginal density caps are controlled. In particular cap `sqrt(2)` on each bank costs only an overall factor two. This is exactly the kind of bank-first payment required by the previous B03 overlap obstruction; it does not assert that every three-eigenvalue matrix admits such a bank decomposition.

### Partner hierarchy applied downstream

Applying fleet03/B03 Theorem 4.2 to (4.2), the complete all-order time hierarchy satisfies

`J_m(eps) <= [4sqrt(3)|c|^(-2/3)|a|^(-1/3)]^(m-1)`                (4.8)

for every integer `m>=2` and `eps>0`. Hence this branch has the desired exponential collision growth and linear small-ball scale, not merely a fixed-`m` Holder exponent.

## 5. Critical endpoint of the regularized determinant after one square pivot

The regularized determinant report proves direct `L^1` Fourier inversion when the number `r` of controlled cross singular values is strictly larger than `2q`. Exactly at `r=2q`, the bound is only `1/|t|` and direct inversion diverges logarithmically. The newest designated-partner half-Riesz theorem pays exactly this missing endpoint once an independent physical square pivot is available.

### Theorem 5.1 (`QFORM-CRITICAL-REGDET-PIVOT-v1`)

Choose an original coordinate `k` with `d=A_kk!=0`, and complete its square. On the remaining original coordinates let `C` denote the Schur residual. Let `I,J` be disjoint sets not containing `k`, and put `B=C[I,J]`. Fix `r` in `{2,3,4}` and assume `B` has singular values `s_1,...,s_r>0` (it may have arbitrary additional singular values). Put

`D_r=prod_{j=1}^r s_j`.

For `r=2`, assume the coordinate leverage of `range(B)` on one physical side is at most `1/2`. For `r=3`, assume it is at most `3/4`. For `r=4`, no leverage assumption is needed. Then

`boxed(
 ||p_(X^TAX)||_infinity
 <= 4 sqrt(2e) r^(-1/4) |d|^(-1/2) D_r^(-1/(2r)).
)`                                                                      (5.1)

The constants are approximately `7.843`, `7.087`, `6.595` for `r=2,3,4` before the homogeneous coefficient factor.

#### Proof

Set `q=r/2`. For `r=2,3`, the stated leverage condition is exactly `max leverage <= q/2`; for `r=4`, `q=2` is the unconditional endpoint of the source theorem. The regularized determinant estimate gives the residual characteristic function

`|eta(t)| <= det(I + r t^2 BB^T/(pi^2 e^2))^(-1/(2r)).`             (5.2)

Retaining only the selected `r` singular-value factors,

`|eta(t)|`
` <= prod_{j=1}^r (1+r t^2 s_j^2/(pi^2e^2))^(-1/(2r))`
` <= min(1, K_r/|t|)`,                                               (5.3)

where

`K_r = (pi e/sqrt(r)) D_r^(-1/r)`.                                  (5.4)

The square completion has the form required by fleet03/B03's `QFORM-HALF-RIESZ-ENDPOINT-v1`. Therefore

`||p||_infinity`
` <=4sqrt(2/pi)|d|^(-1/2)K_r^(1/2)`
` =4sqrt(2e)r^(-1/4)|d|^(-1/2)D_r^(-1/(2r))`,

which is (5.1). QED.

The point is structural, not the modest constant improvement: extra small cross singular values do not enter the denominator, and the theorem pays the exact `r=2q` endpoint that the source's direct Fourier inversion deliberately leaves open.

## 6. What remains unpaid

These results do not prove that every target matrix exposes either packet. The current hard structural debt is now more precise:

* a local/aggregate **saddle-square packet** is paid at the sharp homogeneous scale `|a b^2|^(-1/3)` by Theorem 4.1;
* a physical square pivot plus a **critical diffuse cross packet** with `r=2,3,4` is paid by Theorem 5.1 without a product of all small singular values;
* previous corrections show that one cannot demand a uniformly good fixed principal triple, one fixed rank-two Schur extraction, or one fixed rank-three cross cut from the three-large-eigenvalue hypothesis.

The first unproved implication is therefore a product-coordinate structural transfer: in the heavy/overlap regime, extract either (i) a saddle-square packet in original coordinates or disjoint independent banks, (ii) a critical regularized cross packet after a valid physical pivot, or (iii) a genuinely diffuse bank tail already covered by the existing aggregate/diffuse theorems. The exact-rank-three coloop-bank family from the preceding B03 run shows that the bank branch is logically necessary.

No continuity statement is claimed for Theorem 4.1 or 5.1; only essential boundedness and linear interval bounds are proved. No full-solution claim is made.

## 7. Finite algebra checks used in this run

Only exact algebraic sanity checks were used, not as proof premises:

* `det [[0,b,0],[b,0,0],[0,0,a]] = -ab^2` and characteristic polynomial `(a-lambda)(b-lambda)(b+lambda)`;
* normalized saddle-square constant `2^(4/3)sqrt(3) = 4.364494543886885...`;
* product collision constants `||p_XY||_2^2 <=3sqrt(3)` and `||p_XY||_3^3<=24sqrt(3)`;
* critical regularized-pivot front constants for `r=2,3,4` are `7.842684263...`, `7.086665214...`, `6.594885083...`.

The all-parameter proofs are the analytic derivations above.