---
name: headless_runner_reused_task_sessions_2026_11_12
description: "Headless Claude or Codex runner resumes an old session for a different task"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:28:02+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The owner accepted a fix for headless workers: one task per session. The quoted status said the runner still resumed sessions across tasks. This is one identified runner behavior; the number of contaminated sessions is not stated.

Why it happened: Runner session reuse crossed task boundaries instead of allocating a fresh session per task. No further implementation detail is given.

**Why:** Task isolation is broken when unrelated work inherits the previous task session.

**How to apply:** Start a new headless session for each task in both runners and preserve previous results before moving on.

Source: 2026-10-09 17:40 [agent] (input line 280)

[[owner_prompts_w16_2026_11_12]]

Later verified source says this was fixed that night at 17:58, with 33/33 controls passing versus 21/33 with the decision disabled. Resume within the same task remains allowed; this is a recurrence warning, not an assertion that the fix is absent now.

[[headless_workers_run_one_task_per_session_2026_10_09]]

Drafted by Codex worker W16 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

