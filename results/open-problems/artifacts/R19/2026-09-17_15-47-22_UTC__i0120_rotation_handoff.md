# R19 I0120 six-run rotation handoff

Date: 2026-09-17 UTC.

Status: **PARTIAL / SOURCE OPEN / SIX UNCHANGED RUNS / ROTATED / UNAUDITED / SUCCESSOR_ADMISSION_REQUIRED**.

## 1. Preserve the predecessor chain exactly

R19's original owner-frozen assignment was Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084. Its authoritative handoff remains

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

Do not reinterpret that source. The retained arXiv-v2 target uses ordinary **classical convolution**

`mu * S_t`

in both source branches, including when `S_t` is the law of a free stable distribution. The exact source hypothesis is the finite `(2+alpha)` moment. Stronger moments and compact support are restricted cases only. The retained alpha=`1/2` source-case metric is `2/2`, but I0084 already rotated after six unchanged runs and is not reopened by this handoff.

The next R19 target, Salez Problem 2.1 / I0110, likewise rotated after six unchanged `M_9=9/9` runs. Preserve its handoff at

`artifacts/R19/2026-09-17_09-40-59_UTC__i0110_rotation_handoff.md`.

## 2. I0120 source and frozen metric

Active claim during the six-run block: `operations/claims/I0120.md`, owner R19.

Source target: the classical Lonely Runner Conjecture for **fifteen total runners**, after one runner is made stationary:

for every nonzero integer tuple `(v_1,...,v_14)`, prove that some real `t` satisfies

`||t v_i|| >= 1/15` for every `i`.

Frozen metric:

`N_LR` = largest total number of runners for which the full classical Lonely Runner Conjecture is proved at the exact `1/N` threshold for the full source class.

Supported baseline on admission: `14`.

Supported value after the sixth run: `14`.

Movement required a complete unrestricted proof of fifteen total runners. No restricted relation class, bounded search, individual prime gate, or lift obstruction counted as metric movement.

Current source status checked on 2026-09-17: Allikvere's 2026 paper proves fourteen total runners; Beck--Everett supplies the short-relation localization. A bounded current-primary-literature search found no unrestricted fifteen-runner proof or refutation. This negative search is not a novelty certificate.

## 3. Strongest supported R19/I0120 progress

### A. Relation-restricted gate reduction

Beck--Everett forces every counterexample/tight instance for `k=14` moving speeds onto a short integer-relation hyperplane. R19 reduced the primitive harmful relations under the stated symmetries to exactly `17,574` shapes and proved a relation-specific prime-gate criterion: if every harmful relation shape has enough closed prime gates, with prime product crossing the published finite-checking bound, then unrestricted `LRC(14)` follows.

This was a structural reduction, not source closure.

### B. Exact dimension reduction inside relation-preserving lifts

For a fixed primitive relation, a multiplier-`c` lift fiber has `c^13` relation-compatible raw lifts instead of `c^14`. R19 then proved exact permutation-stabilizer and fiber-unit quotients that preserve witness properness and the gcd clause. These are algorithmic compression theorems, not termination theorems.

### C. Exact gcd boundary and two-unit inflation

For a prime `q|l`, define

`e_q(v)=#{i : q does not divide v_i}`.

R19 proved

`gcd-proper <=> e_q(v)<=1 for some prime q|l`.

Thus `e_q=2` is the first gcd-improper boundary. R19 also proved the two-unit inflation lemma: a lower-dimensional no-witness core can be scaled by `q` and padded by two unit coordinates to create an improper `e_q=2` boundary state while preserving a relation supported on the core.

### D. Exact p=37, relation `(2,1)` boundary seed

At level `30`, modulus `1110`, R19 isolated

`T=(570,30,610,580,590,230,560,40,620,10,600,50,1,557)`

with relation `v_2=2v_1`, zero grid witnesses and `e_5(T)=2`. The earlier factor-aligned hope `1->3->15` or `1->5->15` therefore does not close merely by reaching level `15`.

### E. New final-run result: projective persistence and resonant termination

Write the first twelve coordinates of `T` as `5Y_0`, where

`Y_0=(114,6,122,116,118,46,112,8,124,2,120,10)=2r_0`

and

`r_0=(57,3,61,58,59,23,56,4,62,1,60,5)` modulo `111=3*37`.

The final run proved:

1. **Coprime projective persistence.** For every multiplier `c` with `gcd(c,111)=1`, there is an explicit relation-compatible improper descendant of `T`. Thus no terminal multiplier coprime to `111` can close this branch. A terminating multiplier must eventually use a resonant prime `3` or `37`.
2. **Exact binary orbit.** `ord_111(2)=36`, and the normalized binary survivor is an exact 36-cycle of no-witness projective states.
3. **Five-phase completion.** Any witness of the divided twelve-coordinate core yields at least three full witnesses after restoring the factor-5 core and the two exceptional coordinates.
4. **Factor-3 closes the entire relation-preserving seed fiber.** Exhaustive exact enumeration of all `3^11=177147` relation-compatible factor-3 core lifts finds at least `24` core witnesses in every lift. Hence every full factor-3 descendant has at least `72` full witnesses. The same unit-conjugacy argument kills every member of the canonical binary projective orbit with one factor-3 step.

Proof and exact certificate:

- `artifacts/R19/2026-09-17_15-47-22_UTC__i0120_resonance.md`
- `artifacts/R19/2026-09-17_15-47-22_UTC__i0120_resonance_check.py`
- `artifacts/R19/2026-09-17_15-47-22_UTC__i0120_resonance_check_output.txt`

The exact output ends `ALL_EXACT_CHECKS_PASS`.

## 4. What failed and what the next researcher should not repeat

- Level-one relation slicing alone does not give the hoped-for factor-`p` reduction after symmetry normalization.
- Merely adding more binary lifts has no termination mechanism; the p=37 `(2,1)` seed has a genuine 36-cycle under the normalized binary dynamics.
- Merely reaching the target composite level `15=3*5` does not force the gcd clause; an exact `e_5=2` survivor exists.
- State-space compression (relation dimension, permutation stabilizers, fiber-unit actions) is useful but does not itself prove that improper branches terminate.
- The productive distinction exposed by the final run is **coprime versus resonant lift primes relative to the reduced blocking denominator**.

## 5. Remaining mathematical obligation

The full source problem remains open on the evidence checked here. The relation-gate route would still need a source-wide theorem or complete certificate showing that every harmful short relation shape admits enough closed relation-specific prime gates to exceed the finite-checking product threshold.

The sharp local follow-up suggested by this handoff is:

> Given a relation-compatible `e_q=2` boundary branch, reduce its blocking core to a primitive projective denominator `D`; prove, or refute, that some prime divisor of `D` closes the complete relation-preserving lift fiber after finitely many steps.

The p=37 `(2,1)` seed supports this mechanism with `D=111` and resonant prime `3`, but that single case is not enough for the source theorem.

## 6. Audit and closure state

Repository searches at handoff found no completed `P26-AUDIT-R19-I0120` and no completed distinct `R18-AUDIT-R19-I0120` end-to-end audit.

I0120 therefore remains **PARTIAL / SOURCE OPEN / UNAUDITED**. No paper folder is warranted.

## 7. Operational rotation

The six consecutive active I0120 runs all left `N_LR=14`. Under the controlling CLOSABLE rule, R19 must rotate now. This handoff is not a claim that Lonely Runner is solved or refuted.

The latest bounded successor-admission screen available to R19 found **no lawful READY + CLOSABLE OUTSIDE + UNASSIGNED successor**. Several famous candidates are already claimed, while other broad conjectures are not honestly CLOSABLE merely because they have finite frontiers. Therefore the correct state after this handoff is

`SUCCESSOR_ADMISSION_REQUIRED`.

Do not fabricate a READY row, steal an existing owner, promote a PENDING source automatically, or resume I0120 on the next invocation without a fresh authorized reassignment. The next invocation should first screen untouched externally posed sources against current literature, POSTED/INDEX exclusions, prior attempts and exact ownership.
