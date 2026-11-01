# PROB20-05 — `n=12` eleven-bin checkpoint delivery receipts

This append-only receipt accompanies

`runs/2026-09-16/2026-09-16T05-04-48Z__report.md`.

## Main report

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/runs/2026-09-16/2026-09-16T05-04-48Z__report.md`

Creation commit:

`d0dadbe9a04cc04364e2c74c13ff85e01311770e`

Exact-commit readback blob:

`731cc16af50ef20df8fd287ee8c854e8801e325a`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

## Phase-1 / domino census source

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T05-04-48Z__s11_n12_phase1_domino.cpp`

Creation commit:

`b2e0d3463708d2c8a8a08ac74faf2b94841c5572`

Exact-commit readback blob:

`5d5c799c4f099fddb61eb9b394b3633d188711a3`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Successful local checker output from the archived source was:

```text
total=39916800
universal_pass=39049390 universal_fail=867410 min_pass=2 max_fail=-8
fixed_pass=610996 fixed_unique_tuples=49641
adaptive_pass=8820 uses=0,993,3325,1452,3050 adaptive_unique_tuples=453
remain=247594 canonical_reps=144834
EXACT/LOCATOR S11 N12 PHASE1+DOMINO CENSUS PASSED
```

The C++ checker can optionally emit the two coefficient-tuple CSVs and the canonical representative CSV used by the postchecker. These generated data files were not separately uploaded because they are reproducible outputs of the archived source.

## Exact radical/cell postcheck source

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T05-04-48Z__s11_n12_exact_postcheck.py`

Creation commit:

`f17f18868ad87d3052dc8e998b708fdc5a33baa4`

Exact-commit readback blob:

`6dfe64be2490a1a44512967f6b9c1fa9e2f11358`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Successful exact radical output was:

```text
fixed tuple count=49641
minimum rigorous lower bound = 58468275106451/1089000000000000000
minimum tuple = (27,64,9,46,99,0)
adaptive tuple count=453
minimum rigorous lower bound = 884512957239853/1089000000000000000
minimum tuple = (25,62,13,-1,74,70)
EXACT S11 N12 RADICAL POSTCHECK PASSED
```

The full `144,834` canonical representative cell stage was executed in four disjoint bounded chunks. Their exact post-check census was:

```text
chunk 1: checked 36209, successes 36207, failures 2, min success margin 1056
chunk 2: checked 36208, successes 36208, failures 0, min success margin 7836
chunk 3: checked 36209, successes 36209, failures 0, min success margin 1896
chunk 4: checked 36208, successes 36208, failures 0, min success margin 5796
```

The two exact cell failures were

```text
identity: (0,1,2,3,4,5,6,7,8,9,10,11), margin -1104
adjacent swap: (0,1,2,3,4,5,6,7,8,9,11,10), margin -264
```

They are handled analytically in the main report; the adjacent case cites the archived all-resolution adjacent-transposition theorem at creation commit `4405249247bbca48e9bac56dd4ae2c046f376e1b`.

## Delivery status

All three new UTF-8 files for this checkpoint were committed successfully and read back at their exact creation commits. No security/approval denial occurred in this delivery.
