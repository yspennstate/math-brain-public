# Deterministic checks

Executed the committed `check_fusion.py` logic with Python/numpy in the run environment.

Output:

```text
max_cauchy_binet_relative_error 1.024e-15
target_family_eigenvalues [-1.0, 1.0, 2.0]
partner_Z2_floor 0.007994596888238
diagonal_bank_bound 22.055052186064
rank1_plus_diagonal_bound 46.938073727121
diffuse_exact_target_bound 8.373674550517
```

The numerical Cauchy--Binet tests are diagnostic only; the symbolic proof of the fused-volume identity is in `REPORT.md`. The eigenvalue and constant checks verify the explicit target family and the arithmetic used in the partner applications.
