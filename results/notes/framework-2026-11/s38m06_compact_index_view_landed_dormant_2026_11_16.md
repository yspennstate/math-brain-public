---
name: s38m06_compact_index_view_landed_dormant_2026_11_16
description: "index_text.py prompt/restore: opt-in compact MEMORY index view, -33% bytes on the live index, exact restore (S38M06, caa41a47c6a0); not wired into any hook until a paired agent test passes"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T13:23:14+02:00
  status: verified
  evidence: "AUD_S38M06/AUDIT.md; commit caa41a47c6a0; live MEMORY.md copy round trip 16 Nov"
---

Landed 16 Nov by an agent: index_text.py prompt <index> drops self-link destinations, restore rebuilds canonical bytes exactly; links followed by '(' are left untouched (the S37 codec broke there). Live index copy: 19,370 -> 12,889 bytes, round trip byte-identical. The audit's unchecked claim is the one that matters: nobody has tested whether agents choose the same memories from the compact view. Before any hook serves it, run paired agent evaluations (same questions, canonical vs compact). Install note: git apply on Windows wrote CRLF into the new lines (hash mismatch); land the audited candidate file byte for byte instead. S38M09 (knapsack context fitter for hook_dispatch.py) was NOT landed: hook_dispatch.py moved since the audit (9086b4d6 vs base 2de26b03) and the API is dormant with no real-recall gain shown. Related: [[s38m01_recall_ranking_chain_landed_2026_11_16]] the recall-speed task.
