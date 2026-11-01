# T357 completed solvable-regime theorem and continued research

Date: 2026-10-23.

The original T357 problem explicitly asks for a two-layer classifier trained by gradient descent in a solvable regime, permitting random features. The categorical random-feature construction in this package supplies that regime. It gives the proportional-limit calibration law as a function of sample ratio, width and every fixed integer training time; proves overconfidence; and answers the early-stopping question, including finite data-dependent stopping rules.

The main result is **T357_CATEGORICAL_COMPLETE_THEOREM.md**. Its model has isotropic categorical inputs, an informative logistic single-index teacher, frozen random ReLU hidden weights, and genuine discrete full-batch cross-entropy gradient descent on the output weights. The hidden features have disjoint supports. This is a complete explicitly permitted instance of the original request, not a theorem for arbitrary two-layer networks.

A concrete common regime has teacher success probability p=0.9, step c=5, n/(2d)→1/200 and m/(2d)→3/200, so m/n→3. The first update strictly improves population log-loss, while every non-neutral limiting score is overconfident. No finite positive stopping rule achieves asymptotic calibration. A finite positive population-risk-optimal stopping time exists with probability tending to one and remains miscalibrated.

## Reading order

1. **T357_CATEGORICAL_COMPLETE_THEOREM.md** — unified theorem, exact model, proofs and scope.
2. **ORIGINAL_PROBLEM_SCOPE_AUDIT.md** — original registry wording and independent scope assessment.
3. **categorical_rf_calibration.md** and **T357_independent_review.md** — full occupancy/GD law and independent audit.
4. **T357_one_step_calibration_discontinuity.md** — exact divisor formula and small-step calibration discontinuity.
5. **T357_gaussian_first_step_attempt.md**, **T357_gaussian_first_step_independent_review.md**, and **T357_gaussian_calibration_consequences.md** — additional work for Gaussian inputs and tanh features, limited to the first update. The historical filename “attempt” does not itself determine final proof status; consult the final review and theorem statements.

## Other completed work

The T336 reports prove exact all-real-label Gaussian-process posterior representation for a specified finite-rank polynomial prior using an explicitly counted ReLU-attention architecture with one controlled ordinary LayerNorm branch. They also prove finite-sample, prior-averaged ERM convergence for a non-singleton structured class. They do not prove learned uniform-all-label convergence, conventional softmax-transformer equivalence, or SGD optimization convergence. The constructive and negative architecture results are independently reviewed.

The T354 report and independent audit give a counterexample to an unqualified almost-sure ODE-tracking claim for a very slowly decreasing step schedule. The corrected proof and its earlier version are both preserved. It does not refute the weaker liminf statement or the separate audited inverse-square-root-step rate theorem.

## Evidence and limits

Exact arithmetic checks accompany the T336 compiler. Gaussian simulations retain all predeclared configurations and results, including a supplementary point outside its approximate pointwise confidence interval; simulations are not proofs. The original problem rows are preserved in source_registry_rows.json. Historical checkpoints and corrections are explicitly identified rather than overwritten as if no gap had existed.

No publication-level novelty certification, broad Gaussian multi-step T357 solution, central registry mutation, or new count for previously credited T228 is claimed. The earlier T228 package remains frozen. This package records the completed categorical T357 solution and the other scoped results separately.
