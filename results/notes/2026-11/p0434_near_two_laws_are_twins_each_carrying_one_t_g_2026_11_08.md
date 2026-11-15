---
name: p0434_near_two_laws_are_twins_each_carrying_one_t_g_2026_11_08
description: "P0434 8 Nov 19:0x: near-2 laws = two near-tied twins each carrying about one T_G under M-SERPT (0.97-0.99) while the small classes fall from 0.99 to 0.004 of T_G; candidate cap max_k p_k T_MS,k <= T_G held over 9 weak starts"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T19:02:08-05:00
  status: provisional
  evidence: "codex_fleet/runs/own_p0434/per_class_table.out, class_cap_hunt.out"
---

P0434 (Conj. 8.1, T_MS <= 2 T_G), 8 Nov 19:0x, an agent. Class by class (g_k = p_k T_G,k / T_G, m_k = p_k
T_MS,k / T_G), the laws near 2 all look the same. The small classes hold about 0.99 of T_G under Gittins and about
0.004 under M-SERPT. Two near-tied twin classes (sizes 2.1909 and 2.1943 on the Mac mini law; 2.1300 and 2.1302 on the
polished 1.985 law) hold about 0.009 under Gittins and 0.97-0.99 EACH under M-SERPT. So the factor 2 is two twins,
each absorbing about one whole T_G.

Candidate lemma (open): max_k p_k T_MS,k <= T_G. A Nelder-Mead hunt (class_cap_hunt.py, 9 starts, m 3-5) found
nothing above 1.00000; every run went to a one-class corner where m_k = R = 1. That is a weak search, not a bound.
Charging each loser against its own g_k plus all the gains below it fails slightly (1.010 at 1-rho 1e-7, 1.002 on the
polished law), and the two twins draw on the same gains.

How to apply: to attack 8.1, try (a) the cap m_k <= 1 and (b) "at most two classes near the cap at once". Search for
a breaker of (a) starting from twin laws rather than random starts, since random starts collapse to the trivial
corner. Files: codex_fleet/runs/own_p0434/per_class_table.py/.out, class_cap_hunt.py/.out, NOTE.md section 19:0x.
Related: [[p0434_suffix_netted_charge_fails_small_classes_gain_2026_11_08]], [[p0434_mserpt_jump_is_the_twin_rank_crossing_its_held_max_2026_11_08]], [[p0434_gross_loss_lemma_is_false_mac_mini_law_1_95_2026_11_08]].


Addendum 19:1x (twin_cap_hunt2.py): starting from the twin laws, the cap still held (best single-class m_k 0.99827).
There is a second shape near 2: the small classes KEEP their Gittins share (m about 0.98 in total) and one twin sits
near the cap on top (three-twin optimum R 1.980442, max-m_3 optimum R 1.9763). Scar: dropping the far atom (p 2.2e-9 at
s 17259) turns R from 1.966801 into 1.000000; that near-massless atom drives M-SERPT's ranks, so never prune it as
negligible (twin_cap_hunt.py made this mistake).

Addendum 19:3x (second): Conj. 8.1 = (a) max_k m_k <= 1 plus (b) R - max_k m_k <= 1. (b) under a direct Nelder-Mead from three
near-2 laws (rest_hunt2.py) stayed below 1 in every round, best 1 - 2.3e-7 at 1-rho 1.5e-8 (the search floor): its sup
looks like 1, reached only in heavy traffic. Each half is tight where the other is slack. Weak search, not a bound.

Addendum 19:5x: (b) is T_MS <= T_G + max_k p_k T_MS,k, which is stronger than 8.1. It is tight trivially (R = 1 with n
equal classes gives rest = 1 - 1/n, the corner a fixed-load search falls into, rest_trace.py) and also at R 1.35-1.98.
To measure anything, exclude the trivial corner with a floor on R.
