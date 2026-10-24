# A077: sparse negative sets, a cardinality-uniform restricted FEI bound and asymptotic upper-set potential

Version: ACC03-B16-A077-SPARSE-NEGATIVE-SETS-v1. Date: 2026-10-12. Status: SELF-DERIVED / INDEPENDENT REVIEW PENDING. Full FEI OPEN.

## Exact statement

Work on the uniform d-dimensional cube {0,1}^d, Walsh characters chi_S(x)=(-1)^(sum_{i in S} x_i). For every integer d>=1 and every nonempty proper set A, set a=|A|, alpha=a/2^d, L=log2(a), f_A=1-2*1_A. Let p_S=hat f_A(S)^2, H=sum_S p_S log2(1/p_S), I=sum_S |S|p_S, pi(S)=sum_{T containing S}p_T, U=sum_S p_S log2(pi(S)/p_S). Zero terms are zero, including when hat f(empty)=0. Then

(1) I = 2^(1-d) b(A), with b(A)=d*a-2*e(A), e(A) the count of internal cube edges. In particular
      2*alpha*(d-L) <= I <= 2*alpha*d.

(2) m=sum_{S nonempty}p_S=4*alpha*(1-alpha), p_empty=(1-2*alpha)^2, and
      (2*d-2-2*L)*m <= H <= (2*d-2+log2(e))*m < 2*d*m.
Hence for 1<=a<2^d (so d-L>0), an actual uniform restricted FEI inequality holds:
      H/I <= 4*d*(1-alpha)/(d-L).
For all A satisfying a<=2^(gamma*d), with a fixed 0<=gamma<1, the universal-for-that-class constant 4/(1-gamma) works.

(3) Let E0=p_empty*log2(1/p_empty) (defined as 0 if p_empty=0).
There is a real E_A with |E_A|<=2*m*L such that
      U = d*m - I + E0 + E_A,
      0<=E0<=m*log2(e).

(4) For ANY sequence of actual nonconstant Boolean f_{A_d} with log2|A_d|=o(d):
      H(f_{A_d})/I(f_{A_d}) --> 4,
      U(f_{A_d})/I(f_{A_d}) --> 1.
Both limits are uniform over all set geometries with log2 a_d/d -->0 (the convergence rate depends only on that size ratio and 1/d). This is a restricted-class result and NOT full FEI.

## Proof

Write delta=2^(-d) and F(S)=sum_{x in A}chi_S(x), an integer. The Fourier coefficients are hat f(empty)=1-2*a*delta and hat f(S)=-2*delta*F(S) for nonempty S. Parseval for the Boolean f gives m=1-(1-2*alpha)^2=4*alpha*(1-alpha). Every nonzero F(S) has 1<=|F(S)|<=a. Thus p_S=4*2^(-2d)*F(S)^2, and its nonempty-atom log is 2*d-2-2*log2|F(S)|. Summing yields the exact entropy identity
      H = E0 + (2*d-2)*m - 2*sum_{S nonempty,p_S>0}p_S*log2|F(S)|.
The final sum lies in [0,m*L]. Since -(1-m)ln(1-m)<=m, E0<=m/ln2=m*log2(e). This proves (2).

For (1), coordinate i contributes Pr(f(x)!=f(x flipped at i)), counting each crossing edge twice among 2^d vertices. Summing gives I=2*b(A)/2^d. Degree counting gives b=d*a-2*e(A). The elementary induced-edge bound e(A)<=a*log2(a)/2 holds by induction on d: partition A by the final coordinate into A0,A1 of sizes a0,a1. The crossing internal edges are at most min(a0,a1), while the within-layer induction gives
      2e(A) <= a0*log2(a0)+a1*log2(a1)+2*min(a0,a1).
If a0<=a1 and t=a0/(a0+a1), binary entropy h2(t)>=2*t for 0<=t<=1/2 by concavity and the chord between (0,0) and (1/2,1). Hence the right side is <=a*log2(a). Use 0log0=0. The upper bound b<=d*a is immediate. This proves (1).

For (3), fix a nonempty S of size k. Split cube coordinates into u on S and y on its complement. Set z_y=sum_{u:(u,y) in A}chi_S(u), an integer. Then
      F(S union R)=sum_y z_y*chi_R(y), for R subset S^c.
Parseval for the UNNORMALIZED Walsh transform over the complement yields
      sum_{R subset S^c} F(S union R)^2=2^(d-k)*sum_y z_y^2.
With R_S=sum_y z_y^2, pi(S)=4*2^(-2d)*2^(d-k)*R_S. When p_S>0, F(S)!=0 implies 1<=R_S<=a^2; integrality and the triangle bound sum_y|z_y|<=a give the upper bound. Also 1<=F(S)^2<=a^2. Therefore
      log2(pi(S)/p_S)=(d-k)+log2(R_S/F(S)^2)
and the second logarithm belongs to [-2L,2L]. Summing p_S over all nonempty S gives
      U=E0+d*m-I+E_A, |E_A|<=2mL.
The k=0 term is exactly E0 since pi(empty)=1. This is an exact derivation, not an approximation.

For (4), L=o(d) forces alpha=a*2^(-d)->0. The influence bounds imply I/[2*alpha*d] ->1 and m/[4*alpha]->1, uniformly in A. Therefore d*m/I ->2 and m*(L+1)/I ->0. Substituting into the entropy and upper-set formulas proves H/I->4 and U/I->1. No FEI-equivalent universal estimate was assumed.

## Explicit new growing cluster and stress cases

Radius-one Hamming ball A={x: Hamming weight(x)<=1} has a=d+1, e(A)=d, b(A)=d(d-1). For d>=2, F(S)=d+1-2k with k=|S|, so
      p_empty=(1-2*(d+1)/2^d)^2,
      p_S=4*2^(-2d)*(d+1-2k)^2 for nonempty S.
For k>=1, pi(S)=4*2^(-2d)*2^(d-k)*[(k-1)^2+d-k].
This is a genuine overlapping (not disjoint-tensor) cluster, and H/I->4, U/I->1. Radius-two Hamming balls and arbitrary subexponential cardinality clusters are also covered by (4), without requiring spatial disjointness or an independent-padding assumption.

Stress boundary: appending t spectator coordinates replaces a by a*2^t but leaves H,I,U exactly unchanged. Thus log2 a=o(d) is a sufficient geometry-agnostic condition, NOT a necessary one, and should not be treated as spectator-invariant. Replacing f by -f exchanges the negative set with its complement without changing p,H,I,U; if the complement is small, apply the theorem to that complement instead. For a growing fixed-radius Hamming ball, a is polynomial in d, so it meets the theorem. No claim about all balanced Boolean functions or subexponential spectral support follows.

## Obstruction

This rules out an actual H/I or U/I divergence for all rare negative clusters with log2|A|=o(d), including arbitrarily overlapping clusters. The size condition is essential to the proof: the gap d-log2 a in the edge lower bound can shrink for large sets; the theorem does NOT exclude dense, high-rank or structurally complex negative sets as a potential full-FEI counterfamily. It also does not refute possible divergence of an auxiliary selector charge or a nonphysical information surrogate.

## Independent review requested

A092 or A088 should independently check: (i) the induced-edge entropy induction, (ii) the unnormalized conditional Walsh Parseval identity and the sum over all supersets, (iii) the exact coefficient lower bound from integrality, (iv) no missing contribution from p_empty=0 or spectator coordinates, and (v) whether a stronger existing result makes this class increment redundant. No independent reviewer has accepted this version.
