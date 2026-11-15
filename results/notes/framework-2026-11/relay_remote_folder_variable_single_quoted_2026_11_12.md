---
name: relay_remote_folder_variable_single_quoted_2026_11_12
description: "score_relay2 SSH folder variable single quotes no score empty run"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T14:45:44+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 2026-11-12 the first score_relay2.sh invocation read nothing and printed no score. The command passed the folder name inside single quotes to the Mac. After the folder travelled in the command correctly, the scorer reported 87/100 opened, 0 wrong and agreement with the report.

Why it happened: Single quoting kept the folder variable literal across the local-to-remote shell boundary, so the scorer did not read the intended run.

**Why:** An empty scorer display was a quoting failure, not a scored run.

**How to apply:** Verify the exact remote run-folder argument and require a nonempty score tied to the expected manifest before reporting success.

[[relay_hunt_rl2_warm_87_of_100_first_hour_68_2026_11_12]]

Drafted by Codex worker W02 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

