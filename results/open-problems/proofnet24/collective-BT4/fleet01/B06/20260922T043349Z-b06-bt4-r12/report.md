# BT4 fleet01/B06 — regenerated-sink closure of the double-pivot high-exit branch

Run: `20260922T043349Z-b06-bt4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-REGENERATED-SIX-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent target: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, hence directed digons, are allowed in the source problem.

The controlling owner programme is the collective open-problems allocation. New brain-installation/benchmark work is superseded and was not performed.

The campaign's external source boundary remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): the genuine conjecture remains unresolved for `k>=4`; their theorem allows one reversed arc per packed cycle and is not used below as a directed-cycle theorem. The inherited genuine `k=3` input is the Lichiardopol--Por--Sereni minimum-outdegree-five theorem.

## Exact live team state consumed

Latest complete campaign-lead report read and used:

- fleet02/B04 run `20260922T041847Z-b04-bt4-r11`, candidate `BT4-HT-PREDECESSOR-SPLICE-v1`, report blob `596929efe56393d3ab515544fa33ec6a19e75c83`.

I retain its exact minimum-counterexample normal form: `D` is oriented, every vertex has outdegree exactly seven, `(H,S,U)` is a globally minimum-total packing of three directed cycles, the remainder is nonempty and acyclic, packed cycles are chordless, every arc is dominated, and `D` is 3-vertex-strong. I also retain the lead correction that the live four-remainder frontier is a genuine splice problem, not a no-cross problem.

Named OTHER-account result actually applied:

- fleet02/B05 run `20260922T042100Z-b05-bt4-e5df42d4`, candidate `BT4-R4-DOUBLE-PIVOT-CONFLUENCE-v1`, report blob `590d5e9665e1289a7f2fc0c99e53265e54946435`.

Its exact long-source four-remainder F2 state is the input of the theorem below. I use the complete arc/fan relations proved there, not its outcome label.

## Imported F2 two-sink state

Work in the lead's global-`NO-SIX` four-remainder branch. Along the source cycle write consecutive vertices

`p -> q -> s -> t -> ... -> p`, with `|S|>=6`.

The old remainder is

`R={x,y,z,c}`,

where `x,y` are distinct sinks. The named B05 input gives:

1. `p->x`, with `N+(x) intersect S={q,s}`;
2. `q->y`, with `N+(y) intersect S={s,t}`;
3. `x` has heavy fan three on `H` and light fan two on `U`;
4. there is an inport `u in U -> x`, with `N+(x) intersect U={v,w}`, where `v=u+`, `w=u++`;
5. `c->x`, and `{p,u,c}` induces a directed triangle (one of the two cyclic orientations);
6. `q->y,z`, while `q not->c`;
7. when `|S|>=6`, neither `y` nor `z` reaches `x` or `c` inside the old DAG `R`.

B05 performs the commuting neutral pivots

`S_y = q -> y -> t -> S[t,q]`,

`U_x = u -> x -> w -> U[w,u]`.

They give another globally minimum packing `(H,S_y,U_x)` with acyclic remainder

`R''={c,z,s,v}`.

The freed vertices have unique support outneighbors `s->t` and `v->w`. Put

`e_s=d^+_{R''}(s)`, `e_v=d^+_{R''}(v)`.

The named result already sends `e=0` to SIX and `e=1` to a five-witness. Its only high-exit residual is

`e_s>=2`, `e_v>=2`.                                             (HE)

It proved that under (HE) at least one of `s->c`, `v->c` holds, and from there only obtained the bounded alternative `|S|=6` or `|U|<=4`.

This run removes that bounded high-exit residual entirely from persistent `NO-SIX`.

## Compact conditional end-to-end route

At the current campaign frontier, a complete BT4 proof follows once the remaining SIX and genuine packed-port splice interfaces are closed. In the long-source F2 branch, the route can now be sharpened to:

1. perform the B05 simultaneous neutral pivots;
2. `e=0` enters SIX and `e=1` enters the existing five-witness linkage interface;
3. the theorem below proves that `e_s,e_v>=2` also necessarily enters SIX: if the regenerated sink tried to stay `NO-SIX`, two explicit small directed cycles would strictly undercut the globally minimum three-packing;
4. hence `BT4-R4-BOUNDARY-CLOSURE-v1` is no longer needed for this F2 high-exit branch. Its first unpaid implication is the already-existing SIX closure, while the other `SC+` configurations and the separate global SIX interface remain live.

## Lemma 1 — the source-only equality pivot forbids `s->c`

Consider only the source pivot, keeping the old cycle `U`:

`(H,S_y,U)`.

This is also a globally minimum three-cycle packing, because `|S_y|=|S|`. Its remainder is

`R_y={x,z,c,s}`

and must be acyclic.

But the imported arcs give

`c->x->s`.

Therefore

`s not->c`.                                                      (1)

Otherwise `c->x->s->c` would be a directed cycle in `R_y`, which together with `H,S_y,U` would be a four-packing.

This uses the equality pivot one step earlier than the named B05 proof and is the key additional global-minimum constraint.

## Lemma 2 — high exit forces a rigid staircase and makes `z` a regenerated sink

Assume (HE).

B05 already proves that at least one of `s->c`, `v->c` holds. By (1), necessarily

`v->c`.                                                          (2)

Now `s` has only the three possible remainder targets `{c,z,v}` in `R''`. Since `e_s>=2` and `s not->c`,

`s->v`, `s->z`.                                                  (3)

Similarly `v` has only `{c,z,s}` available in `R''`. By (2), `e_v>=2`, and orientation of `s->v`,

`v->z`.                                                          (4)

The imported old-remainder reachability statement says that `z` does not reach `c`; in particular

`z not->c`.                                                      (5)

Orientation of (3)--(4) gives `z not->s,v`. Combining with (5),

`d^+_{R''}(z)=0`.                                                (6)

Thus the double-pivot high-exit branch automatically regenerates a **new remainder sink `z`**. The hard state is not a diffuse four-vertex DAG.

## Lemma 3 — the direct inport `q->z` confines the regenerated sink's source fan

The F2 input has `q->z`, and `q` lies on `S_y`. Let `a` be any outneighbor of `z` on `S_y`.

The directed cycle

`q -> z -> a -> S_y[a,q]`

is disjoint from `H,U_x`. If

`d=d_{S_y}(q,a)`

is the forward distance from `q` to `a`, this replacement cycle has order

`|S_y|+2-d`.

Global minimum therefore forces `d<=2`. Hence

`N+(z) intersect S_y subset {y,t}`.                              (7)

Because `z` is a sink of `R''`, all seven of its outneighbors lie on `H union S_y union U_x`.

If the left side of (7) has size at most one, then

`d^+_{H union U_x}(z)>=6`,

so `z` is already a SIX witness for that packed pair.

Consequently, in a persistent `NO-SIX` continuation we must have equality in (7):

`N+(z) intersect S_y={y,t}`.                                    (8)

In particular,

`z->y`.                                                          (9)

This is exactly another neutral adjacent source-pivot pattern, but the next lemma shows that the state cannot survive long enough to perform an opaque orbit.

## Theorem — regenerated-sink high-exit closure

> **BT4-R4-REGENERATED-SIX-v1.** In the imported long-source F2 state with `|R|=4`, `|S|>=6`, after the simultaneous B05 neutral pivots, the high-exit branch `e_s,e_v>=2` necessarily produces a SIX witness. Equivalently, the high-exit branch cannot persist in global `NO-SIX`.

### Proof

Assume for contradiction that no SIX witness appears at the regenerated sink `z`. Then Lemma 3 gives `z->y`.

The imported inport set `{p,u,c}` is a directed triangle. Denote that triangle by `T`; its orientation is irrelevant for the argument.

By the imported source fan of `y` and Lemma 2,

`y->s->v->z->y`                                                  (10)

is a genuine directed 4-cycle; call it `W`.

The cycles `T` and `W` are vertex-disjoint:

- `T` uses exactly `{p,u,c}`;
- `W` uses exactly `{y,s,v,z}`.

They are also both disjoint from `H`. Hence

`(H,T,W)`

is a legitimate three-cycle packing in the original digraph. Its total order is

`|H|+3+4=|H|+7`.

The original globally minimum packing has order

`|H|+|S|+|U| >= |H|+6+3 = |H|+9`,

because `|S|>=6` and the oriented normal form has no directed cycle of order below three.

Thus `(H,T,W)` is a **strictly smaller three-cycle packing**, contradicting global minimality. Therefore the supposition that `z` remains `NO-SIX` is impossible. The regenerated sink `z` must have at most one outneighbor on `S_y`, and hence at least six outneighbors on `H union U_x`. QED.

## Consequence for the named OTHER-account frontier

The named fleet02/B05 theorem ended the high-exit calculation at

`|S|=6 OR |U|<=4`.

The new theorem is stronger on exactly that imported branch:

`e_s,e_v>=2  ==>  regenerated remainder sink z  ==>  SIX`.

So neither bounded boundary family needs a separate high-exit closure here. The mechanism is not a finite-size case check: the strict replacement uses only the uniform inequalities `|S|>=6`, `|U|>=3` and the exact imported arcs.

It also identifies why the double pivot is useful. The two freed vertices force the staircase

`s -> v -> c`,
` s -> z`, `v -> z`,

while the old F2 arc `q->z` turns `z` into an adjacent source-pivot sink. If that sink does not immediately expose a six-fan, its forced return `z->y` closes the 4-cycle `y-s-v-z-y`; the old inport triangle on `{p,u,c}` then supplies a disjoint second replacement cycle. The global minimum is spent directly as a two-cycle strict surgery.

## Updated first unpaid implication

For this F2 long-source branch, the arbitrary `R4` high-exit/boundary splice is paid. The branch now routes as follows:

- `e=0`: SIX;
- `e=1`: existing R-supported five-witness/collar interface;
- `e_s,e_v>=2`: SIX by `BT4-R4-REGENERATED-SIX-v1`.

Thus the first unpaid implication on this line is no longer `|S|=6` / `|U|<=4` case analysis; it is the campaign's genuine **SIX closure** (together with the already-live five-witness linkage when `e=1`). At the target level the lead still has other `SC+` port-splice configurations, the heavy-triangle outputs, and the separate SIX interface, so BT4 is not proved here.

## Failure checks and nonclaims

- Every displayed cycle is genuinely directed in the original digraph; no edge-disjoint or one-reversal substitute is used.
- The argument uses the oriented exact-seven model only after the inherited valid no-digon reduction; the source theorem itself still allows digons.
- The proof of `s not->c` uses the source-only equality packing `(H,S_y,U)`, not the simultaneous packing, so the triangle `c-x-s-c` would indeed lie wholly in its remainder.
- `z` being a sink uses the imported fact that `z` cannot reach `c` in the old remainder; this is an explicit hypothesis of the named B05 long-source state, not inferred from acyclicity alone.
- The confinement (7) is a global-minimum cycle replacement, not a chordlessness shortcut.
- The two-cycle strict surgery uses the directed triangle on `{p,u,c}` supplied by the named state and the separately derived 4-cycle (10); the two vertex sets are explicitly disjoint.
- Entering SIX is not itself claimed to finish BT4. The SIX interface remains a separate campaign obligation.
- No computation was used as proof or evidence in this report.
- No novelty claim is made.

## Honest outcome

`ESSENTIAL_STEP_APPLIED`.

A formerly unbounded/high-exit four-remainder splice branch is completely routed into the existing SIX interface by an explicit regenerated-sink argument and strict two-cycle packing undercut. Full BT4 remains open.
