# HARD8-08 verification addendum — pair-aligned G14 self-gluing run

This addendum records exact GitHub creation receipts and exact-commit readbacks for the append-only checkpoint. It does not add a new mathematical claim.

## Runtime disclosure

Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED (the scheduler exposes no model selector or reasoning-effort selector). Requested GPT-6/maximum was therefore not claimed as an installed setting.

## Main report — VERIFIED

- Path: `hard8_2026-09-16/HARD8-08/runs/2026-09-16/2026-09-16T14-27-40Z__report.md`
- Creation commit: `0cef69e4ea29203c51d91c28baa831f578ecdeef`
- Exact-commit readback blob: `07eaec0210131e23731044942fee736f193c0d5d`
- Status: **VERIFIED**.

## Exact verifier — VERIFIED

- Path: `hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T14-27-40Z__g14_pair_alignment_verifier.py`
- Creation commit: `aad0c03dec9a15d97ff03f3994f1b636848ddddc`
- Exact-commit readback blob: `071d56025e8cb6d6f4b11efa5b727814856f04b7`
- Status: **VERIFIED**.

## Executed verifier output — VERIFIED

- Path: `hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T14-27-40Z__g14_pair_alignment_verifier.out`
- Creation commit: `4161809e42f2fb70578eb5d19c11889f671a5e00`
- Exact-commit readback blob: `f9900d8c98dd35817f6372cd2d5da677e6fccf2a`
- Output terminates `ALL_EXACT_CHECKS_PASSED`.
- Status: **VERIFIED**.

## Ledger delta — VERIFIED

- Path: `hard8_2026-09-16/HARD8-08/ledger_delta/2026-09-16T14-27-40Z__delta.md`
- Creation commit: `cc16ff3b34f040ed598e9d5b9d77717285b170f4`
- Exact-commit readback blob: `1768aff56d3d7b11bb0ffc779428d805474df813`
- Status: **VERIFIED**.

## Mathematical scope retained

The exact finite result is a no-go theorem for the defined 518-copy pair-aligned G14 self-gluing family: its complete 505-vertex, 2008-edge unit-distance supergraph has a verified proper 3-coloring. This is **PARTIAL route elimination**, not a proof or refutation of the Hadwiger-Nelson problem. The fleet metric remains `509 -> 509`, no movement. No closure audit is claimed or required for this open checkpoint.
