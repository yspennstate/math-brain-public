# The exact-rank-three third disjoint volume is a two-base packing probability

Let A=U Lambda U^T have exact rank three, U^TU=I_3, and Lambda invertible. Define
V3(A)=sum_{|S|=|T|=3, S intersect T=empty} det(A[S,T])^2,
with ordered pairs (S,T). For every pair of disjoint triples,
det A[S,T]=det(Lambda) det U_S det U_T.                (1)
Cauchy--Binet gives sum_{|S|=3} det U_S^2=1. Thus p(S)=det U_S^2 defines a probability law on physical row bases (the rank-three projection determinantal law), and
V3(A)/det(Lambda)^2
 =P_{S,T iid p}(S intersect T=empty)
 =E_{S~p} det(I_3-U_S^T U_S).                          (2)
The last identity follows by Cauchy--Binet on the complementary frame U_{E\S}, whose Gram matrix is I_3-U_S^TU_S.

Equation (2) connects the aggregate analytic third-minor currency to two disjoint physical row bases. In particular V3(A)=0 iff no two disjoint bases exist, so the companion matroid classification gives a single physical coloop under N3(1/64). If V3(A)>0 is very small, (2) is an exact quantitative measure of *average* base-packing failure. It does not by itself prove the desired stability statement that there is a set S of small total frame energy whose deletion leaves one coloop: the eigenvalues of Lambda may be arbitrarily unequal, and a bound on the average determinant need not control a prescribed geometric flat. The near-coloop receiver in REPORT.md pays a low-energy deletion once such an S is certified, but does not extract S from V3 alone.

All determinants are formed on original-coordinate rows and columns. No rotated coordinate is treated as an independent random variable.