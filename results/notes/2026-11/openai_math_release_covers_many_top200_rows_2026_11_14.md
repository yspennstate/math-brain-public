---
name: openai_math_release_covers_many_top200_rows_2026_11_14
description: "Top-200 row still open? First check github.com/openai/math preprints (751, Sep-Oct 2026, unrefereed): 32 rows match strongly, T001 already retired"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T18:56:40+02:00
  status: provisional
  evidence: ""
---

Checking whether a top-200 open problem is still open? First look in the OpenAI math release, github.com/openai/math, folder preprints/: 751 AI-written preprints dated 10 Sep - 6 Oct 2026, unrefereed, many with Lean files under lean/. On 14 Nov 2026 a title match against our 471 rows (fillq_ctl/codex_op_1114/oai/match.py, MATCH.tsv) put 32 rows above score 35, among them T136 (SK low-temperature fluctuations), T050 and T095 (FPP limit shape), T063 (six-vertex GFF), T054 (random regular graph bulk universality), T137 (diluted Parisi formula), T304 (log-concave sampling queries), T214 (Ising factor of IID), T010 and T009 (Anderson localisation / extended states), T189 (FPRAS for perfect matchings), T123, T032 (BEC), T078 (Heisenberg ferromagnet), T083, T129, T013. Earlier the same week T001 (theta(p_c)=0) was retired on the release's 'Critical bond and site percolation on the cubic lattice'. Codex workers on Mac mini 1 found the release four times in their first five reports (T050, T056 fixed price, T060 Haldane gap, T001), while our where-it-stands notes, written in Oct-Nov, did not mention it.

How to apply: before attacking or keeping a row, read the matching preprint's main theorem and compare it with the row's statement word by word (dimension, model, strength); a match is a claim, not a solution, until an exposition, arXiv version or referee says so. The 32 verification briefs AV_<ID> run on mini1 (~/codex_op_1114/briefs/AV_*/VERIFY.md, REPORT.md); their verdicts come home through fillq_ctl/codex_op_1114/pull_op.sh. A title match misses rows whose wording differs (score under 35 is not checked yet).


Outcome, 14 Nov 2026 19:5x JST (an agent, pushes 250-254, last e3fea06c): 13 rows retired as claimed solved - T001 T013 T022 T031 T063 T078 T115 T123 T129 T189 T214 T425 by release preprints, T137 by Panchenko's own arXiv:2610.39545 (sole author, checked on arXiv) plus the release's even-K part. 11 rows keep a partial-claim sentence in where-it-stands: T010 T030 T032 T050 T054 T083 T095 T132 T136 T176 T304. NOT-THIS: T045 T046 T049 T120 T144 T163 T170 T190 T285. Log: top200_vet_agent_2026_11_11/STATUS_1114.tsv. The 13 retired rows still need replacement rows screened.
