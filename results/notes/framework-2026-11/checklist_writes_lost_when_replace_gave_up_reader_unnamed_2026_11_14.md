---
name: checklist_writes_lost_when_replace_gave_up_reader_unnamed_2026_11_14
description: "[PROVISIONAL] Checklist 'done' failed with PermissionError 'replace blocked by a reader'? 191 give-ups since 2 Nov, each a lost write; since 14 Nov the give-up line names the holder (pid+cmdline); loop_keeper was the last plain-open reader"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T03:25:30+02:00
  status: provisional
  evidence: ""
---

On 14 Nov 03:06-03:11 the checklist writer's POSIX rename of state.json failed for five minutes straight (six 'replace gave up after ~23 s over 60 tries (dst 32)' in hook.log); two were this agent's own 'done' calls, lost and re-sent. hook.log shows 191 give-ups since 2 Nov (109 on 11 Nov). A give-up raises and the write is gone - nothing queues it. Fix (commit 66682754, an agent): _replace_retrying now logs 'held by: <pid> <app> <cmdline>' from the Windows Restart Manager on a give-up (an empty list means a holder RM cannot see: a scanner or the kernel); loop_keeper.open_entries, run on the Stop of every looping session, used a plain io.open held through json.load of 16.6 MB (1.4 s under load) - it now reads share-delete via shared_read.open_shared and parses after closing. Tests: a held python child is named; replace over a share-delete reader succeeds; open_entries rows identical. Open: the 03:06 burst's holder is unknown (cleared before a 150 s watch); read the next 'held by' line in task_checklist/hook.log. If a CLI write fails with this error, re-send it - it was not saved. Related [[checklist_lock_held_by_os_replace_waiting_on_readers_2026_11_02]] [[compaction_sweep_reparsed_index_per_node_starved_holding_lock_2026_11_14]].
