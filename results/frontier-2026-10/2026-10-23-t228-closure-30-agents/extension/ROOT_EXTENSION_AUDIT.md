# Root audit: large-norm obstruction, stopping splice, and margin transfer

2026-10-24. This file records new extension work. The frozen fullproof package is unchanged.

## Accepted local extension

I read the complete arguments in b06_full_scope_frontier.md Sections 2–3 and b02_overparam_all_time.md Sections 1–9.

The B06 proof is valid: the population feature covariance lower bound and Gaussian Lipschitz moment bounds yield a uniform small-ball event for every coefficient vector. Combining that event with a bounded teacher coordinate uses a union bound, not independence. The signed test function is measurable in the score, which is essential for lower-bounding exact score-conditional calibration error. The resulting calibration floor applies to all sufficiently large coefficient norms. The population cross-entropy bound is linear in the coefficient norm. Both conclusions hold simultaneously over all coefficients, including localized and training-dependent vectors.

The B02 proof correctly uses conditional independence of feature columns given the training inputs. Its uniform small-ball estimate yields a row-Gram lower bound in an explicit sufficiently wide proportional regime. The same estimate permits deletion of a small fraction of columns without an extra union bound. The ordinary smooth convex GD comparator inequality gives a simultaneous empirical-loss bound for all integer times. Jensen's inequality then forces the coefficient norm above any fixed threshold after a deterministic finite time, uniformly in dimension. Splicing with the already-proved finite-time calibration theorem gives an all-positive-stopping-time floor. Population risk coercivity confines the optimum over the entire GD path to a deterministic finite window. These are simultaneous-time statements; they do not interchange two unproved limits.

B02 snapshot independently checked by B05 and B06:
SHA-256 51a29d866ee8cfc3e6da47ce4d36f31df93d1d348a58d6e36d88ef6c01094433.

## Independent audit of the radius/RSC transfer

I read B03 Sections 1–3. The Gaussian radial coupling is sound. In the expansion of tanh(r x), the first radius derivative is the odd bounded-Lipschitz function x sech²(x). Its sample matrix has operator norm O_P(sqrt(d)), while the maximum radius deviation is O_P(sqrt(log(d)/d)). The second radius derivative is uniformly bounded for r at least 1/2, giving a Frobenius remainder O_P(1). The full normalized operator perturbation therefore tends to zero.

The deterministic margin perturbation lemma uses the actual needed dual bound: every simplex minimizer has Euclidean norm O(1/sqrt(n)). This follows from the restricted lower bound plus testing the uniform simplex vector. The projection-of-zero inequality then gives Euclidean closeness of the two minimum-norm convex-hull points. Normalized max-margin directions are close whenever the limiting margin is strictly positive. The argument does not apply at a zero-margin boundary.

## Repair of an unnecessary stronger claim in the source proof

The primary source is Montanari–Ruan–Saeed–Sohn, arXiv:2310.00176v1, https://arxiv.org/html/2310.00176v1 . Its Section 4.1.1 derives a Euclidean dual bound, then asserts a stronger coordinatewise bound. That stronger inference does not follow merely from the displayed Euclidean bound and support size. It is unnecessary for the margin lower bound used here.

Here is the direct deterministic replacement, stated independently. Let A be a signed design, let Delta be the probability simplex, and define
\[
  \widehat\kappa=\min_{u\in\Delta}\|A^\top u\|_2,\qquad
  F(A;r)=\min_{\|\theta\|_2\le1}\frac1n\|(r\mathbf1-A\theta)_+\|_2^2.
\]
Suppose a minimizing u_* satisfies \(\|u_*\|_2\le C/\sqrt n\). For a minimizer theta_r of F,
\[
\begin{aligned}
\widehat\kappa
 &= \max_{\|\theta\|\le1}u_*^\top A\theta\\
 &\ge u_*^\top A\theta_r\\
 &\ge r-u_*^\top(r\mathbf1-A\theta_r)_+\\
 &\ge r-\|u_*\|_2\|(r\mathbf1-A\theta_r)_+\|_2\\
 &\ge r-C\sqrt{F(A;r)}.
\end{aligned}
\]
Only simplex nonnegativity, its unit sum, and Cauchy–Schwarz are used. Thus the margin lower bound follows from the source's independently proved restricted bound and squared-hinge universality, without the stronger coordinatewise assertion. B01 is checking the exact dependency graph before integrating the whole positive-margin phase.

## Frontier

The explicit strongly overparameterized all-time theorem is proved. The exact positive-margin phase transfer, vanishing-step extension, and terminal formulas are being assembled and reviewed separately. The critical zero-margin boundary, a full intermediate nonseparable-phase theorem, and learned hidden features are not covered by this checkpoint.

A general statement that independent nonzero residual noise always forbids calibration is false: B05 has an explicit calibrated additive-noise construction, independently checked by B06. Its representability by the specific proportional Gaussian tanh random-feature span is not established. It is a boundary warning for proof logic, not a counterexample to the accepted model-specific theorem.

