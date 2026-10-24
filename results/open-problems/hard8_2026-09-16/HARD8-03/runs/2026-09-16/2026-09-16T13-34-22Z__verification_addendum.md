# HARD8-03 — verification addendum for 2026-09-16T13:12:51Z

This append-only companion records the exact GitHub receipts and readbacks for the rank-eight nullity-three profile checkpoint.

## 1. Mathematical report

- Path: `hard8_2026-09-16/HARD8-03/runs/2026-09-16/2026-09-16T13-12-51Z__report.md`
- Creation commit: `2449e25ce5d0b39bda62b0c8695c997a0d7c7d12`
- Exact-commit readback: **VERIFIED**.
- Blob SHA: `6e8709db61a8366abf6798ea09b2394a3d5ed91f`.

## 2. Exact verifier

- Path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T13-12-51Z__rank8_normal_form_verifier.py`
- Creation commit: `31e5c6da431c285d8cf5e93f598e2f8e54d5f261`
- Exact-commit readback: **VERIFIED**.
- Blob SHA: `0151308e8f923a66b8e094bf94af35456248c53e`.

The verifier uses only the Python standard library, exact integers, finite signed-relation enumeration, and bit masks. There is no floating point, randomness, external solver, or timeout-based inference.

## 3. Exact execution output

- Path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T13-12-51Z__rank8_normal_form_output.txt`
- Creation commit: `659371002eeaf16ecd8f0a3216030d3742adfe65`
- Exact-commit readback: **VERIFIED**.
- Blob SHA: `0a1dca35a22bffa529534fbbea9df1314f5d320e`.

Completed exact counts:

- heavy-pair coordinate orbits: `280`;
- ternary triple orbits before the minimum-relation filter: `75,312`;
- minimum-relation normal-form candidates: `47,667`;
- profile violations through rank eight: `0`;
- abstract non-Boolean ternary counterexample to the stronger route: independently confirmed;
- terminal status: `ALL_CHECKS_PASSED`.

## 4. Mathematical status

The deterministic log-rank conjecture remains open. The project profile inequality also remains open in general.

New checkpoint consequence: combining the preceding universal nullity-three reductions with this exact orbit enumeration proves the project profile inequality for every nullity-three Boolean configuration of real rank at most eight. Therefore any nullity-three counterexample to the project profile inequality must have rank at least nine.

This is self-review plus a deterministic finite verifier, not independent peer review. No older report, peer file, shared index, workflow, branch setting, or access rule was modified.