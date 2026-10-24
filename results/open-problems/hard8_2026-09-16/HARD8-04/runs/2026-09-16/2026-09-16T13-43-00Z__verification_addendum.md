# HARD8-04 verification addendum — 2026-09-16T13:43:00Z

This append-only note records publication/readback receipts and exact deterministic checks for the quotient-order-six checkpoint.

## Main mathematical report

Path:

`hard8_2026-09-16/HARD8-04/runs/2026-09-16/2026-09-16T13-21-17Z__report.md`

Creation commit:

`9c4f5435a1be371af471a285b602e238d25bca38`

Exact-commit readback blob SHA:

`5295923a21c93da8c3bfee6c8e469c98c40bf21a`

Status: **VERIFIED BY READBACK**.

## Exact verifier

Path:

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-16T13-21-17Z__d6_quotient_verifier.py`

Creation commit:

`6fabcb75645d3650f473cd0c5fd5d71a5e571044`

Exact-commit readback blob SHA:

`72ef2ab05f2c8ab774f1b38a95f8a2fb31741afa`

Status: **VERIFIED BY READBACK**.

The reviewed verifier uses only Python standard-library exact integer arithmetic. It contains no randomization, floating-point acceptance criterion, external solver, network call, repository automation, or timeout-as-nonexistence inference.

## Exact execution output

Path:

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-16T13-21-17Z__d6_quotient_output.txt`

Creation commit:

`4f4ecc0ee8742271ef7b2a11f0632f428235e1eb`

Exact-commit readback blob SHA:

`7dfa142908ceca80714bd9678fb745dc5c478b70`

Status: **VERIFIED BY READBACK**.

Completed output:

```text
BASE_CERTIFICATES_VERIFIED 34
DIRECT_BASE_CERTIFICATES 13
ONE_EXCEPTION_BASE_CERTIFICATES 21
D6_QUOTIENT_CERTIFICATES_VERIFIED 5000
FINITE_RANGE s=1..5000 v=6..30000
ALL_EXACT_D6_CHECKS_PASSED
```

For each `s=1,...,5000`, the script constructs the certificate prescribed by the report, then checks exact row sums, the fiber bounds `0<=n_i(r)<=s`, all three cyclic energy equations, and all six quotient autocorrelation equations. The 34 finite base cases are separately rechecked before the range test.

The universal theorem is stronger than the finite range: it rests on the symbolic parity split plus Legendre's three-square theorem, with every finite exceptional `s` explicitly certified in the report.

## Scope

The checkpoint proves universal feasibility only for the complete **single quotient occupancy system modulo six** associated with the stronger bordered cyclic difference-family target. It does not lift occupancies to binary subsets of `Z_v`, does not prove existence of the bordered cyclic family for arbitrary `v`, and does not resolve the unrestricted Hadamard conjecture.

No independent external mathematical review has been performed. The next useful target is quotient order seven, simultaneous quotient compatibility, or within-fiber binary lifting.
