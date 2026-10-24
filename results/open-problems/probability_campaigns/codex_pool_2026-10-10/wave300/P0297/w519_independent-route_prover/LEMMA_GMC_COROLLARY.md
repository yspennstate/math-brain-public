# W519-L5: the Euclidean logarithmic clock exponent of subcritical disk GMC

Fix 0<gamma<2. On the unit disk D, let h be the zero-boundary GFF with covariance normalized to have singularity log(1/|x-y|). Let mu_gamma be the GMC of planar Lebesgue measure constructed using the dyadic circle averages, mu_n(dy)=2^(-n*gamma^2/2)*exp(gamma*h_{2^(-n)}(y))*dy and its almost-sure weak limit. Almost surely, for mu_gamma-almost every interior x,

lim_{r down to 0} log[(1/pi) integral_{B(x,r)} log(r/|x-y|) mu_gamma(dy)] / log(r) = 2-gamma^2/2.

Proof. The unit disk meets the boundary regularity condition (A0) of Falconer--Jin, arXiv:1601.00556v4, Section 2: it is convex with smooth boundary. Lebesgue measure has exact dimension 2, and gamma^2/2<2. Their Corollary 2.3 therefore gives local mu_gamma mass exponent a=2-gamma^2/2>0 at mu_gamma-almost every x, almost surely. Apply W519-L2 at each such x. Every x is interior, so sufficiently small disks lie in D. This proves the displayed potential exponent.

Deterministic local extension. If w is a strictly positive continuous function on D and mu'=w*mu_gamma, the same assertion holds for mu'-almost every x. For small disks about x, continuity bounds w between two finite positive constants; this bounds both the ball mass and the displayed potential between constant multiples of their unweighted counterparts. Logarithmic exponents are unchanged, and the two measures have the same null sets. This extension does not require w to be independent of h.

This is a derived corollary of an established exact-dimensionality theorem, not a claimed new dimension result. It is an exponent for Euclidean balls. Calling the potential a quenched mean Brownian time-change exit clock additionally requires the correct occupation identity; it does not turn it into a metric-ball or sample-path exponent.

Primary input: Kenneth Falconer and Xiong Jin, Exact dimensionality and projection properties of Gaussian multiplicative chaos measures, Corollary 2.3, PDF p.5, arXiv:1601.00556v4 (2018-12-13). https://arxiv.org/pdf/1601.00556

Source of the displayed derivation: owner-own-work campaign corollary, with the primary theorem explicitly attributed. Referee: w521, pending. No novelty claim and no formal proof receipt.
