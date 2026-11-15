---
name: p0434_three_class_rest_reaches_0_992_on_the_lower_bound_ray_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 20:2x: lemma (b) R - max m_k <= 1 nearly fails for three atoms: rest 0.99189 at K 401 on the 2u/(1+u) ray {1,1+d,K}; Nelder-Mead over three atoms never left R 1.16 since the ray needs t < (K-2-alpha)/(K-1)^2"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T20:26:12-05:00
  status: provisional
  evidence: "codex_fleet/runs/own_p0434/rest_ray_scan2.out, rest_ray_scan.out, rest_ray.out, maxR_three.out; NOTE.md 20:2x"
---

P0434 (Conj. 8.1, T_MS <= 2 T_G), 8 Nov 20:2x, an agent. The candidate lemma (b) R - max_k m_k <= 1 (m_k =
p_k T_MS,k / T_G, R = sum m_k) is free for two classes and can fail for three only where R > 1.5. Nelder-Mead over three
atoms (rest_three2.py, maxR_three.py, 14 starts) never got past R 1.1608, which looked like "three classes are safe".
They are not. The proved lower-bound ray {1, 1+d, K} (a = alpha t at 1+d, b = t at K, eps = 1-rho = gamma t, d = t^2)
reaches 2u/(1+u) -> 2 with three atoms, but only inside t < (K-2-alpha)/(K-1)^2: at alpha = K-2-1e-3, t = 1e-4 it gave
R 1.0001 at every K.

On the ray the 1+d class has g near 0 and carries m = R - 1, while the other two keep m about g. rest climbs with K and
alpha -> K-2: 0.611 / 0.719 / 0.820 / 0.909 at K 5/10/26/101 (alpha K-2.5, gamma u), and 0.99189 at K 401, alpha
0.99(K-2), gamma 0.1u, where all three m sit near 0.5 (rest_ray_scan2.py). So (b) is within 0.008 of failing, and may
fail at larger K or have sup exactly 1. Floats stop near K 401 (d 2.5e-11).

How to apply: a three-atom search that misses the light-load near-equal ray says nothing about three atoms. Seed from
the ray, not from random or Mac mini cuts. Next check: the t -> 0 class shares in closed form with the comparison policy
pi (T_G <= T_pi, so pi-shares bound m_k from below); if that rest passes 1, (b) is false. Files:
codex_fleet/runs/own_p0434/rest_ray*.py/.out, NOTE.md section 20:2x. Related:
[[p0434_mserpt_lower_bound_2u_over_1_plus_u_passed_a_second_audit_2026_11_08]],
[[p0434_near_two_laws_are_twins_each_carrying_one_t_g_2026_11_08]].


Update 8 Nov 20:3x (rest_pi_limit.py, 60-digit mpmath at t = 1e-24): with the comparison policy pi as denominator
(a lower bound on the Gittins shares, one factor for all classes), the best rest on the ray is exactly 1 - 1/K
(0.990099 at K 101 ... 0.999999 at K 1e6), at alpha -> K-2, gamma -> 1, m -> (1/2, 1/2, 1/2), R -> 3/2. So in the
limit (b) has sup 1 on this family and is not passed. Open: Gittins can beat pi (rest_G >= rest_pi), and finite t
moves the split (float t 5e-6 at K 401 gave rest_G 0.99189 against the limit pi value 0.98841 there).

Update 8 Nov 20:4x (soap_mp.py = SOAP in 50-digit mpmath, matches float soap.py to 2e-16; rest_mp_ray.py, 81 points,
K 101-1601): with TRUE Gittins every ray point has rest_G < 1 - 1/K (best 0.999165 at K 1601 vs 0.999375), rising to
1 - 1/K as t -> 0 at gamma 1. So (b) holds on the ray and is tight: sup 1, reached only as K -> infinity. Any proof of
(b) must be sharp on this family. soap_mp.py is the tool for any law with near-tied sizes below float precision.

Update 8 Nov 20:5x: (b) itself is false once atoms may be split into near copies (rest 1.56 at R 1.78); see
[[p0434_lemma_b_false_per_class_charges_die_under_atom_splitting_2026_11_08]]. The three-atom results above stand as
stated, but they only say something about three atoms.
