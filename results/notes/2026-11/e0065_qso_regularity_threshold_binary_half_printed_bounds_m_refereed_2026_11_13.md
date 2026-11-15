---
name: e0065_qso_regularity_threshold_binary_half_printed_bounds_m_refereed_2026_11_13
description: "[PROVISIONAL] QSO regularity threshold lambda_m (Ganikhodzhaev-Rozikov Problem 12): binary value is (3-sqrt7)/4, half the printed one; for m>=3 two-sided bounds with 2m lambda_m -> 1; refereed MINOR"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T07:46:28+02:00
  status: provisional
  evidence: ""
---

E0065, Problem 12 of Ganikhodzhaev-Rozikov 'Quadratic stochastic operators: results and open problems' (arXiv:0902.4207v2 Sec 9 p.7; Theorem 2.28/Problem 2.29 of the 2011 IDAQP version). Asks for the exact threshold lambda_m such that every QSO on the (m-1)-simplex with all heredity coefficients above lambda_m is regular.

Result (Codex run E0065A on mini1, referee E0065AR MINOR, 13 Nov 2026), status PARTIAL, two audits:
- m=2, under the survey's own normalization: lambda_2 = (3-sqrt 7)/4 = 0.0885622, half the printed value. Proof: fixed-point discriminant (2b-1)^2+4c(1-a), f(f(x))-x = (f(x)-x)H(x), explicit two-cycle of delta+(1-2delta)(1-x)^2 below the threshold.
- m>=3: (1-1/sqrt(m+1))/(2m) <= lambda_m <= 2/(3m+2+sqrt(m^2+12m+4)) < 1/(2m); so 2m lambda_m -> 1. Upper bound by contraction in the Fisher-Rao metric (|DW(x)h|_W(x)^2 <= 2|h|_x^2, improved by the coefficient floor); lower bound by explicit strictly positive operators with proper two-cycles.
- Still open: exact lambda_m for m>=3.
Referee caveats: cite Karim-Hamzah-Ganikhodjaev 2022 (binary classification, attributed to Lyubich 1974) and Saburov-Saburov 2025 (English Jan 2026; leaves the unrestricted threshold unknown). The 1988 source [17] was not read, so whether the factor 2 is a transcription error in the surveys is unsettled. Novelty not certified.
Files: brain archive 06_math_research/codex_runs (E0065A, E0065AR); row in probability_1000_intake_E_20260908/problems.jsonl.
