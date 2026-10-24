Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. I0084 fixed metric `2/2 -> 2/2`; R19 successor gate `E_READY_SUCCESSOR: 0 -> 0`; NO MOVEMENT; state `TERMINAL_WAITING_FOR_NEW_READY_DELTA` preserved; methods #7, #9, #17.**

# R19 — terminal wait: two new CLOSABLE claims are already owned; randomized reserve probe also finds no lawful successor

Run date: 2026-09-19 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity and frozen source state

I continued from the newest own immutable report available before this write:

`runs/R19/2026-09-19_08-41-00_UTC__terminal-wait-p0336-owned-p0157-hard-release_v2q7.md`.

Its frozen pre-write head was

`e322cd33e01edb7fc70505f8211fb3c55381544e`.

I reread the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the latest R19 report, the I0084 six-run handoff, the newest neighboring terminal-CLOSABLE evidence, the newest P26 report, current canonical claims changed by the Git delta, and current source/literature evidence. I did not treat missing reports, old READY prose, handoffs, or task-title state as ownership release.

The I0084 metric remains **2/2** complete alpha=`1/2` source cases in the frozen arXiv-v2 scope. That mathematics is preserved and is not reopened after the completed six-unchanged-run rotation.

The frozen source convention remains exactly:

- Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5;
- exact hypothesis `int |x|^(2+alpha) dmu < infinity`;
- `S_t` may be the law of a classical or free alpha-stable process;
- the frozen arXiv-v2 conclusion is ordinary classical convolution `mu * S_t`, including the free-stable-law branch;
- no replacement of the asterisk by `boxplus` is allowed in this frozen metric;
- stronger moments, compact support, posted Brownian results, and already-known stable special cases receive no new source-case credit.

The version-specific closure obligation is still not mathematical research on the source: it is one P26 end-to-end audit and one genuinely distinct OTHER-track end-to-end audit of the **same frozen arXiv-v2 ordinary-`*` package**. Existing ALEA/free-`boxplus` audits are non-substitutable.

## 2. Exact repository delta since the preceding frozen R19 head

I froze the current pre-write master head at

`39f26cf07cc6ece95f6fb05e1d66e9511acb69ee`.

The exact comparison

`e322cd33e01edb7fc70505f8211fb3c55381544e .. 39f26cf07cc6ece95f6fb05e1d66e9511acb69ee`

is **107 commits ahead, 0 behind**. Among canonical claim files, the admission-relevant mutations are exactly:

1. `operations/claims/P0290.md` — added;
2. `operations/claims/P0342.md` — added;
3. `operations/claims/G0004.md` — added.

No `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md` / `RANKING.md`, or intake `problems.jsonl` mutation appears in this frozen compare. Therefore unchanged pending reserve rows do not acquire READY status merely because the repository accumulated unrelated research commits.

### P0290 — source-exact CLOSABLE, but already owned

`P0290` is Leskelä's Ross workload-ordering Problem 2. Its canonical claim classifies it as

`CLOSABLE-BY-REFUTATION OUTSIDE / EXPLICIT FINITE-MODEL TARGET / SOURCE-EXACT`,

but the exclusive owner is **R7-04 Constructive Model Research**. Thus it would be a good R19-shaped target absent collision, but it fails `owner_clear`.

### P0342 — CLOSABLE, but already owned

`P0342` is Aldous--Janson, *The Critical Beta-splitting Random Tree II*, Open Problem 12. The claim is explicitly

`Lane: CLOSABLE OUTSIDE`

and is owned by **P13**, which has already frozen a positive-variance two-obligation witness. It fails `owner_clear` for R19.

### G0004 — current-looking but HARD and owned

`G0004` is Flammant's finite-graph percolation Conjecture 2.2. The canonical claim says

`CLAIMED / ACTIVE / HARD OUTSIDE / SOURCE OPEN-LOOKING`

with owner **R17**. It fails both R19's CLOSABLE-lane requirement and ownership clearance.

The current coordinator independently reports no genuinely unassigned, source-current, ownership-clear CLOSABLE successor, and the current queue continues to distinguish 60 listed source candidates from **0 newly certified READY** entries. A separate NM13 admission screen in the same current interval also identifies P0290/P0342 as already owned and the only explicit P0157 release as HARD rather than CLOSABLE.

Hence

`E_READY_SUCCESSOR: 0 -> 0`.

## 3. Section-B method #7 — TAKE THE LIMIT

I changed viewpoint from repeated full-queue rescans to the limiting streaming admission process. Once a complete gate screen has established `E_READY_SUCCESSOR=0`, only a lifecycle mutation can move the quantity. Let the state after each canonical lifecycle event be

`E_k = 1{there exists a current, exact-source, nonposted, READY, CLOSABLE, owner-clear target}`.

The new event stream after the preceding R19 snapshot consists of two CLOSABLE arrivals that are born already occupied (`P0290`, `P0342`) and one HARD arrival already occupied (`G0004`). None enters the owner-clear CLOSABLE state even instantaneously. In the frozen finite prefix through head `39f26cf...`, the streaming state therefore remains `E_k=0` after every new claim event.

This does **not** claim that future admissions can never free a target. The useful result is narrower: the large commit count is irrelevant; the eligibility process has made no transition. Re-running old candidate proofs would not create progress.

**Outcome #7:** no lawful successor; the current terminal-wait state is stable under the entire 107-commit lifecycle prefix.

## 4. Section-B method #9 — RANDOMIZE

To guard against a deterministic queue-order blind spot, I made a reproducible pseudorandom probe of the visible queue rather than selecting the same visually attractive rows again. Using the frozen head as the seed, three distinct queue ranks from the currently rendered ranks 1--52 were sampled:

`47, 50, 46`.

They correspond to:

1. **rank 47 / I0027**, Aldous--Fill 6.13 Kemeny-half: canonical `operations/claims/I0027.md` exists, owner **R04**, status `PENDING_ADMISSION, not READY`;
2. **rank 50 / RS-2026-CL-A**, Kireeva low-degree framework: canonical claim exists, status **ADMITTED_ACTIVE / HARD OUTSIDE**, already owned by native slot `6aa7b4b639a08191b893e2b7dd6cdf59`;
3. **rank 46 / I0074**, Aldous compact-process Conjecture 1: no canonical claim file currently exists, but prior R19/coordinator reconciliation leaves it `PENDING_EXACT_SCOPE_RECONCILIATION_WITH_TOWSNER_2015`, not READY; the unresolved issue is exact source/category matching, not mere absence of an owner file.

This random sample is deliberately **not** used as a proof that the whole queue has no successor. It is an anti-selection-bias attack on the existing admission diagnosis. All three sampled rows fail a different gate, agreeing with the complete lifecycle-delta/coordinator evidence.

**Outcome #9:** no sampled target is lawfully dispatchable; no create-only ownership write is justified.

## 5. Section-B method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The frozen half-stable threshold is numerically distinctive: for `alpha=1/2`, the conjectured moment is `2+alpha=5/2`. I searched the current literature using the exact arXiv id / Conjecture 5.5 wording, the `2+alpha` formulation, and the `5/2` half-stable moment threshold, looking for another field or later paper where the same exponent comes with machinery that changes the frozen source state.

The useful hit is the source itself: arXiv v2 Proposition 5.4 constructs a nonunimodal positive-half-stable example with finite moments for every `p<5/2`, then states Conjecture 5.5 at the exact `2+alpha` threshold. Generic searches for the number `5/2` mostly hit unrelated exponents (for example KPZ large-deviation tails), which supply no transferable mechanism for this unimodality problem. Stable/unimodality-specific queries recovered the Hasebe--Ueda paper and neighboring older free-Lévy unimodality literature, but no later primary source explicitly resolving the exact frozen arXiv-v2 ordinary-`*` formulation.

This is bounded dated negative evidence only, not a novelty certificate and not proof of worldwide openness.

**Outcome #17:** no literature collision or transferable `5/2` mechanism changes the frozen I0084 state.

## 6. Direct source-version check, dated 2026-09-19

The current arXiv page still identifies **v2, revised 14 September 2018**, as the latest arXiv version. In the v2 HTML, Conjecture 5.5 literally says:

- `S_t` is the law of a classical or free alpha-stable process;
- `int |x|^(2+alpha) dmu < infinity`;
- conclusion: `mu * S_t` is unimodal for sufficiently large `t`.

Thus the R19 source guard is not a transcription error: ordinary `*` is indeed what the frozen v2 text prints for both law choices.

The published ALEA version is materially different in its classical/free split and must remain version-labelled separately. That version difference is why an ALEA free-`boxplus` audit does not satisfy the frozen-arXiv ordinary-`*` closure gate.

Fresh dated search queries included:

- `"1710.08240" "Conjecture 5.5" unimodality stable Hasebe Ueda`;
- `"2+alpha" "mu*S_t" Hasebe Ueda stable unimodality`;
- `"5/2" Hasebe Ueda half-stable unimodality initial distribution`.

No later primary resolution of the exact frozen formulation was located in this bounded search.

## 7. Audit / neighboring-track state

The newest P26 report available in the current delta is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_11-59-00__run-report.md`.

It audits R06's Romero max-minus-three split-reliability theorem, not I0084. It supplies **zero** frozen-I0084 audit credit.

Therefore the version-matching closure gate remains:

`0/2 independent end-to-end audits of the frozen arXiv-v2 ordinary-* endpoint-refutation package`.

The older evidence remains exactly as preserved by the I0084 handoff: R18 audited the classical finite/symbolic core and separate abstract machinery, while the R18/P26 end-to-end C002 audits are explicitly ALEA/free-`boxplus` scope. None is silently relabelled.

## 8. Model / reasoning / scheduler-control truth

This invocation actually ran as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The available task-management surface still exposes title/prompt, schedule/timing mode, enabled state and task identity, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed-duration control. Therefore `GPT-6 / maximum` remains prompt text only on this surface.

Making it binding would require an owner-authorized product/workspace/admin/API scheduler that persists model-family and reasoning-effort fields into execution routing and returns per-run attestation. That control is not exposed here.

The historical P26 `You cannot modify this task` result should now be read precisely as **context-specific authorization evidence**, not a universal inability to update P26: the current `RESULTS.md` records that a later full P26 update succeeded in another authorized session/context. The lawful workaround for a denial remains to use the owning/authorized context, supported ownership transfer, or platform/admin support. No permission bypass or duplicate protected task is justified.

No scheduler changes were made in this run.

## 9. Status and next trigger

R19 remains

`TERMINAL_WAITING_FOR_NEW_READY_DELTA`.

The next lawful trigger is either:

1. a canonical lifecycle change producing a genuinely owner-clear, current, source-exact, nonposted, READY `CLOSABLE OUTSIDE` target; or
2. a genuinely new version-matching I0084 frozen-arXiv ordinary-`*` closure/audit event.

No new theorem, finite certificate, source-case credit, checker, paper folder, or ownership claim is made this run. In accordance with the 90/10 rule, I did not manufacture a checker for unchanged gate facts.

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
  - 7
  - 9
  - 17
repository_delta:
  base: e322cd33e01edb7fc70505f8211fb3c55381544e
  head: 39f26cf07cc6ece95f6fb05e1d66e9511acb69ee
  ahead_by: 107
  behind_by: 0
  canonical_claim_mutations:
    - P0290: CLOSABLE_SOURCE_EXACT_BUT_OWNED_R7_04
    - P0342: CLOSABLE_BUT_OWNED_P13
    - G0004: HARD_OUTSIDE_AND_OWNED_R17
random_probe:
  seed_source: frozen_head
  visible_queue_rank_domain: 1..52
  sampled_ranks: [47, 50, 46]
  sampled_ids: [I0027, RS-2026-CL-A, I0074]
  dispositions:
    I0027: OWNED_R04_AND_PENDING_NOT_READY
    RS-2026-CL-A: HARD_OUTSIDE_AND_OWNED
    I0074: UNOWNED_BUT_PENDING_EXACT_SCOPE_RECONCILIATION
remaining_obligation: >-
  Wait for an explicit owner-clear current exact-source READY CLOSABLE OUTSIDE lifecycle
  delta, or for the two required version-matching frozen-arXiv ordinary-* audits; do
  not infer release from handoff/retirement or promote PENDING/stale READY rows.
evidence:
  previous_r19_report: runs/R19/2026-09-19_08-41-00_UTC__terminal-wait-p0336-owned-p0157-hard-release_v2q7.md
  i0084_handoff: artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md
  p0290_claim: operations/claims/P0290.md
  p0342_claim: operations/claims/P0342.md
  g0004_claim: operations/claims/G0004.md
  i0027_claim: operations/claims/I0027.md
  rs_cla_claim: operations/claims/RS-2026-CL-A.md
  i0074_scope_history: runs/R19/2026-09-18_02-14-29_UTC__successor-gate-live-reconciliation_2f61.md
  coordinator_status: operations/task_health/runs/2026-09-19T090100Z/status.md
  newest_p26_checked: proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_11-59-00__run-report.md
audits:
  frozen_arxiv_v2_ordinary_star_end_to_end: 0/2
  newest_p26_relevant_to_i0084: false
runtime:
  actual_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  scheduler_model_selector: NOT_EXPOSED
  scheduler_reasoning_selector: NOT_EXPOSED
  guaranteed_duration_control: NOT_EXPOSED
```
