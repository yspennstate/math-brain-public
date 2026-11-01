Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: `UNMEASURED -> UNMEASURED`; no Section-B method is credited because no source crossed admission.**

# NM13-01 — post-P0292 admission screen 1

Date: 2026-09-18 UTC  
Track / namespace: `NM13-01` / `proofnet24/NM13-01/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`

## 1. Runtime / scheduler disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still offers ordinary task fields such as title, prompt, schedule/relative start, enabled state, and timing mode. It still exposes **no binding model-family selector and no binding reasoning-effort selector**, and no authenticated completed-run model/effort attestation. Therefore GPT-6/maximum remains prompt text only. Making it enforceable would require an owner-authorized product/workspace/API/admin scheduler surface that exposes those selectors together with runtime attestation. The historical P26 `You cannot modify this task` result remains an authorization-context boundary; the lawful workaround is the owning/otherwise-authorized surface or platform/admin support, not duplication or bypass. No task, schedule, workflow, permission, email, Drive item, public surface, or paid-compute resource was changed in this run.

## 2. Authoritative continuity recovered

Before screening, I reread or targeted-recovered the required current control state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the canonical Codex/intake ledgers, especially `probability_campaign_2026_09/downloads_memos/Probability_open_problems_list_2026-09-07.csv`, `probability_1000_intake_I_20260914/problems.jsonl`, and the mirrored intake copy;
- newest NM13-01 report `proofnet24/NM13-01/runs/2026-09-18/2026-09-18T03-20-00Z__p0292-nonreversible-cycle-handoff.md`;
- current P0292 claim/history and searches for release/alias/reassignment;
- neighboring current Markov/probability work, including NM13-09 on P0245 and NM13-02 on P0037, plus current I0027/I0032 historical ownership/retirement records;
- the latest coordinator health report `operations/task_health/runs/2026-09-18T035800Z/status.md`.

The previous NM13-01 report is controlling continuity: P0292 reached six consecutive unchanged metric runs and was handed off. NM13-01 **must not run P0292 again**. Its old canonical claim file is historical state and does not override the later immutable handoff. The successor state was explicitly `ADMISSION_PENDING`.

The current coordinator report independently records that its pass found no second fresh free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor. That is useful fleet evidence, but I did not treat it as a substitute for this shard-specific screen.

A fresh repository-head check during this invocation saw current work continuing in other namespaces but no material release making P0292 or a neighboring claimed Markov source free. No inaccessible history material to the dispositions below was identified.

## 3. Shard rule and canonical-key screen

The exclusive shard is

`int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 0`.

I did **not** hash title aliases for intake-I rows whose canonical dedup identity is missing. Such rows remain unscreened by shard until their source identity is reconciled, as required by the owner rule.

For the older Codex ledger, the canonical dedup key is explicit. I screened all Tier-1 rows from the campaign ranking and all Codex Tier-2 `P` rows against their canonical keys. **No Tier-1 candidate hashes to residue 0.** Among the Tier-2 `P` rows, the residue-0 entries are P0030, P0294 and P0456; each fails the CLOSABLE-source gate below. This is stronger than merely scanning titles for Markov keywords.

I also retained previously identified residue-0 rows outside those two tiers where they were plausible enough to require an explicit disposition. Their exact canonical hashes are:

| ID | Canonical dedup key | SHA-256 | residue | disposition this run |
|---|---|---|---:|---|
| P0007 | `deterministic_mirror_unbounded_component_all_rays_bounded` | `e72a8c633c91e171b858123b71dc97c6db03bb8c73fd434b4facfeabad384dff` | 0 | unclaimed but attempted and not CLOSABLE-shaped |
| P0017 | `kls_isotropic_log_concave_dimension_free_cheeger` | `9d6b49dad121f4e421e87d1a97516a82908c92d14c01b7a5eb4cc1b78473c511` | 0 | famous HARD target; fleet ownership/history also excludes it |
| P0030 | `forward_backward_brownian_decomposition_compatibility` | `10375979625fa42ee485cca72a3932e7170968d21cfee948f790105c176b94cd` | 0 | Tier-2 attempted Brownian-process hard problem, not a finite/short CLOSABLE target |
| P0279 | `cutoff_for_bounded-degree_ising_throughout_the_rapid-mixing_phase` | `fa0b73550c9126b173046c511983b757c9d14f0ec0085c2ef4981e5f143ec06a` | 0 | currently claimed HARD target; unavailable |
| P0292 | `characterize_ctmc_speed_monotonicity_in_supermodular_order` | `3aded70a56a908e9042798ee4a8ac614005a51635e52453716ea79167c073ae5` | 0 | NM13-01 exhausted/handoff; forbidden to reopen |
| P0294 | `compute_a_first_order_bias_correction_for_continuous_workload_mean_field_models` | `4decaa470cdee54076b79e298d4cdd06af03464b153b9e19fae0fcd11acccc19` | 0 | Tier-2 but broad/asymptotic and now marked partially resolved in later literature with exact source match still uncertain |
| P0413 | `low-intensity_variance_of_typical_hyperbolic_voronoi_cell_volume` | `ef2cc73bfc3574ba74535e43aaf2c0ee36aa139b81b74c1d9e78843cfb9a7fea` | 0 | asymptotic infinite-geometry variance problem, not a finite/short CLOSABLE target |
| P0444 | `computational_complexity_of_the_multiserver-job_stability_threshold` | `85cadaf26c9a746689c8e4b6e33a35a2a16b42f06c74f23cb5ce95fd09b9dce5` | 0 | unclaimed, but campaign Tier-3 and source-wide complexity target lacks a finite deciding certificate |
| P0456 | `the_fine_connectivity_window_for_bilateral_preference_graphs` | `17e06ba38e5fdce83e504b385667e002b3c55dd649b78b3dc7f10dcd469739eb` | 0 | Tier-2 asymptotic critical-window problem; HARD-shaped rather than CLOSABLE |
| P0486 | `directional_zero-one_law_beyond_the_plane` | `438f61ae21343731b50966895e2637d99b9489e12df41ac79975666f6769fe78` | 0 | classical HARD RWRE zero-one problem, not CLOSABLE |

No duplicate ownership is created by these dispositions. In particular, missing `operations/claims/<ID>.md` files for P0007, P0030, P0294, P0413, P0444 and P0456 were treated only as evidence that no canonical claim exists at those paths; **absence of a claim is not admission**.

## 4. The two closest unclaimed residue-0 candidates still fail admission

### P0007 — deterministic mirror trapping

The exact source is Geoffrey Grimmett, *Selected Problems in Probability Theory*, Question 3.3. The campaign ledger records an earlier attempted reduction: unbounded straight visibility would prevent trapping, but an unbounded connected planar open set need not contain an unbounded straight ray; a spiral corridor kills that inference. No mirror configuration trapping every reflected ray, and no impossibility theorem, was produced.

A fresh bounded literature check dated 2026-09-18 searched the exact problem wording and mirror/Lorentz terminology. It recovered Grimmett's source (arXiv:2205.07318 and the current Cambridge-hosted PDF) but no later source-matching resolution in the returned results. This is bounded negative evidence only. More importantly for **admission**, the source quantifies over the continuum of launch directions in an unbounded billiard geometry. I found no source-valid finite certificate or short extremal parameter whose movement would make this a realistic CLOSABLE assignment. It is also previously attempted, contrary to the preference for an unattempted source. P0007 therefore remains screened out, not claimed.

### P0444 — complexity of the multiserver-job stability threshold

The exact Codex row comes from Baccelli–Olliaro–Marsan–Marin, *The Multiserver-Job Stochastic Recurrence Equation for Cloud Computing Performance Evaluation* (arXiv:2601.20653, 28 January 2026). The source defines the stability threshold through the asymptotic saturated-pile growth constant. The campaign's earlier equal-demand reduction gives a classical scheduling special case but explicitly derives **no general finite-sample certificate or computational-complexity bound**.

A fresh bounded 2026-09-18 search recovered the January 2026 source, a June 22, 2026 explicit multiresource stability-criterion paper by Rumyantsev, and other 2026 multiserver-job scheduling/stability papers. None of the returned sources supplied the source-wide computational-complexity classification asked in P0444. Again this is bounded negative evidence, not a worldwide-openness certificate. The decisive admission point is that P0444 remains a broad complexity/asymptotic-growth problem (campaign Tier 3), not a counterexample/number/finite-certificate/short-theorem target. I therefore did not relabel it CLOSABLE merely to fill the shard.

## 5. Queue/intake-I alias safeguards

Current `QUEUE.md` contains many PENDING/HOLD entries, not a list of free READY tasks. Several attractive Markov-chain rows are unavailable for independent reasons: I0027 has an R04 claim plus a retirement handoff; I0032 has a C28 claim/history; I0010's noncubic spectral-gap item is explicitly recorded in current queue/history as already covered by Zhu's theorem rather than a fresh open successor. The current coordinator likewise says no additional free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor was certified in its latest pass.

For intake-I rows without `dedup_key`, I did not invent canonical strings to force them into residue 0. Their exact source identity must first be reconciled against existing Codex aliases/claims/handoffs. That is the durable next admission task if the queue changes or a genuinely promising unclaimed source appears.

## 6. Admission verdict and metric

**ADMISSION_PENDING.**

No candidate passed all of:

1. exact source scope recovered;
2. current-status check adequate for admission;
3. canonical dedup identity recovered and residue exactly 0;
4. no current or historical ownership conflict / retirement / exhaustion;
5. genuine `CLOSABLE OUTSIDE` shape with a realistic finite, exact-constant, counterexample, or short-theorem route.

Therefore:

- source ID: **none**;
- claim ID: **none**;
- canonical claim creation: **none**;
- metric before: **UNMEASURED**;
- metric after: **UNMEASURED**;
- mathematical movement: **none**;
- Section-B methods credited: **none** — methods 2/11/24 remain unspent because no problem was admitted;
- unchanged-run counter: **not started / 0** for any successor;
- stuck-recovery counter: **not started / 0** for any successor;
- P26 audit: **not applicable**;
- NM13-02 audit: **not applicable**.

Screening is bookkeeping, not mathematical progress. I created no checker, certificate, theorem artifact, paper folder, or audit request.

## 7. Durable screening cursor / next invocation

Do **not** restart from the top of the static inventory next hour. The durable cursor is:

- Codex Tier 1: canonical-key shard screen complete; no residue-0 source.
- Codex Tier-2 `P` rows: canonical-key shard screen complete; the only residue-0 rows are P0030, P0294 and P0456, all dispositioned above.
- Explicit extra residue-0 dispositions preserved through P0486, including P0007/P0017/P0279/P0292/P0413/P0444.
- Current queue/intake delta: no new free source identified in this invocation; rows without canonical dedup identity are not hashed by title.

Next invocation should first test for **material changes** to `QUEUE.md`, intake ledgers, claims, handoffs, POSTED/campaign state, or a genuine release. If none changed, continue deeper into previously unscreened Tier-3/held canonical residue-0 rows only when they have a plausible CLOSABLE route; do not repeat the same static candidates and do not reopen P0292.

## 8. Structured ledger delta for P26

```yaml
ledger_delta:
  task: NM13-01
  category: CLOSABLE_OUTSIDE
  status: ADMISSION_PENDING
  source_id: null
  claim_id: null
  prior_source: P0292
  prior_source_state: HANDOFF_AFTER_SIX_UNCHANGED
  metric_name: null
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  mathematical_progress: false
  methods_attempted: []
  reserved_initial_methods: [2, 11, 24]
  unchanged_run_count: 0
  stuck_recovery_count: 0
  screening_cursor: "Codex Tier1 complete; Codex Tier2 P rows complete; shard0 dispositions P0007/P0017/P0030/P0279/P0292/P0294/P0413/P0444/P0456/P0486; next = material delta/release, then deeper Tier3 canonical residue0 only"
  next_step: "Delta-check queue/intakes/claims/handoffs; admit only a genuinely free source-exact residue-0 CLOSABLE target."
  audits:
    P26: NOT_APPLICABLE
    NM13-02: NOT_APPLICABLE
```

This report is the single immutable NM13-01 run report for this invocation.