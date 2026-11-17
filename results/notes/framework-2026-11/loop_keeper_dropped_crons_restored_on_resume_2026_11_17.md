---
name: loop_keeper_dropped_crons_restored_on_resume_2026_11_17
description: "[PROVISIONAL] loop-keeper says 'none armed' after a restart while CronList shows the cron? Claude Code restores session crons on resume; keeper assumed they die. Fixed 17 Nov: a CronList result after proc_start marks the id alive"
metadata:
  type: feedback
  created: 2026-11-17
  created_at: 2026-11-17T04:05:06+02:00
  status: provisional
  evidence: ""
---

17 Nov 03:5x. After a machine restart a session was resumed; CronList showed its 3-minute cron (created 14 Nov) and it kept firing, yet loop_keeper.py blocked every Stop with 'none is armed now'. armed() kept only crons created after proc_start, on the docstring's assumption that crons die with the process. They are restored on resume. Fix in .claude/dreaming/loop_keeper.py: LIST_RE reads a CronList tool_result whose content starts with the job id (a grep or log quoting the line does not match, negative control passed) and records st['listed'][id]; armed() counts a cron as live if created after proc_start OR listed after it. Old code on this transcript: none; new: the cron alive; live Stop run silent. Still true: a cron NOT restored and never listed is still flagged, which is the alarm we want. A listing scanned before the fix lands is not re-read, so the first compaction after landing may still alarm once; the next CronList clears it. Related: [[liveness_stop_order_alarm_was_the_loop_keeper_entries_2026_11_12]].
