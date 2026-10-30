SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-23T04:50:40Z.
attacking: sharpen the parabolic random-slope half-Frostman estimate, feed it into the completed fleet02/B03 indefinite-pair transducer, and optimize the diffuse/heavy crossover in the one-volume quarter-Riesz compiler.

# fleet01/B03 r23 — sharp derivative split and optimized one-volume crossover

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Run: `20260923T045040Z-fleet01-B03-QFORM-r23`  
Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_STRENGTHENED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full conjecture remains OPEN. This run does two concrete things. First, it improves the just-completed fleet02/B03 concentrated-row theorem by a direct derivative split which lowers its half-Frostman constant from `6 sqrt(2)` to `4 sqrt(2)` in the full linear-coefficient normalization. Second, it optimizes the crossover between the completed diffuse one-volume theorem and the heavy-row theorem, lowering the marginal-free quarter-Riesz constant from `4*2^(1/4)=4.756828...` to `4.700897...`; the resulting weighted independent-copy time constant drops from `31.867200...` to `31.492506...`, and the quarter-power indefinite-pair density constant drops from `21.381569...` to `21.213636...`.

No claim below conditions one member of a conjugate sum/difference pair on the other. No spectral rotation is used to assert independence. No Gaussian, moment, support, log-concavity, connected-support, or pointwise law-uniform oscillatory-decay hypothesis is introduced.

## 1. Source boundary and completed partner result actually applied


The designated completed partner is fleet02/B03:

`yspennstate/math-open-problems@ab591d183afaaeb8c8accbc9a80c06241f433532`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T041654Z-fleet02-B03-QFORM-auto11/REPORT.md`.

It proves the concentrated-row theorem: after completing an invertible indefinite physical pair `B`, if the Schur residual contains a genuine original-coordinate hub

`R=aX^2 + X(2 m^T Y + beta) + S(Y)`,

then, with `D=|det B|`, `kappa=sigma_min(B)`, `ell=||m||_2`,

`||p_Q||_infinity <= 8 sqrt(3) 2^(1/8) (D kappa ell)^(-1/4)`

`=15.11051839218372... (D kappa ell)^(-1/4)`.

The same partner report records the completed physical-pair logarithmic transducer used below: if the residual obeys

`sup_s P(|R-s|<=rho) <= H rho^(1/2)`,

then

`||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.                 (1.1)

The diffuse one-volume input used later is fleet03/B03's completed weighted-Riesz theorem, source-pinned in the preceding B03 run. For a nonzero original-coordinate cross block `M`, let

`Z1=||M||_F^2`, `alpha_i=||M_{i,*}||_2^2/Z1`, `h=max_i alpha_i`.

For any `q>=max(1,2h)` with `q<2`, at gamma `1/4` it yields

`H_(1/4)(R):=sup_z E|R-z|^(-1/4) <= C_diff(q) Z1^(-1/8)`,

where

`C_diff(q)=8(2pi)^(1/4)(e/q)^(1/8)/[(2-q)Gamma(1/4)cos(pi/8)]`.    (1.2)

For fixed `h`, this is minimized at the smallest allowed `q=max(1,2h)`.

## 2. Sharper parabolic random-slope lemma

### Lemma 2.1 — `QFORM-RANDOM-SLOPE-DERIVATIVE-SPLIT-v2`

Let `X` have density at most one and be independent of an arbitrary random pair `(L,S)`. Assume only that `L` has density cap `M<infinity`; `L` and `S` may be arbitrarily dependent. For arbitrary `a in R`, define

`T=aX^2+L X+S`.

Then for every `z in R`, `epsilon>0`, and `r>0`,

`P(|T-z|<=epsilon) <= 2 M r + 4 epsilon/r`.                        (2.1)

Consequently

`boxed: sup_z P(|T-z|<=epsilon) <= min(1,4 sqrt(2 M epsilon)).`     (2.2)

This strengthens the partner's `6 sqrt(2) sqrt(M epsilon)` bound under exactly the same hypotheses.

### Proof

Write

`q(x)=a x^2+Lx+S-z`, `q'(x)=2ax+L`.

Split the event into the near-critical part `N_r={|2aX+L|<=r}` and its complement.

Because `X` is independent of `L`, after conditioning on `X=x`, the near-critical condition places `L` in an interval of length `2r`. Therefore

`P(N_r)<=2Mr`.                                                     (2.3)

On the complement, condition on `(L,S)=(l,s)`. The set `{x:|2ax+l|>r}` has at most two connected components, and on each component `q` is monotone with derivative magnitude greater than `r`. The target interval `[-epsilon,epsilon]` has length `2epsilon`, so the inverse-image length on each component is at most `2epsilon/r`. There are at most two components; hence the total active `x`-length is at most `4epsilon/r`. Since `f_X<=1`,

`P(|q(X)|<=epsilon, |q'(X)|>r | L=l,S=s) <=4epsilon/r`.            (2.4)

Average (2.4), combine with (2.3), and optimize at

`r=sqrt(2epsilon/M)`

to obtain (2.2). For `a=0` the far set has only one monotone component and the displayed bound remains valid. QED.

### Equivalent `2LX` normalization

If instead

`T=aX^2+2LX+S`, `||p_L||_infinity<=M`,

then applying (2.2) to the full coefficient `2L`, whose density cap is `M/2`, gives

`boxed: sup_z P(|T-z|<=epsilon) <=4 sqrt(M epsilon).`              (2.5)

This is exactly the r22 lemma, now reconciled with the partner's full-coefficient convention.

## 3. Product-source specialization and dependence-safe time integral

Let `Y=(Y_j)` have independent coordinate densities at most one, independent of `X`, and let `m!=0`. Put

`L=2m^T Y+beta`.

The completed one-dimensional product-projection theorem gives

`||p_(m^T Y)||_infinity <= sqrt(2)/||m||_2`,

hence

`||p_L||_infinity <=1/(sqrt(2)||m||_2)`.                           (3.1)

Lemma 2.1 therefore gives, for

`T=aX^2+X(2m^T Y+beta)+S(Y)`,

`boxed: sup_z P(|T-z|<=epsilon)
 <= H_m epsilon^(1/2),
 H_m=4*2^(1/4)||m||_2^(-1/2)=2^(9/4)||m||_2^(-1/2).`              (3.2)

For every `0<gamma<1/2`, the elementary layer-cake estimate for a half-Frostman law gives

`sup_z E|T-z|^(-gamma) <= H_m^(2gamma)/(1-2gamma)`.                (3.3)

Let `T'` be an independent copy. Conditioning on `T'` preserves the uniform bound (3.3), so

`E|T-T'|^(-gamma) <= H_m^(2gamma)/(1-2gamma)`.                     (3.4)

Using the independent-copy identity

`|phi_T(t)|^2=phi_(T-T')(t)`

as one coupled object, the exact Riesz-energy formula yields

`boxed:
 int_R |t|^(gamma-1)|phi_T(t)|^2 dt
 <= [2 Gamma(gamma) cos(pi gamma/2)/(1-2gamma)] H_m^(2gamma).
`                                                                      (3.5)

At `gamma=1/4`,

`boxed:
 int_R |t|^(-3/4)|phi_T(t)|^2 dt
 <= 8*2^(1/8) Gamma(1/4) cos(pi/8) ||m||_2^(-1/4)
 =29.222351302795506... ||m||_2^(-1/4).
`                                                                      (3.6)

The partner's just-completed constant at this endpoint is `35.7899248881...`; the ratio is exactly `sqrt(2/3)`, reflecting the improvement from `6sqrt(2)` to `4sqrt(2)` in Lemma 2.1.

No endpoint claim at `gamma=1/2` is made; the live correction excluding a one-copy half-Riesz endpoint remains binding.

## 4. Actual application of the completed fleet02/B03 result

Apply the partner's completed physical-pair implication (1.1) to the residual (3.2). Substituting

`H=2^(9/4)||m||_2^(-1/2)`

gives

`boxed:
 ||p_Q||_infinity
 <= 2^(29/8) (D kappa ||m||_2)^(-1/4)
 =12.337686603263526... (D kappa ||m||_2)^(-1/4).
`                                                                      (4.1)

Thus every interval `I` satisfies

`P(Q in I) <=2^(29/8)(D kappa ||m||_2)^(-1/4)|I|`.                (4.2)

This is a direct application of the completed fleet02/B03 result to an actual inequality; only the upstream half-Frostman constant is sharpened.

For comparison, the partner theorem itself gives `15.1105183921...` with the same scale factor. Hence (4.1) is a strict constant strengthening by `sqrt(2/3)`.

### Target-family check

For `s,r` with `|s|>=1`, `|r|>=1`, `||v||_2=1`, and arbitrary real `a`, take

`B_s=[[0,s],[s,0]]`,

`H_(a,r,v)=[[a,r v^T],[r v,0]]`,

`A=B_s direct_sum H_(a,r,v)`.

`B_s` contributes eigenvalues `+|s|,-|s|`. The two nonzero eigenvalues of the star block solve

`lambda^2-a lambda-r^2=0`; their product is `-r^2`, so at least one has modulus at least `|r|>=1`. Thus the owner target holds. Here

`D=s^2`, `kappa=|s|`, `ell=|r|`,

so (4.1) gives

`boxed: ||p_(X^T A X)||_infinity <=2^(29/8)|s|^(-3/4)|r|^(-1/4).` (4.3)

The partner's completed theorem applied to the same family gives the weaker scalar `8sqrt(3)2^(1/8)` in place of `2^(29/8)`.

Essential boundedness/absolute continuity is proved in this branch. Continuity is not established by this argument.

## 5. Optimized diffuse/heavy crossover for one-volume quarter-Riesz smoothing

The preceding r22 run combined the diffuse branch at `h<=1/2` with the heavy branch at `h>1/2`. That threshold was convenient but not optimal. Because both formulas are valid on an overlap, we can choose the crossover exactly.

For `h>1/2`, set `q=2h` in (1.2). Then

`C_diff(h)=8(2pi)^(1/4)(e/(2h))^(1/8)/[(2-2h)Gamma(1/4)cos(pi/8)]`. (5.1)

The heavy-row random-slope bound from r22 / Lemma 2.1 gives

`C_heavy(h)=4*2^(1/8) h^(-1/8)`                                   (5.2)

in

`H_(1/4)(R)<=C_heavy(h) Z1^(-1/8)`.

`C_diff(h)` is increasing for `h>=1/2`, while `C_heavy(h)` is decreasing. Solving

`C_diff(h_*)=C_heavy(h_*)`

is elementary after cancelling `4 h^(-1/8)`:

`boxed:
 h_*=1-[pi^(1/4)e^(1/8)]/[Gamma(1/4)cos(pi/8)]
 =0.5496212850267048... .
`                                                                      (5.3)

The common value is

`boxed:
 C_*=4*2^(1/8) h_*^(-1/8)
 =4.700897674324740... .
`                                                                      (5.4)

For `h<=1/2`, the diffuse constant is the still smaller `4.2847485783...`. For `1/2<h<=h_*`, use the diffuse formula; for `h>=h_*`, use the heavy formula. Therefore every nonzero original-coordinate cross block satisfies the improved marginal-free theorem

`boxed:
 sup_z E|R-z|^(-1/4)
 <= C_* ||M||_F^(-1/4),
 C_*=4.700897674324740... .
`                                                                      (5.5)

This strictly improves the r22 constant `4.7568284600...` without changing scope.

Consequently the dependence-safe time integral improves to

`boxed:
 int_R |t|^(-3/4)|phi_R(t)|^2 dt
 <= 2 Gamma(1/4)cos(pi/8) C_* ||M||_F^(-1/4)
 =31.492505546446097... ||M||_F^(-1/4).
`                                                                      (5.6)

Again `|phi_R|^2` is treated through the full difference law and no sum/difference conditional cap is introduced.

## 6. Improved marginal-free pair + one-volume density certificate

If an invertible indefinite physical pair `B` is completed and its Schur residual contains any nonzero original-coordinate cross block `M`, then Markov applied to (5.5) gives a quarter-power small-ball coefficient

`H=C_* Z1^(-1/8)`.

Substitute this into the completed fleet02/B03 quarter-power pair transducer from its preceding report:

`||p_Q||_infinity <=3*2^(4/3)H^(2/3)D^(-1/3)kappa^(-1/6)`.

Hence

`boxed:
 ||p_Q||_infinity
 <= C_pair,* D^(-1/3)kappa^(-1/6)Z1^(-1/12),
 C_pair,*=3*2^(4/3)C_*^(2/3)
 =21.213636077138162... .
`                                                                      (6.1)

The r22 marginal-free constant was `21.3815692353...`; (6.1) is the optimized version.

In the concentrated regime one should not use (6.1) if the half-power certificate (4.1) is quantitatively better. The complete adaptive statement is the minimum of the quarter-power certificate (with the exact `h`-dependent `min{C_diff(h),C_heavy(h)}`) and the half-power certificate

`2^(29/8)(D kappa)^(-1/4) h^(-1/8) Z1^(-1/8)`.

## 7. What remains unpaid

This run improves a real analytic endpoint and the all-row-marginal compiler, but it does not solve the structural bottleneck. The bare hypothesis `s_3(A)>=1` still does not force a single physical indefinite pair with `D`, `kappa`, and residual cross resource bounded below at universal scale. Existing source counterexamples rule out several naive one-minor and one-Schur extraction principles.

The remaining full-target implication is therefore still aggregate-before-inversion: convert third spectral/exterior mass into one of the already-paid ridge, cross-volume, physical-core, mixed-hub, or pair-plus-one-volume packets before paying reciprocal local determinants. The unrestricted bounded-density theorem and unrestricted continuity theorem remain OPEN.

## 8. Status

- Main new lemma: proved.
- Designated fleet02/B03 completed result: applied directly in (4.1)--(4.3).
- Dependence-safe independent-copy time estimate: improved in (3.5)--(3.6) and globally optimized in (5.6).
- Linear small-ball scaling: obtained in the stated physical-pair branches through (4.2) and (6.1).
- Full conjecture: OPEN.
- Continuity: not proved by these branches.
- No schedule, task, email, notification, permission, installation, paid-call, remote-workflow, or public-release changes were made.
