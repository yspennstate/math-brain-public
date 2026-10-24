# r56 deterministic check record

`check_r56.py` was run with fixed seed `5601` for `5000` random rank-one hub packets.

Output summary:

- `QFORM_B06_R56_CHECK_PASS`
- maximum normalized five-coordinate determinant identity discrepancy: `2.9516564435820586e-15`
- maximum normalized post-pivot cross-area identity discrepancy: `6.075986783912449e-14`

These computations are diagnostic only. The mathematical proof is the exact determinant-one congruence, Cauchy--Binet identity, literal scalar Schur completion, and rank-two crossing half-Riesz argument in `REPORT.md`.
