---
name: math_cards_stored_without_edges_2026_11_12
description: "Math store cards not connected by edges graph walk reaches only one fifth"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:15:33+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 28 Oct 05:21 and 05:10, the pasted finding said only 16,234 of 86,605 math-store nodes touched an edge. The remainder is 70,371, consistent with the prompt's about 70,000. This is an input-reported snapshot, not a fresh graph count.

Why it happened: The reported harvested claims were stored as nodes without enough depends_on or cites links. The input proposes those relations; it does not prove which individual edges are valid.

**Why:** Storing a card does not make it reachable by walking the graph.

**How to apply:** Check graph membership after ingestion and add only supported meaningful links; do not fabricate edges merely to raise connectivity.

Sources: [[owner_prompt_2026_10_28_05_21_agent]], [[owner_prompt_2026_10_28_05_10_agent]]

Drafted by Codex worker W13 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

