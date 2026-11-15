---
name: p0434_mserpt_residence_excess_beats_gittins_waiting_at_light_load_2026_11_09
description: "[PROVISIONAL] P0434 9 Nov 02:0x: R_MS-R_G<=Q_G fails at light load (1.137, Mac m11 law) but only by O(rho) R_G; R_MS<=2R_G+Q_G holds on all tests, which with Lemma 5.6 would give a 3-approx (published 5)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T02:01:45-05:00
  status: provisional
  evidence: "own_p0434/res_light.out, res_beta.out (simulated)"
---

P0434 (M-SERPT vs Gittins), 9 Nov 01:4x-02:0x, an agent. All numbers simulated with soap.py/split.py (exact SOAP formulas, no closed form).

Audit first: the waiting bound E[Q_MS] < 2 E[Q_G] proved 01:0x-01:1x is the published Lemma 5.6 of Scully et al. (arXiv 1907.10792). A Gittins block is a valley, so that work is a second proof only ([[p0434_levels_on_a_gittins_block_wait_under_twice_by_record_telescoping_2026_11_09]]).

Residence. res_light.py at rho 1e-3, 1e-4, 1e-5 (settled) gives (R_MS-R_G)/Q_G = 0.772 (yitz8 m6 law), 0.878 (res_excess climb law) and 1.137 (Mac mini m11 law). So the lemma R_MS-R_G <= Q_G, which would give T_MS <= 3T_G directly, is false, like L+ <= Q_G ([[p0434_light_load_l_plus_over_q_g_passes_one_so_that_lemma_is_false_2026_11_08]]). The excess over Q_G is beta*R_G with beta = O(rho): +2.4e-5 at rho 1e-3.

res_beta.py, 3600 random law-loads: max beta -0.169; a climb on beta reaches -0.008. On the Mac mini in heavy traffic R_MS/R_G is 3.07, so R_MS <= 2R_G alone fails, but beta is -7189 there.

Candidate lemma: R_MS <= 2R_G + Q_G. It holds with room on every test. With Lemma 5.6 it gives T_MS <= 3T_G, against the published 5. Not proved.

Files: ~/codex_fleet/runs/own_p0434/res_excess, res_light, res_beta (.py/.out); NOTE.md sections 9 Nov 01:4x and 02:0x.

Scar: check any P0434 bound against NOTE's 8 Nov 23:56 list of published lemmas before calling it new.

