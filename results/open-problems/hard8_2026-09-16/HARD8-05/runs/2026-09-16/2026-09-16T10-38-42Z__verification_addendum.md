# HARD8-05 verification addendum — saturation-subgroup checkpoint

This append-only receipt records the exact GitHub commits/readbacks and the completed deterministic verification run for the checkpoint beginning at `2026-09-16T10-31-10Z`.

## 1. Mathematical report

Path:

`hard8_2026-09-16/HARD8-05/runs/2026-09-16/2026-09-16T10-31-10Z__report.md`

Creation commit:

`8279a8b140d16903d6ba344e1049e8c6b78dabc2`

Exact-commit readback succeeded. GitHub content blob SHA:

`b030fd1827b0e867b658cdfaeb20ab436af90b81`

Status: **VERIFIED BY EXACT-SHA READBACK.**

## 2. Exact standard-library verifier

Path:

`hard8_2026-09-16/HARD8-05/artifacts/2026-09-16T10-31-10Z__saturation_escape_verifier.py`

Creation commit:

`9b270a193b28443bf81304b86b0575110e176be2`

Exact-commit readback succeeded. GitHub content blob SHA:

`068f0e17059cfcfdc55115337ad410b8b004ad08`

Status: **VERIFIED BY EXACT-SHA READBACK.**

## 3. Escape-subgroup data

Path:

`hard8_2026-09-16/HARD8-05/artifacts/2026-09-16T10-31-10Z__escape_subgroups.csv`

Creation commit:

`a1b568c4c8fce331dc95d53390b263d83dfa46c3`

Exact-commit readback succeeded. GitHub content blob SHA:

`dc94b11bfd9a36608801545ffa5a4e5b30677d61`

Status: **VERIFIED BY EXACT-SHA READBACK.**

## 4. Actual execution record

The archived verifier source was executed before publication. The mathematical script completed with process return code `0` and printed:

```text
hard primes <= 4,300,000: 37716
signature checks m16/m20: (2048, 79) (2048, 79)
minimal portal depth counts: {1: 19162, 2: 16554, 3: 1695, 4: 211, 5: 82, 6: 10, 7: 1, 8: 1}
depth >= 6: [(53089, (6, 1, 6, 1295)), (345601, (7, 7, 2, 279)), (670321, (6, 1, 6, 119)), (670849, (8, 1, 8, 319)), (830041, (6, 1, 6, 23)), (1113961, (6, 6, 5, 61319)), (1350001, (6, 1, 6, 32927)), (1372849, (6, 1, 6, 1199)), (1445161, (6, 6, 1, 211487)), (2176729, (6, 1, 6, 95)), (2188729, (6, 1, 6, 11831)), (4010161, (6, 6, 1, 119))]
m40 failed portal counts: {(2, 5): 24502, (5, 2): 32991}
m40 min-exception distributions: {'(2, 5)': {0: 18118, 1: 5969, 2: 388, 3: 27}, '(5, 2)': {0: 27623, 1: 5276, 2: 1, 3: 91}}
ALL CHECKS PASSED
```

The same run also printed the complete maximal `-1`-avoiding subgroup table for moduli `16,20,32,40,48,56,60,80,120`; that table is preserved verbatim in the CSV artifact.

The Python environment emitted a non-fatal spreadsheet-runtime warmup timeout to stderr after the verifier output. This warning was unrelated to the standard-library verifier; the script itself returned code zero and all assertions had completed.

## 5. What the verifier checked

1. all `2048` capped signatures modulo 16 and all `2048` capped signatures modulo 20;
2. the prior exact `79` failure count in each `C4 x C2` case;
3. every maximal subgroup avoiding `-1` for the nine listed moduli;
4. that each corresponding quotient is cyclic of 2-power order and has `-1` as its unique order-two element;
5. the exact six modulus-40 maximal avoiding subgroups and budgets `8` or `16`;
6. every prime `n <= 4,300,000` with `n == 1 mod24`;
7. every ordered coprime portal pair with `1 <= a,u <= 8` until the exact minimum depth was reached;
8. an actual divisor `s` and exact positive `(x,y,z)` identity for every one of the `37,716` finite census primes;
9. the reciprocal gcd identity for `(2,5)/(5,2)` across the entire finite range;
10. the saturation theorem on every failed modulus-40 reciprocal portal in the range;
11. the exact minimum-exception distributions;
12. the explicit `n == 97 mod120` unit-fraction identity on a deterministic progression.

No floating point, randomization, external solver, or timeout-based mathematical inference was used.

## 6. Scope

The full Erdős–Straus conjecture remains **OPEN**. The saturation/maximal-escape theorem and the class-`97 mod120` identity are exact symbolic results. The depth-eight coverage and exception distributions are bounded experiments only and are not universal closure evidence.
