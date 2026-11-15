---
name: loop_dies_after_compact_only_without_a_live_cron_2026_11_11
description: "[VERIFIED] Agent stops after a compaction / loop stuck? 755 compactions in 36 h: with a live cron 719/720 resumed; stalls = manual /compact with nothing armed (no turn, no Stop) or a ScheduleWakeup not re-armed. loop_keeper.py (Stop+SessionStart) blocks once when a loop is left unarmed."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T03:51:52+02:00
  status: provisional
  evidence: ""
---

The author, 11 Nov 03:13: a report that loops stalled after a compaction.

Measured (every Claude transcript touched in 36 h, 755 compact_boundary records): with a recurring CronCreate alive, the session took its next turn after the compaction 719 of 720 times (a cron fires when the REPL is idle and survives compaction). The stalls: (1) a MANUAL /compact starts no turn and fires no Stop, so keep_working_after_compact.py never runs; with no cron or wakeup armed the session sits until the author types (an agent 02:50-03:13, its timed loop had ended 02:36; an agent from 01:29, 110 min). (2) A self-paced /loop lives only while each turn re-arms ScheduleWakeup; a turn ending on a recap kills it. (3) Crons and wakeups live in the process, so a restart or resume loses them while the transcript still shows them.

Fix: ~/.claude/dreaming/loop_keeper.py (mirror 12_cognitive_architecture/dreaming/loop_keeper.py, commit f8c23f45), wired in settings.json Stop (beside keep_working_after_compact, not through hook_dispatch so the block decision passes) and SessionStart (all sources). Stop blocks ONCE per lapse when the session ran a loop and nothing is armed: a wakeup lapsed, or a cron was deleted/expired/lost while checklist entries under its id stay open. Silent when a cron is alive, a wakeup is pending, or the loop was stopped with stop:true. SessionStart startup/resume records the process start; compact prints whether the loop survived. Tested on a 99 MB transcript (0.4-0.8 s) plus synthetic lapsed / re-armed / stopped / restart cases. Scar caught while testing: a cron id quoted inside a grep's output read as a live cron; match only CronCreate's unescaped toolUseResult {id, humanSchedule}.

How to apply: on a long ask keep a recurring CronCreate (not only ScheduleWakeup), so any compaction is followed by a fire. When a timed loop ends with the author's work still open, arm a slower heartbeat or close the entries and say why. No hook can wake an idle session; only a fire or the author's prompt can. Related: [[after_a_compaction_agents_stopped_on_a_recap_stop_hook_sends_them_back_2026_10_16]].

