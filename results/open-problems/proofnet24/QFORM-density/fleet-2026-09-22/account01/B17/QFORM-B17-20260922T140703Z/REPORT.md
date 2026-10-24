# account01/B17 — sharp calibration of the rank-three ruled-sheet bound

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Run:** `QFORM-B17-20260922T140703Z`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `AUXILIARY_ONLY / SHARP_CALIBRATION_OF_RANK3_MAJORITY_SIDE`  
**Full conjecture:** `OPEN / NOT PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. What is new and what was already known

The full target remains the arbitrary-dimensional, arbitrary-independent-law quadratic-form density conjecture. This report does **not** prove it.

A prior account01/B16 result, canonical report creation commit `8004481452c19f103fd5dd24c2cb4d787860b56a`, already proved the following important partial statement. If

`A=R diag(a,b,-c)R^T`, `R^TR=I_3`, `a,b,c>=1`,

then for independent input coordinates with one-dimensional densities bounded by one, the quadratic-form density satisfies on the majority-sign / one-sheet side

`ess sup_{s>0} p_Q(s) <= pi sqrt(2)`.

It uses the straight-line ruling of a one-sheet hyperboloid and the sharp two-dimensional product-marginal cap of Livshyts--Paouris--Pivovarov. I do not re-label that earlier theorem as new.

The new B17 contributions are:

1. an **exact identity** identifying the full coefficient-dependent B16 ruling constant with `4pi` times the zero-density of the corresponding centered Gaussian quadratic form;
2. application of the completed account02/B17 Gaussian theorem to show that this geometric bound has exactly the same coefficient extremizer `a=b=c` as the sharp Gaussian cone problem;
3. a separate **critical-cone trace bound** at level zero, without assuming continuity of the output density;
4. a dimension-three refinement using the stronger finite-dimensional Livshyts--Paouris--Pivovarov constant, giving `pi sqrt(3/2)` on the one-sheet side when the physical dimension is exactly three.

These are sharp-constant/witness constraints, not a solution of the remaining two-sheet or higher-rank problems.

## 2. Source input: product marginal bounds

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, prove that if

`F(x)=prod_i f_i(x_i)`, `||f_i||_infinity<=1`,

then every `k`-dimensional orthogonal marginal has density bounded by

`M_{n,k} = min( (n/(n-k))^((n-k)/2), 2^(k/2) )`.

For `k=2`, this is at most `2`; for `n=3` it improves to `sqrt(3)`.

Let `Z=R^T X` and let `g` be its density on `R^3`. Every affine line integral of `g` is the value of a two-dimensional orthogonal marginal of the original product law, hence

`int_L g d ell <= M_{n,2} <= 2`.                                  (2.1)

No independence after rotation is asserted.

## 3. Exact ruled-sheet constant

Write

`q(z)=a z_1^2+b z_2^2-c z_3^2`, `a,b,c>0`.

For `s>0`, a global ruling of `q=s` is

`Phi_s(theta,t)=(`
` sqrt(s/a)(cos theta-t sin theta),`
` sqrt(s/b)(sin theta+t cos theta),`
` sqrt(s/c)t )`.

Directly `q(Phi_s)=s`. With

`D(theta)=ab+ac cos^2(theta)+bc sin^2(theta)`,

a direct Jacobian computation gives

`(|partial_theta Phi x partial_t Phi|/|grad q(Phi)|)/|partial_t Phi|`
`=1/(2 sqrt(D(theta))).`                                           (3.1)

Thus coarea and (2.1) give for a.e. `s>0`

`p_Q(s) <= (M_{n,2}/2) K(a,b,c)`,                                 (3.2)

where

`K(a,b,c)=int_0^{2pi}`
` [ab+ac cos^2(theta)+bc sin^2(theta)]^(-1/2)dtheta`.               (3.3)

For general `n`, `M_{n,2}<=2`, recovering B16's bound `p_Q(s)<=K(a,b,c)`.

## 4. New identity with the partner Gaussian cone density

The completed partner result account02/B17 is

`yspennstate/math-open-problems@cdd32fd16a694a5f8acc7ba758e0db6596a3e4a1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T125054Z-account02-B17-QFORM-r11/REPORT.md`.

It proves that for independent standard Gaussians,

`Y=aG_1^2+bG_2^2-cG_3^2`,

its global density maximum is at zero and

`p_Y(0)=(1/(4pi)) J(a,b,c)`,                                      (4.1)

`J(a,b,c)=int_0^{2pi}[A(phi)(A(phi)+c)]^(-1/2)dphi`,
`A(phi)=a cos^2(phi)+b sin^2(phi)`.

### Proposition 4.1 — exact Gaussian/ruling identity

`boxed( K(a,b,c)=J(a,b,c)=4pi p_Y(0) ).`                           (4.2)

**Proof.** Restrict both integrals to a quadrant. Put

`r=b(a+c)/(a(b+c))`.

For the ruling integral, `t=tan theta` gives

`K/4 = 1/sqrt(a(b+c)) int_0^infinity`
` dt/[sqrt(1+t^2)sqrt(1+r t^2)].`                                 (4.3)

For `J`, tangent substitution gives

`J/4 = 1/sqrt(a(a+c)) int_0^infinity`
` dt/[sqrt(1+(b/a)t^2) sqrt(1+((b+c)/(a+c))t^2)].`

Put first `u=t sqrt(b/a)` and then `u=sqrt(r)v`. The resulting expression is exactly (4.3). This proves (4.2). `QED`

This is the completed partner theorem applied to the actual B16 coefficient integral, rather than merely cited.

If `s_0=min(a,b,c)`, the partner's sharp Gaussian bound gives

`p_Y(0)<=1/(2sqrt(2)s_0)`,

hence

`K(a,b,c)<=pi sqrt(2)/s_0`.                                       (4.4)

Equality in (4.4) occurs exactly at `a=b=c=s_0`. Thus the extremal coefficient geometry of the ruled-sheet estimate is exactly the Gaussian cone extremizer.

## 5. New finite-dimensional sharpening

Equation (3.2) retains the exact finite-dimensional marginal constant. If the physical dimension is `n=3`, then the Livshyts--Paouris--Pivovarov theorem gives

`M_{3,2}=sqrt(3)`.

Therefore, for every three-dimensional product input with scalar density caps one and every rank-three signature `(2,1)` form with `a,b,c>=1`,

`boxed( ess sup_{s>0} p_Q(s) <= pi sqrt(3/2) )`                    (5.1)

and the reflected statement holds for signature `(1,2)` on `s<0`.

Numerically,

`pi sqrt(3/2)=3.847649490485592...`,

which is strictly below the known universal lower bound `3sqrt(2)=4.242640687119285...`. Hence any witness approaching the universal lower-bound scale must use physical dimension at least four (and the known attaining mechanism is genuinely diffuse/high-dimensional).

For `n>=4`, the uniform two-dimensional marginal constant is `2`, so this particular finite-dimensional improvement disappears.

## 6. New critical-cone trace bound

At level zero a pointwise density value is representative-dependent, so continuity is not assumed or claimed. Instead define the geometric cone trace.

Let

`C={omega in S^2:q(omega)=0}`,
`dmu(omega)=dell(omega)/|grad_{S^2}q(omega)|`,

and

`T_0(g)=int_C int_0^infinity g(r omega)dr dmu(omega)`.

Pair antipodal points. Each pair is one complete line through the origin, so (2.1) gives

`T_0(g)`
`=(1/2)int_C[int_R g(r omega)dr]dmu(omega)`
`<= (M_{n,2}/2) mu(C).`                                           (6.1)

For the standard Gaussian density, radial integration on the same cone gives exactly

`p_Y(0)=mu(C)/(4pi)`.

Therefore Proposition 4.1 and the partner Gaussian bound yield

`boxed( T_0(g) <= 2pi M_{n,2} p_Y(0)`
`                  <= (pi M_{n,2})/(sqrt(2)s_0) ).`                (6.2)

In particular, for arbitrary physical dimension,

`T_0(g)<=pi sqrt(2)/s_0`,

and for `n=3`,

`T_0(g)<=pi sqrt(3/2)/s_0`.

This is a source-valid critical-level coarea trace estimate. It is not a proof that an arbitrary density representative is continuous at zero.

## 7. Sharp-witness consequences

Account02/B17 proves that every centered diffuse Gaussian projection mechanism has exact ceiling `3sqrt(2)` and that the three-block uniform family attains this value. The present calibration adds three constraints:

- the B16 ruled-sheet constant is not an unrelated geometric artifact: it is exactly `4pi` times the corresponding Gaussian cone peak;
- the worst coefficient configuration for this bound is the isotropic mixed-sign triple `(1,1,-1)`;
- in physical dimension three, the one-sheet branch is uniformly below `3sqrt(2)`, so no three-coordinate majority-sheet construction can improve the known universal lower bound.

The general ruled-sheet ceiling is

`pi sqrt(2) = (pi/3)(3sqrt(2))`,

a factor `pi/3=1.04719755...` above the known lower bound. Thus this branch is already constrained to within about `4.72%` of the current sharp witness scale.

## 8. Remaining gap and correction discipline

This report does **not** control the minority-sign two-sheet levels. The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` proves that an arbitrary three-dimensional probability density can have all line integrals bounded while its two-sheet quadratic trace diverges. Therefore (2.1) cannot simply be recycled on that side; a successful argument must retain additional product-projection provenance.

It also does not control arbitrary higher-rank forms, where additional spectral components are correlated with the selected triple after projection.

Corrections consumed before publication include:

- `QFORM-POINTWISE-DECAY-FALSE`;
- `QFORM-FIBER-SUP-DIMENSION-LOSS`;
- `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`;
- `QFORM-CROSSMINOR-ALONE-FALSE`;
- `QFORM-TWOSHEET-XRAY-ONLY-FALSE`;
- `QFORM-UV-CONDITIONAL-CAP-FALSE`;
- `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`;
- `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`;
- `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`;
- `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`.

No refuted intermediate claim is used.

## 9. Source pins and next step

Run-start coherent control source: `yspennstate/math-research-brain@61c55c4006501a0cd6e55f43fb92e88d451dc779`; control revision `2026-09-22.5`. Fresh pre-publication control/correction recheck reached `a9acf04a55c16e2ab843047c8ca4f73ce4254491`; no later stop or contradictory correction was present.

Prior ruled-sheet theorem explicitly consumed: account01/B16 handoff `qform-20260922T114042Z-account01-B16-r11.md`, canonical report creation commit `8004481452c19f103fd5dd24c2cb4d787860b56a`.

Named assignment partner actually applied: account02/B17 report commit `cdd32fd16a694a5f8acc7ba758e0db6596a3e4a1`.

External theorem used: Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1.

**Next unpaid implication:** obtain a two-sheet trace inequality for actual orthogonal marginals of cap-one product laws that uses more than the generic X-ray norm, or construct a genuine product-projection counterexample. For sharpness, search mesoscopic/non-Gaussian witnesses; Gaussian and fixed diffuse mechanisms cannot exceed `3sqrt(2)` by the completed B17 partner/previous-run results.
