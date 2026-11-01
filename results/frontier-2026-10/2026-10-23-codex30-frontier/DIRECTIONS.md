# Directions, limits, and rejected shortcuts

## T336 — directions that remain worth pursuing

1. Finish an end-to-end finite hierarchical-GP transformer theorem, including evidence log determinants, posterior mixture weights, their readout architecture, and training. Componentwise posterior moments alone do not determine mixture weights. A26 and A30 isolate this issue and supply explicit error budgets.
2. Replace exact/approximate finite-class ERM with a justified efficient optimization algorithm. The sample bound does not imply that gradient descent reaches the required empirical risk.
3. Sharpen the explicit raw-RBF encoder and grid bounds. The constructive proof deliberately permits large widths; analytic multiplication/exp approximators and better kernel features could improve the dependence on dimension and accuracy.
4. Extend the exact signed, unnormalized ReLU-attention construction to the specific normalized or softmax architecture of interest. Fixed scalar normalization can be absorbed into weights; a data-dependent denominator, layer normalization, and softmax require separate proofs.
5. Study growing query count, random context length beyond a fixed maximum, and data-dependent query designs. Current finite-size estimates name N and m and assume an exogenous bounded input design in the unconditional statistical result.
6. Obtain an external novelty and human proof review before describing these extensions as publishable breakthroughs. Current Brain status entries were stale twice; consult moves, claims, reviews, and current source files together.

## Mathematical checks that prevent false claims

- A nonnegative approximate covariance is weaker than a conservative covariance. Feature-space and data-space inverse formulas reverse the direction of inverse-approximation error.
- Gaussian KL has no triangle inequality. Compose errors in mean/covariance or use the explicit mixture latent-label argument.
- The GP label distribution is unbounded. A bounded-loss Hoeffding argument is invalid for Gaussian NLL; use the proved subexponential bound and state the task sampling law.
- A small numerical quadrature error is not an interval certificate. T228 root decimals are diagnostics; its (1,2) bracket is certified with rational moments.
- Average radial contraction is not the expected global vector Lipschitz norm. For rank-one updates in d≥2 the latter can be at least one. Fixed-pair expected contraction is a different valid statement.
- A positive tail constant does not follow from a formal moment-root equation alone. The stationary support, noise, tilted log moment, and a positivity theorem must be checked.

## Preserved side directions

- A04: joint GP posterior covariance with Richardson kernel attention; a useful baseline, not a new resolution of scalar T336.
- A05: sphere-uniform quartic tensor objective at component and generic directions, plus a deterministic perturbative spurious-maximum criterion. It does not prove high-probability spurious maxima for the random T364 model.
- A09: exact leaky-ReLU minibatch moments and the p≥1 monotonicity boundary. Reported low-index numerical counterexamples are not interval-certified.
- A18: bounded perturbations of a linear activation preserve the asymptotic multiplier under explicit derivative bounds. A bounded oscillatory perturbation such as sin can fail the needed uniform gradient remainder; bounded tanh activation alone has multiplier one and does not meet the same contraction criterion.
- A11: a direct repeatable expansion-event argument gives a polynomial lower tail without identifying its exact index.

T069 and the already-refuted T353 conjecture were excluded. T228's completed core is recorded as replication. No duplicate work is used to inflate the frontier claim count.
