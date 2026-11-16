---
name: also_see_line_beats_fused_never_loses_a_hit_2026_11_09
description: "[VERIFIED] File-node where-is lookup: fused list loses private-repo hits, plain loses all-repo first answers - how to keep both? Print the fused top 8 then an 'also see' line of up to 3 plain picks; live 9 Nov"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T16:29:16+02:00
  status: provisional
  evidence: ""
---

File-node lookup (, task dir 12_cognitive_architecture/brain_10x_file_nodes_2026_11_08). Every arm that let the mention vote into the top 8 cost plain a private-repo hit (rerank, half, tail, pin1, vote_gate_eval.log). Arm also3r (also_see_eval.py): the fused top 8 (plain + vote by RRF, as live), then up to 3 of plain's top 8 the fusion left out. Being the fused list plus extras it can never show fewer hits than the fused list and its first answer is the fused one. hits@shown/hits@1 on the commit banks, 9 Nov: all-repo named plain 142/78, fused 161/109, also3r 178/109; private-repo named plain 47/26, fused 36/22, also3r 46/22; private-repo strict plain 10/5, fused 8/4, also3r 9/4; all-repo strict plain 77/54, fused 100/68, also3r 104/68. Landed 16:2x 9 Nov: file_node_lookup.main prints the fused top 8 then 'also see:' (new function lookup_also; lookup() unchanged). It printed on 30 of 30 private-repo bank questions; a hand-typed question with an empty vote prints no also line. Still one short of plain on private-repo hits@shown and four short on private-repo hits@1 - a first-answer arm that keeps the fused all-repo gain is the open question. Related: [[more_mention_edges_cost_where_is_v1_stays_live_2026_11_09]] [[memory_vote_per_path_norm_wins_no_bank_2026_11_09]] [[folder_gate_on_mention_vote_trades_old_bank_for_brain_repo_2026_11_09]]
