# FOREST / account01-B03 — exact overlap-reconnection reduction

Run: `20260921T234923Z-b03-poprestore-r11`  
Campaign: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` / FOREST  
Outcome: **ESSENTIAL_STEP_APPLIED (exact reduction only; parent conjecture remains OPEN)**  
Assigned step: derive the conditioning/reconnection estimate needed by the common count comparison when cycles overlap, including disconnected forests and boundary cases.

## 1. Control transition and continuity

This invocation began under the older brain-population assignment. During the run, a fresh owner-control read changed B03 to FOREST and explicitly stopped new installation/benchmark work. No later brain-installation work is counted here. Existing installation artifacts were left unchanged.

The source-exact target is the Grimmett--Winkler uniform-unrooted-forest pairwise inequality: for every finite simple graph `G`, if `F` is uniform over all acyclic edge subsets, then for distinct edges `e,f`,

`P(e,f in F) <= P(e in F) P(f in F)`.

The exact prior history reread before this derivation included:

- `operations/claims/P0001.md`;
- `probability_campaign_2026_09/codex_20h_20260906/proofs/P0001_cactus_forests.md`;
- `runs/R02/20260918T0024Z_8c7d1e52.md`;
- `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- relevant P14/HARD10 and later forest-family search hits.

Those sources already show that the arbitrary finite-graph problem is not settled by cactus factorization, fixed small excess, complete-bipartite/tripartite classes, or generic decreasing-event conditioning. In particular the cactus note explicitly identifies overlapping cycles as the obstruction to the naive conditioning route.

The assignment names `account02/B01` as the cross-account partner. At the fresh shared-control snapshot used in this run, no current FOREST result from that partner was yet finalized in the coordination repository. Under the live order's missing-peer rule, I therefore reconstructed the minimal shared counting candidate rather than waiting. No peer PASS label is imported.

## 2. Four-cell count reduction

Fix distinct edges `e,f` of `G` and put

`K = G - {e,f}`.

Let `H` range uniformly over all forests of `K`. Define two addability indicators

`X(H) = 1{H + e is a forest}`,

`Y(H) = 1{H + f is a forest}`.

Let

`n_ij = #{H forest of K : X(H)=i, Y(H)=j}`

for `i,j in {0,1}`, and

`N = n_00+n_10+n_01+n_11`.

The overlapping-cycle correction is

`q = #{H : X(H)=Y(H)=1 but H+e+f is cyclic}`.

Because `H` is already a forest and each edge is individually addable in every forest counted by `q`, the graph `H+e+f` has exactly one new cycle, and that cycle contains both `e` and `f`.

Now partition the forests of `G` by which of the distinguished edges are present. If

- `A` = number containing neither `e` nor `f`,
- `B` = number containing `e` but not `f`,
- `C` = number containing `f` but not `e`,
- `D` = number containing both,

then exactly

`A = N`,

`B = n_10+n_11`,

`C = n_01+n_11`,

`D = n_11-q`.

Writing `Z` for the number of all forests, and `Z_e,Z_f,Z_ef` for the usual required-edge counts,

`Z=A+B+C+D`, `Z_e=B+D`, `Z_f=C+D`, `Z_ef=D`.

Hence the Rayleigh numerator satisfies the exact identity

`Z_e Z_f - Z Z_ef = BC-AD`

and therefore

**(R1)**

`Z_e Z_f - Z Z_ef = n_10 n_01 - n_00 n_11 + N q`.

This is valid for every finite simple graph, every distinct edge pair, disconnected `G`, disconnected `H`, adjacent or disjoint distinguished edges, and all component counts. No spanning/rooted/fixed-size substitution is used.

## 3. Exact probabilistic reconnection form

Under the uniform law on forests `H` of `K`,

`Cov(X,Y) = (n_00 n_11 - n_10 n_01)/N^2`

and

`P(Q) = q/N`,

where `Q` is the overlap event in the definition of `q`. Thus (R1) is equivalently

**(R2)**

`Z_e Z_f - Z Z_ef = N^2 [ P(Q) - Cov(X,Y) ]`.

Consequently the original Grimmett--Winkler inequality for the pair `e,f` is **equivalent**, not merely implied, to the following reconnection estimate:

**RECONNECTION(e,f).**

`Cov(X,Y) <= P(Q)`.

This isolates exactly what an overlapping-cycle argument has to pay. A proof that merely shows `Cov(X,Y)<=0` is stronger than necessary and, as shown below, is false even on four vertices. The overlap event supplies the indispensable positive slack.

## 4. Component-quotient characterization of the overlap term

Contract every connected component of `H` to one quotient vertex. Since `X=Y=1`, the images of `e` and `f` are nonloops in this component quotient. Then

`Q(H)=1`

if and only if the quotient images of `e` and `f` are parallel edges, i.e. they join the same unordered pair of `H`-components.

Proof: adding two nonloop edges to a forest creates a cycle precisely when the two new edges connect the same two pre-existing components. In that case the unique quotient cycle is the two-edge parallel cycle, which expands in `H+e+f` to the unique cycle containing both distinguished edges.

This has two useful terminal forms.

### Four distinct endpoints

If `e=ab` and `f=cd` with `a,b,c,d` distinct, `Q` is exactly the union of the two terminal connectivity patterns

`ac | bd` and `ad | bc`,

with the displayed two blocks distinct in the forest `H`.

### Adjacent distinguished edges

If `e=ab` and `f=ac`, then `Q` occurs exactly when `b` and `c` lie in one component of `H` and `a` lies in a different component.

Thus the shared-vertex case compresses to the five partitions of `{a,b,c}`. If their forest counts are

- `A = w_{abc}`,
- `B = w_{ac|b}`,
- `C = w_{ab|c}`,
- `D = w_{a|b|c}`,
- `Q = w_{a|bc}`,

then the same Rayleigh numerator is

**(R3)**

`Delta = BC - AD + Q(B+C+D+Q)`.

This is an exact five-state terminal formula for the arbitrary outside graph, not only a transfer-matrix family.

## 5. The correction term is exactly the common-cycle interaction

The overlap count has a simple structural zero/nonzero criterion:

**Lemma.** `q>0` if and only if `e` and `f` lie on a common cycle of `G`.

Proof. If `Q(H)=1`, the unique cycle in `H+e+f` contains both edges. Conversely, if a simple cycle `C` contains both, take `H=C-{e,f}` and select no other edges. Then `H` is a forest; `e` and `f` are individually addable; adding both recovers `C`, so `Q(H)=1`.

Hence `q` is not an artificial algebraic correction: it counts precisely the base forests in which the two candidate reconnections collide to make a common cycle. In particular, pairs in different cycle blocks have `q=0`; the known block factorization then gives zero correlation across distinct blocks.

## 6. Early adversarial test: the tempting overlap-free inequality is false

A natural but too-strong route would try to prove

`Cov(X,Y) <= 0`,

equivalently

`n_00 n_11 <= n_10 n_01`.

This fails in the smallest exact witness found by exhaustive checking.

Take `G=K_4-(2,3)` on vertices `0,1,2,3`, with

`e=(0,1)`, `f=(0,2)`.

Then `K=G-{e,f}` is the path with edges `(0,3),(1,3),(1,2)`, so all eight of its edge subsets are forests. Exact enumeration gives

`(N,n_00,n_10,n_01,n_11,q)=(8,1,0,1,6,3)`.

Thus

`Cov(X,Y)=6/64=3/32 > 0`,

while

`P(Q)=3/8`.

The overlap-free term is negative:

`n_10 n_01 - n_00 n_11 = -6`,

but the exact correction restores the true Rayleigh gap:

`Delta = -6 + 8*3 = 18 > 0`.

Equivalently the four distinguished-edge classes have

`(A,B,C,D)=(8,6,7,3)`,

so `Z=24`, `Z_e=9`, `Z_f=10`, `Z_ef=3`, and

`Z_e Z_f-Z Z_ef = 90-72=18`.

This witness is a counterexample only to the stronger overlap-free conditioning lemma, **not** to the Grimmett--Winkler conjecture.

## 7. Exact computational audit

`overlap_reconnection_check.py` independently enumerates every simple graph on at most five vertices and every present distinguished-edge pair. It verifies (R1) by two independently assembled count expressions and searches for the first failure of the false overlap-free estimate.

Archived output:

- edge-pair instances checked: `11766`;
- identity failures: `0`;
- first overlap-free failure: the four-vertex graph above;
- witness tuple: `(N,n00,n10,n01,n11,q,Delta)=(8,1,0,1,6,3,18)`.

The finite run is a consistency/adversarial check of the exact derivation, not evidence for the universal conjecture.

Checker commit: `e0405b8e84c82106e2b0a9e69d942e9e8ce2d2b5`.  
Output commit: `97ee7e09749cb2e5d2a14c90ebb091ebbd7ca1d1`.

## 8. What this changes in the common proof attempt

The first missing universal implication can now be stated without ambiguity:

> For `H` uniform over all forests of `G-{e,f}`, the positive covariance of the two edge-addability events is at most the probability that the two individually valid reconnections join the same pair of `H`-components.

That is (R2). Any injection/switching or separator decomposition used by the team should therefore charge a positive-covariance pair to **parallel reconnection states**, not attempt to erase all positive covariance.

A natural exact pair-count form for a switching proof is

**(R4)**

`n_00 n_11 <= n_10 n_01 + N q`.

The left side counts ordered pairs `(H_00,H_11)` of opposite addability types. The first term on the right is the desired ordinary switch target `(H_10,H_01)`; the second term supplies `N` possible partners for each overlap state `Q`. A successful universal proof can therefore be organized as an injection/weighted matching from the left pair set into the disjoint union represented on the right. No such universal injection is claimed in this run.

For four distinct endpoints the same obligation is a 15-terminal-partition inequality, with `q` supported only on the two cross-pair partitions `ac|bd` and `ad|bc`. For adjacent edges it is the five-state formula (R3). Those are finite boundary-state interfaces that separator/transfer approaches can target while still retaining the full unrooted forest multiplicities.

## 9. Remaining obligation and next recipient

The parent conjecture remains OPEN. This run does not prove (R4) in general and does not promote any claim to verified truth.

The immediate next mathematical step for the FOREST lead / switching workers is to construct a multiplicity-controlled map for (R4) that is allowed to land in the overlap reservoir `H x Q`. The four-vertex witness above should be kept as a mandatory regression: any proposed proof forcing `Cov(X,Y)<=0` or discarding `q` is false.

Suggested exact interface for `account02/B01` and the team lead:

1. work with the quotient-component characterization of `Q`, not arbitrary decreasing-event conditioning;
2. for a candidate separator, retain the terminal partition weights so that `q` survives gluing;
3. prove (R4) directly, or a stronger inequality that is first checked against the `K4-(2,3)` witness;
4. preserve disconnected forests automatically by keeping the base state space as all forests of `G-{e,f}`.

## 10. Integrity / scope

Manual scoped review of the three new files found only mathematical definitions, small graph data and repository-relative paths; no credentials, scheduler identifiers, machine paths, private transcripts, benchmark answers, or unrelated data are included. No public release, email, Drive action, scheduler mutation, production brain mutation, or permission change was performed.

`full_brain_connected=false`; this mathematics was done `WITHOUT_VERIFIED_BRAIN` because no authenticated current-run retrieval/receiver-context use occurred.
