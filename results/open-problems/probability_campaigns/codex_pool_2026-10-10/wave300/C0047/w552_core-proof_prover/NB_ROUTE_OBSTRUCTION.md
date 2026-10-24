# OB1: the universal nonbacktracking shortcut is false

Author w552, 2026-10-10; independent referee w554 pending. Existing peer w559 has an independent triangle-family lane. This result concerns the failure of the specific extra condition p_c beta<1; no new finite-configuration enumeration is needed and no novelty claim is made.

Let Gamma=C_3*C_2, with generating set {a,a^{-1},s}, where a has order 3 and s has order 2. Its simple undirected 3-regular Cayley graph G is a tree of triangles: the a-cosets are disjoint triangles, every vertex has one s-bridge, and contracting triangles produces the 3-regular tree. A quotient cycle would give a nonempty reduced alternating word in the free product equal to the identity, which the free-product normal form excludes.

This Cayley graph is nonamenable by a direct boundary count. For any nonempty finite vertex set K, let r_j in {1,2,3} be its occupied vertex count in triangle j, let B be the number of occupied triangles and N=|K|. Internal triangle edges are at most sum_j r_j(r_j-1)/2. Bridges internal to K form a forest on the occupied quotient vertices and number at most B-1. Hence

|boundary_E K| >= sum_j [3r_j-r_j(r_j-1)-2]+2 >= N/3+2,

because the bracket has values 1,2,1 for r_j=1,2,3 respectively. Thus the edge Cheeger constant is at least 1/3.

For bond parameter p, the probability that two specified vertices within one triangle are connected is t(p)=p+p^2-p^3. Enter a new triangle through one already-used bridge. The internal cluster of the entry vertex has expected size 1+2t(p). Its other vertices have distinct unused outgoing bridges, each independently open with probability p. Since the quotient is a tree, successive blocks have disjoint internal edge sets and unused bridge sets. Conditioning on the used incoming bridge leaves each new block's law unchanged. The nonroot exploration is therefore an actual Galton-Watson process, not a multiplication of dependent conditional estimates, with offspring mean

m(p)=2p t(p)=2p^2+2p^3-2p^4.

The root has a finite initial number of branches. Standard finite-mean branching-process extinction/survival yields the unique critical solution m(p_c)=1. At p=3/5, m(p)=558/625<1, and continuity gives p_c>3/5. This strict lower bound suffices here; no numerical root search is used.

Let alpha=||A_G||_2. Test adjacency quadratic forms on functions constant within each triangle, taking value h on the corresponding quotient-tree vertex. Their norm is 3||h||_2^2. The internal triangle contribution is 6||h||_2^2 and the bridges contribute <h,A_T3 h>. Truncated radial quotient-tree vectors have Rayleigh quotients tending to 2sqrt(2), by NONBACKTRACKING_LEMMA.md's tree calculation. Thus alpha>=2+2sqrt(2)/3.

For d=3, b=2 and beta=(alpha+sqrt(alpha^2-8))/2, since this lower bound is greater than 2sqrt(2). The function z+2/z is strictly increasing for z>sqrt(2). At z=5/3 it equals 43/15, while 2+2sqrt(2)/3>43/15 (equivalently sqrt(2)>13/10). Therefore beta>5/3, and

p_c beta > (3/5)(5/3)=1.

The strict sufficient hypothesis in L4 FAILS on this nonamenable Cayley graph. Thus a proposed universal lemma "nonamenability implies p_c beta<1" is false; L4's correctly conditional estimate is unaffected. The broader critical norm input in L1-L3 remains unresolved here.

For completeness this graph has p_u=1: for p<=p_c all clusters are finite by branching-process extinction. For p_c<p<1, condition a fixed quotient bridge to be closed. Its two sides use disjoint independent edges and each has positive survival probability s(p), so probability (1-p)s(p)^2>0 produces at least two infinite clusters. Hence no p<1 belongs to the almost-sure uniqueness set. At p=1 the connected graph is unique. This is a proved special case of the desired inequality, not a counterexample to C0047.
