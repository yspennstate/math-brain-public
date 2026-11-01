# C27 execution/readback addendum — 16 September 2026

This append-only note corrects one delivery sentence in the immutable main report and records the verified execution/readback state. It does not alter the mathematics or overwrite prior files.

## Main report receipt

Canonical report:

`proofnet24/C27-toth-interchange/runs/2026-09-16/2026-09-16_15-25-29__run-report.md`

Creation commit:

`16baf3c8c1a7f89c975ff616dff2bf714a83ff32`

Exact-commit readback blob:

`5eae3de02281e41dc4ee68091abe807d995d9b57`

The first line, target/source, fixed metric, and source/status sections were read back from that exact commit. Main-report delivery is therefore **VERIFIED**.

## Execution chronology correction

The main report's final sentence said that the two checker artifacts "were executed before upload." An earlier local Python execution attempt did not complete successfully, so that chronology sentence was too strong. The scripts and expected-output files had already been committed when the successful execution was subsequently run.

The exact checks were then rerun successfully in this same research run. The successful execution produced, verbatim in the load-bearing lines:

```text
RANDOM-CUT SIMPLE-CYCLE CHECK
PASS k=2..64: maximal threshold with tail >=1/2 is ceil((k-1)/4).
P3 DEPENDENCE CHECK
P(1 in C0) = (x - 1)*(3*x - 1)*(x**2 + x + 1)/(6*x**4)
P(2 in C0) = (x - 1)**2*(3*x**2 + 2*x + 1)/(6*x**4)
P({1,2} subset C0) = (x - 1)**2*(x**2 + x + 1)/(3*x**4)
joint-product = (x - 1)**2*(x**2 + x + 1)*(3*x**4 + 6*x**3 + 2*x**2 + 2*x - 1)/(36*x**8)
PASS: for x=e^t>1, all covariance factors are positive; final polynomial is increasing and equals 12 at x=1.
Therefore the two cycle-membership events are strictly positively correlated for every t>0.
ALL_EXACT_CHECKS_PASS
EXPLICIT CONSTANT ARITHMETIC
infinite-volume coefficient upper bound = 4581/8 < 573
torus coefficient upper bound = 123687/8 < 15461
PASS
```

Thus the mathematical checker claims in the main report are now execution-verified; only the phrase "before upload" is corrected.

Archived checker source:

`proofnet24/C27-toth-interchange/artifacts/2026-09-16_15-25-29__block-counterexample-check.py`

creation commit `f0d8f6ec92248aaaa00a39d424b6c2ccc7865597`, readback blob `0ff25016241a421188da4344d086764ab839a339`.

Archived matching output:

`proofnet24/C27-toth-interchange/artifacts/2026-09-16_15-25-29__block-counterexample-check.out`

creation commit `ec763f975282842b8a30f5ac2a08e9b1e9b47521`, readback blob `9a2ec5ac7fc126bb4ea148596cecb22ea1e86005`.

Explicit-constant output:

`proofnet24/C27-toth-interchange/artifacts/2026-09-16_15-25-29__explicit-constants-check.out`

creation commit `698c91e9eeab6e361ca58e471540624094104f31`, readback blob `e829156d9bbc33d271494374e3d3e82b7164ae2c`.

No status upgrade follows from this correction: the source conjecture remains **OPEN**, and the present work remains **PARTIAL** pending the source-matching theorem and required independent audits.
