# account03/B13 handoff — 20260924T133300Z fixed-multiplicity audit r4

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924` (later owner objective; supersedes conflicting older per-run focus while preserving the unrestricted QFORM target as open).
Execution: `WITHOUT_VERIFIED_BRAIN`.
Pinned baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## New mathematics

`QFORM-FIXED-MULTIPLICITY-NINE-3078-v1`: for arbitrary independent real coordinate densities bounded by `K`, arbitrary symmetric `A`, arbitrary affine `b,c`,

` s_9(A)>=s>0  =>  ||p_(X^TAX+b^TX+c)||_infinity < 3078 K^2/s.`

Proof source: `yspennstate/math-open-problems@d9a4eeae28a70eb694e591b7ad0d96e0e78779fe`, path
`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B13/20260924T133300Z-account03-B13-fixedmult-audit-r4/IMPROVEMENT.md`.

The proof combines the checked account03/B04 marginal-free order-three density / order-two half-potential receivers with the B13 exact hyperbolic and singular-kernel improvements. The strengthened pivot bound is `H(Q)<306.75`; after the outer scalar-square profile the worst normalized branch is `<3077.5`, hence `<3078`.

The designated account04/B13 no-attainment purification is applied to the actual slab kernel, giving the exact normalized extremal-product statement

`sup_{cap-one product laws} P(Q in J)
 = sup_{|E_i|=1, bounded finite unions} |{x in prod E_i:Q(x) in J}|
 <3078 |J|`

under `s_9(A)>=1`, with no interval/centering/bounded-diameter/fixed-fragment assertion.

## Audit

Full B13 re-audit: `yspennstate/math-open-problems@d9a4eeae28a70eb694e591b7ad0d96e0e78779fe`, path
`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account03/B13/20260924T133300Z-account03-B13-fixedmult-audit-r4/REPORT.md`.

Baseline 17 theorem: PASS in this run, no fatal defect found. One nonfatal source wording repair remains in `lem:projection`: after omitting `b_i=0`, use `sum_{b_i>0}(1-b_i)<=d`, not equality; the `e^(d/2)` conclusion is unchanged. The earlier package gap is repaired: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json` are present.

## Remaining obstruction

An eight-eigenvalue theorem is not proved. The current `s_8` terminal state has three disjoint physical two-banks with a determinant-ratio lower bound but no absolute pair-minor floor. The next B13 mechanism should be a product-preserving three-bank/cycle receiver that consumes this ratio before reciprocal-minor payment. Indefinite rank-two density alone is logarithmically singular and cannot close the endpoint.

Full three-eigenvalue conjecture remains OPEN. Global continuity remains OPEN; the nine-eigenvalue no-pivot Fourier branch is continuous.
