---
name: derrida_retaux_moment_reduction_referee_sound_2026_11_14
description: "[PROVISIONAL] derrida-retaux-moment-conjecture (q_n ~ A n^-b => geometric conditional limit, all moments; Conj 1 <=> Conj 3 under criticality) refereed 14 Nov: SOUND, citations match; numerics need tilted coords + mass renormalisation"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T10:12:24+02:00
  status: provisional
  evidence: ""
---

Paper yspennstate/derrida-retaux-moment-conjecture at bb0e790, refereed by an agent 14 Nov 2026. Verdict SOUND, no change; two optional one-liners (q_n>0 under criticality; index range in Lemma 3.1). Report: 06_math_research/referee_reports/2026-11-14/DRM_posted_referee/REPORT.md. Every CDHLS page and number (arXiv 1705.04787v2), CHS 2108.05610v1 Thm 1.2, Chen-Shi 2006.06140 Thm 1.1, HMP 1811.08749 Thm 1.9(iii), CDDHLS 1907.01601 Thms 1.1-1.2 checked against the PDFs. The implication Conj 1 => mean prediction is already CDHLS Section 6 (Lemmas 4-5) and the paper credits it. Exact check, m=2, P(X0=2)=1/5: n^2 q_n 4.25/4.05/4.02 at n=100/1000/3000, E[X]/q -> 2, E[X^2]/q -> 6, TV ~ 1/n. HOW TO COMPUTE THE DERRIDA-RETAUX RECURSION: plain floats double any total-mass error each step (M -> M^m) so renormalise every step; untilted truncation at K loses tilted mass and drifts the run subcritical within a few hundred steps; FFT convolution noise blows up too. Work in r_k = m^k P(X=k) with direct np.convolve, K >= 2n, renormalise mass: stable to n=3000 in seconds. G_n(m) still depends on K because E[m^X|X>0] grows like n.
