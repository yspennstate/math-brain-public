---
name: near_regular_percolation_components_referee_sound_lp_section_fixed_2026_11_14
description: "[PROVISIONAL] near-regular-percolation-components (CMW Q5.2 near-regular case) refereed 14 Nov: all proofs re-derived sound; Paley-Zygmund cite LP16 5.1->5.5 fixed, fa9fa06"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T13:16:51+02:00
  status: provisional
  evidence: ""
---

Posted paper yspennstate/near-regular-percolation-components (answers the near-regular case of Christoph-Morawski-Wigderson arXiv:2608.19145 Question 5.2: O(log n) below (1-eps)(1+delta)=1, O((log n)^3) at it, n^c components above via clique+blown-up b-ary tree) refereed by an agent on 14 Nov 2026. Verdict SOUND; every lemma re-derived. One fix: Paley-Zygmund is Lyons-Peres Section 5.5, not 5.1 (the book's 5.3 points there); plus the missing star-with-clique slope 0.52 in Remark 6.2; commit fa9fa06, SHA256SUMS regenerated, clean LF clone passes 15/15. Slopes reproduce from trials.csv to 4 digits; an independent sim (nrpc_refs/indep_nrpc.py) matches lambda to 6 digits and medians within bands; verify.py PASS on worker machine 2 (it needs Unix: resource and os.getpriority). Lesson: a local clone made with core.autocrlf=true passed sha256sum -c too, so only the autocrlf=false clone counts as the checksum check. Report: 06_math_research/referee_reports/2026-11-14/NRPC_posted_referee/REPORT.md. Related: [[tridiagonal_edge_freezing_referee]] [[bridge_pattern_waiting_time_referee_sound_tab_ate_arrows_2026_11_14]]
