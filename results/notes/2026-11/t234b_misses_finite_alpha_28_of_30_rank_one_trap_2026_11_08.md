---
name: t234b_misses_finite_alpha_28_of_30_rank_one_trap_2026_11_08
description: "No (8 Nov): T234's 1.4d threshold and 'neither' verdict are finite-alpha readings - 28 of 30 n>d misses recover at smaller alpha; d40 n60 trial 1 has a reproduced positive-loss rank-one local minimum (OPEN-T234b)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T10:52:35+04:00
  status: verified
  evidence: "~/brain/online/frontier_rows/T234/open_t234b_agent_11_08/REPORT.md"
---

Is T234's "neither minimum rank nor minimum trace" verdict, or its threshold near 1.4d, a real small-initialization limit? No, both are finite-alpha readings (8 Nov, Codex OPEN-T234b). It replayed every reported alpha = 1e-12 miss: 65 baselines reproduce the historical counts. Of the 30 misses with n > d, 28 fall below 0.01 error at some smaller tested alpha. One of them, d40 n50 trial 1, is still at 0.703 at alpha 1e-96 and drops to 4.1e-7 only at 1e-288. All d160 "genuine" misses recover.

The two exceptions are real obstructions of the greedy rank-one stage. d40 n60 trial 1 (seed 60001) has a strict local minimum of the rank-one problem with positive loss and an escape direction in full width. My rebuild from the seed gives loss 0.006960465948, gradient norm about 4e-11, rank-one Hessian minimum 0.0058006 and transverse eigenvalue -0.1740358, the same across four step and alpha settings. d80 n100 trial 4 is the same kind, with loss 0.0032 after 210,000 raw GD updates. From that point a two-column flow reaches rank-two interpolants with trace ratio 1.446.

What is still not known: the ordered limit alpha -> 0 then t -> infinity for any miss. The worker's local stability lemma reduces it to certifying the minimum and branch (interval arithmetic) and proving finite-stage shadowing. Full-width endpoints at alpha 1e-288 change by 0.043 under harmless reordering, so deeper float64 runs cannot settle it.

Before quoting a T234 threshold: say which alpha it was measured at, and do not call a finite-alpha miss a limit.

Files: ~/brain/online/frontier_rows/T234/open_t234b_agent_11_08 (REPORT.md, the three .md lemmas, review_check_agent.py). Pushed to 06_math_research/frontier/T234 (7 chunks, ending f7fedc5555). Card claim_62fa31be78af444c806fcc8d7418fd2e.

Related: [[t234_small_init_gd_recovers_below_the_convex_threshold_2026_10_30]] is the reading this corrects. The single-instance version came first: the d80 n120 trial 0 miss was finite-alpha (card claim_93cdb856).

