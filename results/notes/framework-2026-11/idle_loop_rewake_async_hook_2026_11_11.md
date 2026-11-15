---
name: idle_loop_rewake_async_hook_2026_11_11
description: "Loop stuck after a compaction or a dead tick, session idle? loop_rewake.py (asyncRewake hook on Stop+SessionStart) wakes it: exit 2 from a background hook starts a turn in an idle session. 32 controls, live wake 07:20."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T07:23:21+02:00
  status: verified
  evidence: "test_loop_rewake.py 32 controls 0 failed; loop_rewake_fires.jsonl forced wake 2026-11-11T07:20:22 on an agent"
  lesson: true
---

The author, 11 Nov 07:07 (second ask the same day, after loop_keeper.py landed at 03:51): a report that loops stalled after a compaction.

What loop_keeper.py could not do: it speaks only at a hook event (it blocks a Stop, prints one line after a compaction). Three stalls have no event: a manual /compact with no cron and no wakeup armed (no turn, no Stop); a tick that dies before its end (API error, limit, interrupt) and so never re-arms ScheduleWakeup; a wakeup recorded as pending that does not fire. Its memory said "no hook can wake an idle session". That is wrong on Claude Code 2.1.322: a command hook with "asyncRewake": true runs in the background, and when it exits with code 2 its stderr reaches the model as a new turn ("Stop hook blocking error ..."), even when the session is idle.

Fix: ~/.claude/dreaming/loop_rewake.py, wired in ~/.claude/settings.json on SessionStart and Stop beside loop_keeper, {"asyncRewake": true, "timeout": 6300}. One watcher a session (file <sid>.alive, a later start leaves at once). Every 20 s it reads the transcript's mtime; once the session is quiet 180 s after a finished turn or a compaction (1500 s after a record that looks mid-turn) it reads the loop state with loop_keeper's scanner and wakes the model when: the last wakeup's time passed 300 s ago with nothing armed and no cron (up to 3 wakes a lapse, later ones after 10 and 30 more quiet minutes); a loop ran, none is armed and checklist entries stay open (one wake); a cron is alive but the session was quiet 45 min (one wake). Never wakes a session with no loop in 24 h, a loop stopped with stop:true, or a wakeup or cron still to come. State ~/.claude/compact_hooks/loop_rewake/<sid>.json, wakes logged in ~/.claude/brain_graph/compactions/loop_rewake_fires.jsonl.

Measured: 32 controls on synthetic transcripts, 0 failed (test_loop_rewake.py: five wake cases, ten silent cases, the budget, record shapes, one watcher a session, the forced wake). Live on an agent: a forced wake set for 75 s after a Stop was logged at 07:20:22 and started a turn in an idle session. At 07:22, of 33 sessions with a loop state 8 had a cron, 1 a pending wakeup, none was stuck. Not yet measured: a real lapse woken in another session; count the fires log after a day and judge wakes per session (a high count means the watcher, not the sessions, is at fault).

Limits: a session already idle when the hook landed has no watcher until its next Stop or compaction. A watcher lives at most 100 minutes after the last Stop. Crons and wakeups still die with the process; after a restart the "none" rule wakes once if entries are open. Test the wake path on one session: write a number of seconds into ~/.claude/compact_hooks/loop_rewake/<sid>.force, and to limit the watcher to listed sessions create ONLY_SESSIONS.txt there. Undo the wiring: restore ~/.claude/settings.json.before_loop_rewake_20261111.

How to apply: for a hook that must act later or on an idle session, use asyncRewake and exit 2; keep a budget on it. Related: [[loop_dies_after_compact_only_without_a_live_cron_2026_11_11]], [[after_a_compaction_agents_stopped_on_a_recap_stop_hook_sends_them_back_2026_10_16]].

