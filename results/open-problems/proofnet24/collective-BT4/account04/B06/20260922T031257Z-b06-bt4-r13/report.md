# BT4 account04/B06 — neutral sink-port escape and two-light second interface

Run: `20260922T031257Z-b06-bt4-r13`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-SC-v2-inport-escape`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, hence directed digons, are allowed in the source problem.

The current external source boundary remains Stéphane Bessy, Matthijs Muis, Jean-Sébastien Sereni, Raphael Steiner and Sebastian Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract states that the genuine conjecture remains unresolved for every `k>=4`; the result proved there at the same `2k-1` threshold allows each packed cycle either to be directed or to become directed after reversing one arc. No such relaxed cycle is counted here.

The lower-`k` input retained from the campaign state is Lichiardopol--Pór--Sereni, *A Step toward the Bermond-Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992: minimum outdegree five gives three vertex-disjoint directed cycles, and their strengthened two-cycle theorem is the pair-deletion input used by the lead.

## Exact team state consumed

Latest complete team-lead package actually read:

- account02/B04 `20260922T022208Z-b04-bt4-r11`, report Git blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`;
- controlling correction Git blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`.

Named OTHER-account partner result actually applied:

- account01/B04 `20260922T024418Z-b04-bt4-r11`, candidate `BT4-MCR-v5-sink-cross-collapse`, report Git blob `bbf3afa52d8d0587ae5e210eecaacb7017ac672e`.

The exact partner theorem used below is its **canonical sink-cross theorem**: in the inherited normal form every sink `x` of the acyclic remainder has a direct packed inport `p->x`; if `S` is the packed cycle containing `p`, then

`m_S(x)=|N+(x) intersect S| <= 2`,

and because `x` is a remainder sink there is a different packed cycle hit by `x`. Among the two cycles other than `S`, one cycle `H` has `m_H(x)>=3`, and no vertex of `H` sends an arc to `x`.

The supporting domination lift is read from account02/B05 `BT4-RSC-v5-two-support-lift`, report Git blob `9727b3f919f8c071dd12a6e9c4baf0b631424b08`, with correction blob `ab145f55b225f7cbf6b807546ba240112d246786`. Its exact Lemma 1 says: if `z->rho` is an arc inside `R`, repeated arc domination terminates at a packed apex `a` and gives a directed path `a->...->z` with all internal vertices in `R`, while every ladder vertex, including `a`, also has a direct arc to `rho`.

I also retain account03/B05 `BT4-TCEX-v4-switchwall`, report blob `95b8f15691b688223206db39eee3085c9019ab5d`, only for the already proved fact that overlap of opposite cross/support paths can be switched into a same-support path or another cross interface. No peer outcome label is promoted to a theorem.

## Inherited normal form

Assume for contradiction that BT4 is false and work in the campaign's inherited normal form. Thus `D` is oriented, every vertex has outdegree exactly seven, `(A,B,C)` is a three-cycle packing of globally minimum total order, the remainder

`R=V(D)\(V(A) union V(B) union V(C))`

is nonempty and acyclic, the packed cycles are chordless, every arc is dominated, and `D` is 3-vertex-strong.

For an `R`-internal path of edge length `L` from a packed cycle `C` to `x in R`, put

`m_C(x)=|N+(x) intersect C|`.

The repaired path-fan inequality is

`L >= m_C(x)-1`.

The lead's equality-completion theorem says that equality gives an explicit globally minimum size-neutral replacement of `C`, with acyclic exchanged remainder. In the nonsaturated equality case the fan targets are exactly the first `m_C(x)` forward successors of the path's packed start.

The named partner has reduced the global frontier to the canonical sink-cross splice: start from a sink `x`, a direct inport `p in S -> x`, source fan `m_S(x)<=2`, and a heavy target cycle `H` with `m_H(x)>=3` and `H not->x`; turn that local object into a disjoint two-cycle replacement, a strict packing contradiction, or a fourth cycle. One cross transition alone is not enough.

This run attacks the source side of that exact splice.

## Lemma 1 — exact source-port classification

Let `x` be a remainder sink and let `p in S` satisfy `p->x`. Write `m=m_S(x)<=2`.

1. If `m=2`, then

   `N+(x) intersect S = {p+,p++}`.                              (1)

2. If `m=1` and `s` is the unique target of `x` on `S`, then the forward directed distance

   `d=d_S(p,s)`

   satisfies `d<=2`. Thus `s` is either `p+` or `p++`. If `s=p++`, then `p->x->p++` is a size-neutral replacement of the two-edge segment `p->p+->p++`.

### Proof

For `m=2`, the direct inport `p->x` has edge length `L=1=m-1`. The oriented cycle `S` has order at least three, so this is the nonsaturated equality case of the lead's repaired path-fan theorem. Equality-completion therefore gives exactly the consecutive fan targets (1).

For `m=1`, let `s` be the unique fan target. The directed path

`p -> x -> s`

followed by the forward segment `S[s,p]` is a directed cycle disjoint from the other two packed cycles. It has order `|S|+2-d`. If `d>=3`, replacing `S` by this cycle would strictly reduce the globally minimum total three-packing, impossible. Hence `d<=2`. For `d=2` the replacement is size-neutral. QED.

This leaves only two genuinely nonneutral direct-source possibilities before any further structure is used: `m=0`, or `m=1` with the unique source target equal to `p+`. Both lie in the partner's remainder-supported six-or-seven-fan side because the other two packed cycles receive at least six arcs from `x`.

## Lemma 2 — domination of a neutral inport forces a second interface

Assume now `m_S(x)=2`, so by Lemma 1

`N+(x) intersect S={p+,p++}`.

Let `H` be the heavy target cycle, `m_H(x)>=3`, and let `U` be the third packed cycle. Then at least one of the following holds.

**(X) Other-light-to-source cross.** There is a directed path

`Q: a -> ... -> p`

from a vertex `a in U` to `p in S`, with every internal vertex in `R`. Moreover `a->x` is an arc and therefore

`m_U(x)<=2`.                                                     (2)

**(W) Source return cycle.** There is a simple directed cycle `W` whose only packed vertex is `p`; all other vertices of `W` lie in `R`. Consequently

`|S| <= |W| <= |R|+1`.                                          (3)

In particular, if `|S|>|R|+1`, alternative (X) is forced.

### Proof

Dominate the inport arc `p->x`. There is a vertex `q` with

`q->p` and `q->x`.                                               (4)

First `q` cannot lie on `S`. Chordlessness says that the only vertex of `S` that can send to `p` is its predecessor `p^-`. If `q=p^-`, then `p^-->x` is another direct `S`-to-`x` path of length one. Since `m_S(x)=2`, equality-completion applied with start `p^-` would require

`N+(x) intersect S = {p,p+}`,                                   (5)

contradicting (1), which says the same set is `{p+,p++}``. Thus `q notin S`.

If `q` is packed, the direct arc `q->x` and the path-fan inequality imply that the fan of `x` into the packed cycle containing `q` is at most two. Hence `q` cannot lie on the heavy cycle `H`. It lies on `U`, and the arc `q->p` is already alternative (X), with `a=q`.

It remains that `q in R`. Apply account02/B05's exact finite domination lift to the internal remainder arc `q->x`. It gives a packed apex `a`, a directed path

`a -> ... -> q`

whose internal vertices lie in `R`, and the direct arc `a->x`.

Again the length-one path-fan inequality excludes `a in H`. Thus `a` lies on `S` or `U`.

If `a in U`, append the arc `q->p` from (4). This gives the cross path

`a -> ... -> q -> p`

with `R`-only interior, and the lift also gives `a->x`; hence (2). This is alternative (X).

Suppose instead `a in S`. Since `a->x` is another direct inport and `m_S(x)=2`, equality-completion forces

`N+(x) intersect S={a+,a++}`.

Together with (1),

`{a+,a++}={p+,p++}`.

On a directed cycle of order at least three, a proper consecutive two-vertex block has a unique predecessor, so `a=p`. The lifted path, followed by `q->p`, is therefore a directed closed walk

`p -> ... -> q -> p`

whose non-`p` vertices all lie in `R`. The lift has no repeated remainder vertex, so this is already a simple directed cycle `W`. It is disjoint from the other two packed cycles. Replacing `S` by `W` in the three-packing and using global minimality gives `|W|>=|S|`; because `W` uses only `p` plus vertices of `R`, `|W|<=|R|+1`. This is (3). QED.

### Why the heavy cycle cannot be the source in (X)

This exclusion is not a naming convention. Every packed apex produced above sends directly to `x`. A direct packed-to-`x` path has `L=1`, so the path-fan inequality gives fan at most two on its source cycle. The partner's heavy cycle satisfies fan at least three. Therefore every cross produced by Lemma 2 genuinely starts on the *other light cycle* `U`, not on `H`.

## Lemma 3 — domination of the far source-fan arc gives a second, port-separated output

Still assume `m_S(x)=2`, so `x->p+` and `x->p++`. Dominate the **far** fan arc `x->p++`. There is `q` with

`q->x` and `q->p++`.

Then one of the following holds.

1. there is an `R`-internal cross path from `U` to `p++ in S`, and its packed start also sends directly to `x`; or
2. there is an `R`-internal same-support path from `p` to `p++`.

In case 2, if `ell` is its edge length then `ell>=2`; equality is a size-neutral one-cycle exchange and `ell>=3` is a strict collar.

### Proof

A dominator `q` cannot lie on `S`. The only vertex of chordless `S` sending to `p++` is `p+`; but `p+->x` together with `x->p+` would be a digon, impossible in the oriented normal form. Thus `q notin S`.

If `q` is packed, the direct arc `q->x` again excludes the heavy cycle `H`, so `q in U`, giving case 1 directly.

If `q in R`, apply the finite domination lift to `q->x`. Its packed apex `a` sends directly to `x`, so `a notin H`. If `a in U`, appending `q->p++` gives case 1. If `a in S`, the same two-target uniqueness argument used in Lemma 2 forces `a=p`, and appending `q->p++` gives case 2. Global minimum applied to the replacement of the two-edge forward segment `p->p+->p++` gives `ell>=2`, with equality neutral. QED.

Thus the neutral source state carries *two independently forced interfaces*: domination of the inport `p->x` yields (X) or a closed source return, while domination of the far fan arc `x->p++` yields another `U`-to-`S` cross or a port-separated same-support bypass.

## Corollary 4 — long-light no-six sinks force opposite cross geometry

Assume the global `NO-SIX` sink pattern

`(m_H(x),m_S(x),m_U(x))=(3,2,2)`

up to relabeling, and suppose both light cycle orders satisfy

`|S|>|R|+1`,  `|U|>|R|+1`.                                     (6)

Then there is an `R`-internal cross transition from `U` to `S` and an `R`-internal cross transition from `S` to `U`, and both light cycles have their unique direct inports to `x`.

### Proof

Apply Lemma 2 to the direct inport `p in S -> x`. Condition (6) excludes alternative (W), so an `R`-internal `U`-to-`S` cross exists. The proof of Lemma 2 supplies a packed start `a in U` with the direct arc `a->x`.

Now apply Lemma 2 again with `U` as the source cycle and `a->x` as its direct inport. Its fan is two. The heavy cycle `H` is again excluded as the source of the second interface. The long-cycle condition `|U|>|R|+1` excludes the return-cycle alternative. Hence an `R`-internal `S`-to-`U` cross exists. QED.

No disjointness between the two cross interiors is asserted.

If the two opposite cross paths meet at a remainder vertex `w`, switch at `w`: the prefix of the `U->S` path to `w` followed by the suffix of the `S->U` path from `w` is an `R`-internal same-`U` path, and symmetrically the other two pieces form an `R`-internal same-`S` path. If an endpoint pair coincides, the corresponding closed walk contains a simple cycle through that packed port and otherwise in `R`. Hence overlap returns to the already quantified same-support exchange/collar interface. The only pure-cross residual may therefore be taken to have internally disjoint `R` interiors.

This is exactly the kind of disjointness-preserving normalization needed by the campaign: the old statement “a cross exists” is strengthened, in the long-light `(3,2,2)` case, to an **opposite light-cross pair**, and overlap of that pair is not an unstructured failure.

## Compact conditional end-to-end argument after this run

Combine the lead and the named account01/B04 partner as follows.

1. Reduce a hypothetical counterexample to the inherited exact-seven, oriented, arc-dominated, 3-vertex-strong normal form with a globally minimum three-cycle packing and acyclic remainder.
2. Pick a remainder sink `x`. The partner gives a direct packed inport `p in S -> x`, `m_S(x)<=2`, and a canonical length-two cross from `S` through `x` toward another packed cycle. A heavy target `H` has `m_H(x)>=3` and no direct inport to `x`.
3. Lemma 1 localizes the source port. If `m_S=1`, its unique source target is at forward distance at most two; distance two is already a neutral exchange. If `m_S=0`, or `m_S=1` with target `p+`, the partner's remainder-supported six-or-seven-fan branch remains.
4. If `m_S=2`, Lemmas 2-3 force a second interface: another light cycle enters `S`, or `S` has an explicit return cycle / same-support bypass. Long source cycles force the cross outcome.
5. In the no-six `(3,2,2)` state, if both light cycles are longer than `|R|+1`, Corollary 4 forces opposite light-to-light cross transitions. If those transitions overlap in `R`, switching yields same-support exchange/collar objects; otherwise one is left with two `R`-internally disjoint opposite light crosses, plus the common sink and its heavy-target fan.

Therefore the canonical sink-cross splice is no longer a one-cross local object in its neutral two-fan branch. It necessarily exports a second source-valid interface.

## Exact first remaining implication

BT4 is **not proved**. The first unpaid implication is now the following narrower splice statement.

> **(SC2) Two-interface sink splice.** In the inherited normal form, close either:
> 
> (a) the remainder-supported six/seven sink branch `m_S=0` or `m_S=1` with the sole adjacent source target `p+`; or
> 
> (b) the `m_S=2` branch after Lemmas 2-3, where there is a light-to-source cross, a source return cycle, or a same-support bypass. In the long-light no-six subcase this can be sharpened to two opposite light-cycle cross transitions with internally disjoint `R` interiors.
> 
> From those exact objects, construct two vertex-disjoint replacement directed cycles, a strictly smaller three-cycle packing, or a directed cycle in an exchanged remainder.

A single cross, a strict bypass, a return cycle longer than the old support, or one opposite cross pair is **not** silently counted as closure. In particular, two opposite directed cross paths generally make only one mixed directed cycle; an additional disjoint cycle or strict packing improvement must still be exhibited.

## Failure checks and nonclaims

- The target permits digons; orientation is used only in the inherited minimum-counterexample normal form after the source-valid digon reduction.
- Lemma 2 uses the domination lift only on an actual internal remainder arc `q->x`; if the dominator is already packed, no lift is invoked.
- The heavy-cycle exclusion uses the exact path-fan theorem with a direct path of edge length one; it does not assume a missing return by fiat.
- The uniqueness of the direct inport on a two-fan cycle follows from equality-completion's consecutive two-target block; it is not a tournament argument.
- A source return cycle in Lemma 2 may be longer than `S`; only the valid bound `|S|<=|R|+1` is claimed.
- A strict same-support bypass is not a contradiction; it remains a quantified collar.
- Opposite cross paths are not claimed vertex-disjoint unless their `R` interiors have explicitly been reduced to that residual case.
- No finite computation was used in this run.
- No full BT4 proof and no literature-novelty claim are made.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The named partner reduced the full campaign to the canonical sink-cross splice. This run pays the first neutral-source substep: a direct two-fan sink inport has rigid consecutive ports, and arc domination forces a second light-cycle/source interface. In the long-light no-six branch it forces opposite light-cycle cross geometry; overlap switches back to same-support exchange structure. The remaining target-level difficulty is the final disjoint two-cycle splice, plus the explicitly retained remainder-supported six/seven source branch.
