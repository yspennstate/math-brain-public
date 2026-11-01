# P0104 independent route, recorded before reading peer proofs

The ranking label suggests first-passage percolation fluctuation exponents, but the exact edge-weight law, dimension, and asserted exponent remained to be recovered at this first checkpoint. A candidate route was to partition the environment into separated blocks and use a resampling identity for passage-time variance. I would seek a quantitative bound on the probability that a geodesic uses a given block, conditional on outside weights. A matching lower bound would require a pivotal-block event with controlled probability. Each conditional product or martingale step must be proved under its sigma field. This is a plan, not a proof or a claim that P0104 remains open.

## Course correction after route-boundary check

w363 had already developed a spectral/resampling route, and the owner's earlier FPP campaign had a block-chaos framework. I therefore retire the above as an independent contribution; it overlaps both. My distinct route is **stationary Busemann cocycle covariance accounting**. If a directional stationary cocycle B exists, write its axis increments as a stationary sequence X_i. Its variance has the exact covariance formula Var(sum_{i=1}^n X_i)=n gamma(0)+2 sum_{k=1}^{n-1}(n-k)gamma(k). To transfer this to the original passage time one needs a proved L2 approximation of centered T(0,ne1) by the centered cocycle at error o(n^(1/3)), plus two-sided n^(2/3) variance for that cocycle sum. Neither premise is known here. In particular, summing covariance signs or using expected curvature without a quantitative rate cannot establish chi=1/3. This approach is distinct from w363's spectral measure and w364's interface profile, although all confront a two-sided fluctuation estimate.

The exact primary Question 13 leaves suitable laws and the meaning of the exponent open. For rigor, any attempted special case will specify iid nearest-neighbor edge weights and chi_2 via the directional log L2 fluctuation, if its limit exists.

NEXT: Audit the two peer proofs and identify the first invalid or missing load-bearing step; then derive the cocycle transfer lemma with its exact premises.
