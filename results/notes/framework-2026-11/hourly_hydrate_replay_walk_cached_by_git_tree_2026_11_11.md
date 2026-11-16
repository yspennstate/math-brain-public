---
name: hourly_hydrate_replay_walk_cached_by_git_tree_2026_11_11
description: "[VERIFIED] Hourly project-memory pass stuck 10-30 min in hydrate_review_rows? It was _configured_replay_files walking the frozen replay archive (11_raw_session_transcripts, ~360 folders) at I/O priority 1; since 11 Nov the walk's listing is cached per git tree id (replay-listing-cache.json)"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T02:51:38+02:00
  status: verified
  evidence: ""
---

Hourly project-memory pass stuck in hydrate_review_rows (11 Nov 02:3x, owner present): py-spy showed the main thread in scandir under _configured_replay_files (sources.py), walking the replay roots 11_raw_session_transcripts/claude_projects and codex_sessions with pathlib glob '**/*.jsonl' (two scandirs per folder, ~360 folders). The pass's thread sat in Wait/Executive at about 1 pct CPU with 0 bytes read: the scheduled task's children run at I/O priority 1 and memory priority 2 (memory priority7_task_children_inherit_memory_priority_2_and_io_1_2026_11_09) and run_bounded raises neither while he is present, so every directory enumeration queued behind the renders. The same walk takes 0.1 s warm and 1.4 s from a Normal shell. The archive has not changed since 7 Jul and all 20,077 files in it are tracked.

Fix (runtime/project_memory/sources.py, backup sources.py.bak_20261111_0245 in session agent's scratch area): _replay_listing(root, pattern) returns the walk's own output, cached in state/project_memory/replay-listing-cache.json per (root, pattern) and keyed on git rev-parse HEAD:<root> (about 0.7 s); on a new tree id, or without git, it walks as before. A file added under the archive without a commit is not seen until the next commit there. _configured_replay_files also skips a root whose kind no needed id has. Tested: identical results to the walk on 302 needed ids (104 found) and on all 14,352 archive ids (4,235 found); cache hit about 3 s at Normal priority warm (where the walk is 1 s), so the gain is only under low I/O priority, where the walk measured 10-30 min.

Not yet seen on a live pass: the 02:06 pass ran the old code (in the walk from about 1,302 s to about 2,200 s). To check: the next owner-present pass's hydrate time ('phase: hydrate_review_rows at' minus 'phase: contract_cache at' in hourly_bounded.log.child). Next bottleneck behind it: the line-index reads, 53 sources in 393 s at I/O priority 1 against 472 to read. That makes the case for giving the hourly child Normal I/O priority while keeping BelowNormal CPU when he is present; run_bounded's owner-present gate currently raises neither. What would change this: a pass where hydrate is still slow with the cache hit, meaning the time is in the reads, not the walk. Related: [[the_hourly_ingest_was_cpu_starved_lock_holder_now_raised_2026_11_10]].

Addendum 11 Nov 05:4x (an agent): the git call that gives the tree id was itself the wait. On the 05:00 pass (owner present, BelowNormal, box saturated) py-spy found 21 of 25 samples in hydrate_review_rows waiting on that `git rev-parse` subprocess; the same call takes 0.4-1.8 s from a Normal shell. `_replay_tree_key` now remembers the tree id against HEAD's commit id, read straight from .git/HEAD and the ref file (or packed-refs), in state/project_memory/replay-tree-key-cache.json, so git runs only when HEAD has moved (4 commits in 3 hours on the brain repo). Checked: same id as git for both roots, second call 2 ms, at most one git call per root, a non-repository root still returns None; runtime/test_project_memory_hot_hook.py 50 passed. Backup sources.py.bak_20261111_0535. Not yet seen on a production pass.

Verified 11 Nov 06:00 pass: hydrate 474 sources (line index 470, tail 4, no full reads) in 68 s, against the 05:00 pass at 296 sources in 1,778 s before its cap kill.
