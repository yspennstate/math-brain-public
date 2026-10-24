# PROB20-05 — n=19 delivery and execution receipts

This append-only receipt belongs to `2026-09-16T12-02-10Z__report.md`.

## Recovery backfill

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/backfill/2026-09-16T11-56-12Z__2026-09-16T11-02-34Z.md`

Creation commit: `6767d0b866ae2a98bb9571f7e5beef1faaf79bcd`

Exact-commit readback blob: `27a8a8e5288802f26ac994f3f5323b0ad24e4aee`

Status: VERIFIED BY EXACT-COMMIT READBACK.

This is the authentic retained `n=18` response from the preceding delivery-blocked run, with its original blocked/verified statuses preserved.

## Main report

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/runs/2026-09-16/2026-09-16T12-02-10Z__report.md`

Creation commit: `36d100fbee179c3a071fb8afa3a9d6eb658b47ae`

Exact-commit readback blob: `3089c83a126fac8119dd5937e526f7b5b438b98b`

Status: VERIFIED BY EXACT-COMMIT READBACK.

## Exact phase-one checker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T12-02-10Z__s11_n19_phase1_exact.cpp`

Creation commit: `bf9d0e22daf90375a93af30d4562018abe7f4853`

Exact-commit readback blob: `f6c7df508b00f0614eccab627305b87d5d62810b`

Status: VERIFIED BY EXACT-COMMIT READBACK.

The finalized source was compiled with `g++ -O3 -std=c++17` and executed separately on all five reflection classes. Each completed with its hard-coded exact census assertion and printed `S11 N19 EXACT PHASE1 PASSED`.

Final outputs:

- `k=0`: universal pass `6,935,898`; universal fail `32,980,902`; deterministic exact pass `32,914,915`; adaptive exact pass `63,954`; nonzero adaptive tilings `132`; residual `2,033`; canonical reps `1,277`; deterministic minimum lower numerator `804047211151938`; adaptive minimum lower numerator `16194182462904`.
- `k=1`: universal pass `1,683,006`; universal fail `38,233,794`; deterministic exact pass `38,223,239`; adaptive exact pass `10,176`; nonzero adaptive tilings `64`; residual `379`; canonical reps `261`; deterministic minimum lower numerator `622076634922764`; adaptive minimum lower numerator `11682544682123160`.
- `k=2`: universal pass `140,238`; universal fail `39,776,562`; deterministic exact pass `39,772,416`; adaptive stage not used; residual `4,146`; canonical reps `2,914`; deterministic minimum lower numerator `489052982827420`.
- `k=3`: universal pass `0`; universal fail `39,916,800`; closest universal margin `-9208`; deterministic exact pass `39,914,279`; adaptive stage not used; residual `2,521`; canonical reps `1,734`; deterministic minimum lower numerator `956561238099968`.
- `k=4`: universal pass `0`; universal fail `39,916,800`; closest universal margin `-23608`; deterministic exact pass `39,914,630`; adaptive stage not used; residual `2,170`; canonical reps `772`; deterministic minimum lower numerator `15148130227830432`.

The finalized residual CSV SHA-256 digests were:

- `k=0`: `4c1db43e69dcb3da23a28ea124df322928f21af8d40344bd1c86a4be9eebed30`
- `k=1`: `fceb9fd23005d9db86ef7f9c43276df53a4e20f1c9418195bd8fc97f2b763935`
- `k=2`: `ef71ec9ddb086fa084504a67a212a26f24220c76890531b602e1dcb05e06b66e`
- `k=3`: `f7194df5f8bb73cc3f2e2312d67a8da6cc00e03a1128dc94300cd716c55cb684`
- `k=4`: `6c50b54eadf28387b9c5396227a43c585cb8a708320eb959c58d7923f26874be`

## Exact cell postchecker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T12-02-10Z__s11_n19_cell_postcheck.py`

Creation commit: `8ed9f579fbd681dbb05c54860f737d055cf425d4`

Exact-commit readback blob: `39a0415b7a01fe7ee308cb71c3a5610a24e1315a`

Status: VERIFIED BY EXACT-COMMIT READBACK.

The finalized checker was run on all five finalized residual CSVs. Each class passed its exact expected total/success/minimum/failure assertions and printed `EXACT S11 N19 CELL POSTCHECK PASSED`.

Results:

- `k=0`: total `1277`, successes `1275`, minimum success margin `1980`; failures are identity `(margin=-2400,W=60488)` and the global rightmost adjacent transposition `(margin=-720,W=60600)`.
- `k=1`: total `261`, successes `260`, minimum success margin `1980`; only identity fails.
- `k=2`: total `2914`, successes `2913`, minimum success margin `3840`; only identity fails.
- `k=3`: total `1734`, successes `1733`, minimum success margin `5460`; only identity fails.
- `k=4`: total `772`, successes `771`, minimum success margin `6900`; only identity fails.

Identity is the diagonal equality case. The sole nonidentity cell failure is a single adjacent transposition and is independently covered by the archived all-resolution adjacent-transposition transport at commit `4405249247bbca48e9bac56dd4ae2c046f376e1b`.

## Execution notes / failures

Two combined local shell wrappers exceeded their per-call execution windows after one or more already-completed class runs. No mathematical result was inferred from either timeout. The incomplete classes were rerun separately; every finalized phase-one class and every finalized cell class then completed and passed its hard-coded assertions.

There was no GitHub security/approval denial in this run. No existing file was overwritten, no workflow/settings/access was changed, and no email/Drive/public delivery was attempted.

## Final checkpoint status

The complete eleven-bin positive-shuffle theorem at `n=19` is self-checked and archived. The full continuum conjecture remains open. The next finite checkpoint is `n=20`.
