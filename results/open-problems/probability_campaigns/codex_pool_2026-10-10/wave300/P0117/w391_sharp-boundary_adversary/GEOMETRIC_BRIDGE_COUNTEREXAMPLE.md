# Direction does not imply finite-strip confinement

This is a counterexample to a geometric bridge only, not to nonatomic iid P0117.

Give every edge of Z^2 weight 1. For each integer k define f(k)=sign(k) floor(sqrt(abs(k))), with f(0)=0. Form a doubly infinite staircase by taking the horizontal edge from (k,f(k)) to (k+1,f(k)) and then the vertical steps at column k+1 up to height f(k+1).

The function f is nondecreasing. The staircase is an injective path of east and north steps. Every finite contiguous segment is coordinatewise monotone, so its length equals the Manhattan distance between its endpoints. Every competing path has at least that many edges, all of weight 1. Hence every staircase segment is a global geodesic.

At either end, |f(k)|/|k| tends to zero. The two end directions are therefore +e1 and -e1. But f(k) tends to +infinity and -infinity at the corresponding ends, so neither tail is eventually contained in any finite horizontal strip.

This disproves the assertion that an axis-asymptotic bigeodesic must geometrically stay within a finite strip. It does not remove the need for a model-specific confinement theorem in a nonatomic iid law. In particular, uniqueness and iid nonatomicity are not supplied by this constant-law construction.
