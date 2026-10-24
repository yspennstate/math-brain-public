# Continuation checkpoint: explicit last Fisher inequality

Model/reasoning setting not independently exposed. PARTIAL; unrestricted Lyons OPEN. Frozen three-site `B_Phi`: UNMEASURED -> UNMEASURED, no movement. The preceding checkpoint's affine-family and variance-controlled Fourier theorems remain the strongest proved coverage. No independent audits have occurred.

The remaining sufficient route is the count-Fisher matrix inequality `(2/5) I_N - 2 log(P/O)(e_a e_b^T+e_b e_a^T)>=0` for `O<P`. If proved globally, it would combine with the established positive-imbalance theorem to settle the full four-site Fourier family. It is currently UNPROVED.

`FISHER_CONTINUATION.md` derives an exact scalar equivalent of this candidate using the mean block of the inverse count Fisher matrix. The matrix has only one unknown nuisance variance tau. A four-term observable of the count computes tau explicitly, with rational coefficients and a pair-resultant denominator. This identifies a concrete remaining inequality involving rational functions, one square root, and one logarithm.

`verify_fourier_fisher.py` passes: six further exact polynomial identities and five rational candidate-matrix checks with rigorous logarithm enclosures. The candidate checks are finite examples only. Totals for the new Fourier continuation are 75 coefficientwise identities, 70 exact Fourier channel entries, 102 representative rational curvature cases, two exact proof-shortcut obstructions, and five finite candidate-matrix certificates.

Three targeted optimizer runs with seeds 901-903, 4840 evaluations each, found no negative value of the candidate on the uncovered domain. They stopped at their iteration limits without convergence and approached the boundary of the proved domain. No numerical scan is being used as a theorem. `explore_fourier_count_fisher.py` and its complete JSON output are saved.

The full conjecture remains unsolved. The restart sequence is: read README, FOURIER_POSITIVE_IMBALANCE, FOURIER_ONE_SCALAR, then FISHER_CONTINUATION. Either prove the final Fisher scalar inequality, refute that sufficient inequality and use the full determinant Phi_F, or obtain a certified negative value of the actual Hessian. Preserve the proven families and the exact failed shortcuts.
