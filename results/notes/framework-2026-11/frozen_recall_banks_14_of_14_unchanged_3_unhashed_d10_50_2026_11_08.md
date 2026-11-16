---
name: frozen_recall_banks_14_of_14_unchanged_3_unhashed_d10_50_2026_11_08
description: "[VERIFIED] Yes (8 Nov): D10 #50 frozen recall banks on the worker machine, 11 .sha-frozen files and 4 status-line-hashed banks (15: 13 banks, 2 pre-registrations) all unchanged; 3 loose banks had no hash and were hashed then; D10 #76 rerank lift already measured"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:12:33+04:00
  status: verified
  evidence: "d10_50_frozen_banks_unchanged_2026_11_08.py"
---

Do the worker machine's held-out recall banks stay frozen after they are used, as 1000-ways D10 #50 asks? Yes, all 15 hashed files have stayed the same: 13 banks and 2 pre-registrations (the 14 in this slug is a miscount). Measured 8 Nov by an agent.

- Under the porting folder, 11 files are frozen by a .sha beside them: W06 rounds f, j and l, and the D2 #25 PREREG and PREREG_B banks with their pre-registrations. All of them still match their sha256.
- Rounds g, h, i and m have no .sha, but each matches a hash written in a BRAIN_INSTALL_STATUS line.
- Three banks had no recorded hash at all: w06_checks/fresh_bank.tsv, w06_checks/movie_film_syn_bank_2026_11_08.tsv and w06_round_n/bank.tsv. I put their hashes in a status line on 8 Nov, so from then on they can be shown unchanged. Before that date nothing can show it.

So the practice exists and has held. The gap is that hashing is a habit, not a step: a third of the loose banks had none. The math banks in ~/.claude/dreaming/state (bank_*.json) are outside this check.

Check: d10_50_frozen_banks_unchanged_2026_11_08.py, read only, exit 1 on any change. Control: a planted bank with a right and a wrong .sha passes and fails. It reads .sha files, then looks for each loose *bank*.tsv's sha256 (first 12 hex) in the status file.

D10 #76 (rerank marginal lift) was answered earlier, by [[the_query_semantic_lane_lifts_recall_reach_on_the_mac_2026_10_29]] (paired, top 8 39 to 44 of 60, p 0.006) and [[reranker_lifts_top1_4_to_14_of_350_loses_depth_hybrid_rows_1_20_design_2026_11_04]] (a design pass, not yet held-out). A frozen bank like these is what that held-out run would need.

