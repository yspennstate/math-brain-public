# BT4 fleet04/B05 — lexicographic heavy-triangle cage gives an x-free Hall escape pair

Run: `b05-20260922t051421z-r34`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-XFREE-HALL-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent target: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, hence digons, are allowed in the source problem.

The external source boundary was checked again this run. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), explicitly records the genuine conjecture as unresolved for all `k>=4` and proves only the one-reversed-arc relaxation. Lichiardopol--Pór--Sereni, SIAM J. Discrete Math. 23 (2009), 979--992, prove the genuine `k=3` theorem `delta^+>=5 => 3` vertex-disjoint directed cycles and the strengthened `k=2` theorem used by the campaign.

## Live team state actually consumed

Latest complete lead state read before this report:

- fleet02/B04 `20260922T041847Z-b04-bt4-r11`, primary candidate `BT4-HT-PREDECESSOR-SPLICE-v1`, blob `596929efe56393d3ab515544fa33ec6a19e75c83`;
- its controlling strengthening, blob `8bfc5b33fb232c8543856d6d9ad3b0e8fdc3432c`.

The controlling lead normal form is an oriented exact-outdegree-seven counterexample with a globally minimum-total packing `(H,S,U)` of three directed cycles, nonempty acyclic remainder `R`, chordless packed cycles, arc domination and 3-vertex-strongness. In the four-remainder heavy-triangle branch it writes

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

with

`hi->ri->x->hi` for `i=0,1,2`,                                      (1)

and `H not->x`. In the maximal predecessor branch, after rotation, the lead proves

`r0->r1,h1,x`,
`r1->r2,h2,x`,                                                     (2)

and the exact residual identities

`N^+_{H union R}(r2)={x,h0}`,
`N^+_{H union R}(h1)={h2,r1}`,
`N^+_{H union R}(h2)={h0,r2}`.                                   (3)

The controlling strengthening also proves that a cycle-supported exact five-witness cannot receive an arc from its heavy light target: a single such inport already gives a strictly smaller three-cycle packing.

Named OTHER-account results actually applied:

1. fleet01/B04 `BT4-R4-MAX-REMAINDER-ARC-COLLAPSE-v1`, run `20260922T044536Z-b04-bt4-r11`, blob `b9b700749e5723c819b6643aa16c67c38db6c569`: among all globally minimum-total three-cycle packings, refine the choice by maximizing `Phi(P)=|A(D[R_P])|`. Every neutral packing exchange then has remainder-arc potential at most the chosen packing.
2. assigned partner fleet01/B06 fixed-pair/Menger-collar theorem, run `20260922T013522Z-b06-bt4-r11`: for an R-supported five-witness heavy on a packed cycle with fan `m>=3`, either a path meets another packed support and yields a genuine cross transition, or equality gives a neutral exchange, or the strict pure-R branch forces `|R|>=3m-2>=7`.
3. the partner's newer `BT4-R4-REGENERATED-SIX-v1`, run `20260922T043349Z-b06-bt4-r12`, blob `11d846b6ab2c724c302087fff920987e96042888`, was checked for compatibility. It independently routes the long-F2 high-exit branch into SIX; that branch is not reproved here.

## Compact conditional end-to-end route

Choose the campaign packing lexicographically: first minimum total packed order, then maximum `Phi=|A(D[R])|`. Existing minimum-order arguments remain valid. The lead reduces the hard four-remainder heavy-triangle state to a light-inport cover or the exact-two-predecessor cage (1)--(3). This report attacks the latter.

A full BT4 proof would follow after the current genuine packed-port splice and SIX closures. The theorem below pays a specific part of the packed-port problem: it proves that the exact-two-predecessor cage contains three heavy-fan escape transitions that avoid the common sink `x`, have pairwise disjoint remainder interiors, and admit a dependence-correct Hall alternative on their target ports. It also creates a fourth fixed-pair five-witness in the remainder and applies the assigned partner's collar theorem to it.

## Lemma 1 — the seven-vertex cage is exact in the lexicographic packing

Under (1)--(3), no additional arc among `H union R` is possible beyond the following list:

- the three cycle arcs of `H`;
- the nine saturation arcs `hi->ri`, `ri->x`, `x->hi`;
- `r0->r1`, `r0->h1`, `r1->r2`, `r1->h2`;
- `r2->h0`.

In particular,

`r0 not->r2`, `r0 not->h2`, `r1 not->h0`, `h0 not->r1`.           (4)

### Proof

The exact identities (3), orientation, and (1)--(2) leave only three unordered places where an additional arc can occur:

1. between `r0,r2`, only the direction `r0->r2` is possible;
2. between `r0,h2`, only `r0->h2` is possible;
3. between `h0,r1`, either direction is initially possible.

The first three candidate directions are excluded by explicit four-packing certificates.

If `r0->r2`, then

`h0->r0->r2->h0`

and

`h1->r1->x->h1`

are vertex-disjoint directed triangles. Together with `S,U` they give four disjoint cycles.

If `r0->h2`, then

`r0->h2->h0->r0`

and

`h1->r1->x->h1`

are disjoint directed triangles.

If `r1->h0`, then

`r1->h0->h1->r1`

and

`h2->r2->x->h2`

are disjoint directed triangles.

Thus only `h0->r1` remains possible. The original remainder then has exactly the five mandatory arcs

`r0->r1`, `r1->r2`, `r0->x`, `r1->x`, `r2->x`,

so `Phi(P)=5`. Replace the packed triangle `H` by the equal-size saturation triangle

`T2=h2->r2->x->h2`.

The new remainder is `{h0,h1,r0,r1}` and already contains

`h0->h1`, `h0->r0`, `r0->h1`, `r0->r1`, `h1->r1`.

If `h0->r1` also existed, this neutral packing would have remainder potential six, contradicting lexicographic maximality of `Phi(P)=5`. Hence `h0 not->r1`. QED.

A small exact enumeration was used only as a check of this hand proof. With the lead's required arcs and exact-out identities, the three optional families were

`{none,h0->r1,r1->h0}`,
`{none,r0->h2}`,
`{none,r0->r2}`.

The checker discarded a choice if `H union R` contained two vertex-disjoint directed cycles or if one of the neutral triangle replacements had larger remainder-arc potential. Exact output:

```
survivors = [((None, None, None), 5, [5, 4, 5])]
```

The three numbers in the last list are the remainder potentials after replacing `H` by `T0,T1,T2`, respectively. No finite search is used to infer BT4 itself.

## Lemma 2 — four exact five-witnesses for the fixed light pair

In the exact cage of Lemma 1,

`d^+_{H union R}(h0)=d^+_{H union R}(h1)=d^+_{H union R}(h2)=d^+_{H union R}(r2)=2`.

Hence exact outdegree seven gives

`|N+(v) intersect (S union U)|=5`                                (5)

for every

`v in {h0,h1,h2,r2}`.

Moreover each `h_i` has exactly its support successor and its unique remainder exit `r_i` inside `H union R`:

`N^+_{H union R}(h_i)={h_{i+1},r_i}`.                            (6)

Thus `h0,h1,h2` are three cycle-supported exact five-witnesses for the fixed pair `{S,U}`, while `r2` is an R-supported exact five-witness for that same fixed pair.

This is stronger than the inherited double-witness statement for `h1,h2`.

## Lemma 3 — the missing saturation triangle fixes one heavy-target polarity

Because the predecessor relation for `T0=h0->r0->x->h0` is the missing one, the lead's external-three-hit argument supplies a light packed vertex

`w in L`, `L in {S,U}`,

with

`w->h0`, `w->r0`, `w->x`.                                       (7)

Let `M` denote the other light cycle. Then the five-witness `h0` cannot be heavy on `L`; consequently it is heavy on `M`.

### Proof

If `h0` were heavy on `L`, it would have at least three distinct outneighbors on `L`. Since `w->h0` and the graph is oriented, `h0 not->w`. Choose a fan target `y` minimizing the forward directed distance `d_L(y,w)`. At least three distinct positive distances are occupied, so

`d_L(y,w)<=|L|-3`.

Then

`w->h0->y->L[y,w]`

is a genuine directed cycle of order at most `|L|-1`. It is disjoint from the saturation triangle `T1=h1->r1->x->h1` and from the untouched other light cycle `M`. These three cycles have total order at most

`(|L|-1)+3+|M| < |L|+|H|+|M|`,

contradicting global minimum because `|H|=3`. QED.

Thus the missing predecessor is not merely a light witness: it determines that `h0`'s heavy light target is the *other* support.

## Lemma 4 — every heavy witness has an x-free one-vertex escape

For each `i=0,1,2`, let `A_i in {S,U}` be a heavy target of `h_i` and put

`F_i=N+(h_i) intersect A_i`,  `|F_i|>=3`.

Then there is a genuine cross-packed transition `P_i` ending at a vertex of `A_i` such that

- `x` is not a vertex of `P_i`;
- the R-interior of `P_i` is either empty or exactly `{r_{i-1}}` (indices modulo three);
- the packed start of `P_i` lies either at `h_{i-1}` on `H` or on the opposite light cycle.

In particular the three paths `P_0,P_1,P_2` have pairwise disjoint R-interiors.

### Proof

First, `A_i not->h_i` for every `i`. The controlling lead strengthening proves this for `h1,h2`; the identical argument applies to `h0` now that Lemma 2 shows it is an exact five-witness: use any saturation triangle `T_j` with `j!=i` as the disjoint length-three replacement for `H`. One heavy-target inport plus three fan targets would strictly shorten the three-packing.

The original sink has light fan size two on each of `S,U`; therefore

`X_i=N+(x) intersect A_i`

has size exactly two. Since `|F_i|>=3`, choose

`a_i in F_i \ X_i`.                                             (8)

Dominate the heavy-fan arc `h_i->a_i`. There is a vertex `q0` with

`q0->h_i,a_i`.

Because `a_i notin N+(x)`, `q0!=x`; because `A_i not->h_i`, `q0 notin A_i`.

Lemma 1 makes the in-neighborhood of `h_i` inside `H union R` exact: apart from `x`, the only such vertices are the support predecessor `h_{i-1}` and the matched remainder predecessor `r_{i-1}`. Hence either `q0` is already packed (`h_{i-1}` or a vertex of the opposite light support), or `q0=r_{i-1}`.

In the latter case dominate `r_{i-1}->h_i`. No remainder vertex can dominate this arc in the exact cage: for `i=0`, `r1->r2` but `r1 not->h0`; for `i=1`, no remainder vertex points to `r0`; for `i=2`, `r0->r1` but `r0 not->h2`. The next dominator is therefore packed, and again it cannot lie on `A_i`. The domination ladder terminates after this one remainder vertex.

Thus the heavy-fan escape path has R-interior `empty` or `{r_{i-1}}`, and it avoids `x`. The three possible singleton interiors are `{r2}`, `{r0}`, `{r1}`, hence are pairwise disjoint. QED.

This is the dependence-sensitive part of the result: the three escapes are not assumed independent; their possible overlap is computed exactly from the cage.

## Lemma 5 — Hall alternative for a same-heavy pair

At least two of `h0,h1,h2` have the same heavy target `A in {S,U}`. Choose such a pair `h_i,h_j`, and write

`X=N+(x) intersect A`, `|X|=2`.

Exactly one of the following holds.

1. **Distinct-port x-free pair.** There exist distinct target vertices

`a_i in (N+(h_i) intersect A)\X`,
`a_j in (N+(h_j) intersect A)\X`,

and Lemma 4 supplies two x-free cross transitions ending at `a_i,a_j` with disjoint R-interiors.

2. **Exact fan collision.** There is a single vertex `a outside X` such that

`N+(h_i) intersect A = N+(h_j) intersect A = X union {a}`.        (9)

In particular both heavy fans have size exactly three and their only target outside the sink's two-port set is the same vertex `a`.

### Proof

Set

`Y_i=(N+(h_i) intersect A)\X`,
`Y_j=(N+(h_j) intersect A)\X`.

Each is nonempty because its full fan has size at least three whereas `|X|=2`. If the two-set system `{Y_i,Y_j}` has a system of distinct representatives, apply Lemma 4 with those targets and obtain case 1.

If it does not, Hall's condition for two sets fails, so

`Y_i=Y_j={a}`

for one vertex `a`. Since each full fan has size at least three but contains at most the two vertices of `X` in addition to `a`, both full fans are exactly `X union {a}`. This is case 2. QED.

Thus the packed-port dependence is reduced to a precise collision, rather than hidden behind a probabilistic independence assumption.

## Lemma 6 — applying the assigned partner to the fourth witness

The vertex `r2` from Lemma 2 is an R-supported five-witness for `{S,U}`. Let `T in {S,U}` be a heavy target and let

`m=|N+(r2) intersect T|>=3`.

Apply fleet01/B06 `20260922T013522Z-b06-bt4-r11`. Since `|R|=4`, its strict pure-R alternative

`|R|>=3m-2>=7`

is impossible. Therefore one of the following occurs:

- a genuine cross-packed transition is produced by a path meeting another packed support; or
- a pure-R equality path from `T` to `r2` gives a size-neutral globally minimum exchange.

In the equality case that path cannot contain `x`: `x` is a sink of `D[R]`, so it cannot precede `r2` on an R-internal directed path. Appending the ambient arc `r2->h0` therefore gives an **x-free light-to-H cross transition** from `T` to `h0`, in addition to the neutral exchange.

So the exact-two-predecessor cage also contains either an extra packed cross supplied by the partner theorem or a reverse x-free light-to-H interface.

## Theorem — BT4-HT-XFREE-HALL-v1

In the lead's four-remainder global-NO-SIX heavy-triangle state, choose the globally minimum three-cycle packing to maximize remainder-arc potential. In the exact-two-predecessor branch:

1. the induced seven-vertex cage `H union R` is exactly the arc system of Lemma 1;
2. `h0,h1,h2,r2` are four exact five-witnesses for the fixed light pair `{S,U}`;
3. the missing saturation triangle has a light three-hit witness whose support is opposite the heavy target of `h0`;
4. each `h_i` has an x-free heavy-fan escape whose R-interior is empty or the distinct singleton `{r_{i-1}}`; hence the three escapes have pairwise disjoint R-interiors;
5. a same-heavy pair satisfies the exact Hall alternative of Lemma 5: either two x-free escapes can be chosen with distinct target ports and disjoint R-interiors, or both heavy fans coincide in the rigid three-set `N+(x) intersect A` plus one common extra port;
6. the fourth witness `r2`, by the named fleet01/B06 collar theorem, forces either an additional genuine cross or a neutral equality exchange carrying an x-free light-to-H return.

This pays the **remainder-interior disjointness** and **target-choice dependence** part of the lead's double-escape port-splice obstruction. It does not yet prove the required two replacement cycles because packed support segments may still overlap, and in the exact fan-collision branch the two same-heavy escapes may share their only target outside the sink's two-port set.

## First remaining essential implication

The first unpaid implication on this branch is now finite and exact:

> **HT-PORT-CLOSE.** Starting from either (a) the distinct-port x-free same-heavy pair of Lemma 5 together with the partner cross/equality return of Lemma 6, or (b) the exact fan-collision state (9) together with that return, prove a legal two-cycle splice, a strict reduction of the lexicographic minimum packing, a directed cycle in an exchanged remainder, a SIX witness, or a fourth disjoint directed cycle.

No independence of path choices may be assumed. The R-interiors are already controlled; only packed-port order/collision remains. The campaign's separate global SIX closure and other SC+ configurations remain unpaid.

## Failure checks and nonclaims

- The lexicographic potential is used only after total packed order has already been minimized; it does not invalidate earlier minimum-order arguments.
- The three explicit disjoint-cycle contradictions in Lemma 1 are genuine vertex-disjoint directed cycles in the original digraph.
- The enumeration checks only the seven-vertex local hand proof and is not evidence for the parent conjecture.
- Lemma 4 chooses fan targets outside the sink's two targets before applying domination; this is what removes `x` from the ladder. No stochastic independence is assumed.
- The partner collar is applied to the actual R-supported witness `r2`; the impossible `|R|>=7` branch is excluded because the inherited state has exactly four remainder vertices.
- A cross transition or neutral exchange is not counted as a fourth cycle by itself.
- No use is made of the 2026 one-reversed-arc relaxation as if it produced genuine directed cycles.
- Full BT4 is not proved and no novelty claim is made.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The exact-two-predecessor heavy-triangle cage is sharpened from two unspecified heavy-fan escapes to an exact lexicographic seven-vertex cage with four fixed-pair five-witnesses, three pairwise R-disjoint x-free escape paths, and a two-set Hall dichotomy reducing target dependence to one explicit three-fan collision. The next unpaid step is packed-segment/port closure, not remainder-interior disjointness.
