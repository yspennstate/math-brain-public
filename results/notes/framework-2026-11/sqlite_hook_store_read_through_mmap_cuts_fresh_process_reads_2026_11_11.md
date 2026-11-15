---
name: sqlite_hook_store_read_through_mmap_cuts_fresh_process_reads_2026_11_11
description: "[VERIFIED] Prompt hook slow opening a big sqlite store in a fresh process? PRAGMA mmap_size=1GB on the read-only connection: graph membrane 3,500 id lookups 24-31 -> 16 ms, evaluation 107 -> 94 ms, tail gone; file-backed, no commit charge"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T19:20:02+02:00
  status: provisional
  evidence: ""
---

Graph membrane (live_membrane.py) opens the 470 MB sidecar.sqlite read-only in a fresh process on every prompt and tool call. With plain reads SQLite copies each page in by a read call; with PRAGMA mmap_size=1073741824 it reads pages in place. Measured fresh processes, same ids: name lookups (about 3,500 rowids) 24-31 ms with 46/86 ms tails -> 15.6-16.7 ms; edge fetch 12.6-15.2 (tail 65) -> 11.4-11.9. Whole Live()+evaluate 107.4 -> 94.2 ms median, p90 124 -> 99, 24/24 transcripts identical output. Landed 11 Nov 2026 19:2x by an agent, live md5 555457c87d, record 12_cognitive_architecture/brain_improvement/membrane_mmap_2026_11_11 (commit b99dd73c96). Safe because: read-only, file-backed (no commit charge on a box at 86 pct commit), the map lives with the connection so a rebuild's rename waits on readers exactly as before (SQLite on Windows opens without FILE_SHARE_DELETE). Not a win: dropping a text column from the lookup (2 of 25 ms) - the cost is the row lookups. How to apply: any hook that opens a large read-only sqlite store per prompt; measure in FRESH processes (a warm in-process loop hides most of it). Related [[membrane_shadow_orders_search_cost_186_ms_every_prompt_now_reused_2026_11_11]] [[rank_prompt_hooks_by_wait_parallel_children_are_off_the_critical_path_2026_11_11]].
