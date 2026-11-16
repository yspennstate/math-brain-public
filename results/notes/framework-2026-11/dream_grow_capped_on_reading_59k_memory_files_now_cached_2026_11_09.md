---
name: dream_grow_capped_on_reading_59k_memory_files_now_cached_2026_11_09
description: "[PROVISIONAL] Dream network grow step (dream_grow) capped at 45 min / slow: adapt_live re-read all ~59k memory files nightly for the description; now cached by mtime+size (adapt_live 146 s -> 27 s, identical output)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T01:37:15+02:00
  status: provisional
  evidence: ""
---

The dream's network grow step (network/dream_grow.py) hit its 2700 s cap on 31 Oct, 1 Nov, 7 Nov and 8 Nov and took 32-44 min on most other nights. On 8 Nov evening it started 23:52; adapt_live finished writing events_full.jsonl at 00:36, so grow had about one minute before the 00:37 kill. The time was adapt_live, not grow.

adapt_live.from_memory_dir opened and read in full every file in the memory folder (58,920 files on 9 Nov) each night, only to take the description line. With the author present the step runs BelowNormal on a starved disk (cold opens 400 ms to 1.4 s that night), so those reads were most of the 44 min.

Fix, 9 Nov 01:3x (an agent, task rank 3): the description is cached in network/.memdesc_cache.json keyed by (mtime_ns, size). os.scandir supplies both with the listing on Windows, so an unchanged file is never opened. The cache is written whole through a .tmp file and os.replace. A missing or unreadable cache falls back to reading every file. Output format unchanged; the function prints "memory dir: N files, H from the description cache".

Measured on the live folder, normal priority:
- function alone: 125 s cold (no cache), 3.3 s warm; the original code took 39 s right after, on a warm OS cache
- whole adapt_live, live inputs: 146 s on the first run (builds the cache), 27 s on the second (58,890 of 58,927 from the cache; 37 files had changed in between)
- other sources: prompts 17 s (110k prompts), outcomes 1.8 s, retrievals 0 s
- identity: cached output against the original code's output, 58,922 ids: 58,919 byte-identical. The other 3 had been rewritten between the two runs (new mtime and text), and 1 file was deleted. None of the differences came from the cache.

Not yet seen: an in-dream timing. The next dream log should show dream_grow finishing well inside the cap with the cache line in its output. If it still caps, grow.py itself is the next suspect (net.sqlite3 is 3.6 GB). The cache file is about 20 MB (descriptions up to 1500 chars) and can be rebuilt; deleting it costs one slow night.

Files: adapt_live.py sha256 b30ca1d7add7fea7 (was 7edf8291062f4081); bench scripts in the session grow_prof/.


Related: the note on evening dream step caps (the same evening caps, measured from the other side), [[dream_capped_steps_two_persistent_rest_follow_evening_load_2026_11_08]] (dream_grow was one of the two persistent cappers). Mirrored to the private repository: 12_cognitive_architecture/dreaming/network/adapt_live.py at 5372026c9e.
