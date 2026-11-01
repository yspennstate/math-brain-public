Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. I0084 fixed metric `2/2 -> 2/2`; R19 successor gate `E_READY_SUCCESSOR: 0 -> 0`; NO MOVEMENT; state `TERMINAL_WAITING_FOR_NEW_READY_DELTA` preserved; methods #5, #12, #28.**

# R19 — terminal wait: F0011 is HARD/owned; P0219 retires locally without canonical release

Run date: 2026-09-19 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity and frozen source state

I continued from the newest own immutable report available before this write:

`runs/R19/2026-09-19_09-43-00_UTC__terminal-wait-p0290-p0342-owned-random-probe_n7k3.md`

created at commit

`a6077d46585b917b61d730609d615c5273db9b1c`.

At run start I reread current `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest operations implementation manifest, the newest R19 report, the I0084 six-run handoff, the current coordinator status, the current P26 report, and all admission-relevant canonical/lifecycle files in the exact Git delta below. I did not treat missing reports, old READY prose, worker-local retirement, or handoffs as ownership release.

The I0084 mathematical state remains frozen and preserved:

- source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5;
- exact hypothesis: `int |x|^(2+alpha) dmu < infinity`;
- `S_t` may be the law of a classical or free alpha-stable process;
- the frozen arXiv-v2 conclusion is ordinary classical convolution `mu * S_t`, including the free-stable-law branch;
- the asterisk is not replaced by free convolution;
- stronger moments, compact support, posted Brownian-unimodality results, and already-known stable special cases earn no new source-case credit.

The fixed metric stays **2/2** complete alpha=`1/2` source cases. The source was already rotated after six unchanged runs; this invocation does not reopen it for another lemma.

The version-specific repository-closure obligation remains separate from mathematical saturation: one P26 end-to-end audit and one genuinely distinct OTHER-track end-to-end audit of the same frozen arXiv-v2 ordinary-`*` endpoint-refutation package. Existing ALEA/free-`boxplus` audits are non-substitutable.

## 2. Exact repository delta since the preceding R19 report

I froze current pre-write `master` at

`753a1270d018cabbbbafc28103627f71c196549e`.

The exact comparison

`a6077d46585b917b61d730609d615c5273db9b1c .. 753a1270d018cabbbbafc28103627f71c196549e`

is:

- status `ahead`;
- **105 commits ahead**;
- **0 behind**;
- `too_large = null`, so the returned changed-file set is complete.

Among canonical claim files, there is exactly one new mutation in this interval:

`operations/claims/F0011.md` — added.

There is no changed root `QUEUE.md`, `RESULTS.md`, or `POSTED.md`; no changed campaign `INDEX.md` or `RANKING.md`; and no changed `probability_1000_intake_*/problems.jsonl` in the complete comparison. Thus unrelated worker commits do not make a stale PENDING queue row READY.

### F0011 — new claim, but HARD and already owned

The new canonical claim is Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 9.4 (Integral spectrum). Its source target is the asymptotic

`P(M_n^sym has all eigenvalues in Z) = 2^{-(1/2+o(1)) n^2}`.

The claim itself classifies F0011 as **CLAIMED / HARD OUTSIDE** and assigns exclusive ownership to **R7-06**. Its finite exact enumeration quantity is only a PARTIAL milestone toward the full asymptotic. Therefore F0011 fails both the R19 CLOSABLE-lane gate and the owner-clear gate.

## 3. P0219 reaches six-run retirement, but does not become free inventory

A materially relevant lifecycle report was added for P0219, Aldous's high-density Hammersley-flow problem:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/rotations/P0219-HAMMERSLEY-FLOW/runs/2026-09-19/2026-09-19_10-03-50_UTC__report.md`.

That report moves the supported unchanged count `5 -> 6`, leaves `alpha_tax: 0 -> 0`, labels the source OPEN / track PARTIAL, and says the worker route is **operationally RETIRED / HANDED OFF from the CLOSABLE lane** at the mandatory six-run boundary.

But the canonical ownership record `operations/claims/P0219.md` is unchanged in this exact Git interval. It still says:

`Status: CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE`

with owner/native slot

`6aa7ebbe26308191a40003a950a2307a`.

Therefore local six-run retirement is **not** an explicit canonical release. P0219 does not become lawful R19 inventory. This also agrees with the current coordinator and independent admission screens, which continue to report no newly certified owner-clear READY CLOSABLE successor.

This is an important lifecycle update, but not a mathematical source result for R19.

## 4. Section-B method #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

Because I0084 is mathematically saturated and rotated, I applied this move to the successor lifecycle rather than manufacturing another stable-law lemma.

Parameterize the repository lifecycle by ordered admission/claim events `tau`, and define

`E(tau) = 1{there exists a current, exact-source, nonposted, READY, CLOSABLE OUTSIDE, owner-clear target for R19}`.

The relevant discrete derivative is the jump `Delta E` at a lifecycle event. In the complete 105-commit interval the only canonical claim jump is F0011, which arrives as HARD and occupied. P0219's local retirement report is not a canonical claim mutation at all. Hence no event in the interval changes any target from ineligible to owner-clear CLOSABLE, and

`Delta E = 0`

at every admission-relevant lifecycle event in this frozen prefix.

This is not a theorem that future events cannot free a target. Its value is operational: commit volume is not progress; only a qualifying lifecycle jump can move the successor gate.

**Outcome #5:** `E_READY_SUCCESSOR` does not move.

## 5. Section-B method #12 — FIND WHAT IS CONSERVED

The conserved object in the current ownership protocol is the **canonical exclusive owner** under worker-local status changes. A route may say RETIRED, TERMINAL, or HANDED OFF, but ownership is not released unless the canonical claim is explicitly deleted or rewritten to an owner-clear release/reassignment state.

P0219 is a clean current witness. Its worker report crosses the six-run retirement boundary, yet `operations/claims/P0219.md` remains claimed by the same native slot and does not appear in the exact changed-claim set. Thus the failed literal `owner_clear=false` is invariant under this local retirement event.

Earlier R19 runs found the opposite kind of event too: explicit releases change the canonical ownership record. The distinction is therefore concrete rather than semantic guesswork.

**Outcome #12:** local retirement conserves canonical ownership here; no successor is freed.

## 6. Section-B method #28 — REPLACE "FOR ALL" WITH "FOR TYPICAL"

As a diagnostic against repeatedly rereading every pending row, I inspected several current near-eligible shapes representing distinct failure modes:

1. **F0011** — source-current-looking but HARD and already owned;
2. **P0219** — CLOSABLE and locally retired, but still canonically owned;
3. **I0087** — currently unowned in the latest admission screen, but its surviving source scope is a broad IPVT classification/convergence programme rather than an honestly frozen finite/short CLOSABLE endpoint;
4. **I0106** — currently unowned in the latest admission screen, but the source itself offers multiple inequivalent transient reinforced-ant variants and does not freeze one exact process/quantity.

These typical near-misses fail different gates: lane, ownership, source shape, and exact source freeze. This is useful for deciding where admission effort is actually bottlenecked.

It is deliberately **not** used as a proof that the whole queue is empty. The no-successor conclusion rests on the complete canonical-lifecycle delta plus current coordinator/admission reconciliation, not on a four-item sample.

**Outcome #28:** the present scarcity is structural across several gate types, but no sampled row is lawfully dispatchable.

## 7. Original source and current-literature refresh — 2026-09-19

I rechecked the primary arXiv record and the v2 HTML text. The current arXiv record still identifies **v2, revised 14 September 2018**, as the latest arXiv version. Conjecture 5.5 literally states that `S_t` may be the law of a classical or free alpha-stable process, assumes

`int |x|^(2+alpha) dmu < infinity`,

and concludes eventual unimodality of

`mu * S_t`.

So the frozen ordinary-`*` convention is confirmed again directly from the source; I did not substitute `boxplus`.

Fresh bounded searches on 2026-09-19 used the exact arXiv id, `Conjecture 5.5`, `mu * S_t`, the `2+alpha` condition, and later Hasebe/Ueda work/citing material. They recovered the original paper and related later free-probability work but did not surface a later primary paper explicitly resolving this exact frozen arXiv-v2 ordinary-`*` formulation. This is bounded negative evidence only, not a novelty certificate or proof of worldwide openness.

## 8. Audit state

The newest P26 report in the current interval is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_12-59-00__run-report.md`.

It is a stuck/thinking run on Romero split-reliability and performs no I0084 audit. Therefore it contributes zero frozen-I0084 audit credit.

The version-matching gate remains:

`0/2 independent end-to-end audits of the frozen arXiv-v2 ordinary-* endpoint-refutation package`.

Preserved older evidence remains scope-labelled: the classical finite/symbolic core has an R18 pass, while the existing R18/P26 C002 end-to-end passes are explicitly ALEA/free-`boxplus` scope and cannot be relabelled.

## 9. Model, reasoning, and scheduler-control truth

This invocation actually runs as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The available task-management surface still exposes ordinary task identity/title/prompt, timing/schedule, and enabled-state controls, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed one-hour execution field. Therefore `GPT-6 / maximum` remains prompt text only on this surface.

Making it binding would require an owner-authorized product/workspace/admin/API scheduler that persists those inference-routing fields and returns authenticated per-run attestation.

The historical P26 `You cannot modify this task` result is authorization-context-specific rather than a universal immutability result: current repository records say a later full P26 prompt update succeeded from another authorized context. The lawful workaround for any denial is the owning/authorized context, supported ownership/permission transfer, or platform/admin support — never a permission bypass or duplicate protected task.

No scheduler, permission, email, Drive, public-posting, or ownership-control change was made in this run.

## 10. Status and next trigger

R19 remains

`TERMINAL_WAITING_FOR_NEW_READY_DELTA`.

The next lawful trigger is either:

1. an explicit canonical lifecycle event producing a genuinely owner-clear, current, source-exact, nonposted, READY `CLOSABLE OUTSIDE` target; or
2. a genuinely new version-matching I0084 frozen-arXiv ordinary-`*` end-to-end audit event.

No new theorem, source-case credit, exact finite certificate, checker, paper folder, or ownership claim is made this run. In accordance with the 90/10 rule, I did not manufacture a checker for unchanged gate facts.

## ledger_delta

```yaml
track: R19
frozen_source:
  intake: I0084
  authors: Takahiro Hasebe and Yuki Ueda
  arxiv: 1710.08240v2
  target: Conjecture 5.5 frozen arXiv source scope
  convolution_guard: ordinary classical `mu * S_t`, including frozen free-stable-law branch
metric:
  name: complete alpha=1/2 classical-stable/free-stable source cases proved
  before: 2/2
  after: 2/2
  movement: NO MOVEMENT
successor_gate:
  name: E_READY_SUCCESSOR
  before: 0
  after: 0
  movement: NO MOVEMENT
status: TERMINAL_WAITING_FOR_NEW_READY_DELTA
unchanged_count: TERMINAL_ROTATED_NO_INCREMENT
methods_tried:
  - 5
  - 12
  - 28
repository_delta:
  base: a6077d46585b917b61d730609d615c5273db9b1c
  head: 753a1270d018cabbbbafc28103627f71c196549e
  ahead_by: 105
  behind_by: 0
  canonical_claim_mutations:
    - F0011: HARD_OUTSIDE_AND_OWNED_R7_06
  lifecycle_notes:
    - P0219: SIX_RUN_RETIRED_LOCALLY_BUT_CANONICAL_CLAIM_STILL_OWNED
remaining_obligation: >-
  Wait for an explicit owner-clear current exact-source READY CLOSABLE OUTSIDE
  lifecycle delta, or for the two required version-matching frozen-arXiv
  ordinary-* end-to-end audits. Do not infer ownership release from a worker
  handoff/retirement and do not promote PENDING or stale READY rows.
evidence:
  previous_r19_report: runs/R19/2026-09-19_09-43-00_UTC__terminal-wait-p0290-p0342-owned-random-probe_n7k3.md
  i0084_handoff: artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md
  f0011_claim: operations/claims/F0011.md
  p0219_claim: operations/claims/P0219.md
  p0219_retirement: probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/rotations/P0219-HAMMERSLEY-FLOW/runs/2026-09-19/2026-09-19_10-03-50_UTC__report.md
  coordinator_status: operations/task_health/runs/2026-09-19T101100Z/status.md
  newest_p26_checked: proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_12-59-00__run-report.md
  queue: QUEUE.md
  results: RESULTS.md
  posted: POSTED.md
  campaign_index: probability_campaign_2026_09/INDEX.md
  campaign_ranking: probability_campaign_2026_09/RANKING.md
  operations_manifest: operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md
audits:
  frozen_arxiv_v2_ordinary_star_end_to_end: 0/2
  required:
    - P26 ordinary-* frozen-package end-to-end PASS
    - distinct OTHER-track ordinary-* frozen-package end-to-end PASS
scheduler_control:
  model_selector: NOT_EXPOSED
  reasoning_selector: NOT_EXPOSED
  authenticated_runtime_attestation: NOT_EXPOSED
  guaranteed_duration: NOT_EXPOSED
```
