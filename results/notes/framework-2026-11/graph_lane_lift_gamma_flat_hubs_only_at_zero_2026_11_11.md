---
name: graph_lane_lift_gamma_flat_hubs_only_at_zero_2026_11_11
description: "Graph lane lift exponent gamma (hand-set 0.5)? Flat from 0.375 to 1.0 on the 544-question bank (lane alone finds gold in top 200 for ~22); gamma 0 (raw conserved mass share) lets 8 hubs take 26 pct of top-20 slots. Leave 0.5."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T00:05:20+02:00
  status: provisional
  evidence: ""
---

The use-graph lane ranks a memory by its walk mass over its background mass to the power gamma (diffusion.memory_matrix: R / p0^gamma), gamma set by hand at 0.5. Swept on the known-answer bank on 11 Nov 00:0x (gamma_fit.py, 544 questions, word seeds, the lane's own walk: alpha 0.3, 20 steps, 390,676 nodes):

- The lane alone is weak at every gamma: the gold memory is in its top 200 for 17-26 of 544 questions, top 20 for 2-5, top 1 for at most 1. MRR .0023-.0030. This matches mixing_depth.json (35 of 544 in the top 200 at the best depth), so it is the lane, not the sweep.
- gamma does not matter between 0.375 and 1.0: all-question MRR .0026-.0030, held-half hit20 0-2, and every gamma beats 0.5 on about 13 questions and loses on about 12. No gamma clearly beats 0.5. Leave it.
- gamma 0 (the raw share of the question's mass that stops on the memory - the conserved quantity of the research statement, section 8) is hub-ridden: 8 memories sit in the top 20 of at least a quarter of all questions and take 26 pct of all top-20 slots (1,425 distinct memories in the top 20s against 2,126 at 0.5). Any gamma >= 0.375 removes those hubs completely; 0.25 leaves one (3.8 pct of slots).
- Median share of a question's walk mass that lands on memory nodes: 4.2 pct. The rest stops on word and other nodes.

So the conserved mass share is a good accounting quantity but a bad ranker until it is divided by background mass; the lift exponent only needs to be big enough to kill the hubs, and past that the lane's ranking is flat. The lane's value, if any, is inside fusion, not on its own. Not done: an end-to-end bank run with gamma changed (no reason to run one - nothing to move to).

What would change this: a bigger bank or a stronger seed set where the lane alone reaches the gold more often; then rerun gamma_fit.py.

Script and result: brain_improvement/rs_implement_21ba_2026_11_10/ (gamma_fit.py, gamma_fit.json). Dial owner: recall-10x (an agent); nothing was edited in diffusion.py or graph_lane.py.
Related: [[use_graph_walk_push_loses_to_eight_steps_2026_11_10]] [[use_graph_decay_fits_0_7_not_0_5_2026_11_10]] [[recall_lost_before_fusion_is_reworded_miss_not_a_cap_2026_11_10]]

