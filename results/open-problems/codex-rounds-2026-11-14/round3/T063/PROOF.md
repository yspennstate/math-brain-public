# Free-energy minimality of near-balanced torus limits

Fix a=b=1 and c>0. All logarithms are natural. Heights are not needed in this argument.

## Statement

Let Z(N,L;n) be the partition function on the labelled N-column, L-row torus, restricted to configurations with exactly n right-pointing horizontal arrows in each vertical cut. Let P(N,L;n) be the corresponding probability measure, extended periodically to the plane. Define

\[
p_L(n)=\lim_{N\to\infty}\frac{\log Z(N,L;n)}{NL},
\qquad
\mu_L=\lim_{N\to\infty}P(N,L;n_L).
\]

These fixed-L limits exist. Suppose L tends to infinity, 0<=n_L<=L, and n_L/L tends to 1/2. Then every local weak subsequential limit of mu_L maximises

\[
\mathcal P_c(\nu)=h(\nu)+\mathbb E_\nu\log w_0
\tag{1}
\]

over all translation-invariant probability measures on allowed six-vertex configurations. Here h is entropy per vertex and w_0 is the local vertex weight. Equivalently, every such limit minimises specific free energy. No uniqueness assertion is assumed in this statement.

Write p_c for the supremum in (1). A finite-strip lower bound used below is

\[
p_L(n)\ge \frac{H}{L}p_c-\frac{3\log2}{L},
\qquad H=2\min(n,L-n)\ge2.
\tag{2}
\]

Consequently p_L(n_L) tends to p_c. If, additionally, the maximiser of (1) is unique, the whole sequence mu_L converges to it.

## 1. Encoding and entropy

At a vertex write (r,s,b,t) for the directions of its left, right, bottom and top incident edges, using 1 for right or up and 0 for left or down. The ice rule is

\[
r+b=s+t.
\tag{3}
\]

There are six such vertex types. Two adjacent vertex labels must agree on their shared edge. The weight is c when r differs from s, and 1 otherwise. In the former case the two horizontal arrows both enter or both leave the vertex.

For a finite rectangle R of vertices, a free filling specifies all incident arrows, including boundary arrows, with compatibility on internal edges. Its weight is the product of its vertex weights. The vertex alphabet has size six, and log w is bounded for fixed c>0.

For a stationary allowed law nu, let H_nu(R) be its finite Shannon entropy. The entropy density satisfies

\[
h(\nu)=\lim_{m\to\infty}\frac{H_\nu([0,m)^2)}{m^2}
=\inf_{a,b\ge1}\frac{H_\nu([0,a)\times[0,b))}{ab}.
\tag{4}
\]

Indeed, tile a large square by translates of any fixed a-by-b rectangle, with a remainder of size O((a+b)m). Subadditivity and stationarity bound its entropy by the number of tiles times the rectangle entropy, plus the remainder size times log 6. Division by m^2 and passage to infinity give the upper bound by every rectangle entropy density. Applied to squares, the same argument shows that the limsup is at most the infimum of square entropy densities. The liminf is at least that infimum by definition, proving existence of the limit. These two statements give (4).

The all-right, all-up configuration has entropy zero and all weights one. Thus

\[
0\le p_c\le\log6+\max(0,\log c)<\infty.
\tag{5}
\]

Let Z_free(N,L) be the free-rectangle partition sum. The elementary finite entropy inequality gives, for every stationary nu,

\[
H_\nu(R)+NL\,\mathbb E_\nu\log w_0\le\log Z_{\rm free}(N,L).
\]

For completeness, if q is the marginal of nu and g(x)=W(x)/Z_free is the finite Gibbs law, nonnegativity of the relative entropy sum q(x)log(q(x)/g(x)) is exactly this inequality. Combining it with (4), then taking the supremum over nu, gives

\[
p_c\le \frac{\log Z_{\rm free}(N,L)}{NL}
\quad\hbox{for every }N,L.
\tag{6}
\]

## 2. Four rectangles give a balanced torus

Fix all 2N+2L boundary arrows of a rectangle and call this boundary condition beta. Let Z_beta be its partition sum; impossible boundary conditions have Z_beta=0. There are at most B=2^(2N+2L) boundary conditions, and Z_free=sum_beta Z_beta.

Let F_x mean reflection in a vertical line followed by reversal of every arrow. Let F_y mean reflection in a horizontal line followed by reversal of every arrow. Both preserve the ice rule and all weights. Under F_x, horizontal directions stay unchanged and vertical directions are reversed; under F_y, vertical directions stay unchanged and horizontal directions are reversed. Both transformations also reverse the order of coordinates in their reflected direction.

Choose four fillings A,B,C,D with boundary condition beta, independently. Put them in a 2N-by-2L array in the following positions:

\[
\begin{matrix}
F_y(C)&F_yF_x(D)\\
A&F_x(B).
\end{matrix}
\tag{7}
\]

All interfaces match. For example the right boundary of A and the left boundary of F_x(B) are the same right-boundary list of beta. The top boundary of A and the bottom boundary of F_y(C) are the same top-boundary list. The other internal interfaces follow by the same transformations. The outer left and right boundaries are copies of the left-boundary list of beta, with the same transformation in the upper half. They match when identified. Likewise the outer bottom and top boundaries match. Thus (7) defines a torus configuration.

On its outer vertical cut, the upper horizontal arrows are the reversed-order, opposite-direction list of the lower horizontal arrows. Exactly L of the 2L arrows point right. Summing the ice rule over a column of the torus shows that the number of right arrows is constant from one vertical cut to the next: all vertical contributions cancel by periodicity. The torus is therefore in the balanced sector. The same construction balances the other flux as well, although that is unnecessary here.

The map from (beta,A,B,C,D) to the labelled torus is injective. Cut at the prescribed N-by-L block boundaries, undo F_x and F_y, and recover all four fillings and beta. Boundary arrows are also determined by the torus, including those on the prescribed cuts. The weight of the image is the product of the four original weights. Hence

\[
Z(2N,2L;L)\ge\sum_\beta Z_\beta^4
\ge \frac{Z_{\rm free}(N,L)^4}{2^{6(N+L)}}.
\tag{8}
\]

The second inequality is Holder's inequality (sum z)^4<=B^3 sum z^4. Notice the exponent three: four copies contribute fourth powers, while summing the possible boundary conditions costs B^3.

The exponent can also be checked by applying Cauchy-Schwarz twice: (sum z)^2<=B sum z^2 and (sum z^2)^2<=B sum z^4. Their combination is exactly the asserted fourth-power inequality.

Equations (6) and (8) imply

\[
p_c\le \frac{\log Z(2N,2L;L)}{4NL}
+\frac{3\log2}{2}\left(\frac1N+\frac1L\right).
\tag{9}
\]

## 3. Fixed-width limits

A column transfer matrix T_L is indexed by the lists r,s of horizontal arrows on its two sides. Its entry is the sum of products of vertex weights over compatible periodic vertical arrows. Equation (3), summed over the column, shows that T_L preserves the number n of right arrows.

Every diagonal entry in a sector is positive: when r=s, choose all vertical arrows up, or all down. For every adjacent cyclic pair of sites occupied by 10 in r, exchanging this pair to 01 in s gives a positive entry: choose the vertical arrows to change value at these two sites and stay constant elsewhere, as required by (3). The reverse exchange is allowed too. Adjacent exchanges connect every pair of binary lists with n ones. Thus the sector matrix is irreducible, and its positive diagonal makes it primitive. The sectors n=0,L are singletons and also primitive.

The Perron-Frobenius theorem supplies a simple positive leading eigenvalue lambda_L(n), with every other eigenvalue smaller in modulus. Since

\[
Z(N,L;n)=\operatorname{Tr}(T_{L,n}^N),
\]

the fixed-width pressure exists and is log(lambda_L(n))/L. Finite local probabilities have the same trace expression with finitely many entries or marked transitions specified. Dividing by the partition sum and using the rank-one Perron limit proves convergence of every cylinder event as N tends to infinity. This gives the stated fixed-L local limit mu_L. Both finite-torus measures and mu_L are invariant under translations in both coordinate directions.

Take N to infinity in (9), using the even-width subsequence, which has the same Perron limit. With H=2L this yields

\[
p_H(H/2)\ge p_c-\frac{3\log2}{H}
\quad\hbox{for every even }H\ge2.
\tag{10}
\]

## 4. Insert rows

Suppose 1<=n<=L/2 and start with a balanced N-by-2n torus. Cut along a horizontal seam and insert L-2n rows. Set every horizontal arrow in the new rows to point left. At each column, extend the seam's vertical arrow straight through every inserted row. At each new vertex r=s=0 and b=t, so it is allowed and has weight one. The top and bottom seams match.

Each vertical cut retains precisely n right arrows. The construction is injective because the inserted row positions are fixed and can be removed. Original weights are unchanged. Therefore

\[
Z(N,L;n)\ge Z(N,2n;n).
\tag{11}
\]

Reversing all arrows gives Z(N,L;n)=Z(N,L;L-n). Put H=2 min(n,L-n). Taking N to infinity in (11) and applying (10) gives

\[
p_L(n)\ge\frac{H}{L}p_H(H/2)
\ge\frac{H}{L}p_c-\frac{3\log2}{L},
\]

which is (2). In particular, if n_L/L tends to 1/2, H/L tends to 1 and H tends to infinity, and

\[
\liminf_{L\to\infty}p_L(n_L)\ge p_c.
\tag{12}
\]

No assertion about open-row operator norms or Bethe eigenvalues is used.

## 5. Entropy bound for local limits

Let pi_j=P(N_j,L_j;n_j), with both N_j and L_j tending to infinity, and suppose its periodic extension converges locally to nu. Let

\[
q_j=\frac{\log Z(N_j,L_j;n_j)}{N_jL_j},
\qquad e_j=\mathbb E_{\pi_j}\log w_0.
\]

The finite Gibbs identity gives

\[
q_j=\frac{H(\pi_j)}{N_jL_j}+e_j.
\tag{13}
\]

Fix m. Partition the fundamental torus rectangle into disjoint m-by-m squares and an uncovered remainder of size at most m(N_j+L_j). By subadditivity, translation invariance, and the six-letter alphabet,

\[
q_j\le \frac{H_{\pi_j}([0,m)^2)}{m^2}+e_j
+m\left(\frac1{N_j}+\frac1{L_j}\right)\log6.
\tag{14}
\]

Every fixed-block entropy is continuous in its finite marginal, including at zero probabilities, because -x log x extends continuously at zero. Also e_j tends to e_nu, since log w_0 is a bounded single-site function. Thus

\[
\limsup_j q_j\le\frac{H_\nu([0,m)^2)}{m^2}+e_\nu.
\]

Letting m tend to infinity gives

\[
\limsup_j q_j\le\mathcal P_c(\nu)\le p_c.
\tag{15}
\]

Compactness used here is elementary: the six-letter product space is compact, and the allowed configurations form a closed subset because compatibility is a local constraint. Stationarity also passes to local limits. In particular every sequence of these torus laws has a locally convergent subsequence when both dimensions grow.

Now let L_j be any subsequence along which mu_L converges locally to nu. For each j choose N_j sufficiently large that N_j>=jL_j, its pressure differs from p_Lj(n_Lj) by less than 1/j, and its marginal on [-j,j]^2 differs in total variation from that of mu_Lj by less than 1/j. There are finitely many patterns for each j, so the fixed-L limit permits this choice. Total variation decreases upon taking marginals; hence these finite-torus laws converge locally to nu. Combining (12) and (15) yields

\[
p_c\le\liminf_j q_j\le\limsup_j q_j
\le\mathcal P_c(\nu)\le p_c.
\tag{16}
\]

Thus every local subsequential limit maximises (1). It follows that p_L(n_L) tends to p_c along the whole sequence: if a subsequence violated this convergence, compactness of mu_L would supply a further locally convergent subsequence, and the same diagonal argument would give (16), a contradiction.

If the maximiser is unique, every convergent subsequence of mu_L has that limit. Compactness then implies convergence of the whole sequence. This last implication requires uniqueness of the translation-invariant maximiser, not merely uniqueness among ergodic zero-slope Gibbs measures.

## Consequence for the earlier report

Take n_L=L/2-floor(L^epsilon) along even L, with 0<epsilon<1. Then H=L-2 floor(L^epsilon), and (2) reads

\[
p_L(n_L)\ge p_c
-\frac{2\lfloor L^\epsilon\rfloor p_c+3\log2}{L}.
\tag{17}
\]

Every subsequential near-balanced limit therefore has the free-energy property required in O2. If the unique-minimiser assertion of Corollary 1.3 in Yan Ru Pei's [November preprint](https://hexagonmath.org/pdf/2611.00291v1) is valid at the chosen c, O1 and identification with that minimiser follow as well. Its uniqueness proof is not a premise of (2)–(17) and is not audited here. The argument establishes neither height correlations nor a GFF scaling limit.

## Finite checks

The independent exact enumeration in `check_surgery.py` checks (8) for rectangles of sizes 1x1, 2x1, 1x2 and 2x2 and c=1,2,3. It also checks (11) in 72 finite cases. Further checks at c=1/2 use exact rational arithmetic. A separate hand check gives Z_free(1,1)=4+2c, sum_beta Z_beta^4=4+2c^4, and Z(2,2;1)=8+2c^4. Direct checks of the actual maps produce 348 distinct four-copy torus images with correct seams, flux and weight, and verify 30 row insertions. These checks support the seam conventions; the proofs above apply to every c>0 and arbitrary sizes.
