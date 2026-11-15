---
name: nbbr_posted_referee_minor_v11_ratio_remark_threshold_fixed_2026_11_14
description: "[PROVISIONAL] Nonbacktracking birthday bound (bounded degree ratio) posted paper: is it sound? Referee 14 Nov (gpt-6.1-sol, Mac 1) MINOR, all proofs SOUND; v1.1 073bd2fd fixes rem:ratio, threshold, address"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T23:25:57+02:00
  status: provisional
  evidence: ""
---

Independent referee of yspennstate/nonbacktracking-birthday-irregular (Theorem 1.2: p_k <= min{1, 256 Q(1+Q) n/k^2}, Q=M/(m-1)). Verdict MINOR; plans, departures, reversal involution, transport multiplicity (at most L per target, no extra factor from excursion lengths), constant 256 and both corollaries SOUND; exhaustive plan enumeration on K4, prism, K3,3, wheels W5/W6 (1,696 plans, 1.3M configs) found no counterexample; sources (Dozier arXiv 2608.26321 Conj 1.5, BGJ26 Thms 1-3, Q4) quoted correctly; no prior proof of the bounded-ratio case found (Scholar blocked by a challenge page, so novelty rests on arXiv/web search). Fixes in v1.1 (main = tag v1.1 = 073bd2fd9cc9493b8a61c1a27d9d17552ff211e9): rem:ratio no longer says all three losses are order M (packing loss is through average degree; terminal and reversal can be order M); check_bound.py threshold floor(sqrt h)+1 (JSON 1386/4382/7839/12394, survivors unchanged, rest reproduced); script comments say Theorem 1.2; Einstein Institute address; code link to tree/v1.1. Report: 06_math_research/referee_reports/2026-11-14/NBBR_posted_referee/ (brain 4f4fde8f). Mac archive agent_run/nbbr_referee/NBBR_mac1.tgz sha 5dcaa85a. Zenodo new version handed to an agent. Related [[fa1f_posted_referee_minor_v11_numbering_and_sharpness_fixed_2026_11_14]].
