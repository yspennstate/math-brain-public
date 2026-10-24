# T357 Gaussian continuation: accepted mathematical result

The owner requested a full proof for another problem from the TOP200_DL list, beyond already credited T228. This continuation now contains a complete, internally checked answer to T357's expressly permitted Gaussian random-feature regime. It goes beyond the earlier categorical example and beyond the earlier first-update calculation. Those historical artifacts remain unchanged.

## Accepted T357 result

Start with `T357_THEOREM_AND_SYNTHESIS.md`, frozen SHA-256 `7b773eba4446340893bd8e67a1397ba06b154bf79b9f89a348e68c1a93282d51`. `T357_GAUSSIAN_COMPLETE_PROOF.md` combines it with the complete detailed proof modules in one readable file.

- Actual Gaussian-input tanh two-layer network, logistic single-index teacher, ordinary full-batch output-weight GD from zero on the same reused cross-entropy sample.
- Deterministic state evolution, population risk, exact unbinned model-conditional calibration, and an integrated calibration curve at every fixed positive time, for all fixed positive finite aspect ratios and learning scales.
- Under explicit sufficiently large sample-to-width ratio and sufficiently small fixed positive step: uniform calibration approximation over all positive times, the MLE, and arbitrary training-measurable stopping times, with a strictly positive common calibration floor.
- Strict average overconfidence and risk below log 2 at the risk-optimal first-step learning scale.
- An explicit nonempty weak-teacher parameter regime where the risk-optimal scale satisfies the all-time assumptions, so the same fixed-step model has all these conclusions.

The matrix hypotheses, ordinary-GD embedding, exact rectangular recursion, nondegeneracy, total-variation upgrade, all-time contraction and delocalization, and scalar overconfidence proof received independent checks. Final reviewers accepted the frozen synthesis. Numerical comparisons are only normalization checks, not proof premises.

## Meaning of completion

This is an accepted internal mathematical answer to the precise solvable-regime question in the user's Top 200 DNN list. It is not certification that a new named published open conjecture has been resolved. The registry's original source/open-status flag was unverified; prior random-feature calibration theory exists. Publication novelty and external expert validation remain unestablished. No central problem registry has been changed, and the earlier categorical result is not counted as a separate additional problem.

The uniform-time theorem has more samples than trained output coefficients and a fixed stable step. It does not cover all overparameterized late-time regimes, vanishing-step schedules, or training both layers. At time zero the constant predictor is calibrated; the obstruction concerns positive training times. Signed overconfidence is an average statement, not a pointwise statement at every confidence.

## Other work preserved

- T321: complete explicit Gibbs functional-inequality and MALA bounds for the original Gaussian phase-retrieval loss, independently checked; publication novelty unverified.
- T355: the original request for some positive quantitative exponent was already answered in primary literature. A square-root-step refinement under stated regularity is proved and preserved without claiming a first solution.
- T366: the requested order was already available; upper/lower proof and source correction preserved.
- T352: fixed-parameter privacy plateau correction preserved.
- T336: fixed-bin and algebraic-circuit impossibility results preserved with their exact architecture restrictions.

All new proof files, audits, code, numerical outputs, source comparison, and verification records are retained in this continuation. Older T228 and T357 packages remain frozen.
