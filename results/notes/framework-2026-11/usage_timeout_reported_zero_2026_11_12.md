---
name: usage_timeout_reported_zero_2026_11_12
description: "Claude account usage probe timeout displayed as zero percent"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:40:17+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 7 Oct 02:43 the pasted diagnosis says every account probe timed out at 180 seconds on the loaded laptop, so Claude readings failed and displayed 0%. A 02:02 table showed 19 running claude2 workers while reporting 0% used; the actual allowance is not established by those failed probes.

Why it happened: The reporting path collapsed failed or unavailable readings into a numeric zero.

**Why:** Zero used is a valid reading and cannot also mean no reading.

**How to apply:** Keep value, status and read time separate, retain the last known reading as stale, and refuse new account allocations while its allowance is unknown.

Sources: [[owner_prompt_2026_10_07_02_43_agent]], [[owner_prompt_2026_10_07_02_02_agent]], [[owner_prompt_2026_10_07_03_32_agent]]

Drafted by Codex worker W18 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

