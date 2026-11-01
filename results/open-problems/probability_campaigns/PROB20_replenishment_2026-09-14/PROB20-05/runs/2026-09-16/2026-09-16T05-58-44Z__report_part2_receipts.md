# PROB20-05 delivery receipts — 2026-09-16T05-58-44Z checkpoint

All files below were created append-only on existing branch `master` and then fetched back using the exact write commit SHA.

## Main mathematical report

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/runs/2026-09-16/2026-09-16T05-58-44Z__report.md`

Creation commit:

`d58713928db60ded73719b12e47a89ce96c4d6ee`

Exact-commit readback blob SHA:

`e0321d84355e54f0c8d5c89baaa1d043ab2f0ac6`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

## Phase-one / domino census checker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T05-58-44Z__s11_n13_phase1_domino.cpp`

Creation commit:

`b4ad8f117562221f132b4e6562a50a7d665176e0`

Exact-commit readback blob SHA:

`c4c413f076ab5a401e5812ab84ba895e16a743cc`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Successful local outputs before upload:

```text
k=0 total=39916800
universal_pass=37659311 universal_fail=2257489 min_pass=2 max_fail=-8
fixed_pass=1995003 fixed_unique_tuples=127855
adaptive_pass=77697 uses=0,26328,26821,13816,10732 adaptive_unique_tuples=3342
remain=184789 canonical_reps=144849
EXACT/LOCATOR S11 N13 PHASE1+DOMINO CENSUS PASSED

k=1 total=39916800
universal_pass=37109281 universal_fail=2807519 min_pass=2 max_fail=-8
fixed_pass=2634546 fixed_unique_tuples=165348
adaptive_pass=68119 uses=0,34929,18932,8977,5281 adaptive_unique_tuples=2936
remain=104854 canonical_reps=58765
EXACT/LOCATOR S11 N13 PHASE1+DOMINO CENSUS PASSED
```

## Exact radical / cell postchecker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T05-58-44Z__s11_n13_exact_postcheck.py`

Creation commit:

`af2f58c97980841f4c242baac44bdbf609c3344f`

Exact-commit readback blob SHA:

`2125a389695fc7913d23935f918f4e2326135f09`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Successful exact radical tuple output before upload:

```text
k0 fixed: count=127855, min lower=7081914994511/196625000000000000, tuple=(21,67,12,56,42,0)
k0 adaptive: count=3342, min lower=142364791528987/294937500000000000, tuple=(28,63,9,8,39,90)
k1 fixed: count=165348, min lower=109222340349379/78650000000000000, tuple=(32,58,10,41,124,0)
k1 adaptive: count=2936, min lower=218061138318209/235950000000000000, tuple=(36,55,9,6,96,90)
EXACT S11 N13 RADICAL TUPLE POSTCHECK PASSED
```

The cell checker was run in eight disjoint ranges whose unions exactly cover the two sorted representative files. Aggregate results:

```text
k=0/k=2 class: 144849 representatives, 144847 successes, 2 certificate failures, global minimum success margin 1416.
Failures: identity margin -1104; adjacent transposition (0,1,2,3,4,5,6,7,8,9,10,12,11) margin -144.

k=1 central class: 58765 representatives, 58764 successes, 1 certificate failure, global minimum success margin 1416.
Failure: identity margin -1104.
```

The negative cell-certificate margins are not counterexamples; identity is equality and the adjacent transposition is covered by the archived all-resolution theorem at creation commit `4405249247bbca48e9bac56dd4ae2c046f376e1b`.

## Recorded checker failure

An initial local draft of the exact radical postchecker used incorrect expected-minimum constants for two tuple files and stopped on an assertion. The tuple signs themselves were positive. The minima were recomputed exactly, the expected constants corrected, and the checker rerun successfully. The corrected checker is the archived artifact above.
