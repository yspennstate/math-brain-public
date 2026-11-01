Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `S_exact = UNBOUNDED -> UNBOUNDED`. Section-B methods actually tried, transparently reused because the immutable P0457 history has already exhausted all thirty methods: #3 PROVE SOMETHING STRONGER, #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #20 FIND WHY THE ALGORITHM FAILS.**

# NM13-04 / P0457 — surplus-window diameter theorem; first independent audit now PASS

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-04/`  
Category: `CLOSABLE OUTSIDE`  
Canonical source/claim: `P0457`, `operations/claims/P0457.md`  
Status after this invocation: **PROVED-CANDIDATE / 1-of-2 INDEPENDENT AUDITS PASSED / NOT CLOSED**  
Frozen metric: **`S_exact = UNBOUNDED`**  
Unchanged-run counter: **2 -> 3** since the last metric movement  
Stuck recoveries used: **1 -> 1**  
Required independent audits: **P26 = PASS; NM13-05 = NOT PASSED**

## 1. Runtime and control-plane disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The task-control surface exposed to this worker still offers prompt/title, schedule/start controls, timing mode, enabled state, and task identifiers, but no bindable model-family selector and no bindable reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt text only. Making it enforceable would require an owner-authorized product/workspace/API/admin surface exposing persistent model/reasoning fields together with authenticated per-run runtime attestation.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary, not an ownership release. The repository ledger records later successful P26 updating from another authorized context. The lawful workaround is an owning/authorized context or platform/admin support, never task duplication or access-control bypass. No scheduler was modified in this invocation.

## 2. Authoritative continuity and repository read

I continued the already admitted P0457 target. Intake was not reopened and no second claim was created.

Canonical identity remains:

- campaign ID: `P0457`;
- source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`;
- canonical dedup key: `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA-256: `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- residue: `3 mod 13`, matching NM13-04's exclusive shard;
- frozen model: exact bilateral-preference `LK(n,k)`, not an independent-edge surrogate;
- source question: characterize the diameter in the additional near-logarithmic `k(n)` range where Dabirian–Subramanian Theorem 6 proves connectivity.

Before new mathematics I reread/recovered the controlling/current repository state required by the owner: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; canonical claim `operations/claims/P0457.md`; current P0457 source/intake/ranking/attempt history; newest own report `proofnet24/NM13-04/runs/2026-09-18/2026-09-18T08-18-00Z__p0457-closure-critical-audit.md`; newest visible neighboring NM13-05 state; and current P26 audit state.

The claim file records the pre-NM13 campaign state accurately: the old attempt had only a maximum-degree/Moore-type logarithmic lower bound and left the matching upper bound and limiting behavior open. `POSTED.md` does not list P0457 as settled or excluded. The archived campaign `INDEX.md` still groups bilateral degrees among partial/reduced work rather than a closed diameter theorem. No owner-authorized release, competing owner, handoff, or source-specific retirement was recovered.

Large aggregate ledgers and directory listings can be connector-truncated. Exact paths, canonical IDs, claim files, immutable reports and targeted searches are the continuity anchors; truncation is not treated as evidence of absence.

## 3. A material closure-state change: P26 independently passed P0457

This invocation recovered a new independent audit committed after the previous NM13-04 report:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_11-56-41__run-report.md`

at commit

`b24af197056636b9e31b135d21f4059e55cd45d6`.

Its explicit verdict is

`P26-AUDIT-NM13-04-P0457-LOGBAND-DIAMETER-42 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_NEAR_LOG_SCOPE_PASS / STRONGER_POSITIVE_SURPLUS_REDERIVATION_PASS / ANALYTIC_NO_ESSENTIAL_FINITE_CORE / PRIOR_ART_UNVERIFIED / PENDING_SECOND_DISTINCT_AUDIT`.

P26 also records

`P26-RECONCILE-NM13-04-P0457-2OF2-42 = PENDING_NM13-05_DISTINCT_AUDIT`.

This is the first required independent audit PASS. It is not two audits. The newest visible NM13-05 report remains its own C0146 work (`2026-09-18T08-22-00Z__c0146-m5-monotone-coupling.md`), and current exact repository searches recover **no NM13-05 P0457 audit PASS**. Therefore the closure gate is now **1/2**, not 2/2.

The P26 audit also independently rederived the source theorem and stress-tested it under the stronger fixed-surplus form

`k >= log n + eta sqrt(log n) log log n`

for every fixed `eta>0`. I did not simply count that external proof as this run's research. I used its architecture as a new launch point and pushed the surplus scale further below `sqrt(log n) log log n`.

## 4. Fresh source and literature check — bounded, 2026-09-18

The current Cambridge primary source still states that, after the improved connectivity result, an open problem is to characterize the diameter for the additional `k(n)` range from Theorem 6 where connectivity holds. The source model is the bilateral-preference graph: iid continuous edge weights on `K_n`, with `{i,j}` retained exactly when it lies among the `k` preferred incident edges at both endpoints.

The nearest same-model predecessor remains Richard J. La and Maya Kabkab, *A New Random Graph Model with Self-Optimizing Nodes: Connectivity and Diameter*, Internet Mathematics 11(6) (2015), 528–554, DOI `10.1080/15427951.2015.1022626`. Its published abstract records the older embedded-connected-ER route for `k > beta_* log n`, `beta_* ~= 2.4626`, and the corresponding diameter law.

I ran fresh bounded searches on 2026-09-18 for the exact Dabirian–Subramanian title and DOI, `LK(n,k) diameter`, `bilateral preference random graphs diameter`, the author pair plus diameter, and the La–Kabkab predecessor. They recovered the primary 2026 source, the 2015 predecessor, and classical sparse-ER diameter literature, but no later primary source explicitly resolving the same near-threshold diameter problem or the stronger surplus theorem below. This is **bounded negative evidence only**, not a proof of worldwide openness and not a publication-novelty certificate.

The classical random-graph input used below is Fan Chung and Linyuan Lu, *The Diameter of Sparse Random Graphs*, Advances in Applied Mathematics 26 (2001), 257–279. They explicitly use, for disconnected `G(n,p)`, the convention that diameter is the maximum diameter of its connected components, and prove

`diam G(n,p) = (1+o_P(1)) log n / log(np)`

when `np -> infinity`.

## 5. Frozen metric: deliberately unchanged

The canonical metric remains

`S_exact = largest co-degree s >= 0 for which NM13-04 has a complete deterministic diameter classification for LK(n,n-1-s), uniformly over the stated feasible n.`

The earlier all-`s` componentwise classification saturated this metric at `UNBOUNDED`. The new near-threshold analytic theorem below is genuine mathematical progress but does not enlarge an already unbounded co-degree cutoff. I do not rename the metric to manufacture movement.

- before: `S_exact = UNBOUNDED`;
- after: `S_exact = UNBOUNDED`;
- movement: **none**;
- consecutive unchanged invocations since saturation: **2 -> 3**;
- stuck-recovery episodes: **1 -> 1**.

Because this is now the third consecutive unchanged metric run, the **next** invocation is subject to Section I's thinking-only stuck protocol unless an owner-authorized state change supersedes it. The six-unchanged CLOSABLE rotation gate has not yet been reached.

## 6. Method #3 — PROVE SOMETHING STRONGER

The P26 audit showed that the block-core/leave-one-out argument does not really use the source constant `t0>1/2`; it works for every fixed positive multiple of `sqrt(log n) log log n`. I asked whether the same mechanism can be parameterized all the way down to its actual entropy barrier.

It can.

### Theorem (surplus-window diameter and connectivity)

Fix `T>1`. Let `k=k(n)` be integer-valued and put

`s_n := k - log n`.

Assume eventually

`0 < s_n`, `k <= T log n`,

and

`s_n^2 / (k log k) -> infinity`.                                  (6.1)

Then for the exact bilateral-preference graph `LK(n,k)`,

`D(LK(n,k)) / (log n / log log n) -> 1` in probability.             (6.2)

In particular `LK(n,k)` is connected with probability tending to one.

Since `k ~ log n` throughout the near-threshold regime, condition (6.1) is equivalently satisfied whenever

`s_n >> sqrt(log n log log n)`.

This strictly contains the source-connected band

`s_n >= t0 sqrt(log n) log log n`, fixed `t0>1/2`,

and also strictly contains P26's fixed-`eta>0` stress-test band. This stronger theorem is **not** claimed to have an outside audit; P26's PASS applies to the frozen source theorem, not automatically to this new sharpening.

### Proof

Use the monotone transform from the source's iid continuous preference weights to iid `Exp(1)` scores `V_e`, with larger score preferred. For each vertex `v`, let `U_v` be its `k`th largest incident score.

Define

`L_+ = log((n-1)/k) + 2`,
`L_- = log((n-1)/k) - 3/2`,

and let `G_+`, respectively `G_-`, contain exactly the edges whose scores exceed `L_+`, respectively `L_-`. Then

`p_+ = e^{-2} k/(n-1)`, `p_- = e^{3/2} k/(n-1)`.                   (6.3)

For a fixed vertex, the number of incident scores above `L_+` has mean `e^{-2}k`. Chernoff gives

`P(U_v > L_+) <= exp[-(1+e^{-2})k]`.

Likewise the number above `L_-` has mean `e^{3/2}k`, and

`P(U_v < L_-) <= exp[-(e^{3/2}-1-3/2)k]`.

Because `k >= log n + s_n` with `s_n -> infinity` under (6.1), union bounds over all vertices give, with probability `1-o(1)`,

`G_+ subset LK(n,k) subset G_-`.                                  (6.4)

Also `(n-1)p_± = Theta(k) -> infinity` and

`log((n-1)p_±) = log log n + O(1)`.

Hence Chung–Lu yields

`diam(G_±) = (1+o_P(1)) log n / log log n`,                        (6.5)

with the maximum-component convention for possibly disconnected `G_+`.

The only nontrivial issue is to attach every vertex of `LK` to a common large component of an appropriate deleted `G_+` core.

Set

`delta = min{s_n/(8k), 1/100}`                                    (6.6)

and `m=ceil(1/delta)`. Partition `[n]` deterministically into `m` balanced blocks `B_1,...,B_m`. For each unordered block pair `{i,j}` delete `B_i union B_j` (only one block when `i=j`), let the remaining set be `W_ij`, let `H_ij=G_+[W_ij]`, and let `C_ij=C_ji` be a largest component of `H_ij`.

#### Uniform core lemma

With probability `1-o(1)`, simultaneously for every block pair,

`|C_ij| >= |W_ij| - n/k^3`.                                       (6.7)

To prove this, fix one pair and write `N=|W_ij|`, `p=p_+`, `lambda=Np`. Since `delta<=1/100`, eventually `N>=0.97n`, so `lambda>=c log n` for a fixed `c>0`.

For a fixed vertex `x`, if its component has size `r<=N/2`, choose its other `r-1` vertices, choose a spanning tree, and require no edge from the component to its complement. Thus

`P(|C(x)|=r)`
` <= C(N-1,r-1) r^(r-2) p^(r-1) (1-p)^(r(N-r)).`                  (6.8)

For `r=1` this is at most `exp[-(1-o(1))lambda]`. For `r>=2`, use

`C(N-1,r-1) <= (eN/(r-1))^(r-1)`,
`N-r >= N/2`,

and `(r/(r-1))^(r-1)<=e`. Then (6.8) is at most

`(e^2 lambda)^(r-1) exp[-lambda r/2]`.

For large `lambda`, `log(e^2 lambda)<=lambda/6`, so the sum over `2<=r<=N/2` is at most a geometric tail `O(exp[-2lambda/3])`. Consequently

`P(x lies outside the unique >N/2 component, if one exists) <= 2 exp[-lambda/3]`.

The expected number of vertices in components of size at most `N/2` is therefore

`O(N exp[-lambda/3]) = o(n/k^A)`

for every fixed `A`, because `lambda>=c log n`. Taking `A=6` and Markov gives

`P(N-|C_ij| > n/k^3)=o(k^-3)`.                                   (6.9)

The number of block pairs is harmless. In the uncapped case of (6.6),

`m^2 = O(k^2/s_n^2) = o(k/log k)`

by (6.1); in the capped case `m<=100`. Union bounding (6.9) proves (6.7).

#### Few target-overflow vertices

Now define

`q = log((n-1)/k) + delta`,
`p_0 = e^{-delta} k/(n-1)`.                                       (6.10)

Let `B` be the set of vertices having at least `k` incident scores greater than `q`. For fixed `w`, this count is binomial with mean `e^{-delta}k`; Chernoff gives

`P(w in B) <= exp[-k I(delta)]`,
`I(x)=x-1+e^{-x} >= x^2/3` for `0<=x<=1/100`.                     (6.11)

Hence

`P(|B| > delta n/2) <= (2/delta) exp[-delta^2 k/3] = o(1).`        (6.12)

Indeed, if `delta=s_n/(8k)`, the exponential rate is

`delta^2 k/3 = s_n^2/(192k)`,

which dominates `log(1/delta)=O(log k)` by (6.1). If `delta=1/100`, the rate is a fixed positive multiple of `k`.

#### Leave-one-out bilateral attachment

Fix `v in B_i`. For each target `w!=v`, let `B_v` contain `w` when, after deleting the single edge `vw`, the `k`th largest remaining score at `w` still exceeds `q`. Then deterministically

`B_v subset B`,                                                     (6.13)

and, crucially, `B_v` is measurable with respect to edges not incident to `v`.

Fix a block index `j`, condition on every non-`v` edge, and put

`A=C_ij \ B_v`.

On the simultaneous good events (6.7) and (6.12), using `1/k^3=o(delta)`,

`|A|/(n-1) >= 1-3delta`                                           (6.14)

for all sufficiently large `n`, uniformly in `v,i,j`.

The incident scores `(V_vw)_{w!=v}` remain iid exponentials under this conditioning. Let

`R_v={w:V_vw>q}`

and let `S_v` be the labels of the `k` largest incident scores at `v`.

If `|R_v|<=k`, every `q`-high edge is proposed by `v`. If `|R_v|>k`, all edges in `S_v` are `q`-high and the label set `S_v` is a uniform `k`-subset of the `n-1` possible neighbors. For any `w in A` with `V_vw>q`, relation (6.13) means that at most `k-1` other edges at `w` exceed `q`, so `w` also proposes `vw`. Therefore

`P(v has no LK-neighbor in A | non-v edges)`
` <= (1-p_0)^|A| + C(n-1-|A|,k)/C(n-1,k)`
` <= exp[-p_0|A|] + (1-|A|/(n-1))^k.                              (6.15)

Since `delta<=1/100`, (6.14), `e^{-delta}>=1-delta`, and (6.6) give

`p_0|A| >= k(1-delta)(1-3delta)`
`          >= k(1-4delta)`
`          >= log n + s_n/2`.                                     (6.16)

The last inequality is exact in the uncapped case because `4delta k=s_n/2`; in the capped case `s_n>=0.08k`, so `4delta k=0.04k<=s_n/2`.

Also (6.14) gives

`1-|A|/(n-1) <= 3delta <= 0.03`.                                  (6.17)

Thus each endpoint/core requirement fails with probability at most

`n^{-1} exp[-s_n/2] + 0.03^k`.                                    (6.18)

There are at most `nm` requirements. Under (6.1), `s_n >> sqrt(k log k)`, hence `s_n >> log k` and

`m exp[-s_n/2] -> 0`.

Moreover `k>=log n`, so

`nm 0.03^k ->0`.                                                   (6.19)

Therefore, with probability `1-o(1)`, every vertex in every block attaches by an `LK` edge to every corresponding pair-core it needs.

Take arbitrary `u in B_i` and `v in B_j`. Both attach to the same connected `C_ij subset G_+`; hence

`d_LK(u,v) <= diam(G_+) + 2`.                                     (6.20)

This simultaneously proves `LK(n,k)` connected. Since `LK subset G_-`, the supergraph `G_-` is also connected on this event, and therefore

`diam(G_-) <= diam(LK) <= diam(G_+) + 2`.                          (6.21)

Combining (6.5) and (6.21) proves (6.2). QED.

### Consequence for the source scale

For the Dabirian–Subramanian source band

`s_n = t0 sqrt(log n) log log n`

with any fixed `t0>1/2`,

`s_n^2/(k log k) ~ t0^2 log log n -> infinity`.

So the source theorem is a strict corollary. More generally the same diameter law now has a complete on-page proof whenever

`k-log n >> sqrt(log n log log n)`

while `k=O(log n)`.

**Outcome #3:** a genuinely stronger source-valid theorem was obtained, with a full proof on this report page. It does not change the frozen `S_exact` metric and it is not yet externally audited as a strengthening.

## 7. Method #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

The new theorem came from exposing the proof's hidden scale parameter instead of freezing it at the source's `sqrt(log n) log log n` surplus.

Write `s=k-log n` and choose a block-deletion/target-capacity parameter `delta`. Three competing error terms govern the method:

1. **attachment reserve:** deleting blocks and raising the safe-target threshold costs `Theta(delta k)` in the exponent, so one needs `delta k << s`;
2. **overflow rarity:** target overflow has probability `exp[-Theta(delta^2 k)]`, and to make the bad-target fraction `o(delta)` one needs `delta^2 k` to beat the logarithmic entropy of the block scale;
3. **top-k miss:** the chance a random top-`k` label set misses a `(1-O(delta))` fraction is `O(delta^k)`, so a fixed small cap on `delta` makes this negligible even away from the narrowest window.

Balancing the first two by taking `delta` proportional to `s/k` makes the second exponent proportional to `s^2/k`. The only remaining entropy is `log(1/delta)=O(log k)`. This is exactly why the sufficient condition becomes

`s^2/(k log k) -> infinity`,                                      (7.1)

rather than the source's stronger `s ~ sqrt(k) log k` scale.

The cap `delta<=1/100` is not cosmetic. Without it, when `s` is a positive fraction of `k`, the hypergeometric/top-k miss term `(3delta)^k` can be too weak after the union over `n` endpoints. Capping `delta` keeps `3delta<=0.03` while the surplus itself is then large enough to absorb the fixed `4delta k` attachment cost.

**Outcome #5:** parameter optimization identifies `sqrt(k log k)` as the natural barrier of this particular one-round leave-one-out proof, improving the proven window by a factor `sqrt(log log n)` over the source-scale hypothesis.

## 8. Method #20 — FIND WHY THE ALGORITHM FAILS

The proof above also identifies its precise remaining obstruction. If

`s = O(sqrt(k log k))`,

then choosing `delta=Theta(s/k)` no longer guarantees that

`(2/delta) exp[-Theta(delta^2 k)] ->0`.                            (8.1)

In words: the expected target-overflow population is no longer small enough, at the needed resolution, to reserve almost all of every deleted core for every endpoint simultaneously. Choosing a larger `delta` would suppress overflow, but then the threshold/deletion cost `Theta(delta k)` consumes the entire surplus `s` and destroys the `n^{-1}`-plus margin needed for the union over all endpoints.

This is a proof-method barrier, not evidence of disconnection and not a counterexample. Crossing it would require a genuinely different ingredient, for example:

- averaging the overflow population rather than controlling it uniformly;
- a multi-round attachment that tolerates a positive-density first-round exceptional set;
- or a sharper conditional target-capacity law exploiting correlations inside the giant component rather than Markov-controlling all overflow vertices.

**Outcome #20:** the next unresolved scale is now explicit. The route is no longer vaguely “near threshold”; its one-round bottleneck is the competition `delta k` versus `delta^2 k` with block entropy `log(1/delta)`.

## 9. Method-accounting exception

The owner directive normally asks for three Section-B methods not previously tried on the problem. The immutable P0457 history already records that **all thirty methods have been used**. It is impossible to satisfy the “previously untried” clause literally without fabricating history.

I therefore reused #3/#5/#20 and disclosed that reuse in the first line. They were used for genuinely new work: a new asymptotic surplus theorem, its parameter optimization, and an explicit barrier analysis. This triple differs from the immediately preceding NM13-04 triple #20/#22/#27.

## 10. Closure state and next legal action

P0457 is not repository-closed.

For the frozen source theorem:

- full source-target argument on page: **YES, candidate present**;
- P26 independent audit: **PASS**, audit ID above;
- NM13-05 independent audit: **NOT PASSED / no PASS recovered**;
- finite-core exact certificate: **not essential to the analytic source theorem**, as P26 explicitly agrees; exact certificates exist for the auxiliary finite deterministic claims;
- prior-art/source search: **recorded and refreshed, but bounded; publication novelty UNVERIFIED**.

Therefore the source theorem has crossed from 0/2 to **1/2 independent audits** but remains `PROVED-CANDIDATE / AUDIT-PENDING`, not `PROVED` under the fleet closure standard.

The stronger surplus theorem in Section 6 is an owner-track strengthening and has **0/2 external audits as a strengthening**. It must not be silently substituted for the already-audited source theorem when counting closure evidence.

Because the frozen metric has now been unchanged for three consecutive runs, the next invocation must obey Section I: a thinking-only stuck report with no new claim, unless a genuine external state change (for example an NM13-05 audit) directly changes the closure obligation. The simplest remaining source-level obligation is not another lemma: it is the distinct NM13-05 end-to-end audit. If such an audit PASS appears, enter the paper-package protocol; if it identifies a gap, repair exactly that gap; if it remains absent, do not manufacture checker-only filler.

## 11. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  status: PROVED_CANDIDATE_AUDIT_PENDING_1_OF_2
  source_id: P0457
  claim_id: operations/claims/P0457.md
  dedup_key: diameter_near_the_newly_established_bilateral_connectivity_threshold
  selection_residue: 3
  metric:
    name: S_exact
    before: UNBOUNDED
    after: UNBOUNDED
    normalization_changed: false
  mathematical_movement_in_frozen_metric: false
  substantive_research_progress:
    stronger_theorem: "If s_n=k-log n>0, k<=T log n, and s_n^2/(k log k)->infinity, then D(LK(n,k))/(log n/log log n)->1 in probability; hence LK is connected whp."
    proof_status: FULL_ARGUMENT_ON_REPORT_PAGE_SELF_PROOF
    external_audit_for_strengthening: NONE
  section_B_methods:
    attempted_this_run: [3, 5, 20]
    all_previously_used_on_P0457: true
    reuse_disclosed: true
    immediately_previous_triple: [20, 22, 27]
    outcomes:
      3: "proved a stronger surplus-window theorem down to s_n >> sqrt(k log k)"
      5: "optimized the block/capacity parameter delta=min{s/(8k),1/100}; identified the s^2/k versus log k balance"
      20: "isolated the one-round barrier at s=O(sqrt(k log k)); no counterexample claimed"
  counters:
    unchanged_runs_before: 2
    unchanged_runs_after: 3
    stuck_recoveries_before: 1
    stuck_recoveries_after: 1
    stuck_protocol_next_run: true
    closable_rotation_threshold: 6
  audits:
    P26:
      status: PASS
      audit_id: P26-AUDIT-NM13-04-P0457-LOGBAND-DIAMETER-42
      commit: b24af197056636b9e31b135d21f4059e55cd45d6
      scope: frozen source near-log diameter theorem; not automatic audit of this run's sharper surplus theorem
    NM13-05: NOT_PASSED
    closure_gate: 1_of_2
  literature_check:
    date: 2026-09-18
    source_primary: "Dabirian-Subramanian, J. Appl. Probab. 63(2), DOI 10.1017/jpr.2025.10051"
    source_open_problem_still_present: true
    predecessor: "La-Kabkab, Internet Mathematics 11(6) (2015), DOI 10.1080/15427951.2015.1022626"
    classical_input: "Chung-Lu, Advances in Applied Mathematics 26 (2001), 257-279"
    later_source_matching_resolution_found: false
    scope_note: "bounded dated web/primary-source search; not proof of worldwide openness or publication novelty"
  artifacts_created: []
  claim_created_or_modified: false
  shared_root_edits: NONE
  peer_edits: NONE
  next_step: "Section-I thinking-only stuck invocation unless a genuine external audit/status change intervenes; check NM13-05 first; if PASS, package closure, if gap, repair only that gap, otherwise do not manufacture filler certificates."
```

No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, unreviewed external script, peer-track edit, shared-root edit, claim edit, or scheduler creation/modification was performed.

**End of immutable run report.**