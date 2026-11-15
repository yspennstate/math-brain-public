---
name: t104_top_eigenvector_dual_state_fails_2026_11_12
description: "T104 single eigenvector state fails transposition dual inequality at n five"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:38:51+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The 12 Nov note records that A A*/tr(A A*) from the top eigenvector fails the transposition-by-transposition dual inequality at n=5. With x=(1,1,0,0,-2)/sqrt(6), (1 5) and (2 5) give 1/2 against 13/24, failing by 1/24.

Why it happened: The route satisfied only the sum against graph weights, while the proposed dual certificate required an inequality for each transposition.

**Why:** An aggregate inequality cannot replace each local inequality required by a certificate.

**How to apply:** Run state_check_n5.py before reviving this route and test each required transposition instead of only the graph-weighted sum.

[[t104_note_what_is_ours_and_what_is_bacher_alon_kozma_2026_11_12]]

Drafted by Codex worker W08 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

