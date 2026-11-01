# HARD8-08 verification addendum — 2026-09-16T15:05:00Z

This append-only addendum records exact GitHub creation receipts and creation-SHA readbacks for the 2026-09-16T14:44:32Z recursive squared-distance-13 G14 run. It does not alter the mathematical claims of the main report.

## Main report

- Path: `hard8_2026-09-16/HARD8-08/runs/2026-09-16/2026-09-16T14-44-32Z__report.md`
- Creation commit: `9d59317b8f8eb2e7ad5d952832d73412e30cd21c`
- Exact-commit readback blob: `9107f70db711d4b468ee57fcce1e0b3c704798df`
- State: **VERIFIED**. The connector display truncated the long report body, but the fetch was explicitly against the creation commit and returned this blob SHA.

## Exact checker

- Path: `hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T14-44-32Z__d13_recursive_exact.py`
- Creation commit: `7dc2b5a7dc61440d1c8abe601e4c65827524fc38`
- Exact-commit readback blob: `3f1e97ae979faf5c6abf15fb479459da3e15b550`
- State: **VERIFIED**. Both the beginning and terminal assertion/output section were read back at this creation commit.

## Archived execution output

- Path: `hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T14-44-32Z__d13_recursive_exact_output.txt`
- Creation commit: `d564d52ab71e2e4b7a235217ec18bfa959ef28f6`
- Exact-commit readback blob: `ea539c300295d3d80904acd2972095c171049d6a`
- State: **VERIFIED**.
- Terminal line: `ALL_EXACT_D13_CHECKS_PASSED`.
- Key checked finite counts: 1,848 first-generation squared-distance-13 target pairs; 29,568 raw second-generation alignments; 10,971 distinct second-generation copies; 17,056 generated points; 80 nonzero mod-3 linear forms tested; 18 successful forms; all 17,056 generated points checked 3-integral.

## Task-local ledger delta

- Path: `hard8_2026-09-16/HARD8-08/ledger_delta/2026-09-16T14-44-32Z__delta.md`
- Creation commit: `ae5c277c7cc498041a9e9cae748f0c3f6c36b9f4`
- Exact-commit readback blob: `d071a781fd9dcabb21071947d2beb14724d75b9f`
- State: **VERIFIED**.

## Verification boundary

The finite arithmetic checks are self-checks, not independent external audits. The all-depth recursive `d^2=13` no-go statement also uses the written algebraic proof in the main report: the checker establishes the exact finite base data and 3-integrality evidence, while the proof shows that division by 13 preserves `Z_(3)[sqrt(3)]` and that `kappa(a+b sqrt(3),c+d sqrt(3))=a+c (mod 3)` separates every exact unit-distance pair in that ring. No source-level closure is claimed, so no closure audit is counted.
