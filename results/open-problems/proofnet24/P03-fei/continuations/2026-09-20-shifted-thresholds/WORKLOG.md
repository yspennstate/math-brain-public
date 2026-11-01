# Research and verification ledger

20 September 2026. **Full FEI: OPEN -> OPEN. Han Question 3.1: negative analytical resolution in REPORT.md, subject to independent review.**

## Consumed sources

- `proofnet24/P03-fei/README.md`, original blob `5a092c58a61ec79413646405c4cb7dafb8457199`: current positive classes, retired resolvent/resource targets, and existing continuation instructions. This exact blob is now preserved as `README_before_2026-09-20-shifted-thresholds.md`.
- `handoffs/2026-09-19__FROZEN_SESSION_RECOVERY.md`, blob `2077f118112bfca756862fe240923ddc444b220e`, read in full: the pointwise erasure shortcut is false; the correctly quantified universal/hereditary implication survives.
- `continuations/2026-09-19-balanced-substitution/REPORT.md`, blob `dc9daa94dc791a075ff2f9569d9c7e2fb0547179`, source lines 1--230 read: resolvent obstruction, allocation identities and majority level law.
- `solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`, read in full: exact restriction identity, JS remainder, B<=H and the universal induction. Its proof is reused only with its quantified hypotheses, not as a pointwise H<=B+constant*I assertion.
- Identified prior Library patch, SHA256 `c9c534b22682e38c0546e521ebdea72ef4cebe7d97773e20229d908077cb0207`: materialized and preserved. The bounded one-step majority affine-drift argument and its harmonic allocation lower bound were read. The entire package was not independently audited or replayed. See RECOVERED_STATUS.md for the precise delivery limitation.
- Primary external sources: Han's exact Question 3.1 (including its existential-coordinate quantifier); Gonzalez--MacManus--Pereyra arXiv:2606.00246v2 (wrong designated coordinate versus well-chosen coordinate); the original O'Donnell--Wright--Zhou symmetric-function theorem with constant 12.04; NIST Hermite asymptotics. References and links appear in REPORT.md. No comprehensive priority clearance is claimed.

## New mathematical delta

The report gives an explicit fully symmetric monotone threshold family with positive equal influences and O_i/I_i >= (1/(2*pi^2))*ln(n)-C_0 at EVERY coordinate. It therefore refutes all universal constants in Han's stronger sufficient criterion, including a best-coordinate choice. The proof also gives qualitative divergence for every fixed nonzero Gaussian threshold shift and separates absolute overlap from the correctly weighted K/B costs.

This result does not rely on the recovered September 19 drift package. Its exact finite coefficient formulas, fixed-argument Hermite asymptotic and growing-degree comparison are proved in full in REPORT.md. Known symmetric FEI is credited, not relabeled as a new positive class theorem.

## Self-check of the analytical proof

The normalization check derives I_i=p_N and verifies the factor p_N*sqrt(N) in the overlap formula directly by counting degree-k subsets outside i. All terms retained in the cutoff argument are nonnegative.

The Hermite check derives the oscillator equation for exp(-x^2/4)*He_k(x)/sqrt(k!), uses the exact even/odd initial data, and bounds the Duhamel remainder in sup norm. The adjacent-product approximation has an absolute O(k^(-3/2)) summable error after dividing by sqrt(k), so zeros of the oscillating sine do not cause a relative-error problem.

The finite-n check groups the two-by-two recurrence matrices in pairs before bounding products. This avoids an uncontrolled exponential-in-sqrt(k) error. The proved bound |c_k-h_k|<=C k^3/N holds through k<=N^(1/4); the summed overlap errors are O(K^(13/4)/N+K^(13/2)/N^2)=o(1). This justifies the growing cutoff. A fixed-degree limit alone is not asserted to establish a quantitative logarithmic-in-n rate.

The quantifier check uses symmetry and strictly positive influence at every coordinate. An irrelevant coordinate or an alternative splitting coordinate cannot evade the witness. The threshold has no ties because its dimension and threshold have opposite parity.

These checks are by the same research session, not independent expert audits or Lean proofs.

## Actual executions

`python verify_threshold_obstruction.py --max-m 64 --output verification.json` completed successfully. It compares all 55 nonconstant symmetric thresholds in dimensions 1--10 with direct integer Walsh transforms, checks each coordinate separately, and verifies Parseval, the influence formula and rational overlap intervals. The exact threshold recurrence then handles dimensions 5,17,65,257,1025,4097 without enumerating their huge truth tables.

A fresh execution to `verification_replayed.json` was compared against the original parsed JSON. Every field agrees except elapsed_seconds. The executed checker SHA256 is `da946d8de5d35c6c8369f5754d4926a7d5a157f696567eb42e74631e262b5fa3`. Its local Git blob matches the readback blob `5d889fdabcd00c6341914cf5e90de5f540a6e7af`. The report's local Git blob likewise matches `6b092f3b051e2fc6b085a99905866e1c2c41d9bc`.

`entropy_weight_probe.py` and its output are **floating-point exploration only**. They use exact finite coefficients but non-certified logarithms and sums. Their successful run ends at dimension 4097. An exploratory larger run including dimension 16385 did not finish within the execution limit and is not counted as a validation. The source now includes an explicit scope docstring; this does not change its arithmetic. The rigorous bound K<=B<=H<=12.04 I for this family comes from the report plus the published symmetric theorem, not from extrapolating those finite numbers.

## Delivery and preserved history

The main proof, checker, exact output, handoff and recovery notice were committed separately to master. Commit `0908f0803a491fe423f92d1e8c5e2b63813f2b7c` indexed the result and preserved the complete prior index byte-for-byte. It was built on the current concurrent-worker head `c3bf32c593b7fa9cc4ecf724e5bf245ebfecd29e` and the ref update succeeded with force=false. No other worker's commit was discarded.

No schedule, ownership assignment, permission, visibility, native finite-dimensional metric or unrelated research file was changed. Successful delivery does not demonstrate that a subsequent scheduled run has consumed the report.

## Superseded targets and remaining gap

Do not revive Han's absolute-overlap majorant, either coordinate-selected or summed. Keep the retired scalar/full-resolvent and fixed-coefficient affine-drift warnings, while preserving valid earlier inequalities and their assumptions.

A universal dimension-free K(f)<=C I(f), or an independently justified alternative global entropy payment, is still missing. The new example does not refute that weighted target and does not establish it. Neither a restricted positive class, a negative auxiliary resolution, finite tests, nor the corrected erasure reformulation is full FEI closure.
