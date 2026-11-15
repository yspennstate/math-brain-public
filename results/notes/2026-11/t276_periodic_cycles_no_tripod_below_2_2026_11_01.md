---
name: t276_periodic_cycles_no_tripod_below_2_2026_11_01
description: [PROVISIONAL] T276: periodic ReLU layer cycles (periods 2-3, widths 3-4, all pass/kink patterns) never carry the tripod legs below mean cost 2
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T02:00:11+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T276 periods >= 2 (1 Nov, an agent). Pushed 5b02880 to research-repo (research_pushes/2026-11-01-loop-T276-periodic-cycles); card claim_c384ca55d8d54334907e79c32c13eb42.

Min mean cost is 2.000000 at (w,m) = (3,1), (3,2), (4,2) and (3,3), over 26, 123, 451 and 282 feasible runs. The best cycle is always a repeated period-1 layer. The two-leg control gives 1.000000.

Method worth reusing: write the ReLU layer at the junction as act(W x), identity on pass coordinates and relu on kink coordinates, and enumerate the patterns. That turns a non-smooth search into 2^(w m) smooth problems, each finishing in seconds. The 18 Oct optimizer could not finish one start in 1,800 s.

Open: cosine cap near 1 (nearly parallel legs), and larger w and m.

Related: [[t239_trained_readout_width_drops_out_2026_11_01]].

Addendum (7246466): the same search with the cosine cap raised to 0.999 still gives a minimum of 2.000000 at m = 1 and 2 (w = 3), with a leg pair at cosine 0.998. The near-parallel corner shows no cost below 2.
