Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `S_exact = UNBOUNDED -> UNBOUNDED`. Adversarial self-audit found and exactly certified a wording error in the auxiliary all-s theorem; methods actually reused as audit lenses: #2, #19, #29. They are NOT represented as previously untried: the prior immutable report records that all thirty Section-B methods have already been used on P0457.**

# NM13-04 / P0457 — disconnected-shell counterexample and corrected all-s classifier

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-04 Graph Counterexamples`, `CLOSABLE OUTSIDE`  
Canonical source/claim: `P0457`, `operations/claims/P0457.md`  
Parent source status after this run: **PROVED-CANDIDATE / AUDIT-PENDING** for the frozen near-logarithmic diameter target; **not repository-closed**  
Frozen deterministic metric: **UNBOUNDED**  
Consecutive unchanged metric runs after the last movement: **1**  
Stuck recoveries used: **1**  
Designated eventual auditors: **P26 and NM13-05; neither is counted as passed**

## 1. Runtime/control disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The task-control surface available to this worker still exposes prompt/title, schedule/timing, timing mode and enabled state, but **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Enforcing it would require an owner-authorized product/workspace/API/admin surface exposing those controls together with authenticated per-run runtime attestation.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary. Current repository policy records later successful P26 modification from another authorized context. If such a refusal recurs, the legitimate route is the owning/otherwise-authorized task context or an authorized product/admin/API/support surface; do not clone the task and do not bypass access controls. No schedule or permission was modified here.

## 2. Authoritative continuity and required repository read

I continued the already admitted P0457 source. Intake was **not** reopened, no new claim was created, and no shared root or peer namespace was edited.

Before new mathematics I reread or targeted-recovered the current state required by the owner from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0457.md`;
- exact-ID/dedup/source/attempt searches for P0457;
- newest own report `2026-09-18T06-18-40Z__p0457-all-s-classification-saturation.md`;
- newest neighboring NM13-03 report `2026-09-18T07-18-05Z__admission-delta-screen-11.md`;
- newest neighboring NM13-05 report `2026-09-18T07-03-00Z__successor-admission-screen-1.md`;
- newest visible P26 audit report `2026-09-18_10-00-00__run-report.md`;
- fresh repository searches for P0457 audit passes and ownership changes.

The canonical identity remains unchanged:

- campaign ID: `P0457`;
- dedup key: `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA256: `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- residue modulo 13: `3`;
- exclusive owner: NM13-04.

The repository delta after the previous NM13-04 report contains many other-track reports and several new ownership claims, but no P0457 release, competing owner, source settlement, or external audit pass. The newest P26 report audits R19/E0071, not P0457. The newest NM13-05 report explicitly says its being named as P0457's eventual auditor is **not** an audit pass. Thus the two-audit gate is still 0/2 for P0457.

Large aggregate ledgers are connector-bounded when rendered wholesale. Exact paths, current roots, exact claims, immutable own reports, and exact-ID searches are the continuity anchors; missing or truncated material is not treated as evidence of absence.

## 3. Fresh source and literature check — 2026-09-18

I rechecked the primary Dabirian--Subramanian source and a fresh bounded search for the exact title/authors plus `diameter` and `bilateral preference random graph diameter`.

Primary source:

`https://www.cambridge.org/core/journals/journal-of-applied-probability/article/connectivity-of-a-family-of-bilateral-preference-random-graphs/0A1D5D7560AB2DC6C8255F1522DC3BB2`

Primary PDF:

`https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0A1D5D7560AB2DC6C8255F1522DC3BB2/S002190022510051Xa.pdf/connectivity_of_a_family_of_bilateral_preference_random_graphs.pdf`

The source still states that an open problem is to characterize the diameter for the additional range of `k(n)` from Theorem 6 where connectivity holds. The bounded current search recovered the source and bibliographic mirrors but no later source-matching resolution. This is **bounded negative evidence only**, not proof of worldwide openness or publication novelty.

The source-level theorem candidate from the earlier report remains:

`diam(LK(n,k)) / (log n / log log n) -> 1` in probability

for fixed `t0>1/2`, fixed `T>1`, and

`log n + t0 sqrt(log n) log log n <= k <= T log n`.

Nothing in the correction below attacks that analytic theorem. The defect found here is in the separate deterministic all-co-degree theorem's treatment of disconnected pairs.

## 4. Frozen metric before/after

The frozen metric is

`S_exact = largest co-degree s for which a complete deterministic diameter classifier is proved uniformly for exact LK(n,n-1-s)`.

The previous run moved it from `4` to `UNBOUNDED` by proving a parameter-uniform complement-degeneracy classifier. This run found a quantifier defect in one clause of the written theorem but repaired it without losing any co-degree.

- before: `S_exact = UNBOUNDED`;
- after: `S_exact = UNBOUNDED`;
- movement: **none**;
- consecutive unchanged metric runs after last movement: **1**;
- stuck recoveries used: **1**.

This is genuine substantive correction but not metric movement.

## 5. Method #2 — ATTACK THE NEGATION FIRST: exact source-valid counterexample to the auxiliary theorem wording

The newest report stated, in item 5 of `P0457-ALL-S-CLASS`, that **for every nonedge** `uv`, the shell grown from `N_G(u)` meets `N_G(v)` within `s` expansions. Its proof invoked a diameter lemma assuming connectivity. I attacked that universal quantifier directly.

Take

`n=4, s=2, k=n-1-s=1`

and assign distinct source edge weights

`w12=1, w34=2, w13=10, w14=11, w23=12, w24=13`.

Each vertex proposes its unique lowest-weight incident edge. Hence the bilateral graph is exactly

`LK(4,1) = {12,34}`,

two disjoint edges.

For the nonedge `u=1, v=3`,

`N(1)={2}`, `N(3)={4}`.

The shells from `N(1)` are

`R_0={2}`, `R_1={1,2}`, `R_2={1,2}`,

and therefore none intersects `N(3)={4}`. No `j_* in {0,1,2}` exists. The universal wording of item 5 is false on this exact source-valid realization.

This is **not** a refutation of the source problem, and it is **not** a refutation of the source-level near-logarithmic theorem candidate. It is a correction to an auxiliary deterministic theorem written by this track in the immediately preceding run.

The idea was recorded before code at commit

`a3abe5f54283aa004f4f75f76ee52fc200e1ae29`.

The exact checker was then committed at

`69ea50be6f8e36d0f1718afd58be5d3d936a0dd3`,

path

`proofnet24/NM13-04/artifacts/2026-09-18/2026-09-18T07-20-00Z__p0457_disconnected_shell_exact.py`.

It was executed with exact integer comparisons in authorized local compute. The archived output is at commit

`c3bd7e0bee3e12ce0aece903c44695eba5371a36`,

path

`proofnet24/NM13-04/artifacts/2026-09-18/2026-09-18T07-20-00Z__p0457_disconnected_shell_exact.out`,

and terminates

`ALL_EXACT_CHECKS_PASS`.

**Outcome of #2:** successful adversarial self-audit; found an exact four-vertex counterexample to the overbroad shell quantifier.

## 6. Method #29 — ADD THE POINTS AT INFINITY: put disconnected distance into the state space

The defect is exactly a missing boundary state. For vertices in different connected components, graph distance is not a large finite integer; under the extended-distance convention it is `+infinity`.

Once `+infinity` is admitted explicitly, the correct pair classifier is:

- adjacent pair: distance `1`;
- nonadjacent pair in the same connected component: finite shell formula below;
- pair in different components: distance `+infinity`.

If one instead uses the convention that the diameter of a disconnected graph means the maximum **finite component diameter**, the third branch is excluded from the maximum and one takes the maximum of the componentwise finite distances. Both conventions are now explicit rather than silently conflated.

**Outcome of #29:** successful; the missing disconnected boundary state is the entire logical gap.

## 7. Method #19 — MAKE IT AN ALGORITHM: corrected all-s classifier

The repair is parameter-uniform and slightly strengthens the old connected-diameter lemma.

### Lemma 7.1 — every source component has diameter at most `s+2`

Let `G=LK(n,n-1-s)` and `H=bar G`. The previous proof that `H` is `s`-degenerate is unchanged.

Take any two vertices in the same connected component of `G`, and let

`v_0,v_1,...,v_d`

be a shortest path between them. This path is induced in `G`: a chord between nonconsecutive path vertices would shorten it. Therefore in the complement induced on these `d+1` path vertices, every internal vertex has at least `d-2` neighbors. Hence that induced subgraph of `H` has minimum degree at least `d-2`.

Because every induced subgraph of an `s`-degenerate graph has a vertex of degree at most `s`,

`d-2 <= s`,

so

`d <= s+2`.

No assumption that **all of G is connected** is needed. Thus every connected component has diameter at most `s+2`. QED.

### Lemma 7.2 — exact finite shell identity for same-component nonedges

Let `u,v` be nonadjacent vertices in the same connected component, and put

`A=N_G(u)`, `B=N_G(v)`.

Exactly as in the previous report,

`d_G(u,v) = 2 + dist_G(A,B)`.

Indeed, a geodesic from `u` to `v` has its first internal vertex in `A` and last internal vertex in `B`, giving one inequality; concatenating `u-a`, an `A`--`B` geodesic, and `b-v` gives the reverse inequality.

By Lemma 7.1, `d_G(u,v)<=s+2`, so

`dist_G(A,B)<=s`.

Define `R_0=A` and `R_{j+1}=R_j union N_G(R_j)`. Then the first

`j_*=min{j>=0:R_j intersects B}`

exists and satisfies `j_*<=s`, with

`d_G(u,v)=2+j_*`.

QED.

### Corrected theorem P0457-ALL-S-CLASS-v2

For every `n>=2`, every `0<=s<=n-2`, and every tie-free source weight assignment, let

`G=LK(n,n-1-s)`.

Then:

1. for `s=0`, `G=K_n`;
2. for `s>=1`, `bar G` is `s`-degenerate;
3. if `G` is disconnected, at most `s` vertices lie outside a largest component (unchanged from the prior proof);
4. **every** connected component of `G` has diameter at most `s+2`;
5. for every pair `u,v`:
   - if adjacent, `d(u,v)=1`;
   - if nonadjacent and in the same component, the shell algorithm above stops by depth `s` and returns `d(u,v)=2+j_*`;
   - if in different components, `d(u,v)=+infinity` in the extended-distance convention.

Therefore a complete deterministic classifier for every co-degree is obtained by first computing connected components and then running at most `s` shell expansions only for same-component nonedges. Under the maximum-finite-component convention, take the maximum finite value over the components. Under the usual extended-distance convention, disconnected graphs have infinite diameter.

This repairs the exact quantifier defect while preserving the parameter-uniform all-`s` result. Hence `S_exact` remains **UNBOUNDED**.

**Outcome of #19:** successful; the corrected classifier is an explicit terminating algorithm and the full proof is on this page.

## 8. Section-B accounting under method exhaustion

The preceding immutable report explicitly records that **all thirty** Section-B methods have already been genuinely attempted on P0457. The generic rule to choose three previously untried moves is therefore no longer satisfiable on this admitted source. I do not fabricate new method numbers or falsely call a reused move untried.

For this adversarial correction I reused #2/#29/#19 as actual proof lenses. This triple differs from the immediately preceding #8/#17/#23 triple, and every outcome is stated above. The reuse is transparent and is not credited as fresh method inventory.

The source-specific continuity still controls the next state: the deterministic metric is saturated; further co-degree bookkeeping is prohibited. The only legitimate reasons for more P0457 mathematics are a concrete audit defect, a source/literature correction, or an owner-authorized closure step.

## 9. Audit gate and effect on source-level status

Fresh current checks recover:

- **P26:** no P0457 pass; its newest visible audit is for R19/E0071.
- **NM13-05:** no P0457 pass; its newest report explicitly says the designation as eventual P0457 auditor is not a pass.

Therefore P0457 remains **PROVED-CANDIDATE / AUDIT-PENDING**, not closed.

The correction in this run concerns only the deterministic all-s auxiliary theorem. The source-level logarithmic diameter proof does not use the false cross-component shell clause and remains exactly at its prior candidate status. No audit is silently promoted by this self-check.

No paper folder is created before both outside audits pass. No new checker is manufactured for the analytic source theorem, which has no essential finite core.

## 10. Next legal state

The next invocation should first check for an actual P26 or NM13-05 P0457 audit or a source/literature correction. If an audit identifies a mathematical flaw, repair exactly that obligation. If both independent audits pass, proceed to the owner closure/paper-package protocol. If neither exists, do not manufacture another finite certificate or another co-degree lemma merely to fill a run.

Because the frozen metric did not move this time, the supported unchanged count is now **1** after the previous run's movement to `UNBOUNDED`. The existing stuck-recovery count remains **1**.

## 11. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  source_id: P0457
  claim_id: operations/claims/P0457.md
  canonical_dedup_key: diameter_near_the_newly_established_bilateral_connectivity_threshold
  owner: NM13-04
  source_status: PROVED_CANDIDATE_AUDIT_PENDING
  source_target:
    model: "LK(n,k) bilateral-preference graph from iid continuous edge weights"
    question: "diameter in the additional logarithmic range from Dabirian--Subramanian Theorem 6"
  metric:
    name: S_exact
    before: UNBOUNDED
    after: UNBOUNDED
    movement: false
    reason: "auxiliary all-s theorem wording corrected; parameter-uniform classifier survives"
  auxiliary_theorem_correction:
    prior_theorem: P0457-ALL-S-CLASS
    defect: "item 5 incorrectly quantified shell intersection over cross-component nonedges"
    exact_counterexample:
      n: 4
      s: 2
      k: 1
      LK_edges: [[1,2],[3,4]]
      cross_component_pair: [1,3]
      old_shell_claim: false
    corrected_theorem: P0457-ALL-S-CLASS-v2
    status: PROVED_ON_PAGE_SELF_CHECKED
  section_B_methods:
    attempted_this_run: [2, 29, 19]
    previously_untried: []
    method_inventory_exhausted_before_run: true
    reuse_disclosed: true
    outcomes:
      2: "found exact source-valid n=4 counterexample to the overbroad auxiliary quantifier"
      29: "made +infinity/cross-component boundary state explicit"
      19: "proved corrected component-first shell algorithm for every s"
  exact_certificate:
    idea_note_commit: a3abe5f54283aa004f4f75f76ee52fc200e1ae29
    checker: proofnet24/NM13-04/artifacts/2026-09-18/2026-09-18T07-20-00Z__p0457_disconnected_shell_exact.py
    checker_commit: 69ea50be6f8e36d0f1718afd58be5d3d936a0dd3
    output: proofnet24/NM13-04/artifacts/2026-09-18/2026-09-18T07-20-00Z__p0457_disconnected_shell_exact.out
    output_commit: c3bd7e0bee3e12ce0aece903c44695eba5371a36
    terminal: ALL_EXACT_CHECKS_PASS
  source_level_candidate:
    theorem: P0457-SHARP-LOGBAND-DIAMETER
    affected_by_this_correction: false
    status: PROVED_CANDIDATE_AUDIT_PENDING
  literature_check:
    date_utc: 2026-09-18
    original_source: RECHECKED
    source_open_problem_wording: RECHECKED
    later_source_matching_resolution_found: false
    negative_search_scope: BOUNDED_NOT_WORLDWIDE_CERTIFICATE
  audits:
    P26: NOT_PASSED_OR_RECOVERED
    NM13-05: NOT_PASSED_OR_RECOVERED
  counters:
    unchanged_runs_since_metric_movement: 1
    stuck_recoveries_used: 1
  next_step: "CHECK_EXTERNAL_AUDITS_FIRST; repair only a concrete audit defect; if both pass, closure/package; otherwise no filler certificate"
  report_policy:
    shared_root_edits: NONE
    peer_track_edits: NONE
    new_claim_file: NONE
    email_drive_public_posting: NONE
    workflow_or_permission_change: NONE
    schedule_change: NONE
```

**End of complete run report.**