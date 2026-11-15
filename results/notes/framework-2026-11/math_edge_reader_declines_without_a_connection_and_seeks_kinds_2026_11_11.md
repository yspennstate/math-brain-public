---
name: math_edge_reader_declines_without_a_connection_and_seeks_kinds_2026_11_11
description: "math_answer_closure_selftest.py red (FakeStore has no attribute connection)? Fixed 11 Nov 03:20: math_sense edge reader declines without a connection and reads the kinds by index seeks (build 0.026 -> 0.011 s). Selftest has --quick; hook_liveness now runs four selftests (8 s). Whole-edge fallback costs 17.5 s on 167,685 edges"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T03:48:10+02:00
  status: verified
  evidence: "brain_improvement/agent_run/closure_reader/; ledger_rows_20261111_e.jsonl"
---

`math_answer_closure_selftest.py` (27 Sep, the guard against serving an old revision as the current answer) was red
at its first fixture on 11 Nov and nobody knew, because nothing ran it. The cause was in the hook, not the test:
`math_sense._revision_edge_reader` (added 12 Oct to avoid building every edge as an object) read `store.connection`
one line before the check its own docstring describes ("None when the store has no row reader"). A store without
the attribute, which is what the selftest's fixtures use, raised AttributeError instead of taking the whole-edge
read. Same class as [[core_steer_selftest_runs_in_hook_liveness_and_the_second_start_2026_11_11]]: a regression net
that no hook, task or dream step runs goes red silently.

**The change (live 11 Nov 03:20; math_sense.py sha 83f5f443ac167930, was 2726b6e0128f7d96):**
- the reader declines for a store with no connection (`getattr(store, "connection", None)`), so the whole-edge read
  is used, as documented;
- the store's distinct edge kinds are read by one index seek per kind (a recursive `min(kind) ... WHERE kind > ?`
  over idx_edges_kind) instead of `SELECT DISTINCT kind`, which walks every entry of that index on every math
  prompt. Same rows; the reader build went from 0.025-0.027 s to 0.011 s (best of 7, live store, 167,685 edges,
  12 kinds). The saving per prompt is small, about 0.015 s, and it no longer grows with the store.

**The selftest and the schedule.** The full selftest now takes 84 s (a 17 s whole-edge read plus the pools of 208
answer targets), too long for the liveness check, so it has `--quick`: the fixtures, then a dozen live answer
targets, a different dozen each day, on a three-kind edge read; 1 s. hook_liveness.py (sha e614b7146d7d8ef0, was
0d2e4a3513a13cea) lists `slow_sense_selftest.py`, `graph_lane_ties_selftest.py` and
`math_answer_closure_selftest.py --quick` beside `core_steer_selftest.py`; a SELFTESTS entry may carry script
arguments as a third element; a check printed as "FAIL <label>" is named by its label. Five runs take 8 s.

**Controls.** test_closure_reader.py: no-connection store, records in created_at/id order, a retracted edge left
out, an empty table, an unknown kind sorting first, last and in the middle (the reader declines each time, as the
old file does), and on the live store 1,757 records and the pools of 16 answer targets identical to the old file's.
The full selftest passes 7/7 on the new file and fails on the old one. test_selftest_runner.py 23/23 on the live
hook_liveness.py, 5 failing on the old one.

**Not scheduled, and why.** `bm25_lane_selftest.py` writes the live index (needs claim memory:brain/bm25_index).
`graph_fire/owner_convention_selftest.py` replays transcripts and runs past 170 s.

**Not covered.** The whole-edge read is the reader's fallback and costs 17.5 s on today's store (it was 0.43-0.50 s
at 17,500 edges). It is taken when the store holds an edge kind `EdgeKind` does not know, when a query fails, or when
a pool id is not ASCII. Today none applies (12 kinds, all known; 0 of 94,503 ids non-ASCII), but a new kind written
to the store before the code knows it would put 17 s on every math prompt. Rollback: `math_sense.py.bak_reader_20261111`,
`math_answer_closure_selftest.py.bak_quick_20261111`, `hook_liveness.py.bak_selftests2_20261111`.

**How to apply.** When a selftest is red, read the code under test before the test: the docstring said what the
function should do and the function did not do it. And a selftest that reads a whole live store needs a quick mode
before it can sit on a schedule; a net that takes a minute and a half will not be run.

