# HARD8-04 verification addendum — 2026-09-16T09:27:50Z

This append-only note records the publication/readback status of the immediately preceding mathematical checkpoint.

## Main mathematical report

Path:

`hard8_2026-09-16/HARD8-04/runs/2026-09-16/2026-09-16T09-24-18Z__report.md`

Creation commit:

`f0391eddbce8df2d06b7b472b51b523bb4350941`

Readback was performed at that exact commit and succeeded. Returned blob SHA:

`d2c779e3e7370f3889c91cf50cdd9da886854620`

Status: **VERIFIED BY READBACK**.

## Exact computations completed before publication

The bounded research run performed exact integer-arithmetic checks of the following facts before the report was published:

1. For the explicit length-19 supports printed in the report, the first pair has half-defect `(0,0,0,0,0,4,0,-4,0)`.
2. The printed compensator rows have half-PAF vectors `(-5,3,-1,-1,3,-1,-1,3,3)` and `(7,-1,3,3,-1,-1,3,3,-1)`, whose sum is exactly `(2,2,2,2,2,-2,2,6,2)`.
3. Their four circulant Gram matrices sum exactly to `76 I_19`.
4. The standard Goethals-Seidel array built from those four circulants is a `76 x 76` sign matrix satisfying `H H^T = 76 I_76` exactly.
5. Exact PAF-type enumeration produced the defect-pattern coverage table in the report for every odd `v` from 5 through 19.

No floating-point acceptance test or solver timeout was used in these checks.

## Artifact publication status

Intended artifact path:

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-16T09-24-18Z__gs_defect_transfer_verifier.py`

The GitHub connector refused the attempted creation with the platform message:

> `This tool call was blocked by OpenAI because we couldn't determine the safety status of the request.`

Per the task's security rule, the denied publication was **not retried or bypassed through an altered payload, tool, task, or channel**.

Artifact status: **BLOCKED / NOT UPLOADED**.

The full mathematical derivations, literal length-19 support certificate, exact PAF vectors, finite census results, and next attack remain preserved in the verified Markdown report. The missing item is only the standalone code artifact; it requires explicit platform review/approval before publication and is **NOT EXPOSED** in the repository.