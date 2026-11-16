---
name: graph_structure_in_brain_recall_only_learned_links_move_the_top_8_2026_11_08
description: "[PROVISIONAL] Does graph structure help brain recall? Ablation 8 Nov, 16 fresh questions, top 8: full 7 first / 10 in top 8 (MRR .499); learned links off 4/10 (.386); association spread off too: identical lists 16/16 (BM25-first ranking puts the spread in a tail); query-meaning lane off 5/9 (.394). Only learned links move rank; new graph structure must reorder the BM25 pool, not add a tail. One rep (rep2 stopped for low memory)."
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:32:24+02:00
  status: provisional
  evidence: ""
---

Measured by an agent on the first machine, 8 Nov 2026 02:0x-03:19, for the Graphify TOP10 item. Arms in fresh processes, BRAIN_RECALL_SERVER=0 in each: full; nolinks (BRAIN_GRAPH_SIDECAR pointed at a missing file); nostruct (+ sr._load_graph patched empty with _r02=True, header reads graph off); lexonly (+ BRAIN_RECALL_QUERY_EMBED=0; the header's 'semantic on' is the seed-centroid lane, which stays). Results: full top1 7 top3 9 top8 10/16 MRR 0.499; nolinks 4/8/10 0.386; nostruct identical to nolinks on all 16 top-8 lists; lexonly 5/7/9 0.394 with all 16 lists changed. Why the spread is inert: brain.py ranks BM25 first, then a graph tail, then a semantic tail (comment near line 3355), so act scores only surface when BM25 runs out. The learned links work because they reorder inside the pool. Status provisional: one repetition only, 16 questions; the second rep was stopped by Claude Code under memory pressure (RAM 1.7 GB, commit 92 pct) before any arm finished. Would change it: a second rep or a larger bank where the spread arm differs. Bench: top10_agent/ablate/run_ablate.py and summary.txt (questions are not copied anywhere). Board: GRAPHIFY page commit 7c9916aef. Related: [[a_monkeypatched_graph_loader_is_bypassed_by_the_sgraph_cache_2026_11_08]].
