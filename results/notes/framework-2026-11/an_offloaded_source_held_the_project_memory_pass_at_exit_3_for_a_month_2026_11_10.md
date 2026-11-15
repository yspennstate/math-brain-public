---
name: an_offloaded_source_held_the_project_memory_pass_at_exit_3_for_a_month_2026_11_10
description: "Project-memory hourly pass exits 3 (reclassification_required) every hour? A held source offloaded to GitHub can never be re-read; since 10 Nov the runner drops holds whose file left every root (stub rule), records reclassification_dropped_gone"
metadata:
  node_type: memory
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T20:41:05+02:00
  status: verified
  evidence: "21:00 pass of 10 Nov (hourly_bounded.log.child): 'dropped 6 row(s) of 1 source(s)'; schema_meta held_rows 0, reclassification_dropped_gone names the 7 Sep rollout with 6; summary line held=0 held_sources=0 carried=0"
  originSessionId: agent-97a2-43df-9434-ab94e00262fe
  modified: 2026-11-10T20:21:08.865Z
---

The hourly project-memory pass (BrainFrameworkProjectMemory, hourly_runner.py under ~/.brain-framework/runtime/project_memory) exited 3 (reclassification_required) on every pass from 12 Oct to 10 Nov. The cause was six owner rows of one Codex rollout, codex-rollout-v2:rollout-2026-09-07T12-50-42-01a07b46..., that a pass refused to reclassify on 12 Oct. A hold clears only when a later pass reads its source and holds nothing in it. The 9 Nov GitHub offload replaced ~/.codex/sessions/2026/09/07 with 07.GITHUB_STUB.json, so no pass could read that file again and the hold was carried forever.

Fix (10 Nov 20:3x, live runner patched, original backed up as hourly_runner.py.bak_heldgone_20261110, sha256 prefix 01eaed1ebf12bf2e): new `_held_sources_gone(store, config)`. It drops a held source when either (a) the configured listing has files of that source's kind and none is this source, or (b) it is a Codex rollout whose day folder (or month folder) under a configured codex root is missing and a `DD.GITHUB_STUB.json` (or `MM.GITHUB_STUB.json`) stands in its place. The offload writes a stub only after checking every part against GitHub's digest. An empty listing with no stub drops nothing. A source held again in the same pass is never dropped. Dropped rows are recorded in schema_meta key `reclassification_dropped_gone` ({"at", "by_source"}), and the pass prints "project-memory holds: dropped N row(s) of M source(s) whose file left every configured root". Controls passed 8/8 on a copy of the package, including the live store read-only (it gives exactly the 7 Sep source) and a synthetic root covering stub+missing, stub+present and missing-with-no-stub.

Second finding, the same hour: the Codex lane of project memory lists zero files. ~/.codex/sessions/2026 holds only stubs (04-08, 10) and a partial 09 folder, and has no November folder. The live Codex sessions on this laptop write under per-account CODEX_HOMEs (~/.codex-img-acc3, -acc4 and -acc5 /sessions/2026/11/10, 379 rollouts on 10 Nov). Those are picture and brain workers launched by agents, not the author's own Codex prompts, so leaving them out of an owner-prompt ingest is probably right. I did not change projects.json. If the author starts typing into Codex here again, check which CODEX_HOME that session uses.

Seen live, 21:00 pass of 10 Nov: it printed the dropped line (6 rows, 1 source), schema_meta now holds 0 rows and `reclassification_dropped_gone` names the 7 Sep rollout. That pass still exited 3, for a different and ordinary reason: health `source_backfill_pending`, 506 rows of 71 sources past the ingest deadline (deadline_rows=506), which roll to the next hour. So exit 3 alone no longer means a stuck hold: read the summary line. held=N means a hold; deadline_rows / changed files left mean backlog, which drains.

Closed, 22:00 pass of 10 Nov: exited 0 (run_bounded 22:17:12, pid 43480), summary held=0 deadline_rows=0 deadline_sources=0 - the first clean exit since 12 Oct. The 21:00 backlog drained in one hour.

What would change this: a later pass printing held>0 again on a source that is gone, or the backlog never draining (exit 3 with deadline_rows>0 for many hours in a row). Read schema_meta `reclassification_held_by_source` first, then the summary line.

Related: [[the_hourly_ingest_was_cpu_starved_lock_holder_now_raised_2026_11_10]], [[the_reconciliation_died_on_six_rows_of_one_codex_rollout_2026_10_12]].

