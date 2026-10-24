Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b6 -> gamma_E >= b7>b6`**; methods actually tried: **B6 / B19 / B30**.

# HARD7-04 bounded research iteration — retrospective parent-ticket exploration for fixed-outdegree PA criticality

Status: **PARTIAL / SOURCE OPEN**. This run gives a strict new lower-bound advance for the exact admitted sequential fixed-outdegree preferential-attachment model. It does **not** identify the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or produce a scaling-limit law.

The complete analytic proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_retrospective_parent_ticket_20260920T0530Z.md`

created at commit

`1e6e84ec6119316d6d727c29ecdcd1b639133752`

and read back at that exact SHA before this report was written.

---

## 1. Continuity, ownership, and evidence consumed

I resumed the exclusive canonical claim

`operations/claims/P0151.md`

owned by `HARD7-04`. I did not restart I0049, P0157, the configuration-model/MST line, any solved degree-count target, or the conditionally-independent-edge growing-graph theorem.

Before the new mathematics I reread/reconciled the required repository surfaces:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the P0151 canonical claim and intake/catalog traces;
- the I0049 source/status history, which records the uniformly-grown critical-window scope as later-literature-known rather than available for duplicate work;
- the neighboring preferential-attachment track, especially `runs/R08/20260917T2326Z_i0048_threshold_comparison_73b9e1.md`;
- the complete current HARD7-04 P0151 chain through the immediately preceding report `runs/hard7_2026-09-18/HARD7-04/2026-09-20T0432Z__p0151_capped_quadratic_bridge.md`.

A repository-wide ownership search still showed `P0151` exclusively owned by HARD7-04, and a fresh directory read immediately before this report showed the `04:32Z` capped-quadratic report as the latest own-track substantive predecessor. No peer claim was overwritten.

The posting registry contains no source-equivalent P0151 paper.

---

## 2. Frozen model and current-literature refresh — 20 September 2026

The model remains Ray/Hazra--van der Hofstad--Ray model (d): fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges from each arriving vertex, target probabilities proportional to current degree plus `delta` with within-birth updates, no self-loops for the new vertex, followed by independent bond retention with probability `pi`.

The exact positive threshold is

`pi_c = delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

Fresh bounded source/current-literature searches on **20 September 2026** rechecked the following.

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026), `https://arxiv.org/abs/2312.14085`, identifies the exact fixed-outdegree threshold and giant/no-giant dichotomy through the Pólya-point-tree mean operator. Its current source record does not state a finite-size critical-window theorem for this exact sequential fixed-`m` model.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025, `https://arxiv.org/abs/2512.18937`, proves a `(log n)^(-2)` window and `sqrt(n)/log n` critical largest-component scale for growing graphs in which the new vertex connects **independently** to earlier vertices. That independence assumption does not automatically include the exact fixed-outdegree sequential model here.
3. Mörters--Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026, `https://arxiv.org/abs/2606.27844`, studies an inhomogeneous PA-kernel graph with `tau in (2,3)` and a moving threshold `p_n`; it is a different ensemble and regime.
4. Ray's thesis, arXiv:2411.14111 / TU Eindhoven thesis (2024), remains the source-side critical-regime program associated with the fixed-outdegree model.

No source-matching fixed-outdegree critical-window resolution surfaced in this bounded refresh. This is bounded negative evidence, not a claim of worldwide novelty.

---

## 3. Frozen source metric: before and after

Put

`a:=m+delta`, `A:=2m+delta`, `pi:=pi_c`.

The frozen admitted metric is

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The preceding run proved

`gamma_E>=b6`,

where

`b2:=m(1+a pi)/A`,

`b6:=b2+m(m-1)pi^2`.

Its capped-shadow second-moment proof also supplied

`b_U:=b2+2m(m-1)pi^2(A+m)/A<1/2`.

Define

`d_*:=1/2-b_U>0`,

`vartheta:=min(1, d_* A/[4(a+m)pi^3])`,

`eta_R:=vartheta a^2 pi^3/A^2`,

and

`b7:=b6+eta_R`.

This run proves

`gamma_E>=b7>b6`,

and also `b7<1/2`.

Thus the source-relevant metric moves strictly:

**Before:** `gamma_E>=b6`.

**After:** `gamma_E>=b7=b6+vartheta a^2 pi_c^3/A^2>b6`.

The Section-I unchanged-run counter therefore resets.

---

## 4. Idea written before validation: use a historical edge only after its child is captured

The previous run explicitly warned against spending another hour merely optimizing the same local bridge coefficient. The new idea changes the exploration in **time**, not merely in the cap profile.

For every ordinary old vertex `u`, distinguish one actual outgoing edge from the birth of `u`, with older endpoint `p(u)`. If `u` and `p(u)` are both still outside the connected shadow, the percolation bit on that old edge can be left unexposed. Later, when a **current** birth simultaneously (i) has a retained gate into the shadow and (ii) captures `u` through a capped bridge, the algorithm reveals that one old percolation bit. If it is retained, a ticket of probability proportional to `1/w_{p(u)}` may capture the historical parent as well.

The key cancellation is

`[parent ticket probability] * [parent attractiveness]
 = vartheta a/w_p * w_p
 = vartheta a`,

so a large parent degree does not create the cubic-moment problem that killed the earlier unthinned route.

The historical retention bit is queried at most once: it is revealed only after a current event that has already captured `u`. That deferred-decision point is essential; without it the apparent extra factor `pi` would be invalid under adaptive conditioning.

No code was written to invent this mechanism. The proof was written analytically first.

---

## 5. B6 — deform toward the independently attached model: direct birthwise coupling fails

I first tried to turn the exact killed-PPT spectral calculation from the 03:30 run into a finite-graph theorem by deforming the fixed-outdegree birth law toward the Jorritsma--Maillard--Mörters independently attached birth law.

The naive version fails for a structural reason: in the present model the number of outgoing edges of every new vertex is **exactly `m`**, whereas an independently attached sparse birth has a random edge count. Thus a birthwise coupling of the complete outgoing-neighbor sets cannot have error `o(1)` merely from matching first moments; the two laws live on different edge-count supports except on the event that the independent model happens to produce exactly `m` edges.

For the source critical-window problem this is not a counterexample, but it kills the most tempting finite-to-local transfer shortcut. One has to compare explorations after conditioning/projecting onto the relevant discovered edges, or compute the dependence correction explicitly.

**Outcome of B6:** failed as a direct total-variation deformation route. It sharpened the transfer obligation: fixed-outdegree dependence cannot simply be declared lower order at a whole-birth level.

---

## 6. B30 — localize on logarithmic age scale: the first dependence correction sits at the window scale

The exact killed local operator from the 03:30 run has spectral loss

`1-r(pi_c T_L)=C_spec/L^2+O(L^-3)`.

Taking `L~log n` points to a `(log n)^(-2)` scale. I therefore tried to localize the finite exploration by log-age blocks and throw away births from which more than one relevant edge is exposed.

A simple stress calculation shows why this cannot be done for free. At the neighboring critical component scale `S~sqrt(n)/log n`, a uniform-proxy birthday count of repeated birth labels is

`S^2/n ~ 1/(log n)^2`.

That is exactly the same order as the killed-operator spectral deficit. The true PA age law is not uniform, so this computation is **not** a theorem for the model; its role is to falsify the proposed simplification. Any proof at the target precision must either compute the repeated-birth correction or prove a model-specific cancellation. An `o(1)` local-weak coupling is far too weak.

**Outcome of B30:** the discard-repeated-birth route was rejected. The dependence term plausibly enters at the leading critical-window order rather than below it.

---

## 7. B19 — make the exploration algorithm explicit: retrospective parent ticket succeeds

The full proof is in the matching artifact. The theorem uses the existing capped connected shadow but adds one two-time operation.

### 7.1 Fresh historical certificates

For each ordinary vertex `u>=3`, designate edge label `1` from its own birth and call its endpoint `p(u)`. If at current time `t`

`u notin Q_t` and `p(u) notin Q_t`,

then the retention bit of `(u,p(u))` has never needed to be revealed. At the birth of `u`, `p(u)` was outside the then-current shadow. If another edge of that birth had been a gate, `u` itself would have entered the shadow, contradicting `u notin Q_t`. At later times the base process never revisits old outgoing edges. Therefore deferred decisions leave this historical bit as an independent Bernoulli(`pi`) variable.

### 7.2 There are linearly many usable roots unless the shadow is already large

Let

`G_t={u>=3: u<=t, u notin Q_t, p(u)>=3, p(u) notin Q_t}`.

Because every ordinary vertex has attractiveness at least `a`, because the number of distinguished edges ending in `Q_t` is at most the total degree of `Q_t`, and because distinguished edges ending in the two seeds are bounded by their degree, one has deterministically

`|G_t| >= t-W_t/a-W_t-Z_t-C`.

Since the cap satisfies `c(w)=min(w,2A)>=a`,

`sum_{u in G_t} c(w_u(t))
 >= a t-(1+a)W_t-aZ_t-C`.                                       (7.1)

### 7.3 Fixed current edge pair plus historical ticket

Use current edge `1` as a retained gate into frozen `Q_t` and current edge `2` as a retained capped bridge to `u in G_t`. Sequential conditioning gives

`P(gate 1 and accepted bridge 2 to u | F_t)
 >= pi^2 W_t c(w_u(t))/(At+K)^2`.                                (7.2)

After this event, reveal the fresh historical bit on `(u,p(u))`. If retained, accept a parent ticket with probability

`vartheta a/w_{p(u)}(t)`.

Multiplying the ticket by the parent reward cancels `w_{p(u)}` and yields conditional expected historical reward `pi vartheta a`. Summing (7.2) with (7.1), and subtracting the `O(1/t)` chance that a later current edge simultaneously captures the same parent, gives the new lower drift

`E[B_t|F_t]
 >= eta_R W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_t/t^2
    -C/t`,                                                        (7.3)

with

`eta_R=vartheta a^2 pi^3/A^2>0`.

Adding the preceding `b6` drift gives coefficient `b7=b6+eta_R`.

### 7.4 The new jump still has a linear square budget

The upper parent drift is

`E[B_t|F_t]
 <= [kappa_U/t+O(t^-2)]W_t+C/t`,

where

`kappa_U=2 vartheta(a+m)pi^3/A <= d_*/2`.

Thus the new upper coefficient is

`b_U':=b_U+kappa_U<1/2`.

For the square jump, if `p(u)` is the distinguished parent of `u`, then

`sum_{u<=t} w_{p(u)}(t)
 <= sum_v d_v(t)w_v(t)
 <= V_t`.

The capped current bridge and the inverse-parent-weight ticket therefore give

`E[B_t^2|F_t] <= C(1+V_t/t)`.

Together with the old global budget `E V_t=O(t)`, the square recurrence closes again:

`E W_t^2=O(t)`.

The same mean bootstrap as before then yields

`E W_n>=c n^b7`.

Finally, a single retained first-edge gate occurs with probability at least `pi W_t/(At+K)`, so summing new-vertex activations gives `E|Q_n|>=c'n^b7`. The shadow is connected in the actual percolated graph, hence

`gamma_E>=b7`.

Because the lower bonus is strictly smaller than the deliberately budgeted upper bonus, `b7<b_U'<1/2`.

**Outcome of B19:** succeeded. This is a theorem-level strict improvement of the frozen metric under exactly the admitted assumptions.

---

## 8. Negation/stress checks actually performed

The run tested the mechanism against the two main ways it could have been false.

1. **Adaptive-retention failure.** The extra historical `pi` factor would be invalid if the old edge had already been revealed. The deferred-decision lemma rules this out precisely on the good-root event and also shows that the bit is queried at most once.
2. **High-degree-parent failure.** Capturing an unrestricted historical parent would normally make the square jump depend on higher moments. The ticket `vartheta a/w_p` cancels one parent-weight factor, and the remaining sum is bounded by `sum_v d_v w_v<=V_t`, for which the old all-`delta>0` budget is linear.
3. **Second-moment-margin failure.** Instead of guessing that the added drift is small enough, `vartheta` is defined from the already proved positive margin `d_*=1/2-b_U`, forcing the new upper coefficient to stay strictly below `1/2` for every `m>=2`, `delta>0`.

No finite simulation or sampled parameter grid is used as evidence for the theorem. No new exact-arithmetic checker was warranted because the new claim is analytic rather than a finite enumeration; the full proof is on the page in the artifact.

---

## 9. Source-level delta versus auxiliary delta

### Source-relevant metric

`gamma_E>=b6  ->  gamma_E>=b7>b6`.

This is genuine movement, but still only a lower exponent for expected largest-component size. Status remains **PARTIAL / OPEN**.

### Auxiliary progress

The run also isolates two sharper facts about the unpaid finite-to-local transfer:

- direct whole-birth coupling to the independent-edge theorem is structurally wrong because exact outdegree is fixed here;
- repeated-birth dependence can occur at the same `1/(log n)^2` order as the local killed-operator spectral deficit at the neighboring `sqrt(n)/log n` scale, so it cannot simply be dropped.

The previous exact local spectral theorem remains unchanged:

`1-r(pi_c T_L)=C_spec/L^2+O(L^-3)`.

This run does **not** transfer it to the finite graph.

---

## 10. Remaining full-scope gap

The source asks for the critical regime, not merely a growing chain of lower exponents. The missing source-level theorem is still a finite sequential exploration analysis precise enough to determine the window and component scale/law. In particular, nothing here proves:

- `gamma_E=1/2`;
- a matching upper bound;
- a `(log n)^(-2)` window for fixed outdegree;
- `sqrt(n)/log n` critical components;
- tightness, surplus scaling, or a limiting component sequence.

The most promising next route is to compute rather than discard the repeated-birth dependence correction in log-age coordinates, and compare its sign/constant to `C_spec`. A subsequent run must use a different B-triple from `B6/B19/B30`.

---

## 11. Runtime/model and scheduler-control honesty

The runtime identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed here, so reasoning is reported as **UNVERIFIED**. GPT-6 maximum was requested only in prompt text; I do not claim it ran.

The exposed scheduler/control interface still has task text/title, schedule/timing, enabled-state style controls, but **no model-family selector, no reasoning-effort selector, and no guaranteed execution-duration field**. Changing that would require the platform to expose supported model/effort controls for scheduled tasks (or an authorized scheduler context that actually has them); repository text cannot enforce a runtime model.

The historical `You cannot modify this task` response for P26/P01/P03 is an authorization-context boundary. The compliant workaround is the task's authorized owning/admin context or platform support/ownership transfer. Duplicating a schedule, bypassing permissions, or editing repository metadata is not a valid workaround. The repository records that P26 was later updated from an authorized context.

No scheduler write, enable/disable action, email, Drive action, public posting, workflow change, permission change, or force push was performed.

---

## 12. Validation and persistence

- Verified the active P0151 exclusive claim and no source-equivalent posting.
- Re-read the control/directive surfaces, campaign index/ranking, root posting/results/queue ledgers, intake/source traces, newest own report, and neighboring PA report.
- Refreshed primary/current literature on 20 September 2026 for the exact fixed-outdegree model and the 2025--2026 neighboring critical-window papers.
- Wrote the new exploration idea before any artifact/checker work.
- Tried three materially different moves: **B6 / B19 / B30**, different from the preceding **B2 / B3 / B24**.
- Wrote the complete theorem proof in `artifacts/hard7_2026-09-18/HARD7-04/p0151_retrospective_parent_ticket_20260920T0530Z.md`.
- Created that artifact at commit `1e6e84ec6119316d6d727c29ecdcd1b639133752` and read it back at that exact SHA.
- This report is immutable own-track output; no shared root ledger or peer file was edited.

Closure requirements are not met: no full source proof and no two independent audits. Status remains **PARTIAL / SOURCE OPEN**.

---

## 13. Own-track ledger delta suggestion

```yaml
ledger_delta:
  track: HARD7-04
  target: P0151 fixed-outdegree PA critical window
  metric: gamma_E lower bound
  before: b6 = b2 + m(m-1) pi_c^2
  after: b7 = b6 + vartheta (m+delta)^2 pi_c^3/(2m+delta)^2
  vartheta: min(1, (1/2-b_U)(2m+delta)/(4(2m+delta? no: a+m)(pi_c)^3)))
  exact_definition_note: "a=m+delta, A=2m+delta, b_U=b2+2m(m-1)pi_c^2(A+m)/A, vartheta=min(1,(1/2-b_U)A/[4(a+m)pi_c^3])"
  status: PARTIAL_SOURCE_OPEN
  methods: [6,19,30]
  artifact_commit: 1e6e84ec6119316d6d727c29ecdcd1b639133752
```

The explanatory `exact_definition_note` is controlling; the compact human-readable row above is not used to mutate the shared ledger.