# HARD8-05 verification addendum — subset-product exception budgets

This append-only receipt records the actual GitHub writes, exact-commit readbacks, and deterministic executions for the checkpoint beginning at `2026-09-16T11-32-10Z`.

## 1. Main mathematical report

Path:

`hard8_2026-09-16/HARD8-05/runs/2026-09-16/2026-09-16T11-32-10Z__report.md`

Creation commit:

`b39ea1dc29738d19933e0ec8777b9b3173578362`

Exact-commit readback blob SHA:

`a67fe03e1fb1d1f6e0399527c8aa6c18aecf1a58`

Status: **VERIFIED BY EXACT-SHA READBACK.**

## 2. Exact subset-product verifier

Path:

`hard8_2026-09-16/HARD8-05/artifacts/2026-09-16T11-32-10Z__subset_product_budget_verifier.py`

Creation commit:

`b25400a70a1ac3273bb7f2f09a3c27c73dd3efa5`

Exact-commit readback blob SHA:

`e0b9a91798f40b1f6bbeb60163f074386246f0f3`

Status: **VERIFIED BY EXACT-SHA READBACK.**

The archived source was also fetched in full at that creation SHA.

## 3. Exact budget table

Path:

`hard8_2026-09-16/HARD8-05/artifacts/2026-09-16T11-32-10Z__subset_product_budgets.csv`

Creation commit:

`29579f001b3a5c4f7a80de9fac2c4be9881cddb8`

Exact-commit readback blob SHA:

`687c9bfb2d9cf8df1d1b26255bfd833f1faec6db`

Status: **VERIFIED BY EXACT-SHA READBACK.**

## 4. Reciprocal-pair obstruction report

Path:

`hard8_2026-09-16/HARD8-05/runs/2026-09-16/2026-09-16T11-37-38Z__report_part2_reciprocal_obstruction.md`

Creation commit:

`108aa2b64ef86ad18914dcff235fefce25c4c89b`

Exact-commit readback blob SHA:

`9d5b794a78354ddff32d5b9329e98acefa86f44c`

Status: **VERIFIED BY EXACT-SHA READBACK.**

## 5. Reciprocal-pair exact verifier

Path:

`hard8_2026-09-16/HARD8-05/artifacts/2026-09-16T11-37-38Z__reciprocal_obstruction_verifier.py`

Creation commit:

`a51191ffd806ba9012c8e0f3f755a08c8e49974d`

Exact-commit readback blob SHA:

`25006a3032012bba0dc389ee82d57a84c595ef1f`

Status: **VERIFIED BY EXACT-SHA READBACK.**

The archived source was fetched in full at that creation SHA.

## 6. Actual execution — subset-product verifier

The standard-library verifier completed with return code zero and printed:

```text
budget table: index, old, complement, exact
16 {(2, 4, 4, 4): 2, (4, 8, 4, 4): 1}
20 {(2, 4, 4, 4): 2, (4, 8, 4, 4): 1}
32 {(2, 28, 28, 24): 2, (4, 52, 28, 28): 1, (8, 56, 28, 28): 1}
40 {(2, 8, 8, 8): 4, (4, 16, 8, 8): 2}
48 {(2, 8, 8, 8): 4, (4, 16, 8, 8): 2}
56 {(2, 32, 32, 16): 4}
60 {(2, 8, 8, 8): 4, (4, 16, 8, 8): 2}
80 {(2, 24, 24, 16): 4, (4, 40, 24, 20): 6}
120 {(2, 16, 16, 16): 8, (4, 32, 16, 16): 4}
mod40 fixed-total exception lengths {7: [(1, 3, 5, 7), (1, 3, 5, 7), (0, 2, 4, 6, 8), (1, 3, 5, 7), (0, 2, 4, 6, 8), (1, 3, 5, 7)], 23: [(1, 3, 5, 7), (1, 3, 5, 7), (0, 2, 4, 6, 8), (1, 3, 5, 7), (0, 2, 4, 6, 8), (1, 3, 5, 7)]}
hard unit residues mod840 24
fixed-q covered 18 residual (1, 121, 169, 289, 361, 529)
fixed-q exact identity checks 54
maximal avoiding subgroups checked 54
ALL_CHECKS_PASSED
```

The verifier used exact integer/bitset state only. It enumerated all maximal `-1`-avoiding subgroups for the nine tracked moduli and optimized target-free exceptional multisets by dynamic programming over exact reachable residue products.

## 7. Actual execution — reciprocal obstruction verifier

The exact verifier completed with return code zero and printed:

```text
n 1201 mod840 361
N1 divisors/residues [(1, 1), (29, 29), (83, 3), (2407, 7)]
N2 divisors/residues [(1, 1), (6007, 7)]
rescue {'a': 4, 'u': 1, 's': 31, 'q': 155, 't': 2, 'x': 310, 'y': 1489240, 'z': 9608}
ALL_CHECKS_PASSED
```

This proves exactly that both reciprocal modulus-40 portals fail at the hard prime `n=1201`, while the `(4,1)` modulus-16 portal gives a valid Erdős–Straus decomposition.

## 8. Scope and review requirement

The full Erdős–Straus conjecture remains **OPEN**. The exact subset-product budget theorem and complement-pair lemma are symbolic deductions. The listed `B_m^*(K)` values are exact finite combinatorial certificates for the specified moduli. The `n=1201` result is a counterexample only to the proposed reciprocal-portal sub-strategy, not to Erdős–Straus itself.

No independent external review has been performed; self-checking plus deterministic code is not independent verification.