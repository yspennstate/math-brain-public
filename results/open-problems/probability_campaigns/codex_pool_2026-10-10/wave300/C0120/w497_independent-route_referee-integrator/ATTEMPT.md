# C0120 independent route (written before opening w495 or w496 proof files)

Target: For the Gaussian up/right path model in Chatterjee, arXiv:0810.4221v2, Section 8, seek constants C and epsilon>0 with Var(M_n) <= C n^(1-epsilon) for all n>=2. This is a working formalization of Section 12(3), not a theorem or a verbatim quote. Current openness: UNKNOWN.

Independent route: use spatially localized dynamic programming and a conditional variance decomposition across dyadic time slabs. At each slab boundary write M_n as the maximum over entrance and exit positions of the optimal interior weight plus exterior weights. Expose the environment slab by slab, and bound each martingale difference by a path-switching comparison between two independently resampled slabs. The hoped-for saving is that near-optimal paths can reroute around a slab whose contribution is unusually high. This avoids taking the OU-noise-chaos implication or the hypercontractive BKS estimate as the main engine.

Load-bearing estimate needed: a uniform quantitative bound on the squared resampling effect for a slab of width m, after maximizing over its boundary points, strong enough that the sum over a dyadic partition is O(n^(1-epsilon)). It must account for dependence between the chosen entrance/exit and the slab weights; an unconditional tail bound cannot be inserted after maximization. I have no such estimate yet. Until it is proved, this route is a sketch and establishes no power bound.

Source discrepancy to audit in peers: the cited 2008 paper studies M_n (zero-temperature maximum) in 1+1 Gaussian vertex disorder. The intake's Var(log Z_n) in general dimension describes a different problem.
