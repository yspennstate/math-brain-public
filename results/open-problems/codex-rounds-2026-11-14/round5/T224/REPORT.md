VERDICT: PARTIAL loss-decay-only polynomial weak rates for one-dimensional output feature spans

The round 4 result holds in its stated scope. An independent velocity subtraction and concentration calculation reproduce its constants, and both inherited audits pass. The new step proves a polynomial weak rate from the slow loss envelope alone for bounded smooth features whose outputs lie in one affine line. This replaces the previous extra global curvature condition with a restriction on the feature span.

Let \(\mathcal H=L^2(P_X)\), \(\phi(w)=b+u\psi(w)\), \(\|u\|=1\), \(|\psi|\le A\), \(|\nabla\psi|\le B\), and \(\|D^2\psi\|\le M<\infty\). The parameter dimension is arbitrary. Use fixed output coefficients, exact Euclidean population gradient flow, and iid initialization from the mean-field initial law. If \(L_t\le C(1+t)^{-c}\), then PROOF.md proves, for every \(m\ge1\),

\[
 \boxed{\displaystyle
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|_{\mathcal H}^2
 \le \bigl(4A^2\max\{1,B^4\}+6C\bigr)m^{-c/(c+2)}.}
\]

This applies to every \(c>0\), including \(0<c<2\), with no square-root-loss integrability or residual-curvature hypothesis. Loss convergence forces the target into the same closed affine line. The prefactor is polynomial in \(d\) when \(A,B,C\) are. Neither this exponent nor any exponent for the full problem is claimed sharp.

The deterministic estimate behind the theorem is

\[
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le \frac{4A^2(1+B^2T)^2}{m}+6L_T,\qquad T\ge0.
\]

All neurons follow the autonomous gradient-ascent flow of \(\psi\), evaluated at a common scalar clock. The population and empirical feature averages are nondecreasing, \(B^2\)-Lipschitz functions of that clock. Their clock difference satisfies \(|\tau_m(t)-\tau(t)|\le\int_0^t|\zeta_s|ds\), where \(\zeta_s\) is an iid sampling fluctuation at the deterministic mean-field clock, with \(\mathbb E\zeta_s^2\le A^2/m\). Thus the finite-time comparison grows quadratically in time without an exponential curvature factor. Loss monotonicity controls later times, and \(T=m^{1/(c+2)}-1\) gives the bound.

The proof includes a source-admissible example with \(X=1\), \(Y=\pi/2\), \(\sigma=\arctan\), and \(\rho_0=(\delta_0+\delta_1)/2\). Its exact autonomous flow satisfies \(Q(\Psi_s(z))=s+Q(z)\), \(Q(w)=w+w^3/3\). Two independent derivations give

\[
 L_t\sim\frac1{2\sqrt t},\qquad
 H(T)\sim\frac{\sqrt6}{4}T^{3/4}.
\]

Here \(H\) is exactly the global integrated negative residual curvature from the prior reports. Its logarithmic bound fails, and the square-root loss is nonintegrable. The new theorem gives \(O(m^{-1/5})\) for this example. This is an application, not a weak-error lower bound. Along its realized nonnegative trajectories the curvature has a favorable sign, so a localized curvature proof could also apply.

Verification commands, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T224/audit_concentration.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T224/audit_cancellation.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_scalar_clock.py
```

All pass. The new audit checks 500 autonomous-flow identities, six exact ordered-sample variances, 6,000 scalar comparison intervals, 95 finite-neuron flow cases with 401 time points each, 500 exact prefactor checks, and six exact exponent balances. Raw particle equations and separately integrated clocks agree within \(4.99\times10^{-11}\). Cases include stationary mean-field output with finite clocks moving in opposite directions. These are finite-time and algebra checks; the all-time statement is proved analytically. Actual nice was 20, peak RSS below 18 MB, and each script finished in under one second. Details and outputs: LOG.md, scalar_clock_results.json, concentration_results.json, cancellation_results.json.

The literature check, completed within five minutes, found no later settlement. Margalit Glasgow and Joan Bruna's [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3), revised 11 November 2026, still treats \(c=2\) in Remark 6 and leaves slower decay open in Section 6. No SOLVED_ELSEWHERE.md was created. The background paper opened was Song Mei, Andrea Montanari, and Phan-Minh Nguyen, [arXiv:1804.06561](https://arxiv.org/abs/1804.06561). No literature-priority claim is made.

What failed or remains uncertain: a time-independent \(O(1/m)\) scalar bound does not follow from the clock comparison, which retains accumulated forcing. For general output spans, multiple feature-gradient fields need not admit a common scalar clock. The proof therefore does not settle the original question, construct a counterexample, establish necessity of a stability condition, or identify a sharp exponent. Scalar-valued regression on many inputs is not automatically within the one-dimensional output-span assumption. Unbounded features, trained output coefficients, sample error, and time discretization remain outside this result.

Next worker: test the two-direction extension when the two feature-gradient fields commute. The concrete missing lemma is whether their joint autonomous flow produces a globally defined feature-average map with a positive semidefinite Jacobian, permitting the same contractive clock comparison in two dimensions. Then isolate the commutator term when the fields do not commute; that is where the scalar proof ceases to apply to general T224.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 08:42 Asia/Tbilisi (first captured shell clock).
