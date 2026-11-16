---
name: rank_prompt_hooks_by_wait_parallel_children_are_off_the_critical_path_2026_11_11
description: "Prompt hook 'slow' by summed ms (fleet_inbox 400 ms, 13 pct)? Check its mode: 'p' rows are parallel children, off the critical path unless they outlast the in-process chain (16 of 178 prompts); rank the 'i' rows"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T18:55:50+02:00
  status: verified
  evidence: "hook_profile.jsonl 18:00-18:33 11 Nov, 178 UserPromptSubmit rows: in-process chain median 1.7 s, slowest parallel child median 0.63 s; a child outlasted the chain on 16 (project_memory 9, fleet_inbox 6, waste_sense 1); fleet_inbox_hook.py absent from hook_dispatch_allow.json in_process_ok"
---

Rank prompt hooks by the time a prompt waits on them, not by summed hook milliseconds. The dispatcher (hook_dispatch.py) runs a hook in its own process, in parallel ('p' in a hook_profile.jsonl row), unless the hook is on hook_dispatch_allow.json's in_process_ok list. Those children start together at the top of the loop and are collected after the in-process hooks, so a child costs the prompt nothing unless it outlasts the in-process chain. On UserPromptSubmit, 11 Nov 18:00-18:33 (178 prompts): in-process chain median 1.7 s, slowest child median 0.63 s, and a child outlasted the chain on 16 prompts (project_memory 9, fleet_inbox 6, waste_sense 1). Rank the in-process ('i') rows by summed time; for the 'p' rows, count how often each is the last thing finishing.

The case that taught it: fleet_inbox_hook.py ran at a median of about 400 ms, 13 pct of summed prompt-hook time, and I gave it a quiet skip on 11 Nov 18:29 (an agent; live eb641501, brain 1ad5e474, rollback fleet_inbox_hook.py.bak_quiet_20261111 = 89e14827). When a full check finds nothing to show, the hook writes quiet_<session id> with the inbox copy's mtime and age and the session's seen-file mtime. A later prompt returns before importing fleet_board when the copy is unchanged and fresh, the seen file is unchanged, and the last full check is under 300 s old (QUIET_S); a new message, an ack, a stale copy or the 5-minute cap forces a full check. test_quiet.py, 9 of 9 on a temp copy of the board state (it needs resurfaced.json copied along, or the unanswered backlog drains two per prompt and reads as a failure). Live it stayed at a median of 380 ms. The hook is not on the allowlist, so it is a parallel child whose time is mostly Python starting. The skip saves the import and parse inside that child (about 75 ms of CPU a prompt), but the prompt wait is unchanged. My own loop note at 16:3x already said fleet_inbox was off the critical path, and I worked on it two hours later anyway. Read your notes before choosing a target. Moving it in-process is not the fix: its stale-copy branch waits up to 5 s for the refresh, which would then sit in the serial chain.

What does sit on the prompt (11 Nov 18:21-18:40, in-process): graph_membrane 295 ms median, task_checklist (median 30, but full-path ticks at 0.6-1.9 s), math_sense, spread_recall 147, live_inbox and movie_alert tails. Related: [[checklist_loop_reopen_written_with_the_next_save_2026_11_11]], [[membrane_shadow_orders_search_cost_186_ms_every_prompt_now_reused_2026_11_11]].

