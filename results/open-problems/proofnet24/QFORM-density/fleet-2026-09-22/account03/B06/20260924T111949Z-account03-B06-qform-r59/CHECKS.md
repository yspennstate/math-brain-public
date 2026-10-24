# r59 diagnostic check

Execution source: `check_r59.py`, fixed NumPy seed 12345.

Observed output in this run:

```text
QFORM_B06_R59_CHECK_PASS
trials 20000
weighted_branch_samples 10018
minimum_ratio 1.5127460597692477
live_eta_currency 2.712673611111111e-05
```

The exact live currency is `1/36864 = 2.712673611111111e-05`.

These numerical checks are diagnostics only. The proof of `QFORM-FIXEDSTAR-PAIRWEIGHT-TRICHOTOMY-v1` is analytic: Parseval, the contraction inequality `G_L^2<=G_L`, positivity of the Schur numerator, a `2x2` trace/eigenvalue bound, and Cauchy-Binet.
