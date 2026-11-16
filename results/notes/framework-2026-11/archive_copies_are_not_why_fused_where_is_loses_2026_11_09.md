---
name: archive_copies_are_not_why_fused_where_is_loses_2026_11_09
description: "[PROVISIONAL] File-node where-is: do the 19 pct archive-copy nodes make the fused lookup lose to plain search? No - folding them into live twins or dropping them wins 1 of 11 lost hits (named 37 vs 36, strict 8 vs 8; plain 47, 10); the mention vote is the cause"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T11:03:38+02:00
  status: provisional
  evidence: ""
---

Measured 9 Nov 09:2x-11:0x on the merged 1,644,216-node store, banks commit_bank_brainrepo_named_v1 and _strict_v1 (150 q each, hits@8/hits@1).

plain (lexical candidates only): named 47/26, strict 10/5
a0 (plain fused with the memory-mention vote, the live lookup): 36/22, 8/4
collapse (archive nodes swapped for their live twin by path, else name+sha): 37/22, 8/4
drop (archive nodes removed from both lists): 37/22, 8/4

So the store audit's 314k archive-copy nodes ([[file_node_store_audit_clean_tree_but_19pct_archive_copies_2026_11_09]]) cost the fused list at most one hit. The loss to plain on private-repo questions comes from the mention vote pushing other files ahead. Rejected by the land rule (beat a0 on both private-repo banks). Next test: vote_gate_eval.py (vote limited to re-ordering the plain top 40, half weight, or only slots 7-8).

Files: 12_cognitive_architecture/brain_10x_file_nodes_2026_11_08/twin_eval.py, twin_eval.log, repo_eval.log. Related: [[memory_vote_per_path_norm_wins_no_bank_2026_11_09]], [[more_mention_edges_cost_where_is_v1_stays_live_2026_11_09]].
What would change it: a bank whose gold files live mostly in the backup repos.
