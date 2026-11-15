---
name: t383_lazy_regime_piece_ratio_1p17_1p03_1p02_widths_32_128_512_2026_11_02
description: T383 target 1 numerics: depth-3 1-D NTK nets, exact piece counts, trained/init ratio mean 1.17, 1.03, 1.02 at widths 32, 128, 512; weights move ~m^-1/2; consistent with lazy-regime constant factor
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T02:05:08+04:00
  status: provisional
  evidence: "research_pushes/2026-11-02-loop-T383-lazy-regions (research-repo 82a79eb); frontier move ffda510"
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---

T383 target 1 (does the linear-region count stay within a constant factor of its initial value in the lazy/NTK regime?): numerics on 2 Nov, at research-repo research_pushes/2026-11-02-loop-T383-lazy-regions (82a79eb; README.md, lazy_regions.py, check_count.py, run1.txt). Frontier move on T383 at brain-repo ffda510.

Setup: depth 3 with two hidden layers of width m, 1-D input, NTK parametrization, all weights N(0,1). Full-batch GD at lr 1 for 2,000 steps on sin(3x) at 64 points; every run fit (loss 0.003-0.009). Pieces of the hidden map on [-3,3] are counted exactly: first-layer breakpoints, then the exact zeros of the second layer's affine pre-activations on each interval. The counter equals a 2,000,001-point grid count on 3 of 3 nets.

Result (3 seeds per width):
- Trained/init ratio: 1.07-1.22 at m = 32 (mean 1.17), 0.995-1.074 at 128 (mean 1.03), 1.009-1.027 at 512 (mean 1.02).
- About 1.45 pieces per neuron at init.
- Training adds pieces slightly: 8 of 9 runs come out above 1.
- The hidden weights' maximum relative move is 0.48-0.60, 0.27-0.37 and 0.15-0.17, about m^(-1/2).

So the region count is within a constant factor at every width, and the factor tends toward 1. That is consistent with target 1, but it is numerics at one depth in one input dimension, not a proof. The rate of the excess is not pinned by 3 seeds.

Next for this row: a proof in the two-layer case, where breakpoints -b/w move O(m^(-1/2)) and only neurons whose breakpoint crosses a segment end change the count. Or more seeds and a 2-D input to fix the rate.

