---
name: fei_star_family_ratio_tends_to_ln3_proved_2026_11_08
description: "FEI star family [n11>=1,n00<=T] or [n00>=U]: R/I -> ln 3 proved (19k-19n) (per-coordinate scale, not the H/I boundary scale)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:03:38+02:00
  status: verified
  evidence: "fei_loop_agent/ratio_limit.py runs/ratio_limit.json wd_bound.py; commits dac4a1de 4ae20203"
---

The FEI loop's orbit-climb closed form f = [n11>=1 and n00<=T] or [n00>=U] on s pairs, with T ~ 0.609090 s and U ~ 0.705074 s,
has a pair-coordinate ratio R_f/I_f that tends to ln 3. This is proved, not only measured. The OR core g = [n11>=1] has
|ghat(S)|^2 = 4 (9/16)^t0 (1/16)^(t1+t2), so its R_g/I_g = ln 3 exactly. The three lemmas:
- 19k tie lemma: T_tie <= 4 sqrt(I_f W_d).
- 19m: W_d/I_f <= 8 (4/3)^(s-1) Pr[Bin(s,1/4) >= T+1]/q ~ 6.24 r^theta/sqrt(s), r = 0.21393.
- 19n: K(p^2,q^2) is 2 max(p,q)-Lipschitz, so R_f/I_f = ln 3 + O(s^-1/4).
Measured R_f/I_f - ln 3 is 0.092 at s=100 and 0.048 at s=800 (T = floor). The proved bounds hold but are loose, about
15x for the tie lemma and 70x for the Lipschitz step.

**Why:** the finite-s edge of that family is a small-s effect. R/I here is the per-coordinate R_k/I_k in nats, not the
whole-function H/I boundary score where PM(K33) holds 6.521845711, so the two are not comparable; on its own scale ln 3 is no ceiling (G(c,1) reaches (c/2)ln3+ln4). Threshold perturbations of the OR core keep its 9:1:1 ratios, so the limit stays ln 3.

**How to apply:** do not spend more FEI loop time on threshold perturbations of [n11>=1]. A family that beats ln 3 in
the limit needs a different core. Note: fei_loop_agent/fei_star_family_note.md. Commits on
the private brain repository: c540ad69 (19l), dac4a1de (19m), 4ae20203 (19n). Related: [[fei_r72_full_tabu_search_no_gain_over_pmk33_2026_11_08]]

