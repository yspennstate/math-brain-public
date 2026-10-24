# Author proofs: directed-reduction obstruction

These are proved special cases by w375, pending independent review by w377. No novelty claim and no proof of P0110.

## L1. A positive-probability axial detour

On Z^d, d>=2, let the undirected nearest-neighbor edge weights be iid and nonnegative. Suppose disjoint intervals I_low and I_high have probabilities p_low,p_high>0, and t<=a on I_low, t>=b on I_high, where 0<=a<b<infinity. Choose an integer k>=1 with Delta=k*b-(k+2)*a>0.

For endpoints 0 and k*e1, the only coordinate-monotone path is the axial path A with k edges. Let B go once in the +e2 direction, k times in +e1, and once in -e2. Its k+2 edges are distinct from all edges of A. On the event A's weights lie in I_high and B's lie in I_low, t(A)>=k*b, t(B)<=(k+2)*a and T(0,k*e1)<=t(B)<t(A). The event has probability p_high^k*p_low^(k+2), by iid independence of these explicitly disjoint edges. This product does not condition on geodesic selection. Thus an exact same-environment reduction to coordinate-monotone minimum passage time fails for every law satisfying the two-support-interval hypothesis.

## L2. A linear axial separation from the directed model

Assume in addition 0<r<=t_e<=R<infinity almost surely and the law is nondegenerate. Let mu=E t_e. Choose I_low,I_high,a,b,k as in L1; nondegeneracy supplies two separated support neighborhoods. Define delta=E[(S_k-H_k)_+], where S_k is the cost of A and H_k the cost of B, on independent disjoint edges as above. Then delta>=Delta*p_high^k*p_low^(k+2)>0.

Divide the axis into blocks of length k+1. In block j, use the cheaper of the axial k-edge path from j*(k+1)*e1 to (j*(k+1)+k)*e1 and its height-one detour, and then use the next axial edge as a connector. Write S_j,H_j,C_j for those costs and the connector. Every block uses distinct edges: a one-edge connector separates successive detour endpoint columns. Consequently the block costs Y_j=min(S_j,H_j)+C_j are iid and bounded, with E Y_j=(k+1)*mu-delta. Concatenating the chosen paths gives a self-avoiding path (their vertex sets meet only at adjacent connector endpoints). Hence T(0,m*(k+1)*e1)<=sum_{j=0}^{m-1}Y_j.

The strong law gives limsup T(0,m*(k+1)*e1)/(m*(k+1))<=mu-delta/(k+1) almost surely. For any n=m*(k+1)+q, 0<=q<=k, append the q axial edges. Their cost is at most k*R, so the same upper bound holds for limsup T(0,n*e1)/n. The same construction yields E T(0,n*e1)<=n*mu-m*delta. Thus, if g(e1) denotes the usual FPP time constant, g(e1)<=mu-delta/(k+1)<mu; the proof of the displayed limsup bound does not assume its existence.

The directed axial passage time is the sum of the n axial weights, whose ratio to n tends to mu almost surely. Therefore liminf [T_directed(0,n*e1)-T(0,n*e1)]/n>=delta/(k+1)>0 almost surely. This rules out even an o(n) raw same-environment approximation to that directed axial model. An appropriately centered comparison with another model, or equality of fluctuation universality classes, remains open.

Coupling clarification, prompted by w376's C008: a different raw coupling alone cannot remove the separation. Let c0=delta/(k+1), choose any 0<c<c0, and eta=(c0-c)/2. For any coupling at each n of the directed and unrestricted passage-time marginals, a union bound gives P((T_dir-T)/n>=c)>=1-P(T_dir/n<mu-eta)-P(T/n>mu-c0+eta), which tends to one by the two marginal limits above. No independence between the coupled passage times is needed. This is still a statement about uncentered costs, not centered fluctuation exponents.

## Single hardest gap for P0110

The full-plane model has no proved matching upper/lower exponent pair for an explicit admissible continuous iid law in this packet. L1 and L2 remove a shortcut; they provide no polynomial fluctuation or wandering estimate. Transferring a solvable directed or fixed-width model would require a quantitatively controlled error on the fluctuation scale and a compatible geodesic-deviation comparison as the width tends to infinity. Those estimates are unproved here.

## L3. A detour obstruction in a diagonal direction

Let d>=2 and suppose the iid nonnegative law has positive masses p_low,p_high on disjoint sets I_low subset [ell,a] and I_high subset [b,infinity), where 0<=ell<=a<b. Choose k>=1 satisfying k*(b+ell-2*a)>2*a. For endpoints (0,0) and (k,k) in the e1,e2 plane, put every horizontal edge of [0,k]^2 in I_high, and every vertical edge of that square with x<k in I_high. Put the k vertical edges on x=k in I_low. Finally put the k horizontal edges at y=-1, plus the vertical edges from (0,0) to (0,-1) and from (k,-1) to (k,0), in I_low.

These assignments involve exactly 2*k^2+k high edges and 2*k+2 low edges, all distinct. The event has probability p_high^(2*k^2+k)*p_low^(2*k+2)>0. Every coordinate-monotone path has k horizontal and k vertical edges within [0,k]^2, so its cost is at least k*b+k*ell. The detour via y=-1 and then up the right column has length 2*k+2 and cost at most (2*k+2)*a. The assumed inequality makes the detour strictly cheaper. A coordinate-monotone path in d>2 cannot use the other coordinates, so the same proof applies there.

This is a finite event, not an asymptotic diagonal time-constant separation. In particular a rare fixed-box event by itself supplies no exponent bound.

## L4. Sharp finite axial threshold for bounded disorder

Let iid weights have essential infimum r and essential supremum R, with 0<r<R<infinity. For each integer n>=1, let T_dir(0,n*e1) be the cost of the unique coordinate-monotone axial path.

If n*(R-r)<=2*r, then T(0,n*e1)=T_dir(0,n*e1) almost surely. Indeed, outside a null event all edges have weights in [r,R]. The axial cost is at most n*R. Every other path has at least n+2 edges: the lattice length has parity n, and length n forces n steps in +e1. Thus every other path costs at least (n+2)*r>=n*R. If the inequality is strict, every minimum path is axial.

Conversely, if n*(R-r)>2*r, put M=n*(R-r)-2*r and eta=M/(4*n+4)>0. Since eta<(R-r)/4, the intervals I_low=[r,r+eta] and I_high=[R-eta,R] are separated and have positive probability by the definitions of essential infimum and supremum. Put a=r+eta and b=R-eta. Then n*b-(n+2)*a=M-(2*n+2)*eta=M/2>0. L1 gives P(T(0,n*e1)<T_dir(0,n*e1))>=p_high^n*p_low^(n+2)>0.

Thus the zero-probability versus positive-probability boundary is exact: strict directed/unrestricted inequality is possible precisely when n*(R-r)>2*r. For Uniform[1,1+epsilon], equality is guaranteed at n*epsilon<=2; once n*epsilon>2, a strictly cheaper non-directed path occurs with positive probability. This does not calculate that probability exactly or establish any asymptotic fluctuation exponent.
