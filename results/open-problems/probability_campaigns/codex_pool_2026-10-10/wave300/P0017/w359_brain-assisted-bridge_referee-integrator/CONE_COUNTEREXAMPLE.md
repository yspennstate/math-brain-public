# P0017: an isotropic log-concave measure with unbounded conditional variance

Owner campaign derivation by w359, 2026-10-10. Independent reviewer: w362, pending. This refutes a proposed bridge, not KLS. No novelty claim.

Let (S,Y) have Lebesgue density p(s,y) = (1/2) exp(-s) on the convex cone s >= 0, |y| <= s, and zero elsewhere. Integrating out y gives p_S(s) = s exp(-s), so S has Gamma(2,1) law. The density is log-concave: its negative log-density is affine on a convex support and +infinity outside it.

Set X = (S-2)/sqrt(2) and Z = Y/sqrt(2). The transformed joint density is exp(-(2+sqrt(2)x)) on x >= -sqrt(2), |z| <= x+sqrt(2). The Jacobian is 2, so the normalization is exact.

Integration by parts gives integral_0^infinity s^k exp(-s) ds = k! for each integer k >= 0. Consequently E S = 2, E S^2 = 6, and Var S = 2. Conditional on S=s, Y is uniform on [-s,s], so E[Y|S] = 0 and E[Y^2|S] = s^2/3. Thus E X = E Z = 0, Var X = Var Z = 1, and Cov(X,Z)=0. The joint law is isotropic.

For every x > -sqrt(2), Z given X=x is uniform on [-a,a], with a=x+sqrt(2). Therefore Var(Z|X=x) = a^2/3. Testing the conditional Poincare inequality on g(z)=z shows C_P(law(Z|X=x)) >= a^2/3. For every M>0, this exceeds M on the positive-probability set S>sqrt(6M). Its probability is (1+sqrt(6M)) exp(-sqrt(6M)) > 0. Hence no finite essential upper bound for these conditional Poincare constants follows from full isotropy and log-concavity, even in dimension 2.

There is a second exact failure. Take f(x,z)=z^2. Its conditional mean is m(x)=a^2/3 and m'(x)=2a/3, whereas E[partial_x f(X,Z)|X=x]=0. Thus the identity d/dx E[f(X,Z)|X=x] = E[partial_x f(X,Z)|X=x] used in product tensorization is false here. Movement of the conditional law contributes a term; the product hypothesis cannot be replaced by zero covariance.

The cone has a nonsmooth boundary, which is allowed in the full log-concave KLS class. This example does not address any strengthened assertion restricted to a fixed smooth potential with a quantitative uniform convexity lower bound. It also does not rule out weighted or averaged conditional arguments that explicitly control the changing conditional law.

NEXT: Independently audit normalization, covariance, positive-probability fibre blowup, and the conditional derivative identity; then retain the obstruction as a draft refuted-route node.
