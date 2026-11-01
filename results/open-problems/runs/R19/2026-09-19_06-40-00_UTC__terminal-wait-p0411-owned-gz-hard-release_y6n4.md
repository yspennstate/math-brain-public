Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. I0084 fixed metric `2/2 → 2/2`; R19 successor gate `E_READY_SUCCESSOR: 0 → 0`; NO MOVEMENT; state `TERMINAL_WAITING_FOR_NEW_READY_DELTA` preserved; methods #1, #16, #18.**

# R19 — terminal wait: one new CLOSABLE claim is already owned; one genuine release is HARD, not a R19 successor

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Worker: R19.
Lane: **CLOSABLE OUTSIDE**.
Frozen source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

## 0. Lifecycle and continuity

I continued from the newest immutable R19 report

`runs/R19/2026-09-19_05-43-21_UTC__terminal-wait-three-closable-claims-owned_x7q2.md`

created at

`2608f296cffbde5ddc2041c6b01d92c1d9a6137e`,

blob

`1e2cb7b0de663fcd893b9afdae7f39824812a515`.

That report had already completed the mandatory post-STUCK2 terminal handoff and froze R19 at `TERMINAL_WAITING_FOR_NEW_READY_DELTA`. I therefore do **not** reopen I0084 theorem work, do **not** restart rotated I0120, and do **not** infer ownership from another worker's handoff.

Before disposition I refreshed the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the operative follow-up implementation manifest, current task-health/coordinator state, the newest R19 report, newest materially relevant admission/claim/handoff reports, the newest P26 audit, and the exact Git delta from the prior R19 creation commit. The prior R19 baseline had already reconciled all intake JSONL ledgers; the complete current Git comparison below contains **no changed `probability_1000_intake_*/problems.jsonl` path**, so I preserve that source baseline rather than pretending unchanged multi-megabyte ledgers changed.

These Section-B methods are being used on the only lawful active problem for a terminal worker — **finding a genuinely owner-clear CLOSABLE successor**. They are not presented as new attacks on the frozen I0084 theorem.

## 1. Idea before code

The new event stream exposes a distinction that the earlier terminal-wait logic had not yet witnessed in the same delta:

- a target can become **explicitly released** and still be unusable by R19 because it is a HARD target;
- a target can be newly **CLOSABLE** and still be unusable by R19 because it was claimed by another worker at creation.

So “release” and “CLOSABLE” are independent gates. The successor predicate must test both, together with current-source/exclusion and R19 ownership clearance.

No checker was written before this idea. No new finite mathematical claim is made by R19 in this run, so no checker is warranted afterward either.

## 2. Exact repository delta

Frozen predecessor commit:

`2608f296cffbde5ddc2041c6b01d92c1d9a6137e`.

Frozen pre-write master:

`bfdba11956b1721e5ff0bac1c3ad40ba585d9dda`.

Exact comparison:

- status: `ahead`;
- **97 commits ahead / 0 behind**;
- `too_large = null`, so the changed-file list is complete for this interval;
- no change to root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md`, campaign `RANKING.md`, or any `probability_1000_intake_*/problems.jsonl` file;
- exactly six canonical claim files were added and one existing canonical claim file changed materially.

The claim mutations are:

1. `operations/claims/B-WEAK-EVEN-LOGCONCAVE.md` — owned by HARD7-01; source OPEN; a HARD log-concave inequality route, not R19 CLOSABLE inventory.
2. `operations/claims/F0095.md` — owned by HARD7-06; sparse-random-graph 3-colorability threshold; HARD.
3. `operations/claims/P0083.md` — owned by NM13-13; explicitly `HARD OUTSIDE`.
4. `operations/claims/P0214.md` — owned by NM13-12; explicitly `HARD OUTSIDE`.
5. `operations/claims/P0257.md` — owned by NM13-11; explicitly `HARD OUTSIDE`.
6. `operations/claims/P0411.md` — **new genuine `CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE`** target, but owner is already `proofnet24/NM13-05`.
7. `operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md` — materially changed from active HARD7-01 ownership to **HANDOFF / source OPEN / research PARTIAL only / released after Section-I exhaustion**. It is a real explicit release event, but it is the full even-log-concave dimensional Brunn--Minkowski conjecture from a HARD track, not a CLOSABLE source for R19.

Thus this delta contains both kinds of near-hit — a CLOSABLE-but-owned claim and a released-but-HARD claim — and still contains **no owner-clear CLOSABLE successor for R19**.

## 3. Method #1 — CHANGE THE CATEGORY: treat successor admission as a typed state transition

I changed the admission problem from a flat list of candidate names into a typed transition system. Each event carries at least four independent types:

`{source status, lane type, ownership state, lifecycle state}`.

This immediately separates the two strongest new events:

- **P0411** has the right lane type (`CLOSABLE OUTSIDE`) but the wrong ownership state (`CLAIMED`, owner NM13-05).
- **GZ-DIMBM-EVEN-LOGCONCAVE** has the right ownership-transition shape (explicit release after exhaustion) but the wrong lane type for R19 (HARD predecessor/full hard inequality problem).

The category change prevents the invalid inference

`released target ⇒ R19 successor`

just as earlier history prevented

`terminal handoff ⇒ released target`.

**Outcome #1:** the current delta improves the admission taxonomy but yields no lawful R19 successor.

## 4. Method #16 — COMPUTE EVERY SMALL CASE: enumerate every canonical claim mutation in the complete delta

Because the exact 97-commit comparison is complete, the finite “small cases” are the seven canonical-claim mutations listed in Section 2. I checked each against the R19 lane/ownership gates rather than sampling promising names.

The result is exhaustive for this delta:

- one new CLOSABLE claim: P0411 — **already owned**;
- five new HARD/source-hard claims — **wrong lane and owned**;
- one explicit release: GZ-DIMBM — **wrong lane (HARD)**.

No canonical claim deletion, CLOSABLE release to unassigned state, or reassignment to R19 appears in the complete changed-file set. R06's Romero finite layer has meanwhile become candidate-complete pending audits, but its canonical ownership remains R06; completion by another worker is not a release to R19. R01's TFIK22 metric also moved inside its own owned claim and does not create free inventory.

Therefore the exact finite event count gives

`E_READY_SUCCESSOR: 0 → 0`.

**Outcome #16:** exhaustive delta enumeration finds zero owner-clear CLOSABLE successor events.

## 5. Method #18 — SAY IT IN ANOTHER LANGUAGE: Boolean gate form

Write the R19 successor predicate for a candidate `x` as

`Eligible_R19(x) = Outside(x) ∧ ExactFullSource(x) ∧ CurrentOpen(x) ∧ Closable(x) ∧ Nonexcluded(x) ∧ OwnerClearForR19(x)`.

Then the two strongest new events fail on complementary literals:

- P0411: `Closable=1`, but `OwnerClearForR19=0` because NM13-05 created the exclusive claim.
- GZ-DIMBM: `Released=1` and source remains open, but `Closable=0` for this worker's lane; it is a HARD handoff from HARD7-01.

The other five new claim files are both owner-bound and HARD/source-hard. Hence no event makes every conjunct true.

This representation also shows why the older H0021 precedent did not itself supply a R19 successor: explicit release is necessary to clear an old owner, but it is not sufficient to establish the required CLOSABLE lane and assignment.

**Outcome #18:** the admission obstruction is now a literal conjunction failure, not a vague shortage of queue candidates.

## 6. I0084 frozen source preserved exactly

I re-read the primary source on **2026-09-19**.

The current arXiv record is still `arXiv:1710.08240v2`, last revised **14 September 2018**. In the arXiv-v2 HTML, Conjecture 5.5 literally says:

- `S_t` is the law of a **classical or free** alpha-stable process at time `t`, with `alpha in (0,2)`;
- the hypothesis is exactly

  `∫ |x|^(2+alpha) dmu(x) < infinity`;

- the conclusion is eventual unimodality of the ordinary convolution

  `mu * S_t`.

Accordingly, this task's frozen source remains ordinary classical convolution `*` **even when `S_t` is the law of a free-stable process**. I do not replace it by `boxplus`.

For alpha=`1/2`, the retained source metric remains exactly **`2/2`**.

Stronger-moment results, compact-support-only results, posted additive Brownian-unimodality results, and already-known stable special cases receive no new source-case credit.

### Published-version provenance warning

The published ALEA text is not identical at Conjecture 5.5: it separately denotes a classical stable law `S_t` and a free strictly stable law `T_t`, and states `mu*S_t` respectively `mu boxplus T_t`. That later/published wording is relevant provenance but does **not** silently rewrite this worker's explicitly frozen arXiv-v2 target. Therefore an ALEA/free-`boxplus` end-to-end audit does not count as a version-matching audit of the frozen arXiv-v2 ordinary-`*` free-stable-law branch.

Primary pages checked:

- `https://arxiv.org/abs/1710.08240`
- `https://arxiv.org/html/1710.08240v2`
- published ALEA DOI/PDF `10.30757/ALEA.v15-15`

## 7. Fresh literature / prior-art check — 2026-09-19

Queries checked included:

- `"Conjecture 5.5" Hasebe Ueda 1710.08240 unimodality stable convolution`;
- `"1710.08240" Hasebe Ueda eventual unimodality stable later resolution 2025 2026`;
- `"Conjecture 5.5" "mu * S_t" unimodal Hasebe Ueda`;
- published ALEA Conjecture 5.5 / free-stable wording.

The bounded search recovered the original arXiv/ALEA paper and the version mismatch above, but did **not** recover a later primary source explicitly proving or refuting the exact frozen arXiv-v2 ordinary-`*` formulation. This is **bounded dated negative evidence only**, not a worldwide openness, novelty, or priority certificate.

No newly found source changes the fixed 2/2 mathematical metric or the terminal lifecycle.

## 8. Audit gate remains version-specific

The newest visible P26 report is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_09-01-52__run-report.md`.

It audits P21/I0104's degree-four MUB/SoS package, not I0084. It therefore contributes zero to the frozen I0084 audit gate.

The version-matching frozen-arXiv ordinary-`*` gate remains **0/2**. Existing noncounting evidence remains:

- `R18-I0084-C001=PASS` — finite/symbolic core check for the classical positive-half-stable endpoint only;
- `R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF` — end-to-end audit of the different ALEA free-`boxplus` formulation, not the frozen arXiv-v2 ordinary-`*` free-stable branch.

Repository closure of the frozen package would still require one P26 frozen-arXiv ordinary-`*` end-to-end PASS and one genuinely distinct OTHER-track frozen-arXiv ordinary-`*` end-to-end PASS. This run does not solicit or manufacture those audits because R19 is in terminal successor wait.

## 9. Model / scheduler control truth

Actual runtime available to this report is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so reasoning level is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The exposed scheduler-management surface still provides task identity/title, prompt, schedule/relative start, timing mode, enabled state, and list/update operations. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed hour-long execution control**. GPT-6 / maximum therefore remains prompt-requested only.

The operative implementation manifest records the historical P26 modification attempt returning `You cannot modify this task`; later repository evidence records successful P26 reconciliation from an authorized context. The lawful workaround is the same task's owning/authorized workspace/account/admin context or platform support. It is not task duplication, identity substitution, permission escalation, or bypass. No scheduler mutation was attempted in this run, as required.

## 10. Validation budget and repository integrity

No mathematical checker or certificate was manufactured because the source metric did not move and this run makes no new finite theorem claim. Validation is limited to:

- direct continuation from the exact prior R19 report;
- exact complete 97-commit Git comparison;
- direct reads of every admission-relevant canonical claim mutation;
- direct primary-source check and bounded current-literature search;
- newest P26 scope check;
- this one create-only immutable report and exact-commit readback.

No shared root, peer file, canonical claim, scheduler, email, Drive, public destination, workflow, purchase, permission, or unrelated artifact is modified.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R19
  lane: CLOSABLE_OUTSIDE
  source: "Hasebe--Ueda arXiv:1710.08240v2, Conjecture 5.5 / intake I0084"
  metric_name: "complete classical-stable/free-stable alpha=1/2 source cases proved"
  metric_before: "2/2"
  metric_after: "2/2"
  status: "TERMINAL_WAITING_FOR_NEW_READY_DELTA"
  unchanged_count: "TERMINAL_HANDOFF; not incremented after move-on"
  tried_moves: [1, 16, 18]
  successor_gate_before: 0
  successor_gate_after: 0
  predecessor_report: "runs/R19/2026-09-19_05-43-21_UTC__terminal-wait-three-closable-claims-owned_x7q2.md"
  predecessor_commit: "2608f296cffbde5ddc2041c6b01d92c1d9a6137e"
  frozen_prewrite_master: "bfdba11956b1721e5ff0bac1c3ad40ba585d9dda"
  compare_ahead_by: 97
  compare_behind_by: 0
  compare_complete: true
  root_or_intake_change_seen: false
  claim_events:
    P0411: "CLOSABLE, already owned by NM13-05"
    GZ_DIMBM_EVEN_LOGCONCAVE: "explicitly RELEASED, but HARD predecessor/full hard target; not R19 lane"
    B_WEAK_EVEN_LOGCONCAVE: "HARD, owned by HARD7-01"
    F0095: "HARD, owned by HARD7-06"
    P0083: "HARD, owned by NM13-13"
    P0214: "HARD, owned by NM13-12"
    P0257: "HARD, owned by NM13-11"
  remaining_obligation:
    - "react only to a literal-changing owner-clear source-exact CLOSABLE successor event or an explicit authorized reassignment into R19's lane"
    - "do not treat a HARD release as a CLOSABLE successor"
    - "do not reopen rotated I0084 theorem work or I0120 merely because another worker hands off a target"
    - "retain frozen I0084 ordinary-* package; before repository closure obtain two independent version-matching end-to-end audits"
  evidence:
    - "complete predecessor-to-master delta: 97 commits, too_large=null"
    - "P0411 canonical claim: CLOSABLE OUTSIDE, owner NM13-05"
    - "GZ-DIMBM canonical claim: released after HARD7-01 Section-I exhaustion; source OPEN/PARTIAL"
    - "no changed root QUEUE/RESULTS/POSTED/campaign INDEX/RANKING/intake JSONL path in complete delta"
    - "arXiv v2 Conjecture 5.5 re-read: ordinary mu*S_t, exact (2+alpha)-moment, classical-or-free stable S_t law"
    - "published ALEA Conjecture 5.5 has separate classical-* / free-boxplus wording; scope mismatch preserved"
    - "latest visible P26 run audits P21/I0104, not I0084"
  audit_ids:
    frozen_I0084_version_matching: "0/2"
    noncounting:
      - "R18-I0084-C001=PASS [finite/symbolic classical endpoint core only]"
      - "R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF [ALEA free-boxplus scope]"
  scheduler_changed: false
  shared_roots_edited: false
  peer_files_edited: false
  email_or_drive_used: false
```

**Net result:** there is a genuine repository update worth preserving — for the first time in this terminal-wait sequence the same exact delta contains both a newly admitted CLOSABLE target that is already owned (P0411) and an explicit released target that is HARD (GZ-DIMBM). That proves the successor gate must track lane and ownership as independent literals. Neither event authorizes R19 to restart research, so the fixed source metric remains `2/2` and R19 remains in terminal wait.