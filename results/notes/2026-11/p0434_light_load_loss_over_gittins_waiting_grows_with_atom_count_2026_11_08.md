---
name: p0434_light_load_loss_over_gittins_waiting_grows_with_atom_count_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 15:0x: light-load limit of L+/Q_G is 0.508/0.691/0.766 for 3/4/5 atoms (seeded search; random starts miss it), steps shrinking; huge tiny atoms; decides if L+<=Q_G can be the lemma"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:01:34-05:00
  status: provisional
  evidence: "own_p0434/adv_lowload5s.out, adv_lowload5s_round.out"
---

P0434 (M-SERPT vs Gittins, Conj. 8.1 T_MS <= 2 T_G). The gross loss L+ = sum_k max(0, T_MS,k - T_G,k) and the Gittins waiting Q_G are both O(rho) at light load, so L+/Q_G has a rho -> 0 limit. Its sup over m-atom laws, found by Nelder-Mead at rho 1e-4 and settled at rho 1e-3 and 1e-5:

- m 3: 0.508
- m 4: 0.691
- m 5: 0.766. This is a search seeded at the m 4 optimum; from random starts it found only 0.168. A 1% nudge reaches 0.7705, so the search is not converged.

At light load the loss is all residence, and L+/T_G is about 3e-5 there. The m 5 optimum is s = (1, 1.0535, 2.1831, 1923, 4657), p = (0.154, 0.292, 0.553, 1.8e-4, 7.3e-5), so the extra atoms are huge with tiny mass. Re-entered rounded to 4 significant figures, it still gives 0.7664. One side of it is a rank-tie edge: atom 1 up 1% drops the value to 0.054.

The steps shrink (0.18, then 0.08). Whether sup over m stays below 1 decides whether the stronger "L+ <= Q_G" can serve as the lemma. "L+ <= T_G" is safe at light load because T_G -> E[S].

How to apply:
- Seed a larger-m search from the previous optimum. Random starts under-search because the good region is a thin rank-tie edge.
- Re-enter every optimum rounded before believing it (see [[p0434_gross_loss_stays_under_gittins_time_and_is_tight_2026_11_08]]).

Files are in ~/codex_fleet/runs/own_p0434: adv_lowload.py/.out, adv_lowload5.py/.out, adv_lowload5s.py/.out, adv_lowload5s_round.py/.out, and NOTE.md 14:3x-15:0x. They are pushed to yspennstate/research-repo.

Update 15:3x (Mac mini an agent, adv_lowload_mac.out at 6e114816, seeded chain, settled at rho 1e-3 and 1e-5): m 6 0.772, m 7 0.829, m 8 0.854, m 9 0.891. The shrinking steps up to m 6 were misleading, and my 15:1x guess that it levels near 0.78 was wrong: the curve still rises about 0.03 per atom past m 6. The m 7-9 optima carry near-coincident atom pairs (twin atoms 2e-8 apart, mass 1e-7), so they needed a merge-and-round check (adv_lowload_mac_round.py, 15:4x, run here): the twins carry nothing, merged laws keep 0.8291 with 6 atoms and 0.8538 with 7, so the sup is at least 0.829 at m 6 and 0.854 at m 7; m 9 rounded to 4 figures keeps 0.8913; a 1e-3 size move drops it to about 0.1 on one side (one-sided rank-tie edge). The Mac reports m 10 at 0.9295. The Mac runs m 10-16 (adv_lowload_mac_ext.py); if it crosses 1, "L+ <= Q_G" is false and "L+ <= T_G" is the form to prove.
