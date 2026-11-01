# PROB20-05 — N=20 delivery and execution receipts

This append-only receipt belongs to `2026-09-16T13-02-07Z__report.md`.

## Main report

Path: `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/runs/2026-09-16/2026-09-16T13-02-07Z__report.md`

Creation commit: `0a1dc9d47709f760e587d13ac159eab6f2037f97`

Exact-commit readback blob: `b612ea530becd4bef4582e5cb598e8be27c70e22`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

## Phase-one exact checker

Path: `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T13-02-07Z__s11_n20_phase1_exact.cpp`

Creation commit: `3e0146886581cdc63c44c0b9aa7c50eece04908f`

Exact-commit readback blob: `8fd90ea075db0fdd1f7af9c77add31c5bb2dab45`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Final asserted outputs:

- `k=0`: universal `2867990/37048810`, fixed exact `36986700`, adaptive exact `60174`, remain `1936`, canonical reps `1215`, min fixed numerator `996323690560983`, min adaptive numerator `27407220037251`.
- `k=1`: universal `268044/39648756`, fixed `39639458`, adaptive `8974`, remain `324`, reps `234`, min fixed `1191558737095480`, min adaptive `240969994929840`.
- `k=2`: universal `0/39916800`, fixed `39913451`, remain `3349`, reps `2367`, min fixed `890404475049968`.
- `k=3`: universal `0/39916800`, fixed `39914916`, remain `1884`, reps `1299`, min fixed `7314982086837426`.
- `k=4`: universal `0/39916800`, fixed `39915381`, remain `1419`, reps `926`, min fixed `2259203795160716`.

Each finalized class terminated with `S11 N20 EXACT PHASE1 PASSED`.

Residual CSV SHA-256 digests:

- `k=0`: `b1d707298e729fe057ca32aaf66e5e66777bada375704b76a75c08b045ed7906`
- `k=1`: `1ead59d602ad27426104c652fa16b7a5cc0d3362762a405289c9e4e308f08ddc`
- `k=2`: `5740cad55fc9845a99f403102c8d605a909efed4c302fe02d6ec9eee1553825e`
- `k=3`: `21742f637d9402052b9665e171f815fe6f81679a1cf7d02eb4893b1500ca2318`
- `k=4`: `2bea5c1eee5db1230dcb37fb56a9118d70a5726fd91914c8d238340787952c48`

Execution note: a combined parallel finalized rerun hit the local execution window before `k=0` returned, while `k=1,...,4` completed. No result was inferred from the interrupted process. `k=0` was rerun separately and passed its hard-coded assertions.

## Exact cell postchecker

Path: `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T13-02-07Z__s11_n20_cell_postcheck.py`

Creation commit: `fb0471974c952f0a0d65901f3fa9d6f1e33c25de`

Exact-commit readback blob: `555ac1f5df99f344a38dd067ba3ed20c4cccf87b`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Final exact cell outputs:

- `k=0`: `total=1215 success=1213 min_success=1620`; failures identity `(-3120,W=74272)` and adjacent transposition `(-1260,W=74396)`.
- `k=1`: `234/233`, minimum `1620`; failure identity only.
- `k=2`: `2367/2366`, minimum `3600`; failure identity only.
- `k=3`: `1299/1298`, minimum `5340`; failure identity only.
- `k=4`: `926/925`, minimum `6960`; failure identity only.

All corrected invocations terminated with `EXACT S11 N20 CELL POSTCHECK PASSED`.

A first postchecker invocation accidentally reversed the two positional arguments and failed immediately with `ValueError`; no mathematical result was accepted from that failed invocation. The corrected invocations above are the certified ones.

## Dependency receipts

Newest prior theorem checkpoint read before this work:

`runs/2026-09-16/2026-09-16T12-02-10Z__report.md`, creation commit `36d100fbee179c3a071fb8afa3a9d6eb658b47ae`.

Independent adjacent-transposition theorem used for the sole nonidentity final residual:

`runs/2026-09-15/2026-09-15T15-08-40Z__report.md`, creation commit `4405249247bbca48e9bac56dd4ae2c046f376e1b`, blob `d19c79e9ff7e7fabcb2fb9eee279ee3115477dd6`.

No existing or peer files were overwritten. No access, workflow, settings, force-push, credential, public-posting, email, or Drive action was performed.
