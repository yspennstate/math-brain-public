# account01/B05 BT4 proof attempt — 20260922T085440Z-b05-bt4-r11

Outcome: `ESSENTIAL_STEP_APPLIED`  
Result: `BT4-F3-R3-PIVOT-GUARD-v1`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Controls and source-bound dependencies


The latest complete campaign-lead handoff actually consumed is account02/B04 `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, shared handoff `BT4-HANDOFF-account02-B04-20260922T0619Z.md`, blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`. It keeps the proof in the oriented exact-outdegree-seven, 3-vertex-strong, arc-dominated, globally minimum three-cycle packing framework and warns that CROSS/BYPASS existence alone is not a fourth cycle.

The named OTHER-account partner result actually consumed and applied is account02/B06 `BT4-RANK2-PORT-PARITY-v1`, report blob `0e2262187f4ba70675c24940d913532224bc88c1`. It proves that bidirectional rank-two connectors splice canonically only when both support port orders are non-`BLOCK` and have matching `ID/SW` parity. Its explicit strong adversary rules out any argument that treats rank two alone as an automatic splice. This run therefore tracks pivot-induced support order changes rather than claiming an unsupported connector closure.

## Inherited local state

Work in the residual-three F3 return branch produced by the existing campaign exchange. There is a three-cycle packing `P` covering `n-3` vertices, while a globally minimum three-cycle packing covers `n-4`. Its residual set `R={t,r,s}` is acyclic. We are in the survivor with:

1. no fourth disjoint directed cycle;
2. no pair-SIX output;
3. no cyclic residual;
4. no exact-R4 compression already obtained;
5. the residual sink `t` has fan profile `(3,2,2)` into the three packed cycles;
6. on a light packed support `Z`, there is a tight pivot at a packed vertex `b`:
   `b->t`, `t->b+`, and `t->b++`.

The previous B05 defect-one collar is used as an established local lemma: for any residual sink `w`, any packed cycle `Y`, any packed `c in Y` with `c->w`, and any `a in N+(w) intersect Y`, the support-correct replacement

`c -> w -> a -> Y[a,c]`

combined with the other two packed cycles gives

`d_Y(c,a) <= 3`.

If some target has support distance exactly three, the replacement covers exactly `n-4`, hence is a new globally minimum exact-R4 packing.

## The pivot and exact vertex accounting

Let

`x := b+`, `c := b++`.

Execute the tight pivot

`Z' = b -> t -> c -> Z[c,b]`.

Then

`V(Z') = (V(Z) \ {x}) union {t}`

and the new residual is exactly

`R' = (R \ {t}) union {x} = {r,s,x}`.

The other two packed cycles are unchanged. Thus the new packing still covers exactly `n-3` vertices. The ambient arcs

`b->x` and `t->x`

remain present: `b->x` was the omitted old support edge and `t->x` was one of the tight fan arcs.

## New Lemma 1 — fresh hole cannot be the next sink

**Lemma (`BT4-F3-R3-FRESH-HOLE-NONSINK`).** In the no-SIX/no-R4 survivor above, the newly exposed vertex `x` is not a sink of `D[R']`.

### Proof

Assume `x` is a sink of `D[R']`. Since the exact normal form has `d+(x)=7`, all seven outneighbors of `x` lie on the three packed cycles. Absence of pair-SIX means every pair of fan counts has sum at most five. Therefore every fan count is at least two, and the three counts are exactly a permutation of

`(3,2,2)`.

Let `m = |N+(x) intersect Z'|`. Thus `m` is either two or three. The packed return `b->x` lets us apply the defect-one collar on `Z'`: every target `a in N+(x) intersect Z'` lies within support distance at most three forward from `b`.

On `Z'` the first successor of `b` is `t`. Orientedness gives both

- `x !-> b`, because `b->x`;
- `x !-> t`, because `t->x`.

Hence among vertices at forward distances `0,1,2,3` from `b`, only the distance-two and distance-three vertices are even available as `x`-targets.

If `m=3`, there are only two available vertices, contradiction.

If `m=2`, both available positions must be used, in particular there is a target `a` at forward distance three. The support-correct replacement

`b -> x -> a -> Z'[a,b]`

reduces the current `n-3` packing by exactly one packed vertex, producing a three-cycle packing covering `n-4`, i.e. an exact-R4 globally minimum packing. That contradicts the no-R4 survivor assumption.

Therefore `x` is not a residual sink. QED.

### Immediate consequence

Because `R'` is an acyclic three-vertex digraph and `x` is not a sink, at least one of the two retained old residual vertices `r,s` is a sink. Thus a tight pivot cannot simply move the sink onto the support successor that it exposes.

## New Lemma 2 — persistence guard

The preceding proof is not merely one-step. Suppose later size-preserving pivots occur but the packed support `Z'` is not modified. The vertex `x` may remain residual while other residual vertices are swapped into other packed supports. If at any such later stage `x` became a residual sink, then:

- the packing would still cover `n-3`;
- `b->x` and `t->x` would still be ambient arcs;
- `b->t` would still be a support edge of the unchanged `Z'`;
- no-SIX would again force at least two `x`-targets on `Z'`.

The same distance-three argument would force exact R4. Hence:

**Persistence guard.** In a no-SIX/no-R4 pivot orbit, the exposed hole `x` cannot become a residual sink while the support edge `b->t` survives unchanged in the packed cycle.

For a later tight pivot on `Z'`, the only way to destroy that protected support adjacency is to pivot at `b` (which removes `t`) or at the predecessor `b^-` of `b` (which removes `b`). Pivots at all other sites leave the support edge `b->t` intact. Therefore any no-R4 orbit that later promotes `x` to a sink must first perform a **local guard-breaking pivot** at one of those two neighboring sites.

This is a genuine localization of the pivot orbit: arbitrary remote repivoting of the same support cannot release the old hole.

## New Lemma 3 — two distinct supports force the next sink

Let the first pivot be on light support `Z`, exposing `x`, so the residual is `{x,r,s}`. Let the next residual sink be `r`, and suppose its tight pivot is executed on the *other* light support `W`, exposing `y`. The new residual is

`{x,s,y}`.

The fresh-hole lemma says `y` is not a sink. The support `Z'` from the first pivot was untouched by the second pivot, so the persistence guard says `x` is not a sink. Since the three-vertex residual is acyclic, it has a sink. Therefore:

`boxed: s is the unique possible residual sink after two consecutive pivots on distinct light supports.`

This is an exact queue rule, not a heuristic. It accounts for every residual vertex: the first sink `t` entered `Z`, the second sink `r` entered `W`, the holes `x,y` were exposed, and the sole twice-retained residual vertex `s` is forced to be the next sink.

## Compact conditional end-to-end route after this run

The current F3 residual-three branch now has the following conditional chain:

1. If the sink fan gives pair-SIX, hand off to the established SIX branch.
2. If a residual becomes cyclic, its directed cycle plus the three packed cycles closes BT4.
3. If a defect-one replacement has support distance three, it produces an exact-R4 globally minimum packing and the exact-R4 machinery restarts.
4. Otherwise a light return gives a tight pivot.
5. Every tight pivot exposes a fresh hole that is not the next sink.
6. That hole remains forbidden as a sink until its own support is modified at one of two local guard-breaking sites.
7. Two consecutive pivots on different light supports force the unique next sink to be the residual vertex retained through both pivots.
8. If the evolving state yields bidirectional rank-two connectors, account02/B06 `BT4-RANK2-PORT-PARITY-v1` must be applied literally: a two-splice is credited only for matching non-`BLOCK` port parity. A `BLOCK`/parity-mismatch state remains debt rather than being silently treated as a fourth cycle.

Thus the old vague `PIVOT-ORBIT-CLOSE` debt has been reduced to a finite local choreography: a surviving orbit must repeatedly break the protected adjacency of an earlier hole by a neighboring same-support pivot, or alternate supports according to the forced three-vertex sink queue, while simultaneously avoiding R4, SIX, cyclic residual, and any parity-compatible rank-two splice.

## First essential missing implication

`BT4-F3-R3-LOCAL-PIVOT-ORBIT-CLOSE-v1`:

> In the residual-three F3 survivor, prove that the forced queue plus the local guard-breaking rule cannot form a finite periodic orbit without producing exact R4, pair-SIX, a cyclic residual, a strict packing decrease, or a bidirectional connector state whose two support orders are non-`BLOCK` with matching parity.

The useful new restriction is that an old exposed hole can become a sink only after its protected support edge is destroyed, and a tight pivot can destroy that edge only from one of two adjacent pivot sites. Since the light supports inherited in this branch have bounded order, this converts the remaining orbit question to a genuinely finite local support-order problem. The next mathematical step is to enumerate/derive those guard-breaking local transitions **under the actual arc constraints**, not merely enumerate abstract token swaps; any rank-two conclusion must still pass the B06 parity criterion.

## Honest status and safeguards

This is not a proof of BT4. No claim is made that a rank-two connector family automatically splices, and no claim is made that the finite pivot orbit has already been closed. The new contribution is the support-correct fresh-hole obstruction, its persistence/locality strengthening, and the forced two-support sink queue.

No benchmark material, protected controls, credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive material, public posting, paid/remote compute, workflow mutation, or permission change is included. Model self-report: `GPT-5.6 Sol`; configured reasoning/provider usage metadata: `UNKNOWN_NOT_EXPOSED`.
