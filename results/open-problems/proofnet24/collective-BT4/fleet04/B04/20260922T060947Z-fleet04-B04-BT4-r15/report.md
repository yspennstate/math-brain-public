# BT4 fleet04/B04 — both-repeat F3 cover forces a short return cycle and a one-cut residual

Run: `20260922T060947Z-fleet04-B04-BT4-r15`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-F3-RETURN-CUT-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Digons are allowed in the source statement.

The current source boundary remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): the genuine Bermond--Thomassen conjecture is stated there as unresolved for every `k>=4`, while that paper proves the threshold only for cycles that are directed or become directed after reversing one arc. No relaxed cycle is counted below.

No authenticated mathematical-brain retrieval was used. This report uses only source-bound repository mathematics and the current private scientific archive.

## Exact inputs consumed

### Team lead

Latest complete fleet02/B04 lead report read:

`proofnet24/collective-BT4/fleet02/B04/20260922T051543Z-b04-bt4-r11/report.md`, blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933`.

Its controlling conditional proof uses an oriented exact-outdegree-seven minimal counterexample, arc domination and 3-vertex-strongness, then a three-cycle packing chosen first with minimum total packed order and second with maximum number of arcs in its acyclic remainder. The current four-remainder debts are the separate SIX interface, the triangular F2/F3 splice, and the heavy-triangle packed-port locks. In its heavy-triangle branch it also proves that the generic remainder-interior coalescence obstruction can be removed; actual packed-port splicing remains unpaid.

### Immediate same-slot predecessor

`BT4-R4-ARCMAX-TRIANGLE-COLLAPSE-v1`, fleet04/B04 run `20260922T051604Z-fleet04-B04-BT4-r14`, report blob `2f802a03755394931009175d7b6a5f94b0b2b084`.

In the canonical `|R|=4`, global-`NO-SIX` low-fan branch this proves that the old remainder sink `x` is unique, the source light cycle is a directed triangle, and after the neutral source pivot the F3 state has three saturation triangles covered by at most two vertices `{p,u}`.

### Assigned OTHER-account partner fleet01/B05

`BT4-R4-INPORT-TRIANGLE-3SWAP-v1`, run `20260922T043014Z-b05-bt4-r11`, report blob `96d3bc9140e9608b165d382851c332b3bbfa29be`.

That theorem gives an explicit size-neutral three-edge packed-cycle swap in the noncanonical long-source F2 / two-old-sink configuration. The previous arc-max theorem shows that its long-source and two-sink hypotheses cannot persist in the canonical representative, so I apply the partner theorem as a valid fallback transition for noncanonical minimum packings, not as a terminal branch and not as closure.

### Fresh decisive OTHER-account result

Fleet03/B06 `BT4-R4-F3-MAJORITY-CROSS-v1`, run `20260922T052316Z-fleet03-B06-BT4-r15`, report blob `697fde372dee5fec64d03923523d13fc6edcab7a`.

It starts exactly from this slot's triangular F3 state and proves a concrete short light-to-light cross. Its exact cover notation and conclusions are the starting point below. Its 18-vertex exact certificate also refutes the stronger shortcut that the cross can always be direct; therefore the one-remainder interior is retained here.

## Compact conditional end-to-end route

Assume BT4 false and enter the inherited oriented, exact-seven, arc-dominated, 3-vertex-strong minimal-counterexample normal form. Choose the three-cycle packing lexicographically by minimum total packed order and then maximum remainder-arc count. Run the inherited SIX / global-NO-SIX split.

In the canonical four-remainder global-NO-SIX source-pivot branch, the previous fleet04/B04 theorem reduces every surviving F3 state to the following exact geometry. The post-pivot packed source is

`S* = p -> x -> s -> p`,

`U` is the other light packed cycle, the freed source vertex is `q`, and

`K={r1,r2,r3}`, `q->K`, `K->x`, `x->q`.

For each `r in K`,

`T_r = q -> r -> x -> q`

is a directed saturation triangle. Every `T_r` has an external three-hit witness in `{p,u}`, where `u`, if present, is the unique `U`-vertex with `u->x`.

The fresh fleet03/B06 theorem proves that `u` in fact exists. Put

`A={r in K : p->{q,r,x}}`,
`B={r in K : u->{q,r,x}}`.

Then `A union B=K`; if `|A|>=2`, there is a directed `U->S*` path

`P : u -> p`  or  `u -> a -> p`, with `a in K\A`;

if `|B|>=2`, there is a directed `S*->U` path

`Q : p -> u`  or  `p -> b -> u`, with `b in K\B`.

If both sets repeat, `P,Q` can be chosen with disjoint interiors. The theorem below spends that exact output against the global no-four-cycle hypothesis rather than merely renaming the splice debt.

## Theorem — BT4-R4-F3-RETURN-CUT-v1

Work in the canonical triangular F3 state above.

### Part I: exact F3 case split

Exactly one of the following occurs.

1. **F3-AONLY.** `|A|>=2` and `|B|<=1`. There is a short `U->S*` cross `u->p` or `u->a->p` with at most one remainder interior vertex.
2. **F3-BONLY.** `|B|>=2` and `|A|<=1`. There is a short `S*->U` cross `p->u` or `p->b->u` with at most one remainder interior vertex.
3. **F3-BOTH.** `|A|>=2` and `|B|>=2`. There are internally disjoint opposite paths `P:u leadsto p` and `Q:p leadsto u`, each direct or with exactly one internal vertex in `K`, and their union is a genuine simple directed cycle `C` of order three or four.

The first two cases are exactly the fresh fleet03/B06 output. The content to prove is the structural collapse of F3-BOTH.

### Part II: return-cycle residual acyclicity

In F3-BOTH let

`I = (V(P) union V(Q)) intersect K`.

Because the inherited minimal counterexample is oriented, `P` and `Q` cannot both be direct: `u->p` and `p->u` would be a digon. Hence `1<=|I|<=2` and

`C=P union Q`

is a directed triangle when `|I|=1` and a directed 4-cycle when `|I|=2`.

Choose any

`c in K\I`.

Then the three cycles

`H`, `C`, `T_c=q->c->x->q`

are pairwise vertex-disjoint. Consequently

`D - (V(H) union V(C) union V(T_c))`                            (1)

is acyclic. Otherwise a directed cycle in (1) would be a fourth cycle disjoint from those three, contradicting the assumption that `D` is a BT4 counterexample.

This is a target-level use of the global no-four-cycle hypothesis, not a local degree surrogate.

### Part III: exact two-indirect subtype

Suppose both paths are indirect. Write

`P = u -> a -> p`, with `a in K\A`,
`Q = p -> b -> u`, with `b in K\B`.

Then `a!=b`. Indeed `a in B\A` and `b in A\B` because `A union B=K`.

Since `|A|,|B|>=2` and `|K|=3`, necessarily

`A=K\{a}` and `B=K\{b}`.

Thus the unique third vertex

`c = K\{a,b}`

lies in `A intersect B`, and

`C = u -> a -> p -> b -> u`.                                  (2)

After deleting `H`, (2), and `T_c`, the vertices left from the current packing/remainder decomposition are exactly

`(U-{u}) union {s}`.                                            (3)

Therefore the induced digraph on (3) is acyclic.

Write the support path obtained by deleting `u` from the directed cycle `U` as

`v1=u+ -> v2 -> ... -> vm=u-`.

Define

`IN={j : vj->s}` and `OUT={i : s->vi}`.

Acyclicity of (3) forces the **one-cut order**

`i > j` for every `i in OUT` and every `j in IN`.               (4)

Equivalently, if both sets are nonempty,

`max(IN) < min(OUT)`.                                           (5)

Proof: if `i<=j`, then

`s -> vi -> v(i+1) -> ... -> vj -> s`

is a directed cycle in (3), contradicting its acyclicity.

Thus the two-indirect F3-BOTH residual is no longer an arbitrary common-port return configuration: all `U->s` ports lie before all `s->U` ports on the broken support path `U-u`.

### Part IV: exactly-one-direct subtype

Suppose exactly one of `P,Q` is direct. Then `C` is a directed triangle using exactly one vertex `a` of `K`. Two vertices `c,d` remain in `K\{a}`.

For either choice of `c`, the three disjoint cycles `H,C,T_c` force the remaining induced graph

`D[(U-{u}) union {s,d}]`                                       (6)

to be acyclic. Interchanging `c,d` gives the second acyclic one-vertex extension. In particular the same one-cut order (4)--(5) already holds in the common subgraph `D[(U-{u}) union {s}]`, and each of the two leftover remainder vertices can be adjoined separately without creating a directed cycle.

This paired-extension condition is stronger than merely knowing that the short return cycle exists.

### Proof of Part I

`A union B=K` and `|K|=3`, so at least one of `A,B` has size at least two. The three alternatives distinguish whether exactly one or both do. The cross statements in the first two alternatives and the internally-disjoint opposite paths in the third are precisely `BT4-R4-F3-MAJORITY-CROSS-v1`.

Parts II--IV were proved above. QED.

## What this changes in the structural tree

The canonical F3 terminal node

`three saturation triangles covered by {p,u} -> short cross -> splice?`

now splits exactly as follows.

- **F3-AONLY:** one short `U->S*` cross with at most one remainder interior.
- **F3-BONLY:** one short `S*->U` cross with at most one remainder interior.
- **F3-BOTH-DIRECT/INDIRECT:** a directed 3-cycle `C` through the two light ports; two different three-cycle deletions force two acyclic one-vertex residual extensions.
- **F3-BOTH-INDIRECT/INDIRECT:** the exact 4-cycle `u->a->p->b->u`, a unique common-witness remainder vertex `c in A intersect B`, and the one-cut residual order `max(IN)<min(OUT)` on `U-u` relative to `s`.

Hence the both-repeat cover no longer needs a generic third-port extraction merely to understand the common-port return: the global no-four-cycle condition itself forces a rigid residual topological wall.

## Application of the assigned fleet01/B05 partner result

The partner's `BT4-R4-INPORT-TRIANGLE-3SWAP-v1` remains a valid equal-size transition whenever a noncanonical long-source F2 state with two old sinks occurs. The arc-max canonicalization used here excludes those hypotheses as a terminal representative. Therefore the branch policy is now explicit:

- long/two-sink noncanonical F2: partner three-edge neutral swap is an admissible transition;
- canonical four-remainder low-fan state: return to the arc-max triangular F2/F3 tree;
- canonical F3: apply the exact AONLY/BONLY/BOTH split above.

No neutral swap is counted as a fourth cycle.

## First exact unpaid implication

`BT4-R4-F3-CUT-SPLICE-v1`:

> Close the three F3 leaves above. For AONLY/BONLY, combine the guaranteed short one-way light cross with the lead's reciprocal/third-port and endpoint-distinct heavy-entry interfaces. For F3-BOTH, use the forced residual acyclicity and, in the two-indirect case, the one-cut order on `U-u` to show that the remaining interfaces either violate the cut, give a directed cycle in the residual, give two vertex-disjoint replacement cycles, strictly reduce the minimum three-packing, or enter SIX.

This is narrower than `BT4-R4-F3-SHORT-CROSS-SPLICE-v1`: the both-repeat common-port return has been converted to an exact length-3/4 cycle plus an acyclic residual cut constraint.

The separate F2, SIX, heavy-triangle consecutive-triple/location-lock and larger-remainder branches remain unpaid and are not promoted here.

## Failure checks and nonclaims

- `C` is one directed cycle, not two replacement cycles.
- The one-cut order is only a necessary consequence of residual acyclicity. Missing arcs are allowed; no completeness or tournament property is assumed.
- The two-indirect conclusion uses `|K|=3` essentially and is not asserted for larger remainders.
- The exactly-one-direct subtype retains the possible extra leftover remainder vertex; it is not silently dropped.
- The fleet03/B06 exact certificate proves that a one-remainder interior can genuinely be needed, so this report does not replace short paths by direct arcs.
- No target-level counterexample or full proof is claimed.
- No computation was used in the new derivation; the only computation mentioned is the source-bound peer certificate, which is not reclassified as proof of BT4.
- No tournament, edge-disjoint or one-reversed-arc substitute is used.

## Honest outcome

`ESSENTIAL_STEP_APPLIED`.

New essential step: in the canonical four-remainder triangular F3 state, a both-repeat witness cover forces an actual length-three or length-four directed return cycle through the two light ports. Pairing that cycle with an unused saturation triangle and the heavy packed cycle forces the entire complementary graph to be acyclic. In the two-indirect subtype this gives an exact one-cut ordering of all arcs between the surviving source vertex `s` and the broken light support `U-u`; in the one-direct subtype it gives two separately acyclic one-vertex residual extensions. BT4 remains open.