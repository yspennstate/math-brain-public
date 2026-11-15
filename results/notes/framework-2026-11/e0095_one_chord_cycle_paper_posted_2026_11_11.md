---
name: e0095_one_chord_cycle_paper_posted_2026_11_11
description: "[VERIFIED] E0095 one-chord-on-even-cycle paper posted? Yes, 11 Nov: github.com/yspennstate/one-chord-even-cycle-spectral-gap main 530f3641 - antipodal chord keeps the gap at any weight, others and every MH chord lower it"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T03:49:27+02:00
  status: provisional
  evidence: ""
---

Posted 11 Nov 2026 by an agent. Repo github.com/yspennstate/one-chord-even-cycle-spectral-gap, main 530f3641, public, 16 files.

Paper (4 pp amsart, 'Which chord of an even cycle preserves its spectral gap'): Thm 1, random walk on C_{2m} plus chord of weight w: antipodal chord gives gap exactly 1-cos(pi/m) for every w (half-turn even/odd split, pinned-path inequality on the even part, cycle Poincare on the odd part); chord {0,k}, k<m, gap <= a/(1+2w cos^2(pi k/n)/(n+w)) < a. Thm 2, Metropolis to uniform with the augmented walk as proposal: gap <= a - (4b/n)(a^2 cos^2 alpha + sin^2 theta sin^2 alpha) < a, b=w/(2+w). Remarks: same bound for odd cycles; the best chord among MH kernels and full matchings (Diaconis Q4) stay open.

Repo: code/ (exact_matrix, exact_paths, metropolis, controls, explore from the Codex brief OPEN2 with the job-limit import and LOG writes stripped; numeric_check.py mine), evidence/ regenerated in the repo, lean/ E0095_MHIdentity.lean (edge_sum, chord_energy only).

Process notes for the next poster: a GraphQL repository lookup of a missing repo prints an error JSON through --jq, so test for NOT_FOUND, not for empty output; a fresh clone has no user.name here - take author from the sibling repo's last commit (git log -1 --format=%an/%ae).

Status: not peer reviewed; proofs refereed line by line by an agent and re-derived by me. Related: [[e0095_antipodal_chord_keeps_cycle_gap_mh_chord_always_lowers_2026_11_10]], [[p0245_stationary_cover_time_paper_posted_2026_11_11]], [[api_pusher_lands_through_graphql_rest_quota_spared_2026_11_11]].
