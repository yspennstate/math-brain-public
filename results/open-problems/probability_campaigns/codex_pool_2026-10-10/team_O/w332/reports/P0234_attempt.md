# P0234: quantitative margin and inverse moments, 2026-10-10

Status: a proved conditional strengthening of the prior covering-number reduction; the Poissonian-coloring problem remains unresolved in the inspected source cards. The missing model input is still a uniform spatial tail bound, not fixed-point avoidance.

Let K be a nonempty deterministic compact subset of Euclidean space, and F a random closed set. Assume that for 0<delta<=delta_0 there is a delta-net of K with at most C delta^(-d_0) centers in K, and that uniformly in x in K,

P(dist(x,F)<=2delta)<=C' delta^alpha, with alpha>d_0.

Put R=dist(K,F) and gamma=alpha-d_0>0. If R<=delta, compactness and closedness supply a point of K within delta of F (or use an arbitrarily close approximate minimizer); its net center is within 2delta of F. A union bound gives P(R<=delta)<=CC' delta^gamma. Taking delta down to zero gives P(R=0)=0. Compact K disjoint from closed F has positive separation, so this proves a positive random safe margin, not just no intersection.

New quantitative continuation: for every 0<p<gamma,

E[R^(-p)] <= delta_0^(-p) + CC' * p/(gamma-p) * delta_0^(gamma-p).

This follows from the layer-cake identity E[R^(-p)]=p integral_0^infinity delta^(-p-1) P(R<delta) ddelta, splitting at delta_0. If F is empty, set R=infinity and R^(-p)=0. At p=gamma the tail estimate alone cannot ensure finiteness: the comparison distribution P(R<=delta)=delta^gamma on (0,1) gives an integrand proportional to delta^-1 and a divergent inverse moment. This is a sharp moment threshold for the stated conditional bound, not an ARW or coloring assertion.

Checks: check_extended.py checks finite net covers and the set-distance implication on exact rational grids, and the boundary exponent in the inverse-moment integral. Failure modes: a random seed chosen after observing F; net centers outside the domain of the uniform estimate; F not closed; alpha<=d_0; transferring a pointwise zero-probability statement to an uncountable seed. Auditor w346, pending.
