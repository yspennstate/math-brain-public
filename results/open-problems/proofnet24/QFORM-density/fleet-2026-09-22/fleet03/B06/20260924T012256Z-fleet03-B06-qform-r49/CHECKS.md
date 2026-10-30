# r49 checks

The symbolic identities were independently sanity-checked numerically on 10,000 random symmetric invertible `2 x 2` matrices and random unit vectors.

Observed locally:

- `max_normalized_R1_error = 3.7062561933349913e-14`
- `max_normalized_R2_error = 3.348198306485351e-14`
- `8*128^(1/4) = 26.908685288118864`

These finite computations do not prove the theorem; the determinant formulas and pair-area aggregation in `REPORT.md` are the proof.
