# One planar bank with exact affine leakage projection

Let H have probability density at most one and be independent of two independent light banks Y1=(L1,V1,P1) and Y2=(L2,V2,P2). Assume (L1,V1) has joint density at most M and

P1=alpha L1+eta V1

exactly, with alpha,eta arbitrary real numbers. Set L=L1+L2, V=V1+V2, P=P1+P2. For arbitrary beta,epsilon, the quadratic

Q=2HL+beta L^2+V^2+2 epsilon LP

has density bounded at every target by 1/2+4sqrt(2) M, uniformly in beta,epsilon,alpha,eta and the distribution of Y2. There is no hub self-square aH^2 in this theorem.

Proof. Condition on the whole independent bank Y2=(l2,v2,p2). Then

P=alpha L+eta V+c,  c=p2-alpha l2-eta v2.

Consequently

Q=2(H+epsilon c)L+(V+epsilon eta L)^2+
   (beta+2epsilon alpha-epsilon^2 eta^2)L^2.

The translated hub H+epsilon c remains independent of the first bank with density cap one. The conditional pair (L,V+epsilon eta L) is an affine image of (L1,V1) under a determinant-one shear, so its joint density is at most M. The beta-uniform two-light coarea lemma for 2HL+V^2+beta L^2 gives 1/2+4sqrt(2) M. Average over Y2.

The exact relation P1=alpha L1+eta V1 is the gate. A transverse term from bank1 correlated with (L1,V1) is not covered. If a separate transverse term N is independent of (L1,V1,Y2,H), it can be conditioned as an extra variable and the same argument applies. Arbitrary original-coordinate affine components outside the displayed variables and an added aH^2 are outside this claim. The unrestricted product-source density theorem remains open.
