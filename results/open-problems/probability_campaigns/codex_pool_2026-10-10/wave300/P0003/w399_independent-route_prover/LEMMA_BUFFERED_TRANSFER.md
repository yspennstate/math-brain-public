# Buffered avoidance transfer (independently checked background)

w401 returned KEEP at the compact-set and buffer-limit hypotheses below. This remains background here: w405 owns the distinct fleet buffer-transfer lane, and this lemma is not in w399's submitted main bundle.

Let X be a compact metric space, and let K_m,K be random nonempty compact subsets of X with K_m => K in the Hausdorff metric. Fix a nonempty closed obstacle A. Write A^r={z in X: dist(z,A)<=r}, p_m(r)=P(K_m intersects A^r in the empty set). Suppose p_m(0)->q, and there are r_j>0 decreasing to zero with p_m(r_j)->q_j for each j and q_j->q. Then P(K avoids A)=q. No no-touching assumption is required.

Proof. F(L)=dist(L,A) is continuous (indeed 1-Lipschitz) in the Hausdorff metric. The open-set part of Portmanteau gives P(F(K)>0)<=liminf_m P(F(K_m)>0)=q. For every j, the closed-set part gives

q_j=lim_m P(F(K_m)>r_j)<=limsup_m P(F(K_m)>=r_j)<=P(F(K)>=r_j)<=P(F(K)>0).

Let j increase to obtain the opposite inequality. Compactness identifies positive distance with disjointness. This proves the claim.

SAW use. Apply this to the finite set of visited lattice vertices, whose Hausdorff distance from its piecewise-linear trace is at most half a lattice edge. Vertex avoidance of A^r is exactly the finite partition quotient obtained by deleting vertices in A^r. Thus a buffer-stable family of quotient asymptotics transfers to continuum trace avoidance. It does not prove the needed asymptotics.

The proof uses only continuity of distance and Portmanteau; no formal checker was run and no novelty is claimed.
