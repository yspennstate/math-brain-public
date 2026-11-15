---
name: p0434_gross_loss_stays_under_gittins_time_and_is_tight_2026_11_08
description: "P0434 8 Nov 13:5x: gross loss sum_k max(0,T_MS,k-T_G,k) <= 0.068 T_G on 384 laws and -> 1 from below on the tie family (ratio 1.9886) - 'loss <= T_G' is a class-separable lemma implying Conj 8.1"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:57:53-05:00
  status: provisional
  evidence: ""
superseded_by: p0434_light_load_lplus_over_qg_passes_1_at_m11_two_job_check_2026_11_09
---

P0434 (M-SERPT against Gittins, M/G/1), 8 Nov 13:5x, an agent.

Gross loss L+ = sum_k max(0, T_MS,k - T_G,k): the mass-weighted loss of the classes M-SERPT slows, with no class's gain netted against it. Since T_MS <= T_G + L+, the lemma "L+ <= T_G" implies Conj. 8.1 (T_MS <= 2 T_G).

Measured: L+/T_G <= 0.068 on 384 sampled hunt laws (random, near-twin, huge_tiny, tiny_heavy; m 3-6, K 3-1000, rho 0.5-0.999; stall_loss.py). Against R_G alone it reaches 4.82, so the loss has to be charged to T_G with Q_G included. On the tie family (n 16, ratio 1e4; stall_tie_grid.py, stall_tie_hi.py, stall_tie_xt.py) L+/T_G rises toward 1 from below: 0.53 at a 0.9, 0.82 at 0.98, 0.977 at 0.999, 0.989 at a 0.9999 with rho 1-1e-6. There the whole T_MS/T_G = 1 + L+/T_G (1.9886) because the large classes gain nothing. So the lemma is exactly as tight as the conjecture on its worst family and splits by class.

The mechanism (near111.py): every positive excess seen is a stall. A job that has outlived a class boundary with little work left has an M-SERPT rank above the fresh rank, so it waits out busy periods of fresh work, while its Gittins rank is near 0. One class ran 111x slower that way.

Not proved. The laws were sampled, and precision at rho 1-1e-6 is unchecked at larger n. Files are in ~/codex_fleet/runs/own_p0434 (+ .out) and the NOTE.md sections 13:5x. Related: [[p0434_no_cut_or_class_local_charge_one_class_can_be_111x_slower_2026_11_08]], [[p0434_least_beta_is_at_least_0_0677_once_a_passes_one_half_2026_11_08]], [[p0434_mserpt_lower_bound_2u_over_1_plus_u_passed_a_second_audit_2026_11_08]].

Superseded 9 Nov 03:1x (an agent): the lemma L+ <= T_G is false. Near critical load, laws whose far atom carries more load than 1 - rho give L+/T_G = 1.950217761 (5 atoms, 1 - rho 1e-6) and 1.994571372 (6 atoms, 1e-9), exact with an agent's soap_indep.py. The sampled laws here never had that shape. superseded_by: [[p0434_light_load_lplus_over_qg_passes_1_at_m11_two_job_check_2026_11_09]]
