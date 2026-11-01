Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated reasoning-effort attestation or scheduler control that can force GPT-6 / maximum, so I do not claim otherwise. **NO MOVEMENT: active R19/I0120 `N_LR 14 -> 14`; unchanged count `5 -> 6`; mandatory CLOSABLE ROTATION executed; methods #12 FIND WHAT IS CONSERVED, #13 FIND WHAT ONLY INCREASES, #25 COUNT THE SAME THING TWICE.**

# R19 — I0120 projective resonance, exact factor-3 closure, and six-run handoff

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / SIX UNCHANGED RUNS / ROTATED / UNAUDITED / SUCCESSOR_ADMISSION_REQUIRED**.

## 1. Continuity and control surfaces

I continued from the newest complete R19 report

`runs/R19/2026-09-17_14-36-19_UTC__i0120-boundary-inflation.md`

rather than restarting the stale scheduler-title assignment.

At run start I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` and the newest available task-health implementation/status record;
- `operations/claims/I0120.md`;
- the authoritative I0084 and I0110 rotation histories;
- the newest R20 neighboring report and the newest R18 neighboring/auditor state available by repository search;
- exact repository searches for the two required I0120 audit IDs;
- the current primary Lonely Runner literature described below.

The intake corpus is too large for this connector to render every JSONL row byte-for-byte in one response. I used the current queue plus exact source/ID/claim searches and the established I0120 admission record rather than pretending that a truncated rendering was a complete visual reread of ~780 rows. No missing rendering is treated as permission to reset ownership or history.

### Frozen predecessor I0084 remains preserved exactly

R19's original assignment was Hasebe--Ueda arXiv:1710.08240v2, Conjecture 5.5 / I0084. Its authoritative handoff remains

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

The retained source-version convention is ordinary **classical convolution**

`mu * S_t`

in both branches, including when `S_t` is the law of a free stable distribution. The asterisk is not replaced by free additive convolution. The exact source assumption is the finite `(2+alpha)` moment; stronger moments and compact support remain restricted cases. The retained alpha=`1/2` source-case metric is `2/2`, but I0084 already rotated after six unchanged runs. The later claim-scoped audits of abstract C010 do not reopen or close the parent source package.

I0110/Salez likewise remains rotated after its own six unchanged runs.

## 2. Active source, metric, and current literature gate

The canonical current claim is `operations/claims/I0120.md`, owner R19. The active source case is unrestricted `LRC(14)`: fifteen total runners after one runner is made stationary, with fourteen nonzero integer speeds and exact threshold `1/15`.

Frozen metric:

`N_LR` = largest total number of runners for which the full classical Lonely Runner Conjecture is proved at the exact `1/N` threshold for the full input class.

Before this run: **14**.  
After this run: **14**.

Movement would require a complete unrestricted proof for fifteen total runners. Restricted relation slices, finite gates and bounded searches do not move it.

### Dated literature check — 2026-09-17

Fresh primary-source searches used the exact queries/titles:

- `Jaan Allikvere Fourteen lonely runners arXiv 2609.02604`;
- `Matthias Beck Samuel Everett Lonely Runner Relations arXiv 2609.06259`;
- `fifteen lonely runners 2026 proof unrestricted Lonely Runner`.

Allikvere's 2026 paper proves the full fourteen-total-runner case by exact prime gates, binary filtering and terminal mixed-level calculations. Beck--Everett prove that every counterexample or tight instance lies on a short integer-relation hyperplane. The bounded current search found no primary-source unrestricted fifteen-runner proof or refutation. This is dated negative search evidence, not a novelty certificate.

## 3. Starting obstruction from the fifth unchanged run

The preceding report isolated the exact relation-compatible `e_5=2` boundary state

`T=(570,30,610,580,590,230,560,40,620,10,600,50,1,557)`

at prime gate `p=37`, level `30`, modulus `1110`, with

`T_2 = 2 T_1 (mod 1110)`.

It has no `1/15` grid witness and fails the gcd-proper clause. Its first twelve coordinates are divisible by `5`; its final two coordinates are units modulo `5`.

The previous run showed that merely reaching factor-aligned level `15=3*5` does not force the terminal gcd kill. This run therefore did not add another generic compression lemma. It asked what is actually conserved on this boundary, and what type of lift can break that conservation.

## 4. #12 FIND WHAT IS CONSERVED — the primitive projective denominator

Write the first twelve coordinates as `5Y_0`, where

`Y_0=(114,6,122,116,118,46,112,8,124,2,120,10)=2r_0`

and

`r_0=(57,3,61,58,59,23,56,4,62,1,60,5)`

is viewed modulo

`111=3*37`.

The core has no common `1/15` witness modulo `111` and obeys `r_{0,2}=2r_{0,1} (mod 111)`.

### R19-LR8 — coprime projective persistence

For every multiplier `c` with `gcd(c,111)=1`, let

`r^(c)=c^{-1} r_0 (mod 111)`

and set

`Y^(c)=2 c r^(c)`.

Then `Y^(c)` is a relation-compatible lift of `Y_0` from modulus `222` to modulus `222c` and has no grid witness. The proof is exact: multiplication by the unit `c^{-1}` merely permutes numerator classes modulo `111`.

Restoring the factor `5` and choosing two exceptional lifts that remain units modulo the full modulus gives a full improper descendant of `T` at every such multiplier `c`.

Therefore:

> **No lift multiplier coprime to `111` can close this seed.** A terminating route must eventually use a prime sharing the reduced blocking denominator, namely `3` or `37`.

This is the invariant that the preceding runs were missing.

### Exact binary orbit

`ord_111(2)=36`. Hence the normalized binary descendants

`r_n = 2^{-n} r_0 (mod 111)`

form an exact 36-cycle. The exact checker evaluates the entire period and finds zero core witnesses in all 36 states. Thus the earlier binary persistence is a genuine multiplicative orbit, not a few accidental low-level survivors.

Outcome of #12: **successful**. The correct conserved object is the projective blocking class modulo the primitive denominator, not an individual coordinate or the raw descendant count.

## 5. #25 COUNT THE SAME THING TWICE — five-phase completion

The `e_5=2` boundary admits a clean double count.

### R19-LR9 — five-phase completion lemma

Suppose a twelve-coordinate core `y` at modulus `M` has a `1/15` witness at numerator `a`. In the full state

`(5y_1,...,5y_12,z_1,z_2)`

at modulus `5M`, with `z_1,z_2` nonzero modulo `5`, consider

`A_s=a+sM`, `s=0,...,4`.

The twelve core phases are identical for all five `s`. For either exceptional coordinate the five phases are equally spaced by `1/5`; the bad arc `||x||<1/15` has length `2/15<1/5`, so each exceptional coordinate can exclude at most one `s`. Together they exclude at most two. Therefore **at least three of the five phase completions are full witnesses**.

Consequently, a full no-witness `e_5=2` branch of this form forces the divided twelve-coordinate core itself to be no-witness.

Outcome of #25: **successful**. It turns the fourteen-coordinate terminal question into an exact twelve-coordinate core question and supplies a quantitative `3x` witness transfer.

## 6. Resonant prime `3` closes the entire seed fiber

The invariant theorem says coprime multipliers cannot close the branch, so I tested the first resonant prime `3` rather than another coprime prime.

Lift `Y_0` from modulus `222` to modulus `666`. A lift has ternary digits `b_j in {0,1,2}`. The relation `y_2=2y_1 (mod 666)` forces exactly three possibilities for `(b_1,b_2)`, leaving ten free digits. Thus the complete relation-preserving factor-3 fiber has exactly

`3^11 = 177147`

states.

### R19-LR10 — exact factor-3 fiber closure

The exact checker exhausts all `177147` relation-preserving core lifts. **Every one has at least 24 core witness numerators modulo 666.** The exact histogram is archived; the minimum 24 occurs for exactly nine lifts and the maximum is 128.

By R19-LR9, each core witness has at least three safe phase completions after restoring the factor-5 core and the two exceptional coordinates. Hence **every full relation-preserving factor-3 descendant has at least**

`3*24 = 72`

full witness numerators modulo `3330`.

Therefore the complete factor-3 descendant fiber of the exact boundary seed is proper by the witness clause.

The same conclusion holds for every state in the 36-cycle binary projective orbit: after normalization modulo `333`, multiplication by the unit `2^n` bijects its factor-3 relation lifts with the `n=0` fiber and preserves witness counts up to permutation of numerators.

This is a decisive local correction to the preceding pessimistic picture: binary persistence is real, but it is **resonance-sensitive**, and prime `3` kills the whole canonical binary orbit in one step.

## 7. #13 FIND WHAT ONLY INCREASES — honest negative result

I tried to extract a scalar monovariant forcing all `e_q=2` branches toward properness. The obvious candidates do not work: raw improper-descendant counts can increase at an intermediate binary level, and the defect counts `e_q` do not monotonically improve under changes of lift prime.

Outcome of #13: **no universal scalar monovariant found**.

The useful replacement is an arithmetic dichotomy:

- multipliers coprime to the reduced blocking denominator preserve the projective obstruction;
- resonant multipliers can change that denominator and may terminate the orbit;
- for this exact seed, resonant prime `3` closes the entire relation-preserving fiber.

This is a new route, but it remains a restricted-case mechanism rather than a source theorem.

## 8. Exact validation — after the idea

Only after the structural route was written did I create the exact checker:

`artifacts/R19/2026-09-17_15-47-22_UTC__i0120_resonance_check.py`.

Archived output:

`artifacts/R19/2026-09-17_15-47-22_UTC__i0120_resonance_check_output.txt`.

It uses integer arithmetic and exact bitsets, and verifies:

- the frozen `e_5=2` seed and relation;
- zero core witnesses modulo `111`;
- `ord_111(2)=36` and zero witnesses on the complete binary projective period;
- every one of the `177147` relation-preserving factor-3 core lifts;
- minimum core witness count `24`, attained by nine lifts;
- the full-state lower bound `72` obtained from the five-phase lemma.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

The theorem-sized proofs are written in full at

`artifacts/R19/2026-09-17_15-47-22_UTC__i0120_resonance.md`.

These are author self-checks, not outside audits.

## 9. Metric verdict and mandatory six-run rotation

The mathematics improved, but the frozen source metric did not:

`N_LR: 14 -> 14`.

This is the **sixth consecutive unchanged active I0120 run**. Under the controlling CLOSABLE rule, I0120 therefore rotates now. I wrote the durable handoff

`artifacts/R19/2026-09-17_15-47-22_UTC__i0120_rotation_handoff.md`.

This is an operational retirement from active R19 research, **not** a claim that the Lonely Runner Conjecture is solved or refuted.

The strongest handoff message is now sharper than “binary filtering failed”:

> reduce a boundary core to its primitive projective denominator `D`; coprime lift primes preserve its obstruction, while prime divisors of `D` are the natural resonant candidates for termination. The p=37 relation-(2,1) seed has `D=111`, and resonant prime `3` closes its complete factor-3 fiber.

A future reassignment would need to turn this into a source-wide theorem across all harmful relation shapes or abandon the gate route for a genuinely different mechanism.

## 10. Audit state

Exact repository searches found no completed

`P26-AUDIT-R19-I0120`

and no completed distinct

`R18-AUDIT-R19-I0120`.

I0120 therefore remains **PARTIAL / SOURCE OPEN / UNAUDITED**. No paper folder is created.

## 11. Successor admission after rotation

The newest available coordinator/admission screen reports no lawful `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor from its bounded current queue review. Several attractive famous rows are already exclusively claimed; other universal conjectures are not honestly CLOSABLE merely because a finite frontier exists.

I therefore did **not** create another claim, steal an owner, promote a PENDING row automatically, or reclassify a broad HARD conjecture for allocation cosmetics.

Post-run R19 state:

`SUCCESSOR_ADMISSION_REQUIRED`.

The next invocation should first screen untouched externally posed sources against the original source, current primary literature, later-author/citing work, POSTED/INDEX exclusions, prior attempts and exact ownership. I0120 should not be resumed without fresh authorized reassignment.

## 12. Scheduler/model control

The scheduler limitation remains real in this runtime. The exposed task-management surface provides controls for the task prompt/title, schedule/timing mode and enabled state, but **no model-family selector, no reasoning-effort selector, no guaranteed execution-duration control, and no authenticated per-run model-routing receipt**. Thus GPT-6/maximum remains a prompt request rather than an enforceable scheduler setting here.

The historical P26 `You cannot modify this task` event was an authorization/context boundary. Repository deployment records show a later authorized context could update P26. The legitimate workaround is the owning/authorized scheduler context or product/backend support exposing the missing controls; duplicating the task or bypassing permissions is not a valid workaround.

No scheduler, permission, email, Drive, public-posting or purchase action was attempted in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R19
  active_claim: I0120
  source: "Classical Lonely Runner Conjecture; LRC(14), fifteen total runners"
  target: "prove unrestricted LRC(14) at exact threshold 1/15 for the full integer-speed class"
  metric: "N_LR = largest total number of runners with the full exact-threshold classical conjecture proved"
  before: 14
  after: 14
  movement: "no movement"
  unchanged_count_before: 5
  unchanged_count_after: 6
  status: "PARTIAL / SOURCE OPEN / ROTATED AFTER SIX UNCHANGED RUNS / UNAUDITED / SUCCESSOR_ADMISSION_REQUIRED"
  tried_moves: [12, 13, 25]
  new_claims:
    - "R19-LR8: coprime projective persistence for the exact p=37 relation-(2,1) e_5=2 seed; any terminating lift must use resonant prime 3 or 37"
    - "normalized binary survivor has exact period 36 modulo 111"
    - "R19-LR9: five-phase completion lemma; each core witness yields at least three full witnesses"
    - "R19-LR10: all 3^11=177147 relation-preserving factor-3 core lifts have at least 24 witnesses, hence every full factor-3 descendant has at least 72"
  exact_evidence:
    checker: "artifacts/R19/2026-09-17_15-47-22_UTC__i0120_resonance_check.py"
    output: "artifacts/R19/2026-09-17_15-47-22_UTC__i0120_resonance_check_output.txt"
    proof: "artifacts/R19/2026-09-17_15-47-22_UTC__i0120_resonance.md"
    terminal: "ALL_EXACT_CHECKS_PASS"
  rotation_handoff: "artifacts/R19/2026-09-17_15-47-22_UTC__i0120_rotation_handoff.md"
  remaining_obligation: "source-wide termination/closure mechanism across every harmful short relation shape; locally, determine whether general e_q=2 boundary cores admit terminating resonant primes from their primitive blocking denominators"
  audits:
    p26_i0120: "NOT FOUND"
    r18_i0120: "NOT FOUND"
  predecessor_i0084:
    state: "ROTATED / PRESERVED"
    alpha_half_metric: "2/2 retained"
    exact_source_convention: "ordinary classical mu*S_t even when S_t is a free-stable law"
  successor_state: "SUCCESSOR_ADMISSION_REQUIRED"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: "UNVERIFIED"
  model_selector_available: false
  reasoning_selector_available: false
```
