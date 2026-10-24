SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T15:38:36Z.
attacking: diffuse k=1 collective child-plus-rank-two cross compiler by macroscopic ORIGINAL-coordinate grouping before local pivot loss.

# Early substantive checkpoint — collective three-frame half-cut

Full target remains OPEN. Work at scale L>0. Put

c=(1/2)sqrt(3/5),   beta=(3/16)sqrt(3/5).

Let I,J be disjoint ORIGINAL-coordinate banks. Suppose the child/cross pair has a structured reference

C0=lambda r r^T + U H U^T + D,    B0=U Sigma V^T,

where r is unit in R^I, U and V have two orthonormal columns, H is arbitrary symmetric 2x2, D is diagonal in ORIGINAL coordinates, |lambda|>=cL, and s2(Sigma)>=beta L. Put

delta=||(I-UU^T)r||,
q=(I-UU^T)r/delta,
W=[q,U],
nu=max_i ||W_{i,*}||^2.

Assume delta>0 and nu<=1/48. A random half-cut S|T of I satisfies for some realization

(1/4)I_3 <= G_S=W_S^T W_S <=(3/4)I_3,
(1/4)I_3 <= G_T=W_T^T W_T <=(3/4)I_3.

Indeed E||G_S-I_3/2||_F^2=(1/4)sum_i||W_{i,*}||^4 <=3nu/4<=1/64, so Markov gives positive probability of Frobenius deviation <=1/4.

Write z=W^T r=(delta,a) with |z|=1 and H3=lambda z z^T+diag(0,H). For the physical cross block from S to T union J,

M0=[C0[S,T],B0[S,J]],

D contributes no cross entries and

M0 M0^T=W_S K W_S^T,
K=H3 G_T H3+diag(0,Sigma^2).

For x=(x0,y), the first coordinate of H3 x is lambda delta <z,x>, hence

x^T K x >= (lambda^2 delta^2/4)<z,x>^2 + beta^2 L^2 ||y||^2.

The right side has least eigenvalue at least

L^2 c^2 beta^2 delta^4/(c^2 delta^2+4 beta^2).

Since G_S>=I/4, the three nonzero singular values of M0 obey

s3(M0) >= kappa(delta)L,
kappa(delta)=c beta delta^2/[2 sqrt(c^2 delta^2+4 beta^2)].

Also range(M0)=range(W_S), so every physical row leverage of range(M0) is at most 4nu<=1/12<1/2.

Therefore, for actual C=C0+E_C and B=B0+E_B, the actual grouped cross block M differs from M0 by operator norm at most

rho=sqrt(||E_C||op^2+||E_B||op^2).

If rho<=kappa(delta)L/16, the completed volume-stability theorem at math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba applies to this literal ORIGINAL-coordinate cross block and gives a continuous C0 density with

||p_Q||inf < 23/[kappa(delta)L].

In particular delta>=1/2 gives kappa(delta)>=0.020140730832359... and ||p_Q||inf<1142/L provided rho<=0.001258795677023 L. The remaining k=1 hybrid is thus forced into quantified child/cross alignment delta<1/2, augmented-frame localization nu>1/48, or non-three-frame leakage exceeding the displayed operator threshold.

This is a supporting theorem, not a full solution. It preserves the original product law because the only probabilistic receiver is the completed physical-coordinate volume theorem after an ORIGINAL-coordinate regrouping.
