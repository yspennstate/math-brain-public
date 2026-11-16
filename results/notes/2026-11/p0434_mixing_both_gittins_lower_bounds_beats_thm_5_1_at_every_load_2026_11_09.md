---
name: p0434_mixing_both_gittins_lower_bounds_beats_thm_5_1_at_every_load_2026_11_09
description: "P0434 9 Nov 02:5x: using E[T_G] >= Q_G + E[X] and >= l E[X] together (convex mix, LP-exact) with the blended numerator bounds M-SERPT/Gittins below Scully Thm 5.1 at every load (3.855 vs 4.636 at rho 0.99); sup still 5"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T02:47:34-05:00
  status: provisional
  evidence: "blend_mix2.out: 3.855 vs 4.636 at rho 0.99, 4.530 vs 4.960 at 1-rho 1e-4; hand check at 0.01"
---

P0434, 9 Nov 02:5x (an agent). Theorem 5.1 of Scully et al. (arXiv 1907.10792) bounds the M-SERPT/Gittins mean response
time ratio by taking the better of two separate routes. Using both Gittins lower bounds at once does better at every load:
E[T_G] >= Q_G + E[X] (Prop. 4.9) and E[T_G] >= l E[X] (Wierman et al.), l = (1/rho) log(1/(1-rho)), so E[T_G] >= any convex mix.
With the blended numerator of [[p0434_blending_trivial_residence_bound_gives_ratio_two_below_rho_0_626_2026_11_09]],
   ratio <= min over theta, alpha of max((2-theta) c/alpha, (theta/(1-rho) + (1-theta) l)/(alpha + (1-alpha) l)),  c = 2/(1+sqrt(1-rho)),
which is the best those ingredients allow (LP duality). Values (blend_mix2.out): 2.901 at rho 8/9 (Thm 5.1: 3), 3.627 at 0.98
(3.992), 3.855 at 0.99 (4.636), 4.317 at 1-rho 1e-3 (4.877), 4.530 at 1e-4 (4.960), 4.782 at 1e-8 (5.000). At heavy load the
numerator is exactly Lemmas 5.6 + 5.7, so the gain comes only from the mix. The sup is still 5, approached like 5 - O(1/l) as alpha -> 4/5.
The <= 2 edge stays at rho 0.626. The heavy-traffic limit <= 2 for OR/MDA(Lambda)/Bounded laws is the published arXiv 2003.13232 Thm 3.2.
Files: ~/codex_fleet/runs/own_p0434 blend_mix.py, blend_mix2.py, NOTE.md 9 Nov 02:4x and 02:5x.


Addendum 9 Nov 02:5x: falsification test mix_check.py (2107 law/load cases, 1-rho 0.5 to 1e-4): every ingredient holds, R_G >= E[X] tight at 0, Wierman's bound within 0.026, true ratio at most 1.267 against the bound 4.530 at 1e-4.

Addendum 9 Nov 03:0x: the slack at mid load is in Lemma 5.6. The worker machine law has Q_MS/Q_G 0.97 at rho 0.5 to 0.9 and reaches 2 only past 1-rho 1e-4 (mm_q_by_load.out). With c replaced by 1 route A gives <= 2 up to rho 0.797 (l(rho) = 2), so a load-dependent waiting lemma is the lever on the 0.626 edge. A climb on Q_MS/Q_G stalls on the plateau of laws where both policies coincide; seed it off that plateau.

Addendum 9 Nov 03:1x (corrects the 03:0x hope): seeded off the plateau, the climb finds Q_MS/Q_G 1.147 at rho 0.7 (c 1.292) and 1.236 at rho 0.8 (c 1.382) on small ordinary laws (q_sup_mid.out). Route A reaches 2 at rho iff (2 - 2/c)(1/(1-rho) - l) <= 2 - l; at 0.7 that needs c <= 1.095, and at 0.8 l > 2 kills it for any c. So the best possible waiting lemma moves the edge only somewhere in (0.626, 0.7), not to 0.797; past 0.7 the residence side (Lemma 5.7 or the trivial bound) must improve too. q_sup_065.py measures rho 0.65.

Addendum 9 Nov 03:2x: the three-atom sup of Q_MS/Q_G is a twin-plus-vanishing-huge-job limit (twins merging, third atom size to infinity with a fixed share f ~ 1 - w of E[X]); checked smooth in K and gap (q_sup_3atom_check.out). It is 1.1845 at rho 0.65 (route A needs 1.1834) and 1.1797 at 0.64 (needs 1.2060). So even the exact waiting constant moves the ratio-2 edge only from 0.626 to between 0.64 and 0.65. The lever for mid load is the residence side, or a route that does not bound Q and R separately.

Addendum 9 Nov 03:3x: a better target than any split route: T_MS <= 2 (Q_G + E[X]) implies Conj. 8.1 through R_G >= E[X]. Measured kappa = sup T_MS/(Q_G + E[X]) is only 1.37, 1.42, 1.43, 1.54 at 1-rho 0.35, 0.3, 0.2, 0.1 (kappa_mid.out, climbs, lower bounds on the sup) - about 25 pct room where route A fails. It must tend to 2 in heavy traffic; check 1-rho 1e-2..1e-4 before trying to prove it.
Heavy traffic (kappa_ht.out): kappa 1.57, 1.61, 1.51 at 1-rho 1e-2, 1e-3, 1e-4; there kappa equals T_MS/T_G to about 1e-3, so the target reduces to the conjecture near rho = 1. Nothing above 1.61 at any load.

Addendum 9 Nov 04:0x (kappa_split.out): against D = Q_G + E[X], sup Q_MS/D + sup R_MS/D is 1.51, 1.69, 1.72, 1.59, 1.65, 1.75 at 1-rho 0.5, 0.35, 0.2, 0.1, 1e-2, 1e-3, so separate waiting and residence lemmas against D suffice at every measured load. Next candidate: Lemma 5.6 for waiting plus R_MS <= (2 - c(rho)) Q_G + 2 E[X].

Addendum 9 Nov 04:1x (resid_z.out): Lemma 5.6 plus (R) R_MS <= (2 - c) Q_G + 2 E[X] would prove Conj. 8.1; the climbed sup of (R_MS - 2E[X])/((2-c)Q_G) is -1.24, -0.43, 0.10, 0.47 at rho 0.5, 0.65, 0.8, 0.9 (needs <= 1) but 1.20 and 1.38 at 1-rho 1e-2, 1e-3. Up to rho 0.65 the search finds R_MS < 2 E[X] on every law. Short climbs only - pin with Nelder-Mead on twin + huge-job laws before trusting.

Addendum 9 Nov 04:5x: CORRECTION - "R_MS < 2E[X] on every law up to rho 0.65" and "sup R_MS/E[X] ~ ell" are wrong; they came from 3-4 atom searches. Near-exponential DFR laws reach 2.078 at rho 0.65 (limit 2.088). (R) with the Q_G term still holds there. See [[p0434_mserpt_residence_over_mean_passes_two_on_near_exponential_laws_2026_11_09]].

Addendum 9 Nov 05:0x: CORRECTION - the 04:1x pair "Lemma 5.6 + (R)" does not cover rho <= 0.9: (R) fails on 0.1 Exp(1) + 0.9 Exp(10) from about rho 0.83 (z 1.26 at 0.9). See [[p0434_residence_lemma_r_fails_on_hyperexponential_dfr_laws_2026_11_09]].
