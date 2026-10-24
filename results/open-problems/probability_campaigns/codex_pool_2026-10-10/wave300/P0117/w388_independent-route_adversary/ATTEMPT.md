# P0117 independent derivation and obstruction

No complete solution is claimed. Independent reviewer: w389; review pending. The original route was locked in INDEPENDENT_LOCK.md before reading any paired proof.

## Exact target and distinction

On the undirected nearest-neighbor graph Z^2 put finite nonnegative iid edge weights with an atomless common law. A bigeodesic is an injective path (v_k) indexed by Z such that each segment v_i,...,v_j achieves the infimum of passage times over all finite paths between its endpoints. The target is that almost surely no such path exists anywhere. Damron--Hanson, arXiv:1512.00804v2, Conjecture 1 states this without a moment hypothesis. For importing the geodesic-density theorem below, additionally assume E[min(t_1,t_2,t_3,t_4)^2]<infinity for four independent incident-edge weights. Their directional Theorem 1.1 instead assumes E[t_e]<infinity and differentiability of the entire limit-shape boundary; its direction is fixed before sampling the environment.

The bare ranking title omits continuity: constant unit weights are an iid counterexample to that broader reading (C01). This does not refute the intended continuous-law target.

## Root-crossing compactness certificate (C02)

This is a deterministic elementary reduction, not a solution or a novelty claim. Let B_n={x in Z^2: ||x||_infinity<=n}, and let S_n be its vertex boundary, of size 8n for n>=1. For any fixed finite nonnegative edge-weight environment, define E_n as existence of a finite simple global geodesic with endpoints in S_n, passing through 0, and with all other vertices in B_(n-1). A geodesic means optimal in the WHOLE graph, not merely in B_n.

1. E_(n+1) implies E_n. On each side of 0 in a witness path, stop at its first encounter with S_n. These stopped pieces have all earlier vertices in B_(n-1). Their concatenation is simple. Any subsegment of a global geodesic is globally minimizing: replacing it by a cheaper path and deleting loops of nonnegative cost would contradict global minimality.
2. A bigeodesic through 0 implies every E_n, by the same first-boundary operation. Each infinite simple half leaves every finite box.
3. If all E_n occur, choose a witness for each n, orient it arbitrarily, and index its vertex 0 by 0. Each arm has at least n edges. At any fixed graph-length m there are finitely many possible central vertex strings indexed -m,...,m, because the lattice degree is finite. Repeated infinite pigeonhole selection over m yields consistent central strings and hence a doubly infinite path. Every finite central string is a segment of some chosen simple global geodesic, so the resulting path is injective and all its finite segments minimize globally. No convergence of passage times or selection of a direction is used.
4. E_n is measurable: there are finitely many eligible simple paths inside B_n, and global minimality of each is a countable intersection of comparisons with finite lattice paths. Thus P(bigeodesic through 0)=lim_n P(E_n) by continuity from above. Under translation invariance, absence everywhere is equivalent to this limit being zero, by the countable union over lattice vertices.

Prior local work already identified an anchoring obstruction in compactness arguments. This certificate makes that issue explicit; it is reused as a check, not presented as an independent new solution method.

## Independent route withdrawn: all-ray shell incidence (C03, referee correction)

For a vertex x, write T_x for the union of all infinite simple geodesic rays starting at x. Under translation invariance define q(z)=P(z in T_0). Ahlberg--Hanson--Hoffman, arXiv:2208.11576, Theorem 1.1, under its iid assumptions A1 from Section 2.4, gives sup_(||z||_infinity>=n) q(z)->0. A1 is iid, continuous common law and E[min(t_1,t_2,t_3,t_4)^2]<infinity. No assumption on limit-shape differentiability is required for that result.

Let H be the event of a bigeodesic through 0. On H, its two arms first hit S_n at two distinct vertices x and y. Starting at either of these vertices and following the bigeodesic through 0 toward the opposite end gives an infinite geodesic ray. Hence

    2*1_H <= sum_(x in S_n) 1_{0 in T_x}.

Taking expectations and translating gives the elementary shell-incidence bound

    P(H) <= (1/2) sum_(x in S_n) q(-x)
         <= 4n * sup_(x in S_n) q(x).

The inequality is valid, but the proposed vanishing shell premise is IMPOSSIBLE in this class. Referee w389 identified this on 2026-10-10: there is almost surely at least one infinite ray from 0, and every such ray hits S_n. Thus

    sum_(x in S_n) q(x) = E[|T_0 intersect S_n|] >= 1,
    sup_(x in S_n) q(x) >= 1/(8n).

Therefore neither vanishing all-ray shell sum nor the proposed o(1/n) rate can be a viable sufficient input here. As a formal implication the sufficiency calculation is true, but its premise contradicts the existence of rays. The original statement that the missing rate was an open piece of this route is withdrawn. This is a stronger obstruction than the marginal-union example: the target statistic has a deterministic floor even in an environment with no bigeodesics.

The existence assertion follows by taking simple geodesics from 0 to ne1 and extracting consistent finite prefixes using finite degree. Every resulting finite prefix globally minimizes, giving an infinite simple ray. It leaves every finite box and hence intersects every S_n. The shell floor needs no independence, shape curvature, or translation invariance. Attribution: this correction was originated by w389; its required independent referee is w392. It remains a concept/draft in the bundle until that check.

The nonvacuous target is the joint two-ended/root-crossing event E_n. One-sided ray reachability cannot supply its decay just by tightening a rate which has the floor above. We have no new bound on P(E_n).

This method uses the entire union of infinite rays and a shell counting identity. It does not assume every ray belongs to a selected Busemann graph, does not approximate a random direction by a rational one, and makes no independence claim about ray events.

## Endpoint union obstruction (C04)

There are binomial(8n,2)=32n^2-4n unordered distinct boundary endpoint pairs. If p_n is the maximum probability that a globally minimizing finite path through 0 exists for a prescribed pair, then P(E_n)<=(32n^2-4n)*p_n. Thus p_n=o(n^-2) suffices; p_n->0 alone supplies no conclusion from this union bound. If finite geodesics are unique, the pair event is precisely 0 in Geo(u,v), with the qualification that E_n additionally requires the stopped path to stay inside B_n.

For a concrete counterexample to the logical inference, let U be uniform on [0,1) and A_(n,j)={floor(n^2 U)=j}, 0<=j<n^2. Each probability is 1/n^2 and the union is the entire sample space, at every n. Thus even nested scale events E_n=union_j A_(n,j) can have probability 1 while all prescribed-witness probabilities vanish uniformly. This abstract witness example is not a counterexample to continuous iid FPP.

## Deterministic localization for a bounded positive law (C05)

Assume 0<a<=t_e<=b<infinity for every edge. For u,v in B_n, a coordinate path inside B_n costs at most 4bn. Any competing path with cost at most 4bn has at most floor(4bn/a) edges and therefore lies in B_R, R=n+ceil(4bn/a). Thus the global distance between every such pair equals the distance computed in B_R. E_n is then measurable using only edges in that deterministic enlarged box. This makes finite diagnostics honest but does not allow a simulation to prove P(E_n)->0.

NEXT: Have w392 check w389's all-ray shell-floor correction, and audit a genuinely two-ended root-crossing comparison rather than pursuing the impossible all-ray rate.
