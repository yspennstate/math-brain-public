# PROB20-05 n=14 checkpoint — delivery receipts and executed checks

This append-only receipt supplements `2026-09-16T06-54-31Z__report.md`.

## GitHub delivery receipts

### Main mathematical report

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/runs/2026-09-16/2026-09-16T06-54-31Z__report.md`

Creation commit:

`617957261419efecc3243ffd4a21242b07f64545`

Read back at that exact commit. Returned blob SHA:

`b2687d9b14cdcbc9b3fb6dc95ed19a8f8058e3d8`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

### Phase-one / complete 891-domino census source

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T06-54-31Z__s11_n14_phase1_all_domino.cpp`

Creation commit:

`ce69a94518a55c4d660f0b5f26c4050b6b57fa5d`

Read back at that exact commit. Returned blob SHA:

`b2b78c921548c20428eb5377626f4320e371db22`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

### Exact radical and cell postchecker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T06-54-31Z__s11_n14_exact_postcheck.py`

Creation commit:

`42afe0d72190a424658437b24805e6bde78497e2`

Read back at that exact commit. Returned blob SHA:

`e26cdc2d298d931919178d46d4b5fbde5604f462`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

## Actual successful checker outputs

Finalized C++ at `k=0`:

```text
k=0 total=39916800
universal_pass=35107045 universal_fail=4809755 min_pass=2 max_fail=-8
fixed_pass=4604655 fixed_unique_tuples=233615
adaptive_pass=196558 nonzero_tilings=212 adaptive_unique_tuples=15594
remain=8542 canonical_reps=4941
S11 N14 PHASE1 + ALL-891-DOMINO CENSUS PASSED
```

Finalized C++ at `k=1`:

```text
k=1 total=39916800
universal_pass=33008145 universal_fail=6908655 min_pass=2 max_fail=-8
fixed_pass=6839065 fixed_unique_tuples=319843
adaptive_pass=67062 nonzero_tilings=161 adaptive_unique_tuples=6205
remain=2528 canonical_reps=1254
S11 N14 PHASE1 + ALL-891-DOMINO CENSUS PASSED
```

Exact postchecker:

```text
k0 deterministic tuples: count=233615, min lower numerator=54001491708670 over 2541000000000000000
k0 adaptive tuples: count=15594, min lower numerator=252900108282995 over 2541000000000000000
k1 deterministic tuples: count=319843, min lower numerator=607489394543570 over 2541000000000000000
k1 adaptive tuples: count=6205, min lower numerator=1547284545289580 over 2541000000000000000
k0 cell reps: total=4941, success=4939, min success=1260; failures exactly identity and (0,1,2,3,4,5,6,7,8,9,10,11,13,12)
k1 cell reps: total=1254, success=1253, min success=1260; failure exactly identity
EXACT S11 N14 RADICAL + CELL POSTCHECK PASSED
```

The adjacent-swap residual is closed by the previously archived explicit all-resolution adjacent-transposition theorem at commit `4405249247bbca48e9bac56dd4ae2c046f376e1b`; identity is the diagonal equality case.

## Execution note

A shell invocation that attempted to execute both finalized C++ position classes under one 180-second wrapper completed and printed the full successful `k=0` result, but the wrapper timed out before returning the `k=1` result. The finalized `k=1` program was therefore executed separately and completed successfully with its hard-coded census assertions. No unchecked result was inferred from the timed-out wrapper.

## Mathematical status

The `n=14` eleven-consecutive-bin theorem is proved/self-checked by the archived explicit certificates. The full Catalano–Lavenant continuum conjecture remains open; this checkpoint does not claim a continuum extreme-copula classification or uniqueness.
