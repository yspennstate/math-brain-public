---
name: recall_filename_lane_and_ppr_no_gain_fsym25_26_2026_11_09
description: "No, neither (FSYM25/26): filename lane 81->80 of 218 hit@5; personalized PageRank ties two-hop walk 119/504, 16x slower; keep live fusion"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T07:40:03+04:00
  status: provisional
  evidence: "private-repo frontier/T021/fsym_workers_2026_11_09/FSYM25,FSYM26 (d5b860e18e)"
---

No, neither (9 Nov, Codex FSYM25 and FSYM26, gpt-6.1-sol high). Keep live recall fusion as it is.

FSYM25, a file-name lane fused at weight 0.1 (fixed on dev paraphrases before the held-out set was opened):
- Held-out September paraphrases: hit@5 81/218 now vs 80/218 with the lane.
- 1 item gained, 2 lost; McNemar p = 1.
- The lane alone found a primary gold in its top 5 on 6/218 items.

FSYM26, converged personalized PageRank vs the current two-hop spreading walk:
- Both hit the same 119 of 504 queries at hit@5 (23.6%), with identical per-query status.
- MRR 0.155884 vs 0.156006.
- Median time per query rose from 31 ms to 504 ms.
- Caveat: the test split was reconstructed, because the original exclusion list is missing, so this is not a fresh held-out result.

So BRAIN_SCIENCE_AUDIT's PPR step does not earn live status on this data. Spreading depth is not where recall misses come from. That matches [[brain_arm_misses_are_surfacing_misses_seen_426_of_479_unseen_23_of_331_2026_11_09]]: most misses have no gold row at all.

Reports: private-repo 06_math_research/frontier/T021/fsym_workers_2026_11_09/FSYM25 and FSYM26 (push d5b860e18e). The rows stay local because they hold test keys.

