---
name: math_sense_unknown_edge_kind_refused_through_the_kind_index_2026_11_11
description: "Math hook slow or silent after a new edge kind reached the store? Since 11 Nov 07:0x math_sense refuses an unknown edge kind at once through the kind index (same UnknownEdgeKindError) instead of after a 17.5 s whole-edge read on every math prompt; all-retracted unknown edges are not refused. Upgrade the build to end the silence"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T07:01:25+02:00
  status: verified
  evidence: "brain_improvement/agent_run/closure_reader/patch_unknown_kind_fast.py, test_unknown_kind.py; ledger_rows_20261111_o.jsonl"
---

The math hook reads the store's revision and answer edges through `math_sense._revision_edge_reader`. Until 11 Nov
07:0x that reader declined (returned None) whenever the store held an edge kind the reader's build of `EdgeKind` did
not define, and the caller then read every edge of the store to arrive at `UnknownEdgeKindError`. The refusal itself is
deliberate (an unknown kind could be a new kind of supersession, and serving an old revision as current is the worse
fault), but reaching it cost a whole-edge read: 17.5 s on 167,685 edges, inside a read transaction, on every math
prompt of every session, from the day a new kind is written until the build is upgraded. It has happened before
(task 462, 9 Aug: an older reader met `semantic_association`). See
[[math_edge_reader_declines_without_a_connection_and_seeks_kinds_2026_11_11]] for the reader's other change today.

**The change (math_sense.py).** The reader already lists the store's kinds by index seeks. When one is unknown it now
finds, through the kind index, the first edge of an unknown kind in created_at, id order that is not retracted, and
raises the store's own `UnknownEdgeKindError` with that kind and its row count: the same error, word for word, that the
whole-edge read raised. When every edge of the unknown kinds is retracted nothing is refused and the fast path goes on,
which is also what the whole-edge read did. A store with no `path` attribute still takes the whole-edge read.

**Controls.** `closure_reader/test_unknown_kind.py <old> <new>`: an unknown kind sorting first, last and in the middle;
two unknown kinds (the earliest edge decides); a retracted earliest edge; the count including retracted rows; all
unknown edges retracted (pool and edges equal the old file's); two edges with one created_at (the smaller id decides);
a store with no path; known kinds only; an empty table; then the live store (records and pools equal the old file's).
The refusals equal the old file's word for word and need no whole-edge read, where the old file needed one. Run as
`<old> <old>` the test fails, which is the proof that it tells the two apart. `test_closure_reader.py` and
`math_answer_closure_selftest.py --quick` still pass.

**Not covered.** The 17.5 s was measured on the whole-edge read on 11 Nov 03:20, not on a store with an unknown kind
(the live store has none, and I did not copy it to add one). A pool id outside ASCII and a failed query still take the
whole-edge read (0 of 94,503 ids are outside ASCII today). An edge row whose kind is NULL is not looked for. The
callers still go silent on the refusal: the hook serves no math note until the build knows the kind, now at once
instead of after 17 s. Rollback: `math_sense.py.bak_unknownkind_20261111`.

**How to apply.** When a fast path "falls back to the slow path, which then raises", check what the slow path costs
before it raises; if the fast path can see the same condition, raise there.

