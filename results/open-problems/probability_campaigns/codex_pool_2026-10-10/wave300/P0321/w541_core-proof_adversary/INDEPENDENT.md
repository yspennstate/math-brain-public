# P0321 independent obstruction, saved before reading the paired proof

2026-10-10. Source anchor recovered: Mathieu Lewin, arXiv:2202.09240v2. Exact intake statement still being recovered. This derivation has not used w540's mathematical artifacts. Reviewer: w542, pending.

Fix a cutoff Lambda > 0, coefficients aT > 0, aL >= 0, and 0 <= s < 2. Define a real centered Gaussian vector field u with stationary increments by its spectral matrix on 0 < |k| <= Lambda:

Q(k) = aT |k|^(-2) PT(k) + aL |k|^(-s) PL(k),

where PL(k) = kk^t/|k|^2, PT = I - PL, and integration uses d^2k/(2 pi)^2. The field is defined modulo an additive constant. Its increments exist because (1-cos(k.x)) = O(|k|^2) near zero. The cutoff also makes its derivatives well-defined in mean square. This is an explicitly stipulated Gaussian elastic surrogate; deriving Q from a particle Gibbs measure is a separate, unproved input.

For completeness, the covariance of u(x)-u(0) and u(y)-u(0) is the integral of [cos(k.(x-y))-cos(k.x)-cos(k.y)+1]Q(k). It is positive semidefinite: the bracket is the sum of the two real feature products (cos(k.x)-1)(cos(k.y)-1)+sin(k.x)sin(k.y). Multiply these features by a measurable square root of Q and use two independent real Gaussian noises. Their square integrability at zero follows from the same increment bound. This constructs the real Gaussian finite-dimensional laws and shows that no stationarity of u itself is being assumed.

For nonzero q and x = r e, Gaussianity gives the exact identity

CT(q,x) := E exp(i q.(u(x)-u(0))) = exp(-Vq(x)/2),
Vq(x) = 2 integral (1-cos(k.x)) q^t Q(k) q d^2k/(2 pi)^2.

Let alpha be the angle between q and e. Polar integration of the transverse part gives

Vq,T(r e) = (aT |q|^2/(2 pi)) integral_0^(Lambda r) [1-J0(t)-cos(2 alpha) J2(t)] dt/t.

The angular identity follows by expanding sin^2(theta-alpha) and integrating cos(t cos(theta)) over the circle. The integrand is O(t) at zero. For t >= 1, the Bessel terms divided by t are absolutely integrable (J0(t), J2(t) = O(t^(-1/2))). Thus the integral equals log r + O(1). The longitudinal integrand is integrable at k=0 since s<2 and bounded above by a constant independent of r. Consequently

An elementary oscillatory bound also suffices here without assuming a Bessel asymptotic formula. For a smooth angular weight a(theta)=sin^2(theta-alpha), remove neighborhoods of radius delta=t^(-1/2) of the stationary points of cos(theta). Their contribution is O(delta). On the complement integrate exp(i t cos(theta)) by parts using derivative -i t sin(theta). Boundary terms are O(1/(t delta)); the differentiated weight contributes O(log(1/delta)/t), and differentiating 1/sin(theta) contributes O(1/(t delta)). Thus the angular cosine integral is O(t^(-1/2)), uniformly in alpha, which makes its quotient by t integrable. Its nonoscillatory angular integral is exactly pi. The same log coefficient follows directly.

Vq(r e) = (aT |q|^2/(2 pi)) log r + O(1),
CT(q,r e) = exp(O(1)) r^(-aT |q|^2/(4 pi)).

In particular there are positive direction-dependent constants c,C and r0 with c r^(-eta) <= CT <= C r^(-eta) for r >= r0, eta = aT |q|^2/(4 pi) > 0. CT cannot satisfy CT <= A exp(-r/xi) for finite A,xi at every large r: the lower bound divided by that exponential tends to infinity.

Define the linearized orientation theta = (partial_1 u_2 - partial_2 u_1)/2. Its spectral density is exactly aT/4 on the cutoff disk, because the longitudinal component is annihilated. Hence

vtheta := Var(theta(0)) = aT Lambda^2/(16 pi),
c_theta(x) = integral exp(i k.x) (aT/4) d^2k/(2 pi)^2 -> 0,
C6(x) := E exp(i 6(theta(x)-theta(0))) = exp[-36(vtheta-c_theta(x))] -> exp(-36 vtheta) > 0.

C6 here is an uncentered two-point function. The centered correlation subtracts |E exp(i6 theta)|^2 and tends to zero. Neither quantity has been identified with a microscopic particle observable.

The covariance tends to zero by the Riemann-Lebesgue lemma; no independence assumption is used. Neither theta nor exp(i6 theta) is automatically the Delaunay bond observable of the gas.

This proves a special-case obstruction: this Gaussian displacement surrogate has algebraic positional correlations and a positive orientational plateau. Its positional correlation is not exponentially decaying, so the Gaussian calculation alone cannot establish an intermediate phase with short-range positional order. It is not a counterexample to hexatic existence in a Riesz particle gas. Defects, their weights, and a justified observable transfer remain necessary in any route using this surrogate.

NEXT: Match the exact source's phase definition, then audit w540's main inference against this independent calculation.
