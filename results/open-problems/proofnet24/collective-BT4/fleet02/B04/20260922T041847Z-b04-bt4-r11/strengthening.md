# Controlling strengthening — heavy-triangle cage has no heavy-target inports

This addendum strengthens the same-run primary report `report.md` (commit `71ff185ec9b372cc24c02c4630cd7c202d13eee7`, blob `596929efe56393d3ab515544fa33ec6a19e75c83`). The primary lemmas remain valid, but its Lemma 4 used two simultaneous inports when one inport already contradicts global minimum. This addendum is therefore controlling for the exact-two-predecessor branch.

Outcome remains `ESSENTIAL_STEP_APPLIED`. Brain status remains `WITHOUT_VERIFIED_BRAIN`.

## Setup inherited from the primary report

In the four-remainder global-`NO-SIX` heavy-triangle state, write

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

with `hi->ri->x->hi` for every `i` and `H not->x`.

Applying the named partner fleet03/B05 external-three-hit lemma to each saturation triangle shows that a remainder three-hit witness for `Ti` can only be `r_{i-1}`. All three predecessor relations would form a directed cycle in `R`. In the maximal remainder-witness branch exactly two occur; rotate indices so

`r0->r1,h1,x`,
`r1->r2,h2,x`.

The primary report then proves the exact residual identities

`N^+_{H union R}(r2)={x,h0}`,
`N^+_{H union R}(h1)={h2,r1}`,
`N^+_{H union R}(h2)={h0,r2}`.                    (1)

Hence `h1,h2` each have exactly five outneighbors in `S union U`.

## Strengthened lemma — one heavy inport already gives a strict smaller packing

Fix `i in {1,2}` and let `A in {S,U}` be the unique heavy target of `h_i`, so

`|N+(h_i) intersect A| >= 3`.                                  (2)

Then

`A not-> h_i`.                                                   (3)

### Proof

Suppose some `s in A` satisfies `s->h_i`. Choose a fan target

`y in N+(h_i) intersect A`

minimizing the forward directed distance

`d=dist_A(y,s)`.

The exact counterexample is oriented, so `h_i->s` is impossible and therefore `y!=s`. The at least three fan targets in (2) occupy at least three distinct positive distances in `{1,...,|A|-1}`. Consequently

`d <= |A|-3`.                                                    (4)

The closed walk

`C = s -> h_i -> y -> A[y,s]`

is a simple genuine directed cycle with

`|C|=d+2 <= |A|-1`.                                             (5)

Let `B` denote the other light packed cycle. The saturation triangle

`T0 = h0 -> r0 -> x -> h0`

is disjoint from `C`: `i` is 1 or 2, so `h_i notin T0`, and all remaining vertices of `C` lie on `A`. It is also disjoint from `B`. Therefore

`C, T0, B`

are three pairwise vertex-disjoint directed cycles. Since `|H|=3`, their total order satisfies

`|C|+|T0|+|B| <= (|A|-1)+3+|B|
               = |A|+|H|+|B|-1`,

strictly smaller than the globally minimum packing `(H,S,U)`. Contradiction. QED.

Thus **neither `h1` nor `h2` receives any arc from its heavy target**, regardless of whether their heavy targets coincide or split.

## Corollary — two compulsory heavy-fan escape crosses

Apply the controlling heavy-fan domination escape separately to `h1` and `h2`. For each `i=1,2`, since `h_i` is a cycle-supported five-witness heavy on `A_i` and `A_i not->h_i`, there is a genuine cross-packed transition ending on `A_i` with all internal vertices in `R`.

No disjointness between the two transitions is asserted. If `A_1=A_2`, both are interfaces into the same light support; if `A_1!=A_2`, there is an interface into each light support. In either case the exact-two-predecessor heavy-triangle cage now forces **two** heavy-fan escape outputs, rather than the weaker primary-report trichotomy.

## Additional light-witness rigidity

For any light cycle `L in {S,U}`, there is at most one vertex of `L` that sends directly to the sink `x` in the `(3,2,2)` state. Indeed, if `p->x` with `p in L`, the source-fan-two equality gives

`N+(x) intersect L = {p+,p++}`.

A second direct inport `q->x` on the same directed cycle gives the same consecutive two-vertex set, and a proper consecutive two-block has a unique predecessor, so `q=p`.

Every light three-hit witness for a saturation triangle sends to `x`; hence each light cycle contributes at most one such witness vertex. A single light vertex cannot witness all three saturation triangles: doing so requires its seven outneighbors to be exactly

`{x,h0,h1,h2,r0,r1,r2}`,

leaving no arc to its mandatory successor on its own packed cycle. Therefore, if no predecessor relation occurs, the three saturation triangles are covered by exactly two light inport vertices, one on `S` and one on `U`, in a `2+1` distribution. If exactly one predecessor relation occurs, the other two triangles are witnessed either by one unique light inport or by the two unique light inports.

This converts the primary report's generic multi-light-three-dominator output into a two-port object directly aligned with the campaign's reciprocal/third-port splice language.

## Strengthened heavy-triangle frontier

The four-remainder heavy-triangle saturation branch therefore has only two live forms:

1. **light-inport cover:** at most one predecessor relation occurs, and the remaining two or three saturation triangles are covered by at most the two unique light inports (with both light cycles necessarily used in the zero-predecessor case); or
2. **double escape cage:** exactly two predecessor relations occur, equations (1) hold, `h1,h2` are exact five-witnesses, neither receives an arc from its heavy target, and heavy-fan domination yields a cross-packed transition for each witness.

The earlier split-heavy/same-heavy distinction is not needed for the inport exclusion.

The first unpaid implication is now a genuine port-disjointness theorem: combine the two-port light-inport cover or the double heavy-fan escape cage with the universal reciprocal sink cross and fleet03/B05 third-port interface to force two disjoint replacement cycles, a strict smaller three-packing, an exchanged-remainder cycle, or a fourth cycle. The separate `SIX` closure remains unpaid.

No full BT4 proof or novelty claim is made.
