---
name: liveness_stop_order_alarm_was_the_loop_keeper_entries_2026_11_12
description: "Liveness or the wake says 'Stop order unsafe: work_timer.py is not final', or tells you to add waste_sense.py and fleet_inbox_hook.py to the fast list? Both were the checker until 12 Nov: the loop keeper hooks are standalone Stop entries on purpose, and prompt-only child hooks run beside the in-process ones at no wait. Fixed, 6 of 6, old file 0 of 4."
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T02:38:03+02:00
  status: verified
  evidence: "agent_run/liveness/judge.txt (6 of 6; the old file passes 0 of the 4 checks the change moves), child_hooks_on_prompts.txt; ledger row of 12 Nov (l)"
---

From 11 Nov to 12 Nov 2026 every run of `hook_liveness.py`, and so every session's wake text, carried "Stop order unsafe: work_timer.py is not final" and a verdict of two safety failures. One was real (Codex hook trust 44 of 46, which waits on the author's /hooks review). The other was the checker: `loop_keeper.py` and `loop_rewake.py` were wired on 11 Nov as their own Stop entries in settings.json, on the author's 03:13 and 07:07 orders, and the check allowed only `keep_working_after_compact.py` and `keep_working_brain.py` beside the dispatcher. `loop_rewake.py` is an asyncRewake watcher, which can only be a settings-level entry, and Claude Code runs an event's settings-level hooks side by side, so neither one stands in front of the dispatcher's Stop list. A red line that is always red stops being read, which is the same failure the 20 Sep and 17 Oct comments in that check describe.

The same report told agents to test and add `fleet_inbox_hook.py` and `waste_sense.py` to the in-process list. Both are wired on prompt events only, where the dispatcher starts its own-process hooks first and collects them after the in-process ones (`hook_dispatch.PARALLEL_SUBPROC_EVENTS`). Measured on 5,597 profiled prompts since 10 Nov 22:15: the in-process hooks took a median 2,135 ms, the slowest child 644 ms, and the child was the longer of the two on 467 prompts. `waste_sense.py` ran over 5 s as a child 51 times. Moving it in-process saves one interpreter start a prompt and adds its own time and tail to the wait, so it stays a child. `fleet_inbox_hook.py` gives different output on two runs and cannot join in any case.

Since 12 Nov the check accepts the two loop hooks by name (an unknown standalone Stop entry still fails), and a hook wired only on those three events is named as running beside the in-process hooks; a hook wired on any other event is still named as waiting. `judge_liveness.py`: 6 of 6 on four full runs of `main()`; the old file passes none of the four checks the change moves and both guard checks. Backup `hook_liveness.py.bak_stoporder_20261112`.

Left open: `hook_dispatch_extend.py --only waste_sense.py` would still add it, because it passes the exact test. When you wire a new standalone Stop entry, add its name to `_STANDALONE_STOP_OK` in the same change. Related: [[rank_prompt_hooks_by_wait_parallel_children_are_off_the_critical_path_2026_11_11]], [[idle_loop_rewake_async_hook_2026_11_11]], [[a_new_hook_runs_as_its_own_process_until_the_allowlist_names_it_2026_11_11]].

