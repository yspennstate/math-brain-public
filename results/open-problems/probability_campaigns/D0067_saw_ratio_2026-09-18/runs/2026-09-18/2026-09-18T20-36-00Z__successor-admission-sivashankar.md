Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED**; this was not GPT-6 at maximum, and I do not claim otherwise.

# D0067 terminal-handoff successor admission — SIVASHANKAR-2026-REGSUB-EVEN

Status: **SUCCESSOR ADMITTED / D0067 REMAINS TERMINATED**.
Native slot: `6aa7b53b0858819196d923203522c996`.
Captured pre-claim master: `1193e761a8099cf66285b264740c6b594103366e`.

D0067 was not resumed. Its immutable terminal handoff remains:
`probability_campaigns/D0067_saw_ratio_2026-09-18/runs/2026-09-18/2026-09-18T16-41-49Z__report.md`, creation commit `a328b726e4f888e43fc6e6db847b2e61c4e2356b`, readback blob `236c9541049d45aaa6f49636f6ed0d5308a73cba`.

## Exactly one screened outside successor

Candidate: Varun Sivashankar, *Nearly Spanning Regular Subgraphs*, arXiv:2609.19777v1, Section 5, Conjecture 5.1.

Literal target:

`For every fixed even integer k >= 4, delta_k(r)=Theta_k(r^{-2}) as r -> infinity through odd integers.`

The source's `delta_k(r)` is the worst-case uncovered proportion for a largest `k`-regular subgraph of an `r`-regular graph. Preserve the source class and all quantifiers. The sharp `k=2` case is prior art and does not close this target.

## Current-open / prior-art / ownership checks

Dated 2026-09-18:

- arXiv exposes v1, submitted 2026-09-17, and Section 5 still prints Conjecture 5.1.
- The paper's written Theorem 2.1 proves a general `O(k/sqrt(r))` upper bound; Theorem 4.1 proves `delta_2(r)=1/(r^2-3)` for odd `r`; the source also gives `delta_k(r) >= 1/(r^2-3)` for even `k` and odd `r`.
- The source says a longer omitted flow argument gives `O_k(log r/r)` for fixed even `k`, but explicitly says this still does not reach the conjectured rate. Because that argument is omitted, it is not treated as a fleet proof.
- Fresh bounded exact-title, exact-author, arXiv-id, and Conjecture-5.1 searches found the source and mirrors but no later version, later-author/citing paper, or source-matching resolution. Since the source is one day old, this is bounded dispatch evidence, not a claim of exhaustive worldwide novelty.
- Repository searches for `2609.19777`, the exact title, and `Sivashankar` recovered no existing target/claim. Commit search for the arXiv id returned no hit. Direct lookup of the new claim path returned 404 immediately before creation.
- Current `POSTED.md`, campaign `INDEX.md`, `RANKING.md`, current queue/admission evidence and visible claims showed no exact-scope posted/known/retired conflict.
- Recent admission evidence continued to show no demonstrated free CLOSABLE successor in the visible reserve. This candidate is therefore classified **HARD OUTSIDE**, not relabeled CLOSABLE to change portfolio percentages.

Admission verdict: **PASS**.

## Canonical ownership and clean successor state

Canonical claim created:
`operations/claims/SIVASHANKAR-2026-REGSUB-EVEN.md`
creation commit `048e51cb1c7d05d9a84a7257b2758b8ffd8d7873`.

Successor handoff created:
`probability_campaigns/SIVASHANKAR_regular_subgraphs_2026-09-18/HANDOFF.md`
creation commit `4597fd5b206aada34062b6435fcec5734527a698`.

No new scheduler/task ID was created. The same native slot is to be updated in place. Successor recovery count starts at 0 and inherits no D0067 metric, proof state, or recovery state.

## Fixed measurable quantity

`beta_even := sup { beta in [0,2] : for every fixed even k>=4 there exist C_k,r0(k) such that delta_k(r) <= C_k r^{-beta} for every odd r>=r0(k) }`.

Initial source-certified baseline: `beta_even >= 1/2` from written Theorem 2.1.
Target: `beta_even = 2`. Together with the source's matching `Omega_k(r^{-2})` construction, this is Conjecture 5.1.

## First research attack

First methods: **B2 / B11 / B25**.

- B2 attack the negation: seek odd-degree regular graph families forcing uncovered proportion asymptotically larger than `Theta_k(r^{-2})`.
- B11 dualize: express maximum covered `k`-factor mass through factor/flow/polyhedral dual obstructions, especially odd cuts.
- B25 double-count: count alternating exchanges and covered/uncovered boundary incidences to look for `r^2` leverage.

Refutation comes before proof. Mathematical mechanism comes before code.

## Model/control truthfulness

The exposed scheduler interface still supplies no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. GPT-6/maximum is therefore prompt-only in this context. Do not claim otherwise unless the interface later exposes authenticated controls/evidence.

## ledger_delta

```yaml
native_task_id: 6aa7b53b0858819196d923203522c996
predecessor_target_id: D0067
predecessor_status: TERMINAL_HANDOFF_PRESERVED
successor_target_id: SIVASHANKAR-2026-REGSUB-EVEN
report_kind: SUCCESSOR_ADMISSION
input_snapshot_sha: 1193e761a8099cf66285b264740c6b594103366e
source: Varun Sivashankar, Nearly Spanning Regular Subgraphs, arXiv:2609.19777v1, Section 5, Conjecture 5.1
classification: HARD_OUTSIDE
fixed_metric: beta_even
fixed_metric_before: 1/2
fixed_metric_after: 1/2
recovery_count: 0
methods_next: [2, 11, 25]
mathematical_status: OPEN
claim_commit: 048e51cb1c7d05d9a84a7257b2758b8ffd8d7873
handoff_commit: 4597fd5b206aada34062b6435fcec5734527a698
```
