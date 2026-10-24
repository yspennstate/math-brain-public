# HARD7-05 route note — polynomial quasimode plus Kato–Temple

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

This note is intentionally written before checker construction.

The inherited six-cycle certificate controls `tr K^6`, and the preceding run spent part of that trace budget by lower-bounding subleading Ritz eigenvalues. A more direct route is to use the same trace bound only to *separate* the top eigenvalue from the rest, then approximate the top eigenfunction by a low-degree polynomial quasimode and invoke Kato–Temple.

For `K=1_{(0,∞)} P_r 1_{(0,∞)}`, `r=287831/500000`, take

`f(x)=(100000+75665 x-2316 x^2) 1_{x>0}`.

Write

`mu=<f,Kf>/<f,f>` and `eps^2=||(K-mu)f||^2/<f,f>`.

The key observation is that `eps^2` can be evaluated rigorously without numerical quadrature. Conditional on the middle site of a three-step stationary AR(1) chain, the two endpoints are independent. Hence `<f,K^2 f>` becomes a one-dimensional integral of the square of a conditional truncated Gaussian moment. For degree two this closes under three families

`U_m=∫_0∞ y^m phi(y) Phi(ay)^2 dy`,
`V_m=∫_0∞ y^m phi(y) Phi(ay)phi(ay) dy`,
`W_m=∫_0∞ y^m phi(y) phi(ay)^2 dy`,

with `a=r/sqrt(1-r^2)`. `U_0` is the exact trivariate Gaussian orthant probability, the other `U_m` follow by integration by parts, `V_m` reduces after scaling to ordinary one-sided Gaussian moments with `Phi(rz)`, and `W_m` is elementary.

The three numbered moves for this run are:

- **B16 (compute small cases):** compute degree 0,1,2 polynomial compressions and inspect whether the residual collapses before increasing degree. It does: the degree-two residual is already about `8e-6` after normalization.
- **B19 (make it an algorithm):** express every `G`, `M=<.,K.>`, and `N=<.,K^2.>` entry through exact recurrences and rational interval arithmetic; no theorem step uses floating quadrature.
- **B30 (one spectral scale at a time):** use the inherited sixth trace only to certify a coarse `lambda_2<0.31`, then isolate the top spectral scale with Kato–Temple instead of trying to resolve the whole spectrum.

Counterexample-first check: I first tried to break the route by seeing whether projection leakage of `Kf` off the polynomial space is too large. Direct exploratory one-dimensional integration gives a normalized residual near `7.99e-6`, small enough that a coarse spectral separation should still improve the persistence exponent. The numerical value is route-finding only; the next artifact must certify it by exact rational interval arithmetic before any bound is claimed.
