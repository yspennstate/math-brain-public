Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6/maximum was requested, but the scheduler exposes no model selector or reasoning-effort selector, so I do not claim otherwise.

# HARD8-01 — verification addendum for 2026-09-16T16-08-55Z checkpoint

Status remains **OPEN / PARTIAL**. Fixed fleet metric remains **7 -> 7, no movement**. This note records creation receipts and exact-commit readbacks only; it does not add a new theorem claim.

## VERIFIED immutable report

- Path: `hard8_2026-09-16/HARD8-01/runs/2026-09-16/2026-09-16T16-08-55Z__report.md`
- Creation commit: `1cda49064e946da064aaf41195616f93637e89ef`
- Exact-commit readback blob: `08800d6c36fc09c4673d78bf94162757ea84e568`
- State: **VERIFIED**.

## VERIFIED code/data artifacts

1. `hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T16-08-55Z__two_cyclic_perm_fast.cpp`
   - creation commit `80e56d4fe01229eac70895905f0d1627519754a1`
   - readback blob `0392204a3c75dbfbc5f4ff4d765d0010497c1302`
   - **VERIFIED**.

2. `hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T16-08-55Z__two_cyclic_n10_n11_output.txt`
   - creation commit `cfad602dc160955ac43494558f780e4fe7a87e33`
   - readback blob `6d047d7b9a863d19d24e3a55159e9d82bda4bff8`
   - exact-SHA readback includes terminal PASS records for n=11 q=3 and q=4 and the q=4 totals `TESTED 22305218`, `SYNCHRONIZING 2026527`, `VIOLATIONS 0`, `MAX_RT 100`, with k=2 `TESTED 21899735`, `SYNCHRONIZING 2020137`, `MAX_RT 90`.
   - **VERIFIED**.

3. `hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T16-08-55Z__one_perm_fast.cpp`
   - creation commit `54c670cc2b9f9c8246a23be18eeddc77815d29fc`
   - readback blob `83cba34d4b9b40f3803f44b4ddeb69f54bf02450`
   - **VERIFIED**.

4. `hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T16-08-55Z__one_perm_n10_n11_output.txt`
   - creation commit `41ba9bc9966d6741eeab3f81dfe00c54e612d525`
   - readback blob `1ef5495261a47c1a108bc08cf8ae653ce8a375ec`
   - exact-SHA readback includes terminal `ALL_EXACT_AT_MOST_ONE_PERM_CHECKS_PASSED n=11 q=4`, total `TESTED 12427856`, `SYNCHRONIZING 1082244`, `VIOLATIONS 0`, `MAX_RT 100`, and k=3 `TESTED 12085920`, `SYNCHRONIZING 1066676`, `MAX_RT 82`.
   - **VERIFIED**.

5. `hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T16-08-55Z__extremal_spotcheck.py`
   - creation commit `bc6736b46e35274d8402f5a59df315d687a2b313`
   - readback blob `8c14828740dd0efad72f5fe7fc11331dfd7e6576`
   - **VERIFIED**.

6. `hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T16-08-55Z__extremal_spotcheck_output.txt`
   - creation commit `284aea032e42cf3c742da1b6e97084f2a8fd8113`
   - readback blob `069dfd7cf8b5ddfe7471c57bccc6aa9d62b29e06`
   - readback records exact reset thresholds 65 and 90 for the two representative k=2 extremals and ends `ALL_EXTREMAL_SPOTCHECKS_PASSED`.
   - **VERIFIED SELF-CHECK**, not independent peer review.

7. `hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T16-08-55Z__literature_status.md`
   - creation commit `01715d17cfc316516d5b9bc7d1bf143ec452923b`
   - readback blob `391ea3868a54c0222508976756996988f8d31029`
   - **VERIFIED**.

8. `hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T16-08-55Z__ledger_delta.md`
   - creation commit `fec9b69b151699a983167db40ca81c535b386470`
   - readback blob `0aac5fabdabec811bb6532248a6e99f838d351db`
   - **VERIFIED**.

## Execution/checking statement

The finite certificates use exact integer/bitmask subset-BFS. The two C++ implementations were regression-checked against prior archived n=8/9 or n=10 totals before their new n=10/11 outputs were accepted. A separate pure-Python subset-BFS replay checked representative new extremals and reconstructed explicit shortest reset words. No timeout, sample, floating-point test, or heuristic miss is classified as exhaustive evidence.

No source-level closure is claimed and no peer audit result is invented. Because this is the third consecutive own revised-contract run with metric 7 -> 7, the next HARD8-01 run is subject to STUCK RECOVERY 1 unless another qualified track moves the fixed metric first.
