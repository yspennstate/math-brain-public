# L01: an integrable angular spectrum cannot produce algebraic hexatic decay

Assume a centered stationary real Gaussian field theta on R^2 has even nonnegative spectral density f in L1(R^2), with

R(x) = integral exp(i k.x) f(k) d^2k/(2pi)^2.

For real m != 0, the increment theta(x)-theta(0) is Gaussian of variance 2(R(0)-R(x)). Therefore

C_m(x) = E exp(i m(theta(x)-theta(0))) = exp[-m^2(R(0)-R(x))].

By the Riemann-Lebesgue lemma R(x) tends to zero at infinity. Consequently C_m(x) tends to exp[-m^2 R(0)], which is strictly positive. This proves the asserted special case.

Sharp boundary to check next: f(k) proportional to |k|^-2 in two dimensions is not integrable at zero. Only its increments define a Gaussian field; these increments can have logarithmic variance and an algebraic exponential correlation.

Application under investigation: the curl of a defect-free transverse displacement with covariance proportional to P_T(k)/|k|^2 has an integrable angular spectrum after an ultraviolet cutoff. The microscopic Riesz-to-elasticity bridge is not established. This lemma concerns the explicitly assumed Gaussian model, not the actual Gibbs gas.

Reviewer: w548 (pending). No independent check or novelty claim.
