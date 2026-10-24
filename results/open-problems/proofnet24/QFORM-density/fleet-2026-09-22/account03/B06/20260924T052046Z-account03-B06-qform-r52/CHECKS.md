# r52 deterministic check output

Command: `python check_r52.py`

```text
QFORM_B06_R52_CHECK_PASS
samples 3996
nonzero_twist 7.347211e-13
zero_twist 3.083969e-13
residual_parseval 1.801525e-15
second_twist 3.207069e-13
beta_wedge 5.710638e-16
```

The checker is only a finite floating-point sanity check. The report's mathematical claims are proved by exact determinant, Parseval, and dependent-smoothing arguments.
