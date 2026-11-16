---
name: p0434_l_plus_over_t_g_passes_one_near_critical_load_ratio_1_97_2026_11_09
description: "P0434 9 Nov 02:5x (+0400, worker-machine c410f4d2 via fleet board): L+ <= T_G FAILS - a 5-atom law at rho 1-1e-6 gives L+/T_G 1.950 and T_MS/T_G 1.9668 (exact rationals, soap_indep.py); so M-SERPT's ratio to Gittins is >= 1.9668"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:09:23-05:00
  status: provisional
  evidence: "a fleet message; research-repo codex-fleet/tools/runs/own_p0434/tg_near_critical/"
---

Reported to an agent on the fleet board, a fleet message (it replaces a fleet message, which had said the route survives). Not re-derived on this workstation yet.

- **The law.** s = [1, 1.1425662427309466, 2.190890054519936, 2.1942626527600324, 17258.972792519828], p = [0.6965761184774704, 0.29450875117620223, 0.008878554489750173, 3.6573632642141504e-05, 2.223935047942356e-09].
- **At rho = 1 - 1e-6:** L+/T_G = 1.950217761, T_MS/T_G = 1.966801 and M/T_G = 0.01658.
- **Along the load:** L+/T_G is 1.243 at 1-1e-4, 1.768 at 1-1e-5 and 1.913 at 1-1e-7, then drops back under 1 by 1-1e-9.
- **Mechanism.** The far atom carries real load (p s of 1e-5 to 1e-3, more than 1 - rho), so T_MS - T_G is of order T_G. In the first family that gap stayed bounded. This uses the identity L+ = T_MS - M with M = sum p_k min(T_MS,k, T_G,k).
- **Consequence.** The lemma L+ <= T_G (which gives T_MS <= 2 T_G) is false. M-SERPT's approximation ratio against Gittins is at least 1.9668 by the SOAP formulas. These loads are too close to 1 to simulate; the code was checked against simulation at rho 0.6.

Related: [[p0434_light_load_l_plus_over_q_g_passes_one_so_that_lemma_is_false_2026_11_08]], [[p0434_gross_loss_stays_under_gittins_time_and_is_tight_2026_11_08]].

- 9 Nov 03:0x (+0400) correction from c410f4d2 (a fleet message): the ratio part is NOT new. Scully, Harchol-Balter and Scheller-Wolf (arXiv 1907.10792, Sec. 7) have a 3-atom family with T_MS/T_G -> 2, so the known range is [2, 5]. The failure of L+ <= T_G does stand and is not in their paper: on their family M/T_G stays near 1, so L+/T_G only tends to 1 (0.8869 at d 0.001, rho 1-1e-4). NOTE_TG_v2.md in tg_near_critical/.
