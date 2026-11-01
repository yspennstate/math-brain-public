# C0060: hitting a cut-point fiber is not a separator (proof, pending w347)

Let G be connected, let c be a cut vertex, and let a,b lie on different sides with finite G-paths to c. Let F be any finite subset of {c} x Z. Choose a height z whose copy (c,z) is not in F. The path from (a,s) vertically to (a,z), then along a-c-b at height z, then vertically to (b,t), avoids F. Thus a finite set of hits on a cut-point fiber does not separate its two sides in G x Z.

For the three-vertex path a-c-b, deleting {(c,z): |z|<=H} still leaves a path from (a,0) to (b,0) of length 2H+4, going through height H+1. It is shortest because every crossing must use a middle vertex with |z|>=H+1, requiring at least 2(H+1) vertical and two horizontal edges.

This refutes the inference 'the interlacement hits every corner region, therefore it blocks every crossing' used heuristically in C0060-A001. Hitting a region and creating a separating occupied set are different events. The interlacement trace is infinite; this finite-fiber example does not determine its vacant threshold, its crossing probabilities, or u*. No isotropic capacity exponent from the earlier heuristic is used as a theorem here.
