Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the exposed runtime provides no authenticated GPT-6 selector, reasoning-effort selector, or applied-run attestation, so I do not claim GPT-6 maximum. NO MOVEMENT on the frozen full-range metric: `r(11) <= 522.9989062413841009635431653560194...` remains, with `r(10)=222.6104736743168493957921796888577...` exact and all retained `n>=12` branches unchanged. Historical F0001 terminal stuck/handoff count `6` is preserved; the current post-movement no-movement streak reaches `3`, so the stuck trigger is binding and this report HANDS OFF F0001 rather than opening another recovery cycle. Methods: #1 CHANGE THE CATEGORY, #11 DUALIZE, #19 MAKE IT AN ALGORITHM.**

# R03 run59 — exact corank split repairs the R2 import at source scale; F0001 handoff

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source not certified closed; F0001 HANDOFF at end of this report.**

The fixed numerical metric does not move in this run. The mathematical progress is asymptotic/source-scale: the whole Blinovsky `R2` regime can be removed at `o(n^2 2^{-n})` scale by combining a published fixed-corank theorem with a rank-preserving finite-field reduction and Bourgain--Vu--Wood Proposition 5.4. This repairs the precise rank/codimension mismatch identified in run58. It does **not** by itself certify the full sharp singularity asymptotic, because the remaining near-full-support/corank-one sector and the end-to-end use of the current Blinovsky preprint have not been independently closed and audited.

## 1. Continuity and exact source normalization

Before doing mathematics I recovered/read the current campaign controls and state required by the deployment:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- newest R03 report `runs/R03/20260918T1208Z_58_sparse_circuit_cutoff_c2a7.md` and the immediately preceding fold-repair report `runs/R03/20260918T1106Z_57_fold_projection_repair.md`;
- the historical terminal F0001 handoff `runs/R03/20260917T1907Z_41_third_stuck_handoff_f0097.md` and the explicit reassignment record in run55;
- the newest neighboring random-matrix report recovered in the repository (`research7_2026-09-17/R7-07/...`, F0003 random-regular adjacency singularity);
- current READY/HARD ownership state in `QUEUE.md` and direct current claim files for the previously READY hard reserve entries I0078, I0079, I0028.

The large intake ledgers are connector-sized; I used exact F0001 provenance/history and current queue/claim records rather than claiming a byte-for-byte display of every intake JSONL row.

The outside source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 2. It defines `M_n` as the `n x n` iid uniform Rademacher sign matrix. On the page containing Conjecture 2.2 it records the elementary equal/opposite row-or-column lower bound

\[
 p_n\ge (4-o(1)){n\choose2}2^{-n}
\]

and states

\[
\boxed{p_n=(2+o(1))n^2 2^{-n}.}
\tag{1.1}
\]

Therefore the owner-retained formulation is source-matched:

\[
\boxed{
\Pr(\det B_n=0)=(1+o(1))n(n-1)2^{1-n}.
}
\tag{1.2}
\]

Let `T_n` be the exact union of equal/opposite signed row-pair and column-pair events. The frozen R03 remainder is

\[
\boxed{r(n)=2^n\Pr(\det B_n=0,T_n^c),}
\tag{1.3}
\]

and retained exact collision-overlap bookkeeping reduces source closure to

\[
\boxed{r(n)=o(n^2).}
\tag{1.4}
\]

The full-domain finite envelope entering this run is

\[
r(10)=222.6104736743168493957921796888577\ldots
\]

exactly and

\[
\boxed{r(11)\le522.9989062413841009635431653560194\ldots .}
\tag{1.5}
\]

No theorem below supplies an effective finite-`n=11` decrement, so (1.5) remains frozen.

## 2. Current primary-literature check

Fresh source checks on 2026-09-18 give the following.

**Jain--Sah--Sawhney, arXiv:2010.06554 / GAFA 2021.** Their abstract still says that for a finite-support law uniform on its support they prove only

\[
\Pr(M_n(\xi)\text{ singular})=(1+o_n(1))^n\Pr(\text{two rows or columns equal}),
\]

while obtaining the sharp elementary-mechanism asymptotic for laws not uniform on their support. Thus this paper does not itself give the missing polynomial prefactor for uniform Rademacher matrices.

**Jain--Sah--Sawhney, arXiv:2103.02467, *Rank deficiency of random matrices*.** The paper proves fixed-corank exponential rates for `Ber(p)` and, crucially for this track, the remark immediately after Theorem 1.1 states that after replacing Proposition 2.7 by the corresponding finite-support versions, for every fixed finitely supported random variable `xi`,

\[
\Pr(\operatorname{corank}M_n(\xi)\ge k)
\le
\left(\max_z\Pr(\xi=z)+o_n(1)\right)^{kn}.
\tag{2.1}
\]

For uniform Rademacher `xi`, `max_z P(xi=z)=1/2`. Taking fixed `k=2` gives

\[
\boxed{
\Pr(\operatorname{corank}B_n\ge2)
\le 2^{-2n+o(n)}
=o(n^2 2^{-n}).
}
\tag{C346}
\]

This published remark is stronger at the source scale than the generic large-corank exponential inputs previously being carried by this track.

**Bourgain--Vu--Wood, arXiv:0905.0461.** In their finite-field proof, `A_H` is the event that all random rows **span** a nontrivial hyperplane `H` exactly, not merely that they lie in it. Their Definition 5.1 partitions such hyperplanes by cube mass, and Proposition 5.4 gives an `o(1)^n` total for each medium combinatorial-dimension class. For the fair sign law, the Section 3 symmetric-distribution calculation at `mu=1` gives the `p=1/2`, exponent `r=2` instance of their framework.

**Blinovsky, arXiv:1511.05283v7.** The current arXiv record was last revised 26 October 2025 and explicitly claims the full tight asymptotic and expansion. Its displayed `R2` step (18) cites BVW Proposition 5.4 for a union over arbitrary real subspaces with the weaker event that all rows merely lie in `V^perp`. Run58 correctly identified that this is not literally the event to which BVW Proposition 5.4 applies. Run56 had independently found that the pointwise fold comparison used later in the current preprint is false; run57 replaced that local fold step by an exact averaging/projection identity. This run repairs the `R2` rank/codimension mismatch at the source scale. I still do **not** relabel the full conjecture KNOWN solely from that preprint without an end-to-end validation or accepted later source.

A bounded fresh search this run found no later peer-reviewed source that both matches (1.2) and supersedes these audit issues. This is dated bounded evidence, not a global novelty certificate.

## 3. Method #1 — CHANGE THE CATEGORY: split by actual corank first

The obstruction in Blinovsky (18) comes from summing over arbitrary relation subspaces before asking what rank the realized matrix actually has. Reverse that order.

Let `R2` denote the source/preprint medium cube-mass class

\[
(0.51)^{n/2}
<
2^{-n}|V^\perp\cap\{\pm1\}^n|
\le
\frac{100}{\sqrt n}.
\tag{3.1}
\]

Let

\[
E_{R2}:=
\bigcup_{V\in R2}
\{\text{every row of }B_n\text{ lies in }V^\perp\}.
\tag{3.2}
\]

Every `V` in (3.1) is nonzero for all sufficiently large `n`, so `E_R2` implies singularity. Split

\[
E_{R2}
=
(E_{R2}\cap\{\operatorname{corank}B_n=1\})
\cup
(E_{R2}\cap\{\operatorname{corank}B_n\ge2\}).
\tag{3.3}
\]

The second term is already source-negligible by C346. Thus the only point where BVW is needed is **actual corank one**, exactly the case where the row span is a genuine hyperplane.

This change of category removes the dimensional ambiguity rather than estimating around it.

## 4. Method #11 — DUALIZE: exact real-hyperplane to finite-field-hyperplane transfer

The key deterministic lemma is the missing bridge.

### Lemma C347 — exact cube-membership preservation for a corank-one sign row span

Let `A` be an `n x n` sign matrix with real rank `n-1`, and let

\[
H_\mathbb R=\operatorname{span}_\mathbb R\{\text{rows of }A\}.
\]

Choose `n-1` independent sign rows `u_1,...,u_{n-1}`. Choose a prime `Q` large enough both for the BVW finite-field setup and so that

\[
Q>n^{n/2}.
\tag{4.1}
\]

Reduce the `u_i` modulo `Q` and put

\[
H_Q=\operatorname{span}_{\mathbb F_Q}(u_1,\ldots,u_{n-1}).
\]

Then:

1. `H_Q` is a hyperplane in `F_Q^n`;
2. the rows of `A` span `H_Q` exactly after reduction;
3. for every `x in {+1,-1}^n`,

\[
\boxed{
x\in H_\mathbb R\iff x\pmod Q\in H_Q;
}
\tag{C347}
\]

hence the sign-cube masses are identical:

\[
2^{-n}|H_\mathbb R\cap\{\pm1\}^n|
=
\Pr(X\pmod Q\in H_Q),
\tag{4.2}
\]

where `X` is a uniform Rademacher row.

#### Proof

Because `u_1,...,u_{n-1}` are independent over `R`, some `(n-1)x(n-1)` minor has a nonzero integer determinant. Hadamard's inequality gives absolute value at most `(n-1)^{(n-1)/2}<Q`; therefore that determinant stays nonzero modulo `Q`. Thus the reduced rows have rank `n-1` and span a finite-field hyperplane.

For a sign vector `x`,

\[
x\in H_\mathbb R
\iff
\det\begin{pmatrix}u_1\\ \vdots\\u_{n-1}\\x\end{pmatrix}=0.
\]

The displayed determinant is an integer of absolute value at most `n^{n/2}<Q`. Consequently it vanishes over the reals iff it vanishes modulo `Q`, proving C347. Every row of `A` lies in the real span and therefore in the reduced finite-field span; because the latter already has dimension `n-1`, the full reduced row family spans `H_Q` exactly. `square`

The point of C347 is stronger than determinant-zero preservation alone: it preserves **membership of every cube point** in the realized corank-one row hyperplane, so the `R2` mass parameter survives exactly.

## 5. Matching the BVW medium-dimension hypotheses

Assume now `B_n` has corank one and lies in `E_R2`. If rows lie in `V^perp` for some `V in R2`, then

\[
H_\mathbb R:=\operatorname{rowspan}(B_n)\subseteq V^\perp.
\]

Since `dim H_R=n-1`, `V` is nonzero, and `dim V^perp<=n-1`, necessarily

\[
\boxed{H_\mathbb R=V^\perp,\qquad \dim V=1.}
\tag{5.1}
\]

Apply C347. Write

\[
\mu_Q:=\Pr(X\in H_Q).
\]

Then (3.1) becomes

\[
(0.51)^{n/2}<\mu_Q\le100n^{-1/2}.
\tag{5.2}
\]

For the uniform sign law, use the BVW parameters

\[
p=\frac12,\qquad r=2.
\tag{5.3}
\]

If `H_Q` lies in the BVW combinatorial-dimension class `Gr(d^pm)`, Definition 5.1 says

\[
p^{n-d^\pm+1/n}<\mu_Q\le p^{n-d^\pm}.
\tag{5.4}
\]

Choose the fixed BVW auxiliary `epsilon_0>0` so small that

\[
p+c_{\rm MedDim}\epsilon_0<0.51.
\tag{5.5}
\]

Then (5.2)--(5.4) imply

\[
(p+c_{\rm MedDim}\epsilon_0)^{n/r}
<
p^{n-d^\pm}.
\tag{5.6}
\]

For the upper medium threshold, (5.4) also gives

\[
p^{n-d^\pm}
<\mu_Q p^{-1/n}
\le100\,2^{1/n}n^{-1/2}.
\tag{5.7}
\]

BVW's constant `c_LgDim` may be fixed larger than its required lower bound; choosing it, say, above `200` makes (5.7) imply

\[
p^{n-d^\pm}<c_{\rm LgDim}n^{-1/2}
\]

for all sufficiently large `n`. Therefore every finite-field hyperplane produced from the corank-one `R2` event lies in the **medium** regime of BVW Proposition 5.4.

Finally, because the reduced rows span `H_Q` exactly, the realized event is exactly BVW's `A_H`, not the weaker containment event that caused the run58 audit gap.

## 6. The repaired R2 theorem

### Theorem C348 — the entire R2 sector is negligible at the sharp source scale

For iid uniform Rademacher `B_n`, with `E_R2` defined by (3.2),

\[
\boxed{
\Pr(E_{R2})=o(n^2 2^{-n}).
}
\tag{C348}
\]

#### Proof

The corank-at-least-two part is `2^{-2n+o(n)}` by C346.

For the corank-one part, C347 and (5.1)--(5.7) send each realization to a nontrivial BVW medium-dimension finite-field hyperplane `H_Q`, with the random rows spanning `H_Q` exactly. BVW Proposition 5.4 gives, for each admissible combinatorial-dimension class,

\[
\sum_{H\in\operatorname{Gr}(d^\pm)}\Pr(A_H)\le o(1)^n.
\tag{6.1}
\]

Their discretization set `D={a/n:0<=a<=n^2}` has only `n^2+1` classes. Hence

\[
\Pr(E_{R2},\operatorname{corank}B_n=1)
\le n^2 o(1)^n
=o(1)^n
=o(n^2 2^{-n}).
\tag{6.2}
\]

Together with C346 this proves C348. `square`

The same bound applies to the transpose version by distributional symmetry. In fact, for square singular matrices the row-span decomposition already classifies every realization, so no transpose copy is needed for the source-level conclusion.

### What C348 repairs

Blinovsky (18) attempts to import BVW Proposition 5.4 directly for arbitrary real `V` and a row-containment event. The exact repair is:

\[
\boxed{
\text{first split actual corank;}\quad
\operatorname{corank}\ge2\text{ by JSS,}\quad
\operatorname{corank}=1\text{ by C347 + BVW spanning.}
}
\tag{C349}
\]

Thus the `R2` regime is no longer a source-scale blocker for R03.

## 7. Method #19 — MAKE IT AN ALGORITHM: a deterministic classifier for the proof

The proof above can be viewed as an explicit classification procedure for any realized singular sign matrix in the `R2` union:

1. Compute its exact rank.
2. If corank is at least two, charge it to the published finite-support corank tail C346.
3. If corank is one, extract `n-1` independent rows and their real row hyperplane.
4. Choose a sufficiently large prime `Q`, reduce the basis, and form `H_Q`.
5. C347 preserves every sign-cube membership, so the `R2` mass interval is unchanged.
6. Assign `H_Q` to its BVW combinatorial-dimension class. Equations (5.5)--(5.7) force that class into Proposition 5.4's medium range.
7. Charge the realization to the exact BVW spanning event `A_H`.

This is not a finite checker and I do not manufacture one: every substantive claim here is theorem-sized and its proof is written on the page. The imported estimates are identified by precise primary-source theorem/remark/proposition.

## 8. What remains; no false closure

C348 removes the intermediate `R2` sector at a scale much smaller than the desired `n^2 2^{-n}` term. Run58 already gives a self-contained source-scale removal of all nontrivial minimal circuits whose support is at most

\[
n-\frac{(2+\epsilon)n}{\log_2 n},
\]

and run57 supplies an exact averaging/projection replacement for the false pointwise folding inequality encountered in the dense completion part of the current Blinovsky preprint.

These pieces are encouraging, but they are **not** yet a complete audited proof of

\[
r(n)=o(n^2).
\]

The main remaining obligation is an end-to-end treatment of the surviving near-full-support, actual-corank-one relations, including the exact separation of the trivial two-row/two-column collisions from all other mechanisms and a clean global assembly that does not inherit unchecked steps from the current preprint. Therefore this run is **PARTIAL**, not PROVED and not KNOWN.

No novelty claim is made for BVW or JSS. C347--C349 are a source-specific synthesis/reduction that repairs a concrete citation mismatch; whether this exact synthesis has appeared elsewhere was not established by the bounded search and is not needed for the present status.

## 9. Frozen metric and binding stuck/handoff rule

The numerical full-range metric remains

\[
\boxed{
r(11)\le522.9989062413841009635431653560194\ldots,
}
\]

with `r(10)` exact as in (1.5) and all retained `n>=12` branches unchanged.

The current explicit-reassignment movement sequence is:

- run55: metric moved;
- run56: metric moved;
- run57: no movement, streak `1`;
- run58: no movement, streak `2`;
- **run59: no movement, streak `3`.**

The earlier terminal F0001 history is not reset: run41 already recorded historical unchanged count `6` and a third-stuck handoff after two permitted recovery cycles. The current owner instruction explicitly required preserving that history. Therefore this new three-run fixed-metric stall does **not** authorize another F0001 recovery cycle. F0001 is handed off at the end of this report.

Current HARD reserve checking also blocks an honest immediate successor assignment. `QUEUE.md`'s previously READY/HARD entries I0078, I0079, and I0028 now each have current exclusive claim files (C27, R06, and HARD10-01 respectively). PENDING rows are not READY. I therefore do not steal a claimed problem or fabricate a successor. R03 enters **ROTATION / SUCCESSOR-ADMISSION HOLD** until a fresh eligible HARD OUTSIDE READY/unassigned target is source- and ownership-verified.

No shared root, peer file, claim file, scheduler, workflow, permission, email, Drive object, purchase, or public post is modified by this run.

## 10. Model/control status

Still unchanged. The exposed task-control surface does not provide a binding model-family selector, a reasoning-effort selector, or authenticated completed-run model telemetry. GPT-6/maximum is therefore prompt-only from this surface. The historical P26 `You cannot modify this task` result is authorization-context dependent; the legitimate workaround is the owning/authorized task-management context or platform support, never task duplication or permission bypass. No scheduler modification was attempted because the current owner instruction expressly forbids it.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R03
  lane: HARD_OUTSIDE
  target_before: F0001 iid Rademacher singularity sharp asymptotic
  source_status: OPEN_OR_UNCERTIFIED_CLAIM_EXISTS
  source_claim_note: "Blinovsky arXiv:1511.05283v7 claims the theorem; R03 has not certified its full proof"
  metric: "full-range normalized nontrivial remainder envelope r(n)"
  before:
    r10_exact: "222.6104736743168493957921796888577..."
    r11_upper: "522.9989062413841009635431653560194..."
  after:
    r10_exact: "222.6104736743168493957921796888577..."
    r11_upper: "522.9989062413841009635431653560194..."
  movement: false
  current_reassignment_no_movement_streak: 3
  historical_terminal_stuck_count: 6
  historical_stuck_count_reset: false
  methods_tried: [1, 11, 19]
  new_claims:
    - "C346: finite-support JSS corank remark gives P(corank B_n>=2)<=2^{-2n+o(n)}"
    - "C347: exact real-to-F_Q corank-one hyperplane transfer preserves all Rademacher cube memberships"
    - "C348: entire Blinovsky R2 sector is o(n^2 2^{-n})"
    - "C349: repaired R2 import = actual-corank split + JSS high-corank + exact BVW spanning transfer"
  novelty: "UNCLAIMED; source-specific synthesis/reduction"
  checker: "none; theorem-sized written proof with identified published inputs"
  status_after: "PARTIAL / F0001 HANDOFF / R03 SUCCESSOR-ADMISSION HOLD"
  handoff_reason: "third consecutive no-movement run in current post-movement sequence; prior F0001 terminal stuck history preserved; no additional recovery cycle allowed"
  successor: "NONE ASSIGNED: current READY/HARD candidates I0078, I0079, I0028 are now claimed; PENDING is not READY"
  remaining_mathematical_obligation: "near-full-support actual-corank-one nontrivial relations and end-to-end collision-excluded assembly for r(n)=o(n^2)"
```
