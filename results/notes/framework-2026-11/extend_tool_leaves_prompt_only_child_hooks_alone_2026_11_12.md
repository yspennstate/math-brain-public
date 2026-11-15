---
name: extend_tool_leaves_prompt_only_child_hooks_alone_2026_11_12
description: "Does hook_dispatch_extend.py with no option move every unlisted hook in-process? Not since 12 Nov: a hook wired only on prompt, stop and start events runs beside the in-process hooks and adds no wait, so the run names it and leaves it (--only NAME still tests it). On the live wiring: fleet_inbox_hook.py, waste_sense.py. 14 of 14, old file 0 of 3."
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T03:01:21+02:00
  status: verified
  evidence: "agent_run/extend_beside/judge.txt (14 of 14; the old file 0 of the 3 cases meant to move); ledger row of 12 Nov (n)"
---

`hook_dispatch_extend.py` moves a wired hook onto the dispatcher's in-process list when it gives the same output in-process as in its own process. That is a gain on a tool event, where every own-process hook is one more process start in the line. On a prompt, a stop and a session start it is not: there the dispatcher starts the own-process hooks first and collects them after the in-process ones (`hook_dispatch.PARALLEL_SUBPROC_EVENTS`), so a hook wired only on those events adds no wait as a child and would add its whole run in-process. Measured 12 Nov on 5,597 profiled prompts: in-process hooks a median 2.1 s, the slowest child 0.6 s; `waste_sense.py` ran over 5 s 51 times as a child.

Until 12 Nov a run of the tool with no option tested and added such hooks with the rest (on the live wiring: `fleet_inbox_hook.py` and `waste_sense.py`). Now a run that names no hook leaves them alone and says so; `--only NAME` still tests one, and `--film` is unchanged. `judge_hde.py`: 14 of 14, the old file 0 of the 3 cases meant to move. Backup `hook_dispatch_extend.py.bak_beside_20261112`.

The test hands the tool a copy of the list (`--allow`), runs it with `--dry-run`, and replaces the step that starts hooks with a recorder, so the question "which hooks would this run touch" is answered without running one. Not covered: the full control (`hook_dispatch_control.py`) writes the list by its own rule. Related: [[rank_prompt_hooks_by_wait_parallel_children_are_off_the_critical_path_2026_11_11]], [[liveness_stop_order_alarm_was_the_loop_keeper_entries_2026_11_12]].

