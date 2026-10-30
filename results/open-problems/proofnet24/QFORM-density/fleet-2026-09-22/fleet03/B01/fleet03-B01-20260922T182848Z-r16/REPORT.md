# QFORM fleet03/B01 — conditional Young smoothing at a null spectral coloop

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `fleet03-B01-20260922T182848Z-r16`  
Assignment: `Oscillatory replacement`  
Status: `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Exact target, fresh corrections, and the mechanism changed this run

The parent target remains open: for arbitrary `n`, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `Q=X^T A X`, or construct a target-valid counterexample. Continuity is tracked separately.

Fresh owner control was revision `2026-09-22.11`, with QFORM as the sole research target. I used the live correction state rather than the older mathematical proposals in the owner-message source. In particular:

* no law-uniform pointwise Fresnel decay is assumed;
* no independence is asserted after a spectral rotation;
* no unrestricted fiber supremum is used;
* the arbitrary-joint 3D coarea cap and the positive conditional-projection moment are treated as false;
* the newer scalar-conditioning supremum `sup_b ||p_(Q3|Q'=b)||_infinity` is also treated as false, by the source-pinned fleet01/B01 Hadamard corner example.

The previous B01 run paid every orientation of a rank-two residual when the **outer physical pivot is nonzero**. The proof-first owner request identifies the zero/near-zero outer pivot as an unpaid branch. This run changes mechanism: instead of dividing by that pivot, it combines a bilinear term with an independent square by conditional `L^4 * L^(4/3) -> L^infinity` smoothing. It closes a genuine zero-pivot endpoint when one physical coordinate is a unit-leverage spectral coloop.

## 2. The pointwise oscillatory counterexample remains mandatory

Fix `s!=0` and `delta>0`. The set

`E(s,delta)={x: dist(s x^2,2 pi Z)<=delta}`

has infinite Lebesgue measure. Choose a measurable subset `E` of measure one and take `f=1_E`. Then

`Re int exp(i s x^2) f(x) dx >= cos(delta)`.

Thus no law-uniform positive power bound at each frequency can hold over all cap-one input densities. Nothing below uses such a pointwise estimate. The averaged-frequency interface used at the end is instead the exact signed Fejer theorem of the designated partner fleet04/B01.

## 3. A square-pushforward `L^(4/3)` lemma

### Lemma 3.1 — `QFORM-SQUARE-L43-v1`

Let `W` have probability density `h<=H`, where `H>0`, and let `beta!=0`. Then, for every real translation `m`, the variable

`Y=beta (W+m)^2`

has a density in `L^(4/3)` satisfying

`||p_Y||_(4/3) <= 2 sqrt(2) H^(1/2) |beta|^(-1/4)`.          (3.1)

#### Proof

Translation does not change the density cap, so first take `m=0`, `H=1`, `beta=1`. For `y>0`,

`q(y)=[h(sqrt(y))+h(-sqrt(y))]/[2 sqrt(y)]`.

With `r=4/3`, `(a+b)^r<=2^(r-1)(a^r+b^r)` gives

`||q||_r^r <= int_R h(x)^r |x|^(-1/3) dx`.

Since `0<=h<=1`, `h^r<=h`. Splitting at `|x|=1`,

`int h(x)|x|^(-1/3) dx
 <= int_(|x|<=1)|x|^(-1/3) dx + int_(|x|>1) h(x) dx
 <=3+1=4`.

Therefore `||q||_(4/3)<=4^(3/4)=2sqrt(2)`. For general cap `H`, rescale `W'=H W`; then `W'` has density cap one and the `L^(4/3)` norm of the square density scales by `H^(1/2)`. Multiplication by `beta` contributes `|beta|^(-1/4)`. QED.

## 4. Dependence-safe bilinear-plus-square smoothing

### Lemma 4.1 — `QFORM-CONDITIONAL-L4-L43-v1`

Let `X` be independent of a pair `(L,Z)`. Assume:

1. `X` has a probability density `f_X<=1`;
2. `(L,Z)` has a joint density `g` with `||g||_infinity<=M`;
3. the marginal density `p_L` satisfies `||p_L||_infinity<=K`.

Let `alpha,beta` be nonzero reals and let `m(l),c(l)` be measurable. Then

`T=alpha L X + beta (Z+m(L))^2 + c(L)`

has a **continuous** density and

`||p_T||_infinity
 <=2 sqrt(2) M^(1/2) |alpha|^(-3/4) |beta|^(-1/4)
   (8 sqrt(K)+2)`.                                             (4.1)

No independence between `L` and `Z` is assumed.

#### Proof

Write `p(l)=p_L(l)`. For almost every `l` with `p(l)>0`, the conditional density of `Z|L=l` is bounded by

`H_l=M/p(l)`.                                                  (4.2)

Because `X` is independent of `(L,Z)`, it remains independent of `Z` after conditioning on `L=l`. The density of

`U_l=alpha l X`

satisfies

`||p_(U_l)||_4
 =|alpha l|^(-3/4)||f_X||_4
 <=|alpha l|^(-3/4)`,                                        (4.3)

because `f_X<=1` and `int f_X=1`. By Lemma 3.1,

`||p_( beta (Z+m(l))^2 | L=l )||_(4/3)
 <=2sqrt(2)(M/p(l))^(1/2)|beta|^(-1/4)`.                     (4.4)

Conditional Young convolution, `L^4*L^(4/3)->L^infinity`, yields

`||p_(T|L=l)||_infinity
 <=2sqrt(2) M^(1/2)|alpha|^(-3/4)|beta|^(-1/4)
    p(l)^(-1/2)|l|^(-3/4)`.                                  (4.5)

After averaging over `l`, it remains to estimate

`J=int_R p(l)^(1/2)|l|^(-3/4) dl`.                            (4.6)

On `|l|<=1`, `p(l)^(1/2)<=sqrt(K)`, hence that contribution is at most

`sqrt(K) int_(|l|<=1)|l|^(-3/4)dl=8sqrt(K)`.                  (4.7)

On `|l|>1`, Cauchy--Schwarz gives

`int_(|l|>1) p(l)^(1/2)|l|^(-3/4) dl
 <=(int p)^(1/2)(int_(|l|>1)|l|^(-3/2)dl)^(1/2)=2`.           (4.8)

Thus `J<=8sqrt(K)+2`, proving (4.1).

For continuity, for almost every fixed `l!=0` the conditional density is a convolution of an `L^4` density and an `L^(4/3)` density, hence is continuous (indeed in `C_0`) by translation continuity and Holder. The right side of (4.5), after multiplication by `p(l)`, is integrable by (4.6)--(4.8). Dominated convergence therefore makes the unconditional density continuous. QED.

The key point is that a possibly very sharp conditional law `Z|L=l` is allowed: its cap `M/p(l)` is paid with exponent `1/2`, while the outer averaging supplies exactly `p(l)^(1/2)`. This avoids the false assertion that a conditional cap stays uniformly bounded.

## 5. Exact zero-pivot endpoint: a unit-leverage spectral coloop

### Theorem 5.1 — `QFORM-RANK3-NULL-COLOOP-CONTINUOUS-v1`

Let

`A=R Lambda R^T`, `R^T R=I_3`,

be an exact-rank-three real symmetric form. Assume all three nonzero eigenvalues satisfy

`|lambda_j(Lambda)|>=1`.

Let `r_i` be one physical row of `R`. Suppose

`||r_i||=1`,                                                     (5.1)

and the corresponding physical quadratic pivot is exactly null,

`A_ii=r_i^T Lambda r_i=0`.                                      (5.2)

Then for arbitrary independent cap-one inputs, `Q=X^T A X` has a **continuous** density satisfying

`||p_Q||_infinity <= C_null`,                                   (5.3)

where

`C_null=2^(3/4)e^(1/2)(8e^(1/4)+2)<34.029`.                     (5.4)

More precisely, if `eta=||Lambda r_i||` and `Delta=|det Lambda|`, then

`||p_Q||_infinity
 <= C_null eta^(-1/4) Delta^(-1/4)`.                            (5.5)

#### Proof

Put `u=r_i`. Since the rows form a Parseval frame,

`sum_j r_j r_j^T=I_3`.

Taking the quadratic form against the unit vector `u` and using `||u||=1`,

`1=sum_j <r_j,u>^2 >= <u,u>^2=1`.

Hence `<r_j,u>=0` for every `j!=i`, and

`sum_(j!=i) r_j r_j^T=I_3-u u^T`.                              (5.6)

Thus the remaining physical coordinates form a Parseval frame on the two-plane `u^perp`. Choose an orthonormal basis `(e_1,e_2)` of that plane and write the corresponding spectral projection of the remaining independent coordinates as `(L,Z)`. The physical coordinate `X_i` is independent of `(L,Z)`.

Apply the completed product-fiber theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` from fleet02/B06. For a `k`-dimensional Parseval projection of independent cap-one coordinates it gives density cap at most `e^(k/2)`. Therefore

`||p_(L,Z)||_infinity<=e`,
`||p_L||_infinity<=sqrt(e)`.                                   (5.7)

Now use the null-pivot geometry. By (5.2), `Lambda u` lies in `u^perp`. Since `Lambda` is invertible, it is nonzero. Put

`eta=||Lambda u||>=sigma_min(Lambda)>=1`,                       (5.8)

choose `e_1=Lambda u/eta`, and choose `e_2` orthogonal to both. In the basis `(u,e_1,e_2)`, the spectral matrix has the exact form

`Lambda = [[0, eta, 0],
           [eta,b11,b12],
           [0,b12,b22]]`.                                      (5.9)

Consequently

`det Lambda=-eta^2 b22`,                                       (5.10)

so `b22!=0`. In the spectral coordinates `(X_i,L,Z)`,

`Q=2 eta X_i L+b11 L^2+2b12 LZ+b22 Z^2`
` =2eta L X_i
   +b22 (Z+(b12/b22)L)^2
   +(b11-b12^2/b22)L^2`.                                       (5.11)

Lemma 4.1 applies with

`alpha=2eta`, `beta=b22`, `M=e`, `K=sqrt(e)`.                  (5.12)

It gives a continuous density and

`||p_Q||_infinity
 <=2sqrt(2)e^(1/2)(2eta)^(-3/4)|b22|^(-1/4)
   (8e^(1/4)+2)`
` =C_null eta^(-3/4)|b22|^(-1/4)`.                             (5.13)

Using (5.10),

`eta^(-3/4)|b22|^(-1/4)
 =eta^(-1/4)|det Lambda|^(-1/4)`.                              (5.14)

Because `eta>=1` and `|det Lambda|>=1`, (5.3)--(5.5) follow. QED.

### What this pays and what it does not

This is a genuine endpoint of the previously unpaid **zero outer physical pivot** problem: the earlier rank-two Schur theorem cannot divide by `A_ii=0`, while (5.11) converts the null pivot into a bilinear coefficient and an independent square smoother. It is not the full exact-rank-three theorem because unit leverage (5.1) is a special structural hypothesis. It also does not yet cover near-zero nonzero leverage pivots, nor arbitrary additional spectral components outside an exact-rank-three form.

## 6. Designated partner fleet04/B01 applied to the new inequality

The completed designated-partner theorem `QFORM-SIGNED-FEJER-EXACT-INTERFACE-v1` proves that for any probability law `mu`,

`D_T mu(y)
 =(1/(2pi)) int_(-T)^T (1-|t|/T)
   Re(exp(-ity) phi_mu(t)) dt`

obeys

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`                  (6.1)

whenever `mu` has a bounded density, and conversely a uniform Fejer cap gives such a density. The canonical partner proof is

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

Applying (6.1) to Theorem 5.1 gives the actual averaged-frequency statement

`sup_(T>0,y) D_T law(Q)(y)
 <=C_null eta^(-1/4)|det Lambda|^(-1/4)
 <=C_null<34.029`.                                                (6.2)

Thus this run pays the correct signed averaged-frequency quantity on a nontrivial zero-pivot branch without invoking the false law-uniform pointwise phase decay or absolute Fourier `L^1` integrability. Continuity is proved separately here by the conditional convolution argument, not inferred from the Fejer cap alone.

## 7. Source-valid dependencies and newer correction applied

The product-projection cap used in (5.7) is the proved theorem from

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

The newer scalar-conditioning correction consumed is fleet01/B01 run `20260922T180807Z-b01-qform-auto11`, canonical mathematics

`yspennstate/math-open-problems@98dd994e199fbaa8c0b0600258c76fc57a15dc88:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260922T180807Z-b01-qform-auto11/`.

Its Hadamard four-variable construction has `sup_b ||p_(Q3|Q'=b)||_infinity=infinity` while the full output density stays bounded. The present proof does not take that false supremum; its conditional singular cap is retained with its exact `p_L(l)` weight and integrated in (4.6).

## 8. Diagnostics

The determinant geometry in (5.9)--(5.10) was independently stress-checked during this run on 10,000 randomly rotated indefinite `3x3` spectral matrices with eigenvalue magnitudes in `[1,21]` and explicit unit null vectors. Maximum relative error in

`det Lambda = -eta^2 b22`

was below `4.2e-15`; the smallest observed `eta` was above `1.11`. This is a numerical diagnostic only; the proof is the exact expansion in (5.10).

The explicit universal constant is

`C_null=34.02845882612358...`.

## 9. Remaining first implication

The full conjecture remains open. The next zero-pivot obligation is now narrower:

**extend the bilinear-plus-square mechanism from a unit-leverage null row to a quantitative high-leverage / near-null outer-pivot branch, or prove a product-preserving dichotomy sending the complementary low-leverage branch into the already paid diffuse/ridge/grouped-coordinate mechanisms.**

A successful extension must retain arbitrary additional spectrum or explicitly bridge it afterward. It may not replace the exact conditional averaging by `sup_b`, use pointwise Fresnel decay, assume a uniformly good physical minor, or rotate the independent variables and keep independence.
