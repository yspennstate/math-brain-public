---
name: top200_dl_candidates_ten_of_thirteen_already_on_list_screen_first_2026_11_13
description: "New top-200 replacement candidates already on the list? 10 of 13 DL candidates were live rows (T226 T231 T301 T235 T265 T227 T306 T271 T447 T325): screen against list.jsonl before the literature check"
metadata:
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T20:28:14+02:00
  status: verified
  evidence: "screen_candidates.py on list.jsonl (464 ids) 13 Nov 20:2x; title hits read by hand; SCREEN_NOTE_1113b.md"
---

Replacement candidates for a top-200 list must be screened against the live list (screen_candidates.py on list.jsonl, then read each title hit) BEFORE the literature check, not after.

On 13 Nov I litchecked 18 deep-learning candidates, kept 13 and mapped them onto 13 BORDERLINE rows (REPLACEMENTS_1113b.tsv, pushed as 157). The screen run afterwards showed 10 of the 13 already live: edge of stability T226, leap complexity T231, depth 3 vs 4 T301, grokking T235, benign overfitting T265, catapult T227, diffusion sampler iteration complexity T306, neural collapse T271, uniform minimal width T447, in-context regression T325/T326. The candidates came from memory of "famous DL open problems", and the list was built from the same memory, so overlap is the default, not the exception. Free ones: deep ReLU convergence below NTK width (C06), deep matrix factorization implicit bias (C14), exact ReLU representation width-depth (C18).

Nothing was landed in the list; the 13 BORDERLINE rows stay live until each has a free, litchecked replacement. Files: 06_math_research/top200_vet_agent_2026_11_11/SCREEN_NOTE_1113b.md, REPLACEMENTS_1113b_SCREENED.tsv.

