# HARD8-06 — verification addendum for 2026-09-16T09-40-33Z

This append-only note records the exact checks and publication receipts for the trace-local p-adic energy checkpoint.

## Mathematical report

Path:
`hard8_2026-09-16/HARD8-06/runs/2026-09-16/2026-09-16T09-40-33Z__report.md`

Creation commit:
`8adf46be8c524165dbfe738c574c37e71999a8fa`

Exact-commit readback succeeded. Returned content blob SHA:
`c87c631fab59f49e9d60bb55b0626cd642552e4e`

Status: **VERIFIED**.

## Exact verifier

Path:
`hard8_2026-09-16/HARD8-06/artifacts/2026-09-16T09-40-33Z__trace_local_energy_verifier.py`

Creation commit:
`11ca0aa172fdebe38e5262553b2af52291387255`

Exact-commit readback succeeded. Returned content blob SHA:
`81a3a52402883f876a97d60771b2772b6679a05a`

Status: **VERIFIED**.

The script was executed before publication with Python 3 + SymPy and completed with output:

```text
PASS
local collision checks: 264
endpoint/norm/discriminant checks: 5
Lehmer benchmark checks: 1
```

All checks used exact integer or symbolic arithmetic. No floating point, randomized search, solver, or timeout-based inference was used.

The 264 local checks verify the `K = Q_p` specialization of

`v_p(Disc R) >= sum_a N_a(N_a-1) >= D^2/p - D`

across deterministic distinct-integer-root test families for degrees 2 through 12 and primes 2,3,5,7,11,13. The remaining checks verify the endpoint norm identity, the archived reciprocal discriminant identity on deterministic samples, and the exact Lehmer benchmark values.

These computational checks are sanity checks only; the general local-field theorem in the report is established by the written valuation and Cauchy-Schwarz proof, not by finite computation.