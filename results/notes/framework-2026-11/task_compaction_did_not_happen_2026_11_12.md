---
name: task_compaction_did_not_happen_2026_11_12
description: "Agent finishes a task without compacting or preserving a linked compaction node"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:31:59+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: At 22:24 on 9 October the author asked why self-compaction had not happened. At 23:10 the author asked for a hook at task completion, following repeated requests that each compaction become its own linked node. At least one missed compaction is evidenced; the number of lost records is unknown.

Why it happened: Compaction was not reliably triggered at the requested task boundary. The input does not establish the implementation cause.

**Why:** A promised compaction is not evidence that its saved node exists.

**How to apply:** At task boundaries, verify the compaction record and edges, perform the context change, and resume the remaining work.

Source: 2026-10-09 23:10 [agent] (input line 212); 2026-10-09 22:24 [agent] (input line 217); 2026-10-09 18:55 [agent] (input line 264); 2026-10-09 17:15 [agent] (input line 289)

[[owner_prompts_w16_2026_11_12]]

Drafted by Codex worker W16 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

