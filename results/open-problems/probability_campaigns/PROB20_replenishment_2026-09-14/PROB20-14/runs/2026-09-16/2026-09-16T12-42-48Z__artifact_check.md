# PROB20-14 multi-deletion checker execution certificate

Artifact:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/canonical_multideletion_check_20260916.py`

Creation commit: `a03462c8e0b4ed7447db165879fc9d604060644c`  
Exact-commit readback blob: `ebe411112db51b424bae154c5e17e51f99aaffaf`

The checker logic was executed on the finite-support critical span-one test law
\[
\Pr(\xi=0)=1/2,\qquad \Pr(\xi=1)=1/4,\qquad \Pr(\xi=3)=1/4.
\]
It checks the direct multi-coordinate deletion identity, the adaptive path identity, and a square-root anti-concentration diagnostic over several bounded deficit fractions.

Execution summary:

```text
ALL_ASSERTIONS_PASSED
direct_identity_cases=145
adaptive_path_cases=143
anti_concentration_diagnostic_cases=18
max_direct_abs_error=5.776e-13
max_adaptive_log_error=5.448e-13
max_sqrt_n_central_atom=0.377182
FINITE_SUPPORT_CHECK_ONLY
```

Interpretation: the numerical checks found no algebra/indexing inconsistency in the new exact identities at the tested cases.  This is **not** proof evidence for the target infinite-variance theorem; the test law has finite support and finite variance, and the mathematical proof is the symbolic derivation in the substantive report.
