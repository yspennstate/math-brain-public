Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on P0025: `E_disk: 0 -> 0`, unchanged count `1 -> 2`; Section-B methods #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #13 FIND WHAT ONLY INCREASES, #20 FIND WHY THE ALGORITHM FAILS.**

# R06 — P0025 exterior-disc synchronous coupling / exact frozen-excursion trace reduction

## 0. Continuity, source, and non-reopening

This run continues the current create-only R06 target

`P0025 — Krzysztof Burdzy, My favorite open problems, Problem 5(ii)`

from `runs/R06/20260918T0222Z_p0025_critical_excursion_cocycle_31.md` at commit `6820f2a7b0de92bc50307bebd822739f75fec632`. I did **not** reopen the BENJ three-source target after its six-run rotation, D0069, or the original Lyons--Peres target.

Burdzy's current author page, checked again on 2026-09-18, still asks:

> If `D` is the complement of a non-degenerate closed disc, is it true that with positive probability `limsup_{t->infinity}|X_t-Y_t|>0` for two synchronously driven reflected Brownian motions?

The canonical R06 claim remains `operations/claims/P0025.md` at create-only commit `7daaafd515f422dcd802f626e7fb4e17eeb855fb`.

The frozen source metric remains binary:

`E_disk=1`

only after a full proof or refutation of the literal source question; otherwise `E_disk=0`. The exact tangent-cocycle calculation from run 31 is a partial mechanism result and did not move the source metric.

For continuity, the original assigned Lyons--Peres state remains frozen exactly:

- Question 6.20 asks for `Phi_V(G)` for regular, co-regular plane graphs and for `Phi_E,Phi_V` more generally;
- R06's normalization is the outer vertex boundary `partial_V K={x notin K: x~y for some y in K}` and `Phi_V=inf |partial_V K|/|K|`;
- the admissible pentagonal regime `H_{5,5}` remains `Phi_V(H_{5,5})=sqrt(5)`, certified interval `[sqrt(5),sqrt(5)]`, width `0`;
- the **full** Lyons--Peres question remains **PARTIAL**;
- Haslegrave--Panagiotis triangular/codegree-3 and quadrangular/codegree-4 results (DOI `10.1002/rsa.20946`) remain excluded prior art.

## 1. Required repository and literature read

I re-read/recovered the current campaign roots and operations state before attacking the mathematics: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the new-methods deployment manifest, the newest R06 report, the live P0025 claim, and the nearest Brownian neighboring report (R15/I0076). I also rechecked the live Burdzy Problem-5 page and later/source-adjacent literature.

Fresh dated searches on 2026-09-18 for the exact exterior-disc synchronous-coupling limsup question again recovered the original/current Burdzy page, Cranston--Le Jan (1989), Burdzy--Chen--Jones (2006), Burdzy's reflected-flow differentiability paper (2009), Burdzy--Lee's multiplicative functional, and later papers citing this family, but no later source-matching proof/refutation. This is bounded search evidence, not a global novelty certificate.

Two pieces of prior art are especially important for this run:

1. Cranston--Le Jan (1989) prove finite-time noncoalescence in the exterior disc and derive the exact reduced three-dimensional diffusion used below.
2. Burdzy (2009), *Differentiability of stochastic flow of reflected Brownian motions*, proves pathwise differentiability in its smooth-domain setting. Its proof contains a quantitative one-block estimate of the form
   `E Xi <= C eps^(4/3)|log eps|`
   and associated probability bounds (their equations (3.166)--(3.167)). Those rates are already summable on geometric scales. The paper's setup is bounded-domain; they are **not** silently imported as an exterior-disc theorem here.

## 2. Recovered run-31 blocker

Run 31 changed category to the tangent reflected-flow cocycle. For the exterior unit circle it derived, for `q>0`,

`Psi(q)=q[1-Gamma((q+1)/2)/(sqrt(pi) Gamma((q+2)/2))]`.

This recovers the **known prior-art** cancellation `Psi'(0)=0` and gives the exact tangent fluctuation rate

`Psi''(0)=2 log 2>0`.

Thus the infinitesimal log-separation is critical but nondegenerate. The unresolved bridge is finite separation: one needs a scale-summable comparison between the nonlinear pair process and this centered tangent cocycle.

This run attacks that bridge by parameterizing the exact geometry by the current half-separation `z`.

# 3. #5 ADD A PARAMETER — the exact finite-separation midpoint domain

Scale the forbidden disc to radius one. While neither particle is reflecting, the two particles receive exactly the same Brownian increment, so their separation vector is fixed during that excursion.

Fix a half-separation `z in (0,1)` and rotate coordinates so that the two particle locations can be written

`X=m+i z,    Y=m-i z`, 

where `m in C` is the midpoint. During a bulk excursion, the midpoint is planar Brownian motion constrained by

`|m-i z|>=1,    |m+i z|>=1`.

Hence the **frozen-separation midpoint domain** is exactly

`Omega_z = C \ ( B(i z,1) union B(-i z,1) ).`

This is the same geometry encoded in Cranston--Le Jan's reduced state space

`x^2+(|y|-z)^2>=1`.

The two circles intersect at

`+/- a(z),    a(z)=sqrt(1-z^2).`

The boundary is a two-arc 'peanut' with corners at these two simultaneous-contact configurations.

## 3.1 Exact conformal uniformization

Set

`alpha=arcsin z`,

`beta=pi/2-alpha`,

`lambda(z)=2 beta/pi=1-(2/pi)arcsin z`,

`kappa(z)=1/lambda(z)=pi/(pi-2 arcsin z)`.

Define

`T_z(w)=(w-a)/(w+a)`.

Both boundary circles pass through `+/-a`, so `T_z` sends them to straight lines through the origin. Evaluate at the topmost point `w=i(1+z)` of the upper circle. Using `z=sin alpha`, `a=cos alpha`,

`(1+z)/a = tan(pi/4+alpha/2)`,

and therefore

`arg T_z(i(1+z))=pi-2 arctan((1+z)/a)=pi/2-alpha=beta`.

The lower arc goes to the ray of argument `-beta`. Since `T_z(infinity)=1`, the exterior domain is the wedge

`W_beta={xi: |arg xi|<beta}`.

Consequently

`G_z(w)=T_z(w)^kappa`

(with the branch on this wedge) maps `Omega_z` conformally onto the right half-plane.

This is an exact finite-`z` statement, not a tangent approximation.

## 3.2 Exact common boundary coordinate

For real `s !=0`, let

`t_z(s)=(i s)^lambda`,

where `arg(i s)=+pi/2` for `s>0` and `-pi/2` for `s<0`. Define

`p_z(s)=a (1+t_z(s))/(1-t_z(s)).`

Extend by `p_z(0)=a` and `p_z(infinity)=-a`. Then

`G_z(p_z(s))=i s`.

So one real coordinate `s in R union {infinity}` parametrizes the entire peanut boundary and, at `z=0`,

`p_0(s)=(1+i s)/(1-i s)`,

which is the usual Möbius parametrization of the unit circle.

### Uniform first variation

At `z=0`, `a'(0)=0`, `lambda'(0)=-2/pi`, and therefore

`t'_0(s)=-(2/pi) i s Log(i s)`.

Since the derivative of `(1+t)/(1-t)` is `2/(1-t)^2`,

`v(s):=partial_z p_z(s)|_{z=0}=-(4/pi) i s Log(i s)/(1-i s)^2.`

The branch is as above. Moreover `v(s)->0` as `s->0` and as `|s|->infinity`.

For, say, `0<=z<=1/2`, `lambda>=2/3` and the ray angle satisfies `beta>=pi/3`. Writing `r=|s|^lambda`,

`|1-t_z(s)|^2=1+r^2-2 z r >= (1/2)(1+r^2)`.

Differentiating once and twice in `z` then only produces terms bounded by constants times

`r(1+|log r|+|log r|^2)/(1+r^2)`

and similar rational expressions, all uniformly bounded for `r>0`. Hence there exists an absolute finite `C` such that

`sup_s |p_z(s)-p_0(s)-z v(s)| <= C z^2,    0<=z<=1/2.`

In particular,

`sup_s |p_z(s)-p_0(s)| <= C z.`

This is useful because it is uniform all the way to the two corners, even though pointwise clock derivatives below are not uniform there.

# 4. Exact excursion kernel: the bulk jump law becomes universal

Let `H_z(p,q)` denote the standard two-dimensional Brownian boundary-excursion Poisson kernel for the frozen domain `Omega_z`, normalized so that for the exterior unit circle (`z=0`) it is

`1/(pi |p-q|^2)=1/[4 pi sin^2((theta-theta')/2)].`

Conformal covariance of the excursion kernel gives, for smooth arc points `p,q`,

`H_z(p,q)=|G'_z(p)| |G'_z(q)| / [pi |G_z(p)-G_z(q)|^2].`

Substitute `p=p_z(s)`, `q=p_z(r)`. Since `G_z(p_z(s))=i s` and arclength satisfies

`d sigma_z(p_z(r))=|p'_z(r)|dr=dr/|G'_z(p_z(r))|`,

we get the exact measure identity

`boxed{ H_z(p_z(s),p_z(r)) d sigma_z(r)
       = |G'_z(p_z(s))| dr/[pi(s-r)^2]. }`

Thus if the boundary-local-time clock is conformally reparametrized by

`d ell_conf=|G'_z(p_z(s))| d ell_phys`,

the excursion endpoint Lévy kernel is **exactly**

`dr/[pi(s-r)^2]`

for every fixed `z in (0,1)`. No small-`z` approximation is involved.

Equivalently, after multiplying by arclength at the starting point as well,

`boxed{ H_z(p_z(s),p_z(r)) d sigma_z(s)d sigma_z(r)
       = ds dr/[pi(s-r)^2]. }`

Therefore the symmetric boundary-trace Dirichlet form in the conformal coordinate is exactly the same Cauchy form for every `z`:

`E_z(f,f)=(1/(2pi)) int int (f(s)-f(r))^2/(s-r)^2 ds dr.`

The frozen bulk-excursion mechanism is not where a new finite-separation drift can hide. The domain dependence is transferred entirely into the **speed measure / physical-clock density** and the physical embedding of boundary states.

I have not located this particular peanut-domain reduction in the bounded search. It is recorded as an R06 derivation; literature novelty is **UNVERIFIED**.

# 5. The physical clock: exact density and an O(z) integrated perturbation

Differentiate the boundary map. With `r=|s|^lambda`,

`boxed{ rho_z(s):=|p'_z(s)|
 = 2 a lambda |s|^(lambda-1) / |1-(i s)^lambda|^2. }`

This is the physical arclength speed measure density `d sigma_z=rho_z(s)ds`. At `z=0`,

`rho_0(s)=2/(1+s^2).`

Pointwise relative comparison is **not** uniform near `s=0,infinity`: because `lambda<1` for `z>0`, `rho_z(s)` has the corner power law `|s|^(lambda-1)` near zero and `|s|^(-lambda-1)` at infinity.

However the singularity is integrable and the whole speed measure is a genuinely first-order perturbation in total variation.

### Lemma (integrated clock perturbation)

There is a finite absolute constant `C` such that, for `0<=z<=1/2`,

`boxed{ int_R |rho_z(s)-rho_0(s)| ds <= C z. }`

**Proof.** For `z<=1/2`, `lambda>=2/3` and

`D_z(s):=|1-(i s)^lambda|^2=1+r^2-2zr >= (1/2)(1+r^2).`

Differentiate `log rho_z` in `z`. Since `a'/a`, `lambda'/lambda` are bounded and

`partial_z r = r lambda'(z) log|s|`,

one obtains

`|partial_z log rho_z(s)| <= C(1+|log|s||)`.

For `|s|<=1`, the displayed lower bound on `D_z` gives

`rho_z(s)<=C |s|^(-1/3)`,

while for `|s|>=1`,

`rho_z(s)<=C |s|^(-5/3)`.

Hence

`sup_{0<=z<=1/2} rho_z(s)(1+|log|s||)`

is integrable on `R`. The mean-value theorem and dominated integration give the asserted `O(z)` bound. `□`

This is precisely the scale of perturbation that the previous run wanted: along geometric separation scales `z_n`, the frozen-excursion speed-measure errors `O(z_n)` are summable.

What it does **not** yet control is the full moving two-point process, because reflection simultaneously changes `z` and the moving coordinate frame.

# 6. Exact localization of instantaneous expansion to the extra peanut arcs

Cranston--Le Jan's exact exterior equation is

`d z = (1/2)(z-|y|) d phi`.

Thus separation expands under a local-time increment exactly when

`A:=|y|-z<0`.

The conformal coordinate makes this set explicit. On the upper peanut arc (`s>0`) write `r=s^lambda`. A direct calculation from `p_z(s)` gives

`|y|-z = [2r-z(1+r^2)]/[1+r^2-2zr].`

The denominator is positive. The two roots of the numerator are

`r_-=(1-a)/z=z/(1+a),`

`r_+=(1+a)/z=1/r_-`.

Therefore the expansion configurations are exactly

`|s| < s_-(z):=r_-^(1/lambda)`

or

`|s| > 1/s_-(z)`.

For small `z`, `s_-(z)=z/2+o(z)` up to the harmless `lambda` exponent correction.

Geometrically, on each unit-circle arc these are just the two short pieces added by separating the coincident circles. Their total physical arclength is exactly

`boxed{ 4 arcsin z = 4z+O(z^3). }`

So the instantaneous-expansion configurations occupy only an `O(z)` boundary-length set. This is consistent with, but does not by itself prove, an `O(z)` nonlinear drift correction because the true moving-frame boundary occupation is not uniform.

# 7. #13 FIND WHAT ONLY INCREASES — an exact prior-art submartingale structure

The 1989 Cranston--Le Jan proof already contains a stronger monotonicity identity than run 31 used. This is **prior art** and is not relabeled as new.

They set

`L=x^2+(y-1)^2`,

`N=x^2+(y+1)^2`,

`u=log(LN)`.

On their stopped exterior pieces, their calculation gives

`boxed{
 d(u+2 log z)
 = dM + [ |y| z (2|y|-z)^2/(L N) ] d phi,
}`

where `M` is a local martingale. The finite-variation coefficient is nonnegative.

Thus

`V=u+2 log z`

is a local submartingale on those pieces.

For the present source question this is encouraging but not a closure argument. If one could sample at regenerative times where `u` were uniformly controlled above and below, a one-way drift `log z -> -infinity` would be hard to reconcile with this submartingale plus the nonzero tangent variance. But the exterior problem makes `u` unbounded at infinity, and the original proof has to stop around the special configurations near `(x,y,z)=(0,+/-1,2)`. Optional stopping without controlling those tails is invalid.

The useful conclusion is narrower: the exact nonlinear finite-variation term visible in the old reduced SDE has the **favorable nonnegative sign** at the level of `u+2log z`. A future negative answer to Burdzy cannot come from a hidden deterministic negative drift in this particular Lyapunov combination.

# 8. #20 FIND WHY THE ALGORITHM FAILS — the remaining obstruction is now a clock/frame problem

Three natural shortcuts fail, for precise reasons.

### Failure 1: total variation of raw excursion measures

The universal kernel

`dr/[pi(s-r)^2]`

has infinite mass at `r=s`. Therefore it is meaningless to claim an `O(z)` total-variation perturbation of the **raw** excursion Lévy measures. The correct objects are compensated generators / Dirichlet forms and the speed measure. In those variables the jump form is exactly universal and the speed measure differs by `O(z)` in `L^1`.

### Failure 2: pointwise clock comparison

Although `int|rho_z-rho_0|=O(z)`, the ratio `rho_z/rho_0` is not uniformly close to one at the two simultaneous-contact corners. Indeed `lambda<1` gives power-law distortion at `s=0,infinity`. The pointwise perturbation becomes order one in exponentially remote conformal-coordinate layers. A proof has to integrate those corner layers, not take a global supremum.

For example, on the moderate set

`exp(-z^(-1/2)) <= |s| <= exp(z^(-1/2))`,

the exact density formula gives

`|log(rho_z/rho_0)| <= C sqrt(z)`,

while the arclength of the two omitted tails is at most `C exp(-c/sqrt(z))`. This is another summable split, but it still concerns the frozen trace only.

### Failure 3: importing the bounded-domain differentiability estimate verbatim

Burdzy's 2009 proof contains the very useful superlinear estimates

`E Xi <= C eps^(4/3)|log eps|`

and corresponding probability bounds, and the proof explicitly uses a bounded smooth-domain setup (one estimate even indexes dyadic spatial scales starting from the diameter of `D`). The exterior disc has no finite diameter and its physical-time excursions can be arbitrarily large. The estimate therefore cannot simply be cited as though it already covered P0025.

The new conformal reduction says exactly how to try to repair this: collapse every bulk excursion to the boundary trace. In the conformal boundary coordinate, the frozen excursion jump form is universal and the only exterior-specific effect is the explicit variable speed measure plus the moving-frame/reflection terms. This removes the need to estimate the physical diameter of a bulk excursion when the quantity of interest is pair separation, which is constant during that bulk excursion.

# 9. What would now be enough for the source problem

The tangent log-cocycle is centered with variance rate `2 log 2`. Run 31 identified the desired finite-separation critical transfer. This run makes the exterior-specific part much more concrete.

A sufficient next lemma would be an **exterior one-block quantitative linearization**: for a fixed boundary-local-time block and pair half-separation `z=eps`, couple the exact finite-pair separation update to the tangent multiplicative functional so that, uniformly over the compact angular state,

`P( relative error > eps^eta ) <= C eps^eta`

for some `eta>0` (or any comparably summable geometric-scale bound).

Burdzy's bounded-domain proof achieves substantially stronger exponents in its setting. The exact peanut uniformization now supplies a replacement for the unbounded bulk-excursion estimates. What remains to be controlled is:

1. the moving orientation/frame during reflection;
2. the conversion between total pair local time and the conformal trace clock;
3. the two simultaneous-contact corner layers;
4. a critical recurrence/Lamperti step converting the centered tangent fluctuations plus summable nonlinear error into recurrent returns of finite separation to a fixed positive scale;
5. finally, the local-time to physical-time passage (each planar exterior reflected Brownian motion is recurrent, but this time change must be stated and proved in the two-point argument).

I do **not** claim these five obligations are completed.

# 10. Current status and next methods

Source metric:

`E_disk: 0 -> 0`.

Supported unchanged count:

`1 -> 2`.

Status: **OPEN / PARTIAL**.

The new exact results are structural reductions of the finite-separation excursion geometry, not a source-level answer.

Methods tried this run:

- **#5 ADD A PARAMETER:** introduced the half-separation `z` as a domain-deformation parameter and exactly uniformized the resulting two-disc peanut domain; derived the exact common boundary coordinate, uniform first variation, universal Cauchy excursion form, and `O(z)` speed-measure perturbation.
- **#13 FIND WHAT ONLY INCREASES:** recovered and reinterpreted Cranston--Le Jan's exact prior-art local submartingale `u+2log z`, whose nonlinear finite-variation term has nonnegative sign.
- **#20 FIND WHY THE ALGORITHM FAILS:** isolated the real obstruction as the moving frame/clock and corner layers; raw excursion TV and verbatim bounded-domain linearization are invalid shortcuts.

Next suggested Section-B moves, deliberately different from `[5,13,20]`: **#6 DEFORM TO A POINT YOU CAN SOLVE, #11 DUALIZE, #30 ONE SCALE AT A TIME.** Concretely: truncate the exact moving-frame generator at one geometric separation annulus, use the universal Cauchy Dirichlet form as the dual energy object, and prove a single-annulus exterior quantitative linearization with an error exponent `eta>0` before attempting global recurrence.

If P0025 remains unchanged on the next run, the unchanged count reaches three and the following run must be the Section-I thinking-only stuck protocol.

# 11. Model / reasoning / scheduler-control truthfulness

The requested GPT-6/maximum setting is still **not enforceable** from the scheduler/control surface exposed to this worker. The current deployment manifest records the controls actually available: title/prompt, schedule or relative start, timing mode, and enabled state. It exposes no binding model-family selector, no reasoning-effort selector, no guaranteed full-hour execution field, and no authenticated completed-run model/reasoning attestation.

Therefore this report says exactly what ran: GPT-5.6 Sol; reasoning level UNVERIFIED.

Actually enforcing GPT-6/maximum would require an authorized product/backend or owner/admin task-control surface that exposes persistent model and reasoning fields plus authenticated applied-run telemetry. The historical P26 `You cannot modify this task` event remains an authorization-context boundary in the repository record; the lawful workaround is the owning/authorized context or platform support, not duplication or a permission bypass. No scheduler or permission change was attempted.

# 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  preserved_origin:
    source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20 / I0056"
    frozen_graph: "H_{5,5}"
    normalization: "outer vertex boundary, unweighted |partial_V K|/|K|"
    interval: "[sqrt(5), sqrt(5)]"
    width: 0
    full_source_status: PARTIAL
    exclusions:
      - "Haslegrave-Panagiotis triangular/codegree-3 cases"
      - "Haslegrave-Panagiotis quadrangular/codegree-4 cases"
  active_target:
    id: P0025
    source: "Krzysztof Burdzy, My favorite open problems, Problem 5(ii)"
    exact_scope: "synchronous reflected Brownian motions in the complement of a non-degenerate closed disc; positive probability of positive asymptotic limsup separation"
    claim_commit: 7daaafd515f422dcd802f626e7fb4e17eeb855fb
    metric: E_disk
    before: 0
    after: 0
    movement: NO_MOVEMENT
    unchanged_count_before: 1
    unchanged_count_after: 2
    status: OPEN_PARTIAL
  tried_moves: [5, 13, 20]
  new_results:
    - "exact frozen midpoint domain Omega_z = C minus union of the two unit discs centered at +/- i z"
    - "exact conformal map G_z(w)=((w-a)/(w+a))^kappa with a=sqrt(1-z^2), kappa=pi/(pi-2 arcsin z)"
    - "exact common boundary coordinate p_z(s)=a(1+(is)^lambda)/(1-(is)^lambda), lambda=1-(2/pi)arcsin z"
    - "uniform first variation p_z=p_0+z v+O(z^2), v=-(4/pi)i s Log(is)/(1-is)^2"
    - "exact universal Cauchy excursion Dirichlet form ds dr/[pi(s-r)^2] after conformal boundary parametrization"
    - "physical speed density rho_z=2 a lambda |s|^(lambda-1)/|1-(is)^lambda|^2 and L1 perturbation int|rho_z-rho_0|=O(z)"
    - "instantaneous expansion configurations are exactly the two conformal tails and have total physical boundary arclength 4 arcsin z"
    - "Cranston-Le Jan prior-art identity d(u+2log z)=dM+[|y|z(2|y|-z)^2/(LN)]dphi has nonnegative drift"
  prior_art_boundary:
    - "Cranston-Le Jan 1989: exterior finite-time noncoalescence and reduced diffusion"
    - "Burdzy-Chen-Jones 2006: exterior-circle Lyapunov exponent zero"
    - "Burdzy 2009: differentiability plus bounded-domain quantitative error estimates; not imported verbatim to exterior"
  remaining_obligation: "prove one-annulus quantitative exterior linearization for the full moving pair (including orientation, local-time clock and corner layers), then apply a critical recurrence argument and return from local time to physical time"
  evidence:
    - "operations/claims/P0025.md @ 7daaafd515f422dcd802f626e7fb4e17eeb855fb"
    - "runs/R06/20260918T0222Z_p0025_critical_excursion_cocycle_31.md @ 6820f2a7b0de92bc50307bebd822739f75fec632"
    - "Cranston-Le Jan, Ann. IHP 25 (1989), 99-107"
    - "Burdzy-Chen-Jones, Illinois J. Math. 50 (2006), 189-268"
    - "Burdzy, Electron. J. Probab. 14 (2009), 2182-2240"
    - "Burdzy-Lee, multiplicative functional for reflected Brownian motion"
  audits:
    p26: NONE
    second_independent: NONE
  closure: false
```

# 13. Delivery boundary

This is the single immutable R06 report for the run. I made no shared-root edit, no peer-track edit, no email/Gmail/Drive action, no public post, no purchase, no permission change, and no scheduler change. No finite exhaustive claim arose, so I did not create a decorative checker.