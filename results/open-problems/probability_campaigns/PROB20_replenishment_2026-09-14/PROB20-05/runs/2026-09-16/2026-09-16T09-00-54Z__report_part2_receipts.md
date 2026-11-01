# PROB20-05 — n=16 checkpoint delivery receipts

This append-only receipt records the actual GitHub creation commits, exact-commit readbacks, and finalized checker outputs for the `2026-09-16T09-00-54Z` checkpoint.

## Main mathematical report

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/runs/2026-09-16/2026-09-16T09-00-54Z__report.md`

Creation commit:

`cffe2970bfeb94e82f75f94d66c905f1e448f7ee`

Exact-commit readback blob:

`7106c6cde1d877003eec7794751703fb9ebcaf48`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

## Phase-one / all-891-domino checker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T09-00-54Z__s11_n16_phase1_all_domino.cpp`

Creation commit:

`41d797a2ef735947c59d4d8e639a7a23633a03f6`

Exact-commit readback blob:

`13750ada48595152ced9302980d6c5bcc63e8252`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Finalized asserted executions:

`k=0 total=39916800`

`universal_pass=25769333 universal_fail=14147467 min_pass=2 max_fail=-8`

`fixed_pass=14040832 fixed_unique_tuples=468848`

`adaptive_pass=103157 nonzero_tilings=165 adaptive_unique_tuples=7004`

`remain=3478 canonical_reps=2115`

`S11 N16 PHASE1 + ALL-891-DOMINO CENSUS PASSED`

`k=1 total=39916800`

`universal_pass=18836094 universal_fail=21080706 min_pass=2 max_fail=-8`

`fixed_pass=21058170 fixed_unique_tuples=610209`

`adaptive_pass=21723 nonzero_tilings=96 adaptive_unique_tuples=1845`

`remain=813 canonical_reps=506`

`S11 N16 PHASE1 + ALL-891-DOMINO CENSUS PASSED`

`k=2 total=39916800`

`universal_pass=14283783 universal_fail=25633017 min_pass=2 max_fail=-8`

`fixed_pass=25620447 fixed_unique_tuples=686413`

`adaptive_pass=12130 nonzero_tilings=80 adaptive_unique_tuples=1288`

`remain=440 canonical_reps=247`

`S11 N16 PHASE1 + ALL-891-DOMINO CENSUS PASSED`

A combined wrapper execution returned the fully successful `k=0` output and then hit its execution limit before returning the later classes. The `k=1` and `k=2` finalized binaries were therefore rerun separately; the outputs above are from those completed separate runs. Nothing was inferred from the interrupted wrapper.

## Exact radical and balanced-cell postchecker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T09-00-54Z__s11_n16_exact_postcheck.py`

Creation commit:

`14b890cac9508560615d0a86f5a0177d7764eea6`

Exact-commit readback blob:

`a0b0631ee9069713028466fcf2c8e2cdd2c7bb36`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Successful exact-postcheck summary:

- `k=0` deterministic tuples: `468848`, minimum rigorous lower numerator `31272940599700` over denominator `726000000000000000`.
- `k=0` adaptive tuples: `7004`, minimum lower numerator `91923809202400`.
- `k=1` deterministic tuples: `610209`, minimum lower numerator `370786206072638`.
- `k=1` adaptive tuples: `1845`, minimum lower numerator `21811280673024`.
- `k=2` deterministic tuples: `686413`, minimum lower numerator `659667425678029`.
- `k=2` adaptive tuples: `1288`, minimum lower numerator `1128085956891390`.
- `k=0` cell representatives: `2115`, exact successes `2113`, minimum successful integer margin `1380`; failures are identity and one adjacent transposition.
- `k=1` cell representatives: `506`, exact successes `505`, minimum successful margin `1380`; sole failure identity.
- `k=2` cell representatives: `247`, exact successes `246`, minimum successful margin `2820`; sole failure identity.

Final line:

`EXACT S11 N16 RADICAL + CELL POSTCHECK PASSED`

## Mathematical status

The complete eleven-bin positive-shuffle case is now proved/self-checked for global resolutions `n=11,12,13,14,15,16`. The full continuum Catalano–Lavenant conjecture remains open, and this receipt does not claim independent external or formal verification.