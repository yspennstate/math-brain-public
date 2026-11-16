---
name: bm25_topk_slugs_one_query_2026_11_11
description: "[VERIFIED] bm25.score_postings slow at large topk? It ran one slug SELECT per hit (300 for the membrane); now one IN query, 80 cases identical, battery ~40 pct faster"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T00:01:01+02:00
  status: provisional
  evidence: ""
---

Question: bm25.score_postings (the BM25 arm behind brain.py recall, the graph membrane's order and word lookups, and other hooks) - after the 14 Oct fast loop and the 4 Nov heap top-k, what was left?

Measured 10-11 Nov 2026 on the workstation under a ui_freeze alarm. Profiling the graph membrane hook cold (1.4-1.7 s) put about 0.36 s in score_postings: 389 sqlite executes and 49 dict.update calls. The update calls are the fast per-term loop and stay. Most of the executes were the last step: one `select slug from d where pos=?` per top-k hit, and the membrane asks for topk=300.

Change: the top-k positions go through one `select pos, slug from d where pos in (...)` per 500 into a dict, then the list is built in the same top-k order, skipping a position with no slug exactly as before. Backup ~/.claude/dreaming/bm25.py.bak_slugbatch_20261110; mirror 12_cognitive_architecture/dreaming/bm25.py.

Checked: old against new on 16 queries (common words, a nonsense token, owner-law wording, long and short) at topk 5, 20, 40, 300 and 600 = 80 cases: every result list identical, scores included. The whole battery ran 34.2 s -> 20.9 s, then 26.6 s -> 15.2 s on a second pass (loaded box, read as a direction; the gain is largest at topk 300-600 and small at topk 20).

Left: names_of in live_membrane.py spends about 0.26 s reading ~4,000 node rows with their use JSON - it is data volume, not query count. The membrane's word_candidates still does one SELECT per hit (topk 40, small).

Related: [[membrane_order_lookup_one_query_not_300_2026_11_10]], [[waste_sense_msys_verdicts_shared_two_minutes_2026_11_10]].

