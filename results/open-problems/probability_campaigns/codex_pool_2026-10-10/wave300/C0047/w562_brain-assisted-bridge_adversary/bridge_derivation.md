# A bounded-congestion coupling, with its exact limit

Author: w562, 2026-10-10. Independent derivation follows independent_obstruction.md. Status: complete written candidate proof, independent referee w563 required. No originality or parent-conjecture solution claim.

Let G and H be countable connected locally finite simple undirected graphs with the same vertex set. To each edge h={x,y} of H assign a finite simple G-path P_h joining x to y. Assume |P_h|<=L for every h, for an integer L>=1, and that every G-edge belongs to at most M of these paths, for an integer M>=1. These are route length and route congestion hypotheses, not consequences of nonamenability.

For the threshold corollary use p_c(K)=sup{r in [0,1]: at parameter r there is almost surely no infinite open component}, the original Benjamini-Schramm convention. On a finite common vertex set both thresholds are 1 and the bound is trivial. On the infinite connected graphs relevant to C0047 this is the usual critical threshold. The coupling itself applies in either case.

For any p in [0,1], set t=1-(1-p)^(1/M) and q=t^L. There is a coupling of iid Bernoulli(q) bond percolation eta on H and iid Bernoulli(p) bond percolation omega on G such that whenever eta(h)=1, every G-edge of P_h is omega-open.

Proof. For each G-edge e allocate M independent Bernoulli(t) variables X(e,1),...,X(e,M), independently over all e. Assign the routes through e different slots. Set omega(e)=max_j X(e,j); then the omega(e) are independent and P(omega(e)=1)=1-(1-t)^M=p. For a route h use its assigned slot at every edge to form A_h=product_{e in P_h}X(e,slot(h,e)). Because routes use distinct variables even when they share a G-edge, the A_h are independent and P(A_h=1)=t^|P_h|. Independently choose B_h~Bernoulli(t^(L-|P_h|)), with t^0 defined as 1, including at t=0. Set eta(h)=A_h B_h. The eta(h) are iid with parameter q and eta(h)=1 implies every edge of P_h is omega-open. The countable product probability space constructs all variables simultaneously; no multiplication of conditional row bounds is involved.

The component of any vertex in eta is contained as a vertex set in its omega-component. Thus if iid H-percolation occurs at q, then iid G-percolation occurs at p. Taking q down to p_c^bond(H), using the continuous increasing inverse, gives

p_c^bond(G) <= 1-(1-(p_c^bond(H))^(1/L))^M.

The cases p_c(H)=0 or 1 follow by the same limiting argument or the trivial p_c(G)<=1 bound. This concerns only existence. Distinct eta-clusters may be joined by extra omega-open edges, so this coupling proves no lower bound on p_u(G) and transfers no nonuniqueness interval. A complete C0047 bridge would need to prohibit those mergers at some p>p_c(G). That is the single hardest unproved piece in this route.

For a comparison at p=1/2 with L=M=2, q=(1-1/sqrt(2))^2, about 0.085786, rather than p^2=0.25. The independent path law can be bought with a parameter penalty; its construction does not solve the merger problem.

NEXT: Referee-check the slot allocation/product-space construction and ask whether an additional cluster-separation premise can hold for the same fixed generating set.
