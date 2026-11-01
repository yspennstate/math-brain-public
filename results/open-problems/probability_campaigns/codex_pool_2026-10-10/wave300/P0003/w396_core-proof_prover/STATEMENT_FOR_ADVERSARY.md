# P0003 statement packet for w397

2026-10-10. Sent before the proof packet. Draft; no success or novelty claim.

Target formulation recovered from Duminil-Copin--Smirnov, arXiv:1007.0575v2, Theorem 1 and Section 4, together with Lawler--Schramm--Werner, arXiv:math/0204277v2, Sections 3.4 and 4.1. The latter formulates the general planar conjecture on the square lattice; applying its chordal ensemble to the honeycomb lattice is the explicit P0003 specialization, not a quotation of a honeycomb convergence theorem.

Let D be a bounded simply connected Jordan domain, analytic near distinct marked boundary points a,b. Let D_delta be compatible finite induced honeycomb approximations of mesh delta, with boundary mid-edges a_delta,b_delta tending to a,b and with the interior of a walk contained in D_delta. Give every self-avoiding mid-edge walk gamma from a_delta to b_delta weight x_c^{ell(gamma)}, where ell is the number of honeycomb vertices visited and x_c=(2+sqrt(2))^{-1/2}. Normalize by the finite, positive total weight Z_delta(D;a,b). The target is weak convergence as delta decreases to zero to chordal SLE(8/3) from a to b in D, in the uniform metric modulo increasing reparametrization. Natural-length parametrization, fixed-length walks, and Hausdorff convergence alone are distinct assertions.

Hardest missing input in this lane (H_5/8): for a compact boundary-attached obstacle A away from a,b, with D\A simply connected and agreeing with D near a,b, prove

    Z_delta(D\A;a,b) / Z_delta(D;a,b)
        -> ( |f_A'(a)| |f_A'(b)| )^{5/8},

where f_A:D\A -> D fixes a,b. Compatible graph deletion, rather than a separately translated lattice, defines the numerator. The derivative product is independent of the remaining endpoint-fixing conformal automorphism. Need this for a determining class of obstacles and for shrinking smooth collars. This remains conjectural. Curve tightness, interior simplicity of subsequential limits, and any needed event stability are also unproved prerequisites for the full target.

Proposed finite lemma for independent attack: take any finite graph G with positive, inherited edge weights, endpoints a!=b, Z_G(a,b)>0, and the probability proportional to the product of edge weights on simple a-to-b paths. Let F_k reveal the stopped prefix, retaining the completed path after reaching b. For forbidden vertex sets A subset B disjoint from a,b, define M_k^A=P(path avoids A | F_k). For an uncompleted prefix eta avoiding A, this equals Z_{G_eta\A}(tip,b)/Z_{G_eta}(tip,b), where G_eta deletes all earlier visited vertices and retains the tip. It is zero if the prefix already hit A and is the avoidance indicator at completion. Proposed inequality, for every lambda>0:

    P( max_k (M_k^A-M_k^B) >= lambda )
        <= ( Z_{G\A}(a,b)/Z_G(a,b)
             - Z_{G\B}(a,b)/Z_G(a,b) ) / lambda.

The bound is intended to be independent of graph size and path length. It must include completed paths, impossible residual states, and arbitrarily chosen stopping times without assuming independence. Check whether this transfers static collar-ratio estimates to uniform control during exploration, and locate the exact point where it still fails to prove H_5/8.

Sources: https://arxiv.org/abs/1007.0575 ; https://arxiv.org/abs/math/0204277 ; restriction identification: https://arxiv.org/abs/math/0209343 .
