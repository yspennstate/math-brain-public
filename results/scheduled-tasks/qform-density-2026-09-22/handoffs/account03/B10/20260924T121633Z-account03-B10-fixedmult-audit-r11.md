SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-24T12:16:33Z.
attacking: current superseding objective `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924` — full 17-eigenvalue manuscript audit with B10 constant/exact-arithmetic/adversarial-example lens.

## Source pins

- Current objective reread from `math-research-brain/main`; objective file SHA `7f4f8a699703674bc3475e6737bf08309794dc7b`.
- Fresh control head before publication: `f6fa86c76afdead4cff47cacd8622d7dfb1b5c99`.
- Pinned manuscript initial commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Advertised manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69` (not independently recomputed because advertised package checker files were absent).

## Result

I independently read all 790 lines and reconstructed every specialized dependency. Verdict: **PASS** for the pinned 17-eigenvalue theorem; no fatal mathematical gap found. This is one independent worker review, not the two-review validation certificate. Full three-eigenvalue QFORM remains OPEN. Global continuity remains unproved; the no-pivot Fourier branch has a continuous density, while pivot branches are established by essential-density domination.

New proved same-threshold improvement: the quarter-power coefficient is bounded elementarily by `35/8`, leading to `H(Q)<434` and full half-potential `<435` under nine large eigenvalues. Therefore the 17-eigenvalue theorem improves from `10000 K^2/s` to

`||p_Q||_infinity < 4350 K^2/s`.

Keeping exact source expressions yields `3210+400 log(16)+40/e = 4333.7506665...` in the dominant scalar-pivot branch.

New adversarial finite example: for

`A=(1/20)[[0,-1,-1],[-1,0,-1],[-1,-1,0]]`

with seed `S={1}, T={2}, L={3}`, there is no `eta=1/100` pivot, yet the manuscript completion has `rank R=3` and `rank R_LL=1`; direct sums give exact `3r` and `r` simultaneously. Thus those two rank constants cannot be improved from no-pivot structure alone. In the terminal order-five `r=4` chamber, `s_16` still forces only four large diagonal entries, compatible with restricted rank four; lowering 17 therefore needs extra combined sampling/large-spectrum structure or a different receiver. This is not a counterexample to a 16-eigenvalue theorem.

Packaging-only GAP: the current root did not contain the advertised `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, or `checks.json`.

## Durable outputs

- Full audit: `yspennstate/math-open-problems@4a53d82c3442126777a5eb16d28e6fceba6a165d:proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account03/B10/20260924T121633Z-account03-B10-fixedmult-audit-r11/AUDIT.md`
- Improvement proof: `yspennstate/math-open-problems@3567c4d364df768356a4ce4a9f401e0c46012b28:proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B10/20260924T121633Z-account03-B10-fixedmult-audit-r11/IMPROVEMENT.md`
- Exact/finite check record: `yspennstate/math-open-problems@0e09d541a8749be0b70a595cb5abaa4ab7559b2d:proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account03/B10/20260924T121633Z-account03-B10-fixedmult-audit-r11/CHECKS.json`

Readback of audit and improvement was verified after commit. Execution status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write is not native learned-memory ingestion.
