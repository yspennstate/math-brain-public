# HARD8-04 verification addendum — 2026-09-16T08:29:16Z

This append-only note records publication/readback receipts for the immediately preceding checkpoint.

## Main mathematical report

Path:

`hard8_2026-09-16/HARD8-04/runs/2026-09-16/2026-09-16T08-26-36Z__report.md`

Creation commit:

`0e45ac59c1a89138bada8e8c6e36bea457b6faf6`

Readback was performed at that exact commit and succeeded. The returned blob SHA was:

`bd7b59ae85a5d95e5473c41cc5c3e64f5d51ec7c`

Status: **VERIFIED BY READBACK**.

## Exact verifier artifact

Path:

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-16T08-26-36Z__e32_tcc_border_rank_verifier.py`

Creation commit:

`3a8f017219aac14b7d86641855d44505bf62df1a`

Readback was performed at that exact commit and succeeded. The returned blob SHA was:

`b3d775f733f319fbc9be39de6b58baa18efce690`

Status: **VERIFIED BY READBACK**.

## Exact execution performed before upload

The pure-Python verifier was executed locally with no floating-point arithmetic in the matrix/rank checks. Output:

```text
v19 exact Gram/factor/rank/border checks passed
principal-border theorem inequalities checked for odd 11<=v<=201
rank formula checked exactly for all defect pairs at odd v<=21
ALL EXACT CHECKS PASSED
```

The verifier reconstructs the explicit length-19 `E=32` state, checks the full `40 x 40` TCC Gram identity in integer arithmetic, computes exact rational matrix ranks, checks the defect factorization, checks the rank formula for every defect pair through odd length 21, and checks the no-proper-border inequalities over all admissible increments for odd lengths 11 through 201.

No solver timeout, numerical tolerance, or probabilistic acceptance criterion is used.