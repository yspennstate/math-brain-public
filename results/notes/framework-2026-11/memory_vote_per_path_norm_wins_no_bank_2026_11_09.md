---
name: memory_vote_per_path_norm_wins_no_bank_2026_11_09
description: "[PROVISIONAL] File-node where-is lookup: dividing each memory's vote by how many paths it names (n=0.5/1) wins no bank of five; live a0n0 stays"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T03:50:28+02:00
  status: provisional
  evidence: ""
---

File-node where-is lookup: dividing a memory's vote for each path by (number of paths that memory names)^n does not help. Five banks, hits@8/hits@1, live a0n0 vs n0.5: where_v1 269/10 vs 268/10; private-repo named 36/22 vs 35/22; private-repo strict 8/4 tie; old named 161/109 vs 160/110; old strict 100/68 tie. n1 and a0.5n0.5 are no better. Wins no bank, so the live a0n0 fused lookup (bm25 memory vote, RRF k=60) stays. Long index notes are not what pulls the fused lookup off private-repo answers.

**Why:** a lead from the private-repo bank loss (fused 36 vs plain 47); this closes the per-memory-length idea alongside agent's damp result (a0 wins 5/5) and the folder gate (net -25).

**How to apply:** don't re-test vote normalisation by memory length or path popularity; the private-repo gap needs memories that name private-repo files. Table: 12_cognitive_architecture/brain_improvement/graph_ablation_2026_11_08/MENTIONS_EDGES.md (private-repo 7852a40d), norm_eval.log, norm_eval.py. Related [[folder_gate_on_mention_vote_trades_old_bank_for_brain_repo_2026_11_09]], [[more_mention_edges_cost_where_is_v1_stays_live_2026_11_09]].

