# Independent obstruction, saved before reading w438

Target: iid Bernoulli bond percolation on an infinite connected locally finite quasi-transitive graph G with p_c(G)<1. Establish that there are almost surely no infinite clusters at p_c. The source recovered so far is Hutchcroft, arXiv:1605.05301, Introduction (Benjamini--Schramm conjecture). Current full openness remains UNKNOWN pending dated source and local-retirement checks.

## Uniform subdivision family

Let T_L be obtained from the infinite 3-regular tree by replacing every edge with a path of exactly L edges, where L is any positive integer. Choose a root o that was a vertex of the original tree. The graph is an infinite connected locally finite tree of maximum degree 3. Its automorphism group has finitely many vertex orbits: the original vertices form one orbit, and interior vertices have at most L-1 additional types, determined by their position within a subdivided edge. Thus it is quasi-transitive. For L>1 it is not vertex-transitive.

At bond retention p, call an original edge usable if all L of its constituent edges are open. Usable original edges are independent Bernoulli bonds of retention r=p^L, since the corresponding finite edge sets are disjoint. There is an infinite open cluster in T_L if and only if there is an infinite usable-edge cluster in the original tree. The forward offspring law is Bin(2,r). Its generating function is f(s)=(1-r+rs)^2. The extinction probability is the smallest fixed point of f on [0,1], obtained by iterating f from 0. If r<=1/2, the only fixed point in [0,1] is 1. If 1/2<r<1, the second fixed point ((1-r)/r)^2 lies below 1; at r=1 extinction is 0. Consequently p_c(T_L)=2^(-1/L)<1, and critical percolation has no infinite clusters. An infinite open path cannot stay indefinitely inside the finitely long subdivided edges, so passing to usable original edges loses no infinite cluster.

For 1<=n<=L, the sphere of graph-distance n from o consists of the three vertices n edges along its three original incident edges. The three paths are disjoint in edges. Therefore

    a_L(n) := P_{p_c(T_L)}(o connects to distance n)
            = 1 - (1 - 2^(-n/L))^3.

In particular a_L(L)=7/8 for every L. For every fixed integer n>=1, letting L tend to infinity with L>=n gives a_L(n)->1. Hence

    sup_{G,o} P_{p_c(G)}(o connects to distance n) = 1

for every n>=1, where the supremum ranges over infinite connected locally finite quasi-transitive graphs of maximum degree at most 3 with p_c(G)<1 and arbitrary roots. There is no graph-independent function f(n)->0 controlling all these probabilities. Any proposed C/n bound with C depending only on maximum degree is false: choosing L>(8/7)C and n=L contradicts it.

This invalidates a uniform-over-graphs bridge, not critical extinction on any fixed graph. It also does not invalidate a bridge restricted to vertex-transitive graphs, or one whose constants depend on the graph. In this family p_c tends to 1, the number of vertex orbits grows, and the growth rate is 2^(1/L), tending to 1; any successful uniform estimate must use assumptions that exclude or quantitatively control this degeneration. No sufficiency claim is made for any one such extra assumption.

## Fixed-graph critical behavior: exact recurrence

Let u_0=1 and u_{k+1}=1-(1-u_k/2)^2=u_k-u_k^2/4. This is the probability of reaching generation k in the critical forward binary tree. For k>=1 the root with three forward branches has

    a_L(kL)=1-(1-u_{k-1}/2)^3.

Since u_{k+1}<u_k for u_k>0 and a limit u satisfies u=u-u^2/4, u_k tends to zero. Moreover

    1/u_{k+1} - 1/u_k = 1/[4(1-u_k/4)] -> 1/4.

Summing and applying the elementary Cesaro limit yields k u_k->4. It follows that k a_L(kL)->6, equivalently (kL) a_L(kL)->6L. Thus critical one-arm probabilities have inverse-distance decay along these radii; they do not have an exponential upper bound even for any fixed T_L. This constant is derived independently, with the root's three branches retained explicitly.

At radius kL there are 3*2^(k-1) original vertices, each connected to o with probability (1/2)^k. Their expected number connected to o is exactly 3/2 for every k>=1. Summing over k gives infinite critical susceptibility, despite almost-surely finite critical clusters. On T_1, for p<1/2, chi(p)=1+3p/(1-2p); it diverges as p increases to p_c. Finite subcritical susceptibility therefore cannot be transferred to the endpoint by an unproved uniform-in-p bound or by exchanging limits.

## What remains hard

These trees already lie in the exponential-growth class handled by Hutchcroft's theorem; the purpose here is a precise obstruction to stronger bridges, with no novelty claim. The hard unsolved step of the full target is not established: a method must control critical infinite clusters on the remaining quasi-transitive, subexponential-growth graphs with p_c<1, including low-dimensional lattice instances unless newer results resolve them. Current openness is recorded separately; this packet is not a solution of P0043.

Independent reviewer: w440, pending. No paired proof was read before saving this file. Numerical checks will validate finite recurrences only; the limit and extinction arguments above are mathematical proofs, pending independent review.

## Final audit and measurement

The independent analysis preceded reading w438. AUDIT_W438.md gives KEEP on the stated reciprocal identity and tree threshold/local-limit claims, without extending them to general graphs. The old C0084 attempt misdescribes Hutchcroft's method; SOURCE_STATUS.json and claim 004 record the narrow source correction. The original P0043 intake points to Lyons--Peres Conjecture 8.15, printed page 285, but that exact book version was not fetched. The target's full quantifiers are verified independently in Hutchcroft's primary paper. Current openness remains UNKNOWN.

Ran python -X utf8 verify_boundaries.py: 30 checks passed, 0 failed, 584 exact configurations, 0.015625 CPU seconds. The finite checks do not prove limits. Two concept-only DRAFT bundles contain five entries and three relations; none is claimed reviewed, ingested or retrievable.

NEXT: w440 reviews the subdivision proof and source correction in REVIEW_PACKET.md, then the integrator handles accepted concepts and the staged hook.

## Review receipt update

w440 independently returned KEEP on w439 boundary claims 001-003, including the subdivision formula, graph-uniformity obstruction, exact 6L asymptotic and susceptibility divergence. See REVIEW_RECEIPT_w440.md. Source correction 004 remains pending. Submitted concept drafts keep their original preparation-time annotations; the receipt and BRAIN_HANDOFF.json record the subsequent review state. Ingestion and retrieval have not been checked.

NEXT: w440 reviews source correction 004; coordinator integrates accepted concept drafts using the receipt and audits the local hook.
