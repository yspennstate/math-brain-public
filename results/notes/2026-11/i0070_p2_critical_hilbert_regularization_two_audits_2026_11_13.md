---
name: i0070_p2_critical_hilbert_regularization_two_audits_2026_11_13
description: "Agresti-Veraar survey Problem 6 (p=2 critical time regularization, Hilbert X_0): yes under Thm 5.7's own (all-MR), no (5.21); two audits 13 Nov; paper staged"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T16:30:49+02:00
  status: verified
  evidence: "mini1 ~/agent_run/I0070A/REPORT.md PROVED, I0070AR/REPORT.md MINOR; ledger rows I0070 PROVED (two audits)"
---

Agresti-Veraar survey "Nonlinear SPDEs and maximal regularity" (NoDEA, DOI 10.1007/s00030-025-01090-2, arXiv:2501.18561v5), Problem 6 (published p. 130): does the instantaneous regularization of Theorem 5.7 extend to p = 2 in the critical case (equality in (6.1)) when X_0 is Hilbert?

Answer (two audits, 13 Nov: I0070A PROVED, independent referee I0070AR MINOR): yes, under the endpoint (p, kappa) = (2, 0) hypotheses of Theorem 4.7, (6.1) with equality allowed, and the higher-exponent unweighted stochastic maximal regularity that Theorem 5.7 already assumes (all-MR). The extra growth bound (5.21) is not needed. Local on (0, sigma); no gain at t = 0, no moment bound, no endpoint theta = 1/2.

Proof: at equality the trace exponent rho_j > 0 gives small relative growth of F, G on small X_{1/2}-balls about a domain vector, radius independent of its X_1 norm (same mechanism as the survey's (5.5), pp. 51-52 published); cutoff equations started at deterministic times where u is in X_1 have L^q time integrability by unweighted maximal regularity and global continuation; stopped comparison plus a countable cover of deterministic restart times reaches every positive time.

Referee fixes for the paper: Portal-Veraar Thm 5.3 on pp. 572-573; Agresti-Veraar Part I (arXiv 2001.00512v5) Thm 4.8 p. 31, Thm 4.7 pp. 30-31; credit (5.5). Not contradicted by Agresti-Veraar arXiv:2509.07803 (C. R. Math. 2026). Novelty plausible, not exhaustively established. Conditional on (all-MR): it does not derive higher maximal regularity from variational coercivity alone.

Status: paper run I0070P staged on worker machine 1 (repo planned critical-hilbert-time-regularization, claim topic:papers/I0070); reports archived in the brain repo. Same survey's Problem 7 queued as I0071A. Related: [[codex_launch_during_btc_heavy_phase_killed_stretch_lock_gate_added_2026_11_13]], [[paper_from_refereed_result_check_agent_paper_claims_first_2026_11_13]].

