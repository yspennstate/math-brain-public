# fleet03/B04 r63 — sharp multi-hub rearrangement

Run 20260924T231717Z-fleet03-B04-QFORM-auto11-r63. Objective QFORM-FIXED-MULTIPLICITY-AUDIT-20260924. Full three-eigenvalue target remains OPEN.

Current five-eigenvalue paper source: yspennstate/math-open-problems@5ba2a4d6b689721601cce7ec7e22ffea9fa98f90, proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/paper.tex, blob bbebd6f6c5a27e9f639186a305008ab43a481e70. The Lemma 5.3 correction (separate coordinates i and i' for the two hyperbola tails) passes; the affine Remark 8.2 extension also passes.

Designated partner actually used: fleet04/B04 audit at commit 18d2a5c7f525cb0cdbebd03664eb99fbeb1b2c23. Its product-projection theorem says that for independent coordinate densities <=K and full-row-rank L in R^{m x d},
||p_{LZ}||_infinity <= e^{m/2} K^m / sqrt(det(LL^T)).

THEOREM QFORM-PHYSICAL-MULTIHUB-LINF-v2.
Let H be m>=2 literal original coordinates, R=H^c, A_{H,H}=0, C=A_{H,R}, G=CC^T, det G>0. Then for arbitrary A_{R,R}, affine b and c,
||p_Q||_infinity <= [m/(m-1)] sqrt(e) K^2 det(G)^(-1/(2m)),
and p_Q is continuous and vanishes at infinity.

Proof. Condition on X_R. Then Q=V^T X_H+Gamma(X_R), V=2CX_R+b_H. For fixed v, choose j with |v_j|=||v||_infinity. Conditioning on the other hubs gives
||p_{Q|X_R}||_infinity <= K/||V||_infinity.
By the partner projection theorem,
||p_V||_infinity <= M=e^{m/2}K^m/[2^m sqrt(det G)].
Layer cake with the l_infinity kernel gives, for any probability density g<=M,
E 1/||V||_infinity
<= int_0^infinity min(1,M(2/t)^m) dt
= [2m/(m-1)] M^{1/m}.
Multiplication by K yields the theorem. Since V has an m-dimensional density, a.s. at least two components are nonzero. The conditional linear-form density is then a convolution of at least two L1 densities, hence C_0, and K/||V||_infinity is an integrable dominating envelope. Dominated convergence gives p_Q in C_0.

For m=2:
||p_Q||_infinity <= 2 sqrt(e) K^2 det(G)^(-1/4),
improving the current four-eigenvalue note's sqrt(2 pi e) constant by sqrt(2/pi).

Explicit genuinely non-diagonal indefinite example:
C=[[2,1,1],[1,2,-1]], D=J_3/20, A_*=[[0,C],[C^T,D]].
Then CC^T=[[6,3],[3,6]], det=27. At D=0 the nonzero eigenvalues are +/-3 and +/-sqrt(3); ||D||=3/20, hence s_4(A_*)>=sqrt(3)-3/20>1.58. Therefore
||p_{X^T A_* X+b^T X+c}||_infinity
<=2 sqrt(e) 27^(-1/4) K^2
=1.4465594793136336... K^2,
with continuous density.

CORRECTION QFORM-SMALL-INDEFINITE-HUB-FULL-GRAM-FALSE-v1.
A small nonzero indefinite hub block is not a harmless extension, even with fixed robust two-hub Gram.
For 0<epsilon<=1 take independent R1,R2 uniform[-1/2,1/2] and U1,U2 uniform[-1/(2epsilon),1/(2epsilon)] with density epsilon. Put
Q_e=2epsilon U1U2+R1U1+R2U2+R1R2/(2epsilon)
=2epsilon (U1+R2/(2epsilon))(U2+R1/(2epsilon)).
Here A_HH=[[0,epsilon],[epsilon,0]], A_HR=I_2/2, so ||A_HH||=epsilon and det(A_HR A_HR^T)=1/16.
For every fixed R, both shifted U-densities equal epsilon on [-1/(4epsilon),1/(4epsilon)]. Thus, for 0<|q|<1/(8epsilon),
p_{Q_e|R}(q) >= epsilon log[1/(8epsilon|q|)].
Averaging preserves this lower bound, hence ess sup p_{Q_e}=infinity.
This is not a full-QFORM counterexample: A has rank two, with nonzero eigenvalues +/-[epsilon+1/(4epsilon)].
It refutes only the intermediate implication “small indefinite hub block + robust two-hub Gram + arbitrary remainder => bounded density.” A four-eigenvalue proof must retain a genuine third/fourth curvature resource on that branch.
