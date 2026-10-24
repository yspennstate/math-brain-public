# ProofNet24 P26 — immutable archive/health fragment

**Run:** `2026-09-16_14-00-49`  
**Repository / branch:** `yspennstate/math-open-problems` / `master`  
**Track:** `proofnet24/P26-proof-audit-recovery`  
**Purpose:** bounded GitHub preservation/health evidence for the selected 20-track registry plus exact delivery receipt for this P26 run.

No email/Gmail source or action was used. No peer report was reconstructed from scheduler metadata, commit titles, or summaries. Existing historical reports/manifests were not overwritten.

---

## 1. Canonical P26 report delivered and verified

Path:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_14-00-49__run-report.md`

Creation commit:

`2ee64b010ef5fbeb47a834f5d9b90cbda400bdc9`

Exact-commit readback blob SHA:

`250fc8da3c7f58b8f0853a96368a4abb3379756c`

Verification status:

`COMPLETE_REPORT_CREATED_AND_READ_BACK_AT_CREATION_COMMIT`

The readback returned the report from the exact creation commit, not moving `master`.

---

## 2. Bounded GitHub scan

Commit API window:

`2026-09-16T08:00:00Z` through `2026-09-16T11:01:30Z`.

This exceeds the required preceding three-hour window.

Pagination used `per_page=100`:

- page 1: nonempty;
- page 2: nonempty;
- page 3: nonempty;
- page 4: exactly `[]`.

Therefore the bounded window was exhaustively paginated through an empty terminal page.

The statuses below are intentionally evidence-tiered:

- `COMMIT_OBSERVED` means a real repository commit SHA was found in the bounded scan. It is **not** promoted to complete-report verification unless the report body was opened.
- `COMPLETE_REPORT_READ_AT_CREATION_COMMIT` means the exact immutable report body was fetched at its creation SHA.
- `P26_COMPLETE_REPORT_VERIFIED` means this run's own report was created and read back at the returned SHA.
- A commit observation is not treated as proof of scheduler execution continuity, and a schedule state is not treated as GitHub delivery.

| Track | Representative actual commit SHA | GitHub verification status | Path evidence |
|---|---|---|---|
| P01 | `380aa6125bb68ca640757b1858cdfae0789d3cd2` | `COMMIT_OBSERVED` | report path not opened in this health pass |
| P02 | `a3fb44c7d69b76059e65ca5d27f2d2702f67f2b8` | `COMMIT_OBSERVED` | path not opened |
| P03 | `a787e3dd452b71e4af12241b863ed524352c0ac9` | `COMMIT_OBSERVED` | path not opened |
| P04 | `c3e1a07f60ec5fcf4e2a9cd11f6d0926ce192980` | `COMPLETE_REPORT_READ_AT_CREATION_COMMIT` | `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_13-46-59__run-report.md`; blob `6ae13780900ecc81af61d744a910227c17f06aba` |
| P11 | `286ca841a74705445c2602b35cbec6a35113e60c` | `COMMIT_OBSERVED` | path not opened |
| P12 | `6f91c31d1cca7465da3e3d296ed4fe86e9b596ef` | `COMMIT_OBSERVED` | path not opened |
| P13 | `63daf2b3b9209a59640b206122987be503fbede8` | `COMMIT_OBSERVED` | path not opened |
| P14 | `ddfbf7f1de3412397899cee869f1b9051da52592` | `COMMIT_OBSERVED` | path not opened |
| P15 | `a7905e2b0d03ed1f870f46fa9b0d94e7c7fc1564` | `COMMIT_OBSERVED` | path not opened |
| P16 | `422c9beba3c4e4612de375fd1f38aa7539a9ba4d` | `COMMIT_OBSERVED` | path not opened |
| P17 | `fbb9d13a86617297dde5111025187c4c93aafff8` | `COMMIT_OBSERVED` | path not opened |
| P18 | `fa5646b93de6ef9de9132bf651176e8222e791db` | `COMMIT_OBSERVED` | path not opened |
| P19 | `9ae438c1f73a3fa44096ead20e36a01f880dd7a4` | `COMMIT_OBSERVED` | path not opened |
| P20 | `9c87b7a5ef188a4c557190ae666c1bd8a7e75e1f` | `COMPLETE_REPORT_READ_AT_CREATION_COMMIT` | `proofnet24/P20-kernel-hard-edge/runs/2026-09-16/2026-09-16_13-11-44__run-report.md`; verified blob recorded by source `3200102f23d979d8d1feca9797abf2d08f469ecf` |
| P21 | `321d2911a8102521fec3b3a45747e72531bd6aa9` | `COMMIT_OBSERVED` | path not opened |
| P22 | `64c2aeadeb970c0c3a1680b114fc9c3c8d21005a` | `COMMIT_OBSERVED` | path not opened |
| P23 | `03e7d7c68012fa6b57b941b19f79af87417d4285` | `COMMIT_OBSERVED` | path not opened |
| P24 | `94444f9500b4c0d845d51a5b7d8b103a6af79b4b` | `COMMIT_OBSERVED` | path not opened |
| P25 | `fa3a8287080a3bedab0774293cb3ce086280054e` | `COMMIT_OBSERVED` | path not opened |
| P26 previous | `4520a093a26a972e7b9850a95a4ea1ae8beaeaf7` | `COMPLETE_PREVIOUS_REPORT_READ_AT_CREATION_COMMIT` | `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_13-00-14__run-report.md` |
| P26 current | `2ee64b010ef5fbeb47a834f5d9b90cbda400bdc9` | `P26_COMPLETE_REPORT_VERIFIED` | `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_14-00-49__run-report.md`; blob `250fc8da3c7f58b8f0853a96368a4abb3379756c` |

All 20 registry tracks therefore have recent durable GitHub commit evidence in the bounded window. Only the stronger verification levels actually performed are claimed.

---

## 3. Scheduler/internal-output distinction

A scheduler metadata surface was genuinely exposed during the run. It was not used as a substitute for GitHub delivery evidence. This P26 schedule was observed enabled; no peer schedule was re-enabled, created, or modified.

No complete scheduler-only peer report body was exposed through that surface. Consequently:

`INTERNAL_OUTPUT_UNAVAILABLE`

for any hypothetical unarchived full peer output not already represented by an actual GitHub report.

No summary, last-run timestamp, task title, or email was used to reconstruct a missing complete report.

---

## 4. Deduplication / preservation actions

- Existing peer reports were not copied when a durable GitHub commit already existed.
- No unarchived complete scheduler output body was available to preserve.
- No historical report or peer ledger was overwritten.
- No content hash beyond Git's actual blob SHA is claimed.
- No fabricated delivery receipt, checksum, or path is recorded.
- The P26 report and this manifest fragment are new immutable UTF-8 files.

---

## 5. Mathematical checkpoint indexed by this fragment

Current run claims:

- `P26-T4-STAR-TRANSVERSE-EXACT-PLANE-27 = PROVED`.
- `P26-T4-STAR-PATH-FIRSTORDER-TRANSVERSE-27 = PROVED`.
- `P26-T4-STAR-TRANSVERSE-SHARP-BLOWUP-27 = PROVED` for fixed `d>=5`, `3/2<alpha<2`.
- `P26-AUDIT-P04-STAR-ONEPARAM-BREAK-59-27 = PASS / STRENGTHENED`.
- `P26-T4-UNIFORM-STAR-NEIGHBORHOOD-BLOWUP-28 = OPEN`.
- P04 Target 4 and full P04 program remain `OPEN`.

End of immutable P26 archive/health fragment.
