---
name: recall_overlay_fell_to_payload_on_server_threads_sqlite_2026_11_13
description: "Recall slow on a third of server calls (lex 'overlay-fallback', p50 2.1 s)? The memoised overlay's sqlite con was thread-bound; fixed check_same_thread=False 13 Nov; plus exact numpy BM25 3.6x"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T05:50:01+02:00
  status: verified
  evidence: "brain commits 1958c1ac (fix) and 30a4b801 (numpy); repro scratch area why_fallback4.py; recall_log.jsonl 231/800 overlay-fallback"
---

A third of served recalls (231 of the last 800 in brain_graph/live/recall_log.jsonl on 13 Nov) took the lexical path logged as `overlay-fallback`, with lex_s p50 2.08 s and p90 6.83 s. The overlay path had p50 0.57 s and the sidecar path 0.26 s. The log showed the signature: an `overlay` recall followed by an `overlay-fallback` one, again and again.

Cause: a threading bug, not load. `_fc_overlay` in brain.py opened its read-only sqlite connection with the default check_same_thread=True. The recall server memoises the overlay (MEMO_NAMES has `_fc_overlay`) and answers each request on a new socketserver.ThreadingTCPServer thread. The second recall on the same overlay therefore raised `ProgrammingError: SQLite objects created in a thread can only be used in that same thread` inside `_FcOverlay._score`. `score()` caught the error and called `_full()`, which builds the 45 MB payload merge and scores every memory in pure Python. Because `_fallback` is then set, every later recall on that overlay took the slow path until a folder change dropped the memo.

Repro: scratch area why_fallback4.py builds the overlay in one thread and scores it in another (before the fix: ProgrammingError and fallback set; after: ok, no fallback). A CLI recall never shows it because it runs in a single thread. Replaying logged questions in-process found nothing, and that was the clue that the cause lived in the server.

Fix (13 Nov 2026, an agent, brain commit 1958c1ac): `check_same_thread=False` on that connection. It is read-only, and the server runs one call at a time under its lock.

The same tick landed an exact numpy BM25 scorer in bm25.py (`_score_numpy`, commit 30a4b801). It uses the same per-posting expression in the same operand order, sums in sorted-term order and breaks ties by position. On 127 queries at topk 20/60/400 it returned 0 mismatches of 381 lists and was 3.6x faster; prompts of 600+ characters went from 2.14 s to 0.34 s a call. A short query in a fresh hook process keeps the old loop and never imports numpy. BRAIN_BM25_NUMPY=0 turns it off.

Lesson: any object the recall server memoises must not hold a thread-bound resource (sqlite connections, some file handles). When a server-only slowdown alternates fast/slow on the same cached object, look at the threads first.

What would change this: a server that moves to one worker thread, or the overlay no longer being memoised. Still open: `_FcOverlay._score` is itself a pure-Python per-posting loop, the next candidate for the numpy scorer.


Related: [[recall_after_gap_faults_spread_no_step_over_23pct_overlay_none_memo_2026_11_06]] (the overlay memo itself), [[recall_speed_exact_fold_tail_collapse_2026_11_12]] (the fold scorer), [[recall_server_spell_correct_df_memo_empties_every_sidecar_rebuild_2026_11_05]] (another memo-shaped server bug).

Update 13 Nov 06:0x: the overlay loop is numpy too now (_FcOverlay._score_np, brain commit acd9abf9): 0 mismatches of 360 lists, 0.37 -> 0.011 s a call warm (x35).
