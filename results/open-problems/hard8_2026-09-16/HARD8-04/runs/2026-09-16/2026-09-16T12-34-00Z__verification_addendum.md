# HARD8-04 verification addendum — 2026-09-16T12:34:00Z

This append-only note records exact publication/readback receipts and the deterministic consistency checks for the quotient-order-five checkpoint.

## Main mathematical report

Path:

`hard8_2026-09-16/HARD8-04/runs/2026-09-16/2026-09-16T12-22-41Z__report.md`

Creation commit:

`7026982f4fbfeb38be467c50728a92e4d04e2d37`

Exact-commit readback returned blob SHA:

`e6072c2ea22971cebf46fce11e71b1fe4b7bf53b`

Status: **VERIFIED BY READBACK**.

## Exact verifier

Path:

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-16T12-22-41Z__d5_quotient_verifier.py`

Creation commit:

`b45e0a77b0c1f12d447d0f523d9554c518b076b5`

Exact-commit readback returned blob SHA:

`ce216af97eee4cb59b4b86474d9d02d27c2e91fc`

Status: **VERIFIED BY READBACK**.

The reviewed verifier uses only Python standard-library exact integer arithmetic. No floating-point acceptance conditions, randomization, external solver, repository automation, or timeout-as-nonexistence inference are used.

## Exact output

Path:

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-16T12-22-41Z__d5_quotient_output.txt`

Creation commit:

`4d156aa5ece6a12915c43f922ddf4a9a8299b4e6`

Exact-commit readback returned blob SHA:

`80eb9f52ac7e29b1056bea201b5e9379c179114a`

Status: **VERIFIED BY READBACK**.

Completed output:

```text
BHARGAVA_HANKE_TEST_VALUES_VERIFIED 29
D5_QUOTIENT_CERTIFICATES_VERIFIED 500
ENERGY_SWAP_IDENTITIES_VERIFIED 1000
FINITE_RANGE s=1..500 v=10..5000
ALL_EXACT_D5_CHECKS_PASSED
```

The finite run checks all 29 explicit Bhargava--Hanke universality witnesses recorded in the report. It then constructs and verifies a valid modulo-five quotient certificate for every `s=1,...,500`, i.e. every compatible `v=10,...,5000`. For every such certificate it checks exact row sums, genuine fiber-capacity bounds, the multiplier-by-two energy swap, both cyclic energy equations, and all five periodic quotient autocorrelation equations.

The universal theorem in the report is stronger than this finite consistency range because its `A_4` norm lemma invokes the Bhargava--Hanke 290-Theorem after the 29 exact test values have been certified.

## Scope limitation

This checkpoint proves only universal feasibility of the **quotient occupancy system modulo five** for the stronger bordered cyclic parameter family. It does not lift the occupancies to four binary subsets of `Z_v`, does not prove that the bordered cyclic difference family exists at every even `v`, and does not resolve the Hadamard conjecture.

No independent external mathematical review has been performed. The next attack should examine quotient order six or seven, simultaneous quotient compatibility, or exact within-fiber binary lifting obstructions.
