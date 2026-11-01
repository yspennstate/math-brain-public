# HARD8-08 — checkpoint 8 verification addendum

This append-only file records exact creation/readback receipts and the deterministic finite checks for the checkpoint beginning at `2026-09-16T12-44-40Z`.

## Mathematical report

Path:
`hard8_2026-09-16/HARD8-08/runs/2026-09-16/2026-09-16T12-44-40Z__report.md`

Creation commit:
`afb2765c7c68953971d03cc32d191d9830ba47bd`

Exact-commit readback blob:
`3f431701553784e4fa14a1c55964bcac13b8eb94`

Status: **VERIFIED** by readback at the creation SHA.

## Exact verifier source

Path:
`hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T12-44-40Z__g14_scaled_minimal_relations.py`

Creation commit:
`b43652aae9244209808319171285c54e3a587737`

Exact-commit readback blob:
`1e9e2f3e8045b7beb3e7805f3dc35e55de6a6f22`

Status: **VERIFIED** by readback at the creation SHA.

## Exact execution output

Path:
`hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T12-44-40Z__g14_scaled_minimal_relations_output.txt`

Creation commit:
`37b194d2efb2b20d4262da951f1092bae01c7308`

Exact-commit readback blob:
`d4b448380c7928e21bd58a6aea3a57005ccb3b4d`

Status: **VERIFIED** by readback at the creation SHA.

## Deterministic checks actually completed

The archived verifier was executed in the working runtime using Python standard-library exact arithmetic. It completed and printed `ALL_CHECKS_PASSED`.

Key exact output:

- scaled source-edge distances: `unit=27`, `sqrt3=18`, `2sqrt3=5`;
- normalized proper five-colourings of the 27-edge unit base: `50261`;
- distinct 23-bit candidate violation masks: `21177`;
- inclusion-minimal violation masks: `19`, with sizes `{1:18, 2:1}`;
- mandatory candidate relations: `18`;
- unique residual two-edge choice: `{i1--i5[sqrt3], a2--a4[sqrt3]}`;
- minimum non-unit relation count: `19`;
- both minimum completions have `14` `sqrt3` relations and `5` `2sqrt3` relations;
- chosen completion has `46` total edges and exact independence number `3`;
- explicit proper six-colouring checked;
- explicit five-colouring witnesses printed for every minimal violation mask.

No floating-point decision, randomization, external SAT solver, solver timeout, or failed heuristic is used as a correctness certificate.

## Scope / review status

The checkpoint establishes an exact finite completion theorem for a three-distance 14-point scaffold. It does **not** produce a pure unit-distance six-chromatic graph and does not improve the unrestricted lower bound beyond five. The Hadwiger–Nelson problem therefore remains open.

Self-review is not independent peer review. External review requirement remains **NOT EXPOSED**.
