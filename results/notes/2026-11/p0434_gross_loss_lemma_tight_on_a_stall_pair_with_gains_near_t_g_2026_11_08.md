---
name: p0434_gross_loss_lemma_tight_on_a_stall_pair_with_gains_near_t_g_2026_11_08
description: "P0434 8 Nov 17:5x: L+ <= T_G is tight at both ends: tie family (R->2, no gains) and a stall pair {1,2.0076,3.316} with R=1.00000, G-/T_G=L+/T_G=0.9919; mixes stay <= 0.9917; sampled G-/T_G<=0.0079 was not the sup"
metadata:
  node_type: memory
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T17:58:34-05:00
  status: superseded
  superseded_by: p0434_gross_loss_lemma_is_false_mac_mini_law_1_95_2026_11_08
  evidence: research-repo b3284d09 own_p0434/lplus_hunt2.out lplus_mix.out
  modified: 2026-11-08T23:16:01.400Z
---

P0434 (M-SERPT vs Gittins, Conj. 8.1 T_MS <= 2 T_G), 8 Nov 17:5x, an agent. The gross-loss lemma
L+ <= T_G (which implies the conjecture) is tight on a second, unlike family, so it has no slack at either end.

The family is a stall pair: {1, 2.0076, 3.316}, p (0.9925, 0.0075, 7e-10), 1-rho 2.9e-6. There L+/T_G = 0.99185,
G-/T_G = 0.99185 and R = T_MS/T_G = 1.00000. Gittins runs it near FCFS: serving to completion at age 0 (rank
1.0075) just beats serving to age 1, so each class has T_G,k about 1.74e5. M-SERPT gives size 1 priority (T 66.8).
The size-2 survivors stall behind fresh work (T 2.3e7), because the tiny third atom lifts their remaining mean
above the fresh rank.

Against the tie family (R -> 2, G- -> 0), this one has R -> 1 and G-/T_G -> 1. Since L+/T_G = R - 1 + G-/T_G
exactly, a mix of the two could have broken the lemma while the conjecture held. lplus_mix.py added one or two
atoms to the pair from 10 starts: the best was 0.99172, nothing went above 1, and every polished law fell back
into one of the two families.

Measured with Nelder-Mead on L+/T_G and on G-/T_G (lplus_hunt.py, 24 starts, m 3-5; lplus_hunt2.py; lplus_mix.py),
all in codex_fleet/runs/own_p0434, NOTE.md section 17:5x, pushed to research-repo b3284d09.

Scar: random sampling (384 laws) had put G-/T_G at most 0.0079. Optimising the quantity itself found 0.99 within
two polishing rounds. A sampled sup is not a sup.

How to apply: a proof of L+ <= T_G cannot bound the gains G- by a small multiple of T_G. It has to use the trade
itself: a class can lose only what another class's Gittins time pays for.

Related: [[p0434_gross_loss_stays_under_gittins_time_and_is_tight_2026_11_08]], [[p0434_fixed_law_heavy_traffic_ratio_tends_to_one_2026_11_08]], [[p0434_no_cut_or_class_local_charge_one_class_can_be_111x_slower_2026_11_08]].


SUPERSEDED 8 Nov 18:0x: the stall pair and the 0.9917 search are real, but "the lemma survives" is wrong. L+ <= T_G is false (worker-machine 5-atom law, L+/T_G 1.950217761, checked with split.py): [[p0434_gross_loss_lemma_is_false_mac_mini_law_1_95_2026_11_08]].
