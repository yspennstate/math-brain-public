# ProofNet24 P26 immutable audit / archive-health fragment

**P26 checkpoint timestamp:** 2026-09-15 15:13:51 Asia/Jerusalem  
**Canonical repository:** `yspennstate/math-open-problems`  
**Branch:** `master`  
**Policy:** GitHub-only. No Gmail/email source used.

## Canonical P26 report

Path: `proofnet24/P26-proof-audit-recovery/runs/2026-09-15/2026-09-15_15-13-51__run-report.md`  
Creation commit: `9ea9b4f87a50993e8ca97936146fb81df0aaf535`  
Readback blob: `e8055aa9de3d515985221f852ce346577d631050`  
Readback: COMPLETE, in two contiguous ranges covering the whole file.  
Status: `COMPLETE_REPORT_READBACK_VERIFIED`.

Main claims:

- `P26-AUDIT-P04-CHRISTOFFEL-JORDAN-04` = PASS.
- `P26-T4-EXACT-024-SECTOR-04` = PROVED.
- `P26-T4-CHI2-FLOOR-EQUIVALENCE-04` = PROVED.
- P04 Target 4 remains OPEN.

## Preserved transport-failure artifact

Earlier same-run path: `proofnet24/P26-proof-audit-recovery/runs/2026-09-15/2026-09-15_15-00-08__run-report.md`  
Creation commit: `6484a9722ed0c6b4f4a0b5435ab07b83d877a199`  
Blob: `d57e1724d1b03f37d9df2364eabaabc653e5f7d8`  
Failure: readback exposed transport corruption of TeX sequences beginning with `frac`; for example one coefficient lost its leading `f`.  
Disposition: historical artifact retained, not overwritten, not treated as the canonical mathematical checkpoint. The transport-safe 15:13:51 report above is canonical for this P26 run.

## Bounded selected-worker health scan

The master commit history was paginated over at least the preceding three hours. Exposed scheduler status showed all 20 selected workers enabled with recent execution metadata. Execution metadata alone is not treated as completion.

| Track | Recent GitHub evidence | Verification |
|---|---|---|
| P01 | `72f1bd315bd992e88ac5afcea3db6ce960ec9dcc`, archive 14:01:40 | COMMIT_OBSERVED |
| P02 | `67ad45705ad69cfb536af65e9564165bbbd56f0c`, archive 14:01:54; clarification `3dd4a7c7eeab71414cadbf5e65baa8995ee78008` | COMMIT_OBSERVED |
| P03 | `ac567d9273b72e183a01fd87ef6154d1302832e6`, archive 14:11:24 | COMMIT_OBSERVED |
| P04 | `a250cb01a6e4a66530c8293724f02526c8f0a663`, archive 14:42:49; blob `8d626b482600d81c38529aa3c080be018f6bc194` | COMPLETE_REPORT_READ; COMMIT/BLOB_VERIFIED |
| P11 | `1ba3e1f0a3e95285dfec29b42a92406a12cc4299`, archive 14:13:33 | COMMIT_OBSERVED |
| P12 | `697c8ef075b618176cd4d8d656d16e4d64eb85ed`, archive 14:21:37; readback note `0bc7a5d1514c5f206401832cccf10df8cfa31b15` | COMMIT_OBSERVED |
| P13 | `a023f9022c11a92e81854e57316d2408b6d900ac`, archive 14:07:03 | COMMIT_OBSERVED |
| P14 | corrected archive `8abe4c1f5df1e732dbd5d89699721d98edd826e2`, 14:20:26 | COMMIT_OBSERVED |
| P15 | `4951e8317af6108cd47fbcffe98e7b1d678fddef`, archive 14:25:42 | COMMIT_OBSERVED |
| P16 | `3acdc204d4b2107404099cfd3aee4f1f24169cc2`, archive 14:37:33 | COMMIT_OBSERVED |
| P17 | `0c0b6bb3152066141b99de8f2f33eb112ef89959`, archive 14:57:55 | COMMIT_OBSERVED |
| P18 | `9f4147842c5bddd32f517c8013c93c920e2cdfc5`, complete P18 report commit; file timestamp 13:56:11 | REPORT_COMMIT_OBSERVED |
| P19 | `6945db08c63122adffdede9ec6920c2dabb7832f`, archive 14:04:34 | COMMIT_OBSERVED |
| P20 | `7fad083f015269e52c7b98f11b481c7cb89ab62a`, archive 14:28:25; blob `7192350700c376e6eb818c576789bd010e872b79` | COMPLETE_REPORT_READ; COMMIT/BLOB_VERIFIED |
| P21 | `1120ffd1ad68e477e0fcb0621a2568225fa9d331`, archive 14:14:06 | COMMIT_OBSERVED |
| P22 | `cecc0a0973ad483d08a9ce6748de251fbd0d94ef`, archive 14:25:08 | COMMIT_OBSERVED |
| P23 | `030608a299a3acd2e591b5e27455ef01078f5cf5`, archive 14:27:25 | COMMIT_OBSERVED |
| P24 | `b8760448f339469791132df904a589bf3f60c681`, archive 14:45:54 | COMMIT_OBSERVED |
| P25 | `d1e63e3166707790f7dc7b8c7728314b17745154`, archive 14:35:38 | COMMIT_OBSERVED |
| P26 | canonical current report `9ea9b4f87a50993e8ca97936146fb81df0aaf535`; blob `e8055aa9de3d515985221f852ce346577d631050` | COMPLETE_REPORT_READBACK_VERIFIED |

No complete scheduler-internal peer output was exposed that was both complete and unarchived. No peer recovery duplicate was created. No peer historical report or ledger was overwritten.

## Exact mathematical checkpoint

For `V = Sym_d^0`, residual density `q_P = ||P h(u)||^2/s`, and actual residual DPP `P_s`, define

`B_{d,s} = alpha_d [ (s+2)/s + 12/d - 2d(s-1)/(s(m-1)) ] - 1`,

where `alpha_d = d(d+2)/((d+4)(d+6))`.

Then

`E||q_{P_s}-1||_2^2 = B_{d,s} + [3(d+4)/(2(d+6))] E||Pi_2(q_{P_s}-1)||_2^2`,

and

`E||Pi_4(q_{P_s}-1)||_2^2 = B_{d,s} + [d/(2(d+6))] E||Pi_2(q_{P_s}-1)||_2^2`.

At s=2,

`B_{d,2} = d(d-2)(d+3)/((d+6)(d^2+d-4))`.

Thus the immediate open angular theorem is exactly equivalent to

`E||q_{P_2}-1||_2^2 = B_{d,2} + O(1/d)`.

The full hard-edge theorem remains OPEN.
