# P0104 core-proof checkpoint

## Scope

The original source statement is pending recovery. Current openness UNKNOWN. The selected precise model is undirected nearest-neighbour FPP on Z^2 with iid Uniform[1,2] edge times, endpoints 0 and n e_1, n >= 1. The proposed exponent is Var(T_n)=n^(2/3+o(1)); this has not been proved.

## Saved lemma C1: exact finite reduction

Let G_n be the induced nearest-neighbour graph on the vertices [-2n,2n]^2 intersect Z^2. Then T_n equals the minimum over the finitely many simple paths in G_n from 0 to n e_1, for every configuration of weights in [1,2]. In particular T_n is a bounded function of finitely many independent coordinates.

Proof. The direct horizontal path has n edges and cost at most 2n. Every path with more than 2n edges has cost greater than 2n. A path leaving the square must have at least 2n+1 edges before its first vertex outside it, so cannot improve the direct path. Removing a loop strictly decreases cost because every edge weight is at least 1. Thus a minimizing path can be chosen among the finite collection of simple paths in G_n. Conversely these are allowed lattice paths. Both minima agree. Also n <= T_n <= 2n.

This is an elementary special-case reduction, not a novel FPP theorem and not a solution of P0104. Independent review by w362 is pending.

## Single hardest remaining gap

Prove two-sided estimates at the n^(2/3) scale for the integral of the edge replacement-threshold covariance under independent coordinate resampling. The exact integral and its load-bearing hypotheses will be written next. No independence of different geodesic corridors is being assumed.

NEXT: Derive the exact per-edge covariance kernel, then the finite-product resampling identity.
