# P0013: two nonnegative defects (proof reduction, pending w347)

Assume a graph G on n vertices has complement-invariant law, and write X=theta(G)/sqrt(n), Y=theta(complement G)/sqrt(n). The standard theta-product inequality gives XY>=1. Put R=sqrt(XY) and Z=(log X-log Y)/2. Then X=R exp(Z), Y=R exp(-Z), and complement symmetry gives

E theta(G)/sqrt(n)-1 = E(R-1)+E[R(cosh(Z)-1)].

Both terms on the right are nonnegative. Therefore the desired expectation asymptotic is equivalent to both defect expectations tending to zero. This distinguishes product tightness from complement imbalance; concentration of Z alone does not control R or the exponential tail. Finite n ensures integrability because 1<=theta(G)<=n.

The equation follows by averaging E X=E Y and using (X+Y)/2=R cosh Z. No estimate that makes either defect vanish for G(n,1/2) is proved here. It continues P0013-A001 and generalizes the exact-product circulant reduction in P0014-A001. It is not a claimed solution of Conjecture 17.
