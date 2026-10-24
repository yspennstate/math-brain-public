Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. NO SOURCE-METRIC MOVEMENT: certified I0095 lower bound `7/sqrt(17) -> 7/sqrt(17)`; successor availability `E_ready: 0 -> 0`; methods #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #10 DERANDOMIZE, #20 FIND WHY THE ALGORITHM FAILS.**

# R02 CLOSABLE OUTSIDE — R13 weighted projective cover suggests an n=12 lift, but the naive pair-lift has an exact 32-class obstruction

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R02  
Lane: **CLOSABLE OUTSIDE**

## 1. Continuity and lifecycle

I continued from the newest immutable R02 report

`runs/R02/20260919T0608Z_successor_admission_complex_relaxation_two_owned_closable_1_23_25_5d8c2a71.md`

at exact commit

`b9d45fc87dc182aaefc3fddab157d98d903c401f`.

Before doing new work I reconciled the current required control/state surfaces: campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the owner/new-methods directive, canonical `operations/claims/I0095.md`, the newest R02 retirement/handoff state, the newest discrepancy-neighbor R13 report, current task-health/admission evidence, the exact Git delta, and the canonical claim files materially changed in that delta. The complete delta below contains no change to the root queue/results/posted files, campaign INDEX/RANKING, or any `probability_1000_intake_*/problems.jsonl`, so the already reconciled intake cursor is preserved rather than reset from a truncated connector rendering.

Canonical `operations/claims/I0095.md` still says **PENDING_ADMISSION, not READY**. The active R02 I0095 route remains **RETIRED / HANDOFF** after six unchanged CLOSABLE runs. I therefore did not restart blind sign-matrix enumeration. The work below is a fresh transfer diagnostic for the preserved handoff, prompted by genuinely new R13 mathematics; it does not reopen I0095 as an active assignment.

All thirty Section-B labels have already appeared in recovered R02 history, so the literal “never tried before” menu is exhausted. The immediately preceding triple was `#1/#23/#25`. This run uses the nonconsecutive triple `#17/#10/#20` on a genuinely new route and does not falsely label the numbers as first-time uses.

## 2. Frozen source metric remains exactly certified

The owner-fixed source metric is

`L_Cstar := greatest certified lower bound for C* from an explicit sign matrix, retaining exact discrepancy and order`.

The durable witness remains the explicit `17 x 17` sign matrix with exact discrepancy `7`, independently audited by R01 over all `65536` Boolean signings. Hence

\[
L_{C^*}=\frac7{\sqrt{17}}=1.697749375254331\ldots .
\]

Before: `7/sqrt(17)`.  
After: `7/sqrt(17)`.  
**No source-metric movement.**

The operational successor diagnostic remains

`E_ready := # { exact-source, current-open, full-source CLOSABLE OUTSIDE targets that are READY, non-excluded, ownership-clear, and lifecycle-available for R02 }`.

Before: `0`.  
After: `0`.

## 3. Exact predecessor-to-prewrite Git delta

Immediately before this report I froze the prewrite master after the two new R02 exact self-check artifacts at

`a81f66945ef6ce5b502704291ce801ba444b6d42`.

The exact comparison

`b9d45fc87dc182aaefc3fddab157d98d903c401f .. a81f66945ef6ce5b502704291ce801ba444b6d42`

reports **119 commits ahead / 0 behind / `too_large = null`**, so the returned changed-file set is complete for this interval.

Admission-critical claim changes are:

1. `P0411` — new **CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE** source, owner `NM13-05`; its first research report claims exact movement `d_bad: UNMEASURED -> +infinity` for the ideal-cell boundary-distance density theorem. This is active owner-bound work, not free R02 inventory.
2. `P0458` — new **ADMITTED_ACTIVE / CLOSABLE OUTSIDE / PARTIAL** source, owner `R7-03`; its first report already moves the two-regime degree-law metric `2 -> 1`. Again owner-bound at creation.
3. `P0083` and `P0214` — new **HARD OUTSIDE** owner-bound claims.
4. `B-WEAK-EVEN-LOGCONCAVE` — newly claimed by HARD7-01; broad all-dimensional source, HARD-shaped.
5. `GZ-DIMBM-EVEN-LOGCONCAVE` — modified to an explicit **HANDOFF / released after Section-I exhaustion**, but the released full dimensional Brunn--Minkowski source remains **HARD OUTSIDE**, not a CLOSABLE successor.

No CLOSABLE claim was released/reassigned to R02. Root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, and intake JSONL ledgers are absent from the changed-file list. The newest coordinator/admission evidence independently continues to report no newly certified free READY CLOSABLE inventory.

Thus `E_ready=0` survives a real release event: the only fresh explicit release is categorically HARD, while the fresh CLOSABLE admissions were claimed at creation.

## 4. Fresh source/current-literature sentinel

The primary arXiv record `https://arxiv.org/abs/2504.20539` still exposes only `arXiv:2504.20539v1`, submitted **2025-04-29**. The HTML source still states Open Problem 11 as

\[
C^*=\sup_{n\in\mathbb N}\sup_{A\in\{\pm1\}^{n\times n}}
\frac{\operatorname{disc}(A)}{\sqrt n}.
\]

The same source explicitly distinguishes the larger unit-column Komlós class from the sign-matrix class and warns, in its discussion of the then-best Komlós lower construction, that a non-`+/-1` witness does not furnish a Spencer/sign-matrix lower bound. This is exactly the transfer issue encountered below.

A bounded fresh exact-topic search on 2026-09-19 recovered no primary paper claiming the exact value of Open Problem 11. This is bounded negative evidence only, not a worldwide novelty/priority certificate and not permission to reactivate the retired route.

## 5. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: the new R13 number is larger, but lives in the wrong class

The newest complete R13 report proves a new exact six-column **general Boolean Komlós** obstruction. In R13 notation,

\[
K_6^*\ge T_6>
\frac{23066933137}{12500000000}
=1.84535465096,
\]

where `T_6` is an algebraic exact row-`l1` value arising from a six-row mixed-support matrix with unit Euclidean column norms. Its six support/sign rows form an exact partition of the `32` projective Boolean signing classes.

Numerically this looks tempting because

\[
1.84535465096 > \frac7{\sqrt{17}}.
\]

But the admissible classes satisfy

\[
\left\{A/\sqrt n:A\in\{\pm1\}^{n\times n}\right\}
\subset
\left\{M:\|M_{*j}\|_2\le1\right\}.
\]

Therefore, if `C_n` denotes the order-`n` flat sign-matrix constant and `K_n^*` the general unit-column constant,

\[
C_n\le K_n^*.
\]

A **lower bound on the larger supremum** `K_6^*` does not lower-bound the smaller flat subclass `C_6`. R13's number is consequently not source-metric movement for I0095.

The useful part is structural: R13's exact projective partition supplies a concrete weighted cover whose support pattern can be tested as a seed for the preserved `n=12` folded-Hamming covering obstruction.

**Outcome #17:** a promising larger constant was found in the neighboring field, but direct class inclusion has the wrong direction for lower-bound transfer. The only high-value question is whether the weighted partition can be flattened into a genuine sign-matrix cover.

## 6. Method #10 — DERANDOMIZE: explicit pair-lift of the R13 six-row pattern toward the n=12 blocker

The preserved R02 handoff identifies the simplest metric-moving special case as

\[
M_{12}\in\{4,6\},
\]

with `M12=6` equivalent to twelve folded Hamming balls of radius `3` covering

\[
G=\mathbb F_2^{12}/\langle\mathbf1\rangle,
\qquad |G|=2048.
\]

Such a cover would give the explicit sign-matrix lower bound

\[
C^*\ge \frac6{\sqrt{12}}=\sqrt3
>\frac7{\sqrt{17}}.
\]

I tried to turn R13's six weighted projective atoms into a deterministic twelve-bit Hamming construction by replacing each of the six original signing coordinates with a **bit pair**.

The R13 support/sign pattern is

```text
(-,+,0,-,0,-)
(+,0,+,0,+,-)
(0,0,-,+,0,-)
(+,+,0,+,0,+)
(-,0,-,0,+,+)
(-,0,+,+,0,0)
```

For the first natural lift `L_eq`:

- each nonzero coordinate becomes an **equal pair** `++` or `--` carrying the row sign;
- each zero coordinate becomes an arbitrary **unequal pair** `+-` or `-+`;
- global complement is quotiented exactly as in the folded radius-3 formulation.

Allowing every zero-pair orientation gives group sizes

`4,4,8,4,4,8`

and **32 distinct projective candidate centers**. This is deliberately more generous than the desired twelve centers: if even the union of all 32 candidates misses a signing class, then no twelve-center selection from this lift can solve `M12=6`.

I also tested the dual polarity `L_neq`, swapping equal and unequal roles, to make sure a convention choice was not hiding the mechanism.

## 7. Method #20 — FIND WHY THE ALGORITHM FAILS: exact 32-class obstruction

The new exact self-check is

`artifacts/R02/20260919T0712Z_r13_pair_lift_exact_check_9f2c6a41.py`

with archived executed output

`artifacts/R02/20260919T0712Z_r13_pair_lift_exact_check_9f2c6a41.out`.

Artifact creation commits are respectively

`24486efb9a1f08e3680c43973f51be2ffde8c49f`

and

`a81f66945ef6ce5b502704291ce801ba444b6d42`.

The checker uses integer Hamming distances only and exhausts all `2048` projective classes. It returns

`R02_R13_PAIR_LIFT_EXACT_SELF_CHECK_PASS`.

For `L_eq` it proves:

- 32 projective candidate centers;
- exactly **32 of 2048 projective signing classes remain uncovered** even after using all 32 centers;
- every uncovered class has pair-type

`101101`,

meaning that pairs `1,3,4,6` are unequal and pairs `2,5` are equal.

There is also a short structural proof of the radius-3 failure. Let

\[
U=\{1,3,4,6\}
\]

be the unequal-pair set of such a target word, and let `S` be a support of one R13 row. Before any same-type sign/orientation mismatches are even counted, the Hamming distance from the target to the best center with that support is at least

\[
|U\cap S|+|U^c\cap S^c|.
\]

For the six R13 rows these exact floors are

\[
4,4,5,4,4,5.
\]

Hence every `L_eq` center lies at folded Hamming distance at least `4` from every word of pair-type `101101`. Radius `3` can never reach them. There are `64` raw words of this type and therefore exactly `32` projective classes after quotienting by global complement, matching the exhaustive checker.

The swapped lift `L_neq` fails symmetrically: it leaves exactly `32` classes of complementary pair-type

`010010`.

The checker additionally verifies that the **union of both full polarity families**, 64 candidate centers total, covers all 2048 projective classes. This is diagnostically useful but does **not** solve the problem: the source-relevant budget is twelve centers, and I have not produced or certified a twelve-center mixed-polarity subcover. No noncertifying optimizer output is used as mathematical evidence here.

**Outcome #20:** the naive weighted-to-flat transfer fails for an exact, simple reason: a one-polarity pair encoding creates a 32-class off-diagonal synchronization hole. A future flattening theorem must handle these off-diagonal pair states rather than merely approximate the weighted row sums on the diagonal subcube.

This is a new exact **route obstruction / handoff fact**, not a new lower bound for `C^*`, not a source refutation, and not closure.

## 8. What the new obstruction says about a future fresh route

If I0095 is ever explicitly reassigned after its retirement, the R13 bridge should not be retried in the naive form above. A credible transfer would need one of two genuinely new ingredients:

1. a **mixed-polarity synchronization gadget** selecting at most twelve folded centers while covering both off-diagonal pair-type holes; or
2. a proof that any such weighted-projective-cover flattening necessarily needs more than twelve centers, in which case R13's support pattern should be abandoned and a different projective exact-cover type sought.

The key lesson is more precise than “general Komlós does not transfer”: the obstruction is the extra signing freedom created when one weighted coordinate is replaced by multiple Boolean coordinates. The diagonal subcube can inherit the weighted partition, but the off-diagonal pair states are the exact missing obligation.

I do not continue that search in this retired slot without an explicit lifecycle reassignment.

## 9. Scheduler/model-control truth and P26 refusal

The model-control limitation is still true. The exposed scheduling surface provides task title/prompt, schedule or relative-start fields, timing mode, enabled state, and list/update operations. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed-duration field**. `GPT-6 / maximum` therefore remains prompt-only here.

Making GPT-6/maximum enforceable would require an owner-authorized product/workspace/API/admin scheduling surface that persists explicit model-family and reasoning-effort fields into execution routing and returns authenticated per-run attestation.

The historical P26 `You cannot modify this task` result remains an authorization/context boundary. Current repository evidence records a later authorized P26 reconciliation. The lawful workaround for any recurrence is the same task's owning/otherwise-authorized workspace/API/admin context or platform support; do not duplicate the task and do not bypass permissions.

Per the controlling owner restriction, **no scheduler mutation** was made in this run.

## 10. Status

No source-current ownership-clear READY CLOSABLE target became lawful R02 inventory. Therefore:

- `L_Cstar: 7/sqrt(17) -> 7/sqrt(17)`;
- `E_ready: 0 -> 0`;
- R02 remains **CLOSABLE OUTSIDE / SUCCESSOR_ADMISSION_HOLD / NO ACTIVE MATHEMATICAL TARGET**;
- I0095 remains **PENDING_ADMISSION / NOT READY** canonically and **RETIRED / HANDOFF** for active R02 research;
- the R13 six-column lower obstruction is **not** a sign-matrix lower bound;
- the natural pair-lift toward the preserved `M12` covering-code blocker is now exactly ruled out in each one-polarity form by a 32-projective-class hole;
- no source-level claim moved and no paper/audit/closure status is asserted;
- no shared-root file, peer-track file, email, Drive item, public post, purchase, permission, workflow, or scheduler state was changed.

## 11. Structured `ledger_delta`

```yaml
ledger_delta:
  worker: R02
  lane: CLOSABLE_OUTSIDE
  active_target: null
  state_before: SUCCESSOR_ADMISSION_HOLD
  state_after: SUCCESSOR_ADMISSION_HOLD
  retired_source:
    id: I0095
    canonical_state: PENDING_ADMISSION_NOT_READY
    active_lifecycle: RETIRED_HANDOFF
  source_metric:
    name: greatest_certified_explicit_lower_bound_for_Cstar
    witness_order: 17
    witness_discrepancy: 7
    exact_ratio_squared: "49/17"
    before: "7/sqrt(17)"
    after: "7/sqrt(17)"
    moved: false
  admission_diagnostic:
    name: E_ready
    before: 0
    after: 0
    moved: false
  new_transfer_diagnostic:
    source_neighbor: R13_K6_weighted_projective_partition
    general_K6_lower_floor: "23066933137/12500000000"
    direct_sign_matrix_transfer: false
    pair_lift_eq_centers: 32
    pair_lift_eq_uncovered_projective_classes: 32
    pair_lift_eq_obstruction_type: "101101"
    pair_lift_eq_support_distance_floors: [4,4,5,4,4,5]
    pair_lift_neq_centers: 32
    pair_lift_neq_uncovered_projective_classes: 32
    pair_lift_neq_obstruction_type: "010010"
    combined_full_family_centers: 64
    combined_full_family_uncovered: 0
    source_metric_effect: NONE
  methods: [17,10,20]
  exact_self_check: PASS
  outside_audits_new_route_obstruction: 0/2
  predecessor_report: runs/R02/20260919T0608Z_successor_admission_complex_relaxation_two_owned_closable_1_23_25_5d8c2a71.md
  predecessor_commit: b9d45fc87dc182aaefc3fddab157d98d903c401f
  prewrite_master: a81f66945ef6ce5b502704291ce801ba444b6d42
  exact_git_delta:
    ahead: 119
    behind: 0
    too_large: false
  artifacts:
    checker: artifacts/R02/20260919T0712Z_r13_pair_lift_exact_check_9f2c6a41.py
    output: artifacts/R02/20260919T0712Z_r13_pair_lift_exact_check_9f2c6a41.out
  scheduler_changed: false
  shared_roots_changed: false
  peer_files_changed: false
  email_drive_public_posting_permissions_workflows: false
```
