---
name: fleet_inbox_cache_move_refused_under_a_reader_dropped_the_fetch_2026_11_11
description: "Leftover inbox_cache.json.<pid> files in ~/.claude/fleet_board, or a fleet message shown a prompt late? The cache move was one bare os.replace, refused on Windows while another session read the copy; the fetched inbox was dropped. Since 11 Nov 04:27 fleet_board.py's four cache writers retry 1.5 s and never raise. 13 controls pass"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T04:32:05+02:00
  status: verified
  evidence: "brain_improvement/agent_run/fleet_cache_swap/patch_fleet_board_swap.py, test_fleet_board_swap.py; ledger_rows_20261111_i.jsonl"
---

`fleet_board.py` keeps the fleet inbox in `~/.claude/fleet_board/inbox_cache.json`, which every session on the workstation reads at every prompt. Its refresh wrote `inbox_cache.json.<pid>` and moved it over the copy with one bare `os.replace`. On Windows that move is refused (PermissionError) while another session has the copy open. The error went up out of `_refresh`, so an inbox that had just been fetched was dropped for that prompt, and the temp file stayed: eleven of them between 30 Oct and 8 Nov.

Since 11 Nov 04:27 the four cache writers (inbox copy, page cache, the per-agent seen list, the resurfaced list) use one step, `_swap(tmp, dst, wait_s=1.5)`: the move is tried again while the reader holds the file (1.5 s; 3 s for the per-agent lists), it never raises, and it removes its temp when it gives up. `_refresh` returns the text it fetched whether or not the copy could be written.

Live sha256 3f8a94d5f74c082d (was 759f4c18b805abdc), backup `fleet_board.py.bak_swap_20261111`, repo mirror equal.

Measured (`brain_improvement/agent_run/fleet_cache_swap/test_fleet_board_swap.py <file>`): 13 controls pass on the live file, 8 fail on the old one. A reader holding the copy 0.5 s is waited out. A reader holding it 3.5 s costs the prompt 1.56 s; the fetched inbox is still returned, the old copy is whole, no temp is left.

Not covered: what the hook did with the exception on each of the eleven days was not read from a log. The Macs' copies are unchanged (a move over an open file succeeds there).

Same fault, same day, in the math index build: [[math_prefilter_publish_waits_out_a_reader_2026_11_11]]. The shape to look for anywhere on this workstation: a file many processes read, published by one bare `os.replace`. A leftover `<name>.<pid>` or `<name>.tmp` beside a cache file is the trace it leaves.

