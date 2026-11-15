---
name: checklist_stop_bursts_written_once_by_a_flush_child_2026_11_11
description: "Checklist Stop hook slow (16 MB state load+save per Stop)? Since 11 Nov a Stop within 60 s of the session's last full Stop leaves its words in .stop_pending and one hidden child applies them in one save: 557 -> 53 ms median, no words lost"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T09:04:53+02:00
  status: verified
  evidence: "scratchpad tc/coal_speed.py + coal_test.py; selftest 0 failed; ledger gaps 8-11 Nov 49 pct under 60 s"
---

Since 11 Nov 2026 09:02 local, task_checklist_hook.py writes a burst of Stops once. Before, every Stop of a session with an open entry took the checklist lock, loaded the whole state.json (16 MB, 7,428 entries; about 85 ms) and saved it back (about 55 ms) to change that entry's last words, and waited seconds whenever another holder had the lock. In the ledger of 8-11 Nov (11,565 repeat Stops on one entry), 44 pct came under 30 s after the previous one and 49 pct under 60 s: a Stop hook sends the agent back to work and it stops again.

How it works now: a Stop within 60 s of the session's last full Stop, with no closing line ("This was your HH:MM ask") and no named ask, writes its words to `task_checklist/.stop_pending/<session12>.<ns>.pend` and returns. A hidden child (`task_checklist_hook.py --flush-stops`, CREATE_NO_WINDOW, one at a time by `.flush.lock`) waits out the window and applies every pending Stop of every session in one locked load and save: a ledger "stop" row for each, the newest words on each entry. A full Stop writes `<session12>.mark` inside the lock and deletes that session's older pending files; the flush drops pending words older than the mark, so it never puts old words over new ones. A prompt removes the mark, so the Stop that answers a new ask is always whole. Marks idle a day are pruned by the child.

Measured on the production path (scratch store copied from live, store registered as live, ten Stops 1 s apart, box loaded): 557 -> 53 ms median per Stop; the first full Stop costs what it did. Nothing lost: 9 pending Stops applied in one save, ledger 10 rows in order, entry ends on the last words. The hook's selftest: 0 failed (coalescing is off off the live store unless TASK_CHECKLIST_STOP_COALESCE is set, so the selftest sees every Stop whole). Live at 09:03: marks and pending files appeared for five sessions and the child ran.

What changes for a reader: the list may show an agent's last words up to about a minute late. Turn it off with TASK_CHECKLIST_STOP_COALESCE=0; another number is the window in seconds. Rollback: task_checklist_hook.py.bak_stopcoalesce_20261111. If pending files pile up without a `stop flush:` line in task_checklist/hook.log, the child is not starting.

How to apply elsewhere: when a hook rewrites a large shared file for a small change and the same caller repeats within seconds, measure the repeat gaps first; if most fall inside a short window, leave the change in a per-caller file and let one child fold them in. Related: [[hook_budget_agent_loop]], [[owner_task_checklist_every_agent_registers_his_asks_2026_09_18]].

