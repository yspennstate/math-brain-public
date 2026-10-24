# PROB20-05 n=15 checkpoint — append-only delivery/check receipts

This receipt part records actual GitHub creation commits, exact-commit readbacks, and finalized local checker outputs for the mathematical report `2026-09-16T07-59-34Z__report.md`.

## 1. Main mathematical report

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/runs/2026-09-16/2026-09-16T07-59-34Z__report.md`

Creation commit:

`dc9c49ed09868122d70611e681b78df02d3e3f3a`

Exact-commit readback returned blob SHA:

`01581267af63cdc99986bda2139eadcf60a8441e`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

## 2. Phase-one / 891-domino enumerator

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T07-59-34Z__s11_n15_phase1_all_domino.cpp`

Creation commit:

`2807c08a7e1606cffecca9a8be4abf82487a658c`

Exact-commit readback returned blob SHA:

`0991b5000b20a4c5987c33f10e1f90a97f184c03`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

The finalized source contains hard-coded census assertions. The observed runs were:

```text
k=0 total=39916800
universal_pass=31144808 universal_fail=8771992 min_pass=0 max_fail=-10
fixed_pass=8627634 fixed_unique_tuples=351224
adaptive_pass=139389 nonzero_tilings=192 adaptive_unique_tuples=9856
remain=4969 canonical_reps=2954
S11 N15 PHASE1 + ALL-891-DOMINO CENSUS PASSED
```

```text
k=1 total=39916800
universal_pass=26621124 universal_fail=13295676 min_pass=0 max_fail=-10
fixed_pass=13259950 fixed_unique_tuples=477114
adaptive_pass=34436 nonzero_tilings=115 adaptive_unique_tuples=2985
remain=1290 canonical_reps=742
S11 N15 PHASE1 + ALL-891-DOMINO CENSUS PASSED
```

```text
k=2 total=39916800
universal_pass=24484885 universal_fail=15431915 min_pass=0 max_fail=-10
fixed_pass=15407600 fixed_unique_tuples=526550
adaptive_pass=23424 nonzero_tilings=108 adaptive_unique_tuples=2323
remain=891 canonical_reps=309
S11 N15 PHASE1 + ALL-891-DOMINO CENSUS PASSED
```

## 3. Exact radical + balanced-cell postchecker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T07-59-34Z__s11_n15_exact_postcheck.py`

Creation commit:

`0ed62d4959e842ee999d8d8855fd54c811eccdd6`

Exact-commit readback returned blob SHA:

`c58f3144489c89a70c33056ed59660437f36880b`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Observed finalized postcheck output:

```text
k0_fixed count=351224 min_lower_num=464700117651048 den=5445000000000000000 tuple=(27,62,11,51,68,0)
k0_adapt count=9856 min_lower_num=262254931637784 den=5445000000000000000 tuple=(22,67,11,30,45,8)
k1_fixed count=477114 min_lower_num=1748832501837588 den=5445000000000000000 tuple=(25,66,9,68,23,0)
k1_adapt count=2985 min_lower_num=2422750720161648 den=5445000000000000000 tuple=(26,69,5,26,6,50)
k2_fixed count=526550 min_lower_num=6847256973591904 den=5445000000000000000 tuple=(29,61,10,69,41,0)
k2_adapt count=2323 min_lower_num=6847256973591904 den=5445000000000000000 tuple=(29,61,10,9,1,100)
k0_reps total=2954 success=2952 min_success=1620 failures=[identity, one adjacent transposition]
k1_reps total=742 success=741 min_success=1620 failures=[identity]
k2_reps total=309 success=308 min_success=3000 failures=[identity]
EXACT S11 N15 RADICAL + CELL POSTCHECK PASSED
```

The postchecker uses exact integer squaring to certify `10^-15` radical enclosures and exact integer recomputation of all cell-assignment margins. The displayed condensed failure labels correspond to the full asserted permutation tuples in the archived source.

## 4. Delivery conclusion

All primary mathematical Markdown and both reproducibility sources for this checkpoint have actual creation commits and exact-commit readbacks. No delivery operation in this checkpoint is being labeled VERIFIED without readback.

The theorem proved in the main report is the complete eleven-bin positive-shuffle theorem at global resolution `n=15`; the full continuum Catalano–Lavenant conjecture remains open.
