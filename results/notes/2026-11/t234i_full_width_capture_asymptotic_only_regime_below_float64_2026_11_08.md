---
name: t234i_full_width_capture_asymptotic_only_regime_below_float64_2026_11_08
description: "Are small full-width starts on T234 captured at rank two with excess >= 0.3408? (T234i) Asymptotically yes, conditional, no alpha cutoff; float64 replay 1e-30..1e-150 still 0.73..0.35 from the capture endpoint, excess 0.196..0.525"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:44:29+04:00
  status: provisional
  evidence: "~/codex_fleet/20261108_pro/workers/OPEN-T234i/REPORT.md"
---

Is every small full-width start on the T234 instance (d=40, n=60, GD step 1/20) captured at a rank-two interpolant with trace excess >= 0.3408? (T234i, 8 Nov 2026, Codex worker, reviewed by an agent.)

As an asymptotic statement, conditionally yes. In practice, no alpha that float64 can start from is in that regime.

The worker's proof (author-audited, no referee) closes T234h's incoming-to-outgoing matching. Under condition (A) on a fixed
Gaussian G, the small-alpha accumulation set is exactly the outgoing endpoint family K, with rank two and excess >= 0.3408326632.
The ordered limit exists iff K is constant, which is unproved. It is "an asymptotic existence argument, with no explicit alpha cutoff".

My replay (own float64 GD from a seed-234 40 x 40 Gaussian), at alpha 1e-30, 1e-50, 1e-80, 1e-120 and 1e-150:
- endpoint excess: 0.196, 0.220, 0.410, 0.525, 0.440
- distance to the capture endpoint (excess 0.349363): 0.73, 0.70, 0.50, 0.41, 0.35
- closest approach to the saddle z: 0.54 at 1e-50, 0.22 at 1e-120, 0.17 at 1e-150

They converge, but slowly. The second eigendirection of M = (1/n) sum y_i A_i survives the linear phase with relative size
alpha^0.085, and the closest approach scales like about (that)^0.05. On that crude extrapolation, the 1e-6 matching would need
alpha far below 1e-308. Also: rank-one GD from M's second eigenvector lands on x itself (loss 1.6e-25), so the landscape has
a second exit. My 48-phase rebuild of K collapsed to one point (spread 0), which fits constancy, but it is weak evidence.

How to apply: do not quote the 0.3408 bound for any alpha a run can use. The next move is an explicit cutoff, or K constant.
Pushed caa436602b (06_math_research/frontier/T234/OPEN-T234i, review and checks 2-7). Card claim_55b0d1d216a4456bb2f260cb675f1087,
depends_on T234h's card. Before it: [[t234h_gd_outgoing_family_captured_rank_two_higher_trace_d40n60_2026_11_08]].

Later (8 Nov 16:1x, T234j): the rate is alpha^0.0028 and the 1e-6 matching is first met between 1e-2125 and 1e-2150; see [[t234j_capture_rate_alpha_0p0028_starts_near_1e_2125_k_constancy_open_2026_11_08]].
