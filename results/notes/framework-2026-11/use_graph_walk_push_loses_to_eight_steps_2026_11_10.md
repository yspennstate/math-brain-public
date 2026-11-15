---
name: use_graph_walk_push_loses_to_eight_steps_2026_11_10
description: "Prune the use-graph walk with the ACL push? No: on the 391k-node walk the push touches 62k nodes and keeps top-20 worse than an 8-step power walk (0.13 s vs 16-step 0.25 s, gold rank identical on 40 q). Step count is the lever."
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T20:51:29+02:00
  status: provisional
  evidence: "Downloads/career/drafts_2026-11-10/rs_implement/push_ppr.json"
---

The research statement (section 3, rs_cv_v3/canonical/rs.txt line ~418) proposes pruning the use-graph walk with the
Andersen-Chung-Lang push. Measured 10 Nov 20:5x on the deployed walk (graph_lane_store, 390,676 nodes, alpha 0.3,
cap 300), 40 bank questions, word seeds only (no lexical-feedback seeds), script
Downloads/career/drafts_2026-11-10/rs_implement/push_ppr.py, result push_ppr.json:

- deployed 16-step walk: 0.25 s median, within 4e-5 L1 of a 100-step walk, top 20 identical.
- 8-step walk: 0.13 s, top 20 shares 20 (median) / 19 (worst) with the 100-step walk, gold rank identical to the
  16-step walk on all 40.
- 4-step walk: 0.07 s, top 20 shares 19 / 17, gold rank 1 better and 1 worse than 16 steps.
- push (frontier form, every node above eps settled each round; leftover residual = certified L1 bound, held on 40/40):
  eps 1e-4 0.17 s, touches 62k nodes, leaves 0.44 L1, top 20 shares 18 / 12; eps 1e-3 0.09 s but top 20 shares only 5.

Why the push loses here: P is row-normalised, so ACL's degree-scaled threshold is just eps, and its bound of
1/(eps*alpha) pushes is 33k pushes at eps 1e-4, each touching up to 300 out-edges - about as many edge visits as 16
full steps. The bound is independent of N but N is not large next to cap/(eps*alpha) on this graph, and word seeds spread
the mass thin (no low-conductance pocket around the seeds). The push's leftover is spread evenly enough that the ranking
survives an L1 error of 0.44 at 1e-4, but a short power walk keeps the ranking far better per millisecond.

So the speed lever on the walk is the step count, not the push: 8 steps halves the walk (about 0.12 s a recall) with no
change seen on 40 questions. Caveats: word seeds only (the served walk adds up to 5 feedback seeds), the walk-alone
gold was never in the top 20 on these 40 (ranks compared inside 200), CPU was loaded (85%) during timing, paired per
question. mixing_depth.py (same folder) measures the depth at which each question's gold rank stops improving; read
mixing_depth.json before changing BRAIN_PPR_ITERS. graph_lane.py's iteration count belongs to the recall-10x owners
(an agent set 20 -> 16 on 4 Nov); handed to them, not changed here.

What would change this: a graph with tight clusters around the seeds (the math store's links?) or a seed that is one
node, where the push is local. Not tested.


Depth on the whole bank (mixing_depth.py, 544 questions, word seeds only, 10 Nov 21:47): the gold memory is in the
walk's top 200 on 35 of 544; on those 35 its best rank is first reached at step 1 (14), 2 (15) or 3 (6), never later,
so 8 steps has margin. Ranks wobble between steps 4 and 16 without improving the best. Three key-free stopping
measures (collision decay from the seeds, one-step escape, top-20 settle depth) do not predict that depth (Spearman
p 0.22 to 0.96), so a per-query adaptive depth has no basis yet. Going below 8 is untested end to end.
