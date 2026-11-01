Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `S_exact = 3 -> 3`. Methods actually tried: #6, #13, #29.**

# NM13-04 / P0457 — independent two-round capacity proof of uniform core attachment

Run UTC: 2026-09-18T04:16:59Z  
Track: `NM13-04 Graph Counterexamples`, CLOSABLE OUTSIDE.  
Canonical source/claim: `P0457`, `operations/claims/P0457.md`.  
Source-level state after this run: **PROVED-CANDIDATE / closure AUDIT-PENDING** for the frozen near-logarithmic target.  
Frozen metric after this run: **`S_exact = 3` (unchanged)**.

## 1. Continuity, ownership, required reads, and runtime controls

I continued the already admitted P0457 assignment. I did not reopen intake and did not create a second claim.

Canonical identity remains:

- source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025;
- exact source target: characterize the diameter of `LK(n,k)` in the additional near-logarithmic range where the paper's Theorem 6 proves connectivity;
- canonical dedup key: `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA256: `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- residue modulo 13: `3`, matching NM13-04's exclusive shard;
- exclusive owner: NM13-04.

Before new mathematics I reread/recovered `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; the later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the canonical claim; canonical dedup/intake history; the P0457 catalog/attempt history; the newest own report `2026-09-18T03-22-30Z__p0457-stuck-recovery-1.md`; and the newest visible neighboring reports. NM13-03 remains admission-pending in its newest visible run. NM13-05's newest visible run is `2026-09-18T03-24-12Z__d0004-stuck-recovery-1.md`, continuing D0004 rather than auditing P0457. Exact repository search recovered no P26 or NM13-05 P0457 audit pass, no release, no competing owner, no handoff, no POSTED settlement, and no source-specific correction superseding the theorem candidate.

Large aggregate ledgers can be connector-truncated, so exact claim/report/dedup reads remain authoritative for continuity. I do not treat inaccessible, deleted, non-master, or truncated history as empty.

The exposed task-control surface still has prompt/title, timing/schedule, enabled-state and timing-mode controls but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-effort telemetry**. `GPT-6 / maximum` is therefore still prompt text only. This invocation actually runs GPT-5.6 Sol; reasoning is `UNVERIFIED`. The historical P26 `You cannot modify this task` refusal is an authorization/context boundary; the legitimate remedy is an owning/authorized account, workspace, product/admin/API surface or platform support, not task duplication or access-control bypass. No support escalation is claimed.

## 2. Fresh source and literature status — 2026-09-18 UTC

I rechecked the current Cambridge source, including the rendered Open Problems page. The source still explicitly asks for “characterizing the diameter for the additional range of `k(n)` from Theorem 6 where connectivity holds.” Its connected side is

`k >= log n + t0 sqrt(log n) log log n`, with fixed `t0>1/2`.

The nearest solved same-model result remains La–Kabkab, *A New Random Graph Model with Self-Optimizing Nodes: Connectivity and Diameter*, Internet Mathematics 11 (2015), 528–554, DOI `10.1080/15427951.2015.1022626`. Their diameter mechanism uses a connected embedded Erdős–Rényi graph under the stronger condition `k > beta_* log n`, `beta_* ~= 2.4626`, and obtains the `log n/log log n` scale.

Fresh bounded searches on 2026-09-18 used the exact 2026 title plus `diameter`, the author names plus `bilateral preference diameter`, `LK(n,k) diameter`, and the 2015 predecessor title. They recovered the current source, the predecessor, and adjacent random-graph material, but no later source-matching resolution. This is **bounded negative evidence only**, not proof of worldwide openness and not a publication-novelty certificate.

## 3. Frozen metric and run counters

The canonical metric remains

`S_exact = largest co-degree s >= 0 for which NM13-04 has a complete deterministic diameter classification for LK(n,n-1-s), uniformly over the stated feasible n.`

The metric is deliberately not redefined to track the asymptotic source theorem.

- before this run: `S_exact = 3`;
- after this run: `S_exact = 3`;
- movement: **none**;
- consecutive unchanged invocations since the last metric movement: **5**;
- stuck recoveries used: **1**;
- CLOSABLE rotation gate: **6 unchanged invocations**, so exactly one further unchanged invocation would trigger the required handoff/rotation unless closure, a source-status correction, or legitimate movement supersedes it.

The preceding stuck recovery chose exactly one action: port the nearest solved sparse-ER/core technique into an **independent two-round exposure/sprinkling derivation of the uniform attachment lemma**, rather than reread the existing leave-one-out proof. This run executes that action.

## 4. Recovered setup and the closure-critical statement

Use the equivalent exponential-score representation: edges of `K_n` receive iid `Exp(1)` scores; every vertex proposes its `k` largest incident scores; an edge survives iff both endpoints propose it.

Fix constants `t0>1/2` and `T>1` and suppose

`log n + t0 sqrt(log n) log log n <= k <= T log n`.

Put

`h := sqrt(log n) log log n`,
`theta := t0/8`,
`delta := theta h/k`,
`m := ceil(1/delta)`.

Partition `[n]` deterministically into balanced blocks `B_1,...,B_m`. For block indices `i,j`, let

`D_ij := B_i union B_j`,
`W_ij := [n] \ D_ij`,

with only one copy removed when `i=j`. The preceding sharp-diameter report defined `C_ij` as the largest component of the threshold graph on `W_ij` whose edges have score above

`L_+ := log((n-1)/k)+2`.

Its standard ER component estimate proved, simultaneously for all `i,j`,

`|C_ij| >= |W_ij| - n/k^3`                                                     (4.1)

with probability `1-o(1)`.

The closure-critical statement is

`P(exists i,j, v in B_i : N_LK(v) intersect C_ij = empty) = o(1)`.              (4.2)

The previous proof of (4.2) used per-target leave-one-out `k`th order statistics `T_w^(-v)` and a global bad set. The argument below does **not** use those variables or that global bad-set device. Instead it exposes internal core capacity first and boundary edges second.

## 5. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: expose a capacity reserve and track it to the source edge

Set the lower boundary threshold

`q := log((n-1)/k)+delta`,
`p := P(Exp(1)>q) = e^(-delta) k/(n-1)`.                                      (5.1)

For fixed `i,j`, abbreviate `D=D_ij`, `W=W_ij`, `d=|D|`, `N=|W|`, and `C=C_ij`.

### Round 1: expose only internal edges of W

For each `w in W`, define its internal `q`-exceedance count

`X_w := #{u in W\{w}: V_wu > q}`.

These counts are now fixed after round 1. Define

`mu_out := (d-1)p`,
`a := delta k/3`,

and the **capacity-good core**

`G := {w in C : X_w <= k - mu_out - a - 2}`.                                  (5.2)

Because `m=ceil(1/delta)`, balanced blocks give

`d <= 2n/m+2 <= 2 delta n+2`,

and hence, uniformly in the block pair,

`mu_out <= 3 delta k`                                                          (5.3)

for all sufficiently large `n`.

Marginally `X_w~Bin(N-1,p)`, with mean `mu_in=(N-1)p`. Since

`mu_in+mu_out=(n-2)p < e^(-delta) k`,

we have

`k-mu_out-a-2-mu_in`
` >= k(1-e^(-delta)) - delta k/3 - 2`
` >= delta k/2`                                                               (5.4)

for all sufficiently large `n`, because `delta ->0` and `delta k=theta h -> infinity`.

Bernstein's binomial upper-tail inequality therefore gives the uniform bound

`P(w not capacity-good before intersecting C) <= exp(-delta^2 k/12)`.          (5.5)

Let

`r := exp(-delta^2 k/24)`.

For any fixed pair `(i,j)`, Markov's inequality implies that more than `nr` capacity-bad vertices occur with probability at most `r`. Moreover

`delta^2 k = theta^2 h^2/k >= (theta^2/T)(log log n)^2`,

so `m^2 r ->0`. A union bound over all `O(m^2)` block pairs, together with (4.1), yields

`|G|/(n-1) >= 1 - 2 delta - o(delta)`                                          (5.6)

simultaneously for every pair, with probability `1-o(1)`.

This calculation is the deformation step. At fixed `k=(1+epsilon)log n`, the attachment exponent below has a macroscopic `epsilon log n` reserve. The same formulas remain valid when that reserve shrinks all the way to

`epsilon_n log n = t0 sqrt(log n) log log n`.

The only loss we will spend is `3 delta k=3 theta h`, leaving the strict positive margin `(t0-3theta)h=5t0 h/8` at the source edge.

**Outcome of method #6:** succeeded. The fixed-epsilon argument deforms quantitatively to the source's shrinking near-threshold excess without changing the model or the quantifiers.

## 6. Round 2 boundary sprinkling: target proposal is certified by spare capacity

Now expose the boundary edges between `D` and `W`; internal `W` edges remain the already fixed round-1 data.

Fix an endpoint `v in D` and a target `w in G`. Define

`Y_w^(-v) := #{u in D\{v}: V_uw > q}`.

Conditional on round 1, as `w` varies these variables use disjoint boundary-edge bundles. Each has law

`Y_w^(-v) ~ Bin(d-1,p)`,

with mean `mu_out`, and `V_vw` is independent of `Y_w^(-v)`.

By the additive Bernstein bound and (5.3),

`P(Y_w^(-v) > mu_out+a) <= exp(-delta k/60) =: eta.                           (6.1)

Indeed,

`a^2/[2(mu_out+a/3)] >= delta k/56`,

so the displayed constant `1/60` is conservative.

Call `w` **safe for v** if

`w in G`, `V_vw>q`, and `Y_w^(-v) <= mu_out+a`.                               (6.2)

For a safe target, (5.2) gives

`X_w + Y_w^(-v) + 1`
` <= (k-mu_out-a-2)+(mu_out+a)+1`
` <= k-1`.                                                                    (6.3)

Thus at most `k` incident edges of `w` exceed `q`, including `vw`; since `V_vw>q`, vertex `w` certainly proposes `vw`.

Conditional on round 1, the safety indicators for distinct `w in G` are independent and each has probability at least `p(1-eta)`. Hence

`P(no safe target for v | round 1)`
` <= exp(-p(1-eta)|G|).                                                       (6.4)

Using (5.1), (5.6), `e^(-delta)>=1-delta`, and `eta=o(delta)`,

`p(1-eta)|G|`
` >= k(1-delta)(1-2delta-o(delta))(1-eta)`
` >= k - 3 delta k - o(h)`
` >= log n + (5t0/8-o(1))h.                                                  (6.5)

Therefore even after union over at most `nm` endpoint/core requirements,

`nm exp(-p(1-eta)|G|) ->0`.                                                   (6.6)

This is already the needed target-side bilateral acceptance. It remains to force the endpoint `v` itself to choose at least one safe edge without using the previous top-`k` hypergeometric calculation.

## 7. Method #13 — FIND WHAT ONLY INCREASES: an unsafe-edge count forces one safe proposal

For fixed `v`, let

`R_v := {w != v : V_vw>q}`

be the set of all its `q`-high incident edges, and let `A_v` be its safe targets from (6.2). Define the number of **unsafe high edges**

`Z_v := |R_v \ A_v|`.                                                         (7.1)

The key deterministic certificate is

`A_v != empty and Z_v < k  ==>  v proposes an edge to A_v`.                   (7.2)

To prove (7.2): if `|R_v|<=k`, every `q`-high edge is among `v`'s top `k`, so every safe edge is proposed. If `|R_v|>k`, all of `v`'s top `k` edges are in `R_v`; if none were safe, all `k` would be counted by `Z_v`, contradicting `Z_v<k`.

This is the monotone quantity the earlier proof did not exploit: enlarging the capacity-good set `G` or turning a target from capacity-bad to capacity-good can only **decrease** `Z_v` and enlarge `A_v`. Once the unsafe count drops below `k`, proposal of a safe edge is forced, regardless of the detailed order of the top `k` scores.

Conditional on round 1, unsafe high targets come from two sources:

1. labels outside `G` (including the endpoint block boundary), whose count is at most `(2delta+o(delta))(n-1)` by (5.6), each high with probability `p`;
2. labels `w in G` for which `V_vw>q` but the capacity tail in (6.1) fails, with probability at most `p eta` each.

For fixed `v` these targetwise events are independent after the natural boundary-edge exposure. Thus `Z_v` is dominated by a Poisson-binomial variable of mean at most

`(3delta+eta)k <= 4 delta k`                                                  (7.3)

for all sufficiently large `n`. The standard Chernoff bound gives

`P(Z_v>=k | round 1) <= (4e delta)^k`.                                        (7.4)

Since `delta=Theta(log log n/sqrt(log n))` uniformly for `k=Theta(log n)`,

`nm (4e delta)^k ->0`.                                                        (7.5)

Combining (6.6), (7.5), and the round-1 high-probability capacity/core event proves simultaneously that every required endpoint has a safe target it proposes. By (6.3), that target also proposes back. Hence (4.2) follows.

**Outcome of method #13:** succeeded. The unsafe-edge count is a monotone forcing certificate that removes any need to analyze the distribution of the endpoint's top-`k` labels conditional on the core.

## 8. Method #29 — ADD THE POINTS AT INFINITY: outsiders become an explicit boundary layer

The direct lower-ER proof failed because its threshold graph is not spanning near `k~log n`; exceptional vertices were silently outside the comparison component. Here those outsiders are not treated as an error in a graph-diameter convention. They are promoted to an explicit boundary layer:

- `C_ij` is the solved interior object;
- `W_ij\G_ij` is a capacity-defective boundary set of relative size `2delta+o(delta)` after including the deleted endpoint blocks;
- every source endpoint is attached from this boundary to the interior by one fresh bilateral edge.

The proof above quantifies that boundary exactly through `Z_v`. Once `Z_v<k`, at least one of the endpoint's top `k` choices must cross to a safe interior target. Thus core diameter and entry-to-core cost are separated rather than conflated.

**Outcome of method #29:** succeeded. Treating outsiders as an explicit boundary state makes the maximum-distance quantifier honest and prevents disconnected lower-comparison components from being hidden by a finite-component diameter convention.

## 9. Independent attachment lemma obtained this run

The previous sections prove the following source-relevant lemma independently of the prior leave-one-out order-statistic argument.

### Lemma P0457-TWO-ROUND-CAPACITY-ATTACHMENT

Fix `t0>1/2` and `T>1`. Uniformly for integer sequences

`log n + t0 sqrt(log n) log log n <= k <= T log n`,

construct the balanced blocks and block-deleted threshold cores `C_ij` as above. Then

`P(exists i,j, v in B_i : N_LK(n,k)(v) intersect C_ij = empty) = o(1)`.

### Proof summary

Round 1 exposes only internal edges of each block-deleted region and shows that all but `o(delta n)` core vertices retain at least `mu_out+a+2` units of proposal capacity for the still-unexposed boundary. Round 2 exposes the boundary. For every endpoint, exponentially many-in-the-relevant-scale safe targets exist with failure exponent

`log n + (5t0/8-o(1))sqrt(log n)log log n`.

A separate unsafe-high-edge count is `<k` uniformly, forcing at least one safe target into the endpoint's top `k`. Safe target capacity forces the reciprocal proposal. Union bounds over all `nm` endpoint/core requirements are summable. QED.

This is a **self-rederivation**, not an independent audit. It strengthens confidence in the closure hinge because it avoids the prior proof's `T_w^(-v)`, `B_v`, and global bad-set conditioning mechanism. It does not count as P26 or NM13-05 certification.

## 10. Consequence for the existing sharp-diameter theorem candidate

The preceding report already proved the standard threshold sandwich

`G_+ subset LK(n,k) subset G_-`,

with `np_+,np_-=Theta(log n)`, and the block cores `C_ij` lie in `G_+`. The new lemma independently supplies the only nonstandard maximum-quantifier attachment step. Therefore the previous squeeze remains:

`diam(G_-) <= diam(LK(n,k)) <= diam(G_+) + 2`,

and the classical sparse-ER first-order diameter law yields

`diam(LK(n,k))/(log n/log log n) ->1`

in probability throughout the frozen near-logarithmic scope.

I do **not** promote the source to repository-closed. Closure still requires end-to-end independent audits by P26 and NM13-05; neither was recovered as passed. No paper folder is created before those audits. No theorem beyond the already stated P0457 source scope is claimed, and publication novelty remains unverified.

## 11. Why no checker artifact was created

This run's finite-looking counts are symbolic binomial/Chernoff estimates inside an asymptotic analytic proof; there is no finite search core whose exact execution would validate the argument. Under the owner's 90/10 rule, manufacturing a checker for the unchanged frozen metric would be bookkeeping without mathematical value. The complete proof is on the page.

## 12. Section-B method accounting

The three methods actually attempted in this run were the reserved post-recovery triple:

- **#6 DEFORM TO A POINT YOU CAN SOLVE.** Started from the easy fixed-`epsilon` logarithmic regime and tracked the capacity reserve to the shrinking Theorem-6 excess. **Succeeded:** the only spent reserve is `3theta h`, leaving `5t0 h/8`.
- **#13 FIND WHAT ONLY INCREASES.** Replaced endpoint top-`k` distribution analysis by the monotone unsafe-high-edge count `Z_v`. **Succeeded:** `Z_v<k` deterministically forces a safe proposal.
- **#29 ADD THE POINTS AT INFINITY.** Made threshold-core outsiders an explicit boundary layer with a one-edge entry cost. **Succeeded:** disconnected lower-comparison vertices no longer contaminate the maximum-distance argument.

These methods were not counted as attempted in the immediately preceding recovery run (#7/#21/#22).

If no audit, source correction, closure, or legitimate metric movement arrives before the next NM13-04 invocation, that run is the **sixth consecutive unchanged-metric invocation** and must preserve a full handoff and rotate at its end rather than begin a seventh unchanged P0457 run.

## 13. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  source_id: P0457
  claim_id: P0457
  canonical_dedup_key: diameter_near_the_newly_established_bilateral_connectivity_threshold
  status: PROVED_CANDIDATE_AUDIT_PENDING
  exact_scope:
    model: "LK(n,k), bilateral preference graph from iid continuous edge scores"
    parameters: "fixed t0>1/2 and T>1; log n+t0*sqrt(log n)*log log n <= k <= T*log n"
    conclusion: "diam(LK(n,k))/(log n/log log n) -> 1 in probability"
  metric:
    name: S_exact
    before: 3
    after: 3
    movement: false
  source_level_progress:
    new_result: TWO_ROUND_CAPACITY_ATTACHMENT_SELF_REDERIVATION
    closure_hinge: "uniform one-edge endpoint-to-block-core attachment"
    dependence_mechanism: "round-1 internal capacity + round-2 boundary sprinkling + unsafe-edge forcing"
    independent_of_previous_leave_one_out_bad_set: true
  section_B_methods:
    attempted: [6, 13, 29]
    outcomes:
      6: "fixed-epsilon capacity reserve deformed to source-scale excess; succeeded"
      13: "unsafe q-high count is monotone forcing certificate; succeeded"
      29: "explicit boundary-layer treatment of core outsiders; succeeded"
  finite_artifact: NONE_ANALYTIC_THEOREM_NO_FINITE_CORE
  literature_check:
    date_utc: 2026-09-18
    original_source: RECHECKED_OPEN_PROBLEM_AND_THEOREM6_SCOPE
    predecessor_2015: RECHECKED_DIAMETER_AND_BETA_STAR_SCOPE
    later_source_matching_resolution_found: false
    negative_search_scope: BOUNDED_NOT_NOVELTY_CERTIFICATE
  audits:
    P26: NOT_YET_PASSED
    NM13-05: NOT_YET_PASSED
    this_self_rederivation_counts_as_audit: false
  unchanged_runs_since_metric_movement: 5
  stuck_recoveries_used: 1
  next_unchanged_run: SIX_RUN_CLOSABLE_ROTATION_GATE
  shared_root_edits: NONE
  peer_track_edits: NONE
```

No email/Gmail, Drive, public posting, paid compute, permission change, unreviewed external script, workflow execution, peer-track edit, shared-root edit, or schedule creation/modification was performed.

**End of immutable run report.**
