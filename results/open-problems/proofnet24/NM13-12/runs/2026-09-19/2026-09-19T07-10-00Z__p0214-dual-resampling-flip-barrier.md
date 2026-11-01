Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `U_T: 3/4 -> 3/4`; Section-B methods actually tried: #11 DUALIZE, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT.**

# NM13-12 — P0214 second substantive run: dual resampling / Delaunay-flip barrier

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-12` / `proofnet24/NM13-12/`  
Category: **HARD OUTSIDE**  
Canonical source / claim ID: `P0214`  
Status after this invocation: **PARTIAL / OPEN / CLAIM RETAINED**

## 1. Result and fixed metric

This invocation continues the already-admitted source target `P0214`, David Aldous's *Shortest routes in random proximity networks*, in the frozen source-valid model selected by the canonical claim:

- unit-intensity planar homogeneous Poisson point process;
- its planar Delaunay triangulation;
- Euclidean edge lengths;
- shortest routes minimize total Euclidean edge length;
- bounded-local endpoint conventions as in the source-matching rigorous literature.

The frozen metric remains

`U_T = best certified polynomial upper exponent in this track for transversal deviation`,

meaning that a value `a` is certified only by a complete proof that for every `epsilon>0`, almost surely all sufficiently long relevant geodesics satisfy `T_r <= r^(a+epsilon)`.

Recovered baseline: `U_T = 3/4`, from Hirsch--Neuhaeuser--Schmidt (2016), Theorem 2.2.

Before this run: `3/4`.  
After this run: `3/4`.  
**No metric movement.**

This run does make a source-relevant route decision. It proves a shielded one-block resampling repair lemma, then proves an exact four-site Delaunay-flip family showing that the repair cost must scale linearly with the stabilization radius in deterministic worst case. Combining that with the shortest-path LP dual shows precisely why the current block-resampling / Efron--Stein / Falik--Samorodnitsky architecture is still polynomially exponent-stuck: local geometry supplies excellent stabilization tails but does not itself supply the required polynomial anti-pivotality or cancellation.

Admitted-target counters after this report:

- unchanged runs after admission: **2**;
- stuck-recovery episodes: **0 / 2**;
- stuck protocol: **not yet triggered** (trigger is three consecutive unchanged runs or repeated unchanged obligation);
- designated eventual auditors remain P26 and NM13-13; neither is presumed to have audited or passed anything here.

## 2. Runtime / scheduler-control truth

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. The runtime exposes no authenticated reasoning-effort telemetry, so reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still provides title/prompt, schedule/timing, enabled state, listing and update operations, but no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated per-run applied-model/applied-effort attestation. `GPT-6 / maximum` therefore remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists those fields into inference routing and returns trustworthy per-run attestation.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary, not permission to bypass controls. The lawful workaround is the owning or otherwise authorized account/workspace/API/admin context, or authorized platform support for that same task. This invocation made **no scheduler or permission change**.

## 3. Continuity and required repository reads

The controlling predecessor is

`proofnet24/NM13-12/runs/2026-09-19/2026-09-19T06-12-30Z__p0214-first-research-curvature-transfer-gate.md`

created at commit

`d7ace4b9761d504334e6eef046973ece729b25c9`.

Its durable state was:

- P0214 admitted and exclusively owned by NM13-12;
- source process frozen to Euclidean Poisson--Delaunay;
- `U_T=3/4` recovered from prior art;
- first-run methods #2/#6/#30 genuinely attempted;
- deterministic curvature-transfer lemma proved;
- the live quantitative gate was a polynomial improvement of passage-length error, not another logarithmic variance refinement;
- unchanged count 1, stuck recoveries 0/2;
- planned next methods #11/#20/#24.

Before substantive work I freshly read or recovered:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling NM13-12 report above;
- newest visible NM13-11 report, which has now admitted P0257 and preserves its own independent metric/history;
- newest visible NM13-13 report, which has now admitted P0083 and moved its whisker threshold metric from 25 to 22;
- `operations/claims/P0214.md` at current `master`;
- the P0214 intake/catalog/rank-sheet material recording `attempted_unsolved` and the earlier deterministic detour calculation;
- exact-ID/title/key searches confirming no ownership mutation or alias collision affecting P0214.

The append-only intake and attempt corpora are too large to claim every unchanged historical byte was freshly rendered model-visible in this invocation. Candidate-specific P0214 source, dedup and attempt records were freshly recovered, and the exact predecessor-to-prewrite Git delta below contained no changed intake `problems.jsonl`, root source-selection ledger, or controlling policy that invalidates carried continuity.

No private-repository history material known to be relevant to P0214 ownership was inaccessible.

## 4. Exact repository delta before the report write

Final pre-report `master` snapshot inspected:

`6a8c0b2fa0e7e0c0bdacd2e2d6460361a3cbaecc`.

Exact comparison:

`d7ace4b9761d504334e6eef046973ece729b25c9 .. 6a8c0b2fa0e7e0c0bdacd2e2d6460361a3cbaecc`

GitHub reported:

- status: `ahead`;
- ahead: **91 commits**;
- behind: **0**;
- total commits: **91**;
- `too_large = null`, so the returned changed-file list is complete for the interval.

No changed file in that interval is root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, an intake `problems.jsonl`, a probability attempt ledger, or a controlling owner/NM13 policy file. `operations/claims/P0214.md` was not changed. The current readback still records NM13-12 as exclusive owner, category HARD OUTSIDE, status CLAIMED/PARTIAL, canonical residue 11.

New claim activity elsewhere in the interval includes `B-WEAK-EVEN-LOGCONCAVE`, an update to `GZ-DIMBM-EVEN-LOGCONCAVE`, and `P0411`; none collides with P0214. A later R7-03 admission of P0458 is also unrelated.

## 5. Source, primary literature and bounded 2026 status check

Dated 2026-09-19 UTC, this run checked the following public source/literature surfaces and queries:

1. David Aldous, maintained `Random Proximity` open-problem page, query `Shortest routes in random proximity networks`. The page still says rigorous study of the order of the transversal deviation `T_r` and variance of route length `D_r` remains open. Aldous's main problem index, crawled on the same date, still lists the problem under open research problems while warning that the maintained collection may lag current literature.
2. Christian Hirsch, David Neuhaeuser and Volker Schmidt, *Moderate deviations for shortest-path lengths on random segment processes*, ESAIM Probab. Stat. 20 (2016), DOI `10.1051/ps/2016012`. I opened the official Numdam PDF. Theorem 2.2 was visually checked on PDF page 5 / indexed page P4: it gives the `|x_1-x_2|^(3/4+epsilon)` tube. Section 4 gives the martingale/block regularization. The indexed text of Section 5.4 / Lemma 5.7 was also checked: Poisson--Delaunay satisfies stability conditions (H1)--(H5), including (H2), which says resampling inside `Q_r` cannot change the Delaunay segment process outside `Q_{3r}` on the good configuration event. A screenshot of this later PDF page returned a cache miss after the parsed text was available; I do not claim visual inspection of that page.
3. Leandro Pimentel, *Asymptotics for First-Passage Times on Delaunay Triangulations*, CPC 20 (2011), pp. 435--453. It supplies martingale/percolation fluctuation upper bounds for a Delaunay FPP model but is not a source-level resolution of Aldous's Euclidean-edge shortest-route question. HNS explicitly notes that in the Euclidean model the edge weights are geometry-dependent, unlike the independent-weight Delaunay setting that motivates part of the older martingale literature.
4. David Coupier and Christian Hirsch, *Coalescence of Euclidean geodesics on the Poisson-Delaunay triangulation*, Bernoulli 24 (2018), 2721--2751. This proves directional coalescence using the known concentration property; it does not give an upper wandering exponent below 3/4.
5. Guanlin Mo, Kangke Cheng and Hu Ding, *The Stretch Factor of Planar Delaunay Triangulations Is Less Than 1.65*, arXiv:2609.07979, posted 2026-09-07. It proves a universal planar Delaunay stretch factor `<1.65`, improving the previous 1.998 upper bound. This is new enough to matter to the local repair constant below, but by itself it has no polynomial fluctuation consequence.
6. Searches `Delaunay geodesic transversal fluctuations Poisson 2026`, `Poisson-Delaunay shortest path variance 2024 2025 2026`, and current citation-neighborhood checks found no checked primary source proving Aldous's exact fluctuation orders or a source-matching Delaunay transversal exponent below 3/4. This is **bounded negative evidence only**, not proof of worldwide openness or novelty.

The 2019 Kartun-Giles--Barthelemy--Dettmann simulations remain only numerical evidence (`xi approximately 0.70`, `chi approximately 0.40` for the Delaunay/excluded-region class).

## 6. Section-B #11 — DUALIZE

### 6.1 Exact shortest-path dual

For a finite connected graph `G=(V,E)` with positive Euclidean edge lengths `l(uv)=|u-v|`, shortest-path distance has the elementary dual form

`D_G(x,y) = max { phi(y)-phi(x) : |phi(u)-phi(v)| <= |u-v| for every uv in E }`.

Proof. Every feasible `phi` telescopes along every `x-y` path, hence `phi(y)-phi(x)` is at most the path length and therefore at most `D_G(x,y)`. Conversely set `phi(v)=D_G(x,v)`. The graph-metric triangle inequality gives `|phi(u)-phi(v)|<=l(uv)` on every edge and `phi(y)-phi(x)=D_G(x,y)`. For the infinite Poisson--Delaunay model this dual may be applied after the usual finite confinement, or directly to the finite portion used by a finite geodesic.

Thus a local Delaunay resampling does not merely alter a path combinatorially: it **removes and adds local Lipschitz constraints in the dual potential problem**. A large change in distance is exactly a large release/tightening of those local constraints.

### 6.2 Influence / entropy gate

Encode the Poisson process by independent spatial boxes and let `D_r` be the frozen passage length. For block `Q`, let `D_r^(Q)` denote the value after an independent replacement of the Poisson configuration in that block and define

`Delta_Q = D_r - D_r^(Q)`.

Efron--Stein gives the standard influence proxy

`Var(D_r) <= (1/2) sum_Q E[Delta_Q^2]`.

A Falik--Samorodnitsky / modified-Poincare refinement can improve a linear influence budget by a logarithmic factor when the squared first influences are much smaller than the squared second influences; this is the mechanism behind the `n/log n`-type Euclidean-FPP variance technology examined in the preceding run.

The dual calculation clarifies the quantitative obstruction. If local repair gives only

`sum_Q E[Delta_Q^2] = O(r)`,

then even a polynomial separation between first- and second-influence sums enters Falik--Samorodnitsky through a **logarithm**. The resulting scale remains `r^(1/2)` up to logarithms and therefore leaves the curvature-transfer exponent at `3/4`.

A genuine exponent move through this architecture would need a polynomial gain, for example an entropy/concentration proxy

`V_r = O(r^(1-delta))`

for some `delta>0`, together with a source-valid centering/rate estimate of matching order and sufficiently strong uniform tails. If one could prove passage error

`|D_r - mu r| <= r^((1-delta)/2 + epsilon)`

with summable uniform failure probabilities, then the curvature lemma from the preceding report would give

`U_T <= (1 + (1-delta)/2)/2 = 3/4 - delta/4`

(up to the arbitrary epsilon convention).

This is a real quantitative gate, but this run does **not** prove such a polynomial influence gain. In particular, a sublinear variance bound alone would not suffice without controlling the bias `E D_r - mu r` and the needed uniform tail probabilities.

**Outcome of #11:** the dual formulation is clean and source-valid, but it turns the previous qualitative warning into a hard numerical barrier: ordinary block influence plus a logarithmic entropy gain cannot move `U_T`.

## 7. Section-B #20 — FIND WHY THE ALGORITHM FAILS

The previous run proposed block resampling as the most plausible way to port Euclidean-FPP concentration technology to Poisson--Delaunay. This run isolated exactly what that algorithm *can* prove locally.

### 7.1 Shielded local-repair lemma

Let `eta` and `eta'` be two locally finite planar point configurations that agree outside `Q_s(o)`. Let `G=Del(eta)` and `G'=Del(eta')`. Assume the local HNS stability-II shield holds in both directions at scale `s`, so the two Delaunay segment processes agree outside `Q_{3s}(o)`. Let `x,y` be persistent vertices outside the resampled region. Then

`|D_G(x,y)-D_G'(x,y)| <= 3 sqrt(2) t_D s`,

where `t_D` is any valid universal Delaunay stretch factor. Using the 2026 theorem, one may take `t_D=1.65`, hence the right side is `<7.001 s`.

Proof. Consider a shortest `x-y` path in `G'`. If it uses no changed edge, it is also a path in `G` and gives the desired one-sided inequality. Otherwise take the first persistent vertex `u` immediately before the first changed-edge portion and the last persistent vertex `v` immediately after the last changed-edge portion. Stability-II confines all changed edge segments to `Q_{3s}(o)`, hence `u,v` lie in that cube and

`|u-v| <= diam(Q_{3s}) = 3 sqrt(2) s`.

The old Delaunay graph `G` contains a route from `u` to `v` of length at most `t_D |u-v|`. Replacing the entire changed portion of the `G'` path by this old route gives

`D_G(x,y) <= D_G'(x,y) + 3 sqrt(2) t_D s`.

Reverse `G,G'` and use the shield in the other direction for the opposite inequality. QED.

This is exactly compatible with HNS (H2): on their good Delaunay configuration event, arbitrary resampling inside `Q_s` cannot affect the segment process outside `Q_{3s}`. Their Section 5 occupancy/count construction and Poisson empty-box estimates also show why the scale needed for such a shield has very light tails; in dimension two the local failure probabilities are exponentially small in area scale. Thus large geometric influence radii are rare.

### 7.2 Why the algorithm still fails to move the exponent

The repair lemma is stronger operationally than the preceding report's vague `Delaunay stabilization/sensitivity term`: the local term is now explicit, linear in the stabilization radius, and has a current deterministic coefficient from the `<1.65` spanner theorem.

But that success exposes the actual failure. Typical stabilization radii are order one, and an `r`-long geodesic encounters order-`r` local opportunities for resampling. Summing squared local influences therefore naturally leads back to a **linear** variance proxy unless one proves a new global anti-pivotality / overlap estimate. The HNS shielding event controls *how far* a perturbation propagates; it does not say that most blocks near a geodesic have a polynomially tiny chance of changing the global optimum.

So the block-resampling algorithm does not fail because Delaunay geometry is too nonlocal. The HNS stability theorem already fixes that. It fails because local stabilization plus bounded repair cost still gives only a first-order sum of local sensitivities.

**Outcome of #20:** the exact transfer term is now identified. Pure local repair / stabilization, even with the 2026 stretch constant, is abandoned as a standalone metric-moving route. It can remain a lemma inside a future argument only if paired with a genuinely new global overlap or anti-pivotal estimate.

## 8. Section-B #24 — FIND THE EXTREMAL OBJECT

The natural remaining question was whether the linear-in-stabilization-radius repair cost above is merely a crude proof artifact. It is not: a four-site Delaunay flip gives an exact scale-linear obstruction.

### 8.1 Exact four-site flip family

Fix `R>=1` and define

`A=(-R,0)`, `C=(R,0)`, `D=(0,-R)`,

and two possible positions for one resampled site

`B_+=(0,R+1/2)`, `B_-=(0,R-1/2)`.

The moved site changes position by Euclidean distance exactly `1`.

For a general `B=(0,b)`, the circle through `A,B,C` has center

`(0,(b^2-R^2)/(2b))`

and radius

`(b^2+R^2)/(2b)`.

The power of `D` with respect to this circle is exactly

`R (b-R)(b+R) / b`.

Therefore:

- for `b=R+1/2`, `D` is strictly outside the `ABC` circumcircle, so the Delaunay diagonal is `AC`;
- for `b=R-1/2`, `D` is strictly inside that circle, so `AC` is not Delaunay and the diagonal is `BD`.

There is no cocircular degeneracy in either configuration.

In the `B_+` triangulation, the Delaunay distance from `A` to `C` is the direct edge

`D_+(A,C)=2R`.

In the `B_-` triangulation, `AC` is absent. The shorter hull route is via `B_-`, because `R-1/2<R`, so

`D_-(A,C)=2 sqrt(R^2+(R-1/2)^2)`.

Hence a unit displacement of one site changes the shortest-path distance by

`Delta_R = 2 sqrt(R^2+(R-1/2)^2) - 2R`.

For every `R>=1`,

`Delta_R >= R/5`.

Indeed, after moving positive terms and squaring, this is equivalent to

`4(R^2+(R-1/2)^2) >= (11R/5)^2`,

whose difference is

`(79/25)R^2 - 4R + 1`.

This polynomial is increasing for `R>=1` and equals `4/25>0` at `R=1`.

Thus **one unit-scale local motion can change a Delaunay shortest-path distance by order `R` when the local Delaunay cavity has scale `R`**.

The inequalities are strict, so the construction survives sufficiently small perturbations of the four sites. In a Poisson configuration one can realize the corresponding geometry inside small neighborhoods while requiring the relevant circumdisk region to be empty; such large cavities are exponentially rare in their area, which is consistent with HNS stabilization tails. This finite construction is route-selection evidence, not an asymptotic exponent theorem.

### 8.2 Dual meaning of the extremizer

The same four-point family is especially transparent in the dual from Section 6. In the `B_+` state, the direct Delaunay edge `AC` imposes the dual constraint

`phi(C)-phi(A) <= 2R`.

After the flip, that constraint disappears and the shortest remaining two-edge route permits the optimal dual gap to rise to

`2 sqrt(R^2+(R-1/2)^2)`.

So the order-`R` sensitivity is not an artifact of path surgery; it is an actual order-`R` release of the local dual constraint system.

**Outcome of #24:** the extremal object kills the hope of replacing the factor `stabilization radius` by a deterministic `O(1)` local repair bound. Any successful polynomial improvement must use the *probability / overlap structure of pivotal cavities*, not just better deterministic Delaunay geometry.

## 9. Route synthesis and explicit abandonment decision

The three methods now fit together:

1. **Dualize (#11):** shortest paths are local Lipschitz-constraint duals; standard block entropy gives at most logarithmic superconcentration from a linear influence budget.
2. **Find the algorithm's failure (#20):** HNS already supplies the needed locality mechanism, and the 2026 spanner theorem makes the repair constant explicit. The missing object is not stabilization but global anti-pivotality / overlap.
3. **Find the extremal object (#24):** a scale-`R` near-cocircular Delaunay cavity makes unit local resampling change the optimal distance by `Omega(R)`, so deterministic local sensitivity really must pay for cavity scale.

Therefore this run **abandons the standalone block-repair route** as a way to move `U_T`. I will not spend a third run optimizing its constants or rebuilding another checker around the same influence inequality. The repair lemma remains available as infrastructure for a genuinely different argument.

The sharpest remaining quantitative obligation is now:

> Prove a polynomial global anti-pivotality / overlap estimate strong enough to turn the locally stabilized replacement derivatives into a polynomially sublinear effective fluctuation scale, *and* control the centering bias at the same polynomial scale.

A convenient sufficient target is: for some `delta>0`, obtain source-valid uniform tails at passage-error scale

`r^((1-delta)/2 + epsilon)`.

That would force

`U_T <= 3/4-delta/4`.

Nothing in this run establishes such a `delta`; the metric therefore honestly remains `3/4`.

## 10. Next run and method rotation

This is the second consecutive admitted run without metric movement, so Section I is not yet mandatory. A third consecutive unchanged run would trigger the full stuck-thinking protocol rather than another lemma run.

If the next invocation occurs before any owner/source change, it should not repeat #11/#20/#24. The planned genuinely different methods are:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** replace hard geodesic minimization by a finite-temperature/soft-min partition function and differentiate in inverse temperature or a local perturbation parameter; the aim is to express susceptibility through a two-replica overlap quantity and then examine the zero-temperature limit.
- **#12 FIND WHAT IS CONSERVED:** exploit exact telescoping of longitudinal Euclidean progress along every path to separate useful forward progress from detour budget; test whether this yields an overlap invariant that local block sensitivity missed.
- **#28 REPLACE FOR ALL WITH FOR TYPICAL:** seek a theorem for a typical block along the geodesic (polynomially small pivotality or controlled replica overlap) rather than a deterministic bound for every cavity, precisely because #24 proves the worst case is scale-linear.

If these methods fail to move `U_T`, that will be the third unchanged run and the following report must be a Section-I stuck recovery, consuming at most the first of two allowed recoveries.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-12
  namespace: proofnet24/NM13-12/
  category: HARD_OUTSIDE
  source_id: P0214
  claim_id: P0214
  admission_state: ADMITTED
  canonical_dedup_key: fluctuations_of_shortest_routes_in_poisson_proximity_networks
  shard_mod_13: 11
  source_status: OPEN
  track_status: PARTIAL
  frozen_process: planar unit-intensity Poisson-Delaunay triangulation with Euclidean edge weights and bounded-local endpoints
  metric:
    name: U_T
    definition: best certified polynomial upper exponent for source-valid transversal deviation
    before: 3/4
    after: 3/4
    moved: false
  methods_attempted:
    - 11
    - 20
    - 24
  method_outcomes:
    B11: exact shortest-path Lipschitz-potential dual; standard linear influence plus logarithmic entropy gain cannot move polynomial exponent
    B20: proved shielded resampling repair |Delta D| <= 3*sqrt(2)*t_D*s; locality is available, global anti-pivotality is missing
    B24: exact four-site near-cocircular Delaunay flip gives unit site motion with Delta D >= R/5; deterministic repair must scale with cavity radius
  new_source_relevant_results:
    - shielded local-repair lemma under HNS stability-II plus universal Delaunay spanner
    - exact parametric four-site Delaunay-flip sensitivity obstruction
    - polynomial influence/centering gate delta>0 would imply U_T <= 3/4-delta/4
  metric_movement_claimed_from_results: false
  unchanged_runs_after_admission: 2
  stuck_recoveries_used: 0
  stuck_recoveries_allowed: 2
  route_abandoned: standalone local block-repair / logarithmic entropy route
  next_methods:
    - 5
    - 12
    - 28
  next_obligation: derive or refute a polynomial typical-block anti-pivotality / two-replica-overlap estimate with matching centering control
  bounded_literature_check_date: 2026-09-19
  literature_scope_note: bounded current-source/primary/citing-paper search; negative search is not worldwide openness or novelty proof
  designated_auditors_if_completed:
    - P26
    - NM13-13
  audits_presumed_passed: false
```

## 12. Save / access discipline

This invocation writes exactly this one immutable report in NM13-12's own `runs/` namespace. No shared root ledger, peer namespace, claim ownership file, workflow, permission, public post, email/Drive resource, paid compute resource, or scheduler is modified. There is no receipt-only follow-up commit; the report is to be read back at its creation commit.