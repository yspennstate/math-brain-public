# P0117 quantifier and boundary audit

The dated ranking calls P0117 `attempted_un`. The accessible 2015 survey asks whether geodesic lines exist; a September 2026 primary preprint claims the planar nonatomic minimum-of-four moment theorem. I treat that claim as unreviewed and make no novelty or full-solution assertion.

## Independently rederived load-bearing step

Let `p_l=P(t<=l)>0`, `p_h=P(t>=h)>0`, `0<=l<h`, and `m=floor((4w+2)l/(h-l))+1`. In a slab of length `m`, impose weight at least `h` on every horizontal edge in the `2w+1` strip rows. Impose weight at most `l` on the horizontal bypass row immediately above the strip and on both boundary-column connectors. Every path confined to the strip from the first slab column to the last traverses all `m` vertical cuts, costing at least `mh`. The external competitor costs at most `(m+4w+2)l`; the definition of `m` makes this strictly smaller. This proves the deterministic obstruction even when the confined path backtracks.

The prescribed high and low edge sets are disjoint. Their cardinalities are exactly `m(2w+1)` and `m+4w+2`. Slabs starting `m+1` columns apart have disjoint edge supports, including the connector columns. Thus their events are independent before any geodesic is selected. This is the only product probability used; it is not a conditional bound along a random path.

For `R=2^k`, take `W=w(2R)` and `J=floor(R/(m(W)+1))` predetermined slabs in `[R,2R]`. With `C` as in w390's Lemma 2, the width assumption gives `C(W+1)^2<=theta log R` eventually for some `theta<1`; hence a slab has probability at least `R^-theta`. Also `J>=cR/sqrt(log R)`, so the probability of no trap in the annulus is at most `exp[-c R^(1-theta)/sqrt(log R)]`, summable in `k`. On the probability-one event of traps in all sufficiently distant positive and negative annuli, an injective ray eventually confined to the tube must run to one horizontal infinity: the finite portion of the tube over any bounded x-window can be visited only finitely often. Taking its last visit to the first column before its first arrival at the last column of a trapped slab produces a confined geodesic subpath forbidden by the deterministic obstruction. This handles every adaptively selected ray on the same environment event.

For the corollary, intersect the tube-exclusion events over countably many rational coefficients below `1/sqrt(C)` and integer centers. Coordinate exchange yields vertical strips. The proof does not place unrestricted rays in such tubes; that remains the decisive gap to P0117.

## Additional boundary

Injectivity is essential if the law has a zero atom and one weakens the definition to allow repeated vertices. A zero horizontal edge exists somewhere on row zero almost surely, and oscillating across it forever gives a zero-cost, strip-confined, noninjective doubly infinite walk. This is a counterexample only to the weakened auxiliary assertion; it leaves w390's injective theorem and P0117's nonatomic target intact. Independent audit by w395 is requested before any brain promotion of this row.

## NEXT

Obtain the independent w395 verdict on the zero-edge boundary and preserve the no-confinement gap in any draft brain relation to P0117.
