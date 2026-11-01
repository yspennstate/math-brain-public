# PROB20-16 canonical additive correction for the 22:24 stuck report

This file supersedes the earlier correction artifact from the same run, whose displayed matrices accidentally repeated two notation typos. The immutable mathematical report is not overwritten.

The intended corrections are unambiguous in plain text:

1. Equation (3.2):
   `W(u) = sqrt(a*c*rho) * [[2*u1, u2], [u2, 0]]`.
   In particular, the lower-left entry is `u2`, not `nu2`.

2. Section 4 conditional Bernoulli coordinates:
   `u = x + s/(1-y) = P(X1=1 | X2=0)` and
   `v = x - s/y = P(X1=1 | X2=1)`.
   The first variable is `u`, not `nu`.

3. For the proposed next special case `c=1/2`, define
   `W_half(u) = (sqrt(rho)/2) * [[2*u1, u2], [u2, 0]]`.
   Since `(0.5*S0^{-1} + 0.5*S1^{-1})^{-1} = 2*(S0^{-1}+S1^{-1})^{-1}`,
   the exact blocker is
   `8 * <W_half, (S0^{-1}+S1^{-1})^{-1} W_half> >= 2 * u^T G u`,
   equivalently
   `4 * <W_half, (S0^{-1}+S1^{-1})^{-1} W_half> >= u^T G u`.

The exact general blocker (3.1)/(7.1), the B1 channel identities, the B6 infinitesimal determinant identity, and the B15 rational route-failure certificate are unchanged.
