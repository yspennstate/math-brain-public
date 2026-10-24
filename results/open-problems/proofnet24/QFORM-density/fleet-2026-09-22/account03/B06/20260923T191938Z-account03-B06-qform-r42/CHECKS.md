# r42 checks

Private exact-arithmetic evaluation of the formulas in `check_r42.py` returned:

```text
QFORM_B06_R42_CHECK_PASS
E0= 0.72674560546875
M0sq= 0.006742268800735474
R2= 0.005765706300735474
R2_half= 0.002882853150367737
zero_core_paid_bound= 52.67854041413689
partner_paid_bound= 232.27325294645095
```

The checker verifies the exact fractions

- `M0sq = 226233/33554432`,
- `R2 = 193465/33554432`,
- `R2/2 = 193465/67108864`,

and the elementary layer-cake identity

`integral_0^infinity min(1,4H/t^2) dt = 4 sqrt(H)`.

These computations are sanity checks only. The proof is symbolic and is given in `REPORT.md`.
