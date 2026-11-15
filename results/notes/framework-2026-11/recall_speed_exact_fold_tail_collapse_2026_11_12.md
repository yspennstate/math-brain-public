---
name: recall_speed_exact_fold_tail_collapse_2026_11_12
description: "[PROVISIONAL] Recall slow in lex/bm25/collapse/listing? Fold scorer 4-5x, tail one-pass, collapse fast path, lazy entry path, resident folder listing in the server on its own watch thread (12b04659) - all hash-exact; served lex.score ~3x in-process"
metadata:
  node_type: memory
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T22:01:13+02:00
  status: provisional
  evidence: ""
  originSessionId: agent-4b92-4833-bcc3-a3ab8aa26344
  modified: 2026-11-12T22:48:59.127Z
---

status: provisional

12 Nov 2026, an agent (loop T-20261112-103). Three exact speedups to brain recall, each checked by hashing the WHOLE ranked list (30-44k rows) with old and new copies alternating in one process (scratch eq_tail.py), not by the printed top rows:
- bm25_fold.score (plural fold): one IN query for every result slug and a key-free heap on (-score, slug) tuples. 75 query x topk cases identical; 24.3 s -> 5.0 s over the set. Brain ae9b0467.
- bm25 tail: one pass splits ltail/gtail/stail; leaner row loop (bound lookups, inline status memo). tails -25 pct, rows -11 pct (~20 ms). Brain 52237d64.
- collapse: a slug with no supersession route skips _current_slug and the repeated SKIP/parent_only gates. Loop -24 pct (~20 ms). Brain 1e98b499.
Measurement lessons: (1) served sub:lex.score (312-1172 ms) is ~3x the in-process figure (59-165 ms) because the query-embed thread and graph prefetch run during it (cpu_ms > ms); a served stage time is not the stage's own cost. (2) cProfile swells per-candidate loops (one call per row) several-fold - time those with perf_counter marks, unprofiled. (3) tail and row costs scale with the candidate count: ~250-350 ms in-process at 30-44k candidates, ~5 ms under 2k. (4) In-process co.superseded_known costs 190-820 ms a call (_load_superseded + set(_corpus_slugs()) rebuilt while peers write); whether the served path pays it was unmeasured at 22:00.
New timers: sub:lex.*, sub:bm.*, sub:co.* in calls.jsonl arms. What would change this: served rows showing co.superseded_known small (then the next target is bm.graph, ~150-230 ms served).
Later the same night (22:3x): co.superseded_known (served med 172, p90 806) is almost all _load_superseded, whose cost is the call's one listing of the 64.8k-entry memory folder (set(_corpus_slugs()) is ~45 ms). Fourth speedup: _FastEntry.path is a property (same os.path.join, made when read); the join on every entry was a third of the listing's Python time. Listing CPU median 859 -> 656 ms over 12 paired runs; full scored hash 4/4 equal. Live 22:37, brain 2d5b93db.
Tried and not shipped: taking the listing on a background thread at _memlist_open. Output equal, but on the loaded laptop the seed stage gained ~400 ms and the other stages gave it back under the GIL.
Equality-test lesson: unfrozen old-vs-new runs on the live folder disagree on the full scored hash 1-3 times in 5 (index refreshes; an old-vs-old control drifts too). Hold one index generation with `python bm25.py freeze 10 "<why>"` for the test, then unfreeze.
bm.graph split (in-process, non-resident): graph_lane.ranked 107-142 ms, link_ranked 297-421 ms; the link walk already has mmap, prefetch and a resident cache.

Fifth speedup (23:0x-00:1x 12-13 Nov): the recall server keeps the memory folder listing between calls (RESIDENT LISTING block in brain.py, only in the server module; BRAIN_RESIDENT_LIST=0 off, =force on anywhere on Windows). A ReadDirectoryChangesW watch on the folder is drained at the start of each call; every name it reports is re-read on its own (FindFirstFileExW, same fields as the listing) for 120 s, new ASCII names go in at their str.upper() place, gone names come out; overflow, a non-ASCII or case-twin name, more than 2000 hot names, or a listing older than 600 s takes a full listing. Served before: seeds med 599 ms, superseded_known med 312 / p90 1478 (both paying the 0.8-2.8 s listing). In-process with bm25 frozen: full scored list hash-equal 4/4; seeds 833-1047 -> 61-102 ms. Against the live folder, resident vs fresh every 5 s, 180 checks: 0 mismatches; resident 0.5-68 ms, fresh 0.3-6.5 s.
Two lessons from building it: (1) Windows sends the MOD notice for an in-place rewrite (CONSCIENCE.md, every few seconds) BEFORE the directory entry moves; the entry updates about a second later with no second notice, so a name must be re-read for a while after its notice, not once (a 30 s window left one 13 s stale size). (2) st_atime differs between a kept and a fresh listing (the watch does not ask for last-access changes; a bulk read moved 538 in a minute); nothing reads it (_stat_key is size, mtime, ctime, birthtime), so the equality key leaves it out. An equality harness on a live folder must re-read on a difference before calling it a mismatch: a change between the two reads is a race, not an error.
(3) Served, the watch died on every call ("watch dropped: drain error" in brain_recall_server/resident_listing.log): Windows cancels overlapped I/O when the thread that issued it exits, and the recall server answers each call on a fresh thread (socketserver.ThreadingTCPServer), so the read armed in one call was cancelled when that call's thread ended. A single-threaded equality test cannot see this; test a server path with each call on its own thread. Fixed by one daemon thread per watch that arms, waits, parses and re-arms; a call only takes the names it gathered. Each call on a fresh thread, 60 checks: 0 mismatches, median 4.95 ms against 403 ms fresh, one full listing.
Stage timers (same ship): stage:pre, stage:tail and stage:qemb_join now name the time that fell in no stage, so the stages sum to stage:total. In-process: tail (display and print) 110-235 ms, pre 24-143 ms, qemb_join 0.
Live 13 Nov 00:5x, brain 12b04659 (sha256 a5ebc8c4).
Related: [[brain_recall_walk_eight_steps_same_answers_2026_11_10]]
