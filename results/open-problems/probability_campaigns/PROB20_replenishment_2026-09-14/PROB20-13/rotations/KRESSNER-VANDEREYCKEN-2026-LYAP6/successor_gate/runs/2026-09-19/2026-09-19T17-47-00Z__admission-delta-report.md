Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this was **not GPT-6 at maximum**, and I do not claim otherwise. Gate metric: **`E_READY_SUCCESSOR: 0 -> 0`**; **NO SUCCESSOR ADMITTED**.

# KRESSNER-VANDEREYCKEN-2026-LYAP6 successor gate — first post-retirement delta screen — 2026-09-19T17:47:00Z

**Native slot:** `6aa7b46f70a8819184095c277974c256`  
**Operational state:** `CLOSABLE OUTSIDE SUCCESSOR-ADMISSION GATE`  
**Retired predecessor:** `KRESSNER-VANDEREYCKEN-2026-LYAP6`, mathematical status **OPEN/PARTIAL**, operational status `RETIRED_AFTER_SIX_UNCHANGED`, frozen retired metric `R_LYAP6=1`.  
**Gate metric:** `E_READY_SUCCESSOR in {0,1}`, before `0`, after `0`.  
**Claim created this run:** **NO**.  
**Scheduler action this run:** **NONE**; preserve the existing enabled native slot and recurrence.  
**Captured pre-write master:** `1b8e295a640e5f98ae15ce4969f68fc9dd34785d`.

## 1. Continuity and immutable predecessor handoff

This is the first gate report under this retired LYAP6 root. There is no earlier `successor_gate/runs/` report to continue from. Continuity therefore begins from the complete immutable retirement handoff rather than from stale scheduler timestamps:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/KRESSNER-VANDEREYCKEN-2026-LYAP6/runs/2026-09-19/2026-09-19T16-57-00Z__report.md`

creation commit `776b566798e71a15c2b7aa89be436977ad1a25ca`, exact-commit report blob `bd39d7baece28d8468924248118cf07b9e05c378`; readback receipt creation commit `16d06bb43dadb5c8402d7c15de7313295fa866d9`.

I preserve the entire mathematical handoff. In particular, this gate run does **not** resume the order-six Lyapunov-operator problem, does not reset its metric, and does not reinterpret its partial theorems as a source solution.

The exact comparison

`776b566798e71a15c2b7aa89be436977ad1a25ca .. 1b8e295a640e5f98ae15ce4969f68fc9dd34785d`

is complete: **90 commits ahead, 0 behind**. The material admission-facing canonical claim additions in that interval are the Artstein-Avidan--Katzin literal equality clause and maximal-intersection ellipsoid uniqueness claims. The delta also contains many worker reports and artifacts but no change to the retired LYAP6 source verdict.

## 2. Repository reconciliation required by the gate

I reconciled the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, current claim events, current admission/task-health evidence, the retirement handoff above, and fresh neighboring successor-gate reports.

The root state remains operationally noisy: historical queue/ledger text contains older native-slot allocations and old READY/admission snapshots, while later claims and path-scoped history control current ownership. I therefore do not promote a row from an old queue label alone.

A fresh neighboring R19 gate report at current history makes the same important distinction: admissibility requires all of `source_exact`, `current_open`, `nonposted`, `CLOSABLE`, `owner_clear`, `retirement_clear`, and a current READY/source-screened state simultaneously. A candidate that is merely unassigned, finite-looking, or counterexample-shaped is not enough.

The current post-P0290 R7-04 intake-tail screen also supplies useful alias/ownership evidence: P0459 is genuinely CLOSABLE-shaped but actively owned; P0461 (Lyons determinantal entropy concavity) has active same-target repository work despite lacking a same-name modern claim file; P0353 and P0407 are literature-excluded; the remaining visible tail candidates screened there are theorem-scale/HARD-shaped. I treat this as neighboring evidence and independently retain this gate's ownership standard rather than inheriting another worker's claim authority.

## 3. Material claim/lifecycle deltas after LYAP6 retirement

### 3.1 Artstein-Avidan--Katzin literal equality clause

`operations/claims/AK-KATZIN-C41-EQUALITY.md` was added under HARD7-01 ownership. A later same-owner report now gives an exact dimension-two counterexample to the literal printed equality classification, with `n_bad: UNMEASURED -> 2`, while carefully separating that refutation from the already-known strong-(B) inequality and from maximal-intersection uniqueness.

Disposition for this gate: **NOT ADMISSIBLE**. It is already owned and source-level refutation work has already occurred. No duplicate claim is created.

### 3.2 Maximal-intersection ellipsoid uniqueness

`operations/claims/MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS.md` is also owned by HARD7-01. Its source-level question is the general-dimensional uniqueness of a maximum-intersection ellipsoid for intermediate radii `r_J<r<r_L`; the recorded baseline is the planar result `D_MI=2` and the higher-dimensional problem remains PARTIAL/OPEN in the checked repository evidence.

Disposition for this gate: **NOT ADMISSIBLE** because ownership is active; additionally the full general-dimensional uniqueness theorem is not the short finite/certificate endpoint sought for this CLOSABLE gate.

### 3.3 Explicit VDH release and other HARD events

Current neighboring gate evidence records `VDH-8.3-DUALITY` as explicitly released to unassigned status after exhausting its HARD recovery history. That is a real lifecycle release, but its retained source obligation is an asymptotic barely-supercritical configuration-model duality theorem and remains **HARD-shaped**, so release does not turn it into CLOSABLE inventory.

Likewise current BHS/MST universality work is theorem-scale and owned. These rows fail the lane requirement even before any attempt to manufacture a finite proxy.

## 4. Current 2025--2026 outside-source screens

This gate is instructed to continue delta-first through genuinely new/current sources, not merely recycle the static intake. I therefore ran bounded current-primary searches in addition to repository reconciliation. Search misses below are never treated as worldwide novelty or openness certificates.

### 4.1 Randomstrasse 101 Problems 32--33 — current source but not gate-ready

Primary current source checked 2026-09-19:

Afonso S. Bandeira, Randomstrasse 101, **“Bisections of large random sparse regular graphs (problems 32 and 33)”**, posted 2026-02-16, https://randomstrasse101.math.ethz.ch/posts/GraphBisections/ .

For fixed `d>=3` and uniformly random simple `d`-regular `G_d` on even `n`, Conjecture 32 asks

`(E MinBis(G_d) + E MaxBis(G_d))/n = d/2 + o(1)`.

The repository already has canonical claim `operations/claims/RS-2026-BIS32.md` and a substantial R14 history. The source target is also an asymptotic all-large-`n` theorem, not a finite certificate endpoint.

Disposition: **OWNED + HARD/ASYMPTOTIC; NOT ADMISSIBLE**. Problem 33 is likewise an asymptotic equality between expected MaxCut and MaxBis and does not supply an owner-clear finite successor here.

### 4.2 Randomstrasse Problem 31 — fresh 2026 theorem claim blocks open admission

A current primary arXiv record checked 2026-09-19 is Huibo Xu, Shi Fu, Youming Qiao, Dacheng Tao, **“Sharp Norms from Finite Structure: Graph Matrices and Structured Chaoses,”** arXiv:`2609.14266`, submitted 2026-09-13, https://arxiv.org/abs/2609.14266 . Its abstract gives the exact polynomial and logarithmic spectral-growth exponents for every fixed simple graph shape in the dense Rademacher model, the scope tracked in the Randomstrasse graph-matrix source.

Repository admission screens already record this as a source-matching current theorem claim and explicitly warn against re-admitting Problem 31 without a contrary scope correction.

Disposition: **KNOWN/RESOLUTION-CLAIMED IN THE MATCHING SCOPE; NOT ADMISSIBLE**. This run does not independently referee every proof line, but a live source-matching theorem claim is enough to block an “open successor” reservation.

### 4.3 I0128 / Sendov — stale queue-style open label rejected by current literature

Fresh 2026-09-19 evidence remains decisive that Sendov is no longer open inventory. Terence Tao's current Sendov materials state that Lech Mazur resolved the conjecture for all degrees and that the result was formalized in Lean; Teng Zhang, arXiv:`2609.19126` (submitted 2026-09-16), explicitly begins from the statement that Mazur proved Sendov and proves a stronger quadratic inequality. Repository task-health screens already classify I0128 as KNOWN/RESOLVED.

Disposition: **KNOWN/RESOLVED; NOT ADMISSIBLE**.

### 4.4 Non-Cancelling Intersections — genuinely new external hit, but already refuted in full

A fresh outside search found Antoine Amarilli, Mikael Monet and Dan Suciu, **“The Non-Cancelling Intersections Conjecture,”** arXiv:`2401.16210` (2024), together with Hermann Wilhelm's August 2026 sequence. The first Wilhelm paper only refuted the left-linear strengthening, which would have looked superficially like an interesting finite-counterexample route. But the later current primary record is Hermann Wilhelm, **“Refutation of the Non-Cancelling-Intersections Conjecture,”** arXiv:`2608.27416`, submitted 2026-08-27, whose abstract explicitly removes the left-linear restriction and refutes the conjecture in full via a finite lattice.

Repository exact-title search recovered no existing NCI project, but that does not matter: the current source status is already **REFUTED/KNOWN**, so it cannot cross an open-problem gate.

Disposition: **CURRENT-LITERATURE RESOLVED/REFUTED; NOT ADMISSIBLE**.

### 4.5 Post-P0290 populated Codex tail

The freshest repository tail screen reviewed CLOSABLE-looking rows before broad theorem rows. Its decisive dispositions are preserved here because they are materially newer than the retired LYAP6 handoff:

- `P0353`: literature-excluded;
- `P0407`: literature-excluded;
- `P0459`: exact CLOSABLE-shaped outside target, but canonical active ownership exists and a new substantive run is present;
- `P0461`: same-target active campaign under `proofnet24/lyons-entropy/`, hence an alias collision even without a modern same-name claim file;
- `P0468`, `P0470`, `P0477`, `P0486` and the remaining prioritized tail rows: broad asymptotic/infinite-volume/theorem-scale source obligations, not current CLOSABLE endpoints.

Disposition: **NO OWNER-CLEAR READY CLOSABLE ROW IN THIS BOUNDED TAIL PASS**.

## 5. Admission decision

No candidate screened in this bounded current pass simultaneously satisfies all required literals:

1. an exact externally posed source statement and locator;
2. current-open status after dated primary/later-author/citing checks;
3. nonposted/nonexcluded status;
4. genuine full-source **CLOSABLE OUTSIDE** shape rather than a convenient restricted slice of a HARD theorem;
5. owner and alias clearance;
6. retirement/lifecycle clearance;
7. a plausible source-level finite witness, exact constant/number, minimal counterexample, or short theorem route.

Therefore

`E_READY_SUCCESSOR: 0 -> 0`.

No canonical successor claim is created. No source metric is frozen. No successor research root is begun. No theorem checker, audit request, or numerical search is manufactured before admission.

## 6. Next delta-first action

Leave this native slot enabled as the CLOSABLE outside gate. The next invocation should begin from the then-current master and inspect only material changes after this report: new canonical releases/claims, newly populated intake rows, explicit current-source status changes, or genuinely new 2025--2026 outside problems not already screened. Do **not** re-open LYAP6 or the rows rejected above absent a material status correction.

Priority remains a source whose entire endpoint is naturally one of: exact yes/no, sharp finite constant/number, explicit finite construction, minimum witness, or a short theorem with a plausible exact route. Historical READY labels, missing claim files, and worker retirement by themselves are insufficient.

## 7. Model/control status

The available task-control surface in this execution context still exposes prompt/title/schedule/timing/enabled controls but no binding model-family selector, no binding reasoning-effort selector, no authenticated runtime-model/effort attestation, and no guaranteed-duration field. Thus `GPT-6 / maximum` remains prompt-only. Making it enforceable would require an owner-authorized platform/workspace/admin scheduler that persists those fields into execution routing and exposes authenticated applied-model telemetry.

Any future `You cannot modify this task` response remains an authorization boundary. The lawful response is the authorized owning context or platform/admin support, never duplication or bypass.

## ledger_delta

```yaml
ledger_delta:
  native_id: "6aa7b46f70a8819184095c277974c256"
  mode: "CLOSABLE_OUTSIDE_SUCCESSOR_GATE"
  predecessor:
    target: "KRESSNER-VANDEREYCKEN-2026-LYAP6"
    mathematical_status: "OPEN/PARTIAL"
    operational_status: "RETIRED_AFTER_SIX_UNCHANGED"
    frozen_metric: "R_LYAP6=1"
    retirement_report: "probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/KRESSNER-VANDEREYCKEN-2026-LYAP6/runs/2026-09-19/2026-09-19T16-57-00Z__report.md"
    retirement_creation_commit: "776b566798e71a15c2b7aa89be436977ad1a25ca"
    retirement_blob: "bd39d7baece28d8468924248118cf07b9e05c378"
  gate_metric: "E_READY_SUCCESSOR"
  gate_before: 0
  gate_after: 0
  movement: "NO SUCCESSOR ADMITTED"
  captured_prewrite_master: "1b8e295a640e5f98ae15ce4969f68fc9dd34785d"
  retirement_to_prewrite_delta:
    commits_ahead: 90
    commits_behind: 0
  screened:
    - id: "AK-KATZIN-C41-EQUALITY"
      disposition: "OWNED; literal clause already exactly refuted by owner; no duplicate"
    - id: "MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS"
      disposition: "OWNED; general-dimensional theorem target"
    - id: "VDH-8.3-DUALITY"
      disposition: "EXPLICITLY RELEASED BUT HARD/ASYMPTOTIC; not CLOSABLE"
    - id: "RS-2026-BIS32/33"
      disposition: "BIS32 OWNED and asymptotic; BIS33 asymptotic/HARD-shaped"
    - id: "Randomstrasse-31"
      disposition: "source-matching resolution claimed by arXiv:2609.14266"
    - id: "I0128-Sendov"
      disposition: "KNOWN/RESOLVED in current 2026 evidence"
    - id: "NCI-2401.16210"
      disposition: "full conjecture refuted by current arXiv:2608.27416"
    - id: "P0353/P0407"
      disposition: "literature-excluded in fresh tail screen"
    - id: "P0459"
      disposition: "CLOSABLE-shaped but active/canonically owned"
    - id: "P0461"
      disposition: "active same-target alias campaign"
    - id: "P0468/P0470/P0477/P0486 and remaining prioritized tail"
      disposition: "HARD/theorem-scale in current source scope"
  canonical_claim_created: false
  successor_metric_frozen: false
  successor_math_started: false
  shared_ledgers_edited: false
  scheduler_mutated: false
  keep_native_slot_enabled: true
  runtime_model: "GPT-5.6 Sol"
  reasoning_level: "UNVERIFIED"
  requested_model_effort_enforceable: false
  next_action: "delta-first current-source and ownership admission screen"
```

The actual creation commit of this immutable report is to be captured from the GitHub write result and the file is to be read back at that exact commit; no second receipt file is created because this gate invocation is limited to exactly one immutable gate report.