Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on P0025: `E_disk: 0 -> 0`, unchanged count `5 -> 6`; Section-B methods #4 PROVE SOMETHING WEAKER, COMPLETELY, #16 COMPUTE THE DIRECT SMALL MODEL, #22 READ THE FAILURES. SIX-RUN CLOSABLE ROTATION / HANDOFF TRIGGERED.**

# R06 — P0025 exterior-disc synchronous coupling: exact excursion-moment obstruction, macroscopic-excursion regeneration, and six-run handoff

## 0. Continuity and source

This run continues the exclusively claimed R06 successor

`P0025 — Krzysztof Burdzy, My favorite open problems, Problem 5(ii)`

from `runs/R06/20260918T0617Z_p0025_corner_layer_trace_smoothing_35.md`. I did not reopen the retired BENJ three-source target or the original Lyons--Peres target.

The source question, checked again on 2026-09-18 at
`https://sites.math.washington.edu/~burdzy/open_mathjax.php`, is still:

> If `D` is the complement of a non-degenerate closed disc, is it true that with positive probability `limsup_{t->infinity}|X_t-Y_t|>0` for two synchronously driven reflected Brownian motions?

The canonical claim is `operations/claims/P0025.md`. The frozen metric remains the binary source-resolution bit `E_disk`: it is `1` only after a full proof/refutation of the literal source question, and otherwise `0`.

For continuity, the original R06 assignment remains frozen exactly:

- Lyons--Peres, *Probability on Trees and Networks*, Question 6.20 asks for `Phi_V(G)` for regular, co-regular plane graphs and for `Phi_E(G),Phi_V(G)` more generally;
- R06's normalization is outer vertex boundary `partial_V K={x notin K: x~y for some y in K}` and `Phi_V=inf |partial_V K|/|K|`;
- the admissible pentagonal regime `H_{5,5}` remains `Phi_V(H_{5,5})=sqrt(5)`, certified interval `[sqrt(5),sqrt(5)]`, width `0`;
- the full Lyons--Peres source question remains **PARTIAL**;
- Haslegrave--Panagiotis triangular/codegree-3 and quadrangular/codegree-4 results, DOI `10.1002/rsa.20946`, remain excluded prior art.

## 1. Required reread and current literature

Before the mathematics I recovered/read the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, canonical `operations/claims/P0025.md`, newest R06 report 35, the exact frozen-peanut report 32, the neighboring Burdzy Problem 5(i) ownership record `operations/claims/P0024.md`, and the current queue-health successor screen.

Fresh dated literature/source checks on 2026-09-18 used the source wording and combinations of `exterior disk/disc synchronous reflected Brownian coupling limsup`, `Cranston Le Jan noncoalescence circle`, and `Burdzy differentiability reflected stochastic flow`. They recovered the live Burdzy problem page, Cranston--Le Jan (1989), Burdzy--Chen--Jones, Burdzy (2009), later pathwise-differentiability work, and later coupling surveys, but no source-matching later proof/refutation in the bounded search. This is not a global novelty certificate.

I read Burdzy's 2009 proof far enough to isolate where boundedness actually enters. The paper explicitly assumes a smooth bounded domain. Its final quantitative step is

`E Xi <= C eps^(4/3)|log eps|`  (3.166)

and then

`P(Xi>C eps^beta1) <= C eps^beta2`  (3.167),

which is summable on geometric scales. But earlier lemmas repeatedly terminate dyadic excursion-displacement sums at `diam(D)`: notably Lemma 3.4(ii), Lemma 3.5, Lemma 3.6, and the estimates feeding Lemmas 3.13--3.14. The exterior disc has no such terminal scale. The calculation below shows this is not a cosmetic proof issue: the corresponding Euclidean excursion moments are genuinely infinite.

# 2. #16 DIRECT SMALL MODEL — exact radial excursion tail

Scale the forbidden disc to the closed unit disc and write

`D_ext={z in C: |z|>1}`.

Fix `x` on the unit circle and use the standard radial-normal excursion normalization

`H^x(A)=lim_{delta downarrow 0} delta^(-1) P^{(1+delta)x}(A)`

for events measurable away from time zero. For an excursion `e`, put

`M(e)=sup_{0<=t<zeta(e)} |e(t)|`.

### Proposition 2.1 (exact exterior radial tail)

For every `R>1`,

`boxed{ H^x(M>=R)=1/log R. }`

**Proof.** Let `tau_1` and `tau_R` be the first hitting times of the circles of radii `1` and `R`. The harmonic function in the annulus `1<|z|<R` with boundary values `0` at radius one and `1` at radius `R` is

`h(r)=log r/log R`.

Therefore

`P^{(1+delta)x}(tau_R<tau_1)=log(1+delta)/log R`.

Divide by `delta` and let `delta downarrow 0`. Since `log(1+delta)/delta ->1`, the claimed excursion-law identity follows. `□`

This exact formula is rotationally invariant.

## 2.1 Exact moment phase transition in the logarithmic radius

Let `Y=log M`. Proposition 2.1 says

`H^x(Y>=y)=1/y, y>0`.

Hence the pushforward excursion measure on `(0,infinity)` has density

`dy/y^2`.

For every `a>0` and `q<1`,

`boxed{ H^x(Y^q;Y>=a)=a^(q-1)/(1-q), }`

while the same integral diverges for `q>=1`.

Equivalently, conditioned on an excursion reaching radius `R0=e^a`,

`P(Y>=y | Y>=a)=a/y, y>=a`,

and

`boxed{ E[Y^q | Y>=a]=a^q/(1-q), 0<q<1, }`

whereas `E[Y | Y>=a]=infinity`.

Even more strongly, for every `p>0`,

`boxed{ H^x(M^p;M>=e)=infinity. }`

Indeed the Stieltjes density corresponding to `H(M>=R)=1/log R` is

`dR/[R(log R)^2]`,

and

`int_e^infinity R^p dR/[R(log R)^2]=infinity`.

Thus positive Euclidean radial moments of a macroscopic exterior excursion do not exist, while fractional moments of its *logarithmic* radius exist exactly below exponent one.

# 3. #22 READ THE FAILURE — why the bounded-domain L1 route cannot be transplanted

Burdzy's bounded-domain proof uses `diam(D)` as the last dyadic shell in several places. Lemma 3.4(ii), for example, obtains an expected excursion displacement of order `b|log b|` by summing shells only up to `diam(D)`. Lemmas 3.5 and 3.6 again use `diam(D)` to turn small probabilities of large excursions into finite first-moment bounds.

Proposition 2.1 shows that replacing `diam(D)` by `infinity` is impossible: the exterior-disc analogue of the relevant positive Euclidean excursion moments is not merely unproved, it is **false**. The direct strategy

`bounded-domain differentiability estimate + an exterior cutoff sent to infinity in L1`

cannot preserve those Euclidean first-moment estimates.

This corrects the overly optimistic version of the annular-cutoff idea from earlier R06 work. Choosing `R(r)=exp(r^(-gamma))` does make the *probability* of a radius-`R(r)` excursion polynomially small, but multiplying by its Euclidean amplitude is fatal: the unconditional positive moment beyond every fixed cutoff is infinite.

The useful replacement variable is logarithmic/compactified excursion size, for which Proposition 2.1 gives the exact `q<1` moment window. More importantly for the source problem, synchronous separation itself does **not** grow with the interior Euclidean amplitude while both particles are in the bulk: before one particle reflects, the common Brownian increment leaves `X-Y` unchanged. This is why the exact boundary-endpoint/conformal-trace formulation from run 32 is the right category, rather than Euclidean excursion-amplitude control.

# 4. #4 PROVE SOMETHING WEAKER COMPLETELY — macroscopic excursion regeneration at zero separation

The heavy radial tail is not only an obstruction. It provides an exact regeneration mechanism for the limiting single-boundary trace.

Suppose Brownian motion starts at `R e^{i alpha}`, `R>1`, and stop it when it first hits the unit circle. By inversion/conformal invariance, the hitting-angle density is the Poisson kernel

`K_R(alpha,beta)
 = (1/(2pi)) (1-R^(-2))/(1-2R^(-1)cos(beta-alpha)+R^(-2))
 = (1/(2pi)) (R^2-1)/(R^2-2R cos(beta-alpha)+1).`

Therefore, uniformly in the incoming angle,

`boxed{
 (1/(2pi)) (R-1)/(R+1)
 <= K_R(alpha,beta)
 <= (1/(2pi)) (R+1)/(R-1).
}`

For `R=2`, the return density is between `1/(6pi)` and `3/(2pi)`.

Now mark the boundary excursions that reach radius `R`. Under the standard exit system, Proposition 2.1 says their characteristic-measure rate is exactly

`lambda_R=1/log R`

per unit boundary local time, independent of the boundary angle. Hence the local-time wait to the first radius-`R` excursion is exponential with rate `1/log R`, and at the end of that excursion the new boundary angle has the above Doeblin density bound, irrespective of the angle from which that excursion began.

### Corollary 4.1 (explicit tangent regeneration)

For the zero-separation / single-circle boundary trace, the stopping rule

`first excursion whose radial maximum reaches R`

is an exact regeneration device: the local-time waiting variable has exponential parameter `1/log R`, and the post-excursion angle kernel minorizes normalized Lebesgue measure by

`boxed{ (R-1)/(R+1). }`

At `R=2` the minorization constant is `1/3`.

This is a more robust smoothing device than waiting a deterministic trace time: it is tied to a concrete excursion event and survives arbitrary pre-regeneration angular history.

# 5. Frozen finite-separation extension: a bounded return density after one macroscopic excursion

Run 32 gave an exact conformal map for the frozen half-separation midpoint domain

`Omega_z=C \ (B(iz,1) union B(-iz,1))`,

for `0<=z<=z0<1`:

`a_z=sqrt(1-z^2)`,
`lambda_z=1-(2/pi)arcsin z`,
`G_z(w)=((w-a_z)/(w+a_z))^(1/lambda_z)`,

and a boundary coordinate

`p_z(s)=a_z(1+(is)^lambda_z)/(1-(is)^lambda_z)`,

with physical arclength density

`rho_z(s)=2 a_z lambda_z |s|^(lambda_z-1)/|1-(is)^lambda_z|^2`.

Fix `z0<1` and a Euclidean radius `R>1+z0`. If the frozen midpoint excursion has reached `|w|=R`, let `w` be its hitting point. Since the compact family

`{(z,w):0<=z<=z0, |w|=R}`

lies strictly inside the frozen domains, `G_z(w)=A_z(w)+iB_z(w)` has

`0<A_*<=A_z(w)<=A^*`, `|B_z(w)|<=B^*`

for constants depending only on `z0,R`.

Harmonic measure in the right half-plane therefore gives the return density in the `s` coordinate

`q_{z,w}(s)= (1/pi) A_z(w)/((s-B_z(w))^2+A_z(w)^2) <= C/(1+s^2).`

On the other hand the explicit `rho_z` formula yields uniformly in `0<=z<=z0`

`rho_z(s)>=c/(1+s^2)`:

- for `|s|<=1`, `|s|^(lambda_z-1)>=1` and the denominator of `rho_z` is uniformly bounded above;
- for `|s|>=1`, the denominator is at most `C|s|^(2lambda_z)`, so `rho_z(s)>=c|s|^(-lambda_z-1)>=c|s|^(-2)`.

Consequently the return point on the peanut boundary has a density with respect to **physical arclength** bounded uniformly:

`boxed{
 sup_{0<=z<=z0} sup_{|w|=R} sup_{s in R}
   q_{z,w}(s)/rho_z(s) <= C(z0,R)<infinity.
}`

This is a complete frozen-`z` smoothing statement. It includes the corner points by limit: for `z>0` the physical density actually tends to zero at both conformal ends.

It is directly compatible with the run-35 corner-layer estimate: after a macroscopic frozen excursion, any arclength-integrable corner drift `f_z` with `int|f_z| dsigma=O(z)` has conditional expectation `O(z)` under the return law.

## What this still does not prove

The full pair process is not frozen while either particle is reflecting. To close Burdzy 5(ii), one still needs a source-valid mechanism showing that before the separation escapes a fixed logarithmic band, the moving pair acquires such a macroscopic-excursion regeneration often enough (or an equivalent bounded-density entrance law) with constants uniform as `z downarrow0`. At the peanut corners the physical-local-time intensity of a macroscopic excursion can degenerate, so the frozen return-density lemma alone is insufficient.

Thus the remaining issue is **not** the law after a large excursion; it is the pre-excursion occupation / corner escape problem for the moving finite-separation state.

# 6. Status and six-run rotation

The source-resolution metric did not move:

`E_disk: 0 -> 0`.

This is the sixth consecutive unchanged P0025 run. Under the CLOSABLE contract, R06 therefore rotates this source now rather than producing a seventh local lemma.

P0025 disposition:

- source status: **OPEN**;
- R06 research status: **PARTIAL / RETIRED-HANDOFF**;
- unchanged count at retirement: `6`;
- no claim of source resolution;
- no claim that the excursion identities are literature-new; novelty is **UNVERIFIED**;
- handoff obstruction: prove a uniform moving-state pre-regeneration/corner-escape estimate, then combine it with the explicit macroscopic return smoothing, run-35 `O(z)` corner drift, the exact tangent zero drift/nonzero variance, and the Lamperti recurrence compiler.

The latest coordinator-grade successor screen available in the repository (`operations/task_health/runs/2026-09-17T225500Z/queue_screening.md`) found **0 newly certified free READY+CLOSABLE+UNASSIGNED successors**, and root `QUEUE.md` itself warns that stale/PENDING rows are not dispatchable. A bounded current ownership delta also confirms that attractive stale candidates such as I0011, I0035, I0066, I0082 and neighboring P0024 are claimed or retired elsewhere. I therefore do **not** auto-promote a PENDING row or steal another track's target.

R06 successor state after this handoff:

`SUCCESSOR_ADMISSION_REQUIRED`.

No new ownership claim is created in this run.

# 7. No checker manufactured

The new claims in this run are analytic identities/inequalities with proofs on the page. There is no finite combinatorial claim whose validity depends on an exact-arithmetic enumeration. In accordance with the 90/10 rule, I did not manufacture a certificate-only script for an unchanged source metric.

# 8. Scheduler/model control status

The requested model line remains prompt text only. The scheduler control surface exposed to this task supports title/prompt, schedule or relative start, timing mode, and enabled state. It exposes no binding model-family field, no reasoning-effort field, no authenticated completed-run model attestation, and no guaranteed hour-long execution field. The repository's operative follow-up manifest records the same limitation.

The historical P26 task ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in one authorization context. This is an authorization boundary, not evidence of a hidden model selector. The legitimate workaround is the owning/admin/product context; enforcing GPT-6 at maximum would require the scheduler/backend to expose persistent model and reasoning controls plus authenticated applied-run telemetry. No scheduler modification or permission bypass was attempted here.

# 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  portfolio: CLOSABLE_OUTSIDE
  source:
    active: P0025
    author: Krzysztof Burdzy
    title: My favorite open problems
    problem: 5(ii), Convergence of synchronous couplings
    literal_scope: exterior of a nondegenerate closed disc; synchronous reflected Brownian pair; positive-probability positive limsup separation
  metric:
    name: E_disk
    before: 0
    after: 0
    movement: false
  status_before: OPEN_PARTIAL
  status_after: OPEN_PARTIAL_RETIRED_HANDOFF
  unchanged_count_before: 5
  unchanged_count_after: 6
  tried_moves: [4,16,22]
  new_evidence:
    - exact exterior excursion tail H^x(M>=R)=1/log R
    - exact logarithmic-radius q<1 moment phase transition and divergence of every positive Euclidean radial moment
    - exact macroscopic-excursion regeneration for the unit-circle boundary trace with rate 1/log R and Doeblin constant (R-1)/(R+1)
    - uniform frozen-peanut physical-arclength density bound after return from a fixed macroscopic radius
    - explicit proof-level identification of why Burdzy-2009 bounded-domain Euclidean L1 estimates do not transplant directly
  corrections:
    - earlier annular-cutoff idea cannot control Euclidean excursion amplitudes in L1; positive radial moments are infinite
  remaining_obligation: >-
    Prove a scale-uniform moving-state pre-regeneration/corner-escape estimate for the finite-separation exterior-disc pair; then combine bounded-density regeneration with the O(z) corner-drift estimate, tangent critical cocycle, and recurrence compiler.
  closure_audits: []
  rotation:
    triggered: true
    reason: six consecutive unchanged source-metric runs
    successor: SUCCESSOR_ADMISSION_REQUIRED
    successor_claim: null
  original_I0056_preserved:
    graph: H_{5,5}
    normalization: outer vertex boundary
    interval: '[sqrt(5),sqrt(5)]'
    width: 0
    source_status: PARTIAL
    excluded_prior_art: Haslegrave-Panagiotis triangular/quadrangular cases
```
