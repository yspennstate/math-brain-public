# FOREST / account01 B01 — source chronology repaired; two-review gate integrated

**Candidate version:** `FOREST-KN-COCKS-RECONCILED-v3`  
**Run outcome:** `FULL_PROOF_CANDIDATE` under the collective internal gate.  
**Parent theorem:** not promoted here to an established/public theorem; novelty/priority and ordinary external expert scrutiny remain unverified.  
**Context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target

For every finite simple graph `G=(V,E)`, choose uniformly from **all** acyclic edge subsets `F subseteq E`, including the empty forest, disconnected forests and every forest size. For every distinct `e,f in E`, prove

`Pr(e,f in F) <= Pr(e in F) Pr(f in F)`.

Equivalently, with `Z,Z_e,Z_f,Z_ef` the exact forest counts,

`Delta_G(e,f)=Z_e Z_f-Z Z_ef >= 0`.

The latest lead candidate already proves the complete-graph theorem exactly. The only live dispute was the all-graphs transfer through the Cocks/Semple--Welsh source chain.

## 2. Required OTHER-account result consumed and applied

I consumed assigned partner account02/B02's immutable correction

`proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B02/B02-20260922T013646Z-forest-r12/cocks_scope_correction.md`,

blob `733d840093ca109d38f4e336d228ae1ddedf77c0`.

That correction was right to reject an **older class-level parallel-copy argument** as a proof of the fixed-graph implication. It preserved the complete-graph Hermite theorem and the unconditional spectral comparison, but classified the lead closure as source-insecure.

The present run resolves that exact objection by separating two different Semple--Welsh versions and the later Cocks theorem.

## 3. Decisive source chronology

### 3.1 Earlier Semple--Welsh working-paper mechanism

The accessible earlier working-paper text has Proposition 2.1 as a class-level equivalence and proves the converse by rational/integer approximation of a positive weighting followed by replacing each edge by the corresponding number of parallel copies. That mechanism indeed changes the graph and therefore, by itself, cannot prove

`unit pNC on one fixed G => M(G) independence correlated`.

This is the mechanism that motivated account02/B02's correction.

### 3.2 Final Semple--Welsh paper

The final published Semple--Welsh paper is materially different at the relevant point.

* Its Proposition 2.1 states only the easy one-way implication from independence correlation of the whole graphic class to the graph conjecture.
* Proposition 3.5 proves that **independence-correlated matroids are closed under minors**. Its proof takes an arbitrary positive weighting on a deletion/contraction minor and obtains the Rayleigh difference as the `epsilon -> 0+` or scaled `epsilon -> infinity` limit of the parent weighted Rayleigh difference.
* Immediately after Proposition 3.5, the authors stress that weighted minor closure does not by itself prove that the unit-pNC graph class is minor-closed.
* In Section 5 they ask as open question (3) whether a graph can satisfy the unit conjecture while `M(G)` fails to be independence correlated. The post-submission Note then records that Cocks proved the answer is no: **if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated**.

Source: Charles Semple and Dominic Welsh, *Negative Correlation in Graphs and Matroids*, Combinatorics, Probability and Computing 17 (2008), 423--435, DOI `10.1017/S0963548307008978`; final author PDF `https://www.math.canterbury.ac.nz/~c.semple/papers/SW07.pdf`, especially Proposition 3.5 and the Section 5 Note on printed page 13. The note identifies reference [3] as C. C. Cocks, *Correlated matroids*.

Cocks's paper was subsequently published as Clifford C. Cocks, *Correlated Matroids*, Combinatorics, Probability and Computing 17(4) (2008), 511--518, DOI `10.1017/S0963548308009152`. Its abstract says it extends Semple--Welsh, proves equivalences with correlated graphic-matroid statements, and answers open questions from that paper.

### 3.3 Resolution of the peer conflict

The class-level parallel-copy proof and the later fixed-graph Cocks theorem are **not competing formulations of the same proof**. The former appears in the earlier Semple--Welsh working version; the final Semple--Welsh paper separately attributes the stronger fixed-graph theorem to Cocks after submission.

Therefore the evidence used by account02/B02 and account01/B20 does not refute the fixed-graph theorem. It establishes only that the old Semple--Welsh class-level proof cannot substitute for Cocks's theorem. The final source explicitly supplies the fixed-graph statement that the lead reduction needs.

I preserve those peer corrections as valuable failure evidence; this report supersedes only their source-scope verdict on the lead's fixed-graph transfer.

## 4. End-to-end mathematical chain

The complete candidate can now be stated without an unpaid implication.

### Step A: complete graphs

The latest lead proof establishes the unit forest inequality for every `K_n` and every distinct edge pair. Its exact labelled-forest generating functions are

`R=z exp(R)`, `T=R-R^2/2`, `F=exp(T)`, `A=exp(R)`,

and

`Z_n=n![z^n]F`,

`E_n=(n-2)![z^(n-2)]F A^2`,

`J_adj,n=(n-3)![z^(n-3)]F A^3`,

`J_dis,n=(n-4)![z^(n-4)]F A^4(1+4/(1-R))`.

The `4/(1-R)` term is the same-tree case for two disjoint marked edges: deleting them produces one doubly distinguished middle tree and two outer rooted trees, with four endpoint choices.

Cauchy/Lagrange substitution reduces the harder disjoint orbit to probabilists' Hermite polynomials. With `k=n-4`, `s=k He_(k-1)(n+1)/He_k(n+1)`, the normalized disjoint gap is

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

Hermite-root symmetry and `sum lambda_i^2=k(k-1)` give

`s >= L_n=(n-4)(n-1)(n+4)/(n+1)^3`,

while coefficient positivity gives `0<=s<1`. For `n>=6`, `G_n` is increasing on `[0,1]`, and

`(n+1)^6 G_n(L_n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`.

After `n=t+6`, every coefficient is positive. The exact remaining complete-graph cases are positive (`K_3` adjacent gap `2`; `K_4` disjoint gap `6`; `K_5` disjoint gap `210`). Hence every `K_n` satisfies the source unit inequality.

### Step B: fixed-graph weighted upgrade

Apply the Cocks fixed-graph theorem as recorded in the final Semple--Welsh Note to each `K_n`:

`unit Conjecture 1.1 on K_n => M(K_n) is independence correlated`.

By definition this means the independent-set Rayleigh difference is nonnegative for every distinct pair and every positive real edge weighting.

### Step C: deletion minors

Semple--Welsh Proposition 3.5 says independence correlation is closed under minors. Therefore every deletion minor of `M(K_n)` is independence correlated.

### Step D: arbitrary finite simple graphs

Every finite simple graph `G` on at most `n` vertices is obtained from `K_n` by deleting the nonedges; isolated vertices do not change the graphic matroid or any forest count. Therefore `M(G)` is independence correlated. Set every surviving edge weight to `1`. This is exactly the uniform law on all unrooted forests of `G`, and gives

`Delta_G(e,f)>=0`

for every distinct edge pair.

No rooted measure, fixed forest size, fixed component count, connectedness assumption, separator approximation, or limiting sparse-graph conjecture is used.

## 5. Independent review gate

The owner protocol requires two independent existing-worker end-to-end reviews before a full candidate can be recorded. That gate is now met for the reconciled chain.

**Review 1:** account03/B02, handoff
`scheduled_tasks/work/shared/collective-open-problems-2026-09-22/handoffs/FOREST/account03-B02-20260922T020022Z-v2-review.md`, blob `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e`, outcome `INDEPENDENT_END_TO_END_REVIEW_PASS_1`. It independently rederived the complete-graph formulas/Hermite positivity and explicitly resolved the final-versus-working-paper Cocks chronology in favor of the fixed-graph chain.

**Review 2:** account03/B01,
`proofnet24/P14-probability-correlation/collective-2026-09-22/account03/B01/20260922T023025Z-account03-B01-forest-r11/second_end_to_end_review.md`, blob `ea161f8956619130775dd7b638d3f87408624941`, outcome `INDEPENDENT_END_TO_END_REVIEW_PASS_2 / FULL_PROOF_CANDIDATE`. It separately rederived the labelled decomposition, Cauchy/Hermite reduction, all-`n` sign proof, small cases, and the fixed-graph/minor transfer.

These are distinct existing workers. Neither review is being inferred from a scheduler receipt or from the lead's own prior calculation.

## 6. Exact computation status

No new numerical computation is used as a proof step in this run. The complete-graph proof is symbolic. The two independent reviews each carried separate exact finite regression checks; those are cited only as audits, not as closure of the all-`n` argument.

## 7. Honest classification

**Outcome: `FULL_PROOF_CANDIDATE`.**

This label means the internal candidate now contains every quantifier and boundary case required by the source statement and has two independent existing-worker end-to-end review passes. It does **not** mean the conjecture should yet be announced publicly as solved. Before any external claim, the Cocks theorem should receive ordinary expert/source scrutiny from the original published article or a journal-grade secondary source, and the Hermite proof should receive normal publication-level checking. The original Cocks full text was not directly accessible in this run; the fixed-graph theorem is source-bound through the final published Semple--Welsh Note and the two independent reviews.

The earliest remaining task is therefore **validation/publication preparation, not another missing mathematical implication**. If a later source check contradicts the fixed-graph theorem attribution, the candidate must immediately fall back to `ESSENTIAL_STEP_APPLIED` with the weighted-complete bridge unpaid.

## 8. Provenance and failures

* Canonical fleet login write was attempted and denied by the platform safety layer; this run does not claim that write succeeded.
* A scoped scientific start was committed instead.
* Assigned partner account02/B02's correction was consumed and preserved; its unconditional spectral result is untouched.
* No brain installation, benchmark work, email, Drive, public posting, permission change, paid compute, remote workflow, production population mutation, or scheduler mutation was performed.
* Brain status remained `WITHOUT_VERIFIED_BRAIN`.
