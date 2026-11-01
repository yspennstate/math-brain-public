Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise. NO SOURCE-METRIC MOVEMENT: `7/sqrt(17) -> 7/sqrt(17)`; successor availability `E_ready: 0 -> 0`; methods #10 DERANDOMIZE, #18 SAY IT IN ANOTHER LANGUAGE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R02 CLOSABLE OUTSIDE — SRG69 enters CLOSABLE but owned; exact A17 two-border obstruction

Date: 2026-09-19 UTC. Repository/branch: private `yspennstate/math-open-problems` / `master`.

R02 remains on the post-I0095 successor-admission gate. I did **not** restart the retired six-run I0095 search, reset its stagnation counter, or resume blind enumeration. The fixed source metric remains the explicit order-17 sign matrix with exact discrepancy 7,

\[
\boxed{C^*\ge 7/\sqrt{17}},\qquad \operatorname{disc}(A_{17})^2/17=49/17.
\]

This run produced a new exact **handoff obstruction** extending the preceding one-border theorem: every 19x19 sign matrix obtained by adding two rows and two columns around the retained A17 principal block has discrepancy at most 7. Thus neither one-border nor two-border growth of this exact A17 orbit can improve the normalized source lower bound.

## 1. Continuity and required reads

Continued from

`runs/R02/20260919T1911Z_successor_gate_p0434_owned_a17_one_border_obstruction_6_19_20_e4b91c72.md`

created at commit

`29317ba0f9ceb97f750a85f58f0a561039b6c4f3`.

Freshly read/reconciled this invocation:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical `operations/claims/I0095.md`;
- the newest complete R02 report above;
- newest coordinator status `operations/task_health/runs/2026-09-19T195800Z/status.md`;
- current neighboring R13 report `runs/R13/20260919T1915Z_cylinder188-recovery1-6d2f.md`;
- the newly admitted canonical claim `operations/claims/SHPECTOROV-ZHAO-2026-SRG69.md` and its first owner run;
- the preceding A17 one-border exact checker and matrix;
- current arXiv source/literature sentinels; and
- the complete predecessor-to-prewrite Git delta below.

The append-only intake JSONL corpora were not re-rendered byte-for-byte. The complete Git delta has `too_large=null`; it contains no intake mutation, no root QUEUE/POSTED/RESULTS mutation, and no campaign INDEX/RANKING mutation. Candidate-specific source and ownership files were opened directly.

## 2. Exact predecessor-to-prewrite repository delta

Frozen pre-write master:

`9fa2f9600f0e618e322c029d14c8a55e7b9f9785`.

Exact comparison

`29317ba0f9ceb97f750a85f58f0a561039b6c4f3 .. 9fa2f9600f0e618e322c029d14c8a55e7b9f9785`

returns:

- status `ahead`;
- **98 commits ahead**;
- **0 commits behind**;
- total commits **98**;
- `too_large = null`.

Exactly one canonical `operations/claims/*.md` mutation appears in this complete interval:

1. `operations/claims/SHPECTOROV-ZHAO-2026-SRG69.md` — **added**, status `CLAIMED / ADMITTED_ACTIVE / CLOSABLE OUTSIDE`, owner native slot `6aa7b46f70a8819184095c277974c256`.

Its exact source target is existence/nonexistence of `srg(69,20,7,5)`. The owner already wrote a first mathematical run and moved its own successor gate `E_READY_SUCCESSOR: 0 -> 1`. It is therefore a genuine new CLOSABLE admission but **not free R02 inventory**.

No claim deletion or release occurred in this complete interval. Consequently

\[
\mathcal F_{R02}
=\{\mathrm{FREE}\}\cap\{\mathrm{READY}\}\cap\{\mathrm{CLOSABLE\ OUTSIDE}\}\cap\{\mathrm{CURRENT\ OPEN}\}\cap\{\mathrm{NONRETIRED}\}
=\varnothing,
\]

and R02 successor availability remains `E_ready: 0 -> 0`.

## 3. Current source / literature sentinel

The official arXiv record for `2504.20539` still shows only **v1**, submitted **29 April 2025**. Open Problem 11 remains the exact universal real sign-matrix discrepancy constant target; no later arXiv revision is listed.

Fresh dated search on 2026-09-19 again recovered Akbas--Sra, `arXiv:2609.20785`, *Boolean Small-Ball Inequalities for Discrepancy Theory*, submitted **17 September 2026**. Its advertised results recover Matrix Spencer and Komlos and provide new Boolean small-ball machinery, but they do not state the exact flat real sign-matrix constant of Open Problem 11.

Bounded searches for the new extension statement used variants of `19x19 sign matrix discrepancy 17x17 border`, `bordered Hadamard discrepancy`, and antipodal/covering-code Hamming-annulus formulations. I found no checked primary source stating the exact A17-specific one- or two-border obstruction. This is **bounded negative evidence only**; novelty and priority remain UNVERIFIED.

## 4. Retained exact A17 data

From the preceding exact artifact:

- projective signings checked: `2^16 = 65536`;
- `disc(A17)=7`;
- projective discrepancy-7 minimizers: `21952`;
- singleton-active minimizers: `3780`.

A singleton minimizer `y` has a unique row `i` with

\[
(Ay)_i=7\sigma,
\]

and every other A17 row sum has magnitude at most 5 because all row sums at odd order are odd.

The independent R01 audit of the source witness remains unchanged. This run does not replace or recount that audit.

## 5. Method #18 — SAY IT IN ANOTHER LANGUAGE: the singleton minimizers are a binary code with a thick central annulus

Projectivize both the singleton minimizers `y` and a prospective added row `r` by fixing their seventeenth coordinate to `+1`. Then

\[
r\cdot y=17-2d_H(r,y),
\]

where the Hamming distance is on the first 16 coordinates.

Therefore

\[
|r\cdot y|\le5
\quad\Longleftrightarrow\quad
6\le d_H(r,y)\le11.
\]

For each projective row `r`, define

\[
G(r):=\{y:\ y\text{ is a singleton A17 minimizer and }6\le d_H(r,y)\le11\}.
\]

The exact finite question becomes a coding-theoretic annulus-density problem: how small can `|G(r)|` be over all `2^16` centers?

Outcome #18: the two-border problem is controlled by one exact XOR-convolution profile, not by a search over pairs of rows, columns, or 2x2 corners.

## 6. Method #10 — DERANDOMIZE: every pair of new rows shares many good singleton minimizers

The exact checker computes the complete XOR convolution of

- the indicator of the 3,780 singleton-minimizer masks; and
- the indicator of all 16-bit masks of Hamming weight 6 through 11.

It proves

\[
\boxed{\min_r |G(r)|=3120},\qquad
\max_r |G(r)|=3780.
\]

Only three projective rows attain the minimum. Since

\[
3120>3780/2=1890,
\]

for every pair `r_1,r_2`, inclusion-exclusion gives

\[
|G(r_1)\cap G(r_2)|
\ge3120+3120-3780
=\boxed{2460}>0.
\]

Thus a uniformly random singleton minimizer has uniformly large one-row success probability, but no probability estimate is needed in the theorem: the strict-more-than-half density derandomizes immediately to a deterministic common minimizer for **every pair** of added rows.

Outcome #10: simultaneous control of two arbitrary new rows follows from a one-center exact annulus count and a deterministic pigeonhole argument.

## 7. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: prove a universal two-border no-go instead of searching for an improvement

### Theorem (A17 two-border obstruction; exact finite handoff result)

Let `A=A17` be the retained explicit 17x17 R02 witness. For every

\[
D=
\begin{pmatrix}
A&C\\
R&E
\end{pmatrix}
\in\{\pm1\}^{19\times19},
\]

where `C` is 17x2, `R` is 2x17 and `E` is 2x2,

\[
\boxed{\operatorname{disc}(D)\le7}.
\]

The same conclusion holds after row/column permutations and sign switches of the A17 core.

### Proof

By independently multiplying the two new rows by `-1` if needed, assume both rows of `R` have seventeenth coordinate `+1`. Write them as `r_1,r_2`.

The exact annulus certificate and inclusion-exclusion above give a projective singleton minimizer `y` of A17 such that

\[
|r_1\cdot y|\le5,
\qquad
|r_2\cdot y|\le5.
\]

Let `i` be the unique active A17 row for `y`, and write

\[
(Ay)_i=7\sigma,
\qquad |(Ay)_j|\le5\quad(j\ne i).
\]

Let `c_i\in\{\pm1\}^2` be row `i` of the new-column block `C`. For `t\in\{\pm1\}^2`, the correction `c_i\cdot t` is one of `-2,0,2`. Among the four possible `t`, at least one satisfies

\[
\sigma(c_i\cdot t)\le0.
\]

Choose such a `t` and set `x=(y,t)\in\{\pm1\}^{19}`.

For the unique active top row,

\[
|(Ay)_i+c_i\cdot t|\le7.
\]

For every other old row `j`,

\[
|(Ay)_j+C_j\cdot t|
\le5+2=7.
\]

For the two new rows, each row of `E` has two entries of magnitude one, so

\[
|r_a\cdot y+E_a\cdot t|
\le5+2=7,
\qquad a=1,2.
\]

Hence

\[
\|Dx\|_\infty\le7,
\]

which proves `disc(D)<=7`. Row/column equivalences preserve discrepancy. QED.

Because a 19x19 sign matrix has odd row sums, any order-19 witness that improves the retained normalized value would need discrepancy at least 9. The theorem therefore eliminates **every** two-border extension of this A17 equivalence class as a route to source-metric movement.

Outcome #23: instead of finding one failed extension, the entire two-border family is ruled out exactly.

## 8. Exact artifacts

Idea written before code:

- `artifacts/R02/20260919T2003Z_a17_two_border_obstruction_idea.md`

Exact checker and archived output:

- `artifacts/R02/20260919T2003Z_a17_two_border_obstruction.py`
- `artifacts/R02/20260919T2003Z_a17_two_border_obstruction.out`

The executed exact computation records:

- `A17_discrepancy = 7`;
- `A17_minimizers = 21952`;
- `singleton_minimizers = 3780`;
- annulus masks of weights 6 through 11: `56134`;
- all `65536` projective prospective border rows counted;
- `min_good_singletons_per_border_row = 3120`;
- `max_good_singletons_per_border_row = 3780`;
- minimum attained by `3` projective rows;
- deterministic two-row common-minimizer lower bound `2460`;
- final `PASS`.

This is a **self-check** of the finite core, not an independent audit. The theorem is a handoff result and is not source closure.

## 9. Consequence for future reassignment

The local-growth map is now sharper:

1. one-row/one-column bordering of A17 gives discrepancy at most 6;
2. two-row/two-column bordering of A17 gives discrepancy at most 7;
3. therefore any order-18 or order-19 improvement must alter the 17x17 core, use a genuinely different equivalence orbit, or use the nonlocal antipodal central-shell construction route.

This does **not** authorize restarting I0095 in R02. The source route remains `RETIRED / HANDOFF`; the theorem is preserved so a future reassignment does not waste runs on an exhausted local extension family.

## 10. Neighbor state

R13's newest complete report has no movement in its fixed upper metric:

\[
B_{R13}(86)=7.28139,
\]

and retains its exact finite lower obstruction

\[
K_{86}^*\ge2.264655.
\]

That general unit-column lower bound does not transfer downward to the flat sign-matrix source class. R13 also records that the qualitative real Komlos source has been resolved in current 2026 literature; its remaining work is finite-dimensional quantitative.

The new SRG69 CLOSABLE admission is owned by a different native slot and therefore does not change the R02 gate.

## 11. Model / scheduler-control truth

The task prompt requests GPT-6 with maximum reasoning, but this invocation actually identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The scheduler control surface available here exposes task title/prompt, schedule/timing mode, enabled state and ordinary update fields. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated applied-runtime receipt**. GPT-6/maximum therefore remains prompt-only from this surface. A binding change requires an authorized product/workspace/admin/API scheduler that persists those fields and attests the values actually executed.

The historical P26 `You cannot modify this task` response is authorization-context-specific; later repository evidence records successful P26 prompt reconciliation from an authorized context. The compliant workaround is the task's owning/authorized workspace or platform/admin support for that same task, not duplication or permission bypass. No scheduler mutation was attempted in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R02
  lane: CLOSABLE_OUTSIDE
  active_target: null
  lifecycle: SUCCESSOR_ADMISSION_HOLD
  retired_source: I0095
  source_status: OPEN_PARTIAL
  source_metric_name: greatest certified explicit-matrix lower bound for C*
  source_metric_before: 7/sqrt(17)
  source_metric_after: 7/sqrt(17)
  source_metric_movement: false
  successor_metric_name: E_ready
  successor_before: 0
  successor_after: 0
  newly_seen_closable_claim:
    id: SHPECTOROV-ZHAO-2026-SRG69
    status: CLAIMED_ADMITTED_ACTIVE
    owner: 6aa7b46f70a8819184095c277974c256
    free_for_R02: false
  mathematical_handoff:
    statement: every 19x19 sign matrix containing the retained A17 as a 17x17 principal block has discrepancy at most 7
    exact_min_good_singletons_per_added_row: 3120
    singleton_family_size: 3780
    exact_two_row_common_lower_bound: 2460
    checker_status: SELF_CHECK_PASS
    independent_audit: false
    novelty: UNVERIFIED
  methods: [10, 18, 23]
  next_state: remain on lawful CLOSABLE successor-admission hold; do not restart retired I0095 absent authorized reassignment
```
