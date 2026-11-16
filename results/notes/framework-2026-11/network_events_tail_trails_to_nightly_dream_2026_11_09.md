---
name: network_events_tail_trails_to_nightly_dream_2026_11_09
description: "[VERIFIED] No: events_full.jsonl is four blocks (prompts, tools, memory writes, then memory reads from the nightly retrievals.tsv), so its tail always trails to the last dream. 9 Nov: tail 19:25, but prompts 02:37, tools 02:35. Judge by max ts per kind or .grow_ran.json"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T02:45:37+04:00
  status: verified
  evidence: "an earlier session 9 Nov 02:4x: block map of events_full.jsonl = prompt 0-57556, tool 57557-63916, mem 63917-114969, mem/empty 114970-121154; max ts per kind prompt 02:37 tool 02:35 mem 02:38; retrievals.tsv last row 19:25"
---

Auditing whether the association network is still growing by reading the tail of events_full.jsonl gives a false alarm. adapt_live (called by dream_grow) rewrites the file in four blocks in a fixed order: prompts, then tool events, then memory writes (mem with text), then memory reads (mem with empty text, rebuilt from retrievals.tsv). The reads block is last, and retrievals.tsv is rebuilt only by the nightly dream (build_retrieval_trace), so the tail always trails to the last dream. On 9 Nov 02:4x the last 200 rows stopped at 19:25 the evening before, while the newest prompt was 02:37, the newest tool event 02:35 and the newest memory write 02:38, and .grow_ran.json said 02:38.

Check the network by the newest timestamp per kind over the whole file (about 121k rows, a second in python), or by .grow_ran.json. Don't use the tail, and don't use net.sqlite3's mtime: readers re-stamp it (dream_grow.py says so).

