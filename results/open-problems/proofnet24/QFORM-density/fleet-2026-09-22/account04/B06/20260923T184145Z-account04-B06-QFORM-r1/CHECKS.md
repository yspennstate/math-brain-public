# Check output

Command: `python check_bankwise_curvature.py`

Deterministic seed: `20260923`.

```
pair 0 3
tau 0.36973409150185055
schur_rank_tail 1.3173327169829148e-15
reconstruction_error 4.1147640850169864e-15
coefficient_identity_relative_error 2.559898353105525e-16
full_gram_identity_relative_error 5.254237457590002e-15
live_gate_bound 232.27325294645095
```

The check independently reconstructs the exact Schur rank-one residual, the three-square bank representation, the coefficient cancellation `D|lambda|=|det Lambda| tau`, and the global Gram identity (4.3). Floating errors are at double-precision scale.
