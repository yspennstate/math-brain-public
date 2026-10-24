# HARD8-02 — verification addendum — 2026-09-16T12:24:00Z

This append-only note records the exact execution and GitHub receipts for the q=1 endpoint-rooted `P_3` absorber checkpoint.

## Main report

Path:

`hard8_2026-09-16/HARD8-02/runs/2026-09-16/2026-09-16T12-18-00Z__report.md`

Creation commit:

`debffffbf7d901a51b767bcbb3545cdc2fd808e1`

Exact readback at that creation commit returned blob:

`9345324a1b05da351e58a09de5ab5d67c53d1e68`

Status: **VERIFIED**.

## Exact verifier

Path:

`hard8_2026-09-16/HARD8-02/artifacts/2026-09-16T12-18-00Z__p3_q1_closed_form_verifier.py`

Creation commit:

`c83c6d20581293ec2ee52119ac564aebe8b91ecc`

Exact readback at that creation commit returned blob:

`b28cf6623c4d0455648db6aeb0008c02708cd07e`

Status: **VERIFIED**.

The reviewed script was executed in the bounded research runtime with Python standard integer arithmetic. It returned:

```
Q1_FORMULA_CHECKS 1999
SPLIT_IDENTITY_PARAMETER_CHECKS 10100
EXAMPLE_H 2 [(8, 0, 7), (10, 5, 1), (11, 2, 4), (9, 3, 6)]
EXAMPLE_H 3 [(12, 0, 11), (15, 7, 1), (16, 2, 9), (13, 3, 6), (17, 4, 8), (14, 5, 10)]
EXAMPLE_H 4 [(16, 0, 15), (20, 9, 1), (21, 2, 11), (17, 3, 13), (22, 4, 8), (18, 5, 10), (23, 6, 12), (19, 7, 14)]
ALL_CHECKS_PASSED
```

The finite loop checks `h=2,...,2000`; the universal claim is proved symbolically in the report and does not rely on extrapolating from that range.

## Archived execution output

Path:

`hard8_2026-09-16/HARD8-02/artifacts/2026-09-16T12-18-00Z__p3_q1_closed_form_output.txt`

Creation commit:

`2af6c85f4620bc28189db6e223c7f2930023b278`

Exact readback at that creation commit returned blob:

`a6facdf4ec1ec9a477f5e5967abc6ff89e77bd9f`

Status: **VERIFIED**.

## Prior checkpoint dependency

The report depends on the previous `P_3` defect identity and lower-bound checkpoint:

`hard8_2026-09-16/HARD8-02/runs/2026-09-16/2026-09-16T11-25-23Z__report.md`

creation commit

`1563babf191c7dd35203009ca17cd3073e3cdcff`

blob

`4791f6fe8682ee4b12c2b8afbd857fdfea999861`.

That file was re-read at the exact creation commit before the new report was created.

## Review posture

The formulas and exact-integer checks support the internal consistency of the new q=1 theorem, but this is self-review rather than independent external verification. The full graceful tree conjecture remains open. No solver timeout, random search, floating-point acceptance criterion, or unproved computational nonexistence claim is used in the theorem.