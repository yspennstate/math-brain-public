---
name: p0434_lemma_b_false_per_class_charges_die_under_atom_splitting_2026_11_08
description: "[VERIFIED] P0434 8 Nov 20:5x: lemma T_MS - T_G <= max_k p_k T_MS,k is false - split each atom of the 2u/(1+u) ray law into near copies: rest 1.56 at R 1.78 (float), 1.25 (50-digit); per-class charges must be split-invariant (by size level, not atom)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T20:51:39-05:00
  status: verified
  evidence: "codex_fleet/runs/own_p0434/rest_split.out, rest_split_float.out; NOTE.md 20:5x"
---

P0434 (Conj. 8.1, T_MS <= 2 T_G), 8 Nov 20:5x, an agent. The candidate lemma (b) R - max_k m_k <= 1 (m_k =
p_k T_MS,k / T_G, R = T_MS / T_G), the same as T_MS - T_G <= max_k p_k T_MS,k, is false. Split every atom into near
copies: the ratio barely moves, but max_k m_k falls by the split factor. On the 2u/(1+u) ray {1, 1+d, K}:
  50-digit soap_mp, K 401, each atom split in two: R 1.496569, max m 0.25001, rest 1.246559.
  float soap.py alone, t 2e-5, each atom split x4: K 26 rest 1.411305 (R 1.618871); K 101 rest 1.562455 (R 1.784315).
Conj. 8.1 itself is not touched (R < 2 throughout). Before this, (b) had held on every three-atom law tried, tight at
1 - 1/K on the ray (memory [[p0434_three_class_rest_reaches_0_992_on_the_lower_bound_ray_2026_11_08]]), because there
all the excess sits in one demoted class.

How to apply: a per-class (per-atom) charging lemma for this problem must be split-invariant. Near-equal atoms behave
as one group, so charge by size level or rank level, never by atom. Splitting test: before trusting a per-class bound
that holds on few-atom laws, split each atom into 2-4 near copies, keeping their order, and re-run. Scar inside the
check: the first float split moved a copy of the 1 atom above 1+d, which broke the law (R 1.65 -> 1.00), so keep copies
on their own side. Files: codex_fleet/runs/own_p0434/rest_split.py, rest_split_float.py (.out), soap_mp.py, NOTE.md
20:5x. Related: [[p0434_near_two_laws_are_twins_each_carrying_one_t_g_2026_11_08]],
[[p0434_suffix_netted_charge_fails_small_classes_gain_2026_11_08]].

