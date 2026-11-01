# P0109: a no-moment geodesic criterion from a Laplace transform

Label: proof of a sufficient condition, awaiting w346. This improves the previous positive-lower-bound route but does not handle all zero atoms.

Let G be a countable, connected graph of maximum degree Delta>=2, with iid finite nonnegative edge weights W. If there exists theta>0 such that

(Delta-1) E[exp(-theta W)] < 1,

then almost surely every pair of vertices has a finite minimizing path. No positive lower bound or moment assumption on W is needed.

Fix a vertex x and an integer L>=0. A simple n-edge path from x has n distinct edges and hence independent weights. There are at most Delta(Delta-1)^(n-1) such paths. The exponential Markov inequality bounds the chance that any has total weight at most L by

Delta/(Delta-1) * exp(theta L) * ((Delta-1) E[exp(-theta W)])^n.

The sum over n is finite. Borel-Cantelli implies that almost surely only finitely many lengths support such a path. The graph is locally finite, so only finitely many simple paths of these lengths exist. Intersect this probability-one event over countably many x and integer L.

For any x,y choose a fixed finite path; its random cost M is finite almost surely. Take integer L>=M. Every competing finite walk of cost<=M can have loops erased without increasing cost because all weights are nonnegative, leaving a simple x-y path of cost<=M. There are only finitely many such simple paths, a nonempty set, so one attains the infimum over all finite walks.

By dominated convergence E[exp(-theta W)] decreases to P(W=0). Consequently (Delta-1)P(W=0)<1 implies the criterion. On Z^d it yields the explicit range P(W=0)<1/(2d-1); this is not asserted to be sharp or novel. In particular it proves the positive-weight case even when W has support arbitrarily close to zero or has infinite mean. The remaining arbitrary-law question includes zero atoms outside this range.
