# R20 idea-before-code — mod-5 route for the first unresolved three-cycle cactus family

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

This is the required idea-before-code note. It records the mathematical route before any checker for this run.

## Continuity

R20 remains on its current exclusive Bensmail–Marcille–Orenga Conjecture 2.6 successor claim, `operations/claims/BMO-2025-PUSHING-DELTA.md`. The stale scheduler-title I0100/Paley target is not reopened. The frozen all-graphs metric remains `n_all=8`.

The preceding stuck report identified the first clean unresolved test family as a central cycle `C_m`, `m>=4`, with two leaf triangles attached at distinct central vertices, and prescribed moves #3, #17, #22. The mod-3 interface had failed because equal residues can still be safely separated by a nonzero multiple of 3.

## New route: change the modulus rather than add an unbounded height coordinate

Let `Q=D+A` be the signless Laplacian and let `rho(v) in {0,1,2}`. Set

`y(v)=2-rho(v) in {0,1,2}`.

Since `Q 1 = 2d`, modulo 5 we have

`d+Q rho = d + Q(2-y) = 5d-Qy = -Qy (mod 5)`.

Thus it suffices to choose `y:V->{0,1,2}` so that `Qy` is a proper vertex-colouring modulo 5. Equivalently the induced edge contribution on `uv` is `y(u)+y(v) (mod 5)` and the colour at a vertex is the sum of these incident contributions.

This is the key categorical change. It is close in shape to neighbour-sum-distinguishing edge-weightings (the 1-2-3 line), but with the strong coboundary restriction that the edge weight on `uv` must be the endpoint sum `y(u)+y(v)` modulo 5. The source itself links cactus pushing to modulo arguments and to the 1-2-3 literature; the point here is that modulus 5 matches the three allowed push values much better than the previous modulus 3 state algebra.

## Leaf-triangle flexibility lemma to prove

Consider a triangle attached at a root `r`. Let `a=y(r)`, let `e` be the contribution to the root colour from edges outside this triangle, and let the two private triangle labels be `b,c in {0,1,2}`. The private-vertex colours are proper against each other iff `b!=c`, and the root-to-private edges are proper iff

`b != e+a (mod 5)` and `c != e+a (mod 5)`.

If `e+a` is `3` or `4`, it lies outside `{0,1,2}`. Then *every* distinct pair `b,c` works on the triangle, and the resulting root colour

`s=e+2a+b+c (mod 5)`

runs through three distinct residues because the distinct-pair sums are `1,2,3`. Hence a flexible triangle root has three possible final colours, enough to avoid two already fixed central-neighbour colours.

## Central-path lemma to prove

Put `y=0` at both nonadjacent attachment vertices. It is enough to label each arc between them so that:

1. all edges whose endpoints are internal to the arc are proper under the degree-2 colour `c_i=2y_i+y_{i-1}+y_{i+1} (mod 5)`;
2. the label immediately next to each root is in `{1,2}`;
3. across the two arcs, the two labels adjacent to each root have sum `3` or `4`, making `e+a in {3,4}` at that root.

The expected path library is tiny: for length 2 use endpoint type `(2,2)`; for length 3 use `(1,2)` or `(2,1)`; for every length at least 4 all four endpoint types `(1,1),(1,2),(2,1),(2,2)` should be realizable. A period-four interior word based on `1,0,0,0` appears to give a direct proof, not an exhaustive table.

If the two attachment vertices are adjacent, use the asymmetric root labels `y_0=0`, `y_1=1`, with the long complementary arc beginning at label `0` next to `y_1` and ending at label `2` next to `y_0`. Then `e+a=3` at both roots. Again a period-four word should handle every `m>=4`.

Once the central labels are fixed, each nonadjacent triangle root has a 3-element list of possible final colours and at most two fixed central neighbours to avoid. For adjacent roots, each 3-list loses at most one fixed central-neighbour colour; the two remaining lists have size at least 2, so one can choose unequal root colours across the edge joining the roots.

## Intended theorem scope

The target for this run is the following strict structural theorem, not the full cactus claim:

> Every cactus obtained from a cycle `C_m`, `m>=4`, by attaching one leaf triangle at each of two distinct vertices of the cycle has a proper pushing scheme with `rho in {0,1,2}`. In fact the construction will make all adjacent vertex sums distinct modulo 5.

This is exactly the simplest infinite family singled out by the preceding stuck review. It would be PARTIAL structural progress only; it does not move the frozen all-graphs metric `n_all=8` and does not close Conjecture 2.6 or the full cactus question.

No checker has been written yet in this run.