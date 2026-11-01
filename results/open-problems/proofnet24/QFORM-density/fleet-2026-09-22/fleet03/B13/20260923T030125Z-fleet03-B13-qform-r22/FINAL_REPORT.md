SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-23T03:01:25Z.
attacking: extremal-product transfer plus aggregate cross-three-volume smoothing through one original scalar pivot.

# fleet03/B13 r22 final report

Programme `QFORM-DENSITY-3EIG-20260922`; live owner control revision `2026-09-22.15`. Execution `WITHOUT_VERIFIED_BRAIN`. Full QFORM and the full continuity conclusion remain OPEN.

This final report incorporates `REPORT.md` and `ADDENDUM_SHARPENING.md`, including the same-run predecessor reconciliation. No moment, support, connectedness, Gaussian, log-concavity, diagonal-basis, or post-rotation-independence assumption is added.

## 1. Sources actually consumed

- fleet03/B13 r21, cross-three-volume `L3` theorem: `yspennstate/math-open-problems@77bd4ea475a11a505c6990630cbdfebdcce0fd8f`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T013555Z-fleet03-B13-qform-r21/REPORT.md`. If an ORIGINAL-coordinate cross block `M` has `Z=e_3(M^TM)>0`, then the full quadratic-affine output has `||p||_3<6.787 Z^(-1/9)`, with arbitrary same-side terms/outside couplings.
- fleet03/B13 r20 plus fleet03/B06 one-row/E2 envelope, assembled in r21: either an `Linfinity` paid three-volume branch holds, or a physical hub supplies a `|t|^(-3/4)` characteristic-function envelope at aggregate currency.
- designated partner fleet04/B13 no-attainment purification: `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T231352Z-fleet04-B13-rough-geometric-transfer-r5/REPORT.md`. Uniform product-indicator slab bounds transfer with zero loss to arbitrary independent cap-one laws; no optimizer, bounded diameter, or bounded fragment count is assumed.
- fleet03/B06 r24, `yspennstate/math-open-problems@6fb28b3e367d9cd8bf1dff3a4ca05b500d5d32c8`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T011959Z-fleet03-B06-qform-r24/REPORT.md`: a dependence-safe one-sided square kernel and an earlier `L3` half-Riesz transducer.
- predecessor fleet02/B13, same snapshot commit/path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T025607Z-fleet02-B13-extreme-cf3f0909/REPORT.md`: it already proved the qualitative scalar-Schur/cross-three-volume gluing with constant `20.870` and the anchored bordered-four-volume identity. This run therefore claims only the quantitative sharpening and the separate three-quarter slab theorem below.

## 2. New direct three-quarter slab estimate from aggregate cross three-volume

Let `M` be any ORIGINAL-coordinate cross block of a quadratic polynomial in independent cap-one coordinates and let

`Z=e_3(M^TM)>0`.

Then for every interval `J`,

`boxed: P(Q in J)<14.486 Z^(-1/8)|J|^(3/4).`                       (2.1)

Proof. For any `L>0`, the r20/r21 dichotomy gives either

`||p_Q||inf <=6 sqrt(e) exp(L/6) Z^(-1/6)`,                       (2.2)

or a hub currency `kappa>=((1-exp(-L))/6)Z` together with

`|phi_Q(t)|<=C0 kappa^(-1/8)|t|^(-3/4)`,
`C0=2^(-1/2)pi^(3/4)e^(5/8)`.                                    (2.3)

In the first branch, `min(1,x)<=x^(3/4)` gives the `|J|^(3/4)` scale. In the second, if `h=|J|` and `c` is its midpoint,

`1_J(x)<=e^(1/8)exp(-(x-c)^2/(2h^2))`.

Fourier inversion against this Gaussian gives

`P(Q in J)<=G C0 kappa^(-1/8)h^(3/4)`,
`G=e^(1/8)2^(1/8)Gamma(1/8)/sqrt(2pi)=3.71405110123522...`.       (2.4)

Equating the two branch constants gives

`L*=7.634462637351169...`

and common constant `14.485199899718856...`, proving (2.1). No pointwise scalar van-der-Corput estimate is used.

## 3. New sharp one-sided `L3` half-Riesz transducer

If `p` is a probability density with `||p||_3<=M`, then

`boxed:
 sup_t int_0^infinity p(t-u)u^(-1/2)du
 <=2 sqrt(pi/sqrt(3)) M^(3/4).}`                                  (3.1)

The same holds with `p(t+u)`. The constant is

`2 sqrt(pi/sqrt(3))=2.693547374177197...`,

improving the earlier fleet03/B06 r24 split-at-radius constant `8/3^(3/4)=3.5095307012...`.

Proof. For `lambda>0`,

`u^(-1/2)<=lambda+(u^(-1/2)-lambda)_+` on `u>0`.                 (3.2)

Using total mass one for the first term and Holder `(3,3/2)` for the second,

`I<=lambda+M(3pi/4)^(2/3)lambda^(-1/3)`,                          (3.3)

because

`int_0^infinity (u^(-1/2)-lambda)_+^(3/2)du=(3pi/4)lambda^(-1/2)`. (3.4)

Optimizing (3.3) gives (3.1).

## 4. Sharpened scalar-Schur / aggregate-three-volume density branch

Choose an ORIGINAL coordinate `i` with `a=A_ii!=0`. Write the quadratic-affine form as

`Q=a x_i^2+2x_i(c^Tz+beta)+z^TBz+2d^Tz+gamma`.

Complete only this original scalar square:

`Q=a(x_i+(c^Tz+beta)/a)^2+R(z)`,                                  (4.1)

where the quadratic matrix of `R` is the Schur complement

`S=B-a^(-1)cc^T`.                                                   (4.2)

The residual coordinates `z` remain independent. Choose disjoint ORIGINAL-coordinate residual sets `I,J` and put

`M=S[I,J]`, `Z=e_3(M^TM)>0`.                                       (4.3)

The dependence-safe square kernel gives

`p_Q(t)<=|a|^(-1/2) int_0^infinity
 p_R(t-sgn(a)u)u^(-1/2)du`.                                        (4.4)

Apply r21 to `R`, then (3.1):

`boxed:
 ||p_Q||inf
 <11.327 |a|^(-1/2)Z^(-1/12).}`                                   (4.5)

The computed safe constant is

`2 sqrt(pi/sqrt(3))*6.787^(3/4)=11.326168157432749...`.             (4.6)

If `s_3(M)>=sigma`, then `Z>=sigma^6` and

`||p_Q||inf<11.327(|a|sigma)^(-1/2)`.                              (4.7)

The predecessor fleet02/B13 identity converts (4.5) to a pure original-matrix aggregate certificate. Define

`W_i(I,J)=sum_{|S0|=|T0|=3}
 det A[{i} union S0,{i} union T0]^2`,                              (4.8)

with `S0 subset I`, `T0 subset J`. The block determinant identity gives

`W_i(I,J)=a^2 Z`,                                                   (4.9)

hence

`boxed:
 ||p_Q||inf
 <11.327 (|A_ii|^4 W_i(I,J))^(-1/12).}`                           (4.10)

This pays the full aggregate bordered four-volume before taking a reciprocal power; it does not select one small minor.

## 5. Exact arbitrary-law transfer using the designated fleet04/B13 theorem

First prove (4.5) for arbitrary bounded finite-union unit-measure product indicators. Then for every interval `J0`,

`P(Q in J0)<11.327 |a|^(-1/2)Z^(-1/12)|J0|`.                     (5.1)

Apply fleet04/B13 Corollary 2.2 to `K=1_{Q in J0}`. Its no-attainment supremum identity transfers (5.1), with zero loss, to every independent probability density `0<=f_i<=1`. Thus (4.5) and (4.10) hold for arbitrary fragmented/unbounded one-dimensional laws. No single interval, centered law, support-radius bound, or fragment-count bound is imposed.

This yields an essentially bounded density in the stated branch. Continuity is not proved by this transducer/mixture argument.

## 6. Remaining structural obligation

The full conjecture remains OPEN. A divergent no-pivot sequence not already covered by another branch must force

`|A_ii|^4 W_i(I,J)->0`                                             (6.1)

for every nonzero original scalar pivot `i` and every residual disjoint physical cut `(I,J)`, otherwise (4.10) gives a uniform bound.

The next B13 obligation is therefore to show that simultaneous collapse of all currencies (6.1) forces one of the already-paid row-diffuse volume-stability, exact/near-null coloop, rank-two tube/grouped-bank, determinant-pair, mixed-hub/Fresnel, or finite-core mechanisms. Small matrix coefficients cannot simply be discarded as small random errors on arbitrary unbounded supports.

The exact-null endpoint `A_ii=0` remains outside (4.5) and must be handled by its separate exact/near-null mechanisms.

## 7. Checks and status

`CHECK_OUTPUT.txt` verifies the `14.486` optimization. `CHECK_SHARPENED.txt` verifies

- `3pi/4=2.356194490192345...` in (3.4);
- one-sided half-Riesz constant `2.693547374177197...`;
- safe final scalar-Schur constant `11.326168157432749... <11.327`.

These are arithmetic checks only; the analytic proofs are above.

Full QFORM: **OPEN / NOT PROVED**.  
Full continuity: **OPEN / NOT PROVED**.
