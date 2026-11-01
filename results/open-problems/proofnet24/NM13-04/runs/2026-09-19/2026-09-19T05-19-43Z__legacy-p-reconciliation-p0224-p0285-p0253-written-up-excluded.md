Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT. Section-B methods #2/#14/#19 were NOT_TRIED because no successor passed admission.

# NM13-04 legacy P-series reconciliation: P0224–P0285

Date: 2026-09-19 UTC
Track: NM13-04
Category: CLOSABLE OUTSIDE
Namespace: `proofnet24/NM13-04/`
Selection shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 3`
Status: `ADMISSION_PENDING`
Successor source: `NONE`
Canonical claim: `NONE`
Metric: successor certified counterexample-size bound or exhaustive finite-case cutoff, exact source scope
Metric before: `UNMEASURED`
Metric after: `UNMEASURED`
Mathematical movement: `NONE`

## Continuity and controlling state

This run continues from the immutable NM13-04 report

`proofnet24/NM13-04/runs/2026-09-19/2026-09-19T04-44-30Z__legacy-p-reconciliation-p0162-p0223-no-closable-residue3.md`

whose durable cursor was `LEGACY_P_RECONCILIATION_NEXT=P0224`.

Preserved terminal predecessor: P0457 remains exhausted/retired for NM13-04 after six unchanged CLOSABLE runs and two stuck-recovery episodes. It was not reopened and its metric was not inherited by a successor.

Before admission work I reread/recovered the required current repository state: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the newest NM13-04 report; newest visible neighboring NM13-03 and NM13-05 reports; the Codex/intake problem ledgers, dedup index, attempt/rank-sheet evidence, and current claim/search evidence. Historical missing or inaccessible external task state was not treated as a release.

The deployment amendment fixes this worker at residue 3, CLOSABLE OUTSIDE, initial research methods #2/#14/#19, with NM13-05 as the proposed second audit partner after P26. A proposed partner is not an audit pass.

## Frozen repository delta before this write

Previous NM13-04 creation commit: `2a3548f751626f0f775db116818ce7bf149fdb79`.
Frozen pre-write master: `80a26846988357e9b006e93ae27d1acabd5bbdfd`.
Exact comparison: `59 commits ahead, 0 behind`.

The changed-file set contained one new canonical claim, `operations/claims/VANBERKEL-BOSMA-2026-TS12.md`, plus worker reports/artifacts and task-health receipts. It contained no deletion of a canonical claim, no owner-authorized release, and no change to `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, intake `problems.jsonl`, or an attempt ledger that creates free residue-3 CLOSABLE inventory. Several tracks recorded terminal handoffs, including C0117; a handoff without a canonical release does not make that source unowned for NM13-04.

No concurrency event in this frozen delta authorizes taking another track's source.

## Repair work: canonical P0224–P0285 reconciliation

The previous run discovered that a delta-only sentinel was unsafe because legacy P-series rows could be admissible even without appearing in a new repository delta. This run therefore continued the full canonical reconciliation rather than reverting to delta-only screening.

I reconciled the 62 consecutive legacy P IDs P0224 through P0285 from the Codex/intake source, using each row's canonical `dedup_key` before hashing. Resolved/excluded rows stayed excluded rather than being revived by an old `admitted=true` flag. Canonical hashes were computed exactly as specified by the owner. Exactly five identities in this interval have residue 3:

| ID | canonical dedup key | SHA-256 | residue | admission disposition |
|---|---|---|---:|---|
| P0228 | `uniqueness_of_the_unbounded_major-road_component` | `4da2a6b126b3e60f6ca14c55d876775890701cd6d170588ed75a73850aaed878` | 3 | REJECT: SIRSN infinite/spatial structural question; not an honest finite-certificate CLOSABLE target |
| P0231 | `a_zero-one_law_for_poisson-coloring_frontier_dimension` | `aa5a650a6de0c088de57db467b08407d80e2d243053bec3edd15fb49921fc193` | 3 | REJECT: continuum/Poisson frontier Hausdorff-dimension law; not a finite graph/counterexample target |
| P0253 | `maximal_stationary_antivoter_variance` | `7247a203aa0e0e6592f851fea2e4062ea48f92ea292e143b6e8770385ee23c9f` | 3 | EXCLUDED DUPLICATE: exact source already has a recovered completed manuscript in repository publication reconciliation |
| P0256 | `weak_concentration_of_nearest-unvisited_walks_under_exponential_edge_noise` | `2ee8d3960625260c8c4a69021f23c67a2cc7c001d826738138cc8478a79f3f43` | 3 | REJECT: asymptotic nearest-unvisited-walk concentration problem; not an honest finite CLOSABLE endpoint |
| P0285 | `finitary_ordering_permutation_of_a_kpz_line_ensemble_vertical_slice` | `4f0250a3e2bb12833efc5892fb7b23679f3b616a1be5c88177fb9f790e7f0a97` | 3 | REJECT: KPZ line-ensemble finitary ordering/displacement problem; asymptotic/continuum HARD rather than finite CLOSABLE |

The four non-P0253 rows fail the worker's CLOSABLE admission class before any temptation to invent a smaller surrogate. I did not relabel an asymptotic or continuum problem as a finite target.

## P0253 is the graph-shaped near-hit, but it is already written up

P0253 is precisely the sort of graph extremal source this worker was intended to prefer: Aldous–Fill, Section 14.4, the unnumbered open problem immediately before Corollary 14.24 asks whether the stationary variance of the antivoter spin sum is maximized by the complete graph. The source computes the complete-graph value

`Var(S) = n(n-2)/(2n-3)`.

The maintained source page still prints the open problem verbatim. It also records the antivoter dynamics, the dual random-walk representation, and the complete-graph value. Source checked on 2026-09-19 at:

`https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch14.S4.html`

However, current repository exclusion evidence is decisive. `POSTED.md` points to the 18 September missing-manuscript assessment, and `publications/researchgate/NOT_IN_SNAPSHOT_2026-09-18.md` records a recovered manuscript titled **Complete-Graph Extremality for Stationary Antivoter Variance**. That row states the exact outside question and records the theorem

`Var(S) <= n(n-2)/(2n-3)`

for connected simple regular graphs, with equality precisely for the complete graph, covering every stationary law. The saved manuscript is `antivoter_variance.pdf` in the owner's Library. The same reconciliation warns that its metadata is not a fresh audit or novelty certificate; nevertheless, it is already a substantive written-up answer to the exact source. Fleet rules prohibit reopening written-up/settled sources under a new worker merely because no canonical `operations/claims/P0253.md` exists.

I explicitly checked for `operations/claims/P0253.md`; it is absent. That absence does **not** create ownership because the publication/manuscript exclusion is stronger evidence against duplicate research. I therefore did not create a claim and did not re-run the manuscript's mathematics.

## Bounded literature check for P0253

Date: 2026-09-19.
Queries included:
- `Aldous Fill antivoter variance complete graph open problem 14.24`
- `"maximal stationary antivoter variance" complete graph`
- `"antivoter model" "variance" "complete graph" regular graph`
- `"anti-voter" stationary variance complete graph`

Public search recovered the maintained Aldous–Fill source page and related antivoter/Stein-method literature, including work on the complete-graph anti-voter model and recent broad pairwise-interaction concentration work. I did not recover from this bounded search a later public source that I can certify as the worldwide first resolution of the exact regular-graph extremal problem. This negative search is **not** a worldwide-openness or novelty certificate. More importantly for admission, the repository already contains the owner's recovered exact-source manuscript, so NM13-04 must exclude P0253 regardless of public posting status.

## Why methods #2/#14/#19 remain unspent

No candidate passed all admission gates. Therefore there is no frozen successor graph class and no legitimate target metric on which to run:
- #2 ATTACK THE NEGATION FIRST,
- #14 FIND THE GROUP ACTING,
- #19 MAKE IT AN ALGORITHM.

Charging those methods against screening would falsely report mathematical research on a source the worker does not own. They remain reserved for the first admitted successor.

No checker, theorem artifact, paper folder, audit request, or mathematical claim was created this run.

## Scheduler/model control status

The currently exposed task-update interface still provides prompt/title, schedule, timing mode and enabled-state controls, but no bindable model-family selector and no reasoning-effort selector. Thus `GPT-6 / maximum` remains a prompt request only. This run actually reports `GPT-5.6 Sol`; reasoning telemetry is unavailable, so `UNVERIFIED` is the only supported label.

The historical P26 `You cannot modify this task` result is an authorization-context boundary, not a reason to clone or bypass a task. `RESULTS.md` records that P26 was later successfully updated from a different authorized context. A binding GPT-6/max configuration would require the scheduler/platform/API to expose model/reasoning fields in an authorized execution context; prompt text cannot manufacture those controls. No support escalation is claimed or sent by this run.

## Counters and next cursor

Successor unchanged-run counter: `N/A` — no successor admitted, and screening is not mathematical progress.
Successor stuck-recovery counter: `N/A`.
Preserved predecessor P0457 counters: `6 unchanged CLOSABLE runs / 2 stuck recoveries / terminal handoff-retirement preserved`.

Durable screening cursor before: `LEGACY_P_RECONCILIATION_NEXT=P0224`.
Durable screening cursor after: `LEGACY_P_RECONCILIATION_NEXT=P0286`.

Do not restore the old strict-delta-only cursor until the legacy P-series reconciliation is complete. Next invocation begins at P0286, canonicalizes before hashing, checks aliases/claims/history, and stops immediately for substantive work only if a genuinely unassigned residue-3 CLOSABLE source passes all gates.

## Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-04
  category: CLOSABLE_OUTSIDE
  source_id: NONE
  claim_id: NONE
  source_dedup_key: NONE
  status_before: ADMISSION_PENDING
  status_after: ADMISSION_PENDING
  metric_name: successor_certified_counterexample_size_bound_or_exhaustive_finite_case_cutoff
  metric_scope: NOT_FROZEN_NO_ADMITTED_SUCCESSOR
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  movement: NONE
  mathematical_progress: false
  methods:
    - "2: NOT_TRIED — no admitted source"
    - "14: NOT_TRIED — no admitted source"
    - "19: NOT_TRIED — no admitted source"
  screening_cursor_before: LEGACY_P_RECONCILIATION_NEXT=P0224
  screening_cursor_after: LEGACY_P_RECONCILIATION_NEXT=P0286
  screened_interval: P0224-P0285
  residue3_identities: [P0228, P0231, P0253, P0256, P0285]
  strongest_near_hit: P0253
  strongest_near_hit_disposition: EXCLUDED_EXISTING_MANUSCRIPT
  predecessor_terminal_target: P0457
  predecessor_unchanged_runs: 6
  predecessor_stuck_recoveries: 2
  successor_unchanged_runs: N/A
  successor_stuck_recoveries: N/A
  next_step: "continue canonical legacy P reconciliation from P0286; admit only after source/current-literature/prior-attempt/exclusive-ownership gates"
  p26_audit: NOT_REQUESTED
  secondary_audit_partner: NM13-05_NOT_REQUESTED
```

## Access and write scope

All repository reads/writes in this invocation used the authorized GitHub connection on private repository `yspennstate/math-open-problems`, branch `master`. Public literature search was bounded web search, not an exhaustive citation database audit. No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, peer-file edit, shared-root edit, scheduler creation/modification, or unreviewed external script was used.

This report is the invocation's sole repository write.