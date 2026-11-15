---
name: centrality_does_not_choose_what_to_serve_at_fusion_2026_11_11
description: "Does a centrality (link PageRank, links in/out, use-graph mass) help pick what recall serves? No (11 Nov): at fusion every fitted weight is 0 or about -0.1; a file-size penalty (-0.2) beats them all; held gain at most 8 nats on 303, hit1 unchanged."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T01:21:54+02:00
  status: provisional
  evidence: ""
---

The research statement (section 6) says "different types of centralities could choose what to serve". Tested 11 Nov 01:1x at recall's fusion stage with cent_fit.py: 606 bank questions whose gold reaches the fusion candidates, the model of [[recall_fusion_weight_048_end_to_end_small_gain_2026_11_11]] plus one term lam * z(log(1 + centrality)) over the candidates. lam was fitted on the even half of the bank ids and judged on the odd half (303 questions each). The link graph is the [[slug]] mentions between 61,823 memory files (314,073 edges).

| Centrality | lam, all items (95 pct interval) | held log-likelihood gain, w 0.3 / 0.48 | held better / worse, w 0.3 | held hit1, w 0.3 |
|---|---|---|---|---|
| link PageRank | 0.0 (-.05, .05) | -2.1 / -2.6 | 42 / 61 | 106 -> 105 |
| links in | -0.1 (-.2, -.05) | +3.9 / +2.4 | 74 / 55 | 106 -> 105 |
| links out | -0.1 (-.2, -.05) | +3.6 / +2.4 | 73 / 48 | 106 -> 108 |
| use-graph background mass p0 | -0.1 (-.2, 0) | +2.6 / +2.8 | 57 / 18 | 106 -> 107 |
| file size (control) | -0.2 (-.25, -.1) | +7.7 / +5.3 | 84 / 53 | 106 -> 106 |

- No centrality works as a positive prior. Every fitted sign is zero or negative: among the candidates bm25 and the cosine already bring in, the gold is slightly less linked, less read and shorter than its rivals.
- The strongest term is the control. A small penalty on file size beats every graph centrality, so the link effects are probably the length confound (links out grow with length). A joint fit of length and links was not run.
- The gains are small: at most 8 nats over 303 held questions, with hit1 unchanged. This is not worth a dial.
- Coverage, so that an empty reading cannot pass as a result: the link features cover 100 pct of candidates and golds; p0 covers 60 pct of candidates and 77 pct of golds (15,132 memories are in the use graph).

What it means for the statement: at the fusion stage, centrality does not choose what to serve. If a centrality helps anywhere, it would be as a mild anti-hub or length penalty, which matches the lift result in [[graph_lane_lift_gamma_flat_hubs_only_at_zero_2026_11_11]] (dividing by background mass removes the hubs).

What would change this: the bank's golds are the source memories its questions were authored from on 22 Sep. If that sample avoided hub notes, the negative sign belongs to the bank. Rerun on a bank whose golds include hubs, or run the joint fit, before using any of this.

Scripts and results are under brain_improvement/rs_implement_21ba_2026_11_10/: cent_fit.py, cent_fit.json. Nothing in the live brain was changed.

