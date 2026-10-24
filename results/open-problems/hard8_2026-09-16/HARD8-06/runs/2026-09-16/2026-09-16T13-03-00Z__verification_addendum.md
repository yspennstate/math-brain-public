# HARD8-06 — verification addendum for 2026-09-16T12-46-00Z

This append-only note records the actual GitHub publication receipts, exact-commit readbacks, and deterministic checks for the all-depth local-field-spectrum checkpoint.

## Mathematical report

Path:
`hard8_2026-09-16/HARD8-06/runs/2026-09-16/2026-09-16T12-46-00Z__report.md`

- creation commit: `f8dc1f23ff0e96746f08e699e8151ee781f060ac`
- exact-commit readback blob: `ff94bc7620850b1f548a968f93802775d887284b`
- status: **VERIFIED**

The readback used the creation commit itself rather than the moving `master` head.

## Exact standard-library verifier

Path:
`hard8_2026-09-16/HARD8-06/artifacts/2026-09-16T12-46-00Z__local_spectrum_energy_verifier.py`

- creation commit: `da0166cc02dd8e0dd51811887e6060a011b49e45`
- exact-commit readback blob: `f1e450bcb6130a1fa60f688fb1a8af0783f1002e`
- status: **VERIFIED**

The reviewed script was executed in Python 3 before publication. It uses only the standard library, integer arithmetic and `fractions.Fraction`; there is no random search, floating-point acceptance test, external solver, network access, or timeout-based mathematical inference.

Exact completed output:

```text
ALL_CHECKS_PASSED
C_increment = 20040
E_digit = 11011
P_increment = 11011
P_recursion = 11011
superadditivity = 91854
balanced_tree_levels = 6744
affine_Qp_sharpness = 396
projective_Qp_sharpness = 177
family_aggregation = 3179
```

The projective sharpness checks use explicit finite rational representatives in `Q_p`: finite first-level branches use `x=b+p*t`, while the infinity branch uses reciprocal coordinate `w=1/x=p(t+p^(L-1))`. Exact chordal valuations reproduce `P_p(s)` for every checked case.

## Exact output record

Path:
`hard8_2026-09-16/HARD8-06/artifacts/2026-09-16T12-46-00Z__local_spectrum_energy_output.txt`

- creation commit: `540e349b7bbd2437db370eb2aef90001fa7ffbe4`
- exact-commit readback blob: `f336aedec8f7cbe9cf77212fc239fab1664239f6`
- status: **VERIFIED**

## Scope of verification

The deterministic checks cover the exact balanced-box increment, affine base-`q` digit-sum identity, projective increment and branch recursion, finite exhaustive superadditivity, simultaneous balanced occupancies at all active depths, explicit affine and projective local sharpness over `Q_p`, and the arithmetic finite-family aggregation inequality on thousands of deterministic parameter spectra.

These checks validate the combinatorial/local arithmetic identities used in the report. They do not independently peer-review the global algebraic argument and do not resolve Lehmer's conjecture.

**SOLUTION STATUS remains OPEN.**
