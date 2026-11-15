---
name: t388_partial_trace_is_fobi_bbp_threshold_oja_step_rule_2026_11_04
description: "T388 partial-trace statistic is FOBI (Cardoso 1989); exact noise variance 2d+12 gives n>2(d^2+6d)/kappa^2; Oja's 16x penalty was the step rule (about 4x with Jain's step)"
metadata:
  type: project
  created: 2026-11-04
  created_at: 2026-11-04T13:56:14+02:00
  status: verified
  evidence: "rank10_t388_check.json, rank10_t388_oja_check.json; board 8d53ab5"
---

T388 (top-400 list, spiked cumulant model) partial-trace and Oja push, research-repo ff4dc32f, reviewed 4 Nov 2026 by an agent with an independent sampler (board brain-tasks-board 8d53ab5).

- The "partial trace" M_n = (1/n) sum (|x|^2 - d - 2) x x^T is FOBI (Cardoso 1989) shifted by (d+2) I: same eigenvectors. Known algorithm; fixed-d theory in arXiv 1406.4765 and 1701.06836; high-d NGCA relative is Tan-Vershynin 1704.01041 (exp(-alpha|x|^2) reweighting, loose ~n^7 bound at r = 4).
- Sharp offline law (checked within 0.03 at d = 16/32/64, c >= 32): off-diagonal noise variance v = E[a^2 x_j^2 x_k^2] = 2d + 12 exactly (size-bias two Gaussian coordinates: |x|^2 becomes chi-square on d + 4 dof). BBP: weak recovery at n > 2(d^2+6d)/kappa^2, overlap^2 = 1 - 2(d^2+6d)/(kappa^2 n). No log factor for weak recovery.
- One-pass Oja: the source's 16x penalty over offline came from its constant step 2 log n/(|kappa| n); Jain et al.'s decaying step alpha/(gap (beta + t)) with alpha 2, beta = V/kappa^2 gives about 4x (d = 32). V = 2(d+2)^2 + 8(d+2).
- Jain et al. 1602.06929 Definition 1 allows indefinite A_i (only E A PSD) but needs ||A_i - Sigma|| <= M a.s.; for a x x^T one must truncate and bound the bias first.
- Lesson for reviewing a "probably known" spectral statistic: write it as a known estimator first (shifts by multiples of I do not change eigenvectors), then derive the noise variance exactly by size-biasing before trusting a quoted noise norm.

Row stays OPEN; no novelty endorsed (tensor-PCA partial trace and Diakonikolas-Kane NGCA literature unread). Review: brain repo 12_cognitive_architecture/top10_7_10_agent/rank10_T388_review.md.

Related (orphan link pass 4 Nov 2026): [[t388_partial_trace_finds_cumulant_spike_at_d2_2026_11_01]].
