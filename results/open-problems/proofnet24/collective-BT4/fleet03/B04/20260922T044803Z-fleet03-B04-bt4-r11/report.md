# BT4 fleet03/B04 — seven-remainder strict-collar pinwheel collapse

Run: `20260922T044803Z-fleet03-B04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R7-PINWHEEL-TRIANGLE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Target and exact peer consumed

Target: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles; opposite arcs and hence digons are allowed in the source problem.

Named OTHER-account partner result actually consumed: fleet04/B05, `BT4-COUNT-v5-SIX-R-SINK-OVERLOAD`, report
`proofnet24/collective-BT4/fleet04/B05/b05-20260922t041051z-r33/report.md`, commit `6247f07d37301e28d05b7849da073ce8a7d13eb9`, blob `6fa55e68f034fc758a5d3c1c76431f93f63c2957`.

That result closes the global-NO-SIX, no-cross, no-neutral strict-collar branch for `|R|<=6` and identifies `|R|=7` as the first possible boundary. It uses the compatible fleet01/B06 fixed-pair collar theorem (blob `0ffb3fb1b521920e0a9cb3693fda8fd5bbb6a588`): an `R`-supported five-witness heavy on a packed cycle with fan `m>=3` gives either a cross-packed transition, a size-neutral equality exchange, or three strict pure-`R` Menger collars with

`|R| >= 1 + sum_i (L_i-1) >= 3m-2 >= 7`,

where the three paths have distinct starts on the heavy packed cycle, common endpoint the witness, and pairwise disjoint interiors.

I attack the partner's first unpaid seven-remainder branch by a shortest-cycle/global-minimum exchange, not by extending the previous four-remainder neutral-pivot argument.

## Inherited hard branch

Assume the campaign's minimum-counterexample normal form:

1. `D` is oriented and every vertex has outdegree exactly seven;
2. `(A,B,C)` is a globally minimum-total packing of three directed cycles;
3. `R=V(D)\(V(A) union V(B) union V(C))` is nonempty and acyclic;
4. the packed cycles are chordless;
5. the state is global `NO-SIX`;
6. there is no genuine cross-packed transition and no size-neutral globally minimum packing exchange in the present branch.

Suppose `|R|=7` and there is an `R`-supported five-witness `z` for a fixed deleted packed pair. Let `T` be a heavy packed cycle for `z`, and put

`m = |N+(z) intersect T| >= 3`.

Apply the inherited strict three-collar alternative.

## Lemma 1 — equality at seven vertices makes the witness a remainder sink

The inherited bound gives

`7 = |R| >= 3m-2 >= 7`.

Therefore equality holds throughout:

- `m=3`;
- all three strict `T -> z` paths have length exactly `L_i=3`;
- each path has exactly two internal vertices in `R\{z}`;
- the six internal vertices of the three paths are pairwise disjoint and exhaust `R\{z}`.

Write the paths

`P_i : t_i -> r_i -> s_i -> z`,  `i=1,2,3`,

where `t_i in T` are distinct.

Every vertex of `R\{z}` therefore has a directed path to `z` inside `D[R]`. Since `R` is acyclic, `z` cannot send an arc to any vertex of `R\{z}`: such an arc followed by that vertex's path back to `z` would be a directed cycle in `R`.

Hence

`N+(z) intersect R = emptyset`.

So `z` is a sink of `D[R]`. Because `z` is a five-witness for the fixed deleted pair and has exact outdegree seven, its remaining two arcs go to the complementary packed cycle. Since the heavy fan has size three, the three packed-cycle fan sizes of `z` are exactly a permutation of

`(3,2,2)`.

This already shows that the first strict `R`-supported seven-vertex case is not a generic collar: it is a full three-arm in-pinwheel around a `(3,2,2)` remainder sink.

## Lemma 2 — every heavy outneighbor lies within three forward steps of every path start unless T is a triangle

Let

`X={t_1,t_2,t_3}`
and
`Y=N+(z) intersect T`.

Both sets have cardinality three.

Fix `t in X` and `y in Y`. The path from `t` to `z` has three edges. If `y=t`, then

`t -> r -> s -> z -> t`

is a directed 4-cycle, disjoint from the other two packed cycles. If `y != t`, let `d_T(y,t)` denote the positive forward distance on the directed cycle `T` from `y` to `t`. Then

`K(t,y) := t -> r -> s -> z -> y -> T[y,t]`

is a genuinely directed cycle, again disjoint from the other two packed cycles, of length

`|K(t,y)| = 4 + d_T(y,t)`.

Let `n=|T|`. Replacing `T` by `K(t,y)` cannot give a smaller three-cycle packing, by global minimum. If the replacement has exactly the same size, then either the exchanged remainder contains a directed cycle, in which case that cycle together with `K(t,y)` and the other two packed cycles gives four vertex-disjoint directed cycles, or the exchanged remainder is acyclic and the replacement is precisely a forbidden size-neutral globally minimum exchange. Therefore in the present hard branch every such replacement must satisfy

`|K(t,y)| > n`.                                                   (1)

Assume `n>=4`. If `y=t`, then `|K|=4`; this is smaller than `n` when `n>4` and neutral when `n=4`, contradicting (1). Hence `y!=t`.

Write `d_T(t,y)` for the positive forward distance from `t` to `y`. Then

`d_T(y,t)=n-d_T(t,y)`.

Using (1),

`4+n-d_T(t,y) > n`,

so

`d_T(t,y) <= 3`.                                                  (2)

Thus for every `t in X`,

`Y subset {t+, t++, t+++}`.

Both sides have three vertices, hence

`Y = {t+, t++, t+++}`                                             (3)

for every `t in X`.

But on a directed cycle of length at least four, the three-successor block `{t+,t++,t+++}` determines `t` uniquely. Therefore (3) cannot hold for the three distinct starts `t_1,t_2,t_3`.

Contradiction. Hence `n<4`.

Since `D` is oriented, a directed cycle has length at least three. Therefore

`|T|=3`.

Because `|X|=|Y|=3`, in this surviving case

`X=Y=V(T)`.

## Theorem — seven-remainder strict-collar branch collapses to a triangular pinwheel

Under the inherited exact-outdegree-seven, globally minimum, global-NO-SIX, no-cross, no-neutral hard branch with `|R|=7`, every `R`-supported five-witness in the strict three-collar alternative has the following forced form:

1. it is a sink `z` of `D[R]`;
2. its packed-cycle fan profile is `(3,2,2)`;
3. its heavy cycle `T` is a directed triangle;
4. its three heavy outneighbors are all three vertices of `T`;
5. the three Menger starts are also all three vertices of `T`;
6. `R\{z}` is partitioned into three directed two-vertex arms

   `t_i -> r_i -> s_i -> z`,  `i=1,2,3`.

Equivalently, the general seven-remainder `R`-supported strict-collar obstruction is eliminated unless it is this exact triangular three-arm pinwheel.

Call this result **`BT4-R7-PINWHEEL-TRIANGLE-v1`**.

## Why this is a real reduction of the partner's unpaid implication

The fleet04/B05 frontier allowed, at `|R|=7`, an arbitrary `R`-supported heavy witness whose three strict collars merely saturated the lower bound. The theorem above shows that saturation plus global packing minimality is much more rigid: there is no such branch with a heavy cycle of length four or more, and the witness cannot have any outgoing remainder arc.

Thus the first unpaid seven-remainder state now splits into:

- support-carried witnesses whose two support collars may omit a common remainder sink; and
- one exact `R`-supported exceptional geometry: a `(3,2,2)` sink attached to a heavy directed triangle by three internally disjoint length-three in-arms covering all of `R\{z}`.

The second branch has no remaining freedom in the heavy-cycle size or collar lengths.

## First remaining implication

The next exact step is the **triangle-pinwheel splice**:

> In the forced configuration above, combine the two light-cycle fans of `z`, the three arms `t_i->r_i->s_i->z`, and the fixed-pair five-witness system to construct a legal two-cycle replacement / fourth directed cycle, or force `SIX`, `CROSS`, or a neutral exchange.

In parallel, the support-carried omitted-sink branch from fleet04/B05 remains open. No claim is made that either branch is closed here.

## Failure checks and nonclaims

- The proof uses exact outdegree seven only after proving `z` has no remainder outarc; a mere lower bound would not determine the `(3,2,2)` fan profile.
- Vertex-disjointness is preserved in every replacement: `K(t,y)` uses only one packed cycle and vertices of `R`, while the other two packed cycles are untouched.
- Equality of replacement sizes is not silently discarded: cyclic exchanged remainder gives four disjoint directed cycles; acyclic exchanged remainder is the explicitly excluded neutral exchange.
- The argument does not use the one-reversed-arc relaxation as a genuine directed cycle.
- No finite-order assumption, tournament reduction, edge-disjoint substitute, or computation is used.
- Digons remain allowed in the original target; orientation is only the inherited minimal-counterexample reduction.
- This is not a proof of BT4 and not a novelty claim.

## Honest outcome

`ESSENTIAL_STEP_APPLIED`.

The first possible `|R|=7` strict `R`-supported collar is reduced from an arbitrary saturated Menger configuration to one exact triangular three-arm pinwheel. Full BT4 remains open.
