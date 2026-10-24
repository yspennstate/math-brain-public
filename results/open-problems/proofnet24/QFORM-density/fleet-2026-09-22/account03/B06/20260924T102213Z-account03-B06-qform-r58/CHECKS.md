# r58 deterministic check record

Executed the committed `check_r58.py` logic in the actual run.

Result:

```text
QFORM_B06_R58_CHECK_PASS
max_cross_identity_error 6.439293542825908e-15
alpha_min 0.995575221238938
kappa0 0.01685452071614474
sigma_star 0.2827697711848991
sigma0 0.11610310451823244
diffuse_bound 70.23796236298338
```

The random check covered 3,000 orthonormal carriers of ranks one through three and verified the exact cross-star identity numerically. It also checked the threshold arithmetic and controlled near-coloop examples. These are diagnostics only; the mathematical proof is in `REPORT.md`.
