VERDICT: PARTIAL improved curvature-dependent polynomial weak rate using an output cancellation

The earlier bounded-feature Euclidean result holds. An independent direct coupling derivation recovers its main inequality, and rerunning its audit reproduces its results.

The new result improves its finite-horizon factor from \((1+T)^4\) to \((1+T)^2\). With exactly the same notation and assumptions—bounded smooth features \(\phi\), bounded first and second derivatives with constants \(A,B,M\), fixed output coefficients, population gradient flow, and iid initialization—PROOF.md establishes

\[
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le \frac{4K_*(1+T)^2e^{2H(T)}}m+6L_T,
 \qquad K_*=2A^2+4A^2B^2+2M^2A^4.
\]

Here \(H\) is the integrated positive part of the worst negative mean-residual curvature, as defined precisely in PROOF.md. Thus, if

\[
 L_t\le C(1+t)^{-c},\qquad H(T)\le h_0+\kappa\log(1+T),
\]

then for \(m\ge2^{c+2+2\kappa}\),

\[
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le (4K_*e^{2h_0}+6C)m^{-c/(c+2+2\kappa)}.
\]

The previous exponent was \(c/(c+4+2\kappa)\). For example, \(c=1,\kappa=0\) improves from \(1/5\) to \(1/3\). The new constant is polynomial in the feature bounds; the old constant included an exponential in those bounds. Consequently the prefactor is polynomial in \(d\) if \(A,B,M,C\) are, \(h_0=O(\log d)\), and \(\kappa\) is dimension independent. Neither exponent is claimed sharp.

The new step keeps the negative output-error square in the exact paired-particle energy identity. For squared RMS parameter discrepancy \(y\), iid output fluctuation norm \(\eta_t\), and residual-curvature bound \(h(t)\), completing the square gives

\[
 y'\le2h(t)y+\eta_t^2+\frac{M^2}{4}y^2.
\]

A reciprocal Riccati comparison, a first-moment bound on \(\int_0^T\eta_t^2dt\), and the bounded output cap control the exceptional initializations. Population-loss monotonicity handles all later times. The conclusion is the requested output norm with the supremum outside expectation, and makes no empirical-measure Wasserstein claim.

Verification commands, run from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114/briefs/T224/audit.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_cancellation.py
```

Both passed. The new audit checks 600 bounded-feature vector-field identities, 300 exact rational cancellation cases, 300 exact scalar Riccati solutions, 300 exact constant cases, and 18 exact exponent balances. Maximum direct-identity error was \(7.11\times10^{-15}\); maximum completed-square error was \(3.55\times10^{-15}\). An exact local equality case independently checks the Riccati coefficient. These supplement the proof, rather than simulate infinite-time convergence. Actual nice was 20, peak RSS below 17 MB, and each audit finished in under one second. Outputs are audit_results.json and cancellation_results.json; commands and details are in LOG.md.

The literature check took under five minutes and found no later settlement. Margalit Glasgow and Joan Bruna, *Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks*, [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3), remains the current source revision, dated 11 November 2026. Remark 6 covers \(c=2\); Section 6 still leaves \(c<2\) open. No full-settlement SOLVED_ELSEWHERE.md was created.

What failed or remains uncertain: inserting only the slow loss envelope into this improved estimate still yields the earlier logarithmic rate \((\log m)^{-2c/(2-c)}\), rather than a polynomial width rate. The extra curvature hypothesis remains sufficient, with no necessity claim. There is no counterexample and no sharp exponent for the original problem. The proof retains the earlier limitations: unbounded activations, sphere constraints, trained output coefficients, finite training data, and discretization are not covered. No literature-priority claim is made for the improved bound.

Next worker: exploit the same exact identity before discarding the negative output square, to seek an estimate on output error that avoids controlling the global parameter discrepancy on rare initializations. A concrete alternative is to replace Markov's exceptional-event estimate with a concentration bound for the time-integrated iid fluctuation; that may sharpen the conditional polynomial rate, but would not by itself remove the exponential dependence on \(H(T)\). To settle decay alone, a further output-level stability estimate or an admissible output-error counterexample is still needed.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 03:32 Asia/Tbilisi (recorded shell clock).
