Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# R7-02 shard-1 delta screen — Matrix Spencer status correction and live-queue exhaustion

Date: 2026-09-18.
Worker: `R7-02 Finite Certificate Research`.
Native ID recovered from `operations/research7_2026-09-17/REGISTRY.md`: `6aabe797a39081919acc889f29f4c556`.
Own root: `research7_2026-09-17/R7-02/`.
Run-start master: `65757c9fd1b8cad4acd937d7e3553e023d6f6d1e`.
Fresh master before this delivery stage: `171ccefc94070b4970779e5c152d87f92ea906e9`.
Previous own checkpoint: `research7_2026-09-17/R7-02/runs/2026-09-18/2026-09-18T122600Z__report.md`, creation commit `a6cc1e4223e30051f80766f1d3944b9db59a8ff4`.

Current state entering and leaving this screen: `PENDING_ADMISSION`.
Successor metric: `UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.
No target-specific stagnation count exists because no successor has been admitted.
The retired P0072 metric is not inherited.

## 1. Why this is a delta screen rather than a repeat

The preceding R7-02 work had already exhausted the then-visible residue-1 D/E/F/G/H/I intake cursor and, in the latest screen, rechecked the remaining I-series candidates. This run therefore did not restart at rank 1. It inspected the current live queue, current canonical claims and post-checkpoint repository changes, and then performed a fresh primary-literature correction on the one residue-1 intake whose status materially changed: `I0090` / Matrix Spencer.

The exact shard gate remains

```text
sum(ord(c) for c in canonical_id) % 7 == 1.
```

It is a selection partition only, never ownership.

## 2. Exact live-queue residue-1 delta

Applying the exact case-sensitive residue test to the currently listed rank-1--55 queue rows gives the following residue-1 rows:

`I0011, I0054, I0079, I0110, I0002, I0045, I0027`.

The owner-added famous finite block `I0120`--`I0129` contributes one additional residue-1 row: `I0126`.

Current disposition:

- `I0011`: exclusive P16 claim; unavailable.
- `I0054`: exclusive R11 reservation/active history; unavailable.
- `I0079`: canonical claim and active historical work exist; unavailable.
- `I0110`: canonical R19 claim; unavailable.
- `I0002`: canonical R12 claim; unavailable.
- `I0045`: latest R7-02 source/later-author review found that the old preferential-attachment local-limit question has been overtaken by later work; it is not a safe fresh CLOSABLE admission.
- `I0027`: canonical R04 reservation; unavailable.
- `I0126`: canonical P03 claim and immutable HARD handoff; unavailable and not CLOSABLE.

Thus the current live queue contributes **zero** lawful residue-1 CLOSABLE successors.

The current queue also contains historical stale READY prose for some rows. That prose does not override newer canonical claims, source-resolution evidence or immutable handoffs.

## 3. Material source-status correction: I0090 / Matrix Spencer is KNOWN

`I0090` satisfies the shard gate (`sum(ord(c) for c in "I0090") % 7 = 1`). The previous R7-02 successor screen conservatively treated it as a broad HARD-shaped source problem. Fresh primary-source review on 2026-09-18 shows that this is now too conservative: the exact square Matrix Spencer conjecture is resolved in 2026 literature.

Source target as preserved by the intake/Randomstrasse source: for real symmetric `n x n` contractions `A_1,...,A_n`, find signs `x_i in {+1,-1}` such that

`|| sum_i x_i A_i || = O(sqrt(n))`.

Fresh current-version/follow-up evidence:

1. Emrullah Akbas and Suvrit Sra, *A Proof of the Matrix Spencer Conjecture*, arXiv:2608.28816, submitted 2026-08-28. Its abstract states the same square `n`-matrix/`n x n` operator-norm hypothesis and says the Matrix Spencer conjecture is resolved with an `O(sqrt(n))` signing.
   URL: https://arxiv.org/abs/2608.28816
2. Zhao Song and Lichen Zhang, *Matrix Spencer: Eight Standard Deviations Suffice and an Almost-Linear Time Algorithm for Dense Input*, arXiv:2609.15025, submitted 2026-09-14. It proves a signing with discrepancy below `8 sqrt(n)` under the same square hypotheses.
   URL: https://arxiv.org/abs/2609.15025
3. Nikhil Bansal and Yunbum Kook, *A simpler proof of the Matrix Spencer Theorem*, arXiv:2609.16100, submitted 2026-09-14, explicitly presents a simpler proof of the Akbas--Sra theorem.
   URL: https://arxiv.org/abs/2609.16100
4. Tarun Kathuria, *A Walk From Free Probability to Matrix Discrepancy I: Matrix Spencer*, arXiv:2609.18914, submitted 2026-09-16, independently states and proves the square `O(sqrt(n))` result and a rectangular extension.
   URL: https://arxiv.org/abs/2609.18914

These are source-matching theorem statements, not a search miss. The honest admission disposition is therefore

`I0090 = KNOWN / RESOLVED_IN_LITERATURE_2026 / NOT CLAIMABLE`.

This is a source-status correction, not R7-02 mathematical progress and not a novelty claim.

## 4. Three Section-B admission-route tests

There is no lawful active mathematical target in this run, so these methods are used only to make the admission screen substantive; they do not start a target stagnation counter.

### B12 — FIND WHAT IS CONSERVED

The conserved object is the exact source identity plus ownership/lifecycle, not a stale queue label. A row does not become free when a worker pauses, and an old `READY` or `admitted=true` label does not survive a newer exclusive claim, source resolution or immutable retirement. Applying that invariant eliminates all eight live-queue residue-1 rows above without interpreting silence as release.

### B18 — SAY IT IN ANOTHER LANGUAGE

Write the admission predicate as an intersection

`Eligible = Shard1 ∩ Outside ∩ CLOSABLE ∩ SourceOpenNow ∩ OwnershipClear ∩ NotRetired ∩ ExactScopeRecovered`.

For the current live-queue residue-1 set, every element fails at least one factor. `I0090` is especially instructive: it passes `Shard1` and is an outside source, but fails `SourceOpenNow` by positive primary-literature evidence. This formulation prevents an attractive old open-problem row from being promoted merely because it has a finite-looking statement.

### B27 — SWAP THE QUANTIFIERS

The unsafe algorithm asks, “Can I find some appealing residue-1 row that looks open?” The safe equivalent for this bounded delta is to enumerate **all** residue-1 rows in the changed/live candidate block first and then require each proposed successor to pass every admission predicate. Under that swapped order the live queue has no survivor, and `I0090` is removed globally by source resolution rather than reconsidered on every later run.

Outcome of B12/B18/B27: no lawful target is admitted, and no source metric is fabricated.

## 5. Ownership/nonduplication and history

The prior current-corpus exhaustion report already screened the residue-1 D/E/F/G/H/I intake candidates not represented by the live queue. This run found no newly added residue-1 intake row beyond the existing owner-added `I0120`--`I0129` block; within that block only `I0126` has residue 1 and it is already claimed/handed off as HARD.

Recent repository commits after the preceding R7-02 checkpoint add research/audit work to existing targets but do not create a newly eligible shard-1 CLOSABLE source. No missing claim was treated as release.

## 6. Admission result and next action

No admission record and no `operations/claims/<ID>.md` file are created in this run. The correct state is still `PENDING_ADMISSION`.

The next run should be delta-driven: inspect newly added/changed canonical candidates or explicit releases since this report, reapply the exact residue-1 gate, and only reopen a previously screened row if there is a material source/ownership/status change. Do not rerun the static current-corpus screen without such a delta.

## ledger_delta

- worker: `R7-02`
- native_id: `6aabe797a39081919acc889f29f4c556`
- target_before: `PENDING_ADMISSION`
- target_after: `PENDING_ADMISSION`
- successor_metric_before: `UNKNOWN/UNMEASURED`
- successor_metric_after: `UNKNOWN/UNMEASURED`
- target_stagnation_count: `NOT_STARTED`
- material_status_change: `I0090: prior conservative HARD/open-looking screen -> KNOWN/RESOLVED_IN_LITERATURE_2026`
- methods: `B12, B18, B27` (admission-route tests only)
- new_claim: `none`
- shared_ROOT_edits: `none`
- peer_edits: `none`
- delivery: pending creation/readback of this screen and the immutable run report
