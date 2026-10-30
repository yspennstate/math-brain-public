# r53 deterministic checks

`check_r53.py` was mirrored in the run interpreter with fixed seed `20260924` and 10,000 instances in each test family.

Observed output:

```text
QFORM_B06_R53_CHECK_PASS
max_general_normalized_error 2.7895927289967028e-14
max_singular_normalized_error 1.1604806058903097e-14
```

The general test checks

`det M_j = delta_j det F + z_j^T[(det F)D_H-D_H adj(F)D_H]z_j`

for arbitrary symmetric invertible core `B`, arbitrary diagonal hub perturbation `D_H`, arbitrary tail column `z_j`, and arbitrary tail diagonal `delta_j`.

The singular test forces an exact rank-two actual hub block and checks

`det M_j = -(mu_1 mu_2) omega_j^2`

for seven arbitrary tail columns and arbitrary tail diagonal perturbations.

These are floating-point sanity checks only. The proof in `REPORT.md` is exact algebra.

Correction to the preliminary diagnostic sentence in `REPORT.md` Section 9: the exact committed checker above gives `2.79e-14` and `1.17e-14`; the preliminary `2.44e-14` / `5.44e-14` figures there came from a slightly different equivalent random harness. This correction changes no theorem, inequality, or proof.
