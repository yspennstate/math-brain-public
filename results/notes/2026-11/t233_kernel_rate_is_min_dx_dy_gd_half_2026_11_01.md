---
name: t233_kernel_rate_is_min_dx_dy_gd_half_2026_11_01
description: [PROVISIONAL] T233 at width cL: lambda_min(K0) ~ e^(-4L/m) at dx=dy=4 (1.3 at dy=1, ~2.5 at 2/4), depth-free; GD exponent half the lazy one; divergence only for big lambda_max
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T06:32:25+04:00
  status: provisional
  evidence: ""
---



Deep linear net, Gaussian init, Du-Hu step d_y/(2L), width m = c L (T233, pushed 31e8fb4, move 5327991a; my earlier T233 notes 29-30 Oct were scalar output).

- The one-step linearized operator K = (1/d_y) sum_i lr_i (P_i^T P_i) (x) (U_i U_i^T) was checked against a real scaled step to 1.6e-7.
- At d_x = d_y = 4: log lambda_min(K0) + 4L/m sits in [-2.35, -1.43] for every cell with m >= 16 (L 16-128, c 2-0.25). The value is fixed by c alone, with no dependence on L.
- At (2,4) and (4,2) the slopes are 2.54 and 2.59: symmetric, near min(d_x, d_y), with an untested log c correction. This rules out "d_y alone".
- lambda_max(K0) has a median of 1.2-2.9 at any c.
- The lazy count, run from each seed's own E0, rises at slope 4.03 in 1/c; real GD rises at 2.01. With scalar output the gap was about 4x.
- Divergence: none of the 39 tracked seeds below lambda_max 18.2 diverged, and both above 45 did; 1 of 3 between. My "cut near 20" claim was wrong: a seed at 29 survived and one at 23 diverged.
- The registered divergence predictions were right in 4 of 5 cells.
- Run 2's medians at c = 0.35 were biased low by the 2e4 cap (run 3 at 4e4 doubled one of them).

**Why:** this points the T233 target 1 proof route. The initial operator has depth-free extremes at fixed c, so a perturbative proof is not ruled out; but it would pay about twice GD's exponent.

**How to apply:** for T233 next steps, test the log c correction over a wider c range, or try a proof that K stays within a constant factor of K0. Divergence is a first-steps event, so a theorem should shrink eta by about lambda_max(K0).

Related: [[t403_tanh_compresses_to_sign_pattern_entropy_2026_11_01]].

Folder: research-repo research_pushes/2026-11-01-loop-T233-kernel (T233_ntk.md)
