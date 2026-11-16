---
name: work_session_clock_restarts_on_every_cron_loop_refire_2026_11_16
description: "[PROVISIONAL] The work-session hook restarts its 10h clock each time a /loop cron re-fires the original prompt, so it keeps demanding work hours past the author's real end time (16 Nov: ask 03:41+10h=13:41, hook said until 23:39). Close at the author's clock, not the hook's."
metadata:
  type: feedback
  created: 2026-11-16
  created_at: 2026-11-16T13:48:01+02:00
  status: provisional
  evidence: ""
---

Seen 16 Nov 2026. A 10-hour loop was started at 03:41, to end at 13:41. The cron job re-fired the same /loop text every 3 minutes; each re-fire reached UserPromptSubmit as a new prompt and work_session reset its clock (until 23:29, 23:30, 23:32 ... 23:39). After the loop closed at 13:41, the Stop hook kept blocking on a clock the author never set. How to apply: compute the end from his first prompt's time plus his stated duration; cancel both crons, ScheduleWakeup stop, log, checklist done, and say in one line why the hook's clock does not apply. Fix belongs in work_session: ignore a prompt whose text equals the running loop's prompt.
