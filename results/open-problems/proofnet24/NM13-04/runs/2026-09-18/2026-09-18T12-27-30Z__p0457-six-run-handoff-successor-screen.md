Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `S_exact = UNBOUNDED -> UNBOUNDED`; this is the sixth consecutive unchanged P0457 invocation after saturation, so P0457 is handed off and NM13-04 rotates. No Section-B method is reported as tried on a successor because no successor passed admission; successor baseline remains `UNMEASURED -> UNMEASURED`.**

# NM13-04 / P0457 — mandatory six-run handoff and residue-3 successor admission screen

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-04/`  
Category: **CLOSABLE OUTSIDE**  
Captured pre-write master: `742f9ab21d7e73d8a5dcb5d388b6ec86249b8320`  
Outgoing canonical source / claim: **P0457**, `operations/claims/P0457.md`  
Outgoing frozen metric before / after: **`S_exact = UNBOUNDED -> UNBOUNDED`**  
Outgoing unchanged-run counter: **5 -> 6**  
Outgoing stuck-recovery count: **2 -> 2**  
Outgoing closure state: **PARTIAL / PROVED-CANDIDATE / P26 PASS / distinct second audit missing / NOT CLOSED**  
Successor state after this invocation: **ADMISSION_PENDING**  
Successor metric before / after: **`UNMEASURED -> UNMEASURED`**  
Successor Section-B methods: **none attempted; screening is not mathematical progress**

## 1. Runtime and control-plane disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The scheduler/task-control surface exposed to this worker still provides prompt/title, schedule or start fields, timing mode, enabled state and task identifiers, but no bindable model-family selector and no bindable reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model/effort controls together with authenticated per-run runtime attestation.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary. Repository policy records that another authorized context later succeeded in updating P26. The lawful workaround for a denied modification is the owning/otherwise-authorized context or authorized platform/admin support, never duplication, permission changes or access-control bypass. No schedule was created, edited, disabled or probed in this invocation.

## 2. Authoritative continuity recovered before the rotation decision

I reread or exact-target-recovered the governing/current state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical P0457 claim `operations/claims/P0457.md`;
- newest own report `proofnet24/NM13-04/runs/2026-09-18/2026-09-18T11-18-00Z__p0457-audit-gate-hold-5.md`;
- newest visible neighboring NM13-05 report `proofnet24/NM13-05/runs/2026-09-18/2026-09-18T12-02-00Z__c0146-positive-q-refutation.md`;
- current P26 P0457 audit/reconciliation searches, including `P26-AUDIT-NM13-04-P0457-LOGBAND-DIAMETER-42` and `P26-RECONCILE-NM13-04-P0457-2OF2-42`;
- current explicit release search across canonical claim files;
- the current E-intake rows `E0001`--`E0010` from `probability_1000_intake_E_20260908/problems.jsonl`;
- current residue-3 ownership evidence for the P0014/RS-2025-TH18 alias and the released H0021 claim.

Large append-only JSONL files and broad code-search responses can be connector-truncated. I therefore do not claim every repository byte was serially rendered in this invocation. Exact canonical claim files, current source rows, immutable run paths, direct directory reads and exact-ID/dedup searches are used as continuity anchors. Missing/truncated text is never treated as a release or as proof of no prior work.

## 3. Why P0457 must rotate now

The preceding immutable P0457 report recorded:

- `S_exact = UNBOUNDED -> UNBOUNDED`;
- fifth consecutive unchanged run after saturation;
- stuck recoveries already exhausted at `2`;
- P26 audit PASS;
- NM13-05 distinct second audit not passed;
- explicit instruction that absent an audit/source correction, the next invocation is the sixth unchanged CLOSABLE run and must preserve a handoff and rotate rather than produce a seventh unchanged P0457 research run.

No intervening source-level mathematical change was recovered. The newest NM13-05 report is substantive C0146 work, not a P0457 audit. Current P26 reconciliation still records

`P26-RECONCILE-NM13-04-P0457-2OF2-42 = PENDING_NM13-05_DISTINCT_AUDIT`.

Therefore the owner rule is now binding: **P0457 reaches six consecutive unchanged runs and NM13-04 rotates.** I do not evade the rule by renaming the metric, filing another stress lemma, manufacturing a checker, or calling an audit/literature update mathematical movement.

The canonical P0457 claim file is not edited by this worker. This handoff is not itself a repository-wide ownership release, and another worker must not infer free ownership merely from this report. Any future reassignment must reconcile the canonical claim and start from the handoff state below rather than restart the source.

## 4. Complete P0457 handoff state

### 4.1 Canonical identity and source

- campaign ID: `P0457`;
- canonical dedup key: `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA-256: `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- selection shard: `3 mod 13`;
- source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (2026), 552--579, DOI `10.1017/jpr.2025.10051`;
- exact source question: characterize the diameter of the bilateral-preference graph `LK(n,k)` in the additional near-logarithmic range covered by the paper's Theorem 6 where connectivity holds.

The exact model uses one iid continuous edge-score family on `K_n`; `{u,v}` is retained iff it is among the `k` preferred incident edges at both endpoints. Independent-edge or geometric mutual-neighbor surrogates are not the source model.

### 4.2 Frozen metric and terminal value

`S_exact` is the largest co-degree `s >= 0` for which the track has a complete deterministic diameter classification for exact source graphs `LK(n,n-1-s)` in the stated all-`n` scope.

Admission baseline was `S_exact=0`, because `LK(n,n-1)=K_n`. The sequence of structural work moved the metric through finite co-degrees and ultimately saturated it at

`S_exact = UNBOUNDED`.

That saturation does not by itself answer the near-logarithmic source question; the later source-scope theorem below does.

### 4.3 Source-scope theorem candidate

The source-matching theorem on the page is:

\[
\boxed{\text{For every fixed }t_0>\tfrac12,\ T>1,\text{ uniformly for integer sequences }
\log n+t_0\sqrt{\log n}\log\log n\le k\le T\log n,\quad
\frac{\operatorname{diam}LK(n,k)}{\log n/\log\log n}\xrightarrow{\mathbb P}1.}
\]

The owner proof is written in the P0457 report chain. Its successful route is a leave-one-out/block-deleted core construction: build a source-valid core measurable without target endpoint edges, prove the core has the required small-diameter expansion, and then attach every endpoint with an explicit union-bound surplus that remains positive throughout the source's fixed `t_0>1/2` range. The lower bound is the source-model degree/Moore-volume side; the upper bound is the new dependent-edge core/attachment argument.

The latest boundary stress re-expansion checked the weakest fixed source surplus and still obtained

`p0 |A| >= log n + (5 t0/8 - o(1)) sqrt(log n) log log n`,

with the complementary top-`k` miss term superpolynomially smaller. The same-block/two-block asymmetry was also checked: deleting both endpoint blocks is quantitatively worst, while deleting one common block only enlarges the core and preserves the required leave-one-out measurability.

### 4.4 Earlier exact finite/high-degree work to preserve

The first substantive run at `k=n-2` identified a functional-digraph representation of the missing-edge graph. Directed cycles of length at least three are impossible by strict edge-weight inequalities, so the missing graph is a forest. This yields a complete diameter classification: disconnected iff the missing graph is a spanning star; connected diameter three iff the missing graph is a spanning non-star double-star; otherwise diameter two. The same run derived the exact disconnection probability

`P(LK(n,n-2) disconnected) = 2^(n-1) n! / (2n-2)!`.

Subsequent exact high-degree work explored and classified further co-degree regimes before the all-co-degree theorem saturated `S_exact`. Those results remain restricted structural results even though the later near-log theorem is source-scoped.

### 4.5 Audit state

P26 independently rederived the near-log theorem and issued

`P26-AUDIT-NM13-04-P0457-LOGBAND-DIAMETER-42 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_NEAR_LOG_SCOPE_PASS / STRONGER_POSITIVE_SURPLUS_REDERIVATION_PASS / ANALYTIC_NO_ESSENTIAL_FINITE_CORE / PRIOR_ART_UNVERIFIED / PENDING_SECOND_DISTINCT_AUDIT`.

Current reconciliation remains

`P26-RECONCILE-NM13-04-P0457-2OF2-42 = PENDING_NM13-05_DISTINCT_AUDIT`.

Thus P0457 has **one of the two required independent audits**. Same-track alternate derivations, self-checks and repeated P26 reads do not count as the missing second auditor. NM13-05 is the designated second audit partner but has not passed P0457 as of this handoff.

The theorem is analytic and has no essential finite computational core, so no checker is manufactured merely to satisfy a bookkeeping pattern. No paper folder is created because closure prerequisites are not complete.

### 4.6 Prior-art / current-source boundary

Fresh bounded checks on 2026-09-18 used the exact source title, author pair, `LK(n,k) diameter`, and `bilateral preference random graph diameter`. The current Cambridge full text still states on journal page 554 that a further open problem is to characterize the diameter in the additional Theorem-6 range where connectivity holds. The search recovered the 2026 source and its earlier preprint/bibliographic forms but no later primary paper explicitly resolving this exact question.

This is bounded negative evidence only. Worldwide openness and publication novelty remain **UNVERIFIED**. A future closure package must preserve this caveat and should repeat the prior-art/citation search before any posting decision.

### 4.7 Method history and why no method is spent here

All thirty Section-B methods have already been used on P0457 across the report chain. Two full Section-I stuck-recovery episodes were also used. The fifth unchanged run then performed a final source-boundary/adversarial stress test. This sixth run is the owner-mandated handoff/rotation run, not permission for a third recovery or another reused triple.

Accordingly **no Section-B method is reported as tried on P0457 in this invocation**, and no successor method is spent before successor admission. This is deliberate compliance, not missing research bookkeeping.

### 4.8 If P0457 is ever reassigned

Do not restart the old high-degree classifications or redo the same leave-one-out proof. First reconcile the canonical claim and all later audits. If a distinct second audit has passed, the next work is closure/prior-art packaging, not another theorem. If a second audit finds a defect, repair exactly that defect. If the audit remains absent and the source is owner-authorized for reassignment, use a genuinely new route rather than a seventh NM13-04-style unchanged pass.

## 5. Successor admission screen after rotation

The successor must satisfy the worker's original shard rule

`int(SHA256(UTF-8 canonical_dedup_key).hexdigest(),16) mod 13 = 3`

and must be an honestly CLOSABLE OUTSIDE source. A pending lead is not READY; a historical handoff does not automatically release ownership.

### 5.1 P0014 / RS-2025-TH18 — correct shard, but already owned

The historical campaign alias `P0014` is the random-circulant Lovasz-theta source. Previous NM13-04 admission work already recovered that it has the correct residue-3 shard, but the canonical current target is `RS-2025-TH18` under an existing exclusive claim `operations/claims/RS-2025-TH18.md`. Current repository search still recovers that ownership chain. It is therefore **ineligible**; no alias is used to create duplicate ownership.

### 5.2 H0021 — canonical residue 3 and explicitly released, but HARD/exhausted, not a CLOSABLE successor

Current canonical claim history `operations/claims/H0021.md` says `Owner: UNASSIGNED AFTER R16 HANDOFF` and identifies the exact source as Cohen Antonir--Lichev--Zhukovskii, arXiv:2608.06358v1, Conjecture 1.4 on the sharp threshold for bounded-degree tree universality.

Its recovered canonical identity is

`arxiv_2608_06358::Conjecture 1.4 (Sharp threshold for tree universality); Section 1.6, "Further challenges"`,

whose SHA-256 is

`5eb8894c6c85250561d00c39076bfe48a685892ea6abedc719f36bacaf537fcd`,

with residue `3 mod 13`.

However, the claim explicitly records two exhausted HARD stuck recoveries, a six-run handoff, frozen metric `Delta_near=2`, and the requirement that any future reassignment use a genuinely fresh route. It is an asymptotic HARD source, not a finite/short CLOSABLE endpoint. The present prompt also forbids reopening exhausted sources. **H0021 is rejected.**

### 5.3 Fresh literal-key E-intake shard advance: E0001--E0010

To avoid hashing titles or aliases, I read the current literal `dedup_key` field for the first ten E-intake rows and evaluated the required SHA-256 residue exactly:

| ID | canonical dedup key | SHA-256 residue mod 13 |
|---|---|---:|
| E0001 | `kesten_percolation_highlights_2002::open_problem_1` | 12 |
| E0002 | `kesten_percolation_highlights_2002::open_problem_2` | 0 |
| E0003 | `kesten_percolation_highlights_2002::open_problem_3` | 4 |
| E0004 | `kesten_percolation_highlights_2002::open_problem_4` | 6 |
| E0005 | `kesten_percolation_highlights_2002::open_problem_5` | 1 |
| E0006 | `kesten_percolation_highlights_2002::open_problem_6` | 8 |
| E0007 | `durrett_coexistence_2009::problem_1` | 7 |
| E0008 | `durrett_coexistence_2009::problem_2` | 6 |
| E0009 | `durrett_coexistence_2009::problem_3` | 1 |
| E0010 | `durrett_coexistence_2009::problem_4` | 5 |

None lies in residue 3, so none is eligible for NM13-04 regardless of subject fit or literature status. These rows are now behind the successor screening cursor and should not be rerun absent a canonical-identity correction.

### 5.4 Current explicit release gate

A fresh exact repository search for canonical claims carrying `UNASSIGNED AFTER ... HANDOFF` still finds H0021 as the relevant explicit release. No second non-exhausted residue-3 CLOSABLE release was recovered in this bounded screen. Queue entries with stale `PENDING` or old `admitted=true` metadata are not promoted merely to fill the slot.

## 6. Successor admission verdict and durable cursor

**ADMISSION_PENDING.** No successor passed all gates in this invocation, so:

- no new `operations/claims/<ID>.md` is created;
- no source-specific successor metric is invented;
- successor baseline remains `UNMEASURED -> UNMEASURED`;
- no Section-B method is counted as attempted on a successor;
- screening does not increment a successor mathematical unchanged-run counter;
- P26 / NM13-05 audit requirements are not applicable to a not-yet-admitted successor.

Durable successor cursor:

1. continue the literal-key E-intake scan at **E0011**, hashing canonical `dedup_key` values before any subject/literature work;
2. then continue through later F/G/H intake rows not already shard-tested by NM13-04;
3. for I-series rows lacking an explicit `dedup_key`, recover the stable canonical source identity plus exact locator before hashing; never hash the short ID/title;
4. retain P0014/RS-2025-TH18 as ownership-blocked and H0021 as HARD/exhausted/ineligible unless a later owner-authorized status correction materially changes those facts;
5. at the first residue-3 candidate, run the full gate in order: exact source -> POSTED/campaign exclusion -> current/historical claims/handoffs/attempts -> current primary/later-author/citing literature -> honest CLOSABLE classification -> create-only canonical claim and readback;
6. after a successful claim, freeze the exact source graph class and source-relevant counterexample-size/cutoff metric and immediately continue into substantive research in that same invocation.

## 7. Runtime/source-access limits

The private repository was accessible for the required current files and writes in this invocation. Large aggregate JSONL/code-search responses are bounded/truncated by the connector, so the successor screen advances with an explicit cursor rather than pretending exhaustive coverage. Public literature search was bounded to currently retrievable web/arXiv/journal surfaces and is not a guarantee of worldwide novelty.

## 8. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  run_status: ROTATED_HANDOFF_SUCCESSOR_ADMISSION_PENDING
  outgoing_source_id: P0457
  outgoing_claim_id: operations/claims/P0457.md
  outgoing_canonical_dedup_key: diameter_near_the_newly_established_bilateral_connectivity_threshold
  outgoing_shard_residue: 3
  outgoing_metric:
    name: S_exact
    before: UNBOUNDED
    after: UNBOUNDED
  outgoing_mathematical_movement: false
  outgoing_unchanged_run_count:
    before: 5
    after: 6
  outgoing_stuck_recoveries:
    before: 2
    after: 2
  outgoing_status: PARTIAL_PROVED_CANDIDATE_HANDOFF
  outgoing_audits:
    P26: PASS
    NM13-05: NOT_PASSED
  outgoing_closure: NOT_CLOSED
  rotation_trigger: SIX_CONSECUTIVE_UNCHANGED_CLOSABLE_RUNS
  successor_source_id: null
  successor_claim_id: null
  successor_metric:
    name: admission_baseline
    before: UNMEASURED
    after: UNMEASURED
  successor_mathematical_progress: false
  successor_methods_attempted: []
  successor_initial_methods_preserved: [2, 14, 19]
  successor_unchanged_research_run_count: 0
  successor_stuck_recoveries: 0
  successor_screen:
    ownership_blocked: [P0014/RS-2025-TH18]
    hard_or_exhausted_rejected: [H0021]
    literal_key_rows_shard_tested_this_run: [E0001, E0002, E0003, E0004, E0005, E0006, E0007, E0008, E0009, E0010]
    next_cursor: E0011
  next_state: CONTINUE_RESIDUE3_SUCCESSOR_ADMISSION
```

**End of complete immutable run report.**