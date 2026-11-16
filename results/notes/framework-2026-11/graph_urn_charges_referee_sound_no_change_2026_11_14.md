---
name: graph_urn_charges_referee_sound_no_change_2026_11_14
description: "[VERIFIED] graph-urn-conserved-charges (P0081 WARM alpha=1 charges, posted 69ce6d0) refereed 14 Nov: every proof checked, C4 density/Var p/tail recomputed, fresh-seed sims within 1.5 s.e.; no change needed"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T08:12:48+02:00
  status: provisional
  evidence: ""
---

Referee of yspennstate/graph-urn-conserved-charges at 69ce6d0 by an agent, 14 Nov 2026. Report: the private repository, 06_math_research/referee_reports/2026-11-14/GU_posted_referee/REPORT.md (commit in gu_push.log).

Verdict SOUND, no edit. Checked: Thm 1 charge martingale and bracket bound; Lemma 2 growth (S_v <= d + clocks of v and neighbours); Thm 3 terminal law via the Gamma-ratio martingale P_theta (generator i theta P sum (B sigma)_v/S_v = 0, |Gamma(x+iy)| <= Gamma(x)), Var <M>_inf = zeta(4) sum sigma^4 via R = [M] - <M>; Remark 4 fibre bijection; Lemma 5 equilibria on C_L (even blocks s = (2k+2)/(k+2), d_e L >= 1/(2k+2)); Thm 5 convergence (K forward invariant since dS_v/dtau >= 1 - S_v, Ben99 Prop 6.4, type-(2) exclusion by internal time, endpoints by Phi -> +-inf); Cor 6 pi^4/(90L); Prop 7 c = zeta(2) by the translation shift.

Recomputed: C4 density = logistic*logistic to 10 digits, E M^2 = 4 pi^2/6, Var p = pi^2/32 - 1/4 to 10 digits, tail density / 4(1-p)log(1/(1-p)) -> 1 like 1 - 1/log(1/(1-p)). Sims with new seeds: C4 Var 6.51 (exact 6.58, se 0.065), C50 79.5 (exact 82.25, se 1.8), KS inside 5 pct; truncation at K rings costs only ~sum 1/N_e.

Status: verified (independent second audit after the Codex pre-post review referee_reports/2026-11-12/P0081). What would change it: a fault in Ben99 Prop 6.4's hypotheses on the boundary of K, which I checked but did not re-derive from Benaim's text. Funding block follows [[funding_statement_names_google_cloud_edu_credit_2026_09_20]].
