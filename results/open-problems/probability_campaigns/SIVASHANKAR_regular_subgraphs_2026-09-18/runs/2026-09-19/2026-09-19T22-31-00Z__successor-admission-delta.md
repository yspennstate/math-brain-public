Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum, and I do not claim otherwise. SUCCESSOR GATE NO MOVEMENT: `E_READY_SUCCESSOR: 0 -> 0`.**

# NEW-METHODS-2026-09-16 — CLOSABLE OUTSIDE successor-admission delta

Repository: `yspennstate/math-open-problems`  
Branch: `master`  
Native slot: `6aa7b53b0858819196d923203522c996`  
Captured input master: `6f0059bbea21c375fd6db23d2ad835fa4c7b5a36`

## 1. Required current-state read

At the captured master I read the current fleet entrypoint, `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`, campaign `RANKING.md`, the newest coordinator/task-health status, canonical claims implicated by the fresh Git delta, and fresh Git history. The comparison from the previous gate input master `2ec2f6be653bc4955b465741609794ab051bb0ef` to this captured master is ahead by 130 commits.

The newest task-health record still reports enabled successor-admission gates with no mathematical target and strict newly certified free READY CLOSABLE additions equal to zero; it expressly forbids manufacturing READY inventory from search misses or already-owned claims.

The previous gate cursor is preserved. I screened exactly one candidate whose canonical lifecycle materially changed in the fresh delta and which was not already in this gate's cursor.

## 2. Exactly one screened material delta — `G0004`

Candidate: `G0004 = flammant_finite_graph_2026::conjecture_2.2`.

Material change: canonical claim `operations/claims/G0004.md` was changed by commit

`70155fb23bac6ef0f0ed9c7a068cb6b969b61208`

with message `R17: release G0004 after hard two-recovery limit`.

Current canonical lifecycle state:

- owner: **UNASSIGNED AFTER R17 HANDOFF**;
- status: **SOURCE OPEN / PARTIAL / RELEASED BY R17**;
- class: **HARD OUTSIDE**;
- release date: 2026-09-19 UTC.

This is a genuine ownership release, so ownership is clear. It is nevertheless not a CLOSABLE admission.

## 3. Source/current-status evidence reused rather than churned

Exact outside source:

Lucas Flammant, *A conjecture implying theta(p_c)=0 for Bernoulli bond percolation on Z^d*, arXiv:2609.03492, Conjecture 2.2.

The source target is the unrestricted arbitrary-finite-graph statement: for every finite graph with origin, boundary and increasing high-probability events `(E_b)`, prove a universal `phi(epsilon) -> 1` lower bound for the probability of a connected boundary point whose event succeeds.

The release claim and its immediately preceding R17 handoff already contain a dated 2026-09-19 bounded source check: arXiv:2609.03492 remained the current primary source; its abstract still presented the arbitrary finite-graph statement as a conjecture; the source proved only the outer-face planar case; bounded exact-title/conjecture/author searches found no later primary source claiming the unrestricted theorem. I reused that completed same-day evidence rather than rerunning unchanged literature searches.

Frozen source-wide metric:

`U_F = 1`,

where `U_F` is the smallest rigorously certified upper bound on `limsup_{epsilon -> 0} R_*(epsilon)` under all source quantifiers. The release record explicitly says the unrestricted source is not solved.

## 4. Exact blocker

`G0004` fails the successor gate because it is source-faithfully **HARD OUTSIDE**, not CLOSABLE OUTSIDE.

R17 exhausted both permitted HARD recovery cycles and still left the unrestricted theorem OPEN/PARTIAL. Its durable positive work includes sharp star asymptotics, downset/shadow reductions, several full-quantifier structured graph families, a cluster-measurable linear modulus, contact-size bounds, a recursive-spine obstruction to overly strong Hölder moduli, and a recursive-module no-go theorem. The remaining source-level obstruction is adaptive boundary-label switching through shared connectivity together with genuinely global decreasing failure kernels. That is a theorem-scale unrestricted percolation problem, not a finite or narrowly decidable endpoint that can be truthfully reclassified as CLOSABLE.

Therefore release does not imply CLOSABLE eligibility. No relabeling is permitted.

Disposition:

`NOT_ADMITTED / OWNERSHIP_CLEAR / HARD_OUTSIDE / SOURCE_OPEN_PARTIAL`

`E_READY_SUCCESSOR: 0 -> 0`

## 5. Predecessor continuity

`SIVASHANKAR-2026-REGSUB-EVEN` remains operationally retired and mathematically **OPEN / PARTIAL**. This run does not resume it, relabel it, alter its mathematical status, inherit any of its state, or create a substitute claim under its name.

There is still **no admitted successor** for this native slot.

## 6. No side effects beyond the immutable delta

Because `G0004` failed the CLOSABLE classification gate:

- no successor canonical claim was created;
- no successor research root/handoff was created;
- no fresh successor metric was initialized;
- no scheduler or task ID was created;
- no existing foreign claim was modified;
- no email, Drive, public posting, paid compute, credential/access change, workflow execution, force-push, or permission bypass was used.

The native slot must remain enabled on its existing recurrence and continue only as this successor-admission gate.

## 7. Cumulative cursor delta

Append:

- `G0004`: materially released by R17 on 2026-09-19 and now ownership-clear, but canonical/source-faithful classification remains **HARD OUTSIDE / SOURCE OPEN / PARTIAL** with `U_F=1`; rejected for this CLOSABLE gate. Do not rescreen absent a material source/classification/lifecycle change.

All prior cursor entries remain unchanged except where a later explicit material lifecycle delta is separately recorded.

## 8. ledger_delta

```yaml
ledger_delta:
  native_task_id: 6aa7b53b0858819196d923203522c996
  report_kind: successor_admission_delta
  input_snapshot_sha: 6f0059bbea21c375fd6db23d2ad835fa4c7b5a36
  previous_gate_report: probability_campaigns/SIVASHANKAR_regular_subgraphs_2026-09-18/runs/2026-09-19/2026-09-19T21-30-26Z__successor-admission-delta.md
  previous_gate_creation_commit: 49d76bc28345adc284fd35bf0478f46b11e3df51
  candidate_id: G0004
  candidate_material_delta: explicit_release_by_R17
  release_commit: 70155fb23bac6ef0f0ed9c7a068cb6b969b61208
  exact_source: "Lucas Flammant, arXiv:2609.03492, Conjecture 2.2"
  source_status: SOURCE_OPEN_PARTIAL
  source_current_evidence: reused_same_day_2026-09-19_release_handoff_check
  ownership_before_screen: UNASSIGNED_AFTER_R17_HANDOFF
  ownership_clear: true
  canonical_class: HARD_OUTSIDE
  frozen_metric: "U_F = 1"
  gate_metric_before: 0
  gate_metric_after: 0
  decision: NOT_ADMITTED_HARD_OUTSIDE
  exclusive_claim_created: false
  successor_root_created: false
  successor_metric_created: false
  scheduler_created: false
  predecessor_status: SIVASHANKAR_OPERATIONALLY_RETIRED_MATHEMATICALLY_OPEN_PARTIAL
```
