# HARD8-08 checkpoint 5 verification addendum

This append-only note records the delivery/readback receipts and exact local verifier execution for checkpoint 5.

## Mathematical report

- Path: `hard8_2026-09-16/HARD8-08/runs/2026-09-16/2026-09-16T09-45-00Z__report.md`
- Creation commit: `142649a2b268a1e070f70cc0e8c15fbc9a2f01ff`
- Git blob SHA returned by exact-commit readback: `4eacbfff859dd3b01170444e4647c3f960b4052d`
- Read back successfully at exactly the creation commit.
- Status: **VERIFIED**.

## Exact verifier

- Path: `hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T09-45-00Z__distance_kempe_verifier.py`
- Creation commit: `d8b4119748de3bf6da16a21c2351af9a252cd6a9`
- Git blob SHA returned by exact-commit readback: `b010241780a6f023b30f4cf3a23b6e6515ba27d4`
- Read back successfully at exactly the creation commit.
- Status: **VERIFIED**.

## Exact execution completed before publication

The verifier exited with return code `0` and produced:

```text
connected_chi3_or4_graphs_checked 24059
universal_rainbow_sets_checked 62466
bichromatic_Kempe_connectivity_checks 5769270
rooted_cut_inequality_checks 3026508
degree_k_minus_1_forced_terminal_cases 17732
n 3 stats (1, 1, 18, 6, 0)
n 4 stats (19, 25, 792, 302, 12)
n 5 stats (532, 940, 52020, 22840, 380)
n 6 stats (23507, 61500, 5716440, 3003360, 17340)
K6_minus_edge_5colorings 120
K6_minus_edge_forced_pair (0, 1) terminal_degree 4
Haugland_5point_scaffold_constrained_squared_distances [Fraction(1, 1), Fraction(3, 1)]
Haugland_5point_scaffold_missing_pair_squared_distance 4
regular_hexagon_squared_distance_multiplicities {Fraction(1, 1): 6, Fraction(3, 1): 6, Fraction(4, 1): 3}
ALL_CHECKS_PASSED
```

The graph/coloring checks are exhaustive for the labelled connected graphs described in the report. The geometric scaffold checks use exact `fractions.Fraction` arithmetic in the representation `a+b*sqrt(3)` and no floating-point tolerance. The computation does not establish the full Hadwiger–Nelson conjecture; the symbolic claims and their limitations are stated in the report.

No previous report, artifact, workflow, repository setting, or peer file was overwritten.
