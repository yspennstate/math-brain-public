# ProofNet24 P26 immutable archive / health fragment — 2026-09-16 05:56:27

Repository / branch: `yspennstate/math-open-problems` / `master`  
Protocol: `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`  
Email/Gmail: not used.  
Number theory: none.

## Canonical P26 report

- Track: `P26-proof-audit-recovery`
- Path: `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_05-56-27__run-report.md`
- Creation commit: `64727d21d6ae282ccf2b848c752d36f0b80aaa8b`
- Git blob at that creation commit: `ccb31f2f8a81bf88994629a86faf146f3ab58629`
- GitHub commit stats: 731 additions, 0 deletions.
- Verification: `COMPLETE_REPORT_READBACK_VERIFIED` at the exact creation commit. The exact creation-commit fetch returned the report beginning and body; the creation-commit metadata independently identifies the added path and blob. The newly authored immutable file was not overwritten.

Primary mathematical claims preserved in that report:

- `P26-T4-NEXT-ROW-JORDAN-DRIFT-19 = PROVED`;
- `P26-T4-AFFINE-JORDAN-LOO-BIAS-19 = PROVED`;
- `P26-T4-AFFINE-NORM-BLINDNESS-19 = PROVED` (narrow first-moment statement);
- `P26-T4-LOO-INVERSE-RATIO-19 = PROVED`;
- `P26-AUDIT-P20-PJ-WARD-AFFINE-19 = PASS` (narrow bridge audit);
- `P26-T4-INVERSE-RATIO-ENDPOINT-19 = OPEN`;
- P04 Target 4 and full P04 remain `OPEN`.

## Bounded GitHub health observation

A paginated GitHub commit scan of `master` covered the interval `2026-09-15T23:20:00Z` through `2026-09-16T03:00:00Z`, more than the required preceding three hours. The query used `per_page=100`; pages 1, 2, and 3 contained commits and page 4 was empty. Pagination for this bounded window was therefore exhausted.

Recent durable GitHub preservation evidence was found for every selected track P01, P02, P03, P04, P11, P12, P13, P14, P15, P16, P17, P18, P19, P20, P21, P22, P23, P24, P25, P26. Stronger complete-report/blob verification was performed for P04, P20, the relevant P23 affine checkpoint / latest P23 state, the preceding P26 checkpoint, and the current P26 report. Rows not fully reread remain conservatively `COMMIT_OBSERVED`; a commit observation is not promoted to a complete report.

The exposed schedule registry was inspected separately. All selected 20 schedules were observed enabled. This is recorded only as `SCHEDULE_ENABLED_OBSERVED`: enabled/scheduled status is not treated as evidence of execution, complete report, or verified commit.

| Track | Durable GitHub evidence retained/observed | Verification level in this run |
|---|---|---|
| P01 | `fe2b8be7171c2df9fc7e764c6ea45d21cbc3728d` | `COMMIT_OBSERVED` |
| P02 | corrected archive `980a991d12131ab5b4879aa32548dfd03b930cf6`; receipt `03b15c97acd3c998c66319c1d5fa0287b28d55aa` | `COMMIT_OBSERVED` |
| P03 | `21f1a34ad3f122e3e8b09047a2b4586e23911fe7` | `COMMIT_OBSERVED` |
| P04 | report `60ee7e1c42af6ded59bad4c1b06fe7b59345f7b9`; verify `8a380611144f533d389d77a12277431b9744eb5b` | `COMPLETE_REPORT_READ + BLOB_VERIFIED`, blob `7218a2cfd4acb866b05d02965dc9df7c9c472d8b` |
| P11 | `97da5e33bb9eedcb8ca11dcd5567cdd3c3cdfa0c` | `COMMIT_OBSERVED` |
| P12 | `e98a2708ebb2e5652e4fd8aee3cc843d174d092c` | `COMMIT_OBSERVED` |
| P13 | `bcedde239e3cda2a1b3d485f10fd817c6a182771` | `COMMIT_OBSERVED` |
| P14 | `9273f349d9e8e907b89be293d78d37b58e30d2dc` | `COMMIT_OBSERVED` |
| P15 | `73a3f2fadd6cc03060cee01671390a3736109e32` | `COMMIT_OBSERVED` |
| P16 | newer archive evidence `5b131ca19993b16c4f60128a57015b07787f819e` | `COMMIT_OBSERVED` |
| P17 | newer certificate `d286eed30c53cf51d3b94f7d21d2d8709aa1d089` | `COMMIT_OBSERVED` |
| P18 | `c45f45b87923fd6feefe6025b71b7eff7eb5cc3c` | `COMMIT_OBSERVED` |
| P19 | corrected archive `86b42fa48aeb4d480b9ab22b861d63c6718a4d2a`; verify `a7d2d8382a9f9e55fbae0a79447b0ee2f43989aa` | `COMMIT_OBSERVED` |
| P20 | report `b186666d4b26efeddbaa7ed14798ec7fa291e4e7`; verify `115a42ee0efaea60b9dba71d5c34cb2d81da166a`; logical readback correction `22540633312c5bee968e6766bf09d8709852008e` | `COMPLETE_REPORT_READ + BLOB_VERIFIED`, blob `17df2aee8c6ef69b61dd27544132eec6ea732a00` |
| P21 | `528964d80d127053de2ea36f00f07924d28cb089` | `COMMIT_OBSERVED` |
| P22 | `669321e73a3088263ed6544f6f9be113ca7665d6` | `COMMIT_OBSERVED` |
| P23 | latest report `fa701077a860bafe416507e36d566153676fac91`, verify `a304620a7d31900a326864cef58d7bed6a1562c0`; affine report `cfdc8f206c50136deae477175db37aa512f5891b`, blob `9528ec050b5358101ee5ea14fbc5525a62cc7f98` | `COMPLETE_REPORT_STATE_READ`; affine source `BLOB_VERIFIED` |
| P24 | `1fbb74ca7f9c22aac14291655ae244009955009b` | `COMMIT_OBSERVED` |
| P25 | `d1f73457d75a6dfb7d156156acef30332bebb9cd` | `COMMIT_OBSERVED` |
| P26 previous | `0bb0f23b523320efd1e98b6be57d19e8a633556c`, blob `14b66c1eab9475b971e08aa3f0061528e47f961a` | `COMPLETE_REPORT_READ + BLOB_VERIFIED` |
| P26 current | `64727d21d6ae282ccf2b848c752d36f0b80aaa8b`, blob `ccb31f2f8a81bf88994629a86faf146f3ab58629` | `COMPLETE_REPORT_READBACK_VERIFIED` |

## Recovery status

Complete scheduler-internal peer output bodies were not exposed to this run. Therefore the scheduler-only recovery status is `INTERNAL_OUTPUT_UNAVAILABLE`.

No complete unarchived peer body surfaced through the exposed durable surfaces. Existing complete GitHub reports were verified/indexed instead of duplicated. No email, Gmail, collaborator contact, or summary reconstruction was used. No peer ledger, report, or historical artifact was overwritten.

## Exact failures / caveats

- Schedule-enabled observations are metadata only; they do not prove an execution completed.
- For rows marked `COMMIT_OBSERVED`, this fragment deliberately does not claim the whole report body was reread.
- No hash or length is stated unless returned by GitHub or already present in the preceding immutable verified fragment.
- GitHub commit signature verification for the current report commit is `unsigned`; this is distinct from content/blob readback verification and is not represented as a delivery failure.
