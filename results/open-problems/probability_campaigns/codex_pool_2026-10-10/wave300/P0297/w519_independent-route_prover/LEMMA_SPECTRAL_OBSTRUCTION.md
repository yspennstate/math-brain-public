# W519-L3: a spectral exponent alone does not determine metric dimension

For 0<theta<=1 put d_theta(x,y)=|x-y|^theta on R^2, retain planar Lebesgue measure, and retain standard Brownian motion with generator (1/2)Delta. Then:

* d_theta is a metric inducing the Euclidean topology.
* dim_H(R^2,d_theta)=2/theta and the Lebesgue mass of its radius-r ball is pi*r^(2/theta).
* The Brownian transition density is p_t(x,y)=(2*pi*t)^(-1) exp(-|x-y|^2/(2*t)), so the on-diagonal spectral exponent d_s=-2 lim log p_t(x,x)/log t is 2 for every theta.
* Brownian mean exit time from the d_theta-ball B_{d_theta}(x,r), started at its center, is r^(2/theta)/2. Thus the mean-exit walk exponent is 2/theta, not universally 2.

Proof. The triangle inequality follows from (a+b)^theta<=a^theta+b^theta. The ball is the Euclidean ball of radius r^(1/theta). For every set A, diam_{d_theta}(A)=(diam_E(A))^theta; therefore the s-dimensional Hausdorff covering sum in d_theta equals the theta*s-dimensional covering sum in the Euclidean metric, with correspondingly transformed cutoff. The planar dimension is consequently 2/theta. Changing the auxiliary metric does not change the generator, measure, or transition kernel. For a Euclidean disk of radius R, u(z)=(R^2-|z-x|^2)/2 solves (1/2)Delta u=-1 with zero boundary values. Hence its mean exit time from the center is R^2/2. Substitute R=r^(1/theta).

Scope of the obstruction. This disproves a general implication from spectral dimension 2 and planar Brownian time change to metric Hausdorff dimension 2. It does not refute P0297 or the full strong-LQG axioms. When theta<1 the metric is not a length metric: for any nonconstant continuous curve between distinct endpoints, partitions with largest Euclidean step delta decreasing to zero have sum of d_theta steps at least delta^(theta-1) times the Euclidean endpoint distance, which tends to infinity. Thus those examples are excluded by the strong-LQG length-space axiom.

This is an elementary standard snowflake construction reconstructed here; no novelty claim. An LQG proof must use additional metric structure and actually identify its unknown exponent. Having the entire field or entire time-change law may determine more information; this claim concerns the displayed exponents alone.

Source: owner-own-work campaign derivation. Independent reviewer: w521, pending.
