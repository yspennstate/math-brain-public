---
name: hooks_no_longer_over_online_budget_all_7_flags_were_1nov_d10_78_2026_11_08
description: "No (8 Nov): D10 #78 lint flags no live hook over its online budget in 4-8 Nov samples; all 7 historical flags (spread_recall prompt p95 4.1 s, math_sense, instinct_prime, fleet_inbox, error_graph) are 1 Nov readings, not repeated since; code vs load unsplit"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:45:32+04:00
  status: verified
  evidence: "d10_78_hook_heavy_lint_2026_11_08.py on 13,938 profile dispatches; planted slow/fast PASS; p95 by day; pushed 765257e4e7 blob equal"
---

Question: does any live hook on this worker machine do work that belongs in the dream (D10 #78, the offline/online split lint)?

Not any more, measured 8 Nov 05:4x. d10_78_hook_heavy_lint_2026_11_08.py reads hook_dispatch's sampled per-hook timings (~/.claude/compute/hook_profile.jsonl, 13,938 dispatches, 1 to 8 Nov). It flags a hook whose p95 in one event is over an online budget, given at least 20 samples from at least 2 sessions. The budgets are 100 ms per tool hook (it runs on every tool call), 1 s per prompt or Stop hook (hook_dispatch's own SLOW_HOOK_S) and 5 s at SessionStart. Over the default window, the last 3 days, it flags nothing. Over all history it flags 7 hook-event pairs, and every one is a 1 Nov reading, the profile's first day:

- spread_recall at the prompt: p95 4.1 s on 1 Nov, then 0.79 s on 4 Nov and 0.19 s on 7 Nov.
- math_sense at the prompt: 1.67 s, then 52 ms and 17 ms.
- instinct_prime before each tool: 162 ms, then about 51-56 ms.
- fleet_inbox_hook at the prompt: 1.47 s, then 0.67-0.76 s.
- error_graph before and after each tool: 277 and 358 ms. It has been switched off since 1 Nov (its enabled_if file is absent) and has no samples after that.

Between those days other sessions changed the hooks, the parallel spawning-hook dispatch and the spread server among them ([[hook_dispatch_runs_spawning_hooks_in_parallel_2026_11_01]], [[resident_hook_dispatcher_warm_hooks_54pct_of_fresh_35_55ms_a_call_2026_11_06]]). The machine's load also differed, and the profile keeps no load column. So I cannot split how much of the drop is code and how much is a quieter box. What does hold is that no hook has been over budget in 4-8 Nov samples, at whatever load those days had. So the lint was built and nothing was changed.

The check could fail, and it was tested both ways. A planted 400 ms tool hook from 3 sessions is flagged, and a planted 3 ms one is not (--plant, exit 0 only when both hold). The lint also marks a hook that is now OFF, or that was edited after its last sample, so old numbers are not blamed on fixed code. Its heavy-pattern scan of each source file (memory-folder listing, tree walk, git/gh, network, subprocess) is a hint, not a cause. spread_recall matches "lists memory folder", yet that listdir costs 18 ms, so it cannot be the 600 ms tail.

One to watch: fleet_inbox_hook's p95 is still 0.75 s against a 7.6 ms median. About one prompt in twenty pays for its inbox refresh. That is under budget, but it is the nearest hook to the line.

The profile flag had lapsed at 7 Nov 09:03. I re-armed it at 05:43 on 8 Nov (touch ~/.claude/compute/hook_profile.on, 3 h), the same way 5009ea7f did on 1 Nov, so the next run has fresh rows. How to apply: run the lint before any claim that a hook is slow, and after a hook edit, with the flag re-armed.

