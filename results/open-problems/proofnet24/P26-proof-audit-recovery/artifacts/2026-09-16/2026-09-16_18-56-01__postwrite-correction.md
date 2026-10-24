Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED (scheduler exposes no model selector or reasoning-effort selector); this was not verified GPT-6/maximum.

# P26 immutable post-write correction — 2026-09-16 18:56 run

This file corrects one repository-state sentence in the already-immutable run report

`proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_18-56-01__run-report.md`

creation commit `30112f348c4a7cdcb0701b43d5ea70027fe7e2ce`, blob `80cd23e622f8bca980413d455da756259aa71a1b`.

The report's Section 10 says that the queue contains **60 unassigned PENDING candidates**. That count became stale during the run after concurrent ownership/repair reconciliation. The authoritative current queue, read from a fresh blob before P26's conflict-safe update and then read back after P26's write, contains **55 unassigned candidate-backlog entries**, none automatically READY. The fleet requirement of at least 60 genuinely unassigned READY problems therefore remains unsatisfied.

Authoritative current queue receipt:

- `QUEUE.md`
- commit `cd3d3875cb4ffe68e8d4f34f4c38583bdb2c933e`
- blob `e9bbaed1a56e44791d78e0d75439e2ac96baec9f`
- state: 55 unassigned candidate-backlog entries; no claim that these are READY.

The same reconciliation records I0099 as **ASSIGNED**, not reserve, under claim `f930bceea271e653d156f45c4b5e701e801b6942`. That separate assignment does not release, retire, or reassign the current C31 package/track.

The final corrected root `RESULTS.md` was also read back after two conflict-safe corrections. It now contains the full P20 report commit SHA, the current I0099 assignment state, the 55-entry queue count, and P26 metric `0 -> 1`:

- `RESULTS.md`
- commit `68f74c4ad76d1eef0ec62dfe67c04401ba130103`
- blob `4420bc949ba90d447c699ac5295563c71fce967a`.

The final root `POSTED.md` keeps C31 explicitly **NOT POSTED / NOT RETIRED** while recording that its source-level assertion is mathematically REFUTED and that both outside audits are complete:

- `POSTED.md`
- commit `bdd6cb8f4e8c508633e48bfda97605ec3cc5ffc0`
- blob `cbb790d3f1e8fbe848055b829399393397954a52`.

No historical report was overwritten. This addendum is the immutable correction for the stale queue-count sentence in the canonical 18:56 run report.
