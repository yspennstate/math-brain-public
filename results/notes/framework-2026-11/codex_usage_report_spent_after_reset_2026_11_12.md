---
name: codex_usage_report_spent_after_reset_2026_11_12
description: "Codex accounts reported exhausted after subscription usage returned stale usage meter"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:14:40+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 22 Oct 23:14 [agent], the author corrected a report that the 2 subscribed Codex accounts were spent: usage had returned. Later prompts repeat that usage is back. No idle-duration or missed-picture count is supplied.

Why it happened: The correction is consistent with reusing an earlier usage observation after a reset. It does not prove whether the meter, its cache or the agent report was stale.

**Why:** Usage exhaustion is a timestamped observation, not permanent account state.

**How to apply:** Read a current meter and timestamp it before reporting exhaustion; the later account-6 ban still applies even if credits remain.

Sources: [[owner_prompt_2026_10_22_23_14_agent]]

Drafted by Codex worker W13 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

