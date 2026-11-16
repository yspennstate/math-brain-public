---
name: fei_symmetric_all_n_restriction_k_4p8677_fsym32_2026_11_09
description: "Probably yes, unrefereed (FSYM32): symmetric f has Delta_1 <= K I_1, K=12-(9/2)log2 3=4.8677, every n, so H <= 4.8677 I; coupled zero-atom tangent closed the gap; reruns identical; FSYM36/37 + 54e83a7b pending"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T08:11:38+04:00
  status: provisional
  evidence: "workers/FSYM32 REPORT.md PROOF.md; rerun fsym32_check; the private brain repository: 46145a7c76"
---

Does the symmetric FEI bound reach the restriction constant 4.8677 in every dimension? Probably yes, computer-assisted, not yet refereed (FSYM32, 9 Nov 08:03). Delta_1 <= K I_1 with K = 12 - (9/2) log2 3 = 4.86767 bits for every symmetric Boolean f and every n, OR_3 attaining it, so H <= 4.8677 I by the restriction induction. That would replace C_sym = 6.1347 in paper v2.

The step that closed the gap: keep the zero atom on the same probability law instead of adding its worst case. With z = mu_0 and C = n - 1/6, L_0 <= z[3 + ln(1 - C z^2) - 2 ln z], which is concave, so a tangent at rational u (constant 2u/(1-Cu^2)) makes it linear in mu_0 and it joins the rational dual certificate with E_mu s >= N/2 and the e^{-v} I_0(v) envelope. Coverage: n <= 15 by the w06 exhaustive checker (131,068 tables, max exactly K at n = 3), n = 16..255 coefficient by coefficient (max 4.848905 at n = 25), five block certificates to 9999 (by monotonicity in n), FSYM04's large-n proof from 10^4 (4.866169).

Checked by an agent: all five scripts rerun from a copy, outputs identical except timing; finish.py fails only on a relative provenance path. I read PROOF.md line by line (tangent reindexing, zero-atom bound and its tangent constant, q(w)q(w+1) <= 0 for the mean, the peak bound, block monotonicity) and found no error. Pending: FSYM36 (hostile math referee), FSYM37 (code-independent recomputation), an agent's rerun. Files: the private brain repository: 06_math_research/frontier/T021/fsym_workers_2026_11_09/FSYM32 (46145a7c76). Paper v3 waits on those three.


Related: [[fei_symmetric_paper_v2_6p1347_level_bound_2p692_2026_11_09]] - this would replace its 6.1347. [[fei_symmetric_min_entropy_3p3975_fsym15_2026_11_09]] - same symmetric program, min-entropy side.
