# BT4 account03/B06 — low-fan reverse inports collapse to opposite crosses or one source-triangle lock

Run: `20260922T041829Z-B06-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-LOWFAN-CROSS-TRIANGLE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED` with one local `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Parent target: `OPEN_NOT_PROVED`

## Exact target and current frontier

The target is the genuine `k=4` Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, hence digons count. The campaign's source check is Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026); that paper proves only the one-reversal relaxation and leaves the genuine conjecture unresolved for `k>=4`.

I use the inherited minimum-counterexample normal form only with its established hypotheses: after removing a digon by the genuine `k=3` theorem one may work in an oriented exact-outdegree-seven counterexample; choose a globally minimum-total packing of three directed cycles with acyclic remainder; the packed cycles are chordless; the digraph is 3-vertex-strong; and every arc is dominated by a common predecessor.

The controlling lead frontier is account02/B04 `BT4-R4-SATURATION-COLLAPSE-v1` plus its controlling `SC+` addendum. In global `NO-SIX`, for a remainder sink `x` there are packed cycles `(H,S,U)` and a light inport `p in S -> x` with fan pattern `(3,2,2)`, `H not->x`, and source targets `{p+,p++}`. The legal neutral source pivot

`S* = p -> x -> p++ -> S[p++,p]`

frees `q=p+` and gives `R*=(R-{x}) union {q}`. It also creates three endpoint-distinct `x`-free cross-packed transitions ending at the three heavy targets of `x`.

## Named other-account result consumed

The assigned partner is account04/B04. I consume its newest complete candidate `BT4-R4-FREED-PROFILE-v1` from run `account04-B04-20260922T034321Z-BT4-r12`.

Specialize to `|R|=4` after the neutral pivot. Let `e=d^+_{R*}(q)`. The partner proves:

- `e=0` is a `SIX` exit.
- If either `H` or `U` receives at least three q-outarcs, a genuine q-avoiding return cross exists.
- Otherwise only two low-fan profiles remain.
- `F2`: `e=2`, `d_H^+(q)=d_U^+(q)=2`, and q has profile `(2,2,1,2)` relative to `(H,U,S*,R*)`. If `r0` is the unique other remainder vertex not dominated by q, then either `r0->q` or a packed inport `H union U -> q` exists.
- `F3`: `e=3`, the `H,U` fan sizes are `{2,1}`, q has profile `(2,1,1,3)`, q dominates all of `R*-{q}`, and there is a packed inport `H union U -> q`.

The partner's first unpaid implication was `BT4-R4-LOWFAN-SPLICE-v1`: spend these reverse inports against the lead's three x-free heavy-entry crosses.

No peer outcome label is used as proof.

## New theorem — low-fan reverse-inport collapse

Define an **opposite cross pair between packed cycles `T,T'`** to mean a directed cross from `T'` to `T` and a directed cross from `T` to `T'` whose interiors are disjoint. In the conclusions below one member is a direct packed-to-packed arc (empty interior) and the reverse member has sole internal vertex `q`, so the interior-disjointness is automatic.

> **BT4-R4-LOWFAN-CROSS-TRIANGLE-v1.**
> In the partner's four-remainder post-pivot state:
>
> 1. every `F3` state contains an opposite cross pair;
> 2. every `F2` state with `r0 not->q` contains an opposite cross pair;
> 3. every `F2` state with `r0->q` contains an opposite cross pair unless the following exact source-triangle lock occurs:
>
>    `|S*|=3`, and with `S*=(p,x,p++)`,
>
>    `x->r0->p->x`, `x->q`, `p->q`, `r0->q`.
>
>    Replacing `S*` by `W=(x,r0,p)` is size-neutral. In a genuine BT4 counterexample the exchanged remainder
>
>    `R**=(R*-{r0}) union {p++}`
>
>    is acyclic.

Thus the partner's two low-fan profiles do not remain generic reverse-inport cases: `F3` disappears into an explicit opposite-cross interface, and `F2` does the same except for one rigid neutral triangle orbit.

### Lemma 1 — a packed inport to q forces an opposite cross pair

Assume `y->q` with `y` on a packed cycle `T`, and assume q has an outneighbor on each of the other packed cycles; this holds in both `F2` and `F3`.

Let `P=N^-(q) intersect T`, so `P` is nonempty. Dominate an arc `v->q`, `v in P`, by a common predecessor `d->v,q`.

If `d` lies on a packed cycle `T' != T`, then `d->v` is a direct cross `T'->T`. Choose any q-target `t' in T'`. Then

`y -> q -> t'`

is a cross `T->T'` with sole internal vertex q. These two crosses form the required opposite pair.

If `d in T`, chordlessness forces `d=v^-` on `T`, and `d` also belongs to `P`.

The only remaining possible obstruction is a remainder dominator. This is absent in `F3`, because q sends to every other remainder vertex and orientation forbids each from entering q. It is also absent in the `F2` subcase `r0 not->q`: q sends to the other two remainder vertices, while `r0` is assumed not to enter q.

Therefore, if no opposite cross pair occurs, every `v in P` has its cycle predecessor in `P`. A nonempty predecessor-closed subset of a finite directed cycle is the whole cycle, so `P=T`. But q has at least one outneighbor on `T` in both low-fan profiles, and orientation makes every q-target on `T` disjoint from `P`. Contradiction.

This proves `F3` and the `F2, r0 not->q` branch.

### Lemma 2 — an H/U dominator of r0->q also forces an opposite pair

Now assume `F2` and `r0->q`. Dominate `r0->q`; let `y->r0,q` be a common predecessor. Suppose first that `y` lies on `T in {H,U}`.

Start dominating the successive inport arcs to q while moving backward on `T`. If a dominator ever lies on a different packed cycle, Lemma 1's direct-arc construction gives an opposite cross pair.

No remainder vertex other than `r0` can dominate such an inport, because q sends to the other two remainder vertices. If `r0` never occurs, the predecessor chain eventually wraps around `T`, putting every vertex of `T` into `N^-(q)`, impossible because q has exactly two outneighbors on `T`.

So suppose the first remainder dominator is `r0`. Write the predecessor chain as

`y, y^-, ..., v=y^{-j}`,

with all `j+1` vertices entering q and with `r0->v,q`. The initial domination gives `y->r0`, hence

`y -> r0 -> v -> T[v,y]`

is a directed cycle of length `j+2` replacing `T` and disjoint from the other two packed cycles.

Global minimum of the three-cycle packing requires `j+2 >= |T|`. On the other hand q has two outneighbors on `T`, disjoint by orientation from the inport chain, so

`j+1 <= |T|-2`,

hence `j+2 <= |T|-1`, a contradiction.

Thus the `H/U` initial-dominator branch necessarily yields an opposite cross pair.

### Lemma 3 — the only no-pair source dominator is the triangle lock

Still assume `F2` and `r0->q`. The partner's source-pivot geometry gives that the only vertices of `S*` that can enter q are `p` and `x`.

If a dominator `y->r0,q` has `y=p`, then `p->r0`. Dominate `p->q`. The vertex `r0` cannot dominate this arc because `p->r0` and orientation forbid `r0->p`. A dominator on `H` or `U` gives an opposite cross pair as in Lemma 1. A same-`S*` dominator is impossible by chordlessness and the fact that only `p,x` enter q. Hence this branch closes by an opposite pair.

The sole remaining possibility is therefore

`x->r0,q`.

Dominate `x->q`. A remainder dominator is impossible: q sends to the two remainder vertices other than `r0`, while `x->r0` and orientation exclude `r0->x`. A dominator on `H` or `U` gives an opposite pair. With no opposite pair, chordlessness of `S*` forces the dominator to be the cycle predecessor `p`, so

`p->x,q`.

Finally dominate `p->q`. A dominator on `H` or `U` again gives an opposite pair; a same-support dominator is excluded by chordlessness. Therefore the only no-pair possibility is

`r0->p,q`.

Together these arcs give the directed triangle

`W = x -> r0 -> p -> x`.

The packing `(H,W,U)` is legitimate and has total size smaller than `(H,S*,U)` unless `3>=|S*|`. Since the counterexample is oriented, every directed cycle has length at least three, hence `|S*|=3`. Therefore `S*=(p,x,p++)` and the exchange is size-neutral.

If its new remainder `R**=(R*-{r0}) union {p++}` contained a directed cycle, that cycle together with `H,W,U` would already be four vertex-disjoint directed cycles. Therefore `R**` is acyclic in a counterexample.

This proves the theorem.

## Exact constrained certificate — the triangle lock is locally feasible

A stronger shortcut is false:

> “The source-triangle lock itself is incompatible with exact outdegree seven, orientation, chordless packed cycles, arc domination, 3-vertex-strongness, and acyclicity of both the old and exchanged remainders.”

The attached standard-library checker verifies a complete 17-vertex digraph with all 119 arcs explicitly encoded. It has:

- every outdegree exactly seven;
- no loops or digons;
- chordless packed cycles
  `H=(0,1,2,3,4)`, `U=(5,6,7,8,9)`, `S*=(10,11,12)`;
- old remainder `R*={13,14,15,16}` acyclic;
- exchanged remainder `{13,12,15,16}` acyclic;
- 3-vertex-strongness, checked after every deletion of zero, one, or two vertices;
- every arc dominated by a common predecessor;
- `q=13`, `r0=14`, and exact F2 profile
  `H:{2,3}`, `U:{7,8}`, `S*:{12}`, `R*:{15,16}`;
- the exact lock triangle `(x,r0,p)=(11,14,10)`;
- for the three lock inport arcs, the internal common predecessors are uniquely
  `cp(14->13)={11}`, `cp(11->13)={10}`, `cp(10->13)={14}`.

So even pre/post-exchange remainder acyclicity does not make the lock locally contradictory.

The certificate is deliberately **not** a BT4 counterexample. It contains the explicit four disjoint directed triangles

`(0,1,5)`, `(2,3,10)`, `(4,6,7)`, `(8,9,11)`.

This failure is informative: after the theorem reduces F2 to the triangle lock, the next step genuinely has to spend the global no-four-packing restriction together with the lead's already-available x-free heavy-entry crosses. More local degree/connectivity/acyclicity alone cannot be assumed to close the branch.

## Exact checker and symbolic sanity

The checker is deterministic standard-library code. It verifies the complete graph certificate above, all arc-domination and 3-connectivity conditions, the two acyclic remainders, the exact F2 profile, the unique three-step domination lock, and the explicit four-pack.

It also independently enumerates the elementary predecessor-closure implication on directed cycles through order 12 and checks the heavy-chain packing arithmetic through cycle order 100. These computations are implementation sanity checks only; the lemmas above are uniform proofs and do not rely on the finite bounds.

Checker SHA-256:
`b6356dc3ed095084948ce9ed58d13be224a9031b00a855d193c02486b065dada`.

Checker stdout SHA-256:
`3887fdf3419bd1c214c589cabc336c03a3b99fc8723b0c7d5bc38e716819aaae`.

Canonical payload SHA-256:
`55aa6207ea39872cdcd4ed230fb46cafab3f185c16ee86d53e9ad913a6ae7af6`.

The exact output records 4,851 chain-arithmetic sanity cases and the expected predecessor-closure cases, with result `PASS`.

## What changed in the shared proof tree

The partner frontier

`F2 or F3 -> reverse inport -> LOWFAN-SPLICE?`

is now sharpened to

`F3 -> opposite cross pair`,

`F2 -> opposite cross pair OR exact size-neutral source-triangle lock`.

An opposite cross pair is still only an interface, not automatically two replacement cycles; the lead already warned that two opposite crosses can make one alternating cycle rather than two disjoint replacements. Thus I do not claim that the cross-pair branch closes BT4.

The first remaining implication for this line is now:

> **BT4-R4-TRIANGLE-LOCK-SPLICE-v1.**
> In the exact source-triangle lock, combine the acyclic exchanged remainder with the lead's three endpoint-distinct x-free heavy-entry crosses (and the post-pivot two-arm structure) to force a legal two-cycle replacement, a strict globally-minimum packing reduction, a SIX state, a directed cycle in the exchanged remainder, or a fourth directed cycle.

The constrained certificate proves that this next implication must use the **global absence of four disjoint cycles and the actual cross interfaces**, not only the local normal-form axioms.

## Mechanism change and status

The preceding account03/B06 runs pursued the G1 support-witness corridor/port mechanism. The newest team frontier moved to the four-remainder freed-vertex split, so this run materially changed mechanism: domination-chain closure plus a fresh constrained full-graph certificate, while retaining the same BT4 target.

BT4 remains `OPEN_NOT_PROVED`. This run establishes an essential structural reduction and refutes one stronger local shortcut; it is not a target-level proof or counterexample and makes no novelty claim.
