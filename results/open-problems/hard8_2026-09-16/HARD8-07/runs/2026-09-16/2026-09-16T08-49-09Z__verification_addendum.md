# HARD8-07 — verification addendum

This append-only addendum records publication and readback receipts for the substantive checkpoint created in the same run.

## Main mathematical report

Path:

`hard8_2026-09-16/HARD8-07/runs/2026-09-16/2026-09-16T08-45-57Z__report.md`

Creation commit:

`b555694d1c1168921015e93193b04ce4ec505a92`

Readback was performed using that exact commit as the ref. The returned file path and content matched the report, with blob SHA:

`8ebb9c2f02797720bf07324b511ed49c1fd251b0`

Status: **VERIFIED**.

## Exact verifier artifact

Path:

`hard8_2026-09-16/HARD8-07/artifacts/2026-09-16T08-45-57Z__portal_cone_verifier.py`

Creation commit:

`86d3f1bd2434f50f5132e3732749cce98f2a55ef`

Readback was performed using that exact commit as the ref. The returned file path and content matched the verifier, with blob SHA:

`506aca22c6765aebe5acf8128273906fd578f5d4`

Status: **VERIFIED**.

## Local exact execution record

The verifier was executed before publication and returned:

```text
HARD8-07 exact portal/cone verifier: PASS
seed=2026091607 trials=500
wedge=2000
nested=1000
nonadjacent=500
canonical=487
modular=487
```

The script uses only Python standard-library integer arithmetic and `fractions.Fraction`. It checks algebraic identities and deterministic finite instances; it is not an independent verification of the open conjecture.

## Last completed mathematical step

The run ended after proving and archiving the critical-scale finite-portal equivalence: in the bounded-type hard core, Matala-aho's bounded-H `++` mechanism at the canonical integer scale

\[
B_{m+1}^3\le D_n^2<B_{m+2}^3
\]

is equivalent up to constants to a fixed portal

\[
q_n=zD_n+vD_{n+1}
\]

hitting the shrinking target

\[
\|q_n\alpha\|=O(D_n^{-1/3})
\]

infinitely often. The same report proves the exact nested `++` wedge geometry and shows that farther bracketing convergents gain angle only by paying exactly the same determinant in sublattice covolume.

The full classical Littlewood conjecture remains open.
