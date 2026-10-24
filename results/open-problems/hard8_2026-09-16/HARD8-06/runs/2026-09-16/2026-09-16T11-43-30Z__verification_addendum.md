# HARD8-06 — verification addendum for 2026-09-16T11-32-33Z

This append-only note records the actual publication receipts, exact-SHA readbacks, and deterministic checks for the projective p-adic residue-tree checkpoint.

## Mathematical report

Path:
`hard8_2026-09-16/HARD8-06/runs/2026-09-16/2026-09-16T11-32-33Z__report.md`

- creation commit: `4973c19bb20dce266179fe8e0cd9c09b5df670e0`
- exact-commit readback blob: `b67838a82f08a94066b407bfdaac049e67925333`
- status: **VERIFIED**

The readback used the creation commit itself, not the moving `master` head.

## Exact standard-library verifier

Path:
`hard8_2026-09-16/HARD8-06/artifacts/2026-09-16T11-32-33Z__projective_residue_energy_verifier.py`

- creation commit: `fb25a1834bf279b5618c9c730fee963afbc315fb`
- exact-commit readback blob: `11597d31a1e4fbd96a7e72b5d33e734ed1c31d97`
- status: **VERIFIED**

The reviewed script was executed in Python 3 before publication. Exact output:

```text
ALL_CHECKS_PASSED
box_minimum_checks = 45
projective_cardinality_checks = 8
projective_determinant_checks = 788185
closed_form_checks = 3500
one_level_comparison_checks = 3500
strict_higher_level_improvements = 3214
geometric_sum_checks = 45
discriminant_identity_checks = 24
sample_energy_checks = 24
```

The checks use exact integer arithmetic and `fractions.Fraction` only. There is no floating-point acceptance condition, random search, external solver, or timeout inference.

## Exact output record

Path:
`hard8_2026-09-16/HARD8-06/artifacts/2026-09-16T11-32-33Z__projective_residue_energy_output.txt`

- creation commit: `c6691fc386677207675dad41430a4ba83f746815`
- exact-commit readback blob: `8a878ee0685ddbdba4a94f84b731174bb26dd185`
- status: **VERIFIED**

## Scope

The verifier confirms the finite projective-line cardinalities, determinant coincidence criterion in representative local rings, balanced-box minima, closed-form projective energy, improvement over the one-level bound, and sample primitive split-polynomial chordal/discriminant identities. These checks are consistency tests of the algebraic/combinatorial ingredients. They are not independent peer review of the proof and do not resolve Lehmer's conjecture.

**SOLUTION STATUS remains OPEN.**
