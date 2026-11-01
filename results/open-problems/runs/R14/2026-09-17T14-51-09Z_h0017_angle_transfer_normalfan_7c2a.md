Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. BIS32 HANDOFF COMPLETED; new H0017 metric initialized `L_cone: pi/4 -> pi/4` (NO MOVEMENT). Methods actually tried: #2 ATTACK THE NEGATION FIRST, #6 DEFORM TO A POINT YOU CAN SOLVE, #11 DUALIZE.**

# R14 HARD OUTSIDE — terminal BIS32 handoff and H0017 cone-survival first attack

Repository / branch: `yspennstate/math-open-problems` / `master`.  
Date: 2026-09-17 UTC.

## 1. Continuity and mandatory handoff

I did not reopen the original negative-margin spherical Gaussian perceptron. Its supported handoff bracket remains

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width `6.48139658710`. I also did not reopen the intervening I0089 Riesz target.

The immediately preceding active R14 target was `RS-2026-BIS32`, Randomstrasse Conjecture 32. Its newest immutable report is

`runs/R14/2026-09-17T13-52-32Z_rs2026bis32_stuck2_gauge_decoder_barrier.md`.

That report records `D_bis: 2 -> 2`, unchanged count `4 -> 5`, and **STUCK-RECOVERY-2/2**. The owner protocol therefore forbids a third BIS32 recovery. This run releases BIS32 from the R14 attacking slot and preserves, rather than extends, its handoff state.

### BIS32 handoff payload preserved

The strongest exact identities are:

- for spins `sigma, eta`, with `tau=sigma eta` and `F_eta` the uncut edges of `eta`,
  `R_eta(sigma) = sum_{uv in F_eta} sigma_u sigma_v = (H_G(sigma)+H_G(sigma eta))/2`;
- `<sigma,eta>` is exactly the magnetization of `tau`;
- for cubic `G`, `cut(tau)=3n/2-cut(sigma)-R_eta(sigma)` and balancing `tau` costs at most `(3/2)|<sigma,eta>|` cut edges;
- unrestricted good-gauge existence is essentially equivalent to the original MinBis/MaxBis defect, so local-stable-gauge entropy is not by itself a reduction;
- in the Hamilton-cycle planted model `G=C union M`, with the alternating cycle gauge `eta_C` and a fixed balanced `sigma`,
  `E_M R_{eta_C}(sigma)=(a^2-2n)/(4(n-1))`, `a=<sigma,eta_C>`; the genuine missing theorem is quenched control when the extremal bisection is a function of the same matching `M`.

Recommended fresh-owner BIS32 route remains **#6 / #25 / #28**: deform to the Hamilton-cycle model, double-count triples `(G,C,sigma_ext)`, and prove a typical-extremizer quenched statement rather than a uniform statement over all balanced spins.

No claim of BIS32 closure is made.

## 2. Required repository recovery and successor eligibility

Before claiming a successor I recovered/read the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, current `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the newest own R14 report above, and targeted neighboring/current task material. The intake ledgers are too large to render byte-for-byte through one connector response, so I used exact-ID/source retrieval for the successor candidate rather than pretending to have rendered all ~780 entries.

The current task-health screen at `operations/task_health/runs/2026-09-17T095600Z/queue_screening.md` identifies H0017 as **OPEN-LOOKING / HARD** and not as a CLOSABLE replacement. Direct fetch of `operations/claims/H0017.md` returned 404 immediately before the claim; bounded repository search found intake/queue/task-health mentions but no competing canonical H0017 claim or H0017 research report.

I therefore created the create-only R14 claim

`operations/claims/H0017.md`

at commit

`53437b0c3aa19e1c550f424ebbc019c97c401b7e`.

## 3. New source H0017 and exact target

Primary source:

Daniel Ahlberg, Maria Deijfen, Matteo Sfragara, *Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589v1, 8 July 2026.

Model: nearest-neighbor FPP on `Z^2` with i.i.d. continuous edge weights supported on `[0,infinity)` and

`E[min{omega_1,...,omega_4}^2] < infinity`.

The two competing types have the same passage-time law. Type 2 starts at the origin. Type 1 occupies `C_alpha^theta \ {0}`, where `C_alpha^theta` is the cone of half-angle `alpha` centered about the ray in direction `-theta`. Let `G^{theta,alpha}` be survival of type 2.

Benjamini's target retained here is the all-direction statement

`P(G^{theta,alpha}) > 0  iff  alpha < pi/2`

for every source-admissible law and every `theta`.

What the July 2026 paper already proves must not be re-claimed:

1. If the asymptotic shape has a tangent in direction `theta`, Theorem 1 proves the full threshold `pi/2` in that direction.
2. Theorem 5 proves extinction at the flat case `alpha=pi/2` for **every** direction without an unverified geodesic assumption.
3. The paper states that differentiability of the general i.i.d. FPP asymptotic shape is widely believed but open.
4. It also states the unconditional all-direction survival baseline `alpha<pi/4`, leaving the geometric detail to the reader.

Fresh exact-title/author/current-FPP searches on 2026-09-17 found no later primary theorem claiming the full all-direction result. Ahlberg's current Stockholm University page still lists the July paper among his preprints. This is bounded negative evidence, not a novelty certificate.

## 4. Frozen H0017 metric

Define

`L_cone := sup { ell in [0,pi/2] : for every source-admissible passage-time law, every theta, and every alpha<ell, P(G^{theta,alpha})>0 }`.

The source gives the rigorous baseline

`L_cone >= pi/4`.

I freeze the supported R14 value as **`L_cone = pi/4`** for metric bookkeeping: this means `pi/4` is the largest source-wide endpoint currently certified in this track, not that the true supremum is known to equal `pi/4`. Full Benjamini closure is the endpoint `pi/2`, since Theorem 5 already supplies extinction at the flat case and larger cones only give type 1 more initial sites.

Before this run: new target, metric uninitialized in R14.  
After source recovery: certified endpoint `pi/4`.  
Research movement after initialization: **none**.

## 5. Method #2 — attack the negation first

The fastest possible win would be a source-admissible counterexample: an i.i.d. **continuous** passage-time law satisfying the source moment assumption for which some direction has critical angle below `pi/2`.

The source itself warns that this phenomenon occurs in broader stationary/ergodic FPP models: it cites an octagonal-shape example with critical angle below `pi/2` in diagonal directions and a diamond-shape example with critical angle exactly `pi/4` in coordinate directions. But it explicitly says these polygonal examples do **not** fit the present i.i.d. setting.

I tried to port the mechanism rather than the model. It immediately hits a classical unresolved wall: a corner of the i.i.d. continuous FPP limit shape would provide the same normal-fan obstruction, but general differentiability of that shape is itself open. Taking a continuous passage-time law very close to deterministic weights only makes the limit shape heuristically close to the `l^1` diamond; it does not prove a genuine corner and therefore does not produce a source counterexample.

**Outcome #2:** no source-valid counterexample. More importantly, the negation route has been reduced to constructing a genuine corner/non-differentiable direction for an i.i.d. continuous FPP asymptotic shape, a problem not currently solved by the literature located here. Polygonal stationary/ergodic examples are useful warnings but not admissible counterexamples.

## 6. Method #6 — exact angular transfer from a solved direction

This run fills in, explicitly, the geometric transfer that the source leaves to the reader. It is source-implied mathematics, not a novelty claim.

### R14-H0017-L1 (angular Busemann transfer)

Let `phi` be a direction for which almost surely there exists an infinite geodesic whose Busemann function is asymptotically linear with direction `phi`. Let

`delta = d_S1(theta,phi)`

be the smaller circular angular distance. If

`alpha + delta < pi/2`,

then

`P(G^{theta,alpha}) > 0`.

### Proof

The cone `C_alpha^theta` is centered about `-theta`. Rotating the center by `delta` and increasing the half-angle by `delta` gives the deterministic inclusion

`C_alpha^theta subset C_{alpha+delta}^phi`.

Run both competition processes in the same edge-weight environment. In the `phi` process, type 1 starts from the **larger** initial set `C_{alpha+delta}^phi \ {0}`. For any vertex `z`, its type-1 arrival time is

`T(I_1,z)=inf_{x in I_1} T(x,z)`.

Shrinking the type-1 initial set can only increase this arrival time, while the type-2 arrival time `T(0,z)` is unchanged. Hence every type-2 vertex in the larger-initial-type-1 process is also type 2 in the smaller-initial-type-1 process. Survival is therefore monotone in the needed direction.

Since `alpha+delta<pi/2`, Theorem 4 of Ahlberg--Deijfen--Sfragara gives positive type-2 survival for the larger cone in direction `phi`. The inclusion/monotonicity coupling transfers that survival to `C_alpha^theta`. QED.

### Consequence

If `B` is any set of directions with Busemann-linear geodesics, then directionwise

`alpha_c(theta) >= pi/2 - dist(theta,B)`

in the natural lower-threshold sense. Thus the whole problem can be attacked by improving the angular covering radius of a rigorously available Busemann-direction set.

For tangent directions the Damron--Hanson theorem supplies exactly such Busemann-linear geodesics. Lattice symmetry/convexity gives tangent directions with maximum uncovered angular interval at most `pi/2`, hence covering radius at most `pi/4`; L1 therefore recovers the source's all-direction `alpha<pi/4` statement rigorously.

**Outcome #6:** exact transfer established, but no endpoint beyond the already-source-recorded `pi/4`; fixed metric does not move.

## 7. Method #11 — dualize to the normal fan of the limit shape

Let `T(A)` denote the set of tangent **normal directions** of the deterministic asymptotic shape `A`, using the source's convention. Define the circular covering radius

`r(A) = sup_theta dist(theta,T(A))`.

By L1 plus Damron--Hanson,

`type 2 survives for every theta whenever alpha < pi/2 - r(A)`.

In planar convex geometry the directions missing from `T(A)` are precisely the interiors of normal cones at nondifferentiable boundary points (corners). If `omega_*(A)` is the largest angular width of such a normal cone, then

`r(A) = omega_*(A)/2`

(with the harmless convention `omega_*=0` for an everywhere differentiable boundary). Therefore the complete output of the **tangent/Busemann-transfer route** is the deterministic bound

`alpha < pi/2 - omega_*(A)/2`.

This makes the route's obstruction exact:

- source symmetry gives `omega_*(A) <= pi/2`, hence `alpha<pi/4`;
- proving `omega_*(A)=0` is exactly proving differentiability of the limit shape and would recover the full `pi/2` threshold through this route;
- a positive corner width leaves a corresponding angular loss for every proof that uses only a neighboring tangent Busemann direction plus cone containment.

This is **not** an equivalence between Benjamini's conjecture and differentiability. The conjecture might still be provable at a corner by a new geodesic/competition argument not requiring an asymptotically linear Busemann geodesic in the exact cone direction. What is proved here is a route characterization: improving the theorem by the existing tangent-transfer mechanism is the same as controlling the largest normal cone.

I also checked the tempting Ahlberg--Hoffman random-coalescing-geodesic route. Their theory gives coalescing geodesics with linear Busemann functions and density in geodesic space, but density in the path topology does not force density of their asymptotic supporting directions: arbitrarily long common initial segments do not control the eventual support functional. The 2026 source itself notes that the random-coalescing reformulation is not of further benefit for its purpose. So this does not currently shrink `r(A)`.

**Outcome #11:** certified structural obstruction. The existing Busemann machinery cannot move `L_cone` beyond `pi/4` without genuinely new information on corner normal cones or a proof mechanism that bypasses exact-direction linear Busemann functions.

## 8. What changed and what did not

New useful information this run:

- BIS32 was lawfully handed off after the second and final HARD recovery rather than receiving a forbidden third recovery.
- H0017 was source/current-status/ownership checked and claimed as R14's new HARD successor.
- the source's omitted `pi/4` argument is now written as an exact angular-transfer lemma;
- the tangent/Busemann route is reduced to the normal-fan quantity `omega_*(A)`, identifying exactly why it stalls;
- the obvious counterexample strategy is shown to require a source-admissible i.i.d.-continuous corner construction, not the known stationary/ergodic polygon examples.

What did **not** change:

`L_cone` remains at the certified source-wide endpoint `pi/4`.

No numerical simulation, near-deterministic heuristic, stationary/ergodic polygon example, or restricted tangent-direction theorem is promoted to metric movement.

## 9. Next methods if H0017 continues

Do not repeat #2/#6/#11 next run. The strongest genuinely different triple is:

- **#15 BREAK THE SYMMETRY ON PURPOSE:** study a cone axis lying strictly inside one hypothetical corner normal cone and ask whether the flat-case coalescence argument can be tilted to prove survival without an exact-direction Busemann geodesic;
- **#20 FIND WHY THE ALGORITHM FAILS:** isolate the exact step in the Section-3 local-modification proof that needs negativity of one linear Busemann functional on the entire cone, then replace it by two one-sided Busemann functionals at the corner endpoints;
- **#25 COUNT THE SAME THING TWICE:** attempt a two-geodesic/two-functional shielding construction, counting access to the escape corridor from both corner sides, rather than demanding a single functional centered at `theta`.

This is the most promising bypass of the differentiability barrier found in this run: use the two extreme support functionals of a corner simultaneously. It is capable in principle of proving survival for axes inside a normal cone without proving the shape differentiable.

## 10. Model / scheduler / access reality

The runtime that actually produced this report identifies as GPT-5.6 Sol; reasoning level is not authenticated, hence `UNVERIFIED`. I do not claim GPT-6 maximum.

The exposed scheduler/task controls still provide title, prompt, schedule/timing and enablement, but no model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long execution. Making GPT-6/maximum enforceable would require an owner-side product/API scheduler that exposes those fields and reports the applied runtime, or a platform-side change.

A task returning `You cannot modify this task` is an ownership/authorization-context boundary. The lawful workaround is to use the authorized owning workspace/account context, explicit ownership transfer if available, or platform support. Creating a duplicate task or bypassing permissions is not a valid workaround.

No scheduler modification, email, Drive operation, public posting, purchase, permission change, workflow execution, or peer-file edit was performed.

## 11. Structured ledger_delta

```json
{
  "worker": "R14",
  "predecessor": {
    "target": "RS-2026-BIS32 / Randomstrasse Conjecture 32",
    "metric": "D_bis",
    "value": "2",
    "status": "OPEN_PARTIAL_HANDOFF",
    "stuck_recoveries": "2/2",
    "rotation": "MANDATORY_COMPLETED",
    "new_research_on_predecessor": false
  },
  "active_target": {
    "id": "H0017",
    "source": "Ahlberg-Deijfen-Sfragara, arXiv:2607.07589v1, Benjamini cone-survival question",
    "category": "HARD_OUTSIDE",
    "claim_commit": "53437b0c3aa19e1c550f424ebbc019c97c401b7e",
    "metric": "L_cone",
    "before": "UNINITIALIZED_IN_R14",
    "source_recovered_baseline": "pi/4",
    "after_research": "pi/4",
    "movement": "NO_MOVEMENT_AFTER_INITIALIZATION",
    "status": "OPEN_PARTIAL"
  },
  "methods_this_run": [2, 6, 11],
  "new_on_page_results": [
    "R14-H0017-L1 angular Busemann transfer (source-implied detail, not novelty claim)",
    "normal-fan characterization of the tangent-transfer obstruction"
  ],
  "counterexample_search": "NO_SOURCE_VALID_COUNTEREXAMPLE; polygonal stationary/ergodic examples violate the iid source scope",
  "exact_checker": "NONE; no finite claim introduced",
  "audits": "NOT_READY; no closure claim",
  "next_methods": [15, 20, 25]
}
```
