VERDICT: PARTIAL uniform weak logarithmic rate and a sufficient curvature condition for polynomial rates

For Euclidean population gradient flow with fixed second-layer coefficients and bounded smooth features, PROOF.md proves

\[
\sup_{t\ge0}\mathbb E\|f_t^m-f_t\|_{L^2(P_X)}^2
\le \frac{4K(1+T)^4e^{2H(T)}}m+6L_T\qquad(T\ge1).
\]

Here the feature map and its first two derivatives have uniform bounds A, B, M, the explicit K is given in (4), and H(T) is the integrated positive part of the worst negative residual curvature, defined in (3). The initialization is iid from the mean-field initial law.

Consequently, for 0<c<2, the loss envelope alone gives

\[
\sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
=O_{A,B,M,C,c}\big((\log m)^{-2c/(2-c)}\big).
\]

A concrete sufficient extra hypothesis is

\[
H(T)\le h_0+\kappa\log(1+T).
\]

It gives an explicit polynomial bound with exponent c/(c+4+2kappa). If h0=O(log d), kappa is dimension independent, and the feature derivative bounds are dimension independent, the prefactor is polynomial in d (also allowing a polynomial loss-envelope constant C). Neither this exponent nor the logarithmic exponent is claimed sharp.

The proof retains the positive Jacobian-square term in the empirical-risk Hessian, controls the nonlinear coupling remainder by stopping at RMS discrepancy 1/T, and bounds the bad event using an integrated iid output fluctuation. Monotonicity of both population losses then controls all later times. The result is sup_t E error squared, not E sup_t error squared.

The source's Euclidean bounded-total-variation activation assumptions give bounded features and derivatives, so this includes that subclass. It does not include the population-data relaxation to unbounded activations, sphere-constrained dynamics, trained second-layer coefficients, sample error, or time discretization.

Literature check: the November 11 source revision already treats c=2 in Remark 6; see SOLVED_ELSEWHERE.md. The source authors are Margalit Glasgow and Joan Bruna, arXiv:2605.22010. The full problem was not found settled, so the session continued for c<2. This is a correction to endpoint coverage in the supplied status, not a claim that the source theorem is a new open problem.

Verification command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit.py
```

Output and data: audit_results.json; exact command and output summary: LOG.md. The audit passed 200 independent Hessian/coupling cases, 200 checks of the constant/stopping threshold, and 15 exact rational exponent balances. Maximum Hessian errors were 7.28e-8 from scalar-risk second differences and 1.51e-9 from gradient differences. These checks supplement the written proof; they are not an infinite-time simulation. The program uses only the Python standard library, runs in well under one second, and has negligible memory use. The inherited process priority was independently read as nice 20, despite the wrapper's harmless setpriority warning.

What failed or remains uncertain: no counterexample was constructed, and no polynomial rate was derived from slow loss decay alone. The curvature condition is sufficient and can be stronger than necessary. The constants and horizon threshold deteriorate as c approaches 2. There is no sharpness or necessity claim and no uniform estimate in c at that endpoint. The qualitative mechanism resembles truncation arguments already present in the source; no claim of literature novelty is made for this rate without a wider search.

Next worker: seek output-level cancellations beyond the global residual-curvature bound. Alternatively, build an admissible bounded smooth example with polynomial loss decay and enough accumulated negative curvature to amplify iid initialization fluctuations into output error larger than every inverse power of m. Parameter separation alone would not give the needed counterexample. A useful intermediate task is to replace the global supremum in h(t) by a rigorously controlled quantity along the sampled trajectories without introducing m-dependent constants.

Task: “push this problem forward by one checkable piece” — 2026-11-14 21:21 Asia/Tbilisi.
