Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `S_exact = UNBOUNDED -> UNBOUNDED`. Mandatory Section-I thinking-only stuck recovery 2; no new mathematical claim. Section-B methods actually tried, transparently reused because P0457 has exhausted all thirty methods: #22 READ THE FAILURES, NOT THE SUCCESSES; #27 SWAP THE QUANTIFIERS; #30 DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME.**

# NM13-04 / P0457 — stuck recovery 2: the source theorem has one independent PASS; the remaining blocker is second-auditor provenance

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-04/`  
Category: `CLOSABLE OUTSIDE`  
Canonical source/claim: `P0457`, `operations/claims/P0457.md`  
Status after this invocation: **PROVED-CANDIDATE / 1-of-2 INDEPENDENT AUDITS PASSED / NOT CLOSED**  
Frozen metric: **`S_exact = UNBOUNDED`**  
Unchanged-run counter: **3 -> 4** since the last metric movement  
Stuck recoveries used: **1 -> 2**  
Required independent audits: **P26 = PASS; NM13-05 = NOT PASSED**

## 1. Runtime and control-plane disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The task-control surface exposed to this worker still offers prompt/title, schedule/start controls, timing mode, enabled state, and task identifiers, but no bindable model-family selector and no bindable reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt text only. Making it enforceable would require an owner-authorized product/workspace/API/admin surface exposing persistent model/reasoning fields together with authenticated per-run runtime attestation.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary, not an ownership release. Current repository policy records that a later P26 update succeeded from another authorized context. The lawful workaround for a future denial is the owning/otherwise-authorized context or platform/admin support, never task duplication or access-control bypass. No scheduler was modified in this invocation.

## 2. Authoritative continuity and required repository read

This is the mandatory Section-I thinking-only run triggered by the newest P0457 report reaching three consecutive frozen-metric-unchanged invocations after `S_exact` saturated at `UNBOUNDED`. I therefore do **not** add a lemma, theorem, checker, paper package, finite certificate, or replacement metric.

I continued the already admitted P0457 target. Intake was not reopened and no second claim was created.

Canonical identity remains:

- campaign ID: `P0457`;
- canonical dedup key: `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA-256: `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- residue: `3 mod 13`, matching NM13-04's exclusive shard;
- exclusive owner: NM13-04;
- source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`;
- exact source question: characterize the diameter of `LK(n,k)` in the additional range from Theorem 6 where connectivity holds.

Before this diagnosis I reread or exact-target-recovered the current controlling state required by the owner from `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; canonical claim `operations/claims/P0457.md`; exact P0457 ID/dedup/source history; newest own report `2026-09-18T09-18-34Z__p0457-surplus-window-first-audit-pass.md`; the prior Section-I report `2026-09-18T03-22-30Z__p0457-stuck-recovery-1.md`; newest neighboring NM13-03 report `2026-09-18T10-10-13Z__admission-delta-screen-14.md`; newest neighboring NM13-05 report `2026-09-18T09-23-00Z__c0146-m8-bernstein-transport.md`; and the current P26 P0457 audit report.

NM13-03 remains admission-pending and creates no P0457 ownership or audit change. NM13-05 is actively continuing its own C0146 source and its newest report is not a P0457 audit. Exact P0457/NM13-05 searches recover no second-auditor PASS.

The current P26 report records exactly one independent PASS:

`P26-AUDIT-NM13-04-P0457-LOGBAND-DIAMETER-42 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_NEAR_LOG_SCOPE_PASS / STRONGER_POSITIVE_SURPLUS_REDERIVATION_PASS / ANALYTIC_NO_ESSENTIAL_FINITE_CORE / PRIOR_ART_UNVERIFIED / PENDING_SECOND_DISTINCT_AUDIT`.

It separately records

`P26-RECONCILE-NM13-04-P0457-2OF2-42 = PENDING_NM13-05_DISTINCT_AUDIT`.

P26 is one auditor. Same-track alternative proofs and self-checks do not count as a second auditor.

Large aggregate files and directory listings can be connector-truncated. Exact claim paths, immutable report paths, exact IDs/dedup keys, and current targeted searches are the continuity anchors; missing or truncated material is not treated as empty.

## 3. Fresh source and literature boundary — 2026-09-18

I rechecked the current Cambridge HTML source rather than relying on intake prose. It still states Theorem 6 in the connected regime

`k >= log n + t' sqrt(log n) log log n`, with fixed `t' > 1/2`,

and its Open Problems discussion still says that another open problem is to characterize the diameter in the additional range of `k(n)` from Theorem 6 where connectivity holds.

Primary source HTML:

`https://www.cambridge.org/core/journals/journal-of-applied-probability/article/connectivity-of-a-family-of-bilateral-preference-random-graphs/0A1D5D7560AB2DC6C8255F1522DC3BB2`

The same source identifies La and Kabkab (2015), *A New Random Graph Model with Self-Optimizing Nodes: Connectivity and Diameter*, *Internet Mathematics* 11, 528–554, as the predecessor.

Fresh bounded queries on 2026-09-18 used the exact 2026 title, DOI, `LK(n,k) diameter`, the author pair plus `bilateral preference diameter`, and the phrase `bilateral preference random graphs diameter`. They recovered the current source, the predecessor/reference chain, and bibliographic mirrors, but no later primary source explicitly resolving this same near-threshold diameter question. This is **bounded negative evidence only**, not proof of worldwide openness and not a publication-novelty certificate.

## 4. Frozen metric and why this is a stuck run

The canonical metric remains

`S_exact = largest co-degree s >= 0 for which NM13-04 has a complete deterministic diameter classification for LK(n,n-1-s), uniformly over the stated feasible n.`

The all-co-degree theorem and its disconnected-case correction already saturated this metric:

- before this run: `S_exact = UNBOUNDED`;
- after this run: `S_exact = UNBOUNDED`;
- mathematical movement: **none**;
- consecutive unchanged invocations after saturation: **3 -> 4**;
- stuck-recovery episodes: **1 -> 2**;
- CLOSABLE rotation gate: **6 unchanged runs**, not yet reached.

The source-level theorem has progressed farther than the frozen special-regime scalar. I will not rename the metric, count audit status as metric movement, or manufacture another finite co-degree certificate after saturation.

## 5. Section-I blocker — the exact statement awaiting second independent certification

The exact source-scoped statement whose closure still awaits the second distinct auditor is:

\[
\boxed{\text{For every fixed }t_0>\tfrac12,\ T>1,\ \text{and every integer sequence }k=k(n)\text{ with}\quad
\log n+t_0\sqrt{\log n}\log\log n\le k\le T\log n,\quad
\frac{\operatorname{diam}LK(n,k)}{\log n/\log\log n}\xrightarrow{\mathbb P}1.}
\]

This is no longer blocked by absence of an owner proof: NM13-04 has a full argument on the page. It is also no longer blocked by absence of any outside proof: P26 independently rederived it and passed the source scope. The remaining closure blocker is **independent provenance from a second OTHER track**, specifically the designated NM13-05 audit, together with the already-recorded prior-art caveat. That is a protocol-critical obstruction, not a missing lemma.

## 6. Method #22 — READ THE FAILURES, NOT THE SUCCESSES

Because all thirty Section-B moves have already been genuinely attempted on P0457, this recovery transparently reuses #22 rather than pretending fresh inventory exists. I read the failed routes as a map of what the theorem had to survive.

### Route A: deterministic co-degree classification

The `s=1,2,3,4` classifiers and the all-`s` complement-degeneracy theorem succeeded on their own axis. Their limitation is exact: in the source regime `k=Theta(log n)`, the co-degree `s=n-1-k` is order `n`, while the deterministic worst-case bound is order `n`; it cannot yield the random `log n/log log n` diameter law. The metric is now saturated, so another deterministic extension is impossible as metric movement.

### Route B: global threshold sandwich

The threshold sandwich `G_+ subset LK subset G_-` identifies the right branching scale. It fails as a complete diameter proof near the new source edge because the lower threshold graph `G_+` is not spanning-connected there. A disconnected lower comparison cannot directly upper-bound every source-pair distance.

### Route C: bulk/typical-pair distance

The bulk argument recovered the correct `log n/log log n` scale for typical pairs. It fails the source's maximum-distance quantifier: exceptional vertices, negligible for a random pair, are exactly what can control graph diameter.

### Route D: leave-one-out block-core attachment

This route repairs the maximum-distance failure by deleting endpoint blocks, exposing a large threshold core independently, and attaching every endpoint with a summable failure probability. It succeeds mathematically and yields the source theorem, but as an NM13-04 proof it is not an independent outside audit.

### Route E: two-round capacity proof

The first stuck recovery ported the sparse-ER/core idea into a genuinely different internal two-round capacity/unsafe-edge proof of the same uniform attachment mechanism. It succeeds mathematically and materially reduces same-track proof risk, but same-track independence is still not a second auditor.

### Route F: adversarial all-`s` self-audit

The exact `n=4,s=2,k=1` disconnected witness exposed an overbroad auxiliary shell clause, which was corrected componentwise. This was a valuable self-correction but it does not attack the near-logarithmic source theorem.

### Route G: closure-critical review and P26 audit

The owner closure review isolated the actual source theorem and P26 independently reconstructed it. This route succeeds and changes the audit gate from `0/2` to `1/2`, but audit movement is not movement of the frozen mathematical metric.

### Route H: stronger positive-surplus theorem

The newest NM13-04 report pushes below the original source surplus, proving the same first-order diameter law under

`s_n=k-log n>0`, `k<=T log n`, and `s_n^2/(k log k)->infinity`.

That is genuine strengthening, but it is not needed to answer the source's stated Theorem-6 range, it is not the frozen metric, and it has not received the second distinct audit. Chasing it farther would be expansion of scope rather than closure work.

**Outcome of #22:** the research failure is no longer mathematical ignorance of the source band. The only source-closure failure left is missing second-track certification. More owner lemmas would not repair that provenance defect.

## 7. Method #27 — SWAP THE QUANTIFIERS

The tempting but wrong operational quantifier is:

> for every still-smaller surplus scale, find another theorem before closure.

The source and closure protocol require something different:

> there exists a second OTHER track that independently verifies the already source-covering theorem for every source-valid sequence `k(n)` in the stated band.

P26 has already checked the universal sequence quantifier in the theorem and even stress-tested a stronger fixed-positive surplus. Therefore proving one more stronger NM13-04 theorem cannot substitute for the existential auditor quantifier.

A second useful swap concerns the exact audit unit. To falsify the source theorem it would suffice to find **one** fixed admissible choice such as

`k(n)=ceil(log n + sqrt(log n) log log n)`

for which the normalized diameter fails to converge to one. Conversely, a second auditor that can independently verify this boundary sequence has checked the most delicate scale before extending the same estimates uniformly through the rest of the Theorem-6 band.

I do **not** call that boundary sequence mathematically unproved: it is covered by the owner theorem and P26 PASS. It is simply the smallest useful independent-verification unit for the missing second audit.

**Outcome of #27:** the correct next object is not a new stronger source claim. It is a second-track rederivation beginning at the lower source boundary and then checking the universal sequence quantifier.

## 8. Method #30 — LOCALIZE ONE SCALE AT A TIME

I localized the remaining verification burden to the lower source scale

`k_*(n)=ceil(log n + sqrt(log n) log log n)`,

which corresponds to the clean fixed choice `t_0=1`.

At this scale every earlier obstruction is maximally visible while remaining strictly within the source's connected range:

1. the definite lower threshold graph can still be disconnected, so the old La--Kabkab spanning-subgraph route is unavailable;
2. the block/core deletion loss is of the same order as the positive surplus and must be budgeted explicitly;
3. a per-endpoint failure probability merely of order `1/n` is insufficient; the proof needs a strict positive surplus in the exponent to union over all endpoints/cores;
4. typical-pair control remains insufficient; the audit must verify uniform attachment of every endpoint to a common large core.

P26 has already independently checked those mechanisms, so this localization creates **no new claim**. Its purpose is to define the smallest clean target for NM13-05's eventual audit and to prevent a second auditor from spending effort on the stronger surplus theorem before certifying the source boundary.

**Outcome of #30:** the second audit should start at `t_0=1`, verify the attachment exponent and diameter squeeze there, then generalize to arbitrary fixed `t_0>1/2`; the stronger `s_n^2/(k log k)->infinity` theorem is optional and should not delay source closure.

## 9. What a closure proof stack must contain that the current repository still lacks

The mathematical ingredients themselves now exist in both the owner proof and the P26 rederivation. What the **closure stack** still lacks is one artifact with independent provenance from NM13-05 (or another owner-authorized distinct track) that verifies, without treating NM13-04 or P26 conclusions as axioms:

1. the exact bilateral-preference source model and Theorem-6 quantifiers;
2. the threshold sandwich and the correct sparse-ER diameter input;
3. the fact that lower-threshold disconnection is harmless only after constructing a near-spanning deleted core;
4. a summable **uniform** endpoint-to-core attachment estimate, including all block/endpoint union bounds;
5. the squeeze from the core diameter and the upper threshold graph to the full `LK` diameter;
6. the dated prior-art boundary and the distinction between standard/folklore ingredients and any new mechanism.

No amount of same-track self-checking supplies item 0: **a second independent OTHER-track provenance chain**. That is the exact thing no owner route can create by itself.

## 10. Simplest special case still unproved / uncertified

There is no honest source-range special case that remains mathematically unproved by NM13-04 after the source theorem, and P26 has independently passed the full source scope. Calling one such case “unproved” would erase existing evidence.

The simplest **still uncertified by the required second auditor** unit is instead

\[
k(n)=\left\lceil\log n+\sqrt{\log n}\log\log n\right\rceil,
\qquad
\frac{\operatorname{diam}LK(n,k(n))}{\log n/\log\log n}\xrightarrow{\mathbb P}1.
\]

The nearest genuinely unproved mathematical extension visible from the newest strengthening is the fixed-critical scale `s_n^2/(k log k)=Theta(1)`, rather than a ratio tending to infinity. That extension lies below the source's currently guaranteed connected band and is **not selected as this CLOSABLE source's next obligation**.

## 11. Nearest solved problem and the ingredient it has that this source range lacks

The nearest solved same-model problem remains La--Kabkab (2015) in the stronger logarithmic regime. Their diameter method has a spanning connected Erdős--Rényi comparison available at sufficiently large constant multiple of `log n`.

The new Dabirian--Subramanian Theorem-6 range lacks that spanning connected lower comparison. Near the lower source edge, the natural definite-edge threshold graph may be disconnected even though `LK(n,k)` is connected. The NM13-04/P26 proof architecture replaces the missing ingredient by a near-spanning threshold core plus an independent uniform attachment layer for every exceptional endpoint.

That is precisely the conceptual point a second auditor must rederive rather than merely quote.

## 12. Exactly one Section-I recovery choice

**Chosen recovery: PROVE THE SIMPLEST UNPROVED SPECIAL CASE FROM (d), interpreted without falsifying history as independently re-proving the smallest still-uncertified verification unit.**

Concretely, if the next invocation still has no NM13-05 PASS or mathematical defect and the six-unchanged rotation gate has not yet been reached, the only justified proof-oriented action is an audit-grade, isolated rederivation of the single boundary sequence

`k(n)=ceil(log n + sqrt(log n) log log n)`

using the source model from first principles, explicitly checking the core/attachment exponent and not importing NM13-04 or P26 conclusions as black boxes. Because NM13-04 cannot manufacture a second auditor by writing another owner proof, this choice is primarily a specification for the distinct audit partner; NM13-04 itself must not count any same-track repetition as closure.

If an actual NM13-05 PASS appears first, the audit gate changes and the next state is closure packaging, not another theorem. If an audit finds a mathematical defect, repair exactly that defect. If neither occurs and `S_exact` remains unchanged through six consecutive runs, preserve the full P0457 handoff and rotate as required for CLOSABLE targets.

No move to a new source is authorized in this invocation because the six-unchanged rotation gate has not yet been reached.

## 13. Audit state and next legal state

Current audit state:

- `P26 = PASS` for the frozen source theorem;
- `NM13-05 = NOT PASSED` for P0457;
- same-track alternate proofs = self/owner evidence only;
- stronger surplus-window theorem = not automatically covered by the source-level closure claim and should not delay source closure.

The next invocation must first recover whether NM13-05 (or another owner-authorized distinct auditor) has actually produced a P0457 PASS, whether P26 has issued a correction, or whether current literature has materially changed the source status. In the absence of those changes, do not manufacture another finite certificate for the saturated `S_exact` metric.

## 14. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  status: PROVED_CANDIDATE_1_OF_2_AUDITS_NOT_CLOSED
  source_id: P0457
  claim_id: P0457
  canonical_dedup_key: diameter_near_the_newly_established_bilateral_connectivity_threshold
  source_target: >-
    Characterize diameter of exact bilateral-preference LK(n,k) in the
    additional Theorem-6 connectivity range of Dabirian--Subramanian.
  metric:
    name: S_exact
    before: UNBOUNDED
    after: UNBOUNDED
    normalization_changed: false
  mathematical_movement: false
  section_B_methods:
    attempted: [22, 27, 30]
    method_inventory_exhausted: true
    reuse_disclosed: true
  unchanged_runs_since_last_metric_movement:
    before: 3
    after: 4
  stuck_recovery_count:
    before: 1
    after: 2
  stuck_protocol: SECTION_I_THINKING_ONLY
  source_theorem:
    t0: "> 1/2"
    upper_band: "k <= T log n, fixed T > 1"
    conclusion: "diam(LK(n,k))/(log n/log log n) -> 1 in probability"
  audits:
    P26:
      verdict: PASS
      audit_id: P26-AUDIT-NM13-04-P0457-LOGBAND-DIAMETER-42
    NM13-05:
      verdict: NOT_PASSED
      newest_report: proofnet24/NM13-05/runs/2026-09-18/2026-09-18T09-23-00Z__c0146-m8-bernstein-transport.md
  closure_gate:
    passed_auditors: 1
    required_auditors: 2
    prior_art: BOUNDED_NEGATIVE_SEARCH_ONLY_NOVELTY_UNVERIFIED
    analytic_finite_core: NO_ESSENTIAL_FINITE_CORE_PER_P26
  neighboring_tracks:
    NM13-03: ADMISSION_PENDING
    NM13-05: C0146_ACTIVE_NO_P0457_AUDIT_PASS
  recovery_choice: >-
    PROVE_THE_SIMPLEST_UNPROVED_SPECIAL_CASE, operationalized as a
    distinct-auditor first-principles verification of the t0=1 boundary
    sequence before generalizing to the full source band; same-track
    repetition does not count as the second audit.
  closable_rotation_gate:
    threshold_unchanged_runs: 6
    current_unchanged_runs: 4
    reached: false
  next_step: >-
    First check for an actual NM13-05/distinct P0457 PASS, P26 correction,
    or source-status change. If none exists, preserve the audit-grade t0=1
    verification specification and avoid new saturated-metric certificates.
    At six unchanged runs without closure, hand off P0457 and rotate.
  shared_root_edits: NONE
  peer_edits: NONE
  new_artifacts: NONE
  new_claims: NONE
```

No shared root, canonical claim, peer namespace, finite artifact, paper package, workflow, permission, public surface, email/Drive resource, paid compute, or scheduler was modified. This invocation writes exactly this one immutable report and reads it back at its creation commit.

**End of complete run report.**