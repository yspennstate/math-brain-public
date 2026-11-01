# Independent derivation, before paired proof

## Finite-width obstruction

A global geodesic ray means an injective adjacent-vertex sequence indexed by the nonnegative integers, every finite contiguous subpath of which minimizes passage time in the ambient lattice. Injectivity matters when a law permits zero-weight edges: repeated traversal of a zero-cost finite cycle is not a ray in this statement.

Let iid finite nonnegative edge weights on nearest-neighbor Z^2 have a nonconstant law. Choose finite 0<=a<b with p=P(t<=a)>0 and r=P(t>=b)>0. No moment assumption or nonatomicity is needed below. Fix an integer w>=0 and S_w=Z x {-w,...,w}. Let

L=floor(a(4w+2)/(b-a))+1,
q=r^((2w+1)L) p^(L+4w+2).

For an integer left column s, make all L(2w+1) horizontal edges inside the strip between columns s and s+L expensive (weight >=b). Make the L horizontal edges on exterior row w+1, and the 2(2w+1) vertical edges on boundary columns s and s+L from row -w to row w+1, cheap (weight <=a). These two edge sets are disjoint, so this finite event has probability exactly q>0.

For any u=(s,y) and v=(s+L,z) with y,z in [-w,w], every path from u to v contained in S_w traverses each of the L intervening column cuts and hence has weight >=bL. This remains true if it backtracks outside the longitudinal block. The exterior-row competitor has at most L+4w+2 cheap edges and weight <=a(L+4w+2)<bL. Therefore no globally minimizing finite path can contain a subpath crossing the block while staying in S_w.

Place blocks at s_j=j(L+1). Their edge supports are disjoint; this independence is unconditional and does not rely on a selected geodesic. For n>=1, every strip-contained global geodesic from column 0 to column n crosses all m=floor((n+1)/(L+1)) full blocks. Consequently its existence has probability at most (1-q)^m <= exp(-qm).

There are almost surely arbitrarily distant successful blocks in both horizontal directions. An injective infinite path confined to S_w has unbounded horizontal coordinate because each bounded horizontal interval contains finitely many strip vertices. Thus it must cross one of these blocks. There is almost surely no global geodesic ray contained in S_w, or eventually contained there. Countable unions over integer widths and vertical shifts, and rotation by 90 degrees, give the same conclusion for every finite horizontal or vertical strip simultaneously, including a strip selected after observing the environment.

Boundary: for a constant law c>=0 the horizontal line is a bigeodesic. Nondegeneracy is therefore necessary for this strip claim. This does not prove P0117: arbitrary bigeodesics need not lie in finite axis-aligned strips.

## Atomic full-target counterexample, conditional construction

Let iid weights be a with probability p and b>a with probability 1-p, where a>0. Declare the a-edges open and orient horizontal edges east and vertical edges north. Assume the probability theta(p) of an infinite open directed ray from the origin is positive. The corresponding backward-ray event has the same probability and depends only on edges whose tail has x+y<0; the forward event depends only on edges whose tail has x+y>=0. They are independent. With probability theta(p)^2>0 both rays exist and concatenate into an injective bi-infinite directed path through the origin.

Every finite contiguous segment is coordinatewise monotone, so it uses exactly the Manhattan distance many edges, all of weight a. Every competing path has at least that many edges, each of weight >=a. The concatenated path is therefore a bigeodesic. The existence of some such path is a translation-invariant event, and iid translation ergodicity upgrades positive probability to probability one. This construction will be instantiated with a primary source for supercritical oriented percolation. It refutes only an extension to all nondegenerate atomic positive-speed laws.

## Single hardest open piece

The strip theorem is pointwise in width, with q deteriorating exponentially in the number of prescribed edges. Passing to growing widths requires controlling the accumulated obstruction probabilities. Neither a union over all fixed widths nor an asymptotic direction statement supplies finite-width confinement.
