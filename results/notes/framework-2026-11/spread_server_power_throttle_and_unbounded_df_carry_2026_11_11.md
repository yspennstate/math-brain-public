---
name: spread_server_power_throttle_and_unbounded_df_carry_2026_11_11
description: "Prompts 13-17 s in spread_recall, or the recall server slow while up? Two fixes 11 Nov: the server was power-throttled (BelowNormal line never applied, untyped pseudo-handle; now typed EcoQoS opt-out), and a df carry on a full rebuild read every document under the lock (93 s at 02:43); capped at 1000 changed docs"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T02:57:48+02:00
  status: verified
  evidence: "server.log 02:46:14 / 02:56:18 'EcoQoS opt-out ok'; faults.jsonl 02:44:44 _df_carry 93192 ms; scratchpad cap_test.py 10/10"
---

Question: why do prompts on the laptop sometimes take 13-17 s in spread_recall, and why does the resident spread_server answer slowly even when it is up?

Two causes, both fixed on 11 Nov 2026 (an agent).

1. Power throttling. The server ran in the state Windows chooses for a windowless process (EcoQoS "system decides"), and on the loaded box that meant throttled: over 1.5 h its calls used a median of 109 ms CPU for 387 ms of wall time (p90 1.9 s). The BelowNormal line in main() never took effect, because SetPriorityClass got GetCurrentProcess() without a HANDLE restype, which truncates the -1 pseudo-handle. The server had always run at Normal, and it stays at Normal. main() now calls _unthrottle(), a typed SetProcessInformation(ProcessPowerThrottling, ControlMask 1, StateMask 0), the same opt-out hook_dispatch gives each hook. The server logs "EcoQoS opt-out ok". The new pid read "explicitly opted out" on the probe. SPREAD_SERVER_UNTHROTTLE=0 turns it off.

2. An unbounded carry under the lock. When the BM25 sidecar's generation changes, df_view carries the df memo over by reading the terms of every changed document, one row at a time, while holding DF_LOCK. A full rebuild renumbers positions, so every document looks changed. At 02:43 one carry ran 93 s (93,214 page faults), and the 13 prompts that arrived during it went cold at 13-17 s each, one of them starting a second server. Reading all 61,870 documents costs about 14 s even with a warm disk (0.22 ms each). _df_carry now counts the changed positions first, which is a dict comparison costing about 70 ms. Above SPREAD_SERVER_DF_CARRY_MAX (default 1000) it raises, and df_view's existing error path starts an empty memo, which is what happened before carries existed. An ordinary rebuild changes about 120 documents and still carries. Tested on the real sidecar (scratchpad cap_test.py, 10/10): 0, 10 and 450 changed positions carry in 70-320 ms and drop only the changed documents' words; 1,200 raises in 65 ms without reading any terms.

Backups: spread_server.py.bak_ecoqos_20261111 (before both changes) and .bak_dfcap_20261111 (before the cap). Mirror: 12_cognitive_architecture/dreaming/spread_server.py.

How to see it again: grep "_df_carry" in dreaming/spread_server/faults.jsonl. Rows over 5 s mean a carry ran long. A "df carry skipped" line in server.log means the cap fired. Any change to a watched code file makes the running server decline and exit, and the next prompt starts a new one, so an install costs one warm start of about 8-10 s.

What would change this: calls.jsonl wall time per call not falling toward its CPU time after 02:46, or cold spread_recall rows at 13 s or more on a rebuild with no "skipped" line.

Related: [[ctypes_pseudo_handle_made_the_ecoqos_opt_out_a_silent_no_op_2026_11_11]] [[prompt_wait_is_the_in_process_hook_sum_not_the_spawned_hooks_2026_11_10]] [[hidden_scheduled_task_slow_start_priority_4_and_early_opt_out_2026_11_11]]


Longer window (11 Nov 02:47-03:12, 83 calls, after the opt-out): wall median 156 ms (387 before), p90 484 (1923), max 1344, CPU median 109 (109): the CPU work is unchanged and the wall time fell, which is the throttling signature. No call over 1.5 s (65 in the 1.5 h before).
