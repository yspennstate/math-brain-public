# FOREST / fleet01 B01 — published-source reconciliation of the Cocks bridge

**Run:** `20260922T010823Z-b01-forest-auto11`  
**Candidate:** `FOREST-KN-COCKS-REDUCTION-v2`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent Grimmett–Winkler conjecture:** **NOT PROMOTED / review gate open**  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and inherited theorem

The target is the Grimmett–Winkler uniform-forest pairwise negative-correlation conjecture: for every finite **simple** graph `G`, if `F` is uniform on **all** acyclic edge subsets (including the empty set, all sizes, and disconnected forests), then for distinct present edges `e,f`,

\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F).
\]

Equivalently, with `Z,Z_e,Z_f,Z_{ef}` the corresponding forest counts,

\[
\Delta_G(e,f)=Z_eZ_f-ZZ_{ef}\ge0.
\]

The latest lead theorem `FOREST-KN-HERMITE-REDUCTION-v1` proves the unit inequality for **every complete graph `K_n`** by an exact labelled-forest/Hermite calculation. The named OTHER-account partner `fleet02/B02`, run `B02-20260922T013646Z-forest-r12`, independently rederived the complete-graph formulas and exact inequalities; its later correction did **not** retract the `K_n` theorem. It instead challenged the scope of the Cocks/Semple–Welsh bridge. This run attacks exactly that first missing all-graphs implication.

## 2. Compact end-to-end argument

If the following published fixed-graph result is admitted exactly as stated in the final Semple–Welsh paper,

> if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated,

then the all-graphs proof is only three steps.

1. `FOREST-KN-HERMITE-REDUCTION-v1` gives the unit forest inequalities for every pair in every `K_n`.
2. The Cocks result, as recorded in the final published Semple–Welsh note, upgrades each fixed `K_n` to the all-positive-weight independent-set Rayleigh inequality for `M(K_n)`.
3. Semple–Welsh Proposition 3.5 proves that independence-correlated matroids are closed under minors. For an arbitrary simple graph `G` on `n` vertices, `M(G)` is the deletion minor of `M(K_n)` obtained by deleting the nonedges. Hence `M(G)` is independence correlated. Setting all surviving edge weights to `1` gives the required unit uniform-all-forests inequality on `G`.

No contraction, minimal-counterexample argument, finite-order census, or conditioning claim is needed. Isolated vertices are harmless: take `K_n` on the same vertex set and delete the absent edges. Graphs with fewer than two present edges have no pair to check.

Thus the sole source issue is whether the Cocks dependency available to this campaign is genuinely **fixed graph** or merely the older **class-level** equivalence.

## 3. The apparent Cocks contradiction is a version-history issue

The fleet02/B02 correction identified a real source hazard but compared two different versions of the Semple–Welsh text.

### 3.1 The 2005 working paper really is only class-level in the relevant proof

The University of Canterbury working-paper version (2005) states Proposition 2.1 as an equivalence between:

- the class of graphic matroids being independence correlated, and
- Conjecture 1.1 holding for all graphs.

Its converse proof begins with a bad positive weighting on `M(G)`, approximates/scales it to positive integers, and replaces every edge `x` by the corresponding number of parallel copies to make a generally different graph `G'`. It then invokes the unit conjecture on that enlarged graph. This proves a **class-level** equivalence; by itself it does not prove

\[
G\text{ unit-pNC}\Longrightarrow M(G)\text{ independence correlated}.
\]

That is exactly the mechanism isolated by the B02 correction.

### 3.2 The final 2008 paper deliberately changed Proposition 2.1

The final published Semple–Welsh paper no longer states the converse in Proposition 2.1. Its Proposition 2.1 gives only the easy implication

\[
[\text{all graphic matroids independence correlated}]
\Longrightarrow
[\text{Conjecture 1.1 for all graphs}].
\]

Later, Proposition 3.5 proves that independence-correlated matroids are closed under minors and explicitly remarks that this **does not itself show** that the unit-conjecture graph class is minor-closed.

Most importantly, the final note after their open questions then records a later result of Cocks: for a **graph `G`**, validity of Conjecture 1.1 on that graph implies that `M(G)` is independence correlated, and says this settles their fixed-graph Question (3).

The chronology matters: the parallel-copy argument belongs to the earlier working paper; it is not evidence that the later Cocks result has only that scope. The published paper has removed that old converse from Proposition 2.1 and separately attributes the stronger graph-local result to Cocks.

### 3.3 Independent source consistency checks

Cocks, *Correlated Matroids*, CPC 17 (2008), 511–518, states in its published abstract that it extends Semple–Welsh, establishes equivalences between the Grimmett–Winkler/Pemantle conjectures and correlated-graphic-matroid statements, and answers open questions from Semple–Welsh. That is consistent with the final-note chronology.

Oxley's later *Matroid Theory* summarizes the weaker class-level iff. This does not contradict the graph-local theorem; it simply does not state it. No later source located in this bounded check states that the final Semple–Welsh fixed-graph attribution is false.

Therefore the B02 correction is best interpreted as a **source-security warning against using the 2005 parallel-copy proof as a proof of the fixed-graph theorem**, not as a refutation of the theorem that the final peer-reviewed paper explicitly attributes to Cocks.

## 4. Exact complete-graph theorem, restated for the final reduction

For completeness, here is the load-bearing `K_n` calculation in compact form.

Let `R=ze^R`, `T=R-R^2/2`, `F=e^T`, and `A=T'=e^R`. For `K_n`, by edge transitivity let `E_n` be the number of forests containing one fixed edge, `J_n^{adj}` two adjacent fixed edges, and `J_n^{dis}` two disjoint fixed edges. Then

\[
Z_n=n![z^n]F,
\quad E_n=(n-2)![z^{n-2}]FA^2,
\]
\[
J_n^{adj}=(n-3)![z^{n-3}]FA^3,
\]
\[
J_n^{dis}=(n-4)![z^{n-4}]FA^4\left(1+\frac4{1-R}\right).
\]

For probabilists' Hermite polynomials `He_m`, Lagrange inversion yields

\[
m![z^m]e^{aR-R^2/2}=He_m(m+a)-mHe_{m-1}(m+a),
\]
\[
m![z^m]\frac{e^{aR-R^2/2}}{1-R}=He_m(m+a).
\]

Put `k=n-4`, `H_j=He_j(n+1)` and `s=kH_{k-1}/H_k`. Then

\[
J_n^{dis}/H_k=5-s,
\quad E_n/H_k=2n+6-3s,
\]
\[
Z_n/H_k=n^2+3n+10-(n+4)s.
\]

Hence the harder disjoint-pair Rayleigh gap has sign equal to

\[
G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14.
\]

All roots of `He_k` lie to the left of `x=n+1=k+5`, and root symmetry plus `\sum_i\lambda_i^2=k(k-1)` gives

\[
s=\sum_i\frac1{x-\lambda_i}
\ge
L_n:=\frac{(n-4)(n-1)(n+4)}{(n+1)^3}.
\]

Also `s<1` because `H_k-kH_{k-1}` is the strictly positive coefficient corresponding to `FA^4`. For `n\ge6`, `G_n` is increasing on `[0,1]`, and exact substitution gives

\[
(n+1)^6G_n(L_n)=
2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170.
\]

Writing `n=t+6` turns this into

\[
2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396>0.
\]

The adjacent count is smaller because `J_n^{dis}=J_n^{adj}+H_k` with `H_k>0`, so disjoint-pair positivity implies the adjacent case. The small complete graphs are exact: for `K_3`, `(Z,E,J_adj, gap)=(7,3,1,2)`; for `K_4`, `(38,14,4,44)` and disjoint gap `6`; for `K_5`, `(291,93,23,1956)` and disjoint gap `210`; for `K_6`, `(2932,822,178,153788)` and disjoint gap `13052`.

This run independently re-expanded the symbolic gap and the shifted positivity polynomial and re-enumerated `K_3,...,K_6`; all values above matched exactly.

## 5. What is proved now, and what is not

**Mathematical implication applied:** the source chronology removes the specific objection that the 2005 parallel-copy proof is the only basis for the fixed-graph Cocks theorem. The final published Semple–Welsh paper explicitly records a later graph-local Cocks result, and its own proposition numbering/text changed between the working paper and final version in exactly the way expected if the old class-level argument was superseded by a later theorem.

**End-to-end chain available:**

\[
\boxed{
K_n\text{ unit theorem for every }n
\xRightarrow[\text{Cocks, as recorded by final S--W}]{\text{fixed graph}}
M(K_n)\text{ independence correlated}
\xRightarrow[\text{S--W Prop. 3.5}]{\text{deletion minor}}
G\text{ unit-pNC for every simple }G.
}
\]

**Why this run is not labelled `FULL_PROOF_CANDIDATE`:** the campaign's promotion rule requires two independent existing-worker end-to-end reviews. One independent partner audit (`fleet02/B02`) fully passed the complete-graph calculation but later suspended the global closure because of the version ambiguity resolved here. I do not silently convert that earlier review into approval of this corrected source reconciliation, and I have not located a second completed end-to-end review of the exact v2 chain. The honest status is therefore `ESSENTIAL_STEP_APPLIED`, with a very short review target rather than a newly unpaid mathematical lemma.

## 6. Required independent review target

A reviewer now needs to check only four load-bearing items end to end:

1. the exact `K_n` Hermite derivation and the `G_n(L_n)>0` argument;
2. the **final published** Semple–Welsh note's graph-local attribution to Cocks, distinguished from the 2005 working-paper parallel-copy proof;
3. Semple–Welsh Proposition 3.5 minor closure for independence-correlated matroids;
4. the deletion identity `M(G)=M(K_n)\setminus(E(K_n)\setminus E(G))` and specialization of positive weights to all ones.

If two independent existing workers pass those four items without a new source objection, this chain meets the mathematical scope of the parent conjecture. If a reviewer obtains the body of Cocks's paper and finds that the final Semple–Welsh attribution was misstated, the chain must be retracted immediately; no such contradiction was found in this run.

## 7. Sources and peer artifacts consumed

- Grimmett–Winkler, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444–460, Conjecture 1.1.
- Semple–Welsh, **2005 working-paper version**, *Negative correlation in graphs and matroids*, University of Canterbury report: class-level converse via rational approximation and parallel copies.
- Semple–Welsh, **final published version**, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), 423–435: final Proposition 2.1, Proposition 3.5, and final note recording the graph-local Cocks result.
- C. C. Cocks, *Correlated Matroids*, CPC 17 (2008), 511–518, DOI `10.1017/S0963548308009152`.
- Oxley, *Matroid Theory*, 2nd ed., negative-correlation discussion: class-level summary, used only as a consistency check.
- `fleet02/B02`, `B02-20260922T013646Z-forest-r12`: independent Hermite audit plus `cocks_scope_correction.md`; the correction is explicitly consumed and answered, not ignored.
- Earlier P14/HARD10 source reconciliation: retained as historical source work, but not counted as a required new end-to-end review.

No novelty claim is made from a search miss. The external-status label remains source-conservative until the review gate is satisfied.
