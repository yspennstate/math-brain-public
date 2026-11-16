---
name: memory_mentions_edges_lift_strict_where_is_17_to_22_2026_11_08
description: "[VERIFIED] Where-is lookup on repo files misses descriptive questions? Memory->path mention edges, fused into file_node_lookup by RRF (agent, 8 Nov 13:1x), lift strict commit bank 17.3 -> 25.6 pct hits@8 (24.9 leak-adjusted per rescue), named 31.6 -> 38.4 (38.2); rescuing memories look like controls"
metadata:
  node_type: memory
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:23:32+02:00
  status: provisional
  evidence: ""
  modified: 2026-11-08T10:53:49.099Z
---

Links from memories to the repository paths they mention, laid on the file-node layer (one node per repo file and folder), lift the where-is lookup on the strict commit bank (questions that describe a place without naming it) from 17.3 to 21.6 pct hits@8 when the mention route fills the last two of eight slots, rescuing 17 and losing 0; 22.9 under reciprocal-rank fusion. Named bank 31.6 -> 34.4 (19 rescued, 7 lost).

Build: 57,745 memory files, 8,606 mention a layer path, 10,887 edges, kept beside the layer in mentions.sqlite with a small FTS5 index of the mentioning memories. Leak check: the memories that supply hits share no three-word run with the question at the median; 3 per bank carry half or more, and counting every one as a leak the strict arm still reads >= 20.9 pct.

Cost: the eval runs at 1.6 s a question, but timed apart (8 Nov 11:4x, 20 strict questions) the base layer lookup takes 1,755 ms and the mention route 92 ms; fts5vocab and a keyed df table give 12-44 ms and identical lists on 100 questions. The route is cheap; the layer lookup is the cost. The build was CPU-starved at BelowNormal on a saturated machine (reads were 500 files/1.1 s); at Normal the last 47,000 files took five minutes.

Write-up and code: private-repo 12_cognitive_architecture/brain_improvement/graph_ablation_2026_11_08/MENTIONS_EDGES.md (main 0b3b2f6d). Peer layer owner: an agent. Decided 8 Nov 12:51 by the layer owner: the edges stay BESIDE the layer in mentions.sqlite (never folded into file_nodes.sqlite, so a layer rebuild cannot drop them); file_node_lookup will ATTACH mentions.sqlite read-only and join by node id. Do not change mentions.sqlite's schema without telling the layer owner. Related: [[graph_structure_in_brain_recall_only_learned_links_move_the_top_8_2026_11_08]] [[belownormal_recall_eval_cpu_starved_not_slow_code_2026_11_08]].

IN THE LOOKUP (8 Nov 16:3x): an agent put the edges into file_node_lookup.lookup itself - ATTACH mentions.sqlite as m, mention_ids() (rarest 10 terms by m.df, top 30 bm25 memories, each votes 1/(i+1) for its nodes), fuse() RRF k 60 over the base list cut at 40; FILE_NODE_MENTIONS=0 turns it off. My per-rescue leak audit on that exact path (graph_ablation_2026_11_08/fused_leak_audit.py, output fused_leak_audit_2026_11_08.txt): strict base 69 (17.3) -> fused 102 (25.6), 34 rescued, 1 lost; named 134 (31.6) -> 163 (38.4), 45 rescued, 16 lost. Rescuing memories: 3-gram share median 0.00, p90 0.08/0.17, no verbatim question; controls (top memory of every other question) have the same median and a high tail of 2 per bank against the rescues' 3 and 1. Counting every rescue with share >= 0.5 as a miss: strict 24.9, named 38.2. So the gain is recall, not copied commit subjects. The earlier line in this note that blamed fts5vocab for the 1.6 s was wrong: the base layer lookup is the cost (see the Cost paragraph above).
