Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-01 admission record — E0057 source/current-scope resolution

Date of literature/source check: 2026-09-19 UTC
Slot: `R7-01`
Native ID: `6aabe777361481919c9e614646464772`
Root: `research7_2026-09-17/R7-01/`
Pre-write master snapshot: `c07094c475a5a53a9d5f0657e66e924be6dc17e3`
Candidate: `E0057`
Disposition: **KNOWN / RESOLVED IN LITERATURE / NOT_ADMITTED**
Claim created: **no**

## 1. Exact shard check

The initial R7-01 gate is the exact case-sensitive quantity

`sum(ord(c) for c in canonical_id) mod 7`.

For `E0057`,

`ord('E')+ord('0')+ord('0')+ord('5')+ord('7') = 69+48+48+53+55 = 273`,

and `273 mod 7 = 0`. Thus E0057 is a genuine shard-zero intake candidate. This is only a partition fact, not an ownership or openness claim.

## 2. Exact outside source and literal scope

Outside source: Afonso S. Bandeira, course notes for MIT 18.S096, *Topics in Mathematics of Data Science* / the 2015 “42 Open Problems” material, Fall 2015.

Exact item: Open Problem 10.4, “Consistency and Sample Complexity of Multireference Alignment.” The current MIT OpenCourseWare standalone source is:

https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-of-data-science-fall-2015/227203dea1424fbb785eff1d3d7d6d68_MIT18_S096F15_Open10.4.pdf

The repository intake locates this as PDF p. 139. The standalone OCW extraction puts the problem on its first page.

The source has two numbered obligations:

1. determine whether the quasi-MLE “(or the MLE)” is consistent for multireference alignment, after the stated power-spectrum correction; and
2. determine the observation/sample complexity as a function of fixed signal length `L` and noise level `sigma` for accurate MRA recovery.

The parenthetical `or the MLE` matters for exact scope. The literal source offers MLE consistency as an alternative acceptable branch; it does not say that both quasi-MLE and MLE consistency must be proved simultaneously.

## 3. Intake state and recovered repository history

The current intake row is `probability_1000_intake_E_20260908/problems.jsonl`, E0057. It records part (2) as answered by Perry–Weed–Bandeira–Rigollet–Singer but retained the row because, as of the 2026-09-08 search, no resolution of part (1) had been found.

A neighboring later screen, `proofnet24/NM13-07/runs/2026-09-17/2026-09-17T22-30-03Z__admission-screen-2.md`, already recovered Abbe–Pereira–Singer and correctly observed that the **MLE branch** is covered. That neighboring report conservatively left a possible quasi-MLE residual as `PENDING_SOURCE_CURRENT`.

The present R7-01 reconciliation tightens only the source-scope logic: because Open Problem 10.4 itself says quasi-MLE **or** MLE, the surviving quasi-MLE-only question is a strengthened residual, not a reason to call the literal source item open after the MLE alternative has been proved.

Current master has no `operations/claims/E0057.md` file. Absence of a claim is not used as openness evidence.

## 4. Current primary literature check

### 4.1 MLE consistency

Emmanuel Abbe, João M. Pereira and Amit Singer, *Estimation in the group action channel*, arXiv:1801.04366 (2018); ISIT 2018.

Primary source:
https://arxiv.org/abs/1801.04366

The paper's model contains one-dimensional MRA as the compact cyclic-shift special case. Its Theorem II.2 proves that the marginalized maximum-likelihood estimator converges in probability to the true signal orbit when

`N / sigma^(2 d_bar) -> infinity`,

where `d_bar` is the moment-order cutoff separating the true orbit from alternatives. In particular, at fixed finite `L` and fixed finite `sigma`, the MRA MLE is consistent as `N -> infinity` whenever the orbit is identifiable in the stated model. This directly supplies the MLE alternative requested by Open Problem 10.4(1), and it is stronger than a statement conditional on manually fixing only the power spectrum because the theorem targets recovery of the orbit itself.

### 4.2 Sample complexity

Amelia Perry, Jonathan Weed, Afonso S. Bandeira, Philippe Rigollet and Amit Singer, *The Sample Complexity of Multireference Alignment*, SIAM Journal on Mathematics of Data Science 1(3) (2019), 497–517; arXiv:1707.00943.

Primary sources:
https://arxiv.org/abs/1707.00943
https://doi.org/10.1137/18M1214317

For generic cyclic MRA in the low-SNR regime, they prove optimal sample complexity proportional to `SNR^(-3)`. Under the standard fixed-signal normalization `SNR ~ sigma^(-2)`, this is the familiar `sigma^6` scale. The source's part (2) asks how `n` must scale to permit accurate recovery rather than demanding an exact finite-n numerical constant, so this is source-level coverage of the intended sample-complexity question in the generic MRA regime recorded by the intake.

The same literature stream identifies the generic moment/invariant cutoff as degree three. This matches the `sigma^(2 d)` consistency/sample-complexity parameterization in Abbe–Pereira–Singer.

### 4.3 Bounded follow-up/currentness check

The 2026-09-19 bounded search used the exact source problem language plus `multireference alignment maximum likelihood consistent`, `group action channel MLE consistency`, and `sample complexity multireference alignment`. It recovered the above primary papers and later MRA literature that treats these results as established background. No later source-version change was found that turns Open Problem 10.4 into a conjunctive demand for both quasi-MLE and MLE consistency.

This is positive prior-art evidence, not a claim that a negative search proves worldwide completeness.

## 5. Frozen source-matching metric

Define

`d_* = least invariant/moment degree needed to identify a generic standard cyclic-MRA orbit in the low-SNR model`.

This single source-matching quantity controls both numbered parts through the scale `N / sigma^(2 d_*)`.

- baseline before evidence: `UNKNOWN/UNMEASURED`;
- evidenced current value for generic standard MRA: `d_* = 3`;
- consequence: optimal generic low-SNR sample complexity is on the `sigma^6` scale, and MLE consistency follows when `N/sigma^6 -> infinity` in that generic case.

This metric is an admission diagnostic only. R7-01 does not inherit it as a research-target metric because E0057 is not admitted.

## 6. Exact disposition

**E0057 is not a fresh open problem for R7-01.**

The literal source-level two-part endpoint is already covered by later literature:

- Open Problem 10.4(1): the source expressly permits the MLE alternative, and MLE consistency is proved by Abbe–Pereira–Singer;
- Open Problem 10.4(2): the sample-complexity scaling is established by Perry–Weed–Bandeira–Rigollet–Singer and related optimal-rate work.

A possible remaining question about the specific quasi-MLE relaxation/estimator from the 2014 SDP line is not silently promoted into the source's original problem. It would need its own exact modern statement, hypotheses and canonical identity before it could be considered as a new target.

Classification: `KNOWN / RESOLVED_IN_LITERATURE / NOT_ADMITTED`.

No canonical claim is created. No Section-B methods are charged. The R7-01 successor remains `PENDING_ADMISSION`, with successor metric `UNKNOWN/UNMEASURED` and successor stagnation `NOT_STARTED`.

## 7. Next lawful cursor

Continue from unscreened or incompletely source-reconciled shard-zero intake rather than returning to E0057 absent a genuine new source-status change. A useful next scope check is E0039, Chatterjee Open Problem (11) on optimal random-assignment fluctuations: the August 2026 Mordant CLT settles the Uniform[0,1] law but, because Uniform[0,1] is outside Chatterjee's `P^+(1)` and a single law is not automatically a “general class,” exact source-level currentness still needs a class-scope reconciliation before any admission decision.
