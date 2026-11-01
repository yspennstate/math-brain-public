# HARD8-08 checkpoint 4 — verification addendum

This append-only receipt records the completed exact finite verification for checkpoint 4.

## Mathematical report

- Path: `hard8_2026-09-16/HARD8-08/runs/2026-09-16/2026-09-16T08-46-46Z__report.md`
- Creation commit: `6d6ecbff99308c0e8b48017a33b1fc635bd93fae`
- Read back successfully at that exact commit.
- Status: **VERIFIED**.

## Exact verifier

- Path: `hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T08-46-46Z__core_attachment_inclusion_verifier.py`
- Creation commit: `e5a3520a7b47f7fd58b89b9efab0a5e80407d635`
- Read back successfully at that exact commit.
- Status: **VERIFIED**.

The verifier uses pure Python exhaustive backtracking, with no floating point and no heuristic solver. It enumerated every connected labelled graph on 2 through 6 vertices, isolated edge-critical 3- and 4-chromatic cores, compared the corrected two-terminal attachment criterion against direct extension logic, and checked the minimum-neighbourhood inclusion theorem and edge-deletion saturation theorem for every forced-equality attachment found.

Exact completed output:

```text
connected_labelled_graphs_checked 27475
edge_critical_k3_cores 13
edge_critical_k4_cores 73
ordered_attachment_pairs_checked 292644
forced_equal_attachment_pairs 11760
directed_saturation_conditions_checked 23520
sharp_k3_example (5, [(0, 3), (0, 4), (1, 2), (1, 4), (2, 3)], (0, 1), (0, 1, 2, 3))
sharp_k4_example (6, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4)], (0, 1, 2), (0, 1, 2, 3, 4))
ALL_CHECKS_PASSED
```

No inference about the full Hadwiger–Nelson problem is made solely from this finite enumeration. The general claims in checkpoint 4 are supported by the written proofs in the mathematical report; the enumeration is an exact sanity check and sharpness check.