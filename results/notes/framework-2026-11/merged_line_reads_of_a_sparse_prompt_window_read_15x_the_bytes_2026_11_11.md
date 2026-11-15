---
name: merged_line_reads_of_a_sparse_prompt_window_read_15x_the_bytes_2026_11_11
description: "[VERIFIED] Merging nearby line reads in project-memory hydrate (gap 128 KB) a good idea? No: prompt lines sit between big tool outputs; a 1,000-line window of 1.8 MB read 27 MB in 110 reads; slower on a busy disk (old 54 s, new 75 s); dropped"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T09:25:21+02:00
  status: provisional
  evidence: ""
---

Tried 11 Nov 2026 (an agent) on _hydrate_by_offsets in runtime/project_memory/sources.py: read each window's lines as merged stretches (gap 128 KB, span 16 MB) instead of one seek per line. Output was identical on the first 4 of 12 real sources, but it was slower: source agent old 53.7 s vs new 75.2 s, agent 1.5 s vs 29.3 s. Measured from line_index without I/O: the window's 1000 owner lines need 1.79 MB; gap 128K = 110 reads / 27.0 MB, 32K = 340 / 11.3 MB, 8K = 824 / 2.3 MB, 0 = 1000 / 1.8 MB. Prompt lines are small and spread among large tool-result lines, so merging buys few seeks for many bytes, and on this saturated disk bytes cost more than seeks. Not applied; live sources.py unchanged. Lesson: before coalescing reads, count bytes read against bytes needed from the index (a 10-line script, no I/O). What would change it: an idle disk or a dense window (lines adjacent), where gap 8K might still pay a little (18 pct fewer reads). Related: [[review_shard_relink_two_calls_and_claude_walk_prune_2026_11_11]]. The win that did land the same hour was group commit in the ingest loop (commit was 41 pct of ingest samples).
