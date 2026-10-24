SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B15, 2026-09-23T03:25:45Z.
attacking: target-level regularity lemma — replace the central density/heat value by an exact positive annular functional that vanishes at the critical level and preserves the universal constant.

# account03/B15 auto11 — exact annular positive-kernel normal form

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** absolute continuity and regularity  
**Run:** `20260923T032545Z-account03-B15-qform-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_ANNULAR_HEIGHT_NORMAL_FORM / UNIVERSAL_HEIGHT_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Result

The unrestricted universal QFORM density-height conjecture remains **OPEN**. This run proves an exact, zero-loss positive regularization normal form that is more annular than the Gaussian heat functional: the testing kernels can be chosen to vanish in a neighborhood of the critical level (compact shell version), or vanish quadratically exactly at the critical level (smooth Gaussian-annular version).

For any probability law `mu` on R, with the extended convention `||p_mu||_infinity=+infinity` when `mu` has no bounded density,

`boxed{ ||p_mu||_infinity = sup_{r>0,y} P(r<|Z-y|<2r)/(2r) }`.

Also, with

`gamma_epsilon(u)=(sqrt(2pi) epsilon)^(-1) exp(-u^2/(2 epsilon^2))`

and

`A_epsilon(y)=E[ ((Z-y)^2/epsilon^2) gamma_epsilon(Z-y) ]`,

we have

`boxed{ ||p_mu||_infinity = sup_{epsilon>0,y} A_epsilon(y) }`.

Thus the full QFORM conjecture with constant `C` is exactly equivalent, without constant loss and without assuming density existence in advance, to either one of the two positive inequalities

`P(r<|X^T A X-y|<2r) <= 2 C r`

for all `r>0,y`, or

`E[ ((X^T A X-y)^2/epsilon^2) gamma_epsilon(X^T A X-y) ] <= C`

for all `epsilon>0,y`.

The second integrand is zero at the exact critical level `Q=y`; the first completely removes the inner band `|Q-y|<=r`. This does not solve the universal bound, but it supplies a precise target-level regularity lemma and a new proof interface that does not ask for a uniform continuity modulus, pointwise oscillatory decay, or a worst conditional density cap.

## 2. General positive approximate-identity height lemma

Let `k>=0` be an `L^1(R)` probability density and

`k_epsilon(x)=epsilon^(-1) k(x/epsilon)`.

Assume the usual approximate-identity property, which holds for every fixed `k in L^1` under this scaling. For a probability measure `mu`, define

`M_k(mu)=sup_{epsilon>0,y in R} (mu*k_epsilon)(y)`.

Then

`boxed{ M_k(mu)=||p_mu||_infinity }`

in the extended sense.

### Proof: bounded-density direction

If `mu=p dx` and `||p||_infinity=M<infinity`, positivity and unit mass of `k_epsilon` give

`(p*k_epsilon)(y)<=M`

for every `epsilon,y`; hence `M_k(mu)<=M`.

At every Lebesgue point `y` of `p`, `p*k_epsilon(y)->p(y)` as `epsilon downarrow0`. For every `delta>0`, the set `{p>M-delta}` has positive measure when `M` is the essential supremum. Choosing a Lebesgue point in that set shows `M_k(mu)>=M-delta`. Let `delta downarrow0`.

### Proof: converse without pre-assumed absolute continuity

Suppose `M_k(mu)<=C<infinity`. Let

`mu_epsilon(dy)=(mu*k_epsilon)(y)dy`.

Then `mu_epsilon<=C dy`, and `mu_epsilon` converges weakly to `mu`. For every nonnegative `phi in C_c(R)`,

`int phi dmu = lim_{epsilon downarrow0} int phi dmu_epsilon <= C int phi dy`.

Therefore `mu<=C dy`; hence `mu=p dy` with `0<=p<=C` almost everywhere. This proves the extended equality as well: if `mu` has no bounded density, `M_k(mu)=+infinity`.

## 3. Compact annular shell criterion

Take

`rho(u)=(1/2) 1_{1<|u|<2}`.

Its integral is one, and

`rho_r(x)=(1/(2r)) 1_{r<|x|<2r}`.

The preceding lemma gives, for every probability law `mu`,

`boxed{ ||p_mu||_infinity = sup_{r>0,y} P(r<|Z-y|<2r)/(2r). }`

This may also be understood directly by dyadic shell summation. If

`P(r<|Z-y|<2r)<=L r`

for every `r,y`, then

`P(|Z-y|<R) <= sum_{j>=0} L R/2^{j+1}=L R`.

Hence the centered-interval density ratio is at most `L/2`, while a bounded density of height `M` trivially gives each shell mass at most `2Mr`. Thus the exact normalized shell functional is the density height.

For QFORM this yields the zero-loss equivalence

`boxed{ ||p_Q||_infinity<=C iff P(r<|Q-y|<2r)<=2Cr for all r,y. }`

The shell deliberately excludes the most singular inner region. Of course the exclusion does not make the theorem automatic: all dyadic shells together still reconstruct the central interval. What it does provide is a positive multiscale interface on which curvature can potentially be aggregated before the final dyadic summation.

## 4. Smooth annular Gaussian criterion

Let

`kappa(u)=u^2 gamma_1(u)`.

Because a standard Gaussian has second moment one,

`int kappa=1`.

Its scaled kernel is

`kappa_epsilon(x)=epsilon^(-1) kappa(x/epsilon)
                  =(x^2/epsilon^2) gamma_epsilon(x)`.

Therefore the positive approximate-identity lemma gives

`boxed{
||p_mu||_infinity
 = sup_{epsilon>0,y}
   E[ ((Z-y)^2/epsilon^2) gamma_epsilon(Z-y) ].
}`

The kernel is nonnegative, smooth and even, but unlike the Gaussian heat kernel itself it vanishes quadratically at `Z=y`.

At a single scale it also quantitatively sees the compact shell: for `1<=|u|/epsilon<=2`,

`(u^2/epsilon^2) gamma_epsilon(u)
 >= [4 e^(-2)]/[sqrt(2pi) epsilon]`.

Hence

`A_epsilon(y)
 >= [4 e^(-2)/(sqrt(2pi) epsilon)]
    P(epsilon<|Z-y|<2epsilon)`.

The exact supremum identity is stronger than this one-scale comparison, but the inequality can be useful when passing a shell estimate into the smooth positive functional.

## 5. Exact differential relation to the assigned partner heat theorem

The completed assigned partner result is account04/B15 r4:

- repository/commit: `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

It proves for every probability law `mu`

`boxed{ sup_{epsilon>0,y} H_epsilon(y)=||p_mu||_infinity }`,

where

`H_epsilon(y)=E gamma_epsilon(Z-y)`,

again with extended value `+infinity` if no bounded density exists.

The annular Gaussian functional is exactly its scale derivative:

`boxed{
partial_epsilon [ epsilon H_epsilon(y) ]
 = A_epsilon(y)
 = E[ ((Z-y)^2/epsilon^2) gamma_epsilon(Z-y) ] >=0.
}`

Indeed

`epsilon gamma_epsilon(u)=(2pi)^(-1/2) exp[-u^2/(2epsilon^2)]`,

whose epsilon derivative is `(u^2/epsilon^2) gamma_epsilon(u)`.

For every QFORM target in the owner's scope, `Q=X^T A X` is atomless before any density-height theorem is invoked. The product law of `X` is absolutely continuous on `R^n`, and for nonzero `A` every polynomial level set `{x:x^T A x=y}` has Lebesgue measure zero. Thus `P(Q=y)=0` for every `y`. Dominated convergence then gives

`lim_{delta downarrow0} delta H_delta(y)=0`.

Integrating the derivative identity from zero to `epsilon` yields the exact positive scale-average formula

`boxed{
H_epsilon(y)=epsilon^(-1) int_0^epsilon A_r(y) dr.
}`

This is the required direct application of the partner theorem to an actual inequality. If one can prove the target-level annular estimate

`A_r(y)<=C`

uniformly over all admissible `A`, product laws, `r`, and `y`, then the scale-average identity gives

`H_epsilon(y)<=C`

for every `epsilon,y`; the partner theorem immediately yields

`||p_Q||_infinity<=C`.

Conversely, once `||p_Q||_infinity<=C`, positivity and unit mass of `kappa_epsilon` give `A_epsilon(y)<=C`. Hence the annular and heat formulations have exactly the same optimal constant.

## 6. Absolutely convergent Fourier representation, without pointwise decay

With the convention `hat mu(t)=int exp(itx) dmu(x)`, the Fourier transform of `kappa_epsilon` is

`boxed{ (1-epsilon^2 t^2) exp(-epsilon^2 t^2/2). }`

Therefore

`A_epsilon(y)
 = (1/(2pi)) int_R e^{-ity}
   (1-epsilon^2 t^2)e^{-epsilon^2t^2/2}
   hat mu(t) dt`.

This integral is absolutely convergent solely because the displayed multiplier lies in `L^1` and `|hat mu|<=1`. No undamped Wiener norm and no law-uniform pointwise van-der-Corput estimate is assumed. The multiplier changes sign in frequency, but the physical-space kernel is positive.

## 7. Relation to B15's previous no-uniform-modulus obstruction

The previous B15 run proved that even for the fixed diagonal matrix `A=I_3`, smooth/analytic-Schwartz target outputs of uniformly bounded height need not have any common modulus of continuity, BV bound, or positive Sobolev bound. That obstruction remains fully compatible with the present theorem.

The annular criterion uses no target-uniform derivative control. It tests each scale by a positive mass functional and then invokes the exact heat-height closure. Thus it is a legitimate replacement mechanism after the regularity-upgrade route was refuted.

## 8. What remains unpaid

The universal conjecture is not proved here. The first unpaid implication is now the following exact positive statement:

`boxed{
E[ ((X^TAX-y)^2/r^2) gamma_r(X^TAX-y) ] <= C
}`

for one universal `C`, all target instances, all `r>0`, and all `y`.

Equivalently one may prove the compact-shell bound

`P(r<|X^TAX-y|<2r)<=2Cr`.

The potential advantage is structural rather than cosmetic: the central critical level has zero weight (or is removed entirely), so one can attempt to aggregate original-coordinate blocks/ridges on a fixed nonzero output shell before paying inverse-curvature or inverse-minor costs. Any such proof still must preserve the independent product provenance and survive all current correction examples.

## 9. Corrections and scope

This report uses none of the refuted intermediate claims. In particular it does not assume:

- uniform pointwise van-der-Corput decay;
- independence after spectral rotation;
- a dimension-free arbitrary fiber supremum;
- the false arbitrary-joint rank-three coarea bound;
- a positive moment bound for conditional projection densities;
- a uniformly conditioned physical minor or cross block;
- near-zero half-Riesz control from a cross-row norm alone.

The theorem is one-dimensional at the pushforward-law level and exact for every probability measure. Its application to QFORM is therefore safe with respect to signs, rotations, extra eigenvalues, and input irregularity. It establishes an exact bounded-density criterion; continuity remains a separate qualitative conclusion and is not inferred from the annular inequality alone.

Control refreshed before publication: live owner control revision `2026-09-22.15`; latest observed math-research-brain main at derivation time `cc53a86507772063a9c55a2f7c3d19e6eadaaa44`. Full QFORM status remains OPEN.
