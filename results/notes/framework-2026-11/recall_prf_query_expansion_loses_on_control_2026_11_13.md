---
name: recall_prf_query_expansion_loses_on_control_2026_11_13
description: "[VERIFIED] Add pseudo-relevance feedback (PRF) terms to recall queries? No: end to end through the served CLI, b139 hit@8 32->33 but the 28 Oct control 82->79 (net -2); not shipped"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T03:57:19+02:00
  status: provisional
  evidence: ""
---

Pseudo-relevance feedback for brain.py recall (PRF 5,3,6: take the top 5 non-noise BM25 hits, keep terms found in at least 3 of their descriptions, append at most 6 new terms to the question) was tested end to end through the served CLI on 13 Nov 2026 (an agent, scratchpad prf_cli.py / prf_full.py, 498 rows, first 8 printed rows scored for gold).

Result: BVNB139 (gold = key reads) hit@8 32 -> 33 (won q010 q011 q071, lost q052 q084); the 28 Oct control (110 queries, gold = target) 82 -> 79 (won 0, lost 029 050 104). The ship bar was b139 up and the control flat. It fails it: net -2, and every control change is a loss.

Why it likely loses: recall already fuses BM25 with the association graph and semantic lanes, so the expansion terms mostly re-weight what the first hits already said (query drift toward the top-5 cluster) and push a correct but lexically different target out of the first 8. A one-hit gain on a 139-question bank is noise.

What would change it: a gated PRF (only when the question is short or the weak-match hint fires) tested on both banks; not tried. status: verified (two banks, one run each). Related: [[recall_speed_exact_fold_tail_collapse_2026_11_12]].
