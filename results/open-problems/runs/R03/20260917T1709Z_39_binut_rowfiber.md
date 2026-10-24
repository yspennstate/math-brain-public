Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the accessible runtime exposes no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the fixed full-range envelope: `r(10)=222.6104736743168493957921796888577...` remains exact and `r(11)<=523.4894710902614257202829985613411...` remains the strongest replay-certified bound; unchanged count `3 -> 4`. Methods used: #23 DO WHAT THE PROPOSER DID NOT EXPECT, #28 REPLACE FOR ALL WITH FOR TYPICAL, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R03 run39 — post-stuck recovery action: bi-nut reformulation and exact row/column completion rigidity

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source OPEN.** This is the action selected by run38's first mandatory Section-I stuck report: attack the simplest still-unproved special case in which both corank-one null vectors are full and all absolute coordinate magnitudes are pairwise distinct. The fixed numerical metric did not move, so this does not reset stagnation. The next R03 invocation must therefore be the second Section-I thinking-only recovery if the owner policy is applied literally; it must not manufacture another local lemma merely because C297 below is new.

All thirty Section-B moves had already appeared somewhere in R03 before run38. I preserve that history and use the planned post-stuck triple `23/28/30`, which is different from run38's `22/24/11`.

## 1. Continuity, source match, ownership, and current literature

Before new mathematics I recovered/read:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- newest own report `runs/R03/20260917T1605Z_38_stuck_thinking_01.md`;
- current neighboring state: newest visible R02 report has already rotated to its separate I0121 union-closed-sets claim, while the relevant R04 history remains its I0027 retirement/closure sequence; neither is a competing F0001 owner;
- targeted canonical F0001 / Rademacher-singularity history rather than falsely claiming that the connector rendered all roughly 780 intake JSONL rows byte-for-byte.

The outside source remains **F0001**, Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / Probability Surveys 18 (2021), Conjecture 2.2. Vu's model is the iid uniform Rademacher matrix, and the source target retained by R03 is

\[
\Pr(\det B_n=0)=(1+o(1))\,n(n-1)2^{1-n}.
\tag{1.1}
\]

This is the sharpened form of the elementary equal/opposite row-or-column mechanism. Let `T_n` be the exact union of those signed row-pair and column-pair collision events. The frozen R03 quantity remains

\[
 r(n)=2^n\Pr(\det B_n=0,T_n^c),
\tag{1.2}
\]

and retained collision-overlap bookkeeping makes source closure equivalent to

\[
\boxed{r(n)=o(n^2).}
\tag{1.3}
\]

I rechecked the current primary literature on 2026-09-17 before continuing. Jain--Sah--Sawhney, arXiv:2010.06554 / GAFA 2021, prove the sharp elementary-mechanism asymptotic when the finite-support entry law is **not uniform on its support**; for a law uniform on its support they state only exponential-scale precision for the total singularity probability, while their compressible/structured analysis is sharp. Song--Wang, arXiv:2607.00495 (submitted 1 July 2026), determine growing-corank Bernoulli probabilities for `k=O(sqrt(log n))`. Hunter--Kwan--Sauermann--Sawhney, *On random matrices with large corank*, IMRN 2026 rnag126, published 18 June 2026, prove `P(corank >= k) <= exp(-c n k)` for all `k`. These later results suppress higher corank but do not determine the missing corank-one polynomial prefactor. A fresh bounded arXiv/primary search did not locate a later accepted proof of (1.1). This is dated bounded search evidence, not a worldwide novelty certificate.

No F0001 exclusion in `POSTED.md` applies. F0001 remains the active R03 HARD OUTSIDE target.

## 2. Frozen metric: before and after

No finite-envelope movement occurred. The retained values are

\[
 r(10)=222.6104736743168493957921796888577\ldots
\]

exactly and

\[
\boxed{
 r(11)\le
 \frac{32615069759481592686393385491735}{62303201039659529147657486336}
 =523.4894710902614257202829985613411\ldots .
}
\tag{2.1}
\]

Every previously certified branch for `n>=12` remains unchanged. Thus the fixed full-range upper envelope is retained rather than replaced by the narrower theorem below.

Stagnation history is preserved:

- run36: unchanged `0 -> 1`;
- run37: unchanged `1 -> 2`;
- run38: unchanged `2 -> 3`, first mandatory stuck thinking recovery;
- run39: unchanged `3 -> 4`, after executing the action selected by run38.

## 3. The special case selected by run38

Put `d=n-1`. Run37 introduced

\[
\mathcal N_d^\circ=
\{B\in\{0,1\}^{d\times d}:\det B=0,\ \det(J-2B)\ne0,\ B\text{ has no zero row or column}\}
\]

and `N_d^circ=|mathcal N_d^circ|`, with the source-equivalent endpoint

\[
\boxed{N_d^\circ=o\!\left(d^2 2^{d^2-d-1}\right).}
\tag{3.1}
\]

Retained C294--C296 localize the source-scale obstruction to real corank one and, after a negligible discard, to left and right null vectors having almost full support and almost all absolute coordinate magnitudes distinct.

Run38 therefore selected the following clean test class. Let `S_d` consist of binary `d x d` matrices `B` such that

1. `rank(B)=d-1`;
2. `ker B=span(v)` and `ker B^T=span(u)` with every coordinate of `u,v` nonzero;
3. the `d` numbers `|v_1|,...,|v_d|` are pairwise distinct;
4. the `d` numbers `|u_1|,...,|u_d|` are pairwise distinct.

The source-relevant full/distinct special case is a subset of `S_d`, obtained by additionally imposing the pivot condition `det(J-2B)!=0` and the collision deletions. Therefore any upper bound for `S_d` is automatically valid for the selected special case.

## 4. Method #23 — do what the proposer did not expect: attack one-sided genericity

A tempting shortcut after C294/C295 is to hope that making **one** null direction maximally generic (full support and all absolute magnitudes distinct) somehow forces the opposite null direction to be generic as well. That is false already at order seven.

The exact binary matrix

\[
B=\begin{pmatrix}
0&0&1&1&0&1&1\\
0&1&0&1&1&0&0\\
0&0&1&1&1&1&0\\
1&0&1&0&0&1&0\\
1&0&1&0&1&0&1\\
1&1&1&1&0&0&0\\
1&1&0&0&1&1&1
\end{pmatrix}
\tag{4.1}
\]

has rank six and

\[
 u=(2,7,-5,6,1,-4,-3)^T\in\ker B^T,
 \qquad
 v=(1,-1,-1,1,0,0,0)^T\in\ker B.
\tag{4.2}
\]

Thus `u` is full and

\[
\{|u_i|:1\le i\le7\}=\{1,2,3,4,5,6,7\},
\]

while `v` has support only four. Moreover `1^T v=0`, and consequently this witness also lies outside the source-pivot class: `det(J-2B)=0`.

This is **R03-X39**, an exact obstruction to the one-sided-genericity shortcut, not a counterexample to the source conjecture. The standard-library exact checker uses Bareiss integer determinants, verifies a nonzero `6 x 6` minor, both null equations, all seven distinct left magnitudes, the sparse zero-sum right null vector and `det(J-2B)=0`; its archived run ends `SELF-CHECK PASS`.

Outcome of #23: any successful asymptotic argument must genuinely use **both** null directions and the pivot/collision conditions. One-sided coefficient complexity is not self-propagating.

## 5. Method #28 — change the quantifier to the right structural population: bi-nut matrices

A fresh literature search found a category that names almost exactly the rank-one-null geometry isolated by C295. Bašić--Fowler--McCarthy--Potočnik, *Nut digraphs*, arXiv:2503.10548 (2025), published in *Discrete Applied Mathematics* 383 (15 April 2026), define a dextro-nut digraph by a one-dimensional kernel spanned by a full vector, a laevo-nut by the corresponding full co-kernel condition, and a **bi-nut** by requiring both. Their paper proves, among other structural facts, that every bi-nut digraph is strongly connected and that deleting any vertex leaves a nonsingular adjacency matrix.

For diagonal-zero adjacency matrices, the full-support part of `S_d` is literally the bi-nut condition. For arbitrary diagonal entries in our `0/1` matrices, it is safest to regard `S_d` as the loop-allowed adjacency-matrix analogue; none of the new proof below relies on a loop convention from the graph paper.

This category change is useful for two reasons.

First, it confirms that the full-left/full-right condition is a studied structural object rather than merely an R03 coordinate artifact. Second, it exposes a sharper source-specific refinement: in `S_d`, pairwise-distinct absolute null coordinates force every row and every column to have weight at least three. Indeed a row of weight one forces one coordinate of `v` to vanish, and a row of weight two forces `v_j=-v_k`, contradicting `|v_j|!=|v_k|`; transpose gives the column statement. The nut-digraph paper's generic bi-nut minimum in/out degree is two, so the R03 distinct-magnitude endpoint automatically excludes the extremal degree-two case.

Outcome of #28: the selected special case is a high-complexity subfamily of the bi-nut matrix population. Existing nut-digraph theory supplies useful construction and structural language but, in the bounded search, no asymptotic enumeration remotely at the `2^{d^2-d}` source scale. Thus the category transfer is informative but not itself a closure theorem.

## 6. Method #30 — one row / one column / one Hamming scale at a time

The full-support hypothesis permits an exact completion formula which is stronger than the one-sided section statement used earlier.

### R03-C297 — exact row/column completion rigidity for the full/distinct class

**Claim.** Let `B in S_d`, with right null vector `v` and left null vector `u`. Then:

1. every `(d-1)x(d-1)` minor obtained by deleting one row and one column is nonzero;
2. replacing row `i` by an arbitrary `y in {0,1}^d` gives a singular matrix **iff** `y dot v=0`;
3. replacing column `j` by `x in {0,1}^d` gives a singular matrix **iff** `u dot x=0`;
4. consequently, for every fixed row-deletion fiber there are at most
   \[
   O(2^d d^{-3/2})
   \]
   singular binary row completions, and analogously for every column-deletion fiber;
5. changing one or two entries within a single row, or within a single column, always makes the matrix nonsingular;
6. globally,
   \[
   \boxed{|S_d|=O(2^{d^2}d^{-3/2}).}
   \tag{6.1}
   \]

**Proof.** Since `rank(B)=d-1`, its adjugate has rank one. Every column of `adj(B)` lies in `ker B` and every row lies in the left kernel, so for some nonzero scalar `gamma`,

\[
\operatorname{adj}(B)=\gamma v u^T.
\tag{6.2}
\]

Because `u_i v_j!=0` for every `i,j`, every cofactor is nonzero. This proves (1), and in particular deleting any one row leaves `d-1` independent rows and deleting any one column leaves `d-1` independent columns.

Let `b_i` be row `i`, let `Delta=y-b_i`, and write

\[
B'=B+e_i\Delta.
\]

The rank-one determinant identity, valid here directly by multilinearity, gives

\[
\det B'=\Delta\,\operatorname{adj}(B)e_i
       =\gamma u_i\,\Delta\cdot v.
\tag{6.3}
\]

Since `b_i dot v=0`,

\[
\boxed{\det B'=\gamma u_i\,y\cdot v.}
\tag{6.4}
\]

As `gamma u_i!=0`, this proves (2). If `y dot v=0`, the unchanged `d-1` rows already have rank `d-1`, so the completed singular matrix still has exact corank one and the same right-null direction. Transposing proves (3).

For (4), write `epsilon_j=2y_j-1`. The condition `y dot v=0` is equivalent to

\[
\sum_j\epsilon_j v_j=-\sum_j v_j.
\]

The coefficients `v_j` have pairwise-distinct absolute values, hence in particular are distinct and nonzero. The Sárközy--Szemerédi refinement of Littlewood--Offord gives concentration `O(d^{-3/2})` for Rademacher sums with distinct coefficients. Thus the number of binary `y` satisfying `y dot v=0` is `O(2^d d^{-3/2})`. The same applies to columns using `u`.

For (5), one changed coordinate would require a nonzero single coefficient to vanish. Two changed coordinates in one row would require `±v_j±v_k=0`, impossible because `|v_j|!=|v_k|`; transpose handles columns.

Finally fix, say, the last row and first choose the other `d-1` rows. There are at most `2^{d(d-1)}` such prefixes. Any prefix that extends to a member of `S_d` has rank `d-1` and determines its projective right null direction; by (4) it has at most `O(2^d d^{-3/2})` singular binary completions. Multiplication gives (6.1). QED.

The Sárközy--Szemerédi `O(d^{-3/2})` bound is classical and asymptotically optimal at that level of coefficient information; recent expositions such as Gunby's *Antichain codes* explicitly recall this theorem. I therefore make no novelty claim for the anti-concentration ingredient. The exact completion identity (6.4) is elementary adjugate algebra; its value here is that it pinpoints exactly what one more scale of information would have to control.

### Why C297 still does not close even the selected special case

The required source-scale special-case bound is

\[
 |S_d\cap\mathcal N_d^\circ|
 =o(d^2 2^{d^2-d-1}).
\tag{6.5}
\]

C297 gives only

\[
 |S_d|\le O(2^{d^2}d^{-3/2}),
\]

which is weaker than (6.5) by a factor on the order of

\[
\frac{2^d}{d^{7/2}}.
\tag{6.6}
\]

This is a quantitative failure, not a renamed coupling lemma. The exact row fiber is already as small as classical distinct-coefficient Littlewood--Offord can force; the missing `2^{-d}`-scale saving must come from how **many row fibers can simultaneously be rich while the transposed column fibers are also rich**.

That is precisely a two-sided matrix-level question. A black-box multiplication of the row and column `d^{-3/2}` probabilities is invalid because they are coupled through the same matrix.

## 7. Closest additional machinery found this run

The new completion formula makes bilinear Littlewood--Offord theory more relevant than it looked in run38. Choosing any nonzero cofactor as a pivot writes a rank-`d-1` matrix in block form

\[
B=\begin{pmatrix}C&a\\ b^T&c\end{pmatrix},\qquad C\text{ invertible},
\]

with singularity equivalent to

\[
c=b^T C^{-1}a.
\tag{7.1}
\]

The selected special case additionally says that both `(-C^{-1}a,1)` and `(-C^{-T}b,1)` have full, pairwise-distinct absolute coordinates. Kevin Costello's bilinear Littlewood--Offord work shows that bilinear forms with concentration substantially above the generic polynomial scale must be close to degenerate. That theorem is nowhere near a plug-and-play proof of (6.5), but it supplies a concrete language for the next two-sided step: classify those cores `C` for which the Boolean bilinear incidence (7.1) is large **and simultaneously** both transformed vectors satisfy the near-injective profile inherited from C294/C295.

The existing R03 black-box counting inverse-LO route failed because it operated below its effective concentration range. The potential difference here is that the bilinear form is not arbitrary: its coefficient matrix is `C^{-1}` for a binary invertible core, and the source endpoint imposes distinctness on both `C^{-1}a` and `C^{-T}b`. I did not prove the required bilinear entropy loss in this run and do not label it as progress on the fixed metric.

## 8. What moved mathematically, and what did not

What **did** move:

- a false one-sided shortcut is killed by the exact R03-X39 witness;
- the run38 special class is identified with the loop-allowed bi-nut matrix geometry studied in current graph-spectral literature;
- C297 gives an exact row/column replacement criterion, radius-two same-row/same-column rigidity, and a complete `O(2^{d^2}d^{-3/2})` upper bound for the full/distinct special class;
- the remaining quantitative deficit is explicit: an additional factor about `2^d/d^{7/2}` is still needed even for the selected special case;
- block-pivoting isolates a concrete next candidate: a nondegenerate **bilinear** Boolean incidence bound for `C^{-1}` under simultaneous left/right distinct-profile constraints.

What did **not** move:

- the frozen full-range numerical envelope;
- the source status;
- the source-equivalent count (3.1);
- closure or publication status.

Therefore the honest label remains **PARTIAL**.

## 9. Exact finite checker

The only finite claim needing a new checker is R03-X39. I executed

`artifacts/R03/20260917T1709Z_39_one_sided_distinct_obstruction.py`

with exact integer arithmetic. Its archived output is

`artifacts/R03/20260917T1709Z_39_one_sided_distinct_obstruction.out`

and ends `SELF-CHECK PASS`.

C297 is a theorem-sized symbolic argument written in full above; no checker was manufactured for it.

## 10. Stuck protocol state and next obligation

Run38 was **stuck recovery 1 of at most 2** and selected the special case attacked here. Because the fixed metric again did not move, the next R03 run must be the **second Section-I thinking-only recovery** under the owner's rule. It should make no new claim and should decide whether the bilinear-core route genuinely contains a source-scale mechanism or whether this target should be prepared for handoff after the allowed second recovery/action cycle.

The exact blocker remains

\[
\boxed{N_d^\circ=o(d^2 2^{d^2-d-1}).}
\]

For the chosen special case the immediate blocker is sharper:

\[
\boxed{
\#\{B\in\mathcal N_d^\circ:\ u,v\text{ full and }|u_i|,|v_j|\text{ pairwise distinct}\}
=o(d^2 2^{d^2-d-1}).
}
\tag{10.1}
\]

C297 reaches only `O(2^{d^2}d^{-3/2})`. A successful next proof must produce an exponential-in-`d` saving from the **joint** row/column or bilinear-incidence structure, not another polynomial Littlewood--Offord factor.

## 11. Model / scheduler interface reality

The requested runtime escalation is still not enforceable through the exposed task-control schema. The available control surface provides title, prompt, schedule/timing, enablement and notification behavior; it has **no model-family field and no reasoning-effort field**. Therefore the string `Model: GPT-6. Reasoning: maximum` remains a prompt request, not authenticated scheduler telemetry. This run's actual model is reported as GPT-5.6 Sol and reasoning level as UNVERIFIED.

The controlling repository policy records historical probes where P26/P01/P03 returned `You cannot modify this task`. Root `RESULTS.md` also records that P26 later updated successfully from another authorized context. The legitimate workaround is therefore to use the owning/authorized workspace or account context, and—separately—to have a product surface that actually exposes model/reasoning controls. A repository edit or duplicate task does not bypass an ownership boundary. I made no scheduler or permission change.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R03
  source: "F0001 / Vu Conjecture 2.2 / iid uniform Rademacher singularity"
  source_status: OPEN
  run_status: PARTIAL
  run_type: "post-stuck-recovery-1 action on simplest full/distinct special case"
  fixed_metric: "full-range replay-certified upper envelope for r(n)=2^n P(det B_n=0,T_n^c)"
  metric_before:
    r10_exact: "222.6104736743168493957921796888577..."
    r11_upper: "523.4894710902614257202829985613411..."
  metric_after:
    r10_exact: "222.6104736743168493957921796888577..."
    r11_upper: "523.4894710902614257202829985613411..."
  movement: "NO MOVEMENT"
  unchanged_count: "3 -> 4"
  methods: [23, 28, 30]
  new_claims:
    - "R03-C297 PROVED: exact row/column completion criterion for full/distinct corank-one binary matrices; row/column fibers O(2^d d^-3/2); |S_d|=O(2^(d^2)d^-3/2)"
    - "R03-X39 EXACT OBSTRUCTION: one full all-distinct null direction does not force the opposite null direction to be full/generic; checker PASS"
  source_closure: false
  next_protocol_state: "second Section-I thinking-only recovery required before another research claim"
  remaining_obligation: "joint two-sided / bilinear basis-completion loss giving o(d^2 2^(d^2-d-1))"
  scheduler_mutation: none
  shared_root_mutation: none
  peer_file_mutation: none
```

No email, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-file edit was performed.
