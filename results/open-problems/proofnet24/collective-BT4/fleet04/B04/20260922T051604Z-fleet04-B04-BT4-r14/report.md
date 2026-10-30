# BT4 fleet04/B04 — arc-max remainder refinement collapses the four-remainder low-fan branch to a triangular source

Run: `20260922T051604Z-fleet04-B04-BT4-r14`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-ARCMAX-TRIANGLE-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Digons are allowed in the source statement.

The current external source boundary remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): its abstract explicitly says the genuine conjecture remains unresolved for every `k>=4` and proves only the one-reversed-arc relaxation. No relaxed cycle is counted as a directed cycle below.

This run deliberately changes proof mechanism after several local-pivot/collar runs: instead of another local port case analysis, it refines the globally minimum packing by a second extremal parameter, the number of arcs induced by its acyclic remainder.

## Exact inherited mathematics consumed

### Campaign lead

Latest complete team-lead package actually read:

- fleet02/B04 run `20260922T041847Z-b04-bt4-r11`, primary report `report.md`, blob `596929efe56393d3ab515544fa33ec6a19e75c83`;
- same-run controlling strengthening `strengthening.md`, blob `8bfc5b33fb232c8543856d6d9ad3b0e8fdc3432c`.

The inherited normal form is a hypothetical BT4 counterexample `D` that is oriented, has exact outdegree seven, is 3-vertex-strong and arc-dominated, together with a globally minimum-total packing `(H,S,U)` of three chordless directed cycles. Its remainder `R` is nonempty and acyclic. In the persistent global `NO-SIX` branch, a remainder sink `x` has fan pattern `(3,2,2)`; if `S` is a light source cycle with direct inport `p->x`, then

`N+(x) intersect S = {p+,p++}`

and the neutral source pivot

`S* = p -> x -> p++ -> S[p++,p]`

frees `q=p+` and changes the remainder to

`R* = (R-{x}) union {q}`.

The lead's newest heavy-triangle branch is controlled by its strengthening: in the exact-two-predecessor cage, two exact five-witnesses have no inport from their heavy target and therefore export two heavy-fan escape crosses; with at most one predecessor relation, the saturation triangles are covered by at most the two unique light inports. Its live missing step remains a genuine port-disjointness splice. This report does not claim that branch closed.

### Immediate same-slot predecessor

The fleet04/B04 report `20260922T041339Z-fleet04-B04-BT4-structural-r13`, blob `d113bed9a8c7d4573e4377ae39d98356ba50b4f8`, proves the post-source-pivot low-fan split at `|R|=4`. After excluding an immediate SIX output, a fan-at-least-three return cross, and a second neutral packed pivot, only these states remain:

- **F2-RONLY:** `d^+_{R*}(q)=2`; if `K=R-{x}`, then `q` dominates exactly two vertices of `K` and the third vertex `r0` satisfies `r0->q`; there is no direct `H/U` inport to `q`.
- **F3-SINGLEPORT:** `d^+_{R*}(q)=3`; hence `q` dominates every vertex of `K`; after labels the packed reverse interface is the single port `y^- -> q -> y` on the one-fan light cycle and there is no heavy-cycle inport to `q`.

### Named OTHER-account partner result

Newest complete fleet01/B05 result actually read and applied:

- fleet01/B05 run `20260922T043014Z-b05-bt4-r11`, candidate `BT4-R4-INPORT-TRIANGLE-3SWAP-v1`, report blob `96d3bc9140e9608b165d382851c332b3bbfa29be`.

In its long-source F2 configuration it assumes two distinct old-remainder sinks `x,y` and proves that the mixed inport triangle forces a size-neutral three-edge packed-cycle swap. Its resulting unpaid step is an orbit-closure statement for four-remainder neutral swaps. The theorem below shows that this two-sink long-F2 state cannot occur after a legitimate secondary extremal choice of the minimum packing. Thus the partner theorem remains a valid exchange for noncanonical minimum packings, but its two-sink orbit is removed from the canonical structural tree used here.

No peer outcome label is treated as a proof; only the source-bound statements above are imported.

## Compact conditional end-to-end route

Assume BT4 false.

1. Enter the inherited exact-seven oriented minimum-counterexample normal form.
2. Among all globally minimum-total three-cycle packings, choose one whose acyclic remainder induces the maximum possible number of arcs. This secondary choice does not weaken any of the lead's minimum-packing deductions.
3. Run the `SIX/NO-SIX` split. The separate SIX interface is still unpaid.
4. In `NO-SIX`, take a remainder sink `x` with source light cycle `S` and perform the canonical neutral source pivot. If the exchanged remainder is cyclic, four cycles already exist. Otherwise it is another globally minimum packing and is eligible for the secondary extremal comparison.
5. Existing work gives an immediate cross/SIX/second-pivot output or F2-RONLY/F3-SINGLEPORT. The theorem below proves that either low-fan exception forces the old sink to be the unique remainder sink and forces the source light cycle itself to be a directed triangle.
6. The latest partner's long-F2 two-sink orbit is therefore absent from this canonical representative. What remains is a short-light witness-cover splice, stated exactly below, together with the lead's heavy-triangle port-disjointness branch and the separate SIX branch.

## Secondary extremal choice

For any globally minimum-total packing `P=(C1,C2,C3)`, let

`R(P)=V(D) \ (V(C1) union V(C2) union V(C3))`

and define

`a(P)=|A(D[R(P)])|`.

Every such remainder is acyclic in a counterexample, because a directed cycle in it together with the three packed cycles would already be four disjoint cycles. Since `D` is finite, choose a globally minimum-total packing `P` maximizing `a(P)`.

All following sink and source-pivot notation refers to this arc-maximal minimum packing.

## Lemma 1 — the neutral source pivot saturates all old remainder-to-sink arcs

Assume `|R|=4` and the post-source-pivot state is F2-RONLY or F3-SINGLEPORT. Put

`K=R-{x}`,

so `|K|=3`, and let `q=p+` be the source vertex freed by the neutral pivot. Then every vertex of `K` sends an arc to `x`:

`K -> x`.                                                        (1)

Consequently `x` is the unique sink of the old remainder `D[R]`. Moreover the source-pivot packing is itself arc-maximal among globally minimum-total packings.

### Proof

Because `x` is a sink of the old acyclic remainder, it has no arc to a vertex of `K`. Hence, writing `e(K)` for the number of arcs induced by `K`,

`a(P)=e(K)+d^-_R(x)`,                                           (2)

with `d^-_R(x)<=3`.

The source pivot replaces `x` in the remainder by `q` and leaves every arc induced by `K` unchanged. In F3-SINGLEPORT, `q` sends to all three vertices of `K`. In F2-RONLY, `q` sends to exactly two vertices of `K` and the unique undominated vertex `r0` satisfies `r0->q`. Thus in either case `q` is adjacent, in exactly one direction, to every vertex of `K`, so the exchanged remainder satisfies

`a(P*)=e(K)+3`.                                                  (3)

The source pivot is size-neutral. If its remainder were cyclic, BT4 would already be closed in this branch; therefore in a counterexample `P*` is another globally minimum-total packing with acyclic remainder. By the secondary extremal choice,

`a(P)>=a(P*)`.

Combining (2) and (3) gives `d^-_R(x)>=3`. Since `|K|=3`, equality holds and every vertex of `K` sends to `x`, proving (1).

Every vertex of `K` therefore has an outgoing remainder arc to `x`; hence none is a sink of `D[R]`. Thus `x` is the unique remainder sink.

Finally (2)--(3) now give `a(P)=a(P*)`. Since `P` was arc-maximal, `P*` attains the same maximum and is itself arc-maximal. QED.

## Lemma 2 — every surviving low-fan source cycle is a triangle

Under the hypotheses of Lemma 1,

`|S|=3`.                                                         (4)

### Proof

In F2-RONLY the freed vertex `q` has two outneighbors in `K`; in F3-SINGLEPORT it has three. Choose any `r in K` with `q->r`.

The old source fan gives `x->q`, while Lemma 1 gives `r->x`. Hence

`T_r = q -> r -> x -> q`                                       (5)

is a genuine directed triangle. It is disjoint from `H` and `U`. Replacing the old source cycle `S` by `T_r` therefore gives a legal three-cycle packing `(H,T_r,U)` of total size

`|H|+3+|U|`.

The original packing is globally minimum, so

`|H|+|S|+|U| <= |H|+3+|U|`,

and therefore `|S|<=3`. The inherited counterexample is oriented, so it has no directed digon and every directed cycle has at least three vertices. Thus `|S|=3`. QED.

### Consequence for the partner's latest branch

The fleet01/B05 long-source F2 theorem starts from a configuration with two distinct old-remainder sinks `x,y` and `|S|>=6`. Lemmas 1 and 2 show that neither condition can hold in the arc-maximal minimum-packing representative of a surviving F2/F3 low-fan state: `x` is the unique old-remainder sink and `S` has exactly three vertices.

Therefore `BT4-R4-INPORT-TRIANGLE-3SWAP-v1` is not discarded; rather, it becomes a fallback exchange for noncanonical minimum packings, while its `R4-3SWAP-ORBIT-CLOSURE` is not an independent branch of the canonical structural tree.

## Lemma 3 — exact external-three-hit cover in the triangular F3 state

Write the now-forced source triangle as

`S = p -> q -> s -> p`,

with `p->x` and `x->{q,s}`. Let `K=R-{x}`. In F3-SINGLEPORT, `q->K` and `K->x`.

For every `r in K`, the directed triangle

`T_r=q->r->x->q`

has an external three-hit witness, by the genuine `k=3` deletion theorem used throughout the team: otherwise deleting `T_r` would leave minimum outdegree at least five and produce three cycles disjoint from `T_r`.

Every such witness lies in a set of size at most two:

`{p,u}`,                                                         (6)

where `u`, if it exists, is the unique vertex of `U` sending directly to `x`. Consequently one of `p,u` witnesses at least two of the three triangles `T_r`; if no `U`-inport to `x` exists, then `p` witnesses all three.

### Proof

A witness must send to `q`, `r` and `x`.

- It cannot lie on `H`, because the canonical `(3,2,2)` state has `H not->x`.
- It cannot be another vertex `t in K-{r}`, because F3 has `q->t` and orientation forbids `t->q`.
- On the triangle `S`, the vertex `s` cannot send to `q` because `q->s`; hence only the predecessor `p` can be an `S`-witness.
- On the other light cycle `U`, a witness must send to `x`. In a `(3,2,2)` light fan there is at most one direct inport from a fixed light cycle to `x`: if `u->x`, the source-fan-two equality locks `N+(x) intersect U` to `{u+,u++}`, whose predecessor `u` is unique.

Thus (6) holds. Three triangles covered by at most two witnesses give the final multiplicity assertion. QED.

## Lemma 4 — exact external-three-hit cover in the triangular F2 state

In F2-RONLY, label

`K={r0,r1,r2}`

so that

`r0->q`, `q->r1`, `q->r2`, and `K->x`.

For each `i=1,2`, the triangle

`T_i=q->r_i->x->q`

has an external three-hit witness lying in

`{p,u,r0}`,                                                      (7)

where again `u` is the unique possible `U`-inport to `x`.

### Proof

The same exclusions as in Lemma 3 apply to `H`, to `s`, and to `U` except for the unique possible inport `u`. The other q-dominated remainder vertex cannot send to `q` by orientation. The sole remainder vertex not dominated by `q` is `r0`, and F2-RONLY already gives `r0->q`; hence `r0` is the only possible remainder witness. This proves (7). QED.

## Structural theorem — BT4-R4-ARCMAX-TRIANGLE-COLLAPSE-v1

Choose the globally minimum three-cycle packing lexicographically by:

1. minimum total packed order;
2. subject to (1), maximum number of arcs induced by the acyclic remainder.

In the inherited `|R|=4`, global-`NO-SIX` source-pivot branch, after excluding an immediate SIX output, an already-proved fan-at-least-three return cross and a second packed neutral pivot, every surviving low-fan state has all of the following:

1. the old sink `x` is the unique sink of the old remainder and every other remainder vertex sends to `x`;
2. the source light cycle `S` is a directed triangle;
3. the neutral source-pivot packing remains arc-maximal for the same secondary criterion;
4. in F3, the three triangles `q->r->x->q` are covered by at most the predecessor `p` of `q` on `S` and the unique possible `U`-inport to `x`, so one of those two vertices hits at least two saturation triangles;
5. in F2, the two q-dominated saturation triangles are covered by at most `{p,u,r0}`, with `r0->q` the unique reverse remainder port;
6. the latest partner's two-sink long-source F2 orbit is absent from this canonical representative.

No larger-remainder or SIX conclusion is asserted.

## Updated structural case split

For the current four-remainder route, the canonical proof tree can now be organized as follows.

- **SIX:** separate support/remainder SIX interface, still unpaid.
- **Immediate exchange/cross:** the existing fan-at-least-three return cross or a second neutral packed pivot; these feed the common splice machinery.
- **Low-fan arc-max branch:** the only surviving F2/F3 state has a triangular source and unique old-remainder sink, with the exact witness covers of Lemmas 3--4.
- **Heavy-triangle saturation branch:** the latest lead strengthening leaves its two-port light-inport cover or double heavy-fan escape cage; this remains a separate genuine port-disjointness problem.

The fleet01/B05 long-source two-sink 3-swap branch is useful for noncanonical minimum packings but is no longer needed as a terminal branch after the arc-max refinement.

## First exact unpaid implication

`BT4-R4-ARCMAX-TRIANGLE-SPLICE-v1`:

> In the arc-maximal minimum-packing representative above, close the triangular low-fan states. In F3, use the two-vertex cover `{p,u}` of the three saturation triangles together with the lead's reciprocal/third-port interfaces to force two vertex-disjoint replacement cycles, a strict smaller packing, a cyclic exchanged remainder, or a SIX state. In F2, do the same from the two-triangle cover `{p,u,r0}` and the unique reverse port `r0->q`. No additional arbitrary long-source orbit or second old sink may be assumed.

This is narrower than the previous `R4-3SWAP-ORBIT-CLOSURE`: the secondary extremality theorem has already removed the long/two-sink part of that orbit.

## Failure checks and nonclaims

- The proof uses the oriented exact-seven inherited normal form. It does not silently prohibit digons in the original BT4 statement; orientation is an inherited minimal-counterexample reduction.
- The secondary extremal packing exists because `D` is finite. It is chosen only among already globally minimum-total packings.
- The comparison `a(P*)=e(K)+3` uses the exact F2-RONLY/F3 adjacency data; it is not asserted before those branches are reached.
- A neutral pivot is never counted as a fourth cycle. If its new remainder is cyclic, that cycle is the fourth; otherwise the pivot is only a state transition.
- The partner's theorem is not refuted. Its hypotheses are shown incompatible with this refined canonical representative.
- No finite census, tournament-only result, reversed-arc relaxation, benchmark material, remote computation or novelty-by-search-miss is used.
- No code was required for the combinatorial derivation.

## Honest outcome

`ESSENTIAL_STEP_APPLIED`.

New essential result: a legitimate secondary extremal choice of the globally minimum three-packing forces every surviving four-remainder F2/F3 low-fan source to be a directed triangle and forces its old remainder sink to be unique. This removes the long-source/two-sink neutral-swap orbit from the canonical structural tree and replaces it by two explicit short witness-cover configurations.
