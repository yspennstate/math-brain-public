---
name: kcm_planar_bounded_odds_posted_referee_sound_decrease_fixed_2026_11_14
description: "[PROVISIONAL] Is the posted KCM planar bounded-odds paper (stationary => detailed balance on Z^2, FA-1f/FA-2f = pi) sound? Yes, refereed 14 Nov: every proof re-derived, 12 DOIs and MST25 theorem numbers checked, code 40/40; fixed 'decrease'->'increase' in Prop 1.4 proof and Lemma 4.2 wording, pushed fc1c0b0"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T16:56:46+02:00
  status: provisional
  evidence: ""
---

Posted repo yspennstate/kcm-planar-stationary-bounded-odds (63e47fe -> fc1c0b0, 14 Nov). Report: 06_math_research/referee_reports/2026-11-14/KCM_posted_referee/REPORT.md. Pre-posting reports were D0028A (claim) and D0028AR (MINOR) on 13 Nov - search the referee folders by problem id D0028 before refereeing a posted paper. Scar: running code/finite_checks.py rewrites data/finite_checks.json with CRLF on Windows, so SHA256SUMS then fails; content equal after stripping CR. Fixed with newline='\n'. SHA256SUMS in our paper repos are sums of the LF git blobs (compute with git show :path | sha256sum when autocrlf is on). Related: [[derrida_retaux_moment_reduction_referee_sound_2026_11_14]] [[i0070_critical_hilbert_posted_referee_sources_checked_2026_11_14]]
