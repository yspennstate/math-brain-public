# r53 deterministic checks

Executed the fixed-seed `check_r53.py` logic locally with Python/NumPy. Output:

```text
QFORM_B06_R53_CHECK_PASS
used_trials 5000
max_schur_minor_error 2.023623929663076120e-13
max_unweighted_aggregate_error 1.288006322401990807e-15
max_weighted_aggregate_error 1.867067100058299103e-15
split_R 3.141592653589793116e+00
weighted_near 1.119578772967990972e+03
weighted_far 1.119578772967991199e+03
density_constant 1.600000000000000000e+01
```

The randomized finite-precision checks are sanity checks only. The proofs are the determinant/exterior-algebra identities and product-Fourier argument in `REPORT.md`.
