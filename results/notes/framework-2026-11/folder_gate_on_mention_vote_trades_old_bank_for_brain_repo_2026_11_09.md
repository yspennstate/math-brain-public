---
name: folder_gate_on_mention_vote_trades_old_bank_for_brain_repo_2026_11_09
description: "[PROVISIONAL] File-node where-is lookup: gating the memory mention vote to the plain top hit's folder recovers private-repo questions (named 36->45 of 150) but loses the old banks (160/110->146/83 named, 101/68->90/56 strict); net -25, ungated fused stays live"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T02:28:34+02:00
  status: provisional
  evidence: ""
---

Folder gate (MENT_VOTE_GATE=2: a mention vote counts only for nodes sharing repo/first-folder with the plain lookup's first hit), tested 9 Nov 02:10 by an agent on a scratch copy of file_node_lookup.py. Private-repo commit banks on the merged 1,644,216-node store: plain 47/26 named, 10/5 strict; ungated fused 36/22, 8/4; gated 45/26, 9/5. Old commit banks on the pre-merge store: plain 146/80, 82/56; ungated fused 160/110, 101/68; gated 146/83, 90/56. The vote's old-bank wins are exactly cross-folder rescues, so any folder gate erases them. Weighting votes by paths named (norm a=0.5/1, cap 5) moved nothing either. What would lift private-repo questions is memories that name private-repo files, not a rule on the vote. Record: private-repo e49f0399, 12_cognitive_architecture/brain_improvement/graph_ablation_2026_11_08/MENTIONS_EDGES.md. status: provisional (one bank pair). Related: [[more_mention_edges_cost_where_is_v1_stays_live_2026_11_09]] [[memory_mentions_edges_lift_strict_where_is_17_to_22_2026_11_08]] [[file_node_layer_merged_brain_repo_1_64m_nodes_live_2026_11_09]]

Full-bank rerun, 9 Nov 21:29 (an agent, vote_gate_eval2.py, vote may only re-order plain's top 40, merged 1.64M store, all banks on the same store). hits@8/hits@1: old named 424q plain 142/78, a0 161/109, gate 155/106, gatehalf 155/106, gate20 148/99; private-repo strict 150q plain 10/5, a0 8/4, gate 9/4, gate20 10/4; private-repo named 150q plain 47/26, a0 36/22, gate 47/22, gate20 47/24. Verdict: the gate keeps plain's private-repo hits@8 (+11 over a0) but costs the old bank 6 hits@8 and 3 hits@1 and never wins hits@1 on the brain repo. Land rule (beat a0 on both private-repo banks without losing the old bank) FAILS; a0 stays live. Caches: brain_10x_file_nodes_2026_11_08/*.cand.jsonl, log vote_gate_eval2.log.
