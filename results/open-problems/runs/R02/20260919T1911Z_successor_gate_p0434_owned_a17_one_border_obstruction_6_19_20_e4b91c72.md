Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. NO SOURCE-METRIC MOVEMENT: `7/sqrt(17) -> 7/sqrt(17)`; successor availability `E_ready: 0 -> 0`; methods #6 DEFORM TO A POINT YOU CAN SOLVE, #19 MAKE IT AN ALGORITHM, #20 FIND WHY THE ALGORITHM FAILS.**

# R02 CLOSABLE OUTSIDE — P0434 is new CLOSABLE but owned; exact A17 one-border obstruction

Date: 2026-09-19 UTC. Repository/branch: private `yspennstate/math-open-problems` / `master`.

R02 remains on the post-I0095 successor-admission gate. I did **not** restart the retired I0095 six-run search, reset its stagnation count, or resume blind order-by-order enumeration. The retained source metric remains the explicit order-17 sign matrix with exact discrepancy 7,

\[
C^*\ge \frac7{\sqrt{17}},\qquad \frac{\operatorname{disc}(A_{17})^2}{17}=\frac{49}{17}.
\]

This run nevertheless produced a new exact **handoff obstruction** for a natural route: every 18x18 sign matrix obtained by bordering the retained A17 witness with one row and one column has discrepancy at most 6. This does not move the fixed lower-bound metric and does not reopen the retired source route. It is preserved because it sharply eliminates a plausible deformation strategy.

## 1. Continuity and required reads

I continued from the newest immutable R02 report

`runs/R02/20260919T1810Z_successor_gate_p0157_release_vdh_reassigned_central_shell_29_3_21_d4b7a6c2.md`

created at commit

`826f97ccd6256cf645a944274f06ac4ef559450e`.

Freshly recovered/read for this invocation:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical `operations/claims/I0095.md`;
- the preceding R02 report;
- the newest coordinator status `operations/task_health/runs/2026-09-19T185900Z/status.md`;
- the newest relevant CLOSABLE admission screen `proofnet24/NM13-01/runs/2026-09-19/2026-09-19T19-06-00Z__admission-delta-screen-40-p0434-owned-r11-no-residue0-admission.md`;
- newly created canonical claim `operations/claims/P0434.md`;
- current R13 commit history to check whether neighboring Boolean-Komlos work moved after the preceding R02 checkpoint;
- the retained independent exact A17 audit and its explicit matrix;
- the complete predecessor-to-prewrite Git delta below; and
- fresh public source/literature checks for Randomstrasse Open Problem 11 and the bordering/covering-code route.

The append-only intake corpora are too large to truthfully claim a fresh byte-for-byte rendering of every unchanged historical JSONL row. I do not make that claim. The complete Git comparison below has `too_large = null` and contains no intake-ledger mutation, no root QUEUE/POSTED/RESULTS mutation, and no campaign INDEX/RANKING mutation. Candidate-specific changed claims and lifecycle evidence were reopened directly.

## 2. Exact predecessor-to-prewrite repository delta

Frozen pre-write master:

`7e55da6649bb193c70e1c35fbaf20c0568100a8d`.

Exact comparison

`826f97ccd6256cf645a944274f06ac4ef559450e .. 7e55da6649bb193c70e1c35fbaf20c0568100a8d`

returns:

- status `ahead`;
- **120 commits ahead**;
- **0 commits behind**;
- total commits **120**;
- `too_large = null`, so the returned changed-file set is complete.

There is exactly one canonical `operations/claims/*.md` mutation in this complete interval:

1. `operations/claims/P0434.md` — **added**, owner **R7-04**, status **CLAIMED / ACTIVE**, category **CLOSABLE OUTSIDE**.

The source is the Scully–Harchol-Balter–Scheller-Wolf / Harchol-Balter M-SERPT-vs-Gittins sharp all-load ratio problem: the source lower endpoint is 2, the proved universal upper endpoint is 5, and the conjectured sharp ratio is 2. It is a genuinely attractive CLOSABLE source, but it was claimed at creation by R7-04. It is therefore not free R02 inventory.

No canonical claim deletion occurred. No root QUEUE/POSTED/RESULTS, campaign INDEX/RANKING, or screened intake JSONL mutation occurred. The newest independent NM13-01 admission screen also records P0434 as CLOSABLE but owned and finds no lawful new admission. The coordinator independently still records zero newly source-current, ownership-clear, free CLOSABLE admissions.

Therefore

\[
\mathcal F_{R02}
=\{\mathrm{FREE}\}\cap\{\mathrm{READY}\}\cap\{\mathrm{CLOSABLE\ OUTSIDE}\}\cap\{\mathrm{CURRENT\ OPEN}\}\cap\{\mathrm{NONRETIRED}\}
=\varnothing,
\]

and `E_ready: 0 -> 0`.

The only R02 files added before this final report are the substantive checker and archived output described below. They are not successor claims and do not alter the source metric.

## 3. Source and current-literature sentinel

The official arXiv record for `2504.20539` still exposes only **v1**, submitted **29 April 2025**. The HTML source continues to state Open Problem 11 as

\[
\sup_n\sup_{A\in\{\pm1\}^{n\times n}}\frac{\operatorname{disc}(A)}{\sqrt n}
\]

and Conjecture 12 as the claim that the corresponding limsup is strictly larger than 1. The source also records that the Sylvester-Hadamard Conjecture 13 was subsequently falsified through the Boolean-function connection; this does not settle Open Problem 11 or Conjecture 12.

Fresh dated searches on 2026-09-19 for the exact sign-matrix constant and nearby discrepancy work again recovered Akbas–Sra, `arXiv:2609.20785`, *Boolean Small-Ball Inequalities for Discrepancy Theory* (submitted 17 September 2026). Its advertised results provide Boolean small-ball machinery and recover Matrix Spencer and Komlos, but they do not state the exact flat real sign-matrix constant of Open Problem 11.

For the new bordering lemma, bounded searches used variants of `bordered sign matrix discrepancy`, `principal submatrix sign matrix discrepancy border`, and `antipodal covering radius 2n n/2 sqrt n`. They recovered general bordered-Hadamard and covering-radius literature, but no checked primary source stating the exact A17-specific obstruction below. This is **bounded negative evidence only**. I make no worldwide novelty or priority claim for the lemma.

## 4. Retained exact A17 certificate

The independent R01 audit fixes the last signing coordinate to +1, exhausts all `2^16 = 65536` projective signings, and returns

- `discrepancy = 7`;
- `argmask = 430`;
- `ratio_squared = 49/17`;
- `PASS`.

The retained explicit matrix is the same 17x17 A17 already archived in the R02 and R01 exact checkers. No part of the present run changes that certificate.

Thus the fixed source metric remains

\[
\boxed{C^*\ge 7/\sqrt{17}}.
\]

## 5. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: border the order-17 extremal witness to order 18

At order 18, every row sum against a sign vector is even. To improve the current normalized lower witness, an 18x18 matrix would therefore need discrepancy at least 8, since

\[
\frac{8}{\sqrt{18}}>\frac7{\sqrt{17}}.
\]

The most direct deformation is to keep the certified A17 core and add one row and one column:

\[
D=\begin{pmatrix}A&c\\ r^T&d\end{pmatrix},
\qquad c,r\in\{\pm1\}^{17},\ d\in\{\pm1\}.
\]

A naive search over `(c,r,d)` is unnecessary. The active-set geometry of the exact A17 minimizers almost completely decides the route.

Exact enumeration of all projective A17 signings gives:

\[
\operatorname{disc}(A)=7,
\]

with **21,952** projective minimizers. If `S(y)={i: |(Ay)_i|=7}`, the active-set-size distribution is

\[
|S(y)|=1:3780,\quad
2:14364,\quad
3:3264,\quad
4:480,\quad
5:64.
\]

The **3,780 singleton minimizers** are the decisive obstruction.

Outcome #6: the order-18 border deformation is not merely unsuccessful in sampled choices; it can be ruled out for every possible added row, column and corner entry.

## 6. Method #19 — MAKE IT AN ALGORITHM: replace the full border search by an exact middle-layer hitting test

Let `y` be an A17 minimizer with a unique active row `i`, so

\[
|(Ay)_i|=7,\qquad |(Ay)_j|\le5\quad(j\ne i).
\]

The second inequality is automatic because all row sums of a 17-entry sign matrix are odd.

For a prospective border column `c`, choosing

\[
t=-c_i\,\operatorname{sgn}((Ay)_i)
\]

makes the active top coordinate exactly 6, while every other top coordinate is at most 6 after the `\pm1` perturbation from the new column.

Thus the only remaining question is whether, for each prospective bottom row `r`, one can find such a singleton minimizer with small `r\cdot y`.

Row-sign symmetry lets us fix `r_{17}=+1`. The same projective convention already fixes `y_{17}=+1`. If the corresponding first-16 bit masks differ in exactly 8 positions, then

\[
r\cdot y=17-2\cdot8=1.
\]

So the entire `2^35`-scale border search collapses to the finite question:

> Do the 3,780 singleton-minimizer masks hit every one of the `2^16` projective bottom-row masks at Hamming distance exactly 8?

The exact checker answers **YES**. It generates all `\binom{16}{8}=12,870` middle-layer masks, translates that layer around every singleton minimizer, and marks all **65,536** projective bottom-row masks. Uncovered count is **0**.

Outcome #19: the border question admits a small exact certificate based on a middle-layer hitting property of the singleton minimizers; there is no reason to enumerate columns `c` or corner bits `d` at all.

## 7. Method #20 — FIND WHY THE ALGORITHM FAILS: a universal one-border obstruction

### Lemma (A17 one-border obstruction; exact finite handoff result)

Let `A` be the retained explicit 17x17 R02 matrix. For every

\[
D=\begin{pmatrix}A&c\\r^T&d\end{pmatrix}\in\{\pm1\}^{18\times18},
\]

we have

\[
\operatorname{disc}(D)\le6.
\]

The same conclusion holds if the upper-left principal block is obtained from `A` by row/column permutations and row/column sign switches.

### Proof

Multiplying the last row of `D` by `-1` if necessary does not change discrepancy, so assume `r_{17}=+1`.

The exact finite certificate proves that there is a projective singleton minimizer `y\in\{\pm1\}^{17}` with `y_{17}=+1` such that

\[
r\cdot y=1.
\]

Let `i` be the unique active A17 row for this `y`, and write

\[
\sigma=\operatorname{sgn}((Ay)_i).
\]

Then

\[
(Ay)_i=7\sigma,
\qquad |(Ay)_j|\le5\quad(j\ne i).
\]

Choose the eighteenth signing coordinate

\[
t=-c_i\sigma.
\]

For the active top row,

\[
|(Ay)_i+t c_i|=|7\sigma-\sigma|=6.
\]

For every other top row,

\[
|(Ay)_j+t c_j|\le |(Ay)_j|+1\le6.
\]

Finally, the bottom row satisfies

\[
|r\cdot y+d t|=|1+d t|\le2.
\]

Thus the 18-sign vector `x=(y,t)` obeys

\[
\|Dx\|_\infty\le6,
\]

so `disc(D)<=6`. Row/column equivalences preserve discrepancy, giving the final statement. QED.

This is much stronger than the original failure target `disc(D)<8`: **every direct one-row/one-column border of the best retained order-17 witness collapses to discrepancy at most 6**.

The conceptual reason is that A17's singleton deep holes form an exact middle-layer hitting family for every prospective new row. The extra signing bit can always cancel the unique `7`, while the new bottom row is simultaneously forced down to at most 2.

Outcome #20: the obvious local-growth algorithm is structurally impossible. Any order-18 improvement must change entries inside the 17x17 core, not merely border an A17-equivalent core.

## 8. Exact checker and archived output

Substantive finite artifacts created and executed this run:

- `artifacts/R02/20260919T1910Z_a17_one_border_obstruction.py`
- `artifacts/R02/20260919T1910Z_a17_one_border_obstruction.out`

The archived output records:

- projective signings checked: `65536`;
- A17 discrepancy: `7`;
- A17 projective minimizers: `21952`;
- active-set histogram `{1:3780, 2:14364, 3:3264, 4:480, 5:64}`;
- singleton minimizers: `3780`;
- exact distance-8 masks: `12870`;
- projective bottom rows covered at dot product `1`: `65536`;
- uncovered bottom rows: `0`;
- final result: `PASS`.

This is a self-check for the finite core. It is **not** an independent audit and does not count toward source closure.

## 9. What this changes and what it does not

It changes the research map in one useful way:

- **do not try to extend the certified A17 witness to order 18 by a single border**; that entire strategy has exact upper bound 6.

It does **not** change any of the following:

- source metric: still `7/sqrt(17)`;
- source status: Open Problem 11 remains OPEN/PARTIAL in this repository context;
- canonical I0095 admission status: still `PENDING_ADMISSION, not READY`;
- operational R02 I0095 route: still `RETIRED / HANDOFF` after six unchanged CLOSABLE runs;
- successor pool: still empty;
- audit count for the source: unchanged;
- novelty status of the one-border lemma: UNVERIFIED.

The natural next handoff directions are therefore nonlocal: mutate the A17 core before bordering, search a different order-18 orbit from scratch, or return to the central-shell antipodal-code formulation from the preceding report and seek a scalable family. None is activated here because the source route remains retired and no lawful successor has been admitted.

## 10. Neighbor state

No new R13 report commit appeared after the preceding R02 checkpoint. I therefore do not recycle an older Boolean-Komlos numerical movement as if it were fresh progress. General unit-column Komlos bounds still do not transfer downward to an explicit flat sign-matrix lower witness.

The newest coordinator status records five enabled CLOSABLE successor gates with no admitted current target. The newly added P0434 source is already owned by R7-04, so it does not relieve the R02 gate.

## 11. Scheduler/model-control truth

The prompt requests GPT-6 with maximum reasoning, but this invocation actually identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so reasoning is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or a guaranteed hour-long execution.

The exposed scheduler control surface provides task identity/title, prompt, schedule/timing mode, enabled state, and ordinary update controls. It exposes **no binding model-family selector, no binding reasoning-effort selector, no guaranteed-duration field, and no authenticated applied-runtime model/effort receipt**. Making GPT-6/maximum enforceable requires an owner-authorized product/workspace/admin/API scheduling surface that persists those fields into inference routing and returns per-run attestation.

The historical P26 `You cannot modify this task` event is authorization-context-specific: repository evidence records a later successful full P26 update from an authorized context. The compliant workaround for any denied task is the same task through its owning/authorized product/workspace/admin/API context or platform support. It is not duplication, identity substitution, or permission bypass.

No scheduler, prompt, permission, credential, public posting, email, Drive, workflow, or access mutation was attempted this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R02
  lane: CLOSABLE_OUTSIDE
  source: I0095
  source_metric:
    name: greatest_certified_explicit_sign_matrix_lower_bound_for_C_star
    before: "7/sqrt(17)"
    after: "7/sqrt(17)"
    movement: false
    retained_order: 17
    retained_discrepancy: 7
    ratio_squared: "49/17"
  operational_status:
    before: SUCCESSOR_ADMISSION_HOLD
    after: SUCCESSOR_ADMISSION_HOLD
  i0095_route:
    canonical_claim_status: "PENDING_ADMISSION, not READY"
    operational_status: "RETIRED / HANDOFF"
    lifecycle_reset: false
  successor_availability:
    before: 0
    after: 0
    newly_seen_closable_claims:
      - id: P0434
        category: CLOSABLE_OUTSIDE
        owner: R7-04
        status: CLAIMED_ACTIVE
        selectable_by_R02: false
  repository_delta:
    predecessor_R02_commit: "826f97ccd6256cf645a944274f06ac4ef559450e"
    frozen_prewrite_master: "7e55da6649bb193c70e1c35fbaf20c0568100a8d"
    commits_ahead: 120
    commits_behind: 0
    too_large: null
    canonical_claim_mutations:
      - "operations/claims/P0434.md: added; R7-04; CLAIMED/ACTIVE; CLOSABLE OUTSIDE"
  new_handoff_result:
    statement: "Every 18x18 sign matrix with the retained A17 as an upper-left principal block has discrepancy <= 6."
    source_metric_movement: false
    novelty: UNVERIFIED
    proof_on_page: true
    finite_core_self_check: PASS
    artifacts:
      - "artifacts/R02/20260919T1910Z_a17_one_border_obstruction.py"
      - "artifacts/R02/20260919T1910Z_a17_one_border_obstruction.out"
    exact_counts:
      A17_projective_minimizers: 21952
      singleton_minimizers: 3780
      distance8_masks: 12870
      prospective_projective_bottom_rows_covered: 65536
      prospective_projective_bottom_rows_uncovered: 0
  methods:
    - "6 DEFORM TO A POINT YOU CAN SOLVE"
    - "19 MAKE IT AN ALGORITHM"
    - "20 FIND WHY THE ALGORITHM FAILS"
  checker_created: true
  checker_executed: true
  checker_output_archived: true
  independent_audit_new: false
  shared_root_edits: false
  peer_file_edits: false
  scheduler_edits: false
```

## 13. Final disposition

**R02 remains `CLOSABLE OUTSIDE / SUCCESSOR_ADMISSION_HOLD / NO ACTIVE MATHEMATICAL TARGET`.**

The source metric is unchanged at

\[
\boxed{C^*\ge 7/\sqrt{17}}.
\]

The substantive new information is the exact route obstruction

\[
\boxed{\text{every one-row/one-column border of the retained A17 has discrepancy at most }6.}
\]

So future work should not spend another run searching that border family. The source itself remains unclosed, and P0434, although newly admitted as CLOSABLE, is already owned by R7-04.
