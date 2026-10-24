Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `L_cone: pi/4 -> pi/4`; unchanged-count remains `UNKNOWN -> UNKNOWN`. Methods actually tried: #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #18 SAY IT IN ANOTHER LANGUAGE, #29 ADD THE POINTS AT INFINITY.**

# R14 HARD OUTSIDE — H0017: positive-temperature endpoint interpolation is exactly a mixture, so a new slope must come from a new extremal harmonic ray or a spatial shock limit

Repository / branch: `yspennstate/math-open-problems` / `master`.  
Date: 2026-09-17 UTC.

## 1. Continuity, ownership, exclusions, and source freshness

I did **not** reopen the original negative-margin spherical Gaussian perceptron. Its supported handoff bracket remains

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width `6.48139658710`. The intervening I0089 and `RS-2026-BIS32` hard targets also remain handed off. Their reports are preserved and are not authorization to restart them.

The active exclusive R14 target remains **H0017**, Daniel Ahlberg, Maria Deijfen and Matteo Sfragara, *Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589v1 (8 July 2026), under `operations/claims/H0017.md`.

At run start I recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the H0017 exclusive claim, and the newest own H0017 report

`runs/R14/2026-09-17T19-52-59Z_h0017_recovering_cocycle_tropical_barrier_b7c2.md`.

The current root ledger still has an old static R14/perceptron row and explicitly says R-series workers must recover newer complete own reports before replacing prior state. The exclusive H0017 claim and the complete R14 report are newer and controlling for this worker. No peer file or shared root was edited.

A bounded fresh primary-source search again found arXiv:2607.07589v1 as the source-matching current cone-survival preprint; I found no later primary paper claiming the full all-direction result. The source proves the `pi/2` threshold in tangent directions and extinction at `alpha=pi/2` in every direction, while retaining the unconditional all-direction `pi/4` survival baseline. A negative search is not a novelty certificate.

I also checked Sean Groathouse, Christopher Janjigian and Firas Rassoul-Agha, *Existence of generalized Busemann functions and Gibbs measures for random walks in random potentials*, Trans. AMS 378 (2025), which includes zero-temperature first-passage settings. Their construction uses extremal supergradients in the main existence theorem, and their zero-temperature recovery relation produces semi-infinite geodesics after a covariant tie-breaker. This supports the distinction from the previous R14 report: the missing bridge is not merely “recovering cocycle -> geodesic,” but an **extremal/interior-slope construction plus coalescence** in the source iid planar setting.

Other nearby literature checked this run includes Chaika--Krishnan on stationary coalescing walks, Damron--Hanson on bigeodesics under differentiability hypotheses, and Brito--Damron--Hanson on point-to-hyperplane geodesic graphs. These results sharpen the coalescence obstruction but do not give the required source-wide corner-interior coalescing family.

## 2. Frozen metric and retained H0017 reductions

For a source-admissible iid continuous law `F`, retain

`alpha_c^F(theta) := sup { alpha : P_F(G^{theta,alpha}) > 0 }`

and the source-wide fixed metric

`L_cone := inf_F inf_theta alpha_c^F(theta)`.

The source certifies

`L_cone >= pi/4`,

and full source closure is `L_cone=pi/2`.

The retained R14 self-check reductions remain:

`alpha_c^F(theta) = pi/2 - dist(theta,C_*(F))`                           (R2)

in the endpoint sense, where `C_*(F)` is the deterministic closed Ahlberg--Hoffman set of slopes of random coalescing geodesics;

`ell(F):=inf_theta alpha_c^F(theta)=pi/2-covrad(C_*(F))`;                (R2')

`ell(F)=pi/4` iff `C_*(F)` is one four-point quarter-turn orbit;         (R4)

full `D4` symmetry restricts the exact four-ray state to the axis orbit or the diagonal orbit; and one new midpoint coalescing slope in an exact four-ray state would force eight equally spaced slopes and the law-level jump `ell(F)>=3pi/8`. None of these law-level statements alone moves the universal `L_cone`.

Metric this run:

`L_cone: pi/4 -> pi/4`.

The authoritative unchanged-run field available to this worker remains `UNKNOWN`, so I preserve `UNKNOWN -> UNKNOWN` rather than inventing a stagnation count.

## 3. Method #5 — ADD A PARAMETER AND DIFFERENTIATE: a positive-temperature two-endpoint interpolation no-go theorem

The preceding report proposed using positive temperature to soften the zero-temperature max-plus shock. This run tests that route exactly.

The algebra below is intentionally formulated for a general positive transfer kernel, so it is independent of sign conventions. Let `K(x,y)>=0` be a kernel on a countable state space and suppose two strictly positive functions `h^-` and `h^+` are `K`-harmonic:

`h^\pm(x) = sum_y K(x,y) h^\pm(y)`.

In the random-potential/Busemann setting, such harmonic functions encode the endpoint Doob/Gibbs states. Fix `beta>0` and a real interpolation parameter `c`; put

`a := exp(beta c)`,

`h_c := h^- + a h^+`.

Linearity of the positive-temperature harmonic equation gives immediately

`h_c(x)=sum_y K(x,y)h_c(y)`.

Define the endpoint and interpolated Doob kernels

`P^\pm(x,y):=K(x,y) h^\pm(y)/h^\pm(x)`,

`P_c(x,y):=K(x,y) h_c(y)/h_c(x)`,

and the local soft branch weight

`q_c(x):= a h^+(x)/h_c(x) in (0,1)`.

Then there is an exact identity

`P_c(x,y) = (1-q_c(x)) P^-(x,y) + q_c(x) P^+(x,y)`.                    (R12a)

This one-step formula is already suggestive, but the stronger path-law statement is the real obstruction.

Let `Q_h^x` denote the Doob path law started from `x`. For a cylinder path `x=x_0,x_1,...,x_n`,

`Q_h^x[x_0,...,x_n] = (prod_{i=0}^{n-1} K(x_i,x_{i+1})) h(x_n)/h(x_0)`.

Using `h_c=h^-+a h^+`, the numerator splits linearly while the denominator is fixed, so on **every cylinder event**

`Q_c^x = (1-q_c(x)) Q_-^x + q_c(x) Q_+^x`.                            (R12b)

Thus an ordinary positive harmonic sum of the two endpoint states creates **no third extremal Gibbs/Doob state at all**. It is literally a convex mixture of the two endpoint path measures, with the branch chosen once at time zero.

This is the finite-temperature analogue of the preceding zero-temperature interpolation barriers. It is stronger than saying “the interpolation might collapse to an endpoint”: it gives the exact decomposition before taking any limit.

### The interpolation derivative

Define the soft potential

`H_{beta,c}(x) := beta^{-1} log h_c(x)`.

Then exactly

`partial_c H_{beta,c}(x)=q_c(x)`,                                      (R12c)

and

`partial_c q_c(x)=beta q_c(x)(1-q_c(x))`.                              (R12d)

Since `q_c(x)` increases from `0` to `1` as `c` runs from `-infinity` to `+infinity`,

`integral_{R} beta q_c(x)(1-q_c(x)) dc = 1`.                           (R12e)

So `beta q(1-q) dc` is a canonical soft-shock localization in the external parameter. This looked like a possible way to Palm-normalize the transition between endpoint phases. The next section shows that the **one-point** version is exactly sterile.

The identities R12a--R12e are complete on-page self-checks, not source closure and not novelty-certified theorems.

## 4. Method #18 — SAY IT IN ANOTHER LANGUAGE: hidden branch, posterior martingale, and a one-point Palm obstruction

Equation R12b has a useful probabilistic language. Introduce a hidden endpoint label `J in {-,+}` at time zero with

`P(J=+)=q_c(x)`.

Conditioned on `J`, sample the path from `Q_J^x`. The resulting marginal path law is exactly `Q_c^x`.

Bayes' formula plus the telescoping Doob density gives

`P(J=+ | X_0,...,X_n)=q_c(X_n)`.                                      (R13a)

Consequently `q_c(X_n)` is a bounded martingale under `Q_c^x`:

`E_{Q_c^x}[q_c(X_{n+1}) | X_n]=q_c(X_n)`.                              (R13b)

This changes the interpretation of the “soft shock.” The soft interpolation is not a new phase wandering between two endpoint phases. It is the evolving **posterior uncertainty about a single endpoint phase that was selected at time zero**.

That language exposes a second exact no-go. Weight the interpolated path law by the natural local susceptibility from R12d:

`beta q_c(x)(1-q_c(x)) dc`.

For any cylinder event `A`, change variables from `c` to `q=q_c(x)` using `dq=beta q(1-q)dc`. Since R12b gives

`Q_c^x(A)=(1-q)Q_-^x(A)+q Q_+^x(A)`,

we obtain

`integral_R beta q_c(x)(1-q_c(x)) Q_c^x(A) dc`

` = integral_0^1 [(1-q)Q_-^x(A)+qQ_+^x(A)] dq`

` = (1/2)Q_-^x(A)+(1/2)Q_+^x(A)`.                                    (R13c)

Therefore **Palm-normalizing only at a one-site soft-shock parameter produces exactly the 50/50 endpoint mixture**. It cannot create an interior extremal state.

This is a certified obstruction to the simplest positive-temperature implementation of the previous run's shock idea. Any useful shock construction has to condition on a genuinely **spatial** interface event -- for example a crossing of a Busemann-difference level set through a transverse window -- rather than just biasing the external parameter by the local derivative of a two-state softmax.

### Zero-temperature compatibility

If along a low-temperature sequence

`beta^{-1} log h^\pm(x) -> H^\pm(x)`,

then

`beta^{-1} log(h^-(x)+exp(beta c)h^+(x))`

converges to

`max{H^-(x),H^+(x)+c}`.

Thus this positive-temperature calculation lands exactly on the max-plus/tropical family from the previous report. The endpoint-mixture identity is the soft precursor of the zero-temperature phase-locking obstruction, not a way around it.

## 5. Method #29 — ADD THE POINTS AT INFINITY: the two-ray harmonic cone has no new extremal boundary point

The same no-go has a clean projective/Martin-boundary interpretation.

The positive harmonic functions generated by the endpoint pair form the two-dimensional cone

`C = { a h^- + b h^+ : a,b>=0 }`.

Projectivizing by positive scalar multiplication turns `C\{0}` into a compact interval. Its only extremal rays are `[h^-]` and `[h^+]`. Every interior point has a nontrivial positive decomposition and, by R12b, its associated Doob/Gibbs state is nonextremal.

So “adding the points at infinity” of **this two-ray cone** does not reveal a hidden midpoint state. There is none. A new interior Busemann/coalescing class must arise from something genuinely outside `cone{h^-,h^+}`:

1. a new minimal/extremal positive harmonic ray, equivalently a new relevant Martin-boundary point; or
2. a singular spatial-interface conditioning/limit in which the order of limits is not equivalent to forming the ordinary endpoint harmonic sum first.

This also clarifies why the generalized-Busemann construction is naturally phrased with **extreme supergradients**. The source-moving object is an extremal state; an interior convex combination of two already known extremal rays cannot manufacture it.

The generalized-Busemann paper does supply weak compactness/continuity tools for sequences of recovering cocycles. A conceivable route is therefore to find finite-temperature **extreme** states whose mean slopes approach an interior zero-temperature corner support functional as temperature tends to zero, and only then pass to a zero-temperature recovering limit. The present calculation says ordinary endpoint sums can never serve as those extreme approximants.

I found no general theorem in the checked literature guaranteeing that an arbitrary interior zero-temperature corner support functional is approximated by such extreme finite-temperature states in the source iid FPP class.

## 6. Coalescence remains the second independent obstruction

Even if the previous extremal-harmonic problem were solved and an interior recovering cocycle were constructed, H0017 still needs a route into the Ahlberg--Hoffman **coalescing** slope set `C_*`.

Chaika--Krishnan's stationary compatible-walk theorem is useful here: in two dimensions, a translation-invariant compatible family has a sharp alternative between coalescence and a positive density of bi-infinite trajectories. Applied to a covariantly selected calibrated-geodesic forest, this suggests that failure of coalescence should produce a bigeodesic-type obstruction.

But current bigeodesic results do not close that alternative in the corner regime needed here. Damron--Hanson exclude deterministic-direction bigeodesics under differentiability hypotheses, and Brito--Damron--Hanson obtain no backward-infinite paths for specific point-to-hyperplane geodesic-graph limits. I found no theorem excluding bi-infinite trajectories for an **arbitrary** recovering-cocycle forest at a nondifferentiable corner under only the H0017 source assumptions.

So there are now two sharply separated missing inputs:

- **extremality:** produce a new harmonic/recovering ray with an interior corner support slope, rather than a convex mixture of endpoint states;
- **coalescence:** show its covariant geodesic family belongs to one coalescence class, or otherwise force a contradiction from the resulting bi-infinite trajectories.

Both are genuinely structural. Neither is another optimization of the existing `pi/4` constant.

## 7. What changed mathematically this run

There is no fixed-metric movement, but the proposed positive-temperature escape route has been decisively classified.

Before this run the route was “soften the endpoint shock at finite temperature and take an extremal zero-temperature limit.” After the calculations above:

- every ordinary positive linear combination `h^-+exp(beta c)h^+` yields **exactly an endpoint path-law mixture** (R12b);
- the local soft branch weight is a posterior martingale (R13a--R13b), so the apparent switching is inference about a hidden endpoint label, not a new phase;
- the natural one-point derivative/Palm bias integrates to the exact 50/50 endpoint mixture (R13c);
- projectivizing the two-ray harmonic cone adds no new extremal ray;
- therefore any successful finite-temperature route must create a **new minimal harmonic ray** or use a genuinely **spatial** shock/interface conditioning whose limit is singular relative to ordinary endpoint summation;
- even after that, planar coalescence remains a separate obligation.

This is a certified obstruction to the simplest #5/#18/#29 route and prevents another run from repackaging endpoint mixtures as an interior Busemann state.

## 8. The simplest next source-valid target

The cleanest remaining special target is not the full continuum of missing slopes. It is:

> **Spatial-shock insertion at an exact four-ray law.** Assume `ell(F)=pi/4`, so the only realized slopes are one axis/diagonal D4 orbit. For one adjacent endpoint pair, construct from the spatial Busemann-difference interface an extremal stationary recovering state whose mean slope is the gap midpoint, and prove its selected geodesic forest coalesces.

By the retained R11 argument, success for one midpoint plus `D4` symmetry would force eight realized slopes and contradict exact four-ray equality. This remains law-level, not universal-metric movement, but it is the smallest nontrivial test of the new mechanism.

A stronger source-closing route would construct an interior coalescing slope in every nonempty gap of `C_*`, then iterate gap splitting to obtain a dense closed slope set and hence `C_*=S`, giving `ell(F)=pi/2` for every admissible law.

## 9. Next genuinely different methods

Next H0017 triple:

- **#1 CHANGE THE CATEGORY.** Move the missing-slope problem from FPP geometry to the minimal Martin boundary / extremal positive harmonic-ray problem. Ask for a new minimal harmonic point between neighboring endpoint rays, not another cocycle average.
- **#22 READ THE FAILURES, NOT THE SUCCESSES.** Read the bigeodesic/coalescence and nonuniqueness literature specifically for where planar finite-energy arguments fail at corners; isolate the exact hypothesis differentiability supplies and test whether spatial-shock extremality can replace it.
- **#28 REPLACE FOR ALL WITH FOR TYPICAL.** Do not demand a stationary interface geodesic for every `c`. Palm-condition on a *typical spatial crossing* of the Busemann-difference shock through a transverse window and ask whether the Palm path is extremal/coalescing. R13c proves that a one-point parameter Palm is useless, so the conditioning must be spatial.

These are genuinely different from the just-exhausted endpoint interpolation route.

## 10. Honest status and closure discipline

H0017 remains **OPEN / PARTIAL**.

New self-checks this run:

- R12a--R12b: positive harmonic endpoint sums give exact endpoint mixtures, including the full path law;
- R12c--R12e: exact external-parameter derivative and normalized soft-shock susceptibility;
- R13a--R13b: hidden-endpoint posterior martingale representation;
- R13c: one-point derivative/Palm bias equals exactly the 50/50 endpoint mixture;
- projective two-ray cone obstruction: no new extremal harmonic ray appears inside the cone generated by the two endpoint rays.

External audits: `0/2`.

No finite checker was created because these are exact analytic kernel/Doob identities, not finite computational claims. No paper folder is created; source closure conditions are not met.

The bounded prior-art check found no source-matching full H0017 resolution and no theorem supplying both interior-corner extremality and coalescence under the full source assumptions. This is bounded negative evidence only.

## 11. Model / scheduler control

The exposed task interface still provides prompt/title/schedule/timing/enablement controls but no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. The actual model exposed to this run is GPT-5.6 Sol; the reasoning level is not exposed and is therefore reported as `UNVERIFIED`. GPT-6/maximum remains prompt text only on this surface.

The repository ledger records that the historical P26 `You cannot modify this task` failure was authorization-context dependent and that a later full update succeeded from an authorized P/C context. If an ID still refuses modification, the legitimate route is its authorized owning workspace/account context or platform support. No scheduler change, permission change, duplicate task, or bypass was attempted in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R14
  allocation: HARD_OUTSIDE
  active_target: H0017
  source: arXiv:2607.07589v1
  status: OPEN/PARTIAL
  metric_name: L_cone
  metric_before: pi/4
  metric_after: pi/4
  movement: no
  unchanged_count_before: UNKNOWN
  unchanged_count_after: UNKNOWN
  methods_this_run: [5, 18, 29]
  new_self_checks:
    - R12a endpoint Doob-kernel mixture identity
    - R12b full path-law endpoint mixture identity
    - R12c-R12e soft-parameter derivative and normalized susceptibility
    - R13a-R13b hidden-branch posterior martingale
    - R13c one-point Palm susceptibility gives exact 50/50 endpoint mixture
    - projective two-ray cone has no new extremal harmonic ray
  external_audits: 0/2
  certified_obstruction: >-
    Ordinary finite-temperature harmonic interpolation of two endpoint states is exactly
    a nonextremal endpoint mixture, and even the natural one-point derivative/Palm bias
    is exactly the half-half endpoint mixture. A new slope therefore requires a new
    minimal harmonic ray or a genuinely spatial singular interface limit; after that,
    coalescence is still a separate obligation.
  remaining_obligation: >-
    Construct an extremal interior-corner recovering state by a mechanism not contained
    in the positive cone of the endpoint harmonic functions, and prove its planar
    covariant geodesic forest coalesces; or find a different source-valid route that
    yields a uniform angular insertion theorem.
  next_methods: [1, 22, 28]
```
