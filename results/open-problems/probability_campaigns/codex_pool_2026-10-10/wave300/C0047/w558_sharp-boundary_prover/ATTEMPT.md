# C0047: a sharp free-product boundary and a failed uniform spectral bridge

Scope: Bernoulli bond percolation, as defined in STATEMENT.md. The parent conjecture is not solved. All results below are author proofs awaiting w560; novelty is not claimed. The regular-tree benchmark is saved separately as CLAIMS.jsonl row C0047-w558-L0.

## Family and hardest remaining gap

Let Gamma=F_2=<a,b>, N>=1, S_N={a^k:1<=|k|<=N} union {b,b^-1}, and G_N=Cay(Gamma,S_N), using right multiplication (isomorphic to the left convention by inversion). D_N=2N+2. These are simple graphs on the **same nonamenable group** for all N.

The single hardest missing step for the parent problem is replacing the fresh, independent factor-line exploration below when a prescribed Cayley graph has relations and no such bridge decomposition. Nonamenability alone supplies neither the disjoint unexplored factors nor isolating bridge cuts. We do not multiply conditional estimates in their absence, infer that every nonamenable group contains F_2, or transfer a generating-set existence result to every prescribed set.

## Lemma A: finite factor clusters and an exact critical equation

Let H_N be the graph on Z with edges {i,j} when 1<=|i-j|<=N. Let K_N(p) be the size of the open cluster of 0 in bond percolation on H_N, and chi_N(p)=E K_N(p). For 0<=p<1 this expectation is finite. The exact p_c(G_N) is the unique alpha_N in (0,1) satisfying

    alpha_N * (2 chi_N(alpha_N) - 1) = 1.

Proof of finiteness. A cut between consecutive integers has M_N=N(N+1)/2 crossing edges. All are closed with probability q=(1-p)^M_N>0. Take cuts separated by N+1; their crossing-edge sets are disjoint, so their closure events are independent. The closest closed cuts on either side confine the root cluster, with geometrically decaying distance tails. Thus K_N has an exponential tail and finite expectation. Uniform tails on 0<=p<=p_0<1 also prove continuity of chi_N by truncation to a finite interval. Its monotonicity follows from the ordinary edgewise coupling. It is at least chi_1(p)=(1+p)/(1-p), and hence diverges as p approaches 1.

Proof of the equation, including the independence needed for it. The a-lines are the sets g<a>. In the ordinary {a,a^-1,b,b^-1} Cayley tree, contract every entire a-line. The quotient is a tree: a cycle would lift to a cycle in that tree, and there is at most one b-edge between any two lines. Added a-power edges stay inside the same line. Every b-edge is consequently a bridge of G_N.

Expose the horizontal open cluster in the initial line; it has law K_N. Its vertices supply 2K_N b-edges to distinct new lines. For a subsequent line reached via a single open b-edge, its horizontal root-cluster again has the same law K_N, independently of all previously exposed lines. Exactly one of its 2K_N b-edges is the incoming edge; the remaining 2K_N-1 lead to distinct unexplored lines. Their states are mutually independent Bernoulli(p), and independent of horizontal states. Quotient acyclicity ensures no line is revisited and no two offspring explore the same line. Thus the noninitial exploration is precisely a Galton-Watson process with offspring law Binomial(2K_N-1,p), where each individual samples its own independent K_N. Its mean is m_N(p)=p(2chi_N(p)-1). The initial offspring law is Binomial(2K_N,p), which has a positive chance of spawning a surviving descendant whenever m_N>1.

For 0<p<1 the offspring law has a positive probability of zero and is not identically one. Since its mean is finite, the Galton-Watson extinction criterion gives extinction for m_N<=1 and survival for m_N>1. Each horizontal cluster is finite, so an infinite G_N cluster is equivalent to infinite exploration. The function m_N is continuous, strictly increasing on (0,1), starts at zero and tends to infinity. This proves the unique equation and also no infinite cluster at alpha_N. This is an exact analytic characterization, not a numerical root claim or a general-Cayley argument.

## Lemma B: uniqueness threshold is exactly one

For all N>=1, p_u(G_N)=1, and almost surely there are infinitely many infinite clusters at every alpha_N<p<1.

Proof. Consider the ordinary-tree ray e,b,b^2,... . At its n-th vertex choose the bridge from b^n a to b^n a b and the component H_n beyond that bridge, away from the ray. These components are mutually disjoint. No added a-power edge crosses any of the b-bridge cuts, since its ordinary-tree path uses only a-edges. Each H_n has the noninitial exploration of Lemma A, so the root has an infinite cluster within H_n with probability s_N(p)>0 when p>alpha_N. The event that this happens and the attaching bridge is closed has probability s_N(p)(1-p)>0. The events use pairwise disjoint edge sets; they are independent. Infinitely many occur almost surely, by independent trials (or the second Borel-Cantelli lemma). Their infinite clusters cannot connect outside H_n because its attaching edge is a bridge and is closed. Below and at alpha_N there is no infinite cluster by Lemma A. At p=1 the connected graph is the unique infinite cluster. Thus p_u=1.

## Lemma C: exact isoperimetry and spectral pollution on a fixed group

Define phi_E(G)=inf over finite nonempty A of |partial_E A|/|A|, and normalized conductance h=phi_E/D. Then

    phi_E(G_N)=2,      h(G_N)=1/(N+1),
    N/(N+1) <= rho(G_N) <= (N-1+sqrt(3))/(N+1) < 1.

Here rho is the l2 operator norm of simple random walk, with uniform probability 1/D on each generator. In particular rho(G_N) tends to 1 although every G_N has p_c<p_u=1. There is no epsilon>0 bounding rho(Cay(F_2,S)) by 1-epsilon for all finite symmetric simple generating sets S.

Proof of isoperimetry. G_N contains the spanning ordinary 4-regular tree. For every finite A that tree has boundary 2|A|+2c(A)>=2|A|, so phi_E(G_N)>=2. For A_L={e,a,...,a^(L-1)} with L>=N, there are 2L outgoing b-edges and 2k outgoing a^k-edges for each 1<=k<=N. Thus |partial_E A_L|=2L+N(N+1); divide by L and let L tend to infinity to obtain phi_E<=2.

Proof of the lower spectral bound. The indicator of A_L has Rayleigh quotient

    <1_A,P_N 1_A>/||1_A||_2^2 = N/(N+1) - N/(2L).

Let L tend to infinity. For the upper bound split the adjacency into the ordinary-tree adjacency plus 2N-2 extra unitary translations. The ordinary-tree adjacency has norm at most 2sqrt(3): orient towards a fixed end, so every vertex has one parent and three children, and apply 2|uv| <= t|u|^2+t^-1|v|^2 with t=1/sqrt(3) to every parent-child edge. Summing over finitely supported vectors gives coefficient 3t+t^-1=2sqrt(3); absolute values also bound the negative spectrum. The triangle inequality now gives ||P_N|| <= (2sqrt(3)+2N-2)/(2N+2), as asserted.

The refuted bridge is the **uniform** spectral-gap claim. We do not refute the correct individual equivalence nonamenability iff rho<1, nor the original percolation conjecture. In fact Juschenko-Nagnibeda already explicitly discuss spectral radius approaching one by adding powers of an infinite-order element (Section 1); this packet supplies exact conductance and an independent percolation decomposition for the concrete F_2 family.

## Quantitative corollaries

chi_N(p)>=1+2Np by counting directly connected neighbors, so

    1/(2N+1) <= alpha_N <= (sqrt(1+16N)-1)/(8N).

The lower bound is the ordinary self-avoiding-path union bound for degree 2N+2. For N=1, chi_1=(1+p)/(1-p); the equation reduces to 3p^2+2p-1=0, giving alpha_1=1/3.

For N>=2 the monotone coupling adds vertices +2 and -2 on the respective events that the direct length-two edge is open while the adjacent root nearest-neighbor edge is closed. Each event has probability p(1-p); on it that vertex was absent from the nearest-neighbor root cluster. Distinct indicators add pointwise, without requiring independence between them. Therefore

    chi_N(p) >= chi_1(p) + 2p(1-p),

which proves alpha_N<1/3. More quantitatively alpha_N is at most the root in (0,1/3) of 4p^4-8p^3+7p^2+2p-1=0. The gated run brackets this upper-bound root exactly and gives approximately 0.289575883313. Since the quartic at 29/100 is exactly 46981/25000000>0, alpha_N<0.29 for every N>=2. This is not an exact value of alpha_N.

## A concrete correction to the prior spectral route

The local C0047-A001 record (intake_claude_20260907/attempts.jsonl, line 37) repeatedly treats p_c<1/rho for normalized simple random walk as a sufficient condition. This omits the degree. Juschenko-Nagnibeda Section 1, Theorem 2 states the sufficient condition D*rho*p_c<1. The missing factor changes the argument: p_c<1/rho is automatic when rho<1 and p_c<=1, and cannot prove the conjecture.

Even the correctly normalized sufficient condition cannot be elevated to a necessary one, or asserted on every nonamenable graph. The ordinary 4-regular tree has p_c=1/3, p_u=1 and rho=sqrt(3)/2, hence D*rho*p_c=2sqrt(3)/3>1. To verify the exact rho rather than cite it silently, combine Lemma C's upper adjacency bound with the finitely supported test functions f_R(v)=3^(-dist(e,v)/2) for dist(e,v)<=R and zero elsewhere. Their squared norm is 1+4R/3 and adjacency quadratic form is 8R/sqrt(3). The quotient tends to 2sqrt(3), giving equality after dividing by degree 4.

This counterexample refutes the proposed stronger auxiliary bridge, and corrects a source normalization error. It supports, rather than refutes, the original target in this example.

## Prior-work digest and review receipt

- Exact local problem row: intake_claude_20260907/problems.jsonl line 47 records the infinite-group Cayley iff statement, source Conjecture 2 p.4, current_status unverified and attempted_unsolved. Its own bounded search did not certify 2026 status.
- Exact local attempt: C0047-A001 at attempts.jsonl line 37 uses a spectral route, omits degree in its putative criterion, acknowledges confusion and supplies no proof. The correction above is the primary landable change from reading it.
- Scoped searches in the named H_20260912 and I_20260914 attempts found no C0047/Benjamini-Schramm file; the annotated Lean list carries only attempted_un, with no C0047 theorem certificate located. This is a negative scoped search, not an audit of all prior work.
- Team O board has no C0047 row; its P0041 is the broader nonamenable quasi-transitive target. No Team O artifact is overwritten.
- The required scar perceptron_proof_open_gaps_fleet_2026_07_12 was read after the capped recall timed out. Applied lesson: distinguish a passing script from a complete mathematical proof, bind review to the actual artifact, and name the hardest unclosed piece. Private scar details remain in the worker report only.
- Primary prior art: Kozakova, arXiv:math/0611668v3, Theorem 1 gives (chi_1-1)(chi_2-1)=1 for the union of factor generating sets. With factors <a> and <b>, chi_b=(1+p)/(1-p), this is exactly p(2chi_N-1)=1. Thus Lemma A is an independently derived specialization of a published result, not a new theorem claim. Section 1.2 also notes p_u=1 for nontrivial free products other than C2*C2.
- Juschenko-Nagnibeda, arXiv:1206.2183v3, Section 1 explicitly notes that adding powers of an infinite-order element can make rho approach one. Lemma C's phenomenon is therefore known; the explicit F_2 constants are a useful boundary record, with no novelty claim.
- Hutchcroft-Pan, arXiv:2409.12283v1, Section 1, explicitly reports the general nonuniqueness conjecture open in September 2024. The bounded 2026 search found a planar-site Conjecture 7 paper, which concerns a different target and cannot retire C0047. The peer's source URL led to the public openai/math overview result 214, independently opened here: it claims a September 24, 2026 bond resolution for all infinite connected locally finite nonamenable quasi-transitive graphs. This includes the present bond Cayley target if sound. Its linked PDF could not be extracted by the web tool (unsupported octet-stream); w560 is auditing that proof. An overview claim is not a mathematical audit. Current openness remains UNKNOWN, with a public resolution claim explicitly recorded.

VALIDATION: the fresh gate admitted one BelowNormal foreground process; 128 configurations, 64 gain events and five boundary/Rayleigh cases passed with zero failures in 0.005496 seconds of Python body time. Independent mathematical review remains pending with w560; w559 independently confirmed the source normalization in a preliminary mesh message. No independently checked proof, current-openness certification, or served-model identity is inferred from file existence or requested settings.
