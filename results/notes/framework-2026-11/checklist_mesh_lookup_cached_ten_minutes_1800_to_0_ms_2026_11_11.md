---
name: checklist_mesh_lookup_cached_ten_minutes_1800_to_0_ms_2026_11_11
description: "Checklist hook 1.7-2.2 s on prompts and Stops while other agents write? The mesh lookup (mesh_task_for, a full scan of the 605 MB rollback-journal agent_mesh.sqlite3) waited on writers; since 11 Nov 19:27 it is cached 10 min per session (mesh_lookup_cache.json), 0.25 s timeout, stale answer on a lock, TASK_CHECKLIST_MESH_CACHE=0 off"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T19:31:24+02:00
  status: verified
  evidence: "trace rows 19:08-19:25 mt 1696-1808 ms; test_meshcache.py ALL PASS 28/28 sessions; --selftest 0 failed; live md5 0df22122776d; brain c9cbbb57"
---

The checklist hook (`task_checklist_hook.py`) asked the agent mesh which agent and task a session belongs to (`mesh_task_for`) on every prompt and every Stop of every session, before it branched. The mesh database (`~/.agents/coordination/agent_mesh.sqlite3`, 605 MB, 11,259 agent rows) runs in rollback-journal mode, and the lookup is a `session_key like '%sid%'` full scan: about 10 ms when nobody writes, but while another agent writes the read waits out sqlite's timeout. On 11 Nov 19:08-19:25 the hook's own trace showed rows of 1.7-2.2 s with `mt` (the mesh lookup) at 1,696-1,808 ms and everything else (load, save, lock, view) under 100 ms, on the fast path too.

Since 11 Nov 19:26:55 the answer is cached per (session prefix, agent hint) in `task_checklist/mesh_lookup_cache.json` for 10 minutes, and the mesh read has a 0.25 s timeout. A locked or failing read returns the last cached answer (or none, as before). Entries older than a day are dropped when the file is rewritten; `TASK_CHECKLIST_MESH_CACHE=0` turns the cache off. A cached call costs 0.08 ms.

Tested on a temp store against the uncached function: same answer on 28 of 28 real session ids (25 found in the mesh), no mesh read within the TTL, expired entries read again, the last answer kept when the read is locked, none when locked with no cache, a broken cache file read past, off switch reads every time and writes nothing; `--selftest` 0 failed; trace test PASS. Brain mirror c9cbbb57.

What would change it: a session that registers in the mesh after its first prompt shows no mesh agent on its checklist rows for up to 10 minutes; if that matters, shorten the TTL for a (None, None) answer.

Related: [[checklist_loop_reopen_written_with_the_next_save_2026_11_11]], [[checklist_stop_bursts_written_once_by_a_flush_child_2026_11_11]], [[rank_prompt_hooks_by_wait_parallel_children_are_off_the_critical_path_2026_11_11]].

