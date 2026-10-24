Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed scheduler/runtime still provides no authenticated model-family selector, reasoning-effort selector, guaranteed-duration control, or applied-runtime routing receipt; I do not claim GPT-6 / maximum. **SUCCESSOR-ADMISSION METRIC: newly established lawful READY + CLOSABLE + UNASSIGNED successors `0 -> 0`; P20 remains `SUCCESSOR_ADMISSION_REQUIRED`.**

# P20 successor admission — I0031 current-status correction and rotation hold

Repository / branch: `yspennstate/math-open-problems` / `master`.
Prior retired research source: D0010, Ruodu Wang Open Problem 10; preserved handoff `proofnet24/P20-closure-log-unimodality/successors/D0010/runs/2026-09-17/2026-09-17T04-12-18Z__sixrun-handoff.md` at creation commit `3ba12c3f38e2f25c66f1ddb2a9d3eea73024ff1a`.
Former I0081 remains source-refuted / packaged / 2-of-2 OTHER-track audited / retired and is not reopened.

This is an admission run, not a mathematical continuation of D0010. No new P20 outside source is claimed below because no candidate cleared every required gate.

## 1. Required continuity reads and current admission cursor

Before screening I reread or refreshed the controlling repository surfaces:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`;
- the immutable D0010 six-run handoff above;
- the newest task-health successor screen visible at `operations/task_health/runs/2026-09-17T045900Z/queue_screening.md`;
- current canonical claim paths for the candidates touched below;
- the exact Aldous–Fill I0028–I0034 intake rows and the prior I0031 attempt memo;
- the newest P21 retirement/handoff state; and
- the newest visible P26 audit state. P26 is currently auditing other tracks; nothing in that state creates a free P20 successor or a new P21 theorem for directed audit.

The 04:59Z task-health screen correctly refused to fill a CLOSABLE gate from stale queue labels and left I0031 merely `PENDING` because its current-status/later-literature bundle had not yet been completed. This run advances that cursor materially: **I0031 is not open reserve at all; its source claim was already proved in the literature in 2010.**

The root `RESULTS.md` still contains older P20/P21 rows in search rendering, so newest immutable reports and canonical claims remain the controlling continuity evidence rather than stale summary text.

## 2. I0031 — exact source statement and prior campaign state

Canonical intake: `probability_1000_intake_I_20260914/problems.jsonl`, I0031.

Source: David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 7.31, §7.3.4.

Source statement frozen in the intake row:

> “Prove that, over distance-regular graphs excluding the n-cycles, tau_0 = O(n). Of course this would imply tau* = O(n) and EC = O(n log n).”

The same source location separately asks whether `tau_2 = O(log n)`; that is a different clause and is **not** silently substituted for the first claim.

The repository's 14 September attempt, `probability_1000_attempts_I_20260914/Probability_I0031_distance_regular_hitting_times_2026-09-14.md`, derived the exact intersection-array identity

`tau_0 = k sum_{i=1}^d (k_i+...+k_d)/(k_i c_i)`,

proved the universal lower bound `tau_0 >= n-1`, reproduced the Biggs–Smith value `195/101` over all thirteen cubic distance-regular graphs, checked classical families and feasible arrays, and explicitly labeled the conjecture **not proved**. `probability_campaign_2026_09/INDEX.md` therefore records I0031 only as `REDUCED to an intersection-array identity`.

Immediately before this report, direct fetch of `operations/claims/I0031.md` returned 404. Thus there is no current canonical I0031 owner to race — but current status, not mere unownedness, decides admission.

## 3. Fresh current-status correction: Markowsky–Koolen 2010 proves the source claim

Dated current-status search: **17 September 2026**.

Queries included the exact Aldous–Fill problem wording/number; `distance-regular graph hitting time O(n)`; `Biggs resistance distance-regular graph`; `195/101`; and later Markowsky/Koolen random-walk consequences.

Primary later source located:

Greg Markowsky and Jacobus Koolen, **“A Conjecture of Biggs Concerning the Resistance of a Distance-Regular Graph,”** *Electronic Journal of Combinatorics* 17 (2010), #R78, DOI `10.37236/350`, published 25 May 2010. Journal page:

`https://www.combinatorics.org/ojs/index.php/eljc/article/view/v17i1r78`

PDF:

`https://www.combinatorics.org/ojs/index.php/eljc/article/download/350/pdf`

Their Theorem 1 treats every distance-regular graph of valency greater than 2. More decisively for the Aldous–Fill wording, **Proposition 3** states for all vertices `u,v`

`H_uv <= 2(n-1)`

(and `C_uv <= 4(n-1)`). The paper derives this from the proved resistance bound and the commute-time identity.

This is source-exact closure of the first clause of Open Problem 7.31:

- the prior I0031 memo uses `tau_0 = max_{u,v} H_uv`;
- Markowsky–Koolen give `H_uv <= 2(n-1)` uniformly for every distance-regular graph of valency `>2`;
- connected distance-regular graphs of valency `2` are precisely cycles, and the Aldous–Fill source explicitly excludes the `n`-cycles.

Therefore

`tau_0 <= 2(n-1) = O(n)`

throughout the exact source class.

This is stronger than the source's requested big-O statement and was published years before the current campaign. The 14 September memo's proposed sharp-constant question remains a mathematically interesting strengthening, but it is **not** the original source question and cannot justify admitting I0031 as an open successor.

Later-author/citing confirmation: Koolen and Markowsky, **“A collection of results concerning electric resistance and simple random walk on distance-regular graphs,”** *Discrete Mathematics* 339 (2016), 737–744, DOI `10.1016/j.disc.2015.10.012`, explicitly describes strong hitting-time and cover-time consequences of their resistance bounds. This reinforces that the 2010 random-walk consequence is established literature rather than an isolated inference.

Admission verdict:

**I0031 = KNOWN / RESOLVED_IN_LITERATURE for the `tau_0=O(n)` source clause. NOT ELIGIBLE for P20 successor admission.**

Limitation: this verdict is clause-specific. It does not claim that the separate `tau_2=O(log n)` question at the same source location is resolved.

## 4. Current ownership checks immediately beyond the stale queue picture

The newest task-health screen did not list every claim created after older queue snapshots. Direct canonical reads matter:

### I0028 — unavailable

`operations/claims/I0028.md` now exists and records **CLAIMED / HARD OUTSIDE / source-verified**, under a different native slot. Its source is Aldous–Fill Open Problem 6.35. Therefore P20 must not claim I0028 even though older reserve text can make it look pending.

### I0030 — unavailable

I0030 / Aldous–Fill Open Problem 7.30 is active under R05. Current R05 reports prove and extend the frozen arc-MNHD statement, and current P26 activity has independently audited that package. Thus I0030 is occupied, not reserve inventory.

### I0032 — unavailable

`operations/claims/I0032.md` exists and records **Owner: C28; CLAIMED / PENDING_ADMISSION — NOT READY**. Exclusive provisional ownership is enough to bar a competing P20 claim. Its broad `N(s*)=2` Dirichlet-form characterization also has not been certified as a P20 CLOSABLE successor.

These direct current-claim reads supersede stale queue impressions.

## 5. I0033 — cursor advanced, but no fabricated READY promotion

The next exact intake row is I0033, Aldous–Fill Open Problem 14.12, §14.3.3:

> For a sequence of vertex-transitive graphs with `tau_2/tau_0 -> 0`, prove `EC ~ tau_0`.

A direct canonical fetch of `operations/claims/I0033.md` returned 404, so no canonical owner was recovered in this bounded check. However, unowned is not READY. A fresh bounded search located substantial later cover-time/spectral literature, but this run did not complete a source-exact later-author/citing bundle establishing that the exact implication is still open, nor did it recover a genuinely CLOSABLE finite/constant source-matching metric. The target is an asymptotic universal theorem over graph sequences, not a naturally finite short counterexample/constant task on the evidence recovered here.

Admission verdict:

**I0033 = PENDING_CURRENT_STATUS / NOT CERTIFIED CLOSABLE. No claim created.**

This is intentionally conservative. Search failure is not evidence of openness.

## 6. Successor conclusion

No candidate screened in this run is simultaneously:

1. exact-source recovered;
2. freshly current-status checked;
3. not later-literature-resolved;
4. unowned;
5. not POSTED/INDEX-source-exact excluded;
6. genuinely CLOSABLE in the source's own scope; and
7. equipped with one stable source-matching metric.

Accordingly P20 remains

`ROTATION HOLD / SUCCESSOR_ADMISSION_REQUIRED`.

No create-only successor claim is made. This is preferable to claiming I0031 despite its 2010 resolution, racing I0028/I0030/I0032 owners, or relabeling broad I0033 as a closable task without evidence.

## 7. P20 -> P21 audit duty

The newest P21 state recovered in this pass is still the I0004 six-run retirement/handoff and its companion no-new-theorem report. There is no genuinely newer P21 mathematical claim to audit. I therefore create **no audit PASS/receipt** in this run.

## 8. Requested `ledger_delta` for P26 only

P20 does not edit shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md`.

Requested reconciliation for P26:

- `I0031`: change current source status for **Open Problem 7.31 first clause (`tau_0=O(n)`)** from `open_per_source` / PENDING reserve to **KNOWN / RESOLVED_IN_LITERATURE**.
- Evidence: Markowsky–Koolen, EJC 17 (2010) #R78, Proposition 3: `H_uv <= 2(n-1)` for distance-regular graphs of valency `>2`; source excludes cycles, the valency-2 case.
- Preserve the separate `tau_2=O(log n)` clause as separate/unchecked here; do not mark the entire source paragraph solved wholesale.
- Remove I0031 first clause from CLOSABLE successor reserve.
- P20 activity remains `SUCCESSOR_ADMISSION_REQUIRED`; no active successor claim exists after D0010 retirement.
- Admission cursor advanced through current checks of I0028 (claimed), I0030 (occupied by R05), I0031 (literature-resolved), I0032 (claimed by C28), and I0033 (pending current-status / not certified closable).

## 9. Runtime/control and prohibited actions

The exposed task controls still provide no model selector, reasoning-effort selector, authenticated applied-runtime telemetry, or guaranteed-duration field. GPT-6 / maximum therefore remains prompt-requested only. The historical P26 modification denial is not bypassed here; P26 is visibly active in an authorized context.

No Gmail/email, Drive, public posting, paid compute, access changes, peer-file edits, shared-ledger edits, workflow execution, checker-only artifact, or extra schedule was used.

END OF CANONICAL SUCCESSOR-ADMISSION REPORT
