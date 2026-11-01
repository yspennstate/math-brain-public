# P0003 adversary packet: a pinching-loop obstruction

The assigned question is Grimmett, arXiv:2205.07318, Question 2.2, PDF p.3: suitably rescaled uniform n-step honeycomb walks from the origin are conjectured to converge weakly to SLE(8/3). The source leaves the scale, topology, parametrization and SLE geometry/stopping convention unspecified. The critical chordal measure in BDGS, arXiv:1206.2092, Conjecture 1.5 and section 3.3, is a related variable-length, fixed-endpoint ensemble. This packet proves no equivalence between them. Current openness remains UNKNOWN; no novelty or target-proof claim is made.

The independent contribution is the exact honeycomb counterexample in INDEPENDENT.md. That note was saved before w402's ATTEMPT.md was read. Its seven-track construction has 22N-12 edges, distinct fixed endpoints, speed <=28, and uniform error <=5/N. Yet its limiting trace contains a macroscopic closed rectangle. Uniform convergence is stronger than convergence modulo increasing reparametrization, so weakening the topology does not repair the inference that the limiting trace must be an arc.

## All-N estimate, separate from the finite checks

On each horizontal track, the x-coordinate progresses linearly in the edge index. Its difference from the limiting anchor interpolation is <=2sqrt(3)/N, while the y-coordinate oscillates by <=1/(2N). On a vertical strip containing k vertical steps and k-1 horizontal steps, put m=2k-1 and let l be the elapsed edge count. The distance progressed vertically is

    [3l/4 + ((l mod 2)/4)] / N.

For the upward strip, k=2N and the target progress is 3l/m. Their difference in units of 1/N is -3l/(4m) + (l mod 2)/4, with absolute value <=3/4. For the downward strips the initial offset is -1/(2N); the corresponding difference is -1/2 + 3l/(4m) - (l mod 2)/4, again of absolute value <=3/4. The columns remain within 2sqrt(3)/N of their limiting vertical line. Hence the Euclidean error is <=sqrt(12+9/16)/N <4/N <5/N on vertical tracks. Between checked lattice vertices the difference of the two parametrized paths is affine, and a norm of an affine function attains its maximum at an interval endpoint. This proves the all-N uniform bound. It uses no SAW probability estimate.

The two neck anchors, at times 1/7 and 5/7, have squared distance 37/N^2. Their intervening excursion has diameter tending to 2sqrt(3), and its image converges to the entire boundary of [0,sqrt(3)] x [0,3]. A simple arc cannot contain a circle: composing an arc's inverse with such a circle would give an injective continuous image of a circle in the real line, which is impossible (remove an interior point of its interval image; a circle with one point removed is connected). The example therefore obstructs simplicity of the trace, not merely injectivity of a chosen parametrization.

## An exact additional criterion

Let P_n converge weakly to P on C([0,1],C), with its uniform metric. For r>=0 and q>0 define E(r,q) as the curves gamma for which some s<t satisfy

    |gamma(s)-gamma(t)| <= r and diam(gamma([s,t])) >= q.

Then P is supported on curves having no nonconstant self-return if and only if, for every q>0,

    lim_{r downarrow 0} limsup_{n to infinity} P_n(E(r,q)) = 0.

This statement permits constant waiting intervals. It does not assert avoidance of the outer domain boundary, Loewner driving convergence, conformal invariance or SLE identification.

Proof. E(r,q) is closed in the uniform metric. Given uniformly convergent curves and witnesses s_n,t_n, take a subsequence of witnesses in the compact triangle 0<=s<=t<=1. Uniform continuity of the limiting curve makes the endpoint distances and subcurve diameters continuous in the curve and the two times. The limiting excursion diameter >=q forces s<t. The nested intersection of E(r,q) as r decreases to zero is E(0,q), by the same witness-compactness argument. If P has no nonconstant self-return then P(E(0,q))=0. Continuity of probability from above and the closed-set inequality for weak convergence give

    lim_{r downarrow 0} limsup_n P_n(E(r,q))
        <= lim_{r downarrow 0} P(E(r,q)) = 0.

Conversely let U(r,q) use the strict inequalities distance <r and excursion diameter >q. For fixed witnessing s,t these strict inequalities persist in a uniform neighborhood, so U(r,q) is open. A curve with a zero-distance return and excursion diameter >2q belongs to U(r,q) for every r>0. The open-set inequality gives

    P(E(0,2q)) <= P(U(r,q)) <= liminf_n P_n(U(r,q))
        <= limsup_n P_n(E(r,q)).

Let r decrease to zero and then use q=1/k, k=1,2,... . Every nonconstant self-return has positive excursion diameter, so it lies in some E(0,2/k). Their countable union has probability zero. This proves the criterion. No independence or multiplication of conditional probabilities is used.

For the deterministic laws on the explicit honeycomb paths, E(r,1) has probability 1 for every sufficiently large N for every fixed r>0. Thus the additional criterion fails as strongly as possible while the laws converge uniformly and their speeds are bounded. This remains a counterexample to a stronger auxiliary bridge only. Each path can occur in a finite honeycomb SAW support, but no lower bound on its probability under uniform or critical Boltzmann sampling is proved.

## Paired prover audit

After the independent note was saved, I read w402's STATEMENT_FOR_ADVERSARY.md and ATTEMPT.md. His lane concerns midpoint fields satisfying the local observable relation; my lane concerns trace topology. The constructions are disjoint. His load-bearing six-edge perturbation is independently rederived in PEER_AUDIT.md, with an exact bounded check in check_peer_mode.py. No review of w404's review was used.

## The open piece

In this lane the unresolved piece is a mesh-uniform bound making macroscopic near-returns improbable for the actual SAW ensemble, with justified parametrization and conditioning. Tightness or exact finite-graph domain Markov identities alone do not supply it. Neither this criterion nor the peer's boundary-kernel calculation proves that bound. Observable convergence, outer-boundary avoidance and SLE identification remain additional gaps in a full chordal route; transfer back to the assigned fixed-length ensemble also remains open in this packet.

All new mathematical statements have an author proof and reproducibility evidence; w404's independent check is requested and is required before theorem promotion. The bounded check is not a formal theorem-prover receipt.

NEXT: Referee w404 checks the all-N honeycomb construction and the weak-convergence criterion; coordinator may land only clearly labeled draft concepts before that check.
