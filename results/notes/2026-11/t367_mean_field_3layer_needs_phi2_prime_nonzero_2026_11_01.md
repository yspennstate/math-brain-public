---
name: t367_mean_field_3layer_needs_phi2_prime_nonzero_2026_11_01
description: [PROVISIONAL] T367: i.i.d. init + constant w3 collapses the middle layer; a phi2 with a critical point traps the 3-layer MF flow at loss 0.49 > 0; noise tau<=0.1 does not help
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T23:42:11+04:00
  status: provisional
  evidence: ""
---



T367 (global convergence of three-layer mean-field nets with iid init), 1 Nov. Took target 2 after agent's target 1. The arXiv search found no multilayer mean-field Langevin result for the neuronal-embedding model; Hu-Kazeykina-Ren treat depth as control, which is a different object.

Result: Pham-Nguyen's Assumption 1 needs phi2' non-zero everywhere (TeX line 279), and that clause cannot be dropped. With constant untrained w3 and zero-mean independent w2, all middle units share one H2 at all times. For one data point, H then obeys a scalar ODE that cannot cross a zero of phi2'.

A bounded bump activation with local max 2.0099 < y = 3 keeps the loss >= 0.490 forever, which is rigorous. Langevin noise at tau 0.01 and 0.1 stays stuck, measured. Trained w3 or a monotone phi2 converge.

Lesson: before building a counterexample, read the theorem's regularity clause in the TeX. The "obvious" counterexample was excluded by a line that the 18 Oct summary did not quote.

Pushed 007028b (research_pushes/2026-11-01-loop-T367-phi2-critical-point); card claim_b43ec1e19bcf4f4082370e322b639ff0 (3 links); frontier move.

Related: [[t390_score_matching_weight_are_closed_form_2026_11_01]] and [[t388_partial_trace_finds_cumulant_spike_at_d2_2026_11_01]] are the same night's take-target-2-after-agent rows; [[t274_mean_field_ticket_lags_rescaled_random_subnet_matches_full_2026_11_01]] covers mean-field exchangeability.
