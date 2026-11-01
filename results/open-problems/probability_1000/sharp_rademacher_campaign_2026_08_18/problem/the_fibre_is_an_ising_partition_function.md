# The correlation excess is an Ising partition function on the sharing graph

Author: session 6c4d55a4, 2026-08-20. Derived and then attacked; 12 of 12 exact matches including
the shapes chosen to break it. Nothing here proves the sharp Rademacher conjecture. What it does is
replace the campaign's central unknown quantity `c` with a closed form.

## Statement

Let `T` be a linear NAE triangle system (no two triangles share two coordinates) in which every
triangle carries **at most two shared coordinates**. Build the graph `G`:

- vertices = the shared coordinates,
- edges = the triangles carrying exactly two shared coordinates (each such triangle joins its two).

Let `C(G)` be the cycle space of `G` — the even subgraphs — and `|S|` the number of edges of `S`.
Then

    |A| / (2^r (3/4)^k)  =  SUM_{S in C(G)} (-1/3)^{|S|}   =:  Z(G)

and therefore, with `c := k*beta - ell` and `ell = r - log2|A|`,

    c  =  log2 Z(G).

## Proof

Integrate out each triangle's private coordinates first.

- A triangle with **three** private coordinates contributes a constant factor `6 = 2^3 (3/4)`.
- A triangle with **two** private coordinates and one shared `u` contributes, given `x_u`, exactly
  `3` of the `4` assignments — independent of the value of `x_u`. Constant factor `2^2 (3/4)`.
  *This is why trees are exactly independent and c = 0 on them.*
- A triangle with **one** private coordinate and two shared `u, v` contributes `2 - [x_u = x_v]`.
  Writing `[x_u = x_v] = (1 + x_u x_v)/2` for `+-1` variables,

      2 - [x_u = x_v]  =  (3 - x_u x_v)/2  =  (3/2) (1 - x_u x_v / 3),

  which is `2^1 (3/4)` times `(1 - x_u x_v / 3)`.

So every triangle contributes its independence factor `2^{#private} (3/4)`, and the ONLY residual
dependence is one Ising-type edge weight `(1 - x_u x_v / 3)` per two-shared triangle. Hence

    |A| = 2^r (3/4)^k * < prod_{(u,v) in E} (1 - x_u x_v / 3) >,

the average being uniform over the shared coordinates. Expanding the product,

    < prod (1 - x_u x_v/3) > = SUM_{S subset E} (-1/3)^{|S|} < prod_{(u,v) in S} x_u x_v >,

and `< prod_S x_u x_v > = 1` if every vertex has even degree in `S`, `0` otherwise. The surviving
subsets are exactly the even subgraphs. QED.

This is the van der Waerden / high-temperature expansion. The system is an Ising model at the single
fixed coupling `-1/3`, on the sharing graph, and `c` is the log of its partition function.

## Immediate corollaries

**Trees and forests.** `C(G)` is trivial, `Z = 1`, `c = 0` exactly — for every topology. That is the
campaign's P5, in one line, and it also explains it: sharing ONE coordinate leaves a factor
independent of the shared value, so tree structure never couples anything.

**Pure m-cycle.** `C = {empty, C_m}`, so `Z = 1 + (-1/3)^m` and `|A| = 3^m + (-1)^m`. Brute-force
verified m = 3..10: 26, 82, 242, 730, 2186, 6562, 19682, 59050.

**Parity.** `c > 0` iff `Z > 1`. On a single cycle that is exactly `m` EVEN, and `|c|` decays like
`3^-m`. The excess over independence is a single vector, either way.

**Why a cycle BASIS is the wrong statistic.** The sum runs over the cycle SPACE, not a basis. In a
theta graph the third cycle is the sum of the other two and appears in its own right; in two
disjoint cycles the union appears as the cross term. Both were measured exactly
(theta(2,3,4) = 2180/2187; two disjoint 4-cycles = 6724/6561). A basis sum matches neither.

**Why the intersection graph misleads.** Three triangles meeting at a single hub make a triangle in
the intersection graph but contribute no edge to `G` at all, so they carry no cycle. Measured:
k=3, r=7, intersection-graph cycle rank 1, `c = 0`.

## What this does to Conjecture RC

RC is `tightness = d_cb*beta/ell <= 1`, equivalently — using the campaign's proved `d_cb <= k` —

    c <= beta * (k - d_cb).

With `c = log2 Z(G)` that becomes a statement with no unknowns on the left:

    **RC  <=>  Z(G)  <=  2^{beta (k - d_cb)}  =  (4/3)^{k - d_cb}.**

Consequences worth stating:

1. Every system with `Z <= 1` satisfies RC automatically, since `d_cb <= k` is proved. So **the
   entire content of RC lives on `{Z > 1}`** — graphs whose even-subgraph sum is dominated by
   even-cardinality subgraphs.
2. RC can only fail where `d_cb = k` (maximal) and `Z > 1`, or more generally where `Z` outruns
   `(4/3)^{k-d_cb}`.
3. Because linearity forbids two triangles sharing two coordinates, `G` has no multi-edges, so every
   nonempty even subgraph has at least 3 edges and contributes at most `3^-3 = 1/27` in absolute
   value. `Z` is therefore pinned near 1 unless the graph carries MANY short even subgraphs.

That is a counting question about even subgraphs of a graph, which is a far more tractable object
than the selector distance. **The remaining RC question is: can a linear triangle system have enough
short even cycles to push `Z` above `(4/3)^{k - d_cb}`?**

## Scope and what is NOT claimed

- The statement is proved only when every triangle carries **at most two shared coordinates**. A
  triangle with three shared coordinates makes `G` a hypergraph and the expansion above does not
  apply as written; the weight is then the NAE indicator itself, not a two-body Ising factor. Random
  sampling hits that case often, so it is not a rare corner. Extending the law there is the obvious
  next piece and is not done.
- Nothing here bounds `d_cb`. RC is reduced, not proved. The reduction is only as useful as the
  proved bound `d_cb <= k`, which is the campaign's, not mine.
- Nothing here bears on the sharp Rademacher conjecture directly. `c` is a Layer-II quantity and the
  conjecture's difficulty was located at Layer III, `ell = 1`, by `STATE_OF_THE_PROOF.md` §1.

## Verification record

`cyclespace_law.py` (<box>, /tmp): 12 of 12 exact to 1e-9 — pure 4- and 5-cycles, two
disjoint 4-cycles, two cycles sharing a vertex-path, K4 as six triangles (cycle space dimension 3),
theta(2,2,3), theta(2,3,4), a 6-cycle with a chord, two 4-cycles glued at a vertex, and three random
linear systems. `cycle_formula_check.py`: the m-cycle formula against brute force, m = 3..10.
`c_additivity.py`: 13 of 13 on disjoint, pendant and vertex-glued shapes.
