# T357 Gaussian proof package

Read `T357_GAUSSIAN_COMPLETE_PROOF.md` for the theorem and all detailed proof modules in one file. For the shorter statement, explicit recursion, and proof composition, read `T357_THEOREM_AND_SYNTHESIS.md`.

The accepted result answers T357's Gaussian random-feature regime from the user's TOP200_DL list. It gives all fixed training times at all positive finite aspect ratios, and an all-time stopping theorem in the explicitly stated large-sample, small-fixed-step regime. A common-regime corollary supplies risk improvement, signed overconfidence, and the all-time obstruction for one model. The package does not certify publication novelty or external peer review.

The original source row is preserved in `references/source_registry_rows.json`. Source comparisons are in `T357_PRIMARY_SOURCE_COMPARISON.md`. `CURRENT_STATUS.md` states the final interpretation. `ACCEPTANCE.json` and `MANIFEST.json` record the reviewed files and their hashes. `SAVE_RECEIPTS.json` records the immutable commits and exact-content readbacks in both Brain repositories.

## Main proof modules

- `b03_gaussian_dynamics.md`: actual random-feature matrix, delocalization, spectral and generalized-invariance hypotheses, and GD embedding.
- `b01_GD_state_evolution_check.md`: explicit finite-time recursion, positive covariances, and first-step check.
- `b04_calibration_transfer.md`: conditional total variation and exact unbinned calibration.
- `b02_uniform_time_GD.md`: coercivity, curvature, MLE, and arbitrary positive stopping times.
- `b06_gaussian_overconfidence.md`: strict signed overconfidence, risk improvement, and the explicit common regime.

Independent reviews include `b01_final_T357_review.md`, `b02_final_T357_review.md`, `b04_state_evolution_audit.md`, `b05_RF_universality_audit.md`, `b05_uniform_time_audit.md`, and `b06_scope_and_mathematics.md`.

`check_T357_finite_time.py` is the reproducible numerical normalization check; its JSON output is included. It uses NumPy and SciPy. Finite-network A,Q values are covariance proxies whose asymptotic equivalence is proved analytically. These computations are not substituted for mathematical proof.

Other fullproof reports preserve the T321, T355, T366, T352, and T336 work and literature-status corrections. They are not additional claimed new open-problem solutions. The `references` directory contains unchanged earlier source and proof records used in this continuation.
