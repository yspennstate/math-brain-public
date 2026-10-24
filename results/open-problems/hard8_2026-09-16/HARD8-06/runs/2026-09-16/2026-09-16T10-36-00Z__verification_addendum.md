# HARD8-06 — verification addendum for 2026-09-16T10-29-35Z

This append-only note records the exact checks and publication receipts for the hierarchical p-adic trace-energy checkpoint.

## Mathematical report

Path:
`hard8_2026-09-16/HARD8-06/runs/2026-09-16/2026-09-16T10-29-35Z__report.md`

- creation commit: `14e9bd377ea63edafbb6a3adb549a2b9cafeb059`
- exact-commit readback blob: `95a87a789762b2353dbcb03aeb053234bb38b1f9`
- status: **VERIFIED**

The readback was performed using the creation commit itself, not the moving branch head.

## Exact standard-library verifier

Path:
`hard8_2026-09-16/HARD8-06/artifacts/2026-09-16T10-29-35Z__hierarchical_trace_energy_verifier.py`

- creation commit: `430586d09d280327aa5620cb98b8df7e8532dd78`
- exact-commit readback blob: `e0d3182a0db019c7da2b66984350c0479508f609`
- status: **VERIFIED**

The verifier was executed before publication in Python 3. It completed with:

```text
ALL_CHECKS_PASSED
box_minimum_checks = 70
exact_decomposition_checks = 594
exhaustive_tree_minimum_checks = 19
single_level_comparison_checks = 1592
strict_higher_level_improvements = 1308
```

The checks use only exact integers and `fractions.Fraction`; there is no floating-point acceptance condition, randomness, external solver, or timeout-based inference.

The exhaustive residue-tree checks independently enumerate finite subsets for representative q-adic trees and verify that the stated balanced energy is the true minimum, while the explicit first-`s` digit construction attains it.

## Scope reminder

These checks validate the finite combinatorial ingredient and its formulas. They do not constitute independent verification of the full number-theoretic argument and do not resolve Lehmer's conjecture. The solution status remains **OPEN**.
