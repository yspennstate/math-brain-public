---
name: p0434_residence_lemma_r_fails_on_hyperexponential_dfr_laws_2026_11_09
description: "[VERIFIED] P0434 9 Nov 05:0x: residence lemma (R) R_MS<=(2-c)Q_G+2E[X] is FALSE - 0.1Exp(1)+0.9Exp(10) gives z 1.15 at rho .85, 1.26 at .9 (closed-form FB, two integrators, 4000-atom check); waiting and residence must be bounded together; few-atom and coarse-soap checks missed it"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:08:42-05:00
  status: verified
  evidence: "codex_fleet/runs/own_p0434/resid_fb_exp.out resid_fb_hyper.out resid_fb_check.out"
---

P0434 (Scully et al. Conj. 8.1, M-SERPT vs Gittins), 9 Nov 05:0x EST, an agent, ~/codex_fleet/runs/own_p0434.

The proposed residence lemma (R) R_MS <= (2-c) Q_G + 2E[X], c = 2/(1+sqrt(1-rho)), meant to pair with Lemma 5.6
(Q_MS <= c Q_G), is FALSE. On DFR laws M-SERPT = Gittins = FB, so everything is closed form (FB waiting lambda m2/(2(1-rho_x)^2),
residence x/(1-rho_x)). On 0.1 Exp(1) + 0.9 Exp(10), z = (R_MS - 2E[X])/((2-c)Q_G) is 1.146 at rho 0.85 and 1.262 at 0.9
(quad and a 400k-point trapezoid agree; the soap-verified atom closed form on 4000 atoms gives z about 1.04 / 1.15 and
still rising). Check passed: on the exponential, FB Q + R = 1/(1-rho) exactly at every load.

The conjecture holds trivially there (T_MS = T_G); what fails is splitting the proof into a waiting lemma and a residence
lemma, because Lemma 5.6's slack (c-1)Q_G is wasted where Q_MS = Q_G. The joint target T_MS <= 2(Q_G + E[X]) still has
room (kappa <= 1.61 measured).

Scar: (R) "holds for rho <= 0.9" came from 3-4 atom random climbs. Soap on 80 atoms also said z = 0.43 because its cell
(0.15) was wider than the fast phase's mean (0.1). Residence sups live on many-atom DFR shapes; test candidate lemmas on
hyperexponentials in closed form before any atom search.

How to apply: bound waiting and residence together, not as two lemmas. Related: [[p0434_mserpt_residence_over_mean_passes_two_on_near_exponential_laws_2026_11_09]], [[p0434_mixing_both_gittins_lower_bounds_beats_thm_5_1_at_every_load_2026_11_09]].

