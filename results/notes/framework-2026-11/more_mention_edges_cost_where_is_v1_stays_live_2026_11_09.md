---
name: more_mention_edges_cost_where_is_v1_stays_live_2026_11_09
description: "[PROVISIONAL] File-node where-is lookup: adding memory->path mention edges (v2/v3 rebuilds, unions) LOWERS fused hits; v1 stays live. Extra edges and extra many-path memories both crowd the vote."
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T00:18:31+02:00
  status: provisional
  evidence: ""
---

Measured 9 Nov 00:1x on the 1,219,021-node file layer, fused lookup (file_node_lookup.py, FILE_NODE_MENTIONS=<store>), penalty 0.6, commit_bank_named_v1 (424) and commit_bank_strict_v1 (398); plain lookup 146/80 and 82/56 in every run.

hits@8 / hits@1, named | strict:
- v1 (mentions.sqlite, 8,606 memories, 10,887 edges): 160/110 | 101/68
- v1 memories + v3 edges on them (15,279 edges): 155/106 | 96/65
- v1 + everything v3 adds (10,122 memories, 20,265 edges): 148/102 | 89/62
- v3 (9,951 memories, 19,489 edges): 148/102 | 89/62
- v2 (26,782 edges): 146/102 | 87/62

Why it matters: the union keeps every v1 edge yet equals v3, so dropped edges were not the cause (a peer guessed they were). Both added parts cost about the same per bank: new edges on old memories -5 hits@8, the 1,516 new memories (compaction notes and run logs quoting many paths) -7 more. A memory that names forty paths spreads its vote thin and matches question words as well as the memory that names the one right file; mirror copies of the right file count as misses. More edges are not more signal.

How to apply: do not swap mentions.sqlite for a bigger build on edge count alone; A/B it on both banks first. Untested next step: weight each memory's vote by 1/(paths it names) or drop memories naming more than a few paths, then re-add the extra memories.

Write-up: private-repo c05228bb, 12_cognitive_architecture/brain_improvement/graph_ablation_2026_11_08/MENTIONS_EDGES.md (union_v13.py and both logs beside it). Related: [[memory_mentions_edges_lift_strict_where_is_17_to_22_2026_11_08]], [[file_node_layer_1_2m_nodes_keeps_where_is_accuracy_5x_slower_2026_11_08]].
