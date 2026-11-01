Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is not GPT-6 at maximum; the exposed runtime provides no authenticated model/reasoning telemetry or binding model/effort selector.

# R7-03 source-status reconciliation — I0091 / Komlós conjecture

Date checked: 2026-09-18 UTC.
Worker: R7-03 Boundary-Case Research.
Native identity recovered from registry: `6aabe7be74008191b526b109ee4e9e80`.
Start-of-run master snapshot: `d694cda7c5ef4b45d4620143bfedcc755b61a5f7`.
Fresh master immediately before this artifact: `3de125dc42adda199e6d7a1944492c2407e7994b`.
Slot state: `PENDING_ADMISSION`.

## 1. Shard and ownership gate

Canonical candidate `I0091` satisfies the R7-03 shard gate exactly:

`ord('I')+ord('0')+ord('0')+ord('9')+ord('1') = 73+48+48+57+49 = 275 ≡ 2 (mod 7)`.

The canonical intake row is `probability_1000_intake_I_20260914/problems.jsonl`, `I0091`. A fresh exact-path search found no `operations/claims/I0091.md` on current master. This does **not** make the source assignable by itself: repository history also contains R13 work on the exact Boolean Komlós mathematical target, so alias/ownership was checked rather than inferred from the absence of an I0091-named claim. In any event the current literature status below excludes I0091 from admission.

## 2. Original outside source and exact endpoint

Outside proposer/source:

- Afonso S. Bandeira,
- “Did just a couple of deviations suffice all along? (problems 10-14),” Randomstrasse 101,
- posted 19 December 2024,
- source URL: https://randomstrasse101.math.ethz.ch/posts/HowManyDeviations/,
- locator: **Conjecture 10 (Komlós Conjecture)**.

The source defines

`disc(A) := inf_{x in {±1}^n} ||A x||_∞`

for an `n x n` real matrix `A`, and asks whether there exists a universal constant `K` such that for every positive integer `n` and every square matrix `A` whose columns have unit Euclidean norm,

`disc(A) <= K`.

The source notes the then-best lower bound `K >= 1+sqrt(2)` from Kunisky. The quantifiers are universal in `n` and `A`; no algorithmic or optimal-constant requirement is part of Conjecture 10. Thus source closure requires only one finite universal upper bound valid for all such matrices.

Historical intake status: `open_per_source` / `not_attempted`.

## 3. Current primary-source literature check

### 3.1 Guo–Fang–Lu, 10 September 2026

Shengtao Guo, Ethan X. Fang and Junwei Lu, **“Vector Balancing via Directional Total Variation,”** arXiv:2609.11189v1, submitted 10 September 2026:

https://arxiv.org/abs/2609.11189

Their main theorem states that every finite family of real vectors `v_1,...,v_N` of Euclidean norm at most one admits signs `epsilon_i in {±1}` such that

`|| sum_i epsilon_i v_i ||_∞ < 3 sqrt(2 pi)`.

This theorem is strictly stronger than Bandeira's Conjecture 10: it permits arbitrary finite family size and ambient dimension and permits column norms at most one, whereas I0091 asks only for `n` unit columns in `R^n`.

A bounded current-version search on 2026-09-18 found the arXiv record still at v1 and found no withdrawal/correction. That negative search is not itself a validity certificate.

### 3.2 Karingula–Lovett, 17 September 2026

Sankeerth Rao Karingula and Shachar Lovett, **“An elementary proof of the Komlos conjecture,”** ECCC TR26-188, published 17 September 2026:

https://eccc.weizmann.ac.il/report/2026/188/

They explicitly give an elementary proof of the Komlós conjecture, simplifying the recent Guo–Fang–Lu proof, and prove the dimension-free bound

`|| sum_i epsilon_i v_i ||_∞ <= 36`

for all finite real vector families with `||v_i||_2 <= 1`.

This is an independent later proof route at the level of authorship and exposition and is enough by itself to match the I0091 endpoint. It is not being counted as one of this repository's P26/OTHER closure audits; those audit rules apply to fleet theorem claims, while the present action is a literature-status reconciliation.

## 4. Exact source-to-theorem implication

Let `A=[a_1 ... a_n]` be any source-admissible matrix, so `a_i in R^n` and `||a_i||_2=1`. Apply Guo–Fang–Lu to the family `(a_i)_{i=1}^n`. There are signs `epsilon_i` for which

`|| sum_{i=1}^n epsilon_i a_i ||_∞ < 3 sqrt(2 pi)`.

But, by matrix multiplication,

`sum_i epsilon_i a_i = A epsilon`,

where `epsilon=(epsilon_1,...,epsilon_n)^T`. Therefore

`disc(A) = min_{x in {±1}^n} ||A x||_∞ <= ||A epsilon||_∞ < 3 sqrt(2 pi)`.

Thus Bandeira's exact Conjecture 10 holds with, for example,

`K = 3 sqrt(2 pi) < 7.52`.

Karingula–Lovett independently gives the weaker but still source-closing constant `K=36`.

There is no residual quantifier, boundary case, or square-matrix restriction left over. The source does not ask for the optimal value of `K`, so the fact that the sharp Komlós constant is not identified does not keep Conjecture 10 open.

## 5. Three Section-B moves and outcomes

### B18 — SAY IT IN ANOTHER LANGUAGE

Translate the matrix statement into vector balancing by taking the columns of `A` as the vectors. The source discrepancy is exactly the infinity norm of a signed vector sum. Outcome: the 2026 theorem statement matches the source without a loss of scope.

### B11 — DUALIZE

For every signing `epsilon`,

`||A epsilon||_∞ = max_{1<=j<=n} |<e_j,A epsilon>| = max_{u in {±e_1,...,±e_n}} sum_i epsilon_i <u,a_i>`.

So I0091 is a finite-coordinate support-function/vector-balancing problem, not a different matrix-only variant. Outcome: no hidden norm convention separates the source from the vector theorem.

### B25 — COUNT THE SAME THING TWICE / BIJECTION

The map

`ordered n-tuple (a_1,...,a_n) of unit vectors in R^n <-> square matrix A=[a_1 ... a_n] with unit-norm columns`

is a bijection, and a sign vector `epsilon` on the tuple is exactly the sign vector in `A epsilon`. Outcome: all objects and quantifiers in Conjecture 10 embed exactly into the theorem's class; there is no unhandled family.

This triple is distinct from R7-03's immediately preceding `B2/B6/B30` triple.

## 6. Repository noncircularity / prior work

A useful neighboring report, `runs/R13/20260916T133352Z_q2-bf3c.md`, had already located Guo–Fang–Lu and recorded the same `3 sqrt(2 pi)` full Boolean Komlós theorem while auditing a Komlós track. Therefore the external theorem is **not a new discovery for the repository as a whole**. The new work here is the explicit source/alias reconciliation showing that canonical intake row `I0091`, still labelled open in its ingest record, is exactly subsumed by that theorem and by the 17 September Karingula–Lovett proof.

The logical status does not depend on R13's internal derivations: the implication in Section 4 uses the external theorem statement directly. Hence there is no circular peer-proof dependency.

## 7. Disposition and metric

Disposition of `I0091`: **KNOWN / RESOLVED_IN_LITERATURE_2026_09**.

Screening-status movement: `OPEN_PER_SOURCE (stale intake) -> KNOWN`.

R7-03 has no admitted successor, so its frozen admitted-target metric remains:

`UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.

No target-specific stagnation counter starts. No admission record or claim is created for I0091. No shared `QUEUE.md`, `RESULTS.md`, or `POSTED.md` edit is made by this worker.

## 8. Admission consequence

I0091 must be excluded from the R7-03 successor pool. The bounded residue-2 I-slice reconciliation still did not yield an honestly CLOSABLE, unclaimed outside successor: the surviving unclaimed-looking rows encountered in that slice are broad/vague or HARD, while claimed/known/posted/retired aliases remain unavailable. R7-03 therefore stays `PENDING_ADMISSION` rather than manufacturing a narrower source problem.

Next attack: continue the residue-2 canonical admission cursor beyond already screened aliases, prioritizing a source with a finite endpoint/sharp boundary and an exact closure criterion; re-run source/current-status/ownership checks before any claim.

## ledger_delta

- `I0091`: stale intake `OPEN_PER_SOURCE` -> **KNOWN / RESOLVED_IN_LITERATURE_2026_09** by exact theorem match.
- R7-03 assignment: unchanged, `PENDING_ADMISSION`.
- admitted-target metric: `UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.
- claims created: none.
- shared ledgers edited: none.
- peer/historical files edited: none.
