---
name: use_graph_decay_fits_0_7_not_0_5_2026_11_10
description: "[PROVISIONAL] Use-graph ACT-R decay d (set by hand 0.5)? Fitted 0.70 on 862 logged reads (interactive sessions 0.75); top-10 hits 207 -> 230-239, first place flat; not yet end-to-end"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T23:26:13+02:00
  status: provisional
  evidence: ""
---

The use graph's node size is an ACT-R base level B_i(t) = ln sum_k (t - t_ik)^-d (graph_recall.py ~line 66, context_rank.py ~line 84), with d set by hand at 0.5. Fitted by maximum likelihood on 10 Nov 23:2x:

- Data: kind "mem" rows of brain_graph/events_touch.jsonl, 17 Aug - 10 Nov (86 days), collapsed to the first read of each memory in each session: 10,425 reads of 6,363 memories. 21 burn-in days, 2,000 reads sampled evenly. Candidates for a read at t are the memories read before t in another session. Model: conditional logit softmax(beta * B_j(t; d)).
- 1,138 of the 2,000 sampled reads (57 pct) are of a memory nobody had read before. No decay can predict those; 862 are modelled (interactive sessions 700, test 105, script 57).
- Fit: d 0.70 on all (bootstrap 0.65-0.70), 0.75 on interactive sessions and on not-test (0.70-0.75). Log-lik at 0.5 is 110 nats worse than at 0.7 on all, 161 worse on interactive sessions. Test workers fit 0.35 and scripts 0.40, so the mix matters.
- Ranks (gold among candidates ordered by B, 862 reads; same reads as the fit, one parameter): d 0.5 -> hit1 59, hit5 148, hit10 207, MRR .127, median rank 67; d 0.6 -> 61 / 156 / 221 / .134 / 55; d 0.7 -> 56 / 157 / 230 / .132 / 50; d 0.75 -> 55 / 156 / 239 / .131 / 51. Interactive sessions alone, 0.5 -> 0.75: hit5 112 -> 139, hit10 165 -> 203, hit1 52 -> 49, MRR .130 -> .142.
- So: a faster decay (0.6-0.75) moves the right memory into the top 10 more often and leaves first place flat. Same shape as the fusion-weight fit (w 0.48, CI 0.42-0.52: hit5 and hit10 up, hit1 flat).

Not done: an end-to-end recall check with d changed in graph_recall.py/context_rank.py (the use-graph lane is one input among several; a base-level gain need not survive fusion), and a date split (fit on early reads, rank on late). Until then d stays 0.5; the dial is the recall-10x agents' to move. What would change this: a date split that puts the late-period optimum back near 0.5, or an end-to-end bank run where d 0.7 loses.

Scripts and results: brain_improvement/rs_implement_21ba_2026_11_10/ (fitd_fit2.py, fitd_rank.py, fitd_result.json, fitd_rank.json). The first fit (6,000 reads, fitd_fit.py) hit its 25-minute limit with nothing written; the lighter one ran in about 10 minutes.
Related: [[use_graph_walk_push_loses_to_eight_steps_2026_11_10]] [[recall_lost_before_fusion_is_reworded_miss_not_a_cap_2026_11_10]]


- DATE SPLIT (23:2x, fitd_datesplit.py on fitd_L.npz, rows in time order): interactive sessions, fit on the earlier 350 reads -> d 0.65; on the later 350 it beats 0.5 by 144 nats, 280 reads better / 70 worse. Not-test the same (0.65; +146 nats; 289/90). All sessions mixed: the early half fits 0.5 (test workers weigh more there), so no gain. The later half alone fits 0.8 in every group: the best decay is rising as the store grows. Still not end-to-end.

- WHERE d IS USED: not brain.py recall. live_membrane.py base_level() (the "a big node right now" memory pick, bar mem_size_min 1.89, and w_size 0.5 in its fusion) and graph_recall.py tie-breaks. A d change rescales sizes, so the bar must move with it (same firing share: 1.89 at 0.5 = 1.60 at 0.6, 1.35 at 0.7, 1.26 at 0.75, 1.20 at 0.8).
- MEMBRANE REPLAY (fitd_membrane_replay.py, every 40th fire row after the burn-in, 8,277 rows, 8,167 interactive): control, rebuilt d 0.5 size vs logged size corr 0.989, median gap 0.0003. Biggest-node pick read by the same session within 30 min: d 0.5 13, 0.6 18, 0.7 28, 0.75 29, 0.8 34; among the 2,338 rows over the (matched) bar 6 / 9 / 12 / 13 / 14. Faster decay about doubles it, but the base is tiny (0.26 -> 0.56 pct of firing rows), and a memory the hook shows needs no file read, so this undercounts. First run read 0 everywhere: fires.jsonl sid is the full uuid, events_touch session the 8-char prefix - match on sid[:8].
- Verdict for now: direction holds three ways (likelihood, date split, membrane replay); the size is small. Not landed: live_membrane.py has no named owner on the mesh tonight and graph_learn.py moves its bars; a change is d 0.7 with mem_size_min 1.35 together.
