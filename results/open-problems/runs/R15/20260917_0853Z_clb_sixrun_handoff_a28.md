Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: active RS-2026-CL-B stays 4/4 -> 4/4, unchanged count 5 -> 6; predecessor Burdzy–Scheutzow I0076 stays retired/frozen at 2/4. Methods: #8 GO THE OTHER WAY AND DISCRETIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #26 HUNT THE SPORADIC CASE. SIX-RUN CLOSABLE ROTATION FIRES.**

# R15 — RS-2026-CL-B six-run handoff and successor-admission gate

Repository / branch: `yspennstate/math-open-problems` / `master`.
Worker/lane: R15 / CLOSABLE OUTSIDE.

## 1. Continuity and source recovery

I continued from the newest immutable R15 report

`runs/R15/20260917_0753Z_clb_stuck2_c4f8e2.md`

rather than restarting either source problem.

Before research I reread or exact-searched the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest R15 report, current R15 claim, current task-health successor screens, current neighboring R17 state, and exact intake/source records needed by this run. Large intake JSONL files were queried by exact ID/source instead of falsely described as visually rendered byte-for-byte.

### Preserved Burdzy–Scheutzow source scope

The predecessor is Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958 / ALEA 11 (2014), Problem 7.2.

The source definitions remain exactly the ones used in the six-run handoff:

- FBM: there exist random times `S_n -> -infinity` a.s. such that `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion for every n;
- BBM: the time-reversal is FBM;
- 2BM: for some random time `S`, the centered forward half and centered backward half are independent standard Brownian motions.

Problem 7.2 assumes FBM + BBM and existence of a random finite `T` such that the complete centered forward and backward half-processes at `T` are independent. It does **not** say that `T` is deterministic, does **not** say it is a stopping time, and does **not** assume either half is Brownian at `T`.

Problem 7.5 remains excluded.

I0076 was retired from active hourly attack after six unchanged runs. Its frozen positive-route metric remains **2/4**: P1 and P2 proved; P3/P4 remain open. The Theorem-6.1-derived `3/4` candidate was eliminated because it has no qualifying independent seam; the alternating Brownian-prefix/BES candidate was eliminated because it is actually 2BM after the Palm/excursion analysis. Nothing in this run reopens either candidate.

A fresh bounded 2026-09-17 source/literature check again recovered the original paper and neighboring Brownian/shift literature but no accessible later paper explicitly claiming to settle exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness or priority certificate.

## 2. Active RS-2026-CL-B state and mandatory six-run handoff

Canonical claim:

`operations/claims/RS-2026-CL-B.md`.

Outside source: Anastasia Kireeva, Randomstrasse 101, *Low-degree hardness of finding the largest clique in Erdős–Rényi graph (problems 36-38)*, posted 5 June 2026, unplanted-setting displayed conjecture (displayed as Conjecture 35 on the page).

The live source still prints, for `G~G(n,1/2)` and `epsilon>0`, a universal comparison over all polynomial maps

`f : {0,1}^{binom(n,2)} -> R^n`

of degree `o(log n)`, with factor `0<C<1`, between the maximum score over `k`-cliques and the maximum score over size-`k` vertex sets having at most `(1-epsilon) binom(k,2)` edges. The displayed statement still gives no `k`-range and no centering/norm/additive-constant restriction on `f`.

The frozen owner counterexample remains

- `k_n=1` for all `n>=2`;
- `f_n(G)=1_n`;
- any fixed `epsilon>0`.

The four frozen obligations are already proved:

1. `f_n` is source-admissible;
2. `deg f_n=0=o(log n)`;
3. both source maxima are exactly `1` for every graph;
4. the displayed inequality reduces to `1<=C`, contradicting `0<C<1`.

The exact self-check from the first owner run remains archived. No new checker is needed or justified.

This run makes **no fifth obligation**. Therefore

`metric: 4/4 -> 4/4`,

and the active unchanged count is now

`5 -> 6`.

Under the controlling CLOSABLE rule, **RS-2026-CL-B now rotates out of active research**. Its honest state is

**REFUTED AS PRINTED / RETIRED-HANDOFF / AUDIT-PENDING**, not CLOSED.

Repository-wide current searches still find no P26 source-level PASS audit and no distinct OTHER-track source-level PASS audit for this exact CL-B claim. The closure-audit coordinate remains **0/2**. I do not invent audit IDs, do not create a paper folder, and do not relabel the broader AIM low-degree clique-finding problem as solved.

## 3. Method #8 — discretize the successor search instead of producing another CL-B lemma

The correct finite action after a saturated 4/4 owner proof is not another robustness theorem; it is to inspect newly admitted finite/short successors without stealing an assigned row.

The latest task-health screen (2026-09-17 08:03 UTC) has newly admitted three CLOSABLE targets — D0044, D0038 and D0047 — and also records H0011 as immediately previously admitted. All four are already assigned to other native slots. In particular D0038 is exactly the kind of finite-state construction target that would fit R15's closable lane, but it already has a canonical claim and owner.

So discretization produced a useful negative result: **the best current finite-looking admitted candidates are occupied; R15 must not duplicate them.**

No competing claim was created.

## 4. Method #17 — look for your numbers somewhere else: D0057 is not safe dispatch inventory

I advanced beyond the already-screened preferential-attachment/Schramm front to a tempting short source conjecture in intake D.

D0057 is the 2017 max-type/Derrida–Retaux **Conjecture 2**, asking for the conditional critical limit law given survival. The intake/campaign notes identify the predicted geometric law and preserve an earlier attempt isolating tightness / escape-to-infinity as the obstruction.

A fresh dated literature search on 2026-09-17 found Zenghu Li and Run Zhang, arXiv:2411.13068 (20 Nov 2024), *Asymptotic behavior of the generalized Derrida-Retaux recursive model*. Its abstract explicitly says that, for the generalized model with geometric offspring distribution, it derives **the conditional limit law** and critical survival/first-moment asymptotics.

That later result is too close to D0057 to permit a create-only R15 claim without exact model reconciliation. This run did **not** establish that Li–Zhang's generalized geometric-offspring theorem is literally identical to the original 2017 fixed-`m` Conjecture 2, so I do not mark D0057 KNOWN. The lawful disposition is:

**D0057 = HOLD_LATER_WORK_SCOPE_RECONCILIATION / NOT READY for R15 dispatch.**

This is exactly why current-status checking must precede ownership claiming.

## 5. Method #26 — hunt the sporadic case: preserve the one-point CL-B defect but do not overuse it

The source-level CL-B sporadic case `k=1` remains decisive: `binom(1,2)=0`, so both feasible families are the singleton family and the all-ones map gives both maxima exactly `1`. The live source has not inserted a `k>=2` or logarithmic-`k` restriction since the owner proof.

But this is already the frozen 4/4 owner core. Repackaging the same edge case as a new lemma would violate the fixed-metric and 90-percent rules. The useful lesson for successor admission is narrower: short exceptional cases are valuable only when they survive current-source and later-work reconciliation. D0057 shows the opposite failure mode — a short-looking source conjecture may have later work directly overlapping its claimed conclusion.

Outcome: no new mathematical claim, no metric credit, no checker.

## 6. Successor-admission result

The current coordinator evidence now says:

- D0044, D0038, D0047 and H0011: newly admitted CLOSABLE targets, **already assigned elsewhere**;
- D0036/D0037: broad classification targets, PENDING / not CLOSABLE READY;
- D0042: HARD-leaning;
- previously screened I0037/I0038/I0040/I0044: resolved, substantially covered, or broad residuals;
- I0045/I0046: not safe open successors under the current van der Hofstad local-limit theorem;
- I0047/I0048/I0050: major later-work coverage / residual scope unfrozen;
- I0049: resolved in queued scope;
- H0013/H0014: prior campaign work already settled their target negatively;
- D0056: genuinely current-looking but a HARD exact-asymptotic-constant problem, not an honest CLOSABLE replacement;
- D0057: this run's fresh later-work overlap requires exact scope reconciliation before any claim.

The task-health screen intentionally leaves one CLOSABLE admission gate unfilled, but it does not name a current source-exact READY+unassigned target for R15. I therefore do **not** manufacture a successor claim from a stale PENDING row and do not take a HARD target merely to fill capacity.

R15 ends this run in

**ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED.**

A future R15 invocation should continue fresh successor admission from the next source-exact unclaimed intake candidate, not resume CL-B research unless a closure audit has arrived and only bookkeeping remains.

Reserved next-method triple if no coordinator assignment has appeared: **#1 CHANGE THE CATEGORY, #9 RANDOMIZE, #25 COUNT THE SAME THING TWICE**.

## 7. R17 neighboring audit trigger

The newest current R17 report is

`runs/R17/20260917_0814Z_c025_activepf_71e3.md`.

It gives a genuine deterministic improvement of the binary Chvátal–Sankoff upper endpoint to

`0.82627917854239782538084052`,

with archived exact finite-history checking. But the report explicitly labels the source problem **OPEN** and R17 **PARTIAL**. Hence there is no source-closure package for R15 to audit under the directed trigger. I did not manufacture an audit ID.

## 8. Model/reasoning controls and permission boundary

The model-control situation remains unchanged in the exposed task surface. It offers title/prompt/schedule/timing/enabled-state controls but **no writable model-family selector, no reasoning-effort selector, no authenticated applied-run model telemetry, and no guaranteed-duration control**. GPT-6 / maximum can therefore only be requested in prompt text from this surface; it cannot be truthfully asserted as the applied runtime setting.

Actually fixing this requires an authorized product/API/owner task-management surface that exposes model and reasoning fields and returns authenticated run metadata, or platform support.

The historical P26 `You cannot modify this task` response remains an ownership/authorization-context boundary. The lawful workaround is the owning authorized context, an owner/admin permission transfer or change where supported, or platform support — not a duplicate task and not a permission bypass. Repository history records that another authorized context later succeeded in modifying P26.

No scheduler modification was attempted in this run.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R15
  run_id: 20260917_0853Z_clb_sixrun_handoff_a28
  retired_predecessor:
    id: I0076
    source: "Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.2"
    metric: "positive-route obligations proved"
    before: "2/4"
    after: "2/4"
    unchanged_count: 6
    state: RETIRED_FROZEN_OPEN_PARTIAL
  active_target_at_run_start:
    id: RS-2026-CL-B
    source: "Anastasia Kireeva, Randomstrasse 101, 2026-06-05, displayed unplanted score conjecture"
    metric: "four source-witness obligations proved for frozen k=1, f=1_n counterexample"
    before: "4/4"
    after: "4/4"
    unchanged_count_before: 5
    unchanged_count_after: 6
    source_verdict: REFUTED_AS_PRINTED
    operational_state_after: RETIRED_HANDOFF_AUDIT_PENDING
    external_audit_count: "0/2"
    required_audits:
      - P26 source-level PASS
      - distinct OTHER-track source-level PASS
  methods_this_run: [8, 17, 26]
  remaining_obligation:
    - "two independent source-level closure audits for RS-2026-CL-B"
    - "admit/claim a new READY + unassigned + genuinely CLOSABLE outside successor"
  evidence:
    - operations/claims/RS-2026-CL-B.md
    - runs/R15/20260917_0257Z_clb_constant_shift_a23.md
    - artifacts/R15/20260917_0257Z_clb_constant_vector_exact_check.py
    - artifacts/R15/20260917_0257Z_clb_constant_vector_exact_check_output.txt
    - runs/R15/20260917_0753Z_clb_stuck2_c4f8e2.md
    - operations/task_health/runs/2026-09-17T080300Z/queue_screening.md
    - runs/R17/20260917_0814Z_c025_activepf_71e3.md
  audit_ids: []
  successor_screen:
    newly_admitted_elsewhere: [D0044, D0038, D0047, H0011]
    D0056: HARD_NOT_CLOSABLE
    D0057: HOLD_LATER_WORK_SCOPE_RECONCILIATION
    new_R15_claim: NONE
  next_methods_if_gate_remains_open: [1, 9, 25]
  overall: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
```

## 10. Delivery / prohibited-action audit

This report is the single R15 immutable report for the run. No shared root, other track file, canonical claim, email/Gmail, Drive, public post, purchase, permission, workflow, scheduler, or notification setting was edited. No numerical Brownian path sample was treated as verification of a Brownian law.

END OF CANONICAL REPORT
