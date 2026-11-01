# BT4 fleet03/B06 — F3 saturation cover forces a short light-to-light cross

Run: `20260922T052316Z-fleet03-B06-BT4-r15`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-F3-MAJORITY-CROSS-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED` with one stronger local claim `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Target status: `OPEN_NOT_PROVED`

## Exact target and source boundary

The target is the genuine `k=4` Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the original statement, so digons count.

The current campaign source check is Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). The source check recorded in the owner target file says the genuine conjecture remains unresolved for every `k>=4`; the paper proves only the one-reversed-arc relaxation. Nothing below counts a relaxed or edge-disjoint cycle as a target cycle.

I use only the inherited minimum-counterexample normal form already established by the team: after the genuine `k=3` input removes digons one may work in an oriented exact-outdegree-seven counterexample; a globally minimum-total packing of three chordless directed cycles has an acyclic remainder; the graph is 3-vertex-strong; and every arc is dominated by a common predecessor.

## Named OTHER-account result consumed

The assigned partner is `fleet04/B04`. I consume its newest complete run

`20260922T051604Z-fleet04-B04-BT4-r14`

candidate `BT4-R4-ARCMAX-TRIANGLE-COLLAPSE-v1`, report blob
`2f802a03755394931009175d7b6a5f94b0b2b084`.

The partner refines the globally minimum three-cycle packing by maximizing the number of arcs in the acyclic remainder. In the four-remainder global-`NO-SIX` low-fan branch this proves:

1. the old remainder sink `x` is unique and every other old-remainder vertex sends to `x`;
2. the source light cycle is a directed triangle;
3. after the neutral source pivot, the F3 state has
   `q -> K`, where `K=R-{x}` has three vertices;
4. writing the source triangle before the pivot as
   `p -> q -> s -> p`, with `p->x` and `x->{q,s}`, the post-pivot packed source triangle is
   `S* = p -> x -> s -> p`;
5. every saturation triangle
   `T_r = q -> r -> x -> q`, `r in K`,
   has an external three-hit witness lying in `{p,u}`, where `u`, if it exists, is the unique vertex of the other light cycle `U` with `u->x`;
6. at most one vertex of `U` can enter `x`.

The partner's F3 unpaid step was to use this two-vertex cover together with the campaign's reciprocal/third-port interfaces to force a legal splice. The theorem below converts the cover itself into a concrete bounded light-to-light cross.

No peer outcome label is treated as proof; only the source-bound statements above are imported.

## Compact conditional end-to-end route

Assume BT4 false and enter the inherited exact-seven oriented minimum-counterexample normal form.

1. Choose the three-cycle packing lexicographically by minimum total packed order and, subject to that, maximum number of remainder arcs.
2. Enter the four-remainder global-`NO-SIX` source-pivot branch.
3. By the partner theorem, every surviving low-fan source is triangular and the F3 saturation triangles are covered by at most the two light inports `{p,u}`.
4. The theorem below proves that F3 always contains a cross between the two light supports whose interior has size at most one and lies in the remainder.
5. If both cover vertices witness at least two saturation triangles, the two opposite light-to-light crosses can be chosen with disjoint interiors.
6. The remaining target-level job is no longer to extract a cross from the F3 cover. It is to spend this short cross (or opposite pair) against the lead's reciprocal/third-port/heavy-entry interfaces to force two disjoint replacement cycles, a strict smaller packing, a cyclic exchanged remainder, SIX, or a fourth cycle. F2 and the separate SIX branch remain live.

## Theorem — BT4-R4-F3-MAJORITY-CROSS-v1

Work in the partner's arc-maximal triangular F3 state. Let

- `S* = p -> x -> s -> p` be the post-pivot packed source triangle;
- `U` be the other light packed cycle;
- `K={r1,r2,r3}` be the three old-remainder vertices other than `x`;
- `q` be the freed source vertex, so `q->K` and `K->x`;
- `T_r=q->r->x->q` for `r in K`.

For every `r in K`, let `p` witness `T_r` when `p->{q,r,x}` and let `u` witness `T_r` when `u->{q,r,x}`. The partner theorem says each `T_r` has at least one of these two witnesses, with `u` the unique possible `U`-inport to `x` when such an inport exists.

Define

`A={r in K : p witnesses T_r}`,
`B={r in K : u witnesses T_r}`.

Then:

1. `u` necessarily exists in every surviving F3 state.
2. `A union B = K`, hence `|A|>=2` or `|B|>=2`.
3. If `|A|>=2`, there is a directed cross from `U` to `S*` of one of the two exact forms

   `u -> p`, or `u -> r -> p` with `r in K\A`.

   Thus its interior is empty or one remainder vertex.
4. If `|B|>=2`, there is a directed cross from `S*` to `U` of one of the two exact forms

   `p -> u`, or `p -> r -> u` with `r in K\B`.

5. If both `|A|>=2` and `|B|>=2`, the two opposite crosses in (3)--(4) can be chosen with internally disjoint interiors.

### Proof

The cover statement gives `A union B=K`. Three objects covered by two sets imply at least one of `A,B` has size at least two.

Assume first `|A|>=2`. Dominate the arc `p->x`; let `d` be a common predecessor of `p` and `x`.

The vertex `d` cannot lie on the heavy cycle `H`, because the exact `(3,2,2)` state has `H not->x`. It cannot be `q`, because both `p->q` and `x->q` hold in the source-pivot geometry. It cannot be the third vertex `s` of `S*`, because `s->p` but `x->s`, and orientation forbids `s->x`. The endpoints `p,x` themselves are not common predecessors.

If `d` lies on `U`, uniqueness of the `U`-inport to `x` forces `d=u`; hence `u->p` is a direct `U->S*` cross.

Otherwise `d` lies in `K`. Since `d->p` and `p` witnesses every vertex of `A`, orientation forbids `d in A`: for `r in A` we have `p->r`. Therefore `d in K\A`. But `A union B=K`, so `d in B`, hence `u->d`. Thus

`u -> d -> p`

is a `U->S*` cross with sole internal vertex `d` in the remainder.

This also proves that `u` exists when `|A|>=2`. In particular, if the original cover had no `U`-inport, then `B` would be empty, so `A=K`; the domination of `p->x` would have no possible common predecessor, contradiction. Hence every surviving F3 state has a genuine `u`.

Now assume `|B|>=2` and dominate `u->x` by a common predecessor `d`.

Again `d` cannot lie on `H`. It cannot lie on `U`: `u` is the unique `U`-vertex entering `x`, so no other `U`-vertex can be a common predecessor of `u` and `x`. On `S*`, only `p` can enter `x`: `x->s` excludes `s->x`. Thus if `d` lies on `S*`, it is `p`, and `p->u` is a direct `S*->U` cross.

If `d` lies in `K`, then `d notin B`, because `u->d` for every `d in B` and orientation forbids `d->u`. Since `A union B=K`, this gives `d in A`, hence `p->d`. Therefore

`p -> d -> u`

is an `S*->U` cross with one remainder interior vertex.

Finally suppose both `A` and `B` have size at least two. In the indirect `U->S*` case the sole interior vertex lies in `K\A`; in the indirect `S*->U` case it lies in `K\B`. These two sets are disjoint because

`(K\A) intersect (K\B) = K\(A union B) = empty`.

Direct crosses have empty interior. Therefore the opposite crosses can always be chosen with disjoint interiors. QED.

## What the theorem changes

The partner's F3 terminal branch

`three saturation triangles covered by {p,u} -> splice?`

is now sharpened to

`F3 -> short light-to-light cross`,
and in the overlap subcase
`F3 -> internally-disjoint opposite light-to-light cross pair`.

The direction of the guaranteed one-way cross points toward the repeated witness:

- if `p` witnesses at least two saturation triangles, a short `U->S*` cross exists;
- if `u` witnesses at least two, a short `S*->U` cross exists.

Thus F3 no longer needs an arbitrary port-extraction argument merely to obtain a light-to-light transition. The next use of F3 should start with this bounded cross and combine it with the already existing reciprocal/third-port/heavy-entry interfaces.

## Exact symbolic-family check

The attached standard-library checker enumerates every witness-cover pattern for the three F3 saturation triangles. Each triangle is labeled `p`, `u`, or `both`, so there are exactly `3^3=27` assignments.

The enumeration gives:

- 13 assignments where both `p` and `u` repeat;
- 7 where only `p` repeats;
- 7 where only `u` repeats;
- 64 admissible common-predecessor scenarios across the repeated-witness cases;
- 37 paired dominator scenarios in the both-repeat case.

For every repeated-`p` scenario, every admissible common predecessor of `p->x` is either `u` or a vertex in `K\A`, which is automatically in `B`; hence it yields `u->p` or `u->r->p`. The symmetric assertion holds for repeated `u`. In every both-repeat paired scenario the two possible one-vertex interiors are disjoint.

This enumeration is only a sanity check of the finite cover logic. The theorem above is uniform and does not depend on the finite enumeration.

## Exact constrained full-graph certificate — the one-remainder interior is genuinely needed

A stronger shortcut is false:

> "In the arc-maximal triangular F3 state the light-to-light cross forced above can always be chosen direct."

The attached checker verifies a complete 18-vertex oriented digraph with all 126 arcs explicitly encoded. Its packed cycles are

`H=(0,1,2,3,4,5)`,
`U=(6,7,8,9,10)`,
`S*=(11,12,13)`,

with

`p=11`, `x=12`, `s=13`, `q=14`, `K={15,16,17}`, `u=6`.

It satisfies all of the following exact properties:

- every outdegree is exactly seven;
- the graph is oriented;
- `H,U,S*` are chordless directed cycles;
- every arc has a common predecessor;
- deleting any zero, one, or two vertices leaves a strongly connected digraph;
- the old remainder `{12,15,16,17}` is acyclic with unique sink `x=12`;
- the post-pivot remainder `{14,15,16,17}` is acyclic;
- all three size-neutral saturation-triangle exchanged remainders are acyclic;
- the old remainder has four induced arcs, and each of those three exchanged remainders also has exactly four induced arcs, so the secondary arc-max criterion is met with equality;
- the freed vertex has exact F3 profile
  `H:{2,3}`, `U:{8}`, `S*:{13}`, `R*:{15,16,17}`;
- the exact three-hit cover is
  `15 <- p`, `16 <- p`, `17 <- u`;
- the only common predecessor of `p->x` is `17`;
- there is no direct `u->p` arc, while the theorem's sharp indirect cross is exactly

  `6 -> 17 -> 11`.

Therefore the one-remainder interior in the theorem cannot be deleted using only the inherited local normal-form, arc-maximality and exchanged-remainder acyclicity hypotheses.

The certificate is deliberately **not** a BT4 counterexample. It contains the explicit four pairwise vertex-disjoint directed triangles

`(0,1,10)`,
`(2,3,8)`,
`(4,5,7)`,
`(6,13,11)`.

So the certificate refutes only the stronger "direct cross" lemma. It reinforces the campaign's recurring message: local exact-degree/connectivity/domination/acyclicity structure does not replace the global no-four-cycle-packing hypothesis.

Checker SHA-256:
`87ca325063e08d58cb1a8d660989a1fbc77aad09257a10ceac3a04c636e342b2`.

Checker-output SHA-256:
`123293c4da013e34e73e2c13589955f2b40259c90a7dafb8ada1514528c86e71`.

Validated payload SHA-256:
`5072a2a3a1709da26ffc7707a4989c743ba3e5e3b3927160a4d6a01041bda11f`.

## First exact unpaid implication

`BT4-R4-F3-SHORT-CROSS-SPLICE-v1`:

> In the arc-maximal triangular F3 state, combine the guaranteed short light-to-light cross from `BT4-R4-F3-MAJORITY-CROSS-v1` (or the internally-disjoint opposite pair when both cover vertices repeat) with the lead's reciprocal sink cross, third-port interface and endpoint-distinct heavy-entry crosses. Prove that the combined interfaces force either two vertex-disjoint replacement cycles, a strict smaller three-cycle packing, a directed cycle in an exchanged remainder, SIX, or a fourth directed cycle.

The new theorem removes "extract some light-to-light transition from the F3 cover" from this obligation. What remains is a genuine disjoint-splice problem. F2 and the separate SIX closure are not claimed closed.

## Honest status

`ESSENTIAL_STEP_APPLIED` with one local `CANDIDATE_REFUTED`.

New applied inference: the partner's F3 two-vertex witness cover always produces a concrete short cross between the two light supports, and overlap of the cover produces an internally-disjoint opposite cross pair.

Refuted stronger statement: the cross need not be direct; a complete exact-seven, arc-dominated, 3-vertex-strong, arc-maximal local certificate realizes the one-remainder interior.

BT4 remains `OPEN_NOT_PROVED`. No target-level proof, counterexample, publication claim, or novelty claim is made.
