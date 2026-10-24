# Final independent review of the T357 synthesis

Reviewer: B02. Date: 2026-10-24.

**Verdict: PASS for the scalar overconfidence theorem, its explicit common-regime corollary, and their integration and normalization in the final synthesis.** No unresolved mathematical correction remains in this review's scope. I independently checked the scalar proof, rather than relying on the other reviewers' verdicts. I checked the synthesis against the all-time theorem and the displayed finite-time recursion; this report does not claim to repeat the independent primary-source audits of the entire random-matrix/AMP input.

## Accepted versions

The following SHA-256 hashes were read directly from the filesystem after the requested amendments:

| Accepted file | SHA-256 |
|---|---|
| `fullproof/T357_THEOREM_AND_SYNTHESIS.md` | `7b773eba4446340893bd8e67a1397ba06b154bf79b9f89a348e68c1a93282d51` |
| `fullproof/b06_gaussian_overconfidence.md` | `b65ea33e7e0208b825f429f5369ac1fbd1e470803848356df749b7208fbcb532` |

The all-time theorem used for comparison is `fullproof/b02_uniform_time_GD.md`, hash `1102592bcfdc5b3b9b82476b7d6065b7f0c596f3f6b14b05d1362637f104483f`. It was independently audited by B05. The displayed finite-time recursion was cross-checked against `fullproof/b01_GD_state_evolution_check.md`, hash `077b6c8134a2780f4ad5132be70fe50ccdfccd7240d00a50b4ea775d1ea0338f`.

## 1. Normal mixture and strict single crossing

The representation
\[
W=2\sum_{j\ge1}E_j/j^2,\qquad L\overset d=\sqrt W N
\]
is justified: the positive series has finite expectation, its Laplace transform gives the convergent Euler product, and the resulting characteristic function equals that of standard logistic noise. The separate strict-support argument is necessary and correct. In particular, the tail of the positive series can be made small with positive probability independently of a finite initial block. Conditioning on that tail gives a positive finite density of \(W\) at every positive argument.

For the two scale distributions, the signed CDF difference is correctly
\[
N_c(u)=F_W(e^{2u}-s^2)-F_W(c^2e^{2u}).
\]
When \(0<c<1\), it is strictly negative before
\(u_c=\frac12\log(s^2/(1-c^2))\) and strictly positive afterward. For \(c\ge1\) it is strictly negative everywhere. The Stieltjes integration-by-parts sign is correct:
\[
F_s(e^t)-\sigma(ce^t)=\int K(t-u)N_c(u)\,du,
\qquad K(v)=e^v\varphi(e^v).
\]
Both boundary terms vanish, and \(\int K=1/2\) ensures absolute integrability.

For \(t_2>t_1\), the ratio
\[
\frac{K(t_2-u)}{K(t_1-u)}
=e^{t_2-t_1}\exp\!\left[-\tfrac12(e^{2t_2}-e^{2t_1})e^{-2u}\right]
\]
is strictly increasing in \(u\). Subtracting its value at \(u_c\) makes its sign agree with that of \(N_c\) everywhere except the crossing. This proves the strict integral inequality and the asserted direction of crossing. Choosing the scale that matches the CDF at any fixed positive point then proves strict increase of \(\operatorname{logit}F_s(x)/x\) for every pair of positive points. The derivative limit at zero and the dominated-convergence tail limit at infinity give the two stated endpoints. No unproved variation-diminishing or total-positivity assertion is used.

## 2. Risk optimum and the sign of overconfidence

The risk derivatives are valid by domination with the first two normal moments:
\[
R'(c)=\mathbb E[U(\sigma(cU)-g(U))],\qquad
R''(c)=\mathbb E[U^2\sigma'(cU)]>0.
\]
The derivative is negative at zero and has a strictly positive limit at positive infinity. Strict convexity therefore gives a unique positive global minimizer. The scalar crossing theorem places it strictly between \(4g'(0)\) and \(\beta k/(k^2+\tau^2)\), and identifies one strict error crossing \(u_*\).

Risk stationarity annihilates the error weighted by \(u\), whereas signed confidence error is the unweighted positive-half-line integral. Consequently
\[
\mathrm{OC}(c_*)=2\int_0^\infty
e(u)(1-u/u_*)\varphi_{k^2+\tau^2}(u)\,du>0.
\]
Both factors have the same strict sign away from \(u_*\), and the integral is finite. The identification with mean confidence minus classification accuracy is correct. The claim is **average** overconfidence: the same proof gives underconfidence in the far tails. Total variation transfers the bounded signed-OC test to the finite trained network; the separately available moment/risk argument handles cross-entropy. The scale minimizes first-step population risk, not risk over every training time or the full coefficient class.

## 3. The common weak-teacher regime really meets both theorems

In the RF model, \(k=a^2\mu_\beta\), \(\mu_\beta\le\beta/4\), and
\(k^2+\tau^2\ge\tau^2\ge v^2/(4\alpha\gamma)\). Under B06's explicit conditions,
\[
\beta<\log(3)/B\quad\Longrightarrow\quad
p_1>p_0/8\quad\Longrightarrow\quad C_*(\beta)\le C_0<\alpha/\gamma.
\]
Also
\[
0<c_*<\frac{\beta k}{k^2+\tau^2}
\le\frac{a^2\alpha\gamma\beta^2}{v^2}
<\frac{\gamma}{64L^2}
<\frac{\gamma}{32L^2}=\frac{\gamma}{2\Lambda}.
\]
Every inequality and normalization is correct. Choose any fixed \(\gamma>0\), then a fixed \(\alpha\) above the stated threshold, and then any fixed positive \(\beta\) below the two positive bounds. The resulting \(c_*\) is a fixed positive deterministic constant, independent of dimension. This is a nonempty open parameter regime, despite its conservative thresholds. It does not substitute a vanishing-step asymptotic for the fixed-step theorem.

Thus one and the same model has a risk-improving, positively overconfident first iterate and a positive calibration floor at every positive stopping time. The risk-constrained stopping observation is also valid: time zero has risk exactly \(\log2\), so any rule achieving a fixed improvement with probability tending to one must choose a positive time with probability tending to one. Such improvement is attainable by the first-step rule for any margin below its strict limiting risk gain.

## 4. Synthesis normalization and scope

- The update coefficient \(cd/(nm)\) is mean-loss GD with step \(cd/m\) in the raw coefficients \(b\), or step \(cd\) in \(w=\sqrt m\,b\). The limiting scale \(\lambda=c/\alpha\) is consistent.
- The query-free matrix recursion agrees with B01's displayed formulas. Evaluating its first stage gives \(A_1=ca^2\mu_\beta\) and both terms of the stated residual variance; no width, sample, or square-root factor is lost.
- The population-risk formula follows from \(\log(1+e^S)=\log(2\cosh(S/2))+S/2\) and Gaussian conditioning, yielding the term \(-\mu_\beta A\).
- The full-TV-norm convention is now explicit and agrees with the signed-measure calibration inequality.
- The requested notation collision is corrected: the synthesis uses \(A_0w^t\) for the matrix times a coefficient vector, while \(Q_t\) remains the scalar fresh-score variance. The normalized weight symbol \(w\) also avoids collision with the scalar Hermite coefficient \(a\).
- The main text now states that compatibility of the risk-optimal first step with the all-time regime is not automatic, and supplies the explicit common-regime corollary. The finite-time theorem permits all fixed positive aspect ratios; the all-time theorem retains its large-sample and small-fixed-step assumptions.
- The document distinguishes exact calibration error from signed average overconfidence, finite time from growing time, first-step scale optimization from optimal stopping, and random-feature training from training both layers. It does not certify publication novelty or claim the all-time result for every overparameterized ratio.

The amendments resolve the presentation issues raised during this review. The accepted hashes above contain no remaining scope conflation or normalization error identified here.
