# BT4 account03/B06 r12 — mixed-return apex and neutral-fork reduction

**Candidate:** `BT4-F3-R3-MIXED-APEX-NEUTRAL-FORK-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Target:** Bermond–Thomassen `k=4`: every finite loopless simple digraph with minimum outdegree at least 7 contains four vertex-disjoint directed cycles. Digons are allowed in the target; this branch is the inherited oriented minimal-counterexample branch.  
**Target status:** `OPEN_NOT_PROVED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## Fresh governing input

The current collective-open-problems control keeps account03/B06 on exact constrained search / symbolic families for BT4, with named partner `account04/B04`.

The named other-account input actually used here is account04/B04 `BT4-F3-R3-SLACKONE-LADDER-v1`, shared handoff blob `d690c16215b074eb27b607e4fe2bd5df24a12d59`, canonical scientific commit `5e34513fe4276b02db2c8edc63fc3a842d3778eb`.

Its R3-D branch supplies the following exact state. There is a current three-cycle packing `(J,L,M)` of total order `n-3`, with residual DAG `R={a,b,t}` and sink `t`. The sink fan type is `(3,2,2)`: `J` is heavy and the two light supports are `L,M`. Both light supports return to `t`, at unique ports

`c -> t` on `L`, and `e -> t` on `M`,

and the exact two-target light fans are

`N+(t)∩L={c+,c++}`, `N+(t)∩M={e+,e++}`.

Repeated domination of the two return arcs produces opposite light-to-light ladder paths whose internal vertices lie in `{a,b}` and every internal ladder vertex also sends an arc to `t`. If the opposite ladders meet internally, the partner already converts this to a taxed same-support bypass. The present report treats the complementary internally-disjoint branch.

## 1. The mixed return is only a triangle or quadrilateral

Let

`P : e -> ... -> c`, `Q : c -> ... -> e`

be the internally-disjoint opposite ladder paths, with interiors contained in `{a,b}`. Their union `K=P∪Q` is a simple directed mixed cycle through `c,e`. Because the branch is oriented, `P,Q` cannot both be direct, and because there are only two residual vertices,

`3 <= |K| <= 4`.

Every vertex of `K` sends an arc to `t`: this is true for the two return ports `c,e`, and for every residual ladder vertex by construction.

Moreover `t` has **zero** outneighbors on `K`. It has no arc to `a,b` because it is the sink of the residual DAG; and it has no arc to `c,e` because `c->t,e->t` and the inherited branch is oriented.

## 2. Deleting K forces a 3-hit apex

Suppose every vertex outside `K` had at most two outneighbors on `K`. Since every vertex has exact outdegree seven in the inherited normal form,

`delta+(D-K) >= 7-2 = 5`.

The established `k=3` theorem would then give three vertex-disjoint directed cycles in `D-K`; together with `K` this is a forbidden four-pack. Therefore:

> **Mixed-cycle apex lemma.** There exists `z∉K` with `|N+(z)∩K|>=3`. The vertex `z` is never `t`.

This is the decisive extra information obtained from the global no-four-pack condition.

## 3. Triangle branch: fresh packed cross or residual triple-hit

If `|K|=3`, then `K` contains the two packed ports `c,e` and exactly one residual vertex. The apex `z` hits all three vertices of `K`.

If `z` is packed, it necessarily creates a **fresh packed-to-packed cross whose source is outside K**:

- `z∈J`: among its three hits are `c` and `e`;
- `z∈L`: it hits `e`, giving an `L->M` cross (and its hit on its own port `c` forces `z=c^-` by chordlessness);
- `z∈M`: symmetrically it gives an `M->L` cross.

The only non-cross leaf is that `z` is the unused residual vertex; then it hits the whole triangle. Thus the triangle branch is reduced exactly to

`FRESH_PACKED_CROSS` **or** `UNUSED_RESIDUAL_TRIPLE_HIT`.

## 4. Quadrilateral branch: fresh packed cross or an immediate two-residual fork

If `|K|=4`, then `K={c,e,a,b}`. Hence the apex cannot be residual: the only residual vertex outside `K` is `t`, which has zero hits. So `z` is packed.

If `z∈J`, at most two of its at least three hits can be residual (`a,b`), so it hits `c` or `e`; this is a fresh `J->L/M` packed cross.

Suppose `z∈L`. If `z->e`, again there is a fresh packed cross `L->M`. If there is no such cross, then at least three hits among `{c,e,a,b}` and the missing hit `e` force

`z -> c,a,b`.

Because `z,c` lie on the chordless directed cycle `L`, the intra-support arc `z->c` is possible only for the immediate predecessor:

`z=c^-`.

Thus the only quadrilateral `L`-exception is the exact fork

`c^- -> c`, `c^- -> a`, `c^- -> b`, and `c^- !-> e`.

The `M`-exception is symmetric: `z=e^-` and `z->e,a,b` while `z !-> c`.

Therefore:

> **Quadrilateral apex dichotomy.** Every R3-D mixed quadrilateral gives a fresh packed-to-packed cross from a source outside `K`, unless one light support has an immediate-predecessor apex hitting its own return port and **both** residual vertices.

This repairs the tempting but false stronger claim that the quadrilateral always gives a fresh cross.

## 5. The exceptional fork produces two exact neutral exchanges

The exceptional fork is substantially more rigid than a generic failure.

Assume without loss of generality that it lies on `L`, so `z=c^-` and

`c^- -> a,b,c`.

Because `K` is a quadrilateral, both `a,b` occur as internal ladder vertices; therefore

`a->t`, `b->t`.

The partner's exact light fan gives `t->c++`. For either `r∈{a,b}`, let `r'` be the other residual vertex and define

`C_r = c^- -> r -> t -> c++ -> L[c++,c^-] -> c^-`.

For `|L|=3`, the segment `L[c++,c^-]` is the single vertex `c++=c^-`; the formula is the directed triangle `c^- -> r -> t -> c^-`.

For every `|L|>=3`, the directed `L`-segment from `c++` through `c^-` contains exactly `|L|-2` vertices. Adding `r,t` gives

`|C_r| = |L|`.

Moreover `C_r` contains precisely the vertices of `L` except `c,c+`, and absorbs `r,t`. Consequently replacing `L` by `C_r` while retaining `J,M` preserves the total packed order `n-3`, and its new residual set is exactly

`{r',c,c+}`.

A directed cycle in this three-vertex remainder would be a fourth cycle disjoint from `J,M,C_r`. Hence a genuine counterexample forces **both**

`D[{a,c,c+}]` acyclic, and `D[{b,c,c+}]` acyclic.

The symmetric `M`-fork forces both `D[{a,e,e+}]` and `D[{b,e,e+}]` acyclic.

A useful immediate consequence is a successor wall: if (say) `a->c` is the incoming residual edge to the port along `K`, then `c+ !-> a`, because otherwise `c->c+->a->c` is a directed triangle in the neutral-exchange remainder. The same statement holds for `b` and symmetrically at `e`.

So the exceptional no-cross leaf is not an unconstrained survivor: it creates **two simultaneous exact size-neutral exchanges and two three-vertex acyclicity constraints**.

## 6. Exact constrained symbolic check

`checker.py` exhaustively enumerates the bounded ladder/apex geometry rather than sampling graphs.

- 4 possible internally-disjoint triangle ladder templates;
- 16 triangle apex-location cases: 12 force a fresh packed cross, 4 are exactly the unused-residual triple-hit leaf;
- 6 quadrilateral ladder templates;
- 102 chordlessness-compatible quadrilateral apex/hit patterns: 90 force a fresh packed cross and exactly 12 are the immediate two-residual fork exceptions;
- 156 neutral-fork cardinality/remainder checks for light support orders `3..80`, with zero violations.

The support-order check is only a finite sanity check; the cardinality proof above is uniform in `|L|` and `|M|`.

The exact checker output payload hash is

`4c36ba5c947b1298cf6aa5f1adb9ddaef15aae25d11533de5e1aa9fc915cef10`.

Local checker source SHA-256 before publication was

`d5ab8993ba3412402fd40c2875f947eaa4f9f05eb2367b7ae66feb6290bbf24b`.

Local checker-output file SHA-256 before publication was

`f266b25947b21da1b9e90560fec0166201d0880a1474789625a86412512a1f71`.

## 7. Failed stronger candidate and repair

The stronger local claim

> “Every quadrilateral mixed return forces a fresh packed-to-packed cross”

is false at the symbolic level. One exact exception is

`K=e->a->c->b->e`,

with `z=c^-` satisfying `z->c,a,b` and `z !-> e`.

This is **not** asserted to be a complete BT4 graph or counterexample; it is a local symbolic obstruction. The correct repair is the neutral-fork theorem above: this exception automatically supplies both `C_a,C_b` and hence both exchanged-remainder acyclicity obligations.

No full-graph certificate is claimed for this local obstruction, so no reduced or partial graph is being passed off as a global counterexample.

## 8. Exact next implication

The R3-D branch is now reduced to the following finite outputs after the partner's intersecting-ladder bypass branch is removed:

1. a fresh packed-to-packed cross from outside the mixed return cycle;
2. a triangle with an unused-residual triple-hit apex;
3. a quadrilateral immediate-predecessor fork with two neutral-exchange acyclic three-vertex remainders.

The next obligation is

`BT4-F3-R3-FRESH-CROSS-OR-NEUTRAL-FORK-SPLICE-v1`:

- feed output (1) into the established fresh-port / third-support connector wall and the exact R4 fresh-cross machinery;
- for output (2), apply arc domination to the two packed hits of the residual triple apex and force a packed fresh source, same-support bypass, third-support mediation, SIX, or an exact restart;
- for output (3), combine the two simultaneous exchanged-remainder acyclicity constraints with the orientation of `K`, especially the successor wall at the residual predecessor of the return port, and force a strict packing decrease, a cyclic exchanged remainder, a fresh reverse connector, third-support mediation, or a fourth cycle.

BT4 remains **open**. No full proof or novelty claim is made.
