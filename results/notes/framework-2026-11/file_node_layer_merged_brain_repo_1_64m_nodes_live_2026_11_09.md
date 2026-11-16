---
name: file_node_layer_merged_brain_repo_1_64m_nodes_live_2026_11_09
description: "[PROVISIONAL] Brain 10x file layer: live store is now 1,644,216 nodes incl. 425,195 private-repo nodes (9 Nov 00:3x). Private-repo commit banks 0/150 -> 47/150 named, 0 -> 10 strict; other-repo banks tie within one question; body-written NODESB bank 0/80 either way (name-asked control 67/80)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T00:35:48+02:00
  status: provisional
  evidence: ""
---

The file-node layer (file_nodes.sqlite) covered every repo except the brain repo itself, which the NODES Codex brief had built separately (file_nodes.sqlite). merge_brain_repo_nodes.py copied its 376,828 files and 48,367 folders into a copy (insert or ignore, contains edges from parents, heading as node_text.head), then fts_add_missing.py indexed the 425,195 new rows. Swapped live 9 Nov 00:3x; the old 1,219,021-node store is file_nodes.sqlite.pre_merge_20261109.

Measured (task folder brain_10x_file_nodes_2026_11_08, logs eval_merged_1644k.log and eval_brainrepo_bank.log): on banks built from the brain repo's own commits (build_commit_bank.py, 150 named + 150 strict), the old store scored 0 and 0, the merged store 47 named and 10 strict at the plain arm. Fused with the memory-mention vote it scores lower there (36, 8), so the vote pulls away from private-repo files on those questions. Other-repo commit banks: fused 161/424 named (old 160), 100/398 strict (old 101). Cost 0.9-1.2 s a question, up from about 0.6.

The NODESB held-out bank (80 questions written from file bodies) scores 0/80 on any name/path/head layer: the median question shares no words with its gold file's name, path or first 400 characters. A positive control asking for the same 80 files by name finds 67, so the zero belongs to the bank, not to a blind lookup. A body-text arm would be needed for those.

What would change this: a recall hookup that reads this store, or a fused arm tuned for private-repo questions.

Related: [[file_node_layer_1_2m_nodes_keeps_where_is_accuracy_5x_slower_2026_11_08]] [[file_node_layer_483k_nodes_where_is_0_to_11_of_20_2026_11_08]] [[memory_mentions_edges_lift_strict_where_is_17_to_22_2026_11_08]] [[commit_history_per_file_finds_files_questions_describe_2026_11_08]]
