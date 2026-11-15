# Rigorous special cases and the induction obstruction

Let E be finite; P_L denotes the projection determinantal measure. If V has orthonormal columns spanning a rank-r space L, then P_L(B)=|det V_B|^2 for |B|=r, by Cauchy–Binet. In particular, the masses sum to one.

## Rank one: a constructive finite flow

Suppose H=span(u) orthogonal-sum W, ||u||=1, dim W=k. Choose an orthonormal basis v_1,...,v_k of W; put w=v_1 wedge ... wedge v_k, z=u wedge w. Their coordinates are the signed minors of V and [u,V]. Let a(B)=|w_B|^2 and b(C)=|z_C|^2 for |B|=k, |C|=k+1.

Make a network: s -> B has capacity a(B); B -> C has capacity 1 whenever B subset C; C -> t has capacity b(C). Fix lexicographic orders and run Edmonds–Karp to obtain a maximum flow. We now prove its value is 1, so this is an explicit finite algorithm, including for real/complex inputs with exact real capacities.

For a family F of k-subsets let N(F) be all (k+1)-subsets containing an element of F. Let Pi_F, Pi_N be the orthogonal coordinate projections on the corresponding exterior powers. The interior product i_u, adjoint to wedge multiplication by u, satisfies ||i_u||<=1 and i_u z=w, since u is unit and orthogonal to W. Its coordinate B depends only on coordinates C containing B. Hence

    Pi_F w = Pi_F i_u Pi_N z,
    sum_{B in F} a(B) <= sum_{C in N(F)} b(C).

This is exactly the weighted Hall condition. To check it directly by cuts: a cut with any crossing B->C edge has capacity >=1; otherwise its capacity is at least 1-a(F)+b(N(F)) >=1. The source cut has capacity 1. Max-flow/min-cut therefore yields a flow gamma(B,C) with both prescribed marginals. The contraction identity is the adjoint Laplace/Plücker expansion and holds over C with the adjoint conjugations; all inequalities use squared absolute values.

Sample (B,C) from gamma, put X_2=B and X_1=C\B. The union law is b=P_H and X_2 has law a=P_W. The difference is one point. For every e,

    P(X_1={e})=P(e in C)-P(e in B)
                 =(P_H)_{ee}-(P_W)_{ee}=|u_e|^2.

Equivalently choose e with probability |u_e|^2 and, when this is positive, sample B with

    q_e(B)=gamma(B,B union {e}) / |u_e|^2,  e not in B.

These conditional laws sum to one and mix to P_W. The required union identity is sum_{e in C} |u_e|^2 q_e(C\{e})=b(C), a direct consequence of the flow's C-marginal. This does not assert that q_e is the ordinary DPP conditioned to avoid e.

This existence statement is already Lyons (2003), Lemma 10.4, from Theorem 6.2 and Strassen. The flow proof above spells out an effective construction from the exterior coordinates.

For countable E and finite-rank W, apply Lyons' stochastic domination and the fixed-size difference argument. For infinite-rank W, approximate W from below by finite-rank W_m orthogonal to the same u and take a weak limit of these couplings in the compact product {0,1}^E x {0,1}^E. Containment and "difference has at most one point" are closed. For each e the limiting difference probability is |u_e|^2. Their sum is one, so the limiting difference has exactly one point a.s. This is the rank-one part of Lyons' Proposition 10.3.

## Complement and permutation symmetry

P_{L perp}(E\B)=P_L(B), from complementary minors (Jacobi's identity for a unitary completion). For an orthogonal decomposition ell^2(E)=H_1 (+) H_2 (+) H_3, a desired union coupling is equivalent to a partition (X_1,X_2,X_3) with X_i~P_{H_i}. Indeed X_3=E\(X_1 union X_2), and conversely complementing X_3 gives the union. This condition is symmetric in the three spaces.

If any of dim H_1, dim H_2, dim H_3 is 0 or 1, the partition exists. For a zero space use complementary samples of the other two. For dim H_3=1, apply the rank-one result to H_3 (+) H_2 = H_1 perp, producing disjoint X_3,X_2 with union law P_{H_1 perp}; set X_1=E\(X_2 union X_3). Thus all codimension-one H and all |E|<=5 are settled. For |E|=6 the first unhandled triple of positive ranks is (2,2,2); for |E|=7 it is permutations of (2,2,3). These facts are consequences of the known rank-one theorem, not new full resolutions. For arbitrary codimension >=2 this argument alone says nothing when all three ranks are >=2.

## Coordinate blocks

Suppose E is partitioned into coordinate blocks E_j and H_i=orthogonal-sum_j H_{ij}, with H_{ij} contained in ell^2(E_j). If a union coupling exists in each block, take these couplings independently and unite each color. The determinant of each block diagonal projection factors, proving all required laws. In particular if H_1 and H_2 have disjoint coordinate supports their independent DPPs suffice. More generally the result holds if, in each finite block, at least one of the three ranks (dim H_{1j},dim H_{2j}, |E_j|-dim H_{1j}-dim H_{2j}) is <=1. Countably many finite blocks follow by taking product measures and checking all finite inclusion events.

## Why the proposed induction does not follow

Write H=H_1' (+) span(u) (+) H_2. Suppose first (A,B) couples P_{H_1'},P_{H_2}, with S=A union B~P_{H_1' (+) H_2}. Then use a rank-one monotone kernel to add e to S and get T=S union {e}~P_H. This preserves B's marginal, disjointness, and the union law. It also gives {e}~P_span(u). It does not determine A union {e}~P_{H_1' (+) span(u)}: the joint dependence of A and e is uncontrolled. Having correct singleton intensities fixes a rank-one DPP, but cannot fix a higher-rank DPP. A separately saved exact example demonstrates failure for valid choices at both stages. This is an obstruction to this composition argument, not to the conjecture.
