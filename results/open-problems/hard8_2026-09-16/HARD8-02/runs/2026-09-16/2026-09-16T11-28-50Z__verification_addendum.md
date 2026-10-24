# HARD8-02 — verification addendum — 2026-09-16T11:28:50Z

This append-only addendum records the concrete persistence and deterministic verification receipts for the immediately preceding `P_3` absorber checkpoint. It does not change the mathematical status: **OPEN**.

## Mathematical report

Path:

`hard8_2026-09-16/HARD8-02/runs/2026-09-16/2026-09-16T11-25-23Z__report.md`

Creation commit:

`1563babf191c7dd35203009ca17cd3073e3cdcff`

Exact-commit readback blob:

`4791f6fe8682ee4b12c2b8afbd857fdfea999861`

Readback was performed at the creation commit and the report header/content matched. Status: **VERIFIED**.

## Exact verifier

Path:

`hard8_2026-09-16/HARD8-02/artifacts/2026-09-16T11-25-23Z__p3_absorber_defect_verifier.py`

Creation commit:

`c4c2d7cf10c98c747a86d9d88715189355768279`

Exact-commit readback blob:

`5a9a24c7e9ec0fb169114b7bf6af426c25ca2343`

Readback was performed at the creation commit. Status: **VERIFIED**.

The same reviewed standard-library verifier logic was executed in the bounded run and returned exactly:

```text
TENSOR_MINIMAL_CHECKS 101
EXPLICIT_NON_TENSOR_CHECKS 2
CENSUS {1: [0], 2: [], 3: [0, 1], 4: [0, 1], 5: [0, 1, 2], 6: [0, 1, 2], 7: [0, 1, 2, 3], 8: [0, 1, 2, 3]}
C2K0_EXHAUSTIVE_NONEXISTENCE True
ALL_CHECKS_PASSED
```

No floating point, randomness, external solver, or timeout-based inference is used in these checks.

## Exact finite witness data

Path:

`hard8_2026-09-16/HARD8-02/artifacts/2026-09-16T11-25-23Z__p3_absorber_witnesses_c1_c8.tsv`

Creation commit:

`1016552065f89770be0bcbd378a75d356675ae6a`

Exact-commit readback blob:

`b12a4e7bbf948a3d5e864a8b59b92e0df406f360`

The TSV records one exact `(root,middle,leaf)` witness for every feasible pair found in the complete `c<=8` census. Readback was performed at its creation commit. Status: **VERIFIED**.

## Previous dependency rechecked

The immediately preceding mathematical checkpoint

`hard8_2026-09-16/HARD8-02/runs/2026-09-16/2026-09-16T10-16-29Z__report.md`

was reread at its creation commit

`27cb714c52148b3c4569e6ac82811aebf4d2c59d`

and returned blob

`7e34e3bdae0f20b6265e854faea2adb920654534`.

Its tensor theorem is therefore an actual archived dependency, not assumed local history.

## Review status

The algebraic proofs in the report are self-reviewed and computationally consistency-checked, but **not independently peer reviewed**. The finite census is exact only for the stated bounded range `c<=8`; it is not a universal existence proof. The project conjecture that every pair `c>=2k+1`, except `(2,0)`, admits a `P_3` suffix-root absorber remains open.
