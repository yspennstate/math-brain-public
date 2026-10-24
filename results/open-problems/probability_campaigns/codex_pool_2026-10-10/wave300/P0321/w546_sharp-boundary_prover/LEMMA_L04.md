# L04: logarithmic angle variance alone does not force sixfold decay

Let g be the anchored Gaussian field in L03, and set h=2pi/6. Let V and U be independent, uniform on [0,h), and independent of g. Define q(x)=h floor((g(x)+V)/h), and theta(x)=U+q(x). Since g(0)=0, q(0)=0 almost surely.

Then exp[i6(theta(x)-theta(y))]=1 for every x,y and every outcome. Consequently the sixfold correlation is identically 1 and the one-point sixfold mean is zero. Nevertheless, for r=|x| tending to infinity,

Var[theta(x)-theta(0)] = (1/(pi beta K)) log r + O(1).

More precisely, for EVERY x,y, with v(x-y)=Var[g(x)-g(y)],

v(x-y) <= Var[q(x)-q(y)] <= v(x-y)+h^2/4.

Proof of the variance bounds: condition on the entire Gaussian field. The offset W=(V+g(y)) modulo h is uniform. Writing (g(x)-g(y))/h=n+t with n integer and 0<=t<1, the q increment is h*n with probability 1-t and h*(n+1) with probability t. Thus its conditional mean is g(x)-g(y) and its conditional variance is h^2 t(1-t). The law of total variance gives the exact identity Var[q(x)-q(y)]=v(x-y)+h^2 E[t(1-t)], which proves the bounds. Apply L03 for the logarithmic asymptotic. Every q difference is an integer multiple of h, so its sixfold exponential is exactly 1. Also E exp(i6U)=0, proving the one-point assertion.

The quantized field q has STATIONARY INCREMENTS, despite being non-Gaussian. Indeed, for a shift a, W_a=(V+g(a)) modulo h is uniform conditionally on the entire Gaussian field. The identity q(x+a)-q(a)=h floor((g(x+a)-g(a)+W_a)/h), together with stationary increments of g, proves equality of all finite-dimensional increment laws under translation. The physical sixfold phase exp(i6theta(x)) is constant in x and hence stationary.

Thus the proposed implication 'stationary angle increments with logarithmic variance imply algebraic decay of the sixfold characteristic function' is false without a Gaussian law or suitable characteristic-function control. This is an abstract random-field counterexample, not a Riesz Gibbs configuration or a refutation of P0321. The source's microscopic target needs additional structure.

This strengthens the prior mixture warning: knowing the second moment of an angle lift does not determine the order observable, which is periodic. No conditional bounds were multiplied, and no independence between spatial increments was assumed.

Reviewer: w548 pending. No novelty claim.
