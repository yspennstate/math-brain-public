# ProofNet24 P26 immutable health fragment — 2026-09-16 07:00:26 Asia/Jerusalem

Canonical run report:

- track: `P26-proof-audit-recovery`
- path: `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_07-00-26__run-report.md`
- creation commit: `b8180ad8fe016468b3a172529498f41a4cb64033`
- Git blob: `a0a4303434e7ca0d9458607499063f4b22a9f942`
- readback status: `COMPLETE_READ_AT_CREATION_COMMIT`
- dedup key used: track + immutable run timestamp + Git blob
- email/Gmail: not used
- scheduler-only complete peer output: `INTERNAL_OUTPUT_UNAVAILABLE`

Mathematical claims preserved in the canonical report:

- `P26-T4-CUBIC-STRUCTURE-TENSOR-20 = PROVED`
- `P26-T4-LEAKAGE-CUBIC-REFINEMENT-20 = PROVED`
- `P26-T4-SIGNED-TAIL-CUBIC-ENERGY-20 = PROVED`
- `P26-AUDIT-P23-SIGNED-OD-WINDOW-20 = PASS`
- `P26-T4-INVERSE-RATIO-ENDPOINT-19 = OPEN`
- P04 Target 4 angular endpoint `e_2=O(1/d) = OPEN`
- full P04 Target 4 = `OPEN`
- full P04 program = `OPEN`

Archive-health check:

- scheduler metadata genuinely exposed: all 20 current registry workers observed enabled; this is recorded separately from execution evidence.
- GitHub recent-history scan crossed the preceding-three-hour boundary and found durable recent evidence for all 20 selected tracks.
- strongest direct verification this run: P04, P20, P23, and preceding P26 complete reports were read and blob-verified; current P26 report was read back completely at its creation commit.
- P15 and P19 report paths plus Git blobs were exposed by their commit objects, but their full bodies were not consumed; they are not mislabeled as complete-read.
- remaining peer rows are conservatively `COMMIT_OBSERVED` unless stronger evidence is stated in the canonical report.
- no complete unarchived peer body was exposed, so no peer report was reconstructed or duplicated.
- no historical report or peer ledger was overwritten.

Relevant directly used sources:

- P04 latest: `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_06-43-52__run-report.md`, creation commit `85ee6d25427d4b54c5e276e32c64b7fe25f967b6`, blob `f63db6fcc9f22eb07a1bc59ed19081d20bb82a07`.
- P20 latest: `proofnet24/P20-kernel-hard-edge/runs/2026-09-16/2026-09-16_06-10-53__run-report.md`, creation commit `485794dbf788ac536e3eded3bda7464657ff666e`, blob `e0de574b41c4c1ccc87c9f38ec92a20fab9ad031`.
- P23 latest: `proofnet24/P23-kernel-obstruction/runs/2026-09-16/2026-09-16_06-29-36__run-report.md`, creation commit `a2db9ccf3761cb8922e317a442f41a45db9264d4`, blob `91875c3aa4ed975385600fc44871ec2f5f527137`.
- preceding P26: `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_05-56-27__run-report.md`, creation commit `64727d21d6ae282ccf2b848c752d36f0b80aaa8b`, blob `ccb31f2f8a81bf88994629a86faf146f3ab58629`.

Runtime metadata honesty:

- exposed model: GPT-5.6 Sol
- requested GPT-6 / maximum reasoning: no exposed setter
- separate effort metadata: unverified
