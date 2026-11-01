# fleet03/B17 — quadratic-form density, rotated saddle-square smoothing

Status: **PROVED SUPPORTING THEOREM / FULL CONJECTURE OPEN**.

## Live target and correction state

The active owner target is the quadratic-form bounded-density conjecture: independent real `X_i` with densities `0<=f_i<=1`; real symmetric `A`; at least three eigenvalues of `A` have absolute value at least `1`; prove a dimension- and law-independent `L^infinity` bound for the density of `X^T A X`.

This run does **not** use the retired FEI assignment. It also does not use the false uniform pointwise stationary-phase claim. The current correction is essential: arbitrary disconnected density supports can phase-match `exp(i s x^2)`, so a pointwise law-independent `|s|^{-1/2}` bound is false.

I consumed the compatible fleet03/B16 result that for `Y=lambda Z^2`, with `Z` having density at most `1`,

`||p_Y||_{3/2} <= 2 |lambda|^{-1/3}`.

I then derived a complementary `L^p` theorem for the logarithmically singular opposite-sign saddle.

## Theorem 1 — product of two bounded-density variables is uniformly L^p

Let `X,Y` be independent real random variables with probability densities bounded by `1`, and let `W=XY`. For every `1<=p<infinity`, `W` has a density satisfying

`||p_W||_p <= A_p := 2^(-2/p) (p+1)^((p+1)/p)`.

In particular,

`||p_{XY}||_3 <= 4`.

### Proof

Split each input density into its positive and negative half-line pieces. It is enough first to treat two nonnegative pieces `alpha,beta` on `(0,infinity)`, with masses `m,n` and `0<=alpha,beta<=1`. Their product pushforward has density

`H(t)=int_0^infinity alpha(x) beta(t/x) dx/x`, `t>0`.

Set

`r=2p/(p+1)`, `A(x)=x^(1/p) alpha(x)`, `B(x)=x^(1/p) beta(x)`.

On the multiplicative group `(0,infinity)` with Haar measure `dx/x`,

`t^(1/p) H(t) = (A *_M B)(t)`.

Moreover

`||H||_{L^p(dt)} = ||A *_M B||_{L^p(dt/t)}`.

Young's convolution inequality applies because `1+1/p=2/r`:

`||H||_p <= ||A||_r ||B||_r`.

Now

`||A||_r^r = int_0^infinity x^(-(p-1)/(p+1)) alpha(x)^r dx`.

Since `0<=alpha<=1`, `alpha^r<=alpha`. The weight is decreasing, so the bathtub principle shows that, among densities capped by `1` with mass `m`, the right side is maximized by `alpha=1_[0,m]`. Hence

`||A||_r^r <= ((p+1)/2) m^(2/(p+1))`,

and therefore

`||A||_r <= ((p+1)/2)^((p+1)/(2p)) m^(1/p)`.

The same holds for `B`, giving each sign-pair branch

`||H||_p <= ((p+1)/2)^((p+1)/p) (mn)^(1/p)`.

For the full real product, the positive density is the sum of the `++` and `--` branches and the negative density the sum of the `+-` and `-+` branches. Using `(a+b)^p<=2^(p-1)(a^p+b^p)` and summing the four quadrant mass products, whose total is `1`, yields

`||p_{XY}||_p^p <= 2^(p-1) ((p+1)/2)^(p+1)`.

Taking the `p`-th root gives exactly

`||p_{XY}||_p <= 2^(-2/p)(p+1)^((p+1)/p)`.

For `p=3`, the constant is `4`. QED.

## Theorem 2 — square term in the dual range

For completeness, the B16 square estimate extends to every `1<=q<2`:

`||p_{lambda Z^2}||_q <= B_q |lambda|^(-1+1/q)`,

where

`B_q = 2^(1-1/q) (2-q)^(-1/q)`.

Indeed, for `lambda=1`, writing `h(x)=f_Z(x)+f_Z(-x)` for `x>0`, one has `0<=h<=2`, `int h=1`, and

`p_{Z^2}(y)=h(sqrt(y))/(2 sqrt(y))`.

Thus

`int p_{Z^2}(y)^q dy = 2^(1-q) int h(x)^q x^(1-q) dx <= int h(x) x^(1-q) dx`.

The decreasing weight is maximized by `h=2 1_[0,1/2]`, giving `2^(q-1)/(2-q)`. Taking the `q`-th root and scaling by `lambda` proves the claim. At `q=3/2`, `B_q=2`, recovering the consumed B16 theorem.

## Theorem 3 — exact smoothing of the opposite-sign saddle by one square

Let `X,Y,Z` be independent, with all three densities bounded by `1`. Let `c,lambda` be nonzero. Then for every `p>2`, with `q=p/(p-1)`, the random variable

`T = c X Y + lambda Z^2`

has a bounded density and

`||p_T||_infinity <= C_p |c|^(-(p-1)/p) |lambda|^(-1/p)`,

where

`C_p = 2^(-1/p) (p+1)^((p+1)/p) ((p-1)/(p-2))^((p-1)/p)`.

Proof: scaling Theorem 1 gives

`||p_{cXY}||_p <= A_p |c|^(-(p-1)/p)`.

Theorem 2 gives

`||p_{lambda Z^2}||_q <= B_q |lambda|^(-1/p)`.

Since the two summands are independent, Young/Hölder convolution `L^p * L^q -> L^infinity` gives the stated product constant.

At the clean choice `p=3`,

`||p_{cXY+lambda Z^2}||_infinity <= 8 |c|^(-2/3) |lambda|^(-1/3)`.

### Canonical rotated three-eigenvalue stress form

Take

`Q = 2 X Y + Z^2`.

Its symmetric matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`,

with eigenvalues `+1,-1,+1`, so it sits exactly at the three-large-eigenvalue threshold and is genuinely non-diagonal in the independent coordinates. The theorem gives

`||p_Q||_infinity <= 8*2^(-2/3) = 2^(7/3) < 5.04`

for **all** independent input laws with density at most `1`.

This is the sharp qualitative control case that the full proof must respect: `2XY` alone has the familiar logarithmic saddle singularity for centered uniform inputs, but one independent square is enough to turn it into a universally bounded density.

For the exact centered-uniform stress law `X,Y,Z ~ Uniform[-1/2,1/2]`,

`p_{2XY}(u)=log(1/(2|u|))`, `|u|<1/2`,

and

`p_{Z^2}(v)=v^(-1/2)`, `0<v<1/4`.

Therefore at the saddle point,

`p_Q(0)=int_0^(1/4) v^(-1/2) log(1/(2v)) dv = 2+log 2`.

This exact rotated witness is below the already-known diagonal `pi` control, so it does not improve the global lower bound on the best universal constant; its value is structural, not extremal.

## Linear terms and conditioning extension

The same bound survives arbitrary linear terms in these three variables. Indeed

`cXY+aX+bY = c (X+b/c)(Y+a/c) - ab/c`,

and

`lambda Z^2+dZ = lambda (Z+d/(2lambda))^2 - d^2/(4lambda)`.

Coordinate translations preserve independence and the density cap.

Consequently, if after conditioning on all other independent coordinates a quadratic form has a three-coordinate principal block

`[[0,c/2,0],[c/2,0,0],[0,0,lambda]]`,

then all couplings from those three coordinates to the conditioned coordinates become only linear terms, and the same conditional `L^infinity` bound holds uniformly. Mixing over the conditioned coordinates preserves the bound. Thus arbitrary outside couplings are allowed for this exact saddle-square principal-block subclass.

## What this closes and what remains

**Closed branch:** the sharp rank-two opposite-sign logarithmic singularity is not an obstruction once an independent square direction is present in the exact coordinate saddle-square geometry. The regularization can be proved without false pointwise stationary phase, using multiplicative `L^p` smoothing plus the square `L^q` estimate.

**Still open:** the spectral hypothesis of the full conjecture does not guarantee a coordinate principal block of the above saddle-square form. A general orthogonal diagonalization destroys independence. The next missing implication is a dimension-free structural or mixed-norm lemma that extracts a comparable product-measure smoothing mechanism from an arbitrary symmetric matrix with three singular eigenvalues at least `1` while retaining the independent-coordinate structure.

Full quadratic-form conjecture: **OPEN / NOT PROVED**.

## Provenance

Consumed compatible peer result: fleet03/B16, run `20260922T113226Z-qform-r11`, square `L^(3/2)` estimate and the correction refuting pointwise one-dimensional stationary-phase decay. At the fresh read there was no completed fleet04/B17 artifact yet on the new quadratic-form programme; its visible B17 outputs were from the superseded FEI programme, so they were not imported as if compatible.

Brain status: `WITHOUT_VERIFIED_BRAIN`; authenticated repository control/state was used, but native brain retrieval/ingestion was not verified.
