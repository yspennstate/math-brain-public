---
name: membrane_order_lookup_one_query_not_300_2026_11_10
description: "[VERIFIED] Graph membrane order_candidates slow? 300 per-hit slug SELECTs (0.06-0.09 s cold) now one IN query (0.005 s), output identical on 44 cases; rest is bm25.score_postings"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T23:44:12+02:00
  status: provisional
  evidence: ""
---

Question: the graph membrane's order lookup (live_membrane.order_candidates, run on every prompt with topk=300 and by codex_orders_hook) - where does its time go, and what was cut?

Measured 10 Nov 2026 23:4x on the workstation under a ui_freeze alarm. After bm25.score_postings returns up to 300 hits, the old code ran one `SELECT descr, status, superseded_by FROM memory WHERE slug=?` per hit to keep only the author's orders (slug owner_* or status owner-stated). slug is the primary key, so each is an index probe, but 300 of them cost 0.06-0.09 s cold and 0.015 s warm.

Change: one `WHERE slug IN (...)` query per 500 hits into a dict before the loop; the superseded_by chain still follows hop by hop with single SELECTs (rare). Batch cost 0.005 s. Backup ~/.claude/brain_graph/bin/live_membrane.py.bak_ordbatch_20261110; mirror 12_cognitive_architecture/brain_graph/bin/live_membrane.py.

Checked: old against new on 11 queries x 2 seen-sets x topk 300/600 = 44 cases, output identical every time.

What is left: the rest of order_candidates is bm25.score_postings itself (0.03-0.18 s; about 306 sqlite executes for postings plus a heapq.nsmallest over ~33k candidates). That is shared recall code; a cut there helps every recall caller and needs its own before/after on the recall bank. The cProfile figure from earlier (0.69 s for the lookups) was inflated by profiling on a loaded box; the plain timing is the one to quote.

