# HARD8-04 verification addendum — 2026-09-16T11:31:00Z

This append-only note records publication/readback receipts and exact execution results for the low-order quotient checkpoint.

## Main mathematical report

Path:

`hard8_2026-09-16/HARD8-04/runs/2026-09-16/2026-09-16T11-18-30Z__report.md`

Creation commit:

`3c4bb2078226830cf50c5c9e192f0e5c4a37c28f`

Exact-commit readback succeeded. Returned blob SHA:

`883e85da2bf73a7dcba61bdcf6538795b89d596a`

Status: **VERIFIED BY READBACK**.

## Exact verifier

Path:

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-16T11-18-30Z__quotient_obstruction_verifier.py`

Creation commit:

`0c83e7acb2bca0355513d6557abb36f594f51fbd`

Exact-commit readback succeeded. Returned blob SHA:

`f34b77ebd2e0f723a9bb57eb664e67d70d3499f3`

Status: **VERIFIED BY READBACK**.

The verifier was executed locally from the reviewed standard-library implementation using exact integer arithmetic. Its completed output was:

```text
exact d=2 quotient certificates: 2000
exact d=3 quotient certificates: 666
exact d=4 quotient certificates: 1000
all quotient autocorrelation identities verified for even v <= 4000
ALL EXACT LOW-ORDER QUOTIENT CHECKS PASSED
```

The run also checked, for every integer in the verifier's finite range, the elementary three-square escape conditions used by the constructive proofs. For every generated quotient certificate it checked:

1. nonnegative integer occupancies;
2. the exact block sizes `(v/2-1,v/2,v/2,v/2)`;
3. every periodic quotient autocorrelation equation, not merely a single Fourier norm;
4. all inverse-Fourier divisibility conditions in the `d=4` construction.

No floating-point acceptance condition, randomization, external solver, repository automation, or timeout-as-nonexistence inference was used.

## Scope limitation

These checks certify only the **quotient occupancy constructions** from the mathematical report. They do not lift the occupancies to four binary subsets of `Z_v`, and therefore do not prove existence of the bordered cyclic difference family or of Hadamard matrices at all orders.

The mathematical theorem in the report is stronger than the finite verifier range because its proof invokes Lagrange's four-square theorem and Legendre's three-square theorem. The finite run through `v=4000` is a consistency check of the explicit constructions, not the proof of their universal quantifiers.

The full Hadamard conjecture remains open. The next proposed obstruction/construction checkpoint is quotient order `d=5`, where the real cyclotomic field `Q(sqrt(5))` first enters and the low-order four-square/Eisenstein/Gaussian reductions no longer directly settle feasibility.
