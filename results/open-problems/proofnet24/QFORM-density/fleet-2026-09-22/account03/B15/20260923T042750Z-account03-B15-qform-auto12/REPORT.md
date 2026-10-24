SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B15, 2026-09-23T04:27:50Z.
attacking: punctured positive-heat hierarchy — arbitrary-order vanishing kernels with exact zero-loss recovery of Gaussian heat height.

# account03/B15 auto12 — arbitrary-order punctured heat kernels with exact height recovery

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** absolute continuity and regularity  
**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_PUNCTURED_HEAT_HIERARCHY / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and first unpaid implication

The full target remains open: for independent real coordinates with densities `0<=f_i<=1` and symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal bound on the density of `Q=X^T A X`, or give a valid counterexample.

The completed account04/B15 heat-height theorem gives, for every probability law `mu`,

`sup_{epsilon>0,y} (mu*gamma_epsilon)(y)=||p_mu||_infinity`,

with value `+infinity` if no bounded density exists. The first unpaid implication is therefore a dimension-, matrix-, law-, center-, and scale-uniform bound on that positive heat functional.

The previous B15 run replaced the heat kernel by one quadratic-zero annular Gaussian kernel. Here I push that mechanism to arbitrary order and prove an exact positive scale-mixture identity. This gives a family of equivalent target tests whose physical kernels vanish to any prescribed even order at the tested level. The point is not that this by itself pays the remaining two-sheet/product-geometry obstruction; it gives a more flexible exact interface for trying to pay that obstruction before a reciprocal local-minor cost appears.

## 2. The punctured Gaussian hierarchy

For `m>=0`, let

`c_m=(2m-1)!!`, with `c_0=1`,

and define

`kappa_{m,epsilon}(u)
 = (1/c_m) (u/epsilon)^(2m) gamma_epsilon(u)`,

where

`gamma_epsilon(u)=(sqrt(2*pi) epsilon)^(-1) exp(-u^2/(2 epsilon^2))`.

Because a standard Gaussian has even moment `E Z^(2m)=c_m`, every `kappa_{m,epsilon}` is a probability density. It is even and nonnegative. For `m>=1` it vanishes at `u=0` to order exactly `2m`.

Equivalently, under the probability density `kappa_{m,epsilon}`, the random radius `|U|/epsilon` has the chi distribution with `2m+1` degrees of freedom. Thus these are genuinely punctured/shell-weighted positive kernels, not signed derivatives masquerading as a positive test.

For a finite positive measure `mu`, write

`H_m(epsilon,y)=(mu*kappa_{m,epsilon})(y)`.

The case `m=0` is the ordinary Gaussian heat profile.

## 3. Exact scale differential recursion

Put `z=u^2/epsilon^2` and `D=epsilon partial_epsilon`. Since

`D z=-2z`,

and

`D gamma_epsilon=(z-1) gamma_epsilon`,

we obtain

`D(z^(m-1) gamma_epsilon)
 = [z-(2m-1)] z^(m-1) gamma_epsilon`.

Using `c_m=(2m-1)c_(m-1)` gives the exact kernel identity

`(D+2m-1) kappa_{m-1,epsilon}
 = (2m-1) kappa_{m,epsilon}`.

Equivalently,

`boxed{
partial_epsilon [epsilon^(2m-1) kappa_{m-1,epsilon}(u)]
 = (2m-1) epsilon^(2m-2) kappa_{m,epsilon}(u).
}`

After convolution,

`boxed{
partial_epsilon [epsilon^(2m-1) H_{m-1}(epsilon,y)]
 = (2m-1) epsilon^(2m-2) H_m(epsilon,y).
}`

For `m>=2` the boundary term at epsilon down to zero vanishes for every finite measure because `||kappa_{m-1,epsilon}||_infinity=O(epsilon^(-1))`, hence `epsilon^(2m-1) H_{m-1}=O(epsilon^(2m-2))`.

For `m=1`,

`epsilon H_0(epsilon,y)
 = (1/sqrt(2*pi)) int exp(-(x-y)^2/(2epsilon^2)) dmu(x)`.

This tends to `mu({y})/sqrt(2*pi)`. Therefore it vanishes whenever `mu` is atomless.

Thus for every atomless finite positive measure,

`boxed{
H_{m-1}(epsilon,y)
 = (2m-1) epsilon^(-(2m-1))
   int_0^epsilon r^(2m-2) H_m(r,y) dr.
}`

This already shows that any uniform bound on `H_m` propagates downward with no constant loss.

## 4. Exact positive scale-mixture formula

The recursion can be iterated explicitly. Set

`a_m = c_m/[2^(m-1)(m-1)!]`.

Then

`w_{m,epsilon}(r)
 = (a_m/epsilon) (1-r^2/epsilon^2)^(m-1) 1_(0,epsilon)(r)`

is a probability density on `(0,epsilon)`. Indeed

`int_0^1 (1-s^2)^(m-1) ds
 = sqrt(pi) Gamma(m)/(2 Gamma(m+1/2))`,

while

`c_m=2^m Gamma(m+1/2)/sqrt(pi)`.

For every `u!=0`, direct substitution `t=u^2/(2r^2)` gives

`boxed{
 gamma_epsilon(u)
 = int_0^epsilon w_{m,epsilon}(r) kappa_{m,r}(u) dr.
}`

A direct verification is short. The right-hand side equals

`a_m epsilon^(-1) c_m^(-1) (2*pi)^(-1/2) u^(2m)
 int_0^epsilon r^(-2m-1)
 (1-r^2/epsilon^2)^(m-1)
 exp(-u^2/(2r^2)) dr`.

With `t=u^2/(2r^2)` and `a=u^2/(2epsilon^2)`, the integral becomes

`2^(m-1) exp(-a) Gamma(m)`.

The chosen value of `a_m` leaves exactly

`(sqrt(2*pi) epsilon)^(-1) exp(-u^2/(2epsilon^2))`.

At `u=0` the pointwise identity fails because every punctured kernel is zero there while the Gaussian is not. Therefore after convolution the identity is exact for every atomless `mu`:

`boxed{
H_0(epsilon,y)
 = int_0^epsilon w_{m,epsilon}(r) H_m(r,y) dr.
}`

The earlier quadratic-zero identity is the case `m=1`, where `w=1/epsilon`. The first genuinely stronger instance is

`boxed{
H_0(epsilon,y)
 = (3/(2epsilon)) int_0^epsilon
   (1-r^2/epsilon^2) H_2(r,y) dr,
}`

with

`kappa_{2,r}(u)=u^4 gamma_r(u)/(3r^4)`.

So an exact quartic-zero positive test recovers ordinary heat by a positive average and loses no constant.

## 5. Target laws are atomless before any density-height theorem

For the QFORM target, `A` has rank at least three and in particular `A!=0`. For every fixed `y`, the level set

`{x in R^n : x^T A x = y}`

is the zero set of a nonconstant real polynomial and has Lebesgue measure zero. The product input law has a Lebesgue density `prod_i f_i`. Hence

`P(X^T A X=y)=0`

for every `y`.

Thus the atomless hypothesis needed for the exact positive scale-mixture identity is automatic under the owner target and does not assume the desired bounded density.

## 6. Application of the assigned account04/B15 theorem

The completed assigned-partner theorem is:

`yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

It proves

`sup_{epsilon>0,y} H_0(epsilon,y)=||p_mu||_infinity`,

with `+infinity` if `mu` has no bounded density.

Apply the new positive scale-mixture identity. If for some fixed `m>=1`

`sup_{r>0,y} H_m(r,y) <= C`,

then for every `epsilon,y`,

`H_0(epsilon,y)
 <= int_0^epsilon w_{m,epsilon}(r) C dr
 = C`.

The partner theorem therefore gives the actual inequality

`boxed{ ||p_mu||_infinity <= C. }`

Conversely, if `mu=p dx` with `||p||_infinity<=C`, convolution by the probability density `kappa_{m,epsilon}` gives `H_m<=C`. If `mu` has no bounded density, the partner theorem gives `sup H_0=+infinity`, while the positive mixture implies `sup H_m>=sup H_0=+infinity`.

Therefore for every atomless probability law, and in particular every QFORM target law,

`boxed{
 sup_{epsilon>0,y} H_m(epsilon,y)
 = sup_{epsilon>0,y} H_0(epsilon,y)
 = ||p_mu||_infinity
}`

for every integer `m>=1`, with `+infinity` under failure of bounded density.

This is a zero-loss target equivalence, not a one-way regularization estimate.

## 7. Fourier form

With the convention `hat f(t)=int exp(i t u)f(u)du`, multiplication by `u^(2m)` gives

`hat kappa_{m,epsilon}(t)
 = [(-1)^m/c_m] He_(2m)(epsilon t)
   exp(-(epsilon t)^2/2)`,

where `He_k` is the probabilists' Hermite polynomial. The multiplier is absolutely integrable for every `m`; no undamped Wiener norm or pointwise van-der-Corput estimate is being assumed.

Examples:

`m=1: (1-epsilon^2 t^2) exp(-epsilon^2 t^2/2)`;

`m=2: (1-2 epsilon^2 t^2 + epsilon^4 t^4/3)
       exp(-epsilon^2 t^2/2)`.

Thus one may choose an arbitrarily high physical zero at the tested output level while retaining a Gaussian-damped Fourier interface and the exact same sharp density constant.

## 8. Compact end-to-end conditional target

For every fixed integer `m>=1`, the full QFORM conjecture with constant `C` is exactly equivalent to

`boxed{
E [ ((X^T A X-y)/epsilon)^(2m)
    gamma_epsilon(X^T A X-y) ]
 <= c_m C
}`

for every admissible `n,A`, every cap-one product law, every center `y`, and every scale `epsilon>0`.

For `m=2`, for example, it is enough — with no constant loss — to prove

`E [ (X^T A X-y)^4 gamma_epsilon(X^T A X-y) ]
 <= 3 C epsilon^4`.

Then the positive scale-mixture formula gives the ordinary heat bound `H_0<=C`, and the completed account04/B15 theorem gives `||p_Q||_infinity<=C`.

This is the first essential missing implication in a new form. It may be useful where the main obstruction is a local singular trace: the physical kernel now suppresses an arbitrarily high-order neighborhood of the tested level before any local inverse-curvature estimate is paid.

## 9. What this does not prove

The full universal constant is still open. In particular, the latest account02/B15 analysis correctly emphasizes that a free output center can move a bad interval into an annulus. Arbitrarily high vanishing at `Q=y` therefore does not, by itself, pay the minority/two-sheet branch or the no-uniform-single-minor structural glue. A proof still has to use original-coordinate product provenance before a dangerous curved trace or reciprocal minor is isolated.

The hierarchy also does not turn essential boundedness into continuity. The completed fixed-matrix `C_0` theorem is a separate qualitative regularity result. The universal height remains a distinct quantitative problem.

The result is compatible with all live corrections: it does not rotate independence, does not use arbitrary-joint coarea, does not use a conditional density-cap moment, does not use pointwise quadratic-phase decay, and does not take a fiber supremum.

## 10. Sources actually consumed

- fresh owner controls on `yspennstate/math-research-brain`, OWNER CONTROL revision `2026-09-22.15`;
- `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/account03/B15.json`;
- assigned partner account04/B15 heat-height theorem: `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`;
- latest account02/B15 minority/annular analysis: `yspennstate/math-open-problems@a7306ce944dac158ce39d8f8e224b6ce9d127b45`;
- latest account03/B20 aggregate-collar handoff, used only to keep the remaining global obstruction aligned with current fleet state.

No source-matching published theorem was located in the limited literature search performed during this run; no novelty claim is made from that search miss.
