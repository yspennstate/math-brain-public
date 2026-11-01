SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-23T06:03:54Z.
attacking: target-level absolute-continuity/regularity reduction; apply fleet02/B15 to a quantitative inequality without rotated independence.

# fleet01/B15 auto11 — fixed-height Poisson/Stieltjes normal form, one-sheet resolvent payment, and non-uniform desmoothing obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Absolute continuity and regularity  
**Status:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_REGULARITY_LEMMA / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and preserved corrections

The full owner target remains OPEN. For every dimension, every product law with independent one-dimensional densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, the required theorem is one dimension- and law-independent bound on the density of

`Q=X^T A X`.

Continuity is stronger and is kept separate.

This run uses no law-uniform pointwise quadratic Fourier decay, no independence after an orthogonal rotation, and no generic projection/X-ray shortcut on the minority two-sheet trace. It uses only original-coordinate conditioning when invoking a physical block.

A previous B15 report proved the general Poisson identity for a single scalar probability measure,

`D(mu)=sup_{eta>0,y} (P_eta*mu)(y)`,

where `D(mu)=sup_I mu(I)/|I|` and

`P_eta(u)=eta/[pi(u^2+eta^2)]`.

The new step below combines that measure-level criterion with the exact spectral homogeneity of the QFORM class and eliminates the smoothing-scale parameter entirely. This produces a fixed-imaginary-height Stieltjes target that, unlike an approximate-identity argument, does not assume a density exists beforehand.

## 2. Measure-level Poisson criterion, in the form needed here

Let `mu` be any finite positive Borel measure on `R`. If

`sup_{0<eta<=1, y in R} (P_eta*mu)(y) <= M`,

then

`mu <= M dx`.

Indeed `mu_eta=(P_eta*mu)(y)dy` converges weakly to `mu` as `eta downarrow0`. For every nonnegative `varphi in C_c(R)`,

`int varphi dmu = lim_eta int varphi(y)(P_eta*mu)(y)dy <= M int varphi(y)dy`.

Hence `mu<=M dx` by regularity/Riesz representation. The converse is immediate because `P_eta` is positive and has mass one.

Thus this is an **absolute-continuity plus L-infinity criterion**. No prior density or continuity representative is required.

## 3. New theorem: exact fixed-height Poisson normal form

For an admissible matrix put

`s(A)=s_3(A)`,

the third largest singular/eigenvalue modulus. Under the owner target `s(A)>=1`.

Let `C_* in [0,infinity]` denote the optimal universal QFORM density constant, with `+infinity` if the theorem fails. Define

`R_* = sup_{admissible (A,X), y in R} s(A) (P_1*mu_Q)(y)`.

### Theorem 3.1 — `QFORM-FIXED-HEIGHT-POISSON-NORMAL-FORM-v1`

`boxed{ C_* = R_* }`.

Equivalently,

`boxed{
 C_* = sup_{A,X,y} [s_3(A)/pi] E[ 1/(1+(X^T A X-y)^2) ].
}`

This identity is valid in the extended sense and does not assume absolute continuity in the direction `R_*<infinity => QFORM`.

### Proof: `R_*<=C_*`

Assume first that `C_*<infinity`. Fix an admissible `A` and write `s=s(A)`. Normalize

`B=A/s`, so `s_3(B)=1`, and `Q_B=Q_A/s`.

By definition of `C_*`, `mu_{Q_B}` has density at most `C_*`. The exact Poisson scaling is

`P_{1/s}(q/s-y/s)=s P_1(q-y)`.

Therefore

`s(P_1*mu_{Q_A})(y)
 = (P_{1/s}*mu_{Q_B})(y/s)
 <= C_*`.

Taking the supremum gives `R_*<=C_*`.

### Proof: `C_*<=R_*` without assuming a density

Assume `R_*<infinity`. Fix any admissible `A`, put `s=s(A)`, and let `0<eta<=1`. The scaled matrix

`A_eta=A/eta`

is still admissible and has `s(A_eta)=s/eta`. Its output is `Q_eta=Q/eta`. The scaling identity

`P_1(q/eta-y/eta)=eta P_eta(q-y)`

gives

`(s/eta)(P_1*mu_{Q/eta})(y/eta)
 = s(P_eta*mu_Q)(y)
 <= R_*`.

Hence for every `0<eta<=1`,

`(P_eta*mu_Q)(y) <= R_*/s <= R_*`.

The measure-level Poisson criterion of Section 2 now implies

`mu_Q <= (R_*/s) dx`.

Thus every target law is automatically absolutely continuous and

`||p_Q||_infinity <= R_*/s <= R_*`.

Taking the universal supremum yields `C_*<=R_*`, completing the proof.

### Consequence

The fixed-height quantity is actually scale-sharp:

`||p_Q||_infinity <= R_*/s_3(A)`

whenever the fixed-height resolvent supremum is `R_*`. In particular the owner target at threshold `s_3(A)>=1` follows with the same constant.

This is stronger logically than first proving absolute continuity and then estimating the density: the positive fixed-scale inequality itself would create the bounded density.

## 4. Exact Stieltjes/resolvent formulation

For `Im z>0` define

`m_Q(z)=E[(Q-z)^(-1)]`.

At the single imaginary height `1`,

`Im m_Q(y+i)=E[1/((Q-y)^2+1)]`.

Therefore Theorem 3.1 is exactly

`boxed{
 C_* = (1/pi) sup_{A,X,y} s_3(A) Im m_Q(y+i).
}`

Only **one horizontal line in the upper half-plane** is needed. The usual all-scale boundary supremum has been absorbed by spectral homogeneity.

There is also the exponentially damped Fourier representation

`(P_1*mu_Q)(y)
 = (1/pi) int_0^infinity e^{-t} Re( e^{-ity} phi_Q(t) ) dt`.

This identity uses cancellation and exponential damping. It is not the refuted estimate `int |phi_Q(t)|dt<infinity`, and it does not assert any law-uniform pointwise decay of `phi_Q`.

Equivalently, if `C_0` is an independent standard Cauchy variable, then

`P_1*mu_Q`

is the density of `Q+C_0`. Thus the full sharp problem is exactly the fixed-noise statement

`sup s_3(A) ||p_{Q+C_0}||_infinity < infinity`,

with the same optimal constant. This is an analytic regularization of the output, but the multiplier `s_3(A)` is essential.

## 5. Target-level regularity of the fixed-height profile

For every probability measure `mu`, without any density assumption,

`H_mu(y)=(P_1*mu)(y)`

belongs to `C^infinity(R)`. Moreover

`||H_mu||_infinity <=1/pi`,

and

`||H_mu'||_infinity <= ||P_1'||_infinity = 3sqrt(3)/(8pi)`.

Indeed

`P_1'(u)=-2u/[pi(1+u^2)^2]`,

whose absolute maximum occurs at `|u|=1/sqrt(3)`.

So the exact normal form replaces every rough output measure by a common smooth positive profile with an explicit law-independent modulus. This is **regularity of the fixed-height Poisson profile**, not a common modulus for the raw output densities.

For instance, on the adaptive grid `(delta/s) Z`, every center is within `delta/(2s)` of a grid point, hence

`s H_mu(y)
 <= sup_k s H_mu(k delta/s) + [3sqrt(3)/(16pi)] delta`.

Thus the center variable in the exact resolvent problem may be discretized at spectral mesh `1/s` with an arbitrarily small universal additive loss.

## 6. Completed assigned-partner result applied to the resolvent inequality

I apply the completed `fleet02/B15` theorem `QFORM-AMBIENT-PHYSICAL-3BLOCK-ONESHEET-v1`, from

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260923T030440Z-fleet02-B15-QFORM-auto11/REPORT.md`.

Let an ORIGINAL-coordinate physical `3 x 3` principal block `B` be invertible and indefinite, of signature `(2,1)` or `(1,2)`, and put

`kappa=min |eig(B)|`.

After conditioning on all outside ORIGINAL coordinates and completing the square only inside this physical block, the partner theorem gives a positive majority-sheet submeasure `nu_+` satisfying

`nu_+(I) <= (pi sqrt(2)/kappa)|I|`

for every interval `I`, uniformly in all outside quadratic coefficients, cross couplings, affine translations and rough cap-one marginals.

Therefore `nu_+ <= (pi sqrt(2)/kappa) dx`, and convolution with the unit Poisson kernel gives the actual fixed-height inequality

`boxed{
 s(A)(P_1*nu_+)(y)
 <= pi sqrt(2) s(A)/kappa.
}`

Writing `nu_-` for the conditional minority/two-sheet submeasure and averaging the conditioning,

`boxed{
 s(A)(P_1*mu_Q)(y)
 <= pi sqrt(2) s(A)/kappa
    + s(A)(P_1*nu_-)(y).
}`

Consequently, whenever `kappa>=c s(A)`, the entire majority contribution to the exact sharp resolvent target costs at most

`pi sqrt(2)/c`.

Only the minority/two-sheet Poisson term remains. This is an application to the exact new target functional, not merely a citation of qualitative regularity. It preserves original-coordinate independence and all outside curvature. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction remains fully active on `nu_-`.

## 7. New obstruction: no target-uniform Poisson desmoothing

The newest completed `fleet02/B15` run records a source-valid high-frequency family (ultimately from the completed phase-aligned construction): for arbitrarily large `tau`, with the fixed target matrix `A=I_3`, there are smooth compactly supported cap-one product sources whose output densities `p_tau` satisfy

- `supp p_tau subset (3,300)`;
- `||p_tau||_infinity<=1/2`;
- `|hat p_tau(tau)|>=27/64`.

Let `eta_tau=1/tau`. Since

`hat P_eta(xi)=exp(-eta |xi|)`,

at frequency `xi=tau` we have

`widehat{p_tau-p_tau*P_{eta_tau}}(tau)
 =(1-e^{-1}) hat p_tau(tau)`.

The elementary Fourier bound `|hat h(xi)|<=||h||_1` therefore yields

`boxed{
 ||p_tau-p_tau*P_{1/tau}||_1
 >= (1-e^{-1}) 27/64
 >0.2666.
}`

Thus the Poisson approximate identity does **not** converge uniformly in `L^1` over the QFORM target class, even for fixed `A=I_3`, smooth compactly supported sources, fixed compact output support, and a common raw height bound.

The failure also occurs in `L^infinity`. Put

`c0=(1-e^{-1})27/64`.

For `J=[2,301]`, because `p_tau` is supported in `(3,300)`, the Cauchy-smoothed mass outside `J` is at most

`P(|C_{1/tau}|>1)
 = (2/pi) arctan(1/tau)
 <= 2/(pi tau)`.

For `tau>=5` this is less than `c0/2`. Hence

`int_J |p_tau-p_tau*P_{1/tau}| >= c0/2`.

Since `|J|=299`,

`boxed{
 ||p_tau-p_tau*P_{1/tau}||_infinity
 >= c0/(598)
 >4.45*10^{-4}
}`

for all sufficiently large members of the family.

Therefore there is no target-uniform `L^1` or `L^infinity` Poisson boundary convergence rate. This is a proof-interface obstruction, not a counterexample to QFORM.

## 8. Precise separation: absolute continuity, bounded density, continuity

The logical ledger is now especially clean.

1. **Absolute continuity alone.** For any nonzero real symmetric `A` and any absolutely continuous joint input law, `x -> x^T A x` pushes the law to an absolutely continuous scalar measure. This follows by coarea/submersion away from `ker A`, which is null. No independence or rank-three threshold is needed.

2. **Fixed-instance boundedness and continuity.** The completed `fleet02/B15` fixed-matrix theorem gives, for every fixed rank-`>=3` symmetric `A` and arbitrary cap-one product inputs, an instance-dependent bounded density with a representative in `C_0(R)`. Hence for each fixed instance

`||P_eta*p_Q-p_Q||_infinity ->0`.

3. **No class-uniform continuity modulus.** Section 7 shows that even Poisson desmoothing has no uniform `L^1` or `L^infinity` rate across the target class. Thus continuity cannot be used as a uniform quantitative substitute for the central height estimate.

4. **Central universal height.** By Theorem 3.1 it is exactly equivalent, with no continuity premise and no pre-existing-density premise, to

`boxed{
 sup_{A,X,y}
 [s_3(A)/pi]
 E[1/(1+(X^T A X-y)^2)] < infinity.
}`

This is the first unpaid target-level implication in the present regularity formulation.

## 9. Why the new normal form is useful and what remains unpaid

Compared with the raw density or a shrinking-window limit, the unresolved quantity is now:

- positive;
- bounded pointwise as a kernel;
- at one fixed output scale;
- `C^infinity` in the center with an explicit common derivative bound;
- a fixed-height Stieltjes imaginary part;
- defined before absolute continuity is known;
- compatible with original-coordinate conditioning and the completed one-sheet theorem.

The unresolved mathematics is still not a regularity issue. It is to control the minority/two-sheet resolvent contribution and, globally, to force either a scale-comparable physical block or one of the completed diffuse/ridge/bank/cross-volume exits **before** paying reciprocal near-singular local curvature.

The projection-only two-sheet shortcut remains invalid; product provenance must stay in the estimate.

## 10. Nonclaims

This report does not prove the full QFORM theorem. It does not supply a universal modulus for the raw density, a uniform Poisson desmoothing rate, a uniformly conditioned physical block, or a generic two-sheet X-ray estimate. It does not rotate the product law and then assert independence. The fixed-height Poisson/Stieltjes identity is an exact reduction and regularity lemma; the remaining universal resolvent bound is still OPEN.
