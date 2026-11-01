# Independent reconstruction of two A096 claims

All entropy and KL use bits. Boolean signs live on physical, finite uniform cubes. This review accepts A096-NONFLAT-POINT-QUOTIENT-REMAINDER@1 and A096-CHILD-BANK-PRICE-FIVE-OBSTRUCTION@1 at their original scope, without repairing either statement. No FEI theorem is inferred.

## Arbitrary-core reconstruction

Put delta=2^-d, beta_T=hat b(T), a_V=hat g(V), c=b-2*1_0, where b(0)=1. Direct character averaging gives hat F(T,V)=beta_T*1[V=0]+delta*(a_V-1[V=0]). The physical gate influence is e_i=delta E_i, and core influence is I_Y=((1+a_0)I(b)+(1-a_0)I(c))/2. These equalities hold regardless of which incident point edges are destroyed.

On the complete derivative row indexed by masks V not containing i, mu(T,V)=hat F(T,V+i)^2/e_i and r(T,V)=hat F(T,V)^2+hat F(T,V+i)^2. Both sums equal one. When V is nonempty, each core conditional law is uniform. At V=0 the derivative core law is uniform, the derivative cell mass is delta*a_i^2/E_i, and the reference cell mass is rho=1-delta+delta*(a_0^2+a_i^2). Its core conditional law is q(T)=((beta_T+delta*(a_0-1))^2+delta^2*a_i^2)/rho. Consequently the KL chain rule gives precisely L_i=delta*a_i^2*D(U||q). Zero a_i gives zero loss, including cells where conditioning would otherwise be undefined. Retaining (V,beta_T) instead preserves the likelihood ratio on every cell and loses zero KL.

If a_i is nonzero, rho<=1 and q(T)>=delta^2*a_i^2/rho. Thus U(T)/q(T)<=1/(delta*a_i^2), and L_i<=delta*a_i^2*(d+log2(1/a_i^2)). A physical Boolean derivative is 0 or +/-1, giving |a_i|<=E_i. For u=|a_i|, u^2 log2(1/u^2)=2u*[u ln(1/u)]/ln2 <=2E_i/(e ln2). Summing yields delta*d*W1+(2/(e ln2))*I_X, where I_X=delta I(g).

Every nonempty proper d-cube vertex set has at least d boundary edges: split into two fibers; two nontrivial fibers give 2(d-1)>=d, one nontrivial fiber gives d-1 internal plus a crossing edge, and two different constant fibers give 2^(d-1)>=d. The d=1 base is direct. Therefore a nonconstant sign has influence >=2d delta. If both b and c are nonconstant, delta*d*W1<=I_Y/2 by Parseval W1<=1. If b is constant, b=+1 and I_Y=d delta*(1-a_0); if c is constant, c=-1 and I_Y=d delta*(1+a_0). In either case W1<=1-a_0^2 proves delta*d*W1<=2I_Y. Finally e>65/24>8/3 by its positive exponential series, and ln2>2/3 by the first term of the atanh series with z=1/3. Hence 2/(e ln2)<9/8. All original bounds follow; no terminal reserve availability follows.

## Actual child-bank reconstruction

Take b=-1+2*1_0, c=-1 and dictator gate. Then F is a point sign on d+1 bits with gate influence e=delta. The reference exceptional core probabilities are q(0)=z=((1-delta)^2+delta^2) and q(T)=2delta^2 for T!=0. Thus

D0=(1-delta)(d-1)+delta*log2(delta/z), L=delta D0.

Since delta<=z<=1, D0<=d-1<=d and D0>=d-1-(2d-1)delta>=d-2. The last bound holds for every integer d>=2 because (2d-1)/2^d<=1 (its consecutive ratio is (2d+1)/(2(2d-1))<=1 for d>=2).

The core has constant Fourier mass p0=(1-2delta)^2 and 2^d-1 other masses 4delta^2. Therefore H(b)=eta(p0)+4delta(1-delta)*(2d-2), I(b)=2d delta. Using -p ln p<=1-p and ln2>1/2 gives eta(p0)<=8delta; hence H(b)<=8d delta=4I(b). This also proves the rate-four bound for the root point sign. Its actual averaged child slack obeys

S4=4delta+4(d-1)delta^2-eta(p0)/2, 0<=S4<=5delta.

The upper bound uses (d-1)delta<=1/4, proved by the same consecutive-ratio argument. For arbitrary real C in [4,5), S_C=S4+(C-4)d delta, so (L-S_C)/e >=(5-C)d-7 tends to infinity. At C=5, S5=S4+d delta>=d delta>=L. This proves the exact asymptotic threshold for this loss alone.

Independent tensor q=-1+2*1_0 on 2d coordinates has I(q)=4d delta^2 and H(q)<=4I(q). Fourier masses of products multiply, so entropy and influence add and complete row laws acquire the same independent factor. L and e remain unchanged, both physical children become nonconstant, and their slack is S'_C=S_C+C I(q)-H(q). The original deficit lower bound weakens by at most 4C d delta, which tends to zero. At C=5 the added slack is nonnegative. This reconstructs the full nonconstant-child continuation with no missing terminal entropy.

## Separate exhaustiveness theorem and finite certificate scope

For fixed d,r, enumerating the odd truth-table masks for b and all truth-table masks for g is exhaustive for the stated hypothesis b(0)=1: bit zero is exactly the prescribed marked sign, and every other output is free. Our domain d=1,2,3 and r=1,2 therefore has (2+8+128)*(4+16)=2760 labeled cases. No symmetry quotient is used. Direct character sums cover every spectral atom and direct edge comparisons cover every physical influence. This finite domain is exhaustive only for this regression application.

The all-dimensional application instead follows from the analytic reconstruction above: the only dimension-dependent inequalities reduce to the cube minimum cut and the two monotonically decreasing integer sequences (2d-1)/2^d and (d-1)/2^d. Their initial values at d=2 and the proved consecutive ratios exhaust their infinite domains. Arbitrary gate dimension is eliminated by Parseval and the Boolean derivative bound, not by a finite gate census. The continuum maximum u ln(1/u)<=1/e is proved by differentiation, including endpoints by continuity. No unstated theorem upgrades the small truth-table census to all Boolean functions.

For log certificates, write x=2^k y, 1<=y<2, z=(y-1)/(y+1). The lower bound for ln y is 2 sum_{j=0}^{23} z^(2j+1)/(2j+1), and its tail is at most 2 z^49/(49(1-z^2)). Divide by rigorous positive ln2 bounds and add k. This is exact rational arithmetic, including signed log values. It certifies the finite inequalities and interval replay of the complete KL chain rule; the chain rule itself is proved by the exact conditional probabilities above.

## First unsupported universal line

The unsupported step is that the actual retained reference price plus conditional loss can be paid from one genuinely unused certified child bank, uniformly for arbitrary Boolean functions. Root influence quotas do not establish this. The threshold-five obstruction rules out the specified same-price loss-only policy at every C<5, including nonconstant physical children. It does not rule out price >=5 or a sufficient signed-amplitude partition and does not imply unbounded H/I.
