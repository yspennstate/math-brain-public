---
name: fa1f_posted_referee_minor_v11_numbering_and_sharpness_fixed_2026_11_14
description: "[PROVISIONAL] Is the posted FA-1f single-infection relaxation paper (MST25 Conjectures 1-2 for q>1/2) sound? Referee 14 Nov (gpt-6.1-sol high): MINOR, Thm and Cor sound, finite speed alone justifies the replacement; fixed sharpness sentence, fixed-window wording, float-not-exact, two 2.3-SE points; conjectures were on the theorem counter (results printed as 1.3/1.4). v1.1 a1bb6eea"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T23:09:00+02:00
  status: provisional
  evidence: ""
---

Repo yspennstate/fa1f-relaxation-high-density, v1.0 adf9c91 -> v1.1 = main = a1bb6eeab6ef26bc6cee8aa5fdbdd36a68a6b407 (14 Nov), with the Einstein address. Report: 06_math_research/referee_reports/2026-11-14/FA1F_posted_referee/REPORT.md (brain commit 0ba32b38); Mac folder archive agent_run/fa1f_referee/FA1FR_mac1.tgz sha256 76d421cd..., 75 entries.

What the referee found: no gap in Theorem 1.1 or Corollary 1.2; BCMRT13 Thm 2.1 applies to the unconditional law of the modified configuration with constants uniform in nu (theta=sqrt(q/p), K=1+B); no prior proof of both conjectures for all q>1/2 found (Scholar blocked, so a search result, not priority). False as written: 'the bound is attained' after Lg<=-lambda g+b (equality is for the d>=1 part, Lg<=-lambda g); 'within two SE at all recorded times' (q=0.6 t=45 and q=0.75 t=70 at 2.3 SE, 30 of 32 within); 'checked exactly' (float, max slack 5.6e-17).

Scar: \newtheorem{conjecture}[theorem] puts quoted conjectures on the theorem counter, so 'Theorem 1.1' in README, abstract and memos silently prints as 1.3. Give quoted conjectures their own counter. Related: [[kcm_planar_bounded_odds_posted_referee_sound_decrease_fixed_2026_11_14]] [[p0167_slab_beats_ball_every_rho_paper_posted_referee_fixes_2026_11_14]]
