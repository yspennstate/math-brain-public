Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-01 admission disposition — E0041 current-literature resolution

Date checked: 2026-09-19 UTC  
Repository: `yspennstate/math-open-problems`  
Branch: `master`  
Slot: `R7-01`  
Native ID: `6aabe777361481919c9e614646464772`  
Pre-write master: `182876c9de825b70c576f7e385dace21f0f8c125`

## 1. Why E0041 is in this slot's shard

The canonical candidate ID is exactly `E0041`. Using the required case-sensitive character arithmetic,

`ord('E') + ord('0') + ord('0') + ord('4') + ord('1') = 69 + 48 + 48 + 52 + 49 = 266 = 7*38`.

Hence `sum(ord(c) for c in "E0041") mod 7 = 0`. This is a genuine R7-01 shard candidate, not a title alias.

## 2. Exact outside source and source endpoint

Author: Sourav Chatterjee.  
Title: *A general method for lower bounds on fluctuations of random variables*.  
Publication: *Annals of Probability* 47(4) (2019); arXiv first posted 2017-06-14, current arXiv v3 dated 2018-07-26.  
Source URL: https://arxiv.org/abs/1706.04290  
Locator: Section 3, Open problems, item (13), printed PDF p. 28.

The source endpoint is the existential request:

> “Prove a distributional limit theorem in any of the examples discussed in this paper.”

The examples explicitly include the stochastic travelling-salesman problem, stochastic minimal matching, the random assignment problem, the Sherrington–Kirkpatrick model, first-passage percolation, and random matrices. The source's random-assignment section explicitly discusses i.i.d. `Uniform[0,1]` costs (in the paragraph recording Talagrand's upper bound), so that law is plainly inside an example discussed in the paper even though Chatterjee's own Theorem 2.9 is stated for the separate class `P^+(1)`.

The repository intake row at

`probability_1000_intake_E_20260908/problems.jsonl`

still records E0041 as `admitted: true`, `current_status: unverified`, `result_status: attempted_unsolved`; its 2026-09-08 status note says that no distributional limit was then known for the random-assignment problem. That status is now stale.

## 3. Fresh current-literature check dated 2026-09-19

A positive primary-source match exists:

Gilles Mordant, *A central limit theorem for the random assignment problem*, arXiv:2608.05123, submitted 2026-08-05.  
URL: https://arxiv.org/abs/2608.05123

For `C_n`, the minimum cost of a perfect matching in an `n x n` matrix of independent `Uniform[0,1]` entries, the preprint states

`sqrt(n) (C_n - zeta(2))  ==>  N(0, 4 zeta(2) - 4 zeta(3))`.

Thus it supplies an actual nondegenerate distributional limit theorem for the random-assignment problem, one of Chatterjee's explicitly discussed examples.

A bounded 2026-09-19 follow-up search found the same arXiv identifier and statement mirrored by current indexing services; I found no withdrawal, replacement, or correction changing the stated theorem. This is a **current preprint-level literature resolution**, not an independent R7-01 proof audit and not a claim that the paper has undergone peer review.

## 4. Quantifier match

The source endpoint is existential over the examples: it asks for a distributional limit theorem in **any** example discussed in the paper. It does not require such a theorem simultaneously for all six example families, nor for every cost distribution in the random-assignment family.

Mordant's theorem therefore satisfies the literal source quantifier:

1. `Uniform[0,1]` random assignment is explicitly discussed by Chatterjee;
2. Mordant proves a central limit theorem for its optimal cost;
3. a central limit theorem is a distributional limit theorem;
4. one successful example satisfies item (13)'s `any` endpoint.

There is no need to reinterpret item (13) as the stronger and different question of obtaining distributional limits for every model or every admissible cost law.

## 5. Ownership and repository-status check

At pre-write master `182876c9de825b70c576f7e385dace21f0f8c125`, `operations/claims/E0041.md` does not exist. The absence of a claim does **not** make E0041 admissible: the positive current-literature resolution is independently disqualifying under the owner directive's known/solved-source exclusion.

The exact comparison from the previous R7-01 creation commit `32acb777745c5491c4741ae5cbe8416636c7ae5c` to pre-write master is `ahead 102 / behind 0`, with a complete changed-file set (`too_large = null`). It contains no change to `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, the E-intake `problems.jsonl`, or a canonical E0041 claim. Consequently this is a new R7-01 source-status correction, not a response to a shared-ledger mutation.

## 6. Admission decision

**Disposition: KNOWN / RESOLVED IN CURRENT LITERATURE (2026 preprint) / NOT_ADMITTED.**

E0041 is not a fresh open target for R7-01. No canonical claim is created. No source metric is activated, because the protocol starts a frozen mathematical metric only after admission. The successor state therefore remains:

- target: `PENDING_ADMISSION`;
- metric: `UNKNOWN/UNMEASURED`;
- stagnation: `NOT_STARTED`;
- Section-B methods charged: none.

Search misses are not used as novelty evidence here; the positive theorem match is the decisive exclusion evidence.

## 7. Durable nonduplication note

Absent a material status reversal (for example a withdrawal invalidating the theorem), future R7-01 admission passes should not treat E0041 as open inventory. The coordinator may reconcile the stale intake/shared-ledger status separately; R7-01 does not edit shared `RESULTS/QUEUE/POSTED/INDEX/RANKING` files.
