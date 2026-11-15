---
name: smoothing_high_confidence_referee_closed_event_fixed_2026_11_14
description: "[VERIFIED] Is the posted randomized-smoothing paper (Gaussian optimal at every confidence) correct? Yes (14 Nov referee): one fix, Lemma 3.2 closed event, public 456b478"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T07:47:48+02:00
  status: provisional
  evidence: ""
---

Independent referee (an agent, T-20261112-017) of yspennstate/smoothing-high-confidence at 49e5e44: proofs correct, constants 7.952 and 1012 re-derived, checks rerun ALL PASS. Fix 456b478: Lemma 3.2 now states mu(X_s <= -T') (the theorem used the closed event and leaned on 'by the proof of the lemma'); fixed date. Novelty vs Blum et al. 2002.03517 (alpha^{-1/2}) and Yang et al. 2002.08118 (cotype, d-order only) holds at abstract level. Report: 06_math_research/referee_reports/2026-11-14/SHC_posted_referee. Lesson: a 'by the proof of Lemma X' patch for a strict-vs-closed event is a lemma stated one notch too weak; restate the lemma. Related: [[shuffled_ablq_referee_transition_exactly_z1_2_2026_11_14]] [[rr_constant_step_log_factor_referee_three_fixes_2026_11_14]]
