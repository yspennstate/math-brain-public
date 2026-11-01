# fleet03/B18 r25 — early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

## New implication under construction: MSS paving + current volume-stability theorem

Let the actual symmetric matrix have spectral decomposition

A = U Lambda U^T + E,

where U has three orthonormal columns corresponding to three actual eigenvalues with |lambda_k|>=1, and E is the remaining spectral tail. Put delta=max_i ||u_i||_2^2, u_i the i-th row of U.

Marcus--Spielman--Srivastava's two-part vector partition theorem says that for a Parseval frame sum_i u_i u_i^T=I_3 with ||u_i||^2<=delta, there is a partition I,J such that

G_I=sum_{i in I}u_i u_i^T <= (1/sqrt(2)+sqrt(delta))^2 I,
G_J<= (1/sqrt(2)+sqrt(delta))^2 I.

Since G_I+G_J=I, both also satisfy G_I,G_J >= c_delta I with

c_delta = 1-(1/sqrt(2)+sqrt(delta))^2 = 1/2-sqrt(2 delta)-delta.

At delta<=1/18 one has c_delta>=1/9 and delta/c_delta<=1/2 (the endpoint identities are exact: sqrt(2 delta)=1/3, c_delta=1/9).

For the rank-three spectral cross block

M0=A0[I,J]=U_I Lambda U_J^T,

write U_I=Q_I G_I^(1/2), U_J=Q_J G_J^(1/2) with Q_I,Q_J having orthonormal columns. Hence the three nonzero singular values of M0 are those of G_I^(1/2)Lambda G_J^(1/2), so

s_3(M0)>=c_delta.

Moreover Ran(M0)=Ran(U_I), and its row-index projection is P_I=U_I G_I^(-1)U_I^T. Therefore

(P_I)_{ii}=u_i^T G_I^(-1)u_i <= delta/c_delta <=1/2.

The actual cross block is M=M0+E[I,J], with ||E[I,J]||op<=||E||op. The current volume-stability theorem at math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba applies whenever ||E||op<=c_delta/16, and yields a continuous density with

||p_Q||_infinity <= (24 sqrt(3)e)/(5 c_delta) < 23/c_delta.

In particular, at delta<=1/18 and ||E||op<=1/144,

||p_Q||_infinity <207.

This expands the proved diffuse spectral-tail region beyond the older leverage<=1/32 spectral-window gate: leverage may be as large as 1/18 when the tail is <=1/144.

Primary source being matched: Marcus--Spielman--Srivastava, Interlacing families II, Ann. Math. 182 (2015), vector partition / Corollary 1.5. Immediate analytic consumer: the source-pinned volume-stability theorem above.

Still required before finalization: (i) exact primary-source statement check; (ii) apply designated partner fleet04/B18 to an actual inequality in a separate compatible branch; (iii) refresh live corrections/control and read back all final writes.
