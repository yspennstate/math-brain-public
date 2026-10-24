# BT4 account03/B05 — long-light opposite crosses force a third packed port

Run: `20260922T034032Z-account03-B05-BT4-r13`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-SC2-THIRD-PORT-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and role

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, hence directed digons, are allowed in the source problem.

This B05 role is the disjointness-preserving exchange step. The report works only inside the team's inherited minimum-counterexample normal form and does not claim BT4.

## Exact source and peer state consumed

The source boundary remains the campaign target record: the genuine `k=4` Bermond--Thomassen case is open; the 2026 Bessy--Muis--Sereni--Steiner--Wiederrecht relaxation permits one reversed arc per packed cycle and is not substituted for a directed cycle. The genuine lower-`k` input retained by the team is Lichiardopol--Pór--Sereni: minimum outdegree five gives three vertex-disjoint directed cycles.

Named OTHER-account partner actually applied:

- account04/B06, `BT4-SC-v2-inport-escape`, run `20260922T031257Z-b06-bt4-r13`, report blob `2c05883b0f7629a4a7691130f2925190283e6b11`, shared handoff blob `84bef161b645b0ec72893a37f52770e3aa4444c3`.

The exact partner input used is its long-light `NO-SIX` consequence. In the inherited normal form, for a remainder sink `x` with fan pattern `(3,2,2)` on packed cycles `(H,S,U)`, if `|S|>|R|+1` and `|U|>|R|+1`, then the two light cycles have unique direct inports `p in S -> x` and `a in U -> x`, with

`N+(x) intersect S = {p+,p++}`,
`N+(x) intersect U = {a+,a++}`,

and there are opposite `R`-internal light-to-light cross transitions. If their `R` interiors meet, the partner/switching machinery already returns to a same-support exchange/collar object. Therefore the pure-cross residual may assume internally disjoint `R` interiors.

I also use the team's already-source-bound finite domination lift: for an internal remainder arc `z->rho`, repeated arc domination terminates at a packed apex `c`, and in particular yields the direct arc `c->rho`. No outcome label is promoted in place of the theorem statement.

## Inherited normal form

Assume for contradiction that BT4 is false. Work in the inherited oriented exact-outdegree-seven counterexample `D` with a globally minimum-total three-cycle packing `(H,S,U)`, nonempty acyclic remainder

`R = V(D) \ (V(H) union V(S) union V(U))`,

chordless packed cycles, every arc dominated, and 3-vertex-strongness.

The partner has reduced the long-light no-six sink branch to the pure opposite-cross residual described above. This run changes mechanism from the previous overlap/switching attack: it combines the genuine `k=3` deletion threshold with domination to force a third packed port.

## Lemma 1 — the opposite crosses have the same two packed ports

In the long-light `(3,2,2)` branch, the partner's first cross can be written

`P : a -> ... -> p`,

with all internal vertices in `R`, where `a in U` and `a->x`. Applying the same inport-escape lemma with `U` as source gives an opposite cross

`Q : b -> ... -> a`,

where `b in S` and `b->x`.

Then `b=p`. Hence the pure-cross residual contains opposite paths

`P : a -> ... -> p`,
`Q : p -> ... -> a`                                                     (1)

with disjoint `R` interiors.

### Proof

For a two-fan direct inport `q->x` on a light cycle `T`, equality-completion forces

`N+(x) intersect T = {q+,q++}`.

For `T=S`, the fixed inport `p->x` gives the set `{p+,p++}`. If `b->x` is another direct `S` inport then also

`{b+,b++}={p+,p++}`.

A directed cycle of order at least three has a unique predecessor for a given proper consecutive two-vertex block, so `b=p`. The same argument gives uniqueness of `a` on `U`. QED.

Neither path in (1) contains `x`. Indeed `x` is an `R`-sink, so it cannot be an internal vertex followed by another remainder vertex; and it cannot be the last internal vertex because orientation plus the inport identities give `x not->p` and `x not->a`.

Thus, when the two `R` interiors are disjoint, their union is a simple directed cycle

`K = P union Q`                                                         (2)

meeting the old packing exactly in the two vertices `{p,a}` and avoiding `x`.

Among all pure-cross pairs (1), choose one for which `|V(K)|` is minimum.

## Lemma 2 — every directed cycle in a BT4 counterexample has an external three-hit witness

Let `C` be any directed cycle in `D`. Then some vertex `v outside C` has at least three outneighbors on `C`.

### Proof

Otherwise every vertex of `D-C` loses at most two outneighbors when `C` is deleted. Since `d_D^+(v)=7`, every vertex of `D-C` has outdegree at least five in `D-C`. The genuine `k=3` Bermond--Thomassen theorem therefore gives three vertex-disjoint directed cycles in `D-C`; together with `C` they are four vertex-disjoint directed cycles in `D`, contradiction. QED.

Apply Lemma 2 to `K`. The sink `x` is not a witness: it has no outneighbor in the `R`-interior of `K` because it is an `R`-sink, and it has no arc to either packed vertex `p,a` because `p->x` and `a->x` in an oriented digraph. Hence

`|N+(x) intersect K|=0`.                                               (3)

Let `v outside K` be a three-hit witness for `K`. Since `K` has only two packed vertices, at least one of the three hits is a vertex

`r in V(K) intersect R`.                                               (4)

## Lemma 3 — an internal hit forces a port-separated packed interface

Let `r` be as in (4), lying on one of the two directed arms of `K`. Write that arm as

`L : s -> ... -> r -> ... -> e`,                                      (5)

where `{s,e}={p,a}` and `s,e` lie on different light cycles.

Then there is a packed vertex `c notin {p,a}` such that

`J : c -> r -> L -> e`                                                 (6)

is an `R`-internal packed-to-packed path. Consequently either:

1. `c` and `e` lie on different packed cycles, so (6) is a genuine cross-packed transition with a packed endpoint outside the common bottleneck `{p,a}`; or
2. `c` and `e` lie on the same packed cycle, with `c!=e`, so (6) is a genuine same-support bypass with distinct packed ports. If its edge length is `ell` and the forward support distance from `c` to `e` is `d`, global minimum of the three-cycle packing gives `ell>=d`; equality is a size-neutral one-cycle exchange and `ell>d` is a strict collar.

### Proof

If the three-hit witness `v` is packed, put `c=v`. Then the arc `c->r` already exists.

If `v in R\V(K)`, apply the finite domination lift to the internal remainder arc `v->r`. It supplies a packed apex `c` with the direct arc `c->r`. Thus in either case (6) exists and has only remainder vertices internally.

It remains to show `c notin {p,a}`.

First suppose `c=s`, the source endpoint of arm (5). Since `r` is internal to `L`, replacing the prefix `sLr` by the single arc `s->r` gives a strictly shorter `s`-to-`e` arm whose interior is a subset of `int(L)`. It therefore remains internally disjoint from the opposite arm of `K`, contradicting the minimum choice of `K`.

Now suppose `c=e`, the terminal endpoint of arm (5). Then

`W = e -> r -> L -> e`

is a simple directed cycle whose only old packed vertex is `e`; all other vertices lie in `R`. If `e` lies on light cycle `T`, then `W` is disjoint from the other two old packed cycles, so replacing `T` by `W` gives another legal three-cycle packing. Global minimum yields

`|T| <= |W| <= |R|+1`,

contradicting the long-light hypothesis `|T|>|R|+1`.

Hence `c` is a packed vertex distinct from both bottleneck ports. The final cross/same-support dichotomy is immediate. In the same-support case, replacing the forward `T[c,e]` segment by `J` gives a legal cycle disjoint from the two untouched packed cycles, so global minimum gives `ell>=d`, with equality exactly size-neutral. QED.

## Theorem — two-port pure-cross closure reduces to a third-port interface

> **BT4-SC2-THIRD-PORT-v1.** In the partner's long-light `NO-SIX` sink state `(3,2,2)`, after reducing intersecting opposite cross paths by switching, the remaining internally-disjoint opposite-cross pair cannot persist as an isolated two-port obstruction. Choose a minimum such pair. Then the resulting two-port return cycle `K` forces, via the genuine `k=3` deletion theorem and finite domination, either
>
> - a genuine cross-packed transition with at least one packed endpoint outside `{p,a}`, or
> - a same-support bypass with two distinct packed ports and the exact minimum-packing tax `ell>=d` (equality neutral, strictness a collar).
>
> In particular, neither the common-port return cycle itself nor the sink `x` can be the terminal obstruction.

### Proof

Lemmas 1--3. QED.

## Why this is a disjointness-preserving advance

The previous SC2 residual had two opposite cross paths but they could close at the same ports `p,a`, so their union produced only one mixed cycle and could not be counted as two replacement cycles. The theorem above attacks exactly that bottleneck. It does not invent disjointness: instead it takes a minimum genuine opposite pair, forms its actual directed cycle, invokes the source-valid three-cycle theorem only after verifying the exact outdegree-loss threshold, and forces a third packed port. A same-support output is kept as a quantified exchange/collar rather than promoted to a contradiction.

This is a materially different mechanism from the prior switch-at-overlap argument and is therefore also the required mechanism change after repeated runs at the cross-splice frontier.

## Compact conditional end-to-end argument after this run

A complete BT4 proof would follow after the remaining closures below.

1. Reduce a hypothetical counterexample to the inherited exact-seven, oriented, arc-dominated, 3-vertex-strong normal form with globally minimum packing `(H,S,U)` and acyclic remainder.
2. Pair deletion gives the campaign's SIX / five-witness alternatives. Existing work reduces the neutral no-six sink branch to SC2.
3. In the long-light `(3,2,2)` SC2 branch, partner account04/B06 gives opposite light crosses; overlap switches to same-support structure.
4. In the internally-disjoint pure-cross residual, this report proves `BT4-SC2-THIRD-PORT-v1`: the common two-port obstruction forces a third packed port or a distinct-port same-support bypass.
5. The remaining first implication is now to splice that **port-separated third interface** with one arm of the minimum return cycle, or to close its strict same-support collar, into two vertex-disjoint replacement cycles / a strict smaller three-packing / an exchanged-remainder cycle. The separate remainder-supported SIX/seven sink branch is still unpaid.

## Failure checks and nonclaims

- A single cross, an opposite cross pair, or a strict same-support bypass is not counted as BT4 closure.
- Lemma 2 uses the genuine minimum-outdegree-five `k=3` theorem on `D-K`; it does not use the 2026 one-reversal relaxation.
- The domination lift is used only for an actual internal `R` arc `v->r`; a packed witness needs no lift.
- The long-light inequalities are essential to exclude the one-port return `c=e`; without them that branch remains possible.
- Minimum choice of `K` is only among genuine internally-disjoint opposite `p<->a` cross pairs already supplied by the partner; no existence is inferred from an average.
- No finite computation and no literature-novelty claim are used.
- Full BT4 remains open.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The assigned partner's SC2 opposite-cross state has been advanced from an isolated common-port pair to a forced third-port packed interface or a distinct-port same-support exchange/collar. The first unpaid disjointness-preserving implication is correspondingly narrower: close the third-port splice (or its strict collar) rather than manufacture a second cross from scratch.
