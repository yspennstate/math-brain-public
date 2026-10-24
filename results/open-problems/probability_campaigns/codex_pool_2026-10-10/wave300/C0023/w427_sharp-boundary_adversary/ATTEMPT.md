# C0023: the exhaustion bridge and its exact missing premise

The dated intake asks for theta(p_c)=0 for Bernoulli percolation on Z^d, d>=3, and labels d=3,...,10 unresolved as of 7 September 2026. The concrete model analyzed here is independent nearest-neighbor bond percolation, with theta_G(p)=P_p(|C_G(o)|=infinity) and p_c(G)=inf{p in [0,1]:theta_G(p)>0}. A 24 September public preprint now claims the bond result for every infinite connected locally finite quasi-transitive graph with p_c<1. Current openness is UNKNOWN in this packet; the recent proof has not been checked. Neither novelty nor a solution of C0023 is claimed.

The independent strip derivation was saved in INDEPENDENT.md before any paired proof was read. The following results identify a boundary condition required by an unrestricted approximation argument.

## Exact transfer criterion

Let G be an infinite connected locally finite graph, o a vertex, and G_n increasing subgraphs containing o whose vertices and edges exhaust G. Restrict one common independent Bernoulli(p) configuration to each G_n; p is fixed. For integer R>=1 set

    a_n(R) = P_p(o connects in G_n to some x with dist_G(o,x)>=R).

Then

    theta_G(p) = inf_R sup_n a_n(R),
    theta_G_n(p) = inf_R a_n(R).

In particular, theta_G(p)=0 if and only if for every epsilon>0 there is an R such that a_n(R)<=epsilon for every n.

Proof. Every connection to ambient distance at least R has a finite path witness, so its event in G is the increasing union of its events in G_n. Continuity from below gives probability sup_n a_n(R). As R increases these full-graph events decrease. Because G is locally finite, its finite-radius balls are finite, and their intersection is exactly the event of an infinite origin cluster. Continuity from above gives the first identity. The same finite-ball argument gives the second identity even when a subgraph is finite or disconnected. The epsilon criterion is precisely the first identity. No independence across n or R is used.

The invalid interchange is sup_n inf_R a_n(R)=inf_R sup_n a_n(R). The always-valid inequality has <= in this direction. Nonpercolation in each G_n establishes only that the left-hand side is zero.

A usable diagonal variant is: choose R_j tending to infinity and n_j large enough to contain all vertices and edges of the ambient ball B_G(o,R_j). If a_n_j(R_j) tends to zero, then theta_G(p)=0. Any full-graph path reaching distance R_j has a first-hit prefix entirely in that ball, so this event is already present in G_n_j. Merely making R large for each fixed thin subgraph does not satisfy this condition.

## A genuine Bernoulli counterexample to unrestricted transfer

Take G=Z^2 and G_k=Z x {-k,...,k}. They are increasing infinite connected locally finite quasi-transitive nearest-neighbor graphs, and their union is G. At p=99/100 every G_k has no infinite cluster by the cut proof in INDEPENDENT.md. Nevertheless G percolates at this same p.

Here is a self-contained elementary lower bound. If the open origin cluster in Z^2 is finite, its exterior bond boundary contains a simple dual-lattice circuit surrounding the origin; every crossed primal bond is closed. One way to see this is to trace the boundary of the union of the unit squares centered at cluster vertices, resolving repeated dual vertices along the exterior boundary. Its enclosing simple circuit separates the origin from infinity. Such a circuit has length m>=4.

An enclosing circuit must cross the positive horizontal ray through the origin. A crossing dual edge has x=j+1/2 for integer j>=0. Since an enclosing circuit also reaches negative x, a circuit of length m has j<m. There are at most m eligible crossing edges, two possible orientations of a chosen first edge, and at most 3 choices per further nonbacktracking step. The looser count N_m<=4m*3^(m-1) is therefore valid. A fixed simple circuit uses m distinct primal bonds, so independence gives probability (1-p)^m that they are all closed. The union bound yields, with a=3(1-p)<1,

    P_p(|C(0)|<infinity) <= (4/3) sum_{m>=4} m*a^m
                           = (4/3)*a^4*(4-3a)/(1-a)^2.

At p=99/100 the right side is 10557/2352250000 < 1/100000. Thus theta_Z2(99/100)>0.99999. This bound is deliberately loose; no sharp planar threshold theorem is needed.

Consequently, for this example,

    sup_k inf_R a_k(R) = 0,
    inf_R sup_k a_k(R) > 0.99999.

This is a counterexample to the unrestricted exhaustion bridge, not to critical nonpercolation on Z^3,...,Z^10. It also does not refute a bridge that additionally assumes convergence of critical thresholds: p_c(G_k)=1 here. Any more specialized bridge must be audited under its actual hypotheses.

## Prior attempt and hardest remaining piece

C0023-A001 (intake attempts.jsonl, line 22) already notices that removing hyperplane-crossing edges can split a unique full-space cluster into infinitely many finite half-space clusters. Its proposed route leaves half-space susceptibility and a gluing statement unproved. The present exhaustion criterion supplies no such gluing statement. The hardest remaining piece for a slab/exhaustion proof is a full ambient-ball connection estimate, uniform over width at p_c(Z^d), or another argument excluding an infinite full-space cluster despite finite restricted pieces. Critical nonpercolation for each slab at its own threshold alone does not supply that estimate.

For q_k=(1-p)^(2k+1), the independent strip bound 2(1-q_k)^R deteriorates with width. An attempted choice R=R(k) must also verify that its restricted graph contains the full ambient ball whose event it claims to control.

Independent reviewer: w428. Review is pending unless the separate review receipt says otherwise. The packet distinguishes elementary proof, bounded computational checks, public source claims, and actual independent review.

NEXT: Audit the paired prover's precise bridge under its own assumptions and save a verdict; otherwise hand off this proved boundary packet for independent checking.
